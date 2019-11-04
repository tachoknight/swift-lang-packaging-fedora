#!/usr/bin/python3

import feedparser
import re
import datetime
import requests
from bs4 import BeautifulSoup

def left(s, amount):
    return s[:amount]

def right(s, amount):
    return s[-amount:]

def mid(s, offset, amount):
    return s[offset:offset+amount]

def getDate(s):
    # Because we know the format of the string, this is safe to do
    # (e.g. swift-4.2-DEVELOPMENT-SNAPSHOT-2018-07-17-a)
    return datetime.datetime.strptime(mid(s, 31, len(s)-31-2), '%Y-%m-%d').date()

def getGitTag(post):
    f = requests.get(post.link)
    soup = BeautifulSoup(f.content, 'html.parser')
    elems = soup.code
    return [elem.string for elem in elems][0]

def getSpecFileContents():
    with open('swift-lang.spec', 'r') as f:
         return f.read()

def changeData(f, textToFind, textToReplace):
    p = re.compile(textToFind)
    s = p.search(f)
    t = s.group() # This is the line from the file we want to replace
    # And replace it
    return f.replace(t, textToReplace)

def changePackageNumber(f):
    p = re.compile('Release: .*')
    s = p.search(f)
    t = s.group()
    
    # Now we need to get the package number
    p2 = re.compile('[0-9].[0-9].')
    s2 = p2.search(t)
    t2 = s2.group()

    # Now we have our number, so we want to increment that
    newPN = int(t2.split('.')[1]) + 1

    # And we need to return the fixed line, as well as the new package number so we can use it for
    # the changelog
    return f.replace(t, 'Release:        0.' + str(newPN) + '.%{swiftgitdate}git%{swiftgithash}%{?dist}'), newPN

def process(post, postDate):
    print("Going to work with " + post.title + " from " + post.link)
    gitHash = getGitTag(post)
    print("The git hash is " + gitHash)
    # We need the spec file contents 
    spec = getSpecFileContents()
    #
    # Now let's fiddle with the file
    #

    # First change the file date
    newTitle = post.title
    newTitle = newTitle.replace('swift-', '')
    spec = changeData(spec, 'swifttag .*', 'swifttag ' + newTitle) 
    # Now the tag
    spec = changeData(spec, 'swiftgithash .*', 'swiftgithash ' + gitHash)
    # Now the date
    #newDate = str(postDate.year) + str(postDate.month) + str(postDate.day)
    newDate = postDate.strftime('%Y%m%d')
    spec = changeData(spec, 'swiftgitdate .*', 'swiftgitdate ' + newDate)
    # We have to handle the package number specially as we need to 
    # increment it and return it so we have it for the changelog
    spec, pn = changePackageNumber(spec)
    # Now we need to write out the changelog
    cl = '%changelog\n* ' + datetime.datetime.now().strftime('%a %b %d %Y') + ' Ron Olson <tachoknight@gmail.com> 5.1-0.' + str(pn) + '.' + newDate + 'git' + gitHash + '\n' + '- ' + 'Updated to ' + post.title
    spec = spec.replace('%changelog', cl)

    nf = open('swift-lang.spec', 'w')
    nf.write(spec)
    nf.close()

    # And write out our last-release file
    nlrf = open('last-release.txt', 'w')
    nlrf.write(post.title)
    nlrf.close()


lastBuild=''
with open('last-release.txt', 'r') as lastbuildfile:
    lastBuild=lastbuildfile.read().replace('\n', '')

lastDate = getDate(lastBuild)

d = feedparser.parse("https://github.com/apple/swift/releases.atom")

# We're gonna start from the top as that's the latest one

print("Gonna go through them...")
for post in d.entries:    
    print(post.title)
    if left(post.title, 9) == 'swift-5.1':        
        postDate = getDate(post.title)
        # Okay, is this date newer than the last time we
        # processed anything?
        if postDate > lastDate:
            print("yep, got to do it!")
            process(post, postDate)
            break

