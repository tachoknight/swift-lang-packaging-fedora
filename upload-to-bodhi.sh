#!/bin/bash
#
# This script handles the commit and submitting of builds
# for production. It assumes the SRPM is ready to go.
# Run from the official directory that is linked to 
# the Fedora repos!
# NOTE! PASS THE COMMIT MESSAGE AS THE FIRST PARAMETER!
# AND USE QUOTES!

function check_authenticated {
  output=$(koji hello)
  
  if echo "$output" | grep -q "Authenticated"; then
    return 0  # True, if "Authenticated" is found
  else
    return 1  # False, if "Authenticated" is not found
  fi
}


# Simple sanity check, we want to start with the
# Rawhide branch, and we don't want to just assume
# that's what's currently selected and we don't
# want to just set it ourselves in case there was a 
# reason for it not being set already
BRANCH="$(git rev-parse --abbrev-ref HEAD)"
if [[ "$BRANCH" != "rawhide" ]]; then
  echo 'NOT ON RAWHIDE! Set that before running this script!';
  exit 1;
fi


# Check if authenticated with Koji
if ! check_authenticated; then
    echo HEY! LOG INTO KOJI! | figlet -c -f future | lolcat
    exit 1
fi

echo WE ARE LOGGED INTO KOJI! | figlet -c -f future | lolcat

START_TS=`date`

export MYDIR=$PWD

# Our current version of Fedora
export FEDORA_VERSION=`rpm -E %fedora`

# Did you remember to actually, you know, build the SRPM file?
export SRPM_FILE=`find $HOME/rpmbuild/SRPMS -name swift-lang\*`
if [ ! -f $SRPM_FILE ]; then
    echo "HEY BUILD THE SRPM FILE!"
    exit 1
fi

echo Working with $SRPM_FILE | figlet -c -f pagga | lolcat

#
# Here we go!
#
echo Importing SRPM into Rawhide | lolcat
# This imports the SRPM file and uploads the artifacts to the server
fedpkg import $SRPM_FILE

# And commit the repo using the commit message from the changelog
fedpkg commit -c -p
fedpkg build --nowait

echo Now doing the other versions | lolcat

# Now do the rest
echo f$FEDORA_VERSION | figlet -c -f mini | lolcat
fedpkg switch-branch f$FEDORA_VERSION
git merge rawhide
git push
fedpkg build --nowait
# Now the previous version of Fedora
let "FEDORA_VERSION -= 1"
echo f$FEDORA_VERSION | figlet -c -f mini | lolcat
fedpkg switch-branch f$FEDORA_VERSION
git merge rawhide
git push
fedpkg build --nowait
# And the next version (this may not work if Rawhide hasn't been
# branched yet)
let "FEDORA_VERSION += 2"
echo f$FEDORA_VERSION | figlet -c -f mini | lolcat
# Let's see if this works...
if fedpkg switch-branch f$FEDORA_VERSION; then
    git merge rawhide
    git push
    fedpkg build --nowait
else
    echo No f$FEDORA_VERSION yet | figlet -c -f mini | lolcat
fi
# And the EPEL versions...
echo epel9 | figlet -c -f mini | lolcat
fedpkg switch-branch epel9
git merge rawhide
git push
fedpkg build --nowait


echo Check status at https://koji.fedoraproject.org/koji/tasks?owner=tachoknight&state=active&view=tree&method=all&order=-id
echo or use:   echo or use: koji list-tasks --mine --before="\"`date -d \"+24 hours\" +\"%Y-%m-%d %H:%M\"`\"" --after="\"`date -d \"today 00:00\" +\"%Y-%m-%d %H:%M\"`\"" 

echo Started:_____$START_TS
echo Ended:_______`date`
