#!/usr/local/bin/python3

import git
import os
import feedparser
import re
import datetime
import requests
from bs4 import BeautifulSoup

# The version of Swift we're checking for
CURRENT_VERSION = "swift-5.3"

def left(s, amount):
    return s[:amount]

def right(s, amount):
    return s[-amount:]

def mid(s, offset, amount):
    return s[offset:offset+amount]

def getDate(s):
    # Because we know the format of the string, this is safe to do
    # (e.g. swift-4.2-DEVELOPMENT-SNAPSHOT-2018-07-17-a)
    return datetime.datetime.strptime(mid(s.strip(), 31, len(s.strip())-31-2), '%Y-%m-%d').date()


def findLastDate():
    lastBuild=''
    with open('last-release.txt', 'r') as lastbuildfile:
        lastBuild=lastbuildfile.read().replace('\n', '')

    print('Last build was ', lastBuild)
    lastDate = getDate(lastBuild)
    return lastDate

def getSpecFileContents():
    with open('swift-lang.spec', 'r') as f:
         return f.read()

def changeData(f, textToFind, textToReplace):
    p = re.compile(textToFind)
    s = p.search(f)
    t = s.group() # This is the line from the file we want to replace
    # And replace it
    return f.replace(t, textToReplace)

def process(post, postDate):
    print("Going to work with " + post.title + " from " + post.link)
   
    # We need the spec file contents 
    spec = getSpecFileContents()

    #
    # Now let's fiddle with the file
    #

    # We're going to change the swifttag global to the currrent build
    newTitle = post.title
    newTitle = newTitle.replace('swift-', '')
    spec = changeData(spec, 'swifttag .*', 'swifttag ' + newTitle) 
    
    nf = open('swift-lang.spec', 'w')
    nf.write(spec)
    nf.close()

    # And write out our last-release file
    nlrf = open('last-release.txt', 'w')
    nlrf.write(post.title)
    nlrf.close()

def commitChanges(versionName):
    print("updating git with changes")
    currentDirectory = os.getcwd()
    repo = git.Repo(currentDirectory)
    assert not repo.bare

    print (repo.git.status())

    repo.index.add('swift-lang.spec')
    repo.index.add('last-release.txt')

    commitMsg = 'Updated to ' + versionName

    repo.index.commit(commitMsg)
    

if __name__ == "__main__": 
    print("okay, we're starting!")
    lastDate = findLastDate()
    print('last date was', lastDate)
    d = feedparser.parse("https://github.com/apple/swift/releases.atom")

    # We're gonna start from the top as that's the latest one

    print("Ok, Gonna go through them...")
    for post in d.entries:    
        print(post.title)
        if left(post.title, 9) == CURRENT_VERSION:        
            postDate = getDate(post.title)
            # Okay, is this date newer than the last time we
            # processed anything?
            if postDate > lastDate:
                print("yep, got to do it!")
                process(post, postDate)
                # And commit it back
                commitChanges(post.title)
                break

