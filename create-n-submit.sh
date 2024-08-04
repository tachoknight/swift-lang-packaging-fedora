#!/bin/bash

THISDIR=$HOME/swift-lang-packaging-fedora

pushd $THISDIR

# First we want to capture the hash of the swift-lang.spec
# file...
bh=`md5sum ./swift-lang.spec`

# Now run the python program to check for updates
# and modify the swift-lang.spec file accordingly
./nrc.py

# Now hash the file again
ah=`md5sum ./swift-lang.spec`

# And now only bother doing the rest of the script
# if the hash was changed, otherwise exit
if [ "$bh" = "$ah" ]; then
	exit 0
fi

#
# Okay, we're gonna do this...
#

# First we're going to commit the changes...
git commit -am "Updated to `awk '/%global swift_version *./{print $3}' ./swift-lang.spec`"
git push 

# ... and now we're going to submit the srpm to koji to do the build
echo Now submitting the srpm for koji to build

# First make sure we log on, using the info in the KOJI_USER environment
# variable
kinit -kt $HOME/fedora.keytab $KOJI_USER

# And call our submit script to do all the work
source $THISDIR/submit-scratch-builds.sh


