#!/bin/bash

THISDIR=$HOME/swift-lang-packaging-fedora

pushd $THISDIR

# Gives us the version number of this platform
THISVERSION=`cat /etc/os-release | grep PLATFORM_ID | awk -F: '/platform:*/{print $2}' | cut -c 2- | rev | cut -c 2- | rev`
echo Building on $THISVERSION of Fedora

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

# Okay, we're gonna do this...

rm -rf $HOME/rpmbuild
rm $THISDIR/cnb-build-output.txt
mkdir -p $HOME/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
cp $THISDIR/*.patch $HOME/rpmbuild/SOURCES
cp $THISDIR/*.conf $HOME/rpmbuild/SOURCES
cp $THISDIR/swift-lang.spec $HOME/rpmbuild/SPECS

pushd $HOME/rpmbuild/SPECS
spectool -g -R ./swift-lang.spec
# Get the dependencies (here for documentation about what to do, this
# needs sudo to run)
#dnf builddep -y ./swift-lang.spec
# Now do the actual build
rpmbuild -ba ./swift-lang.spec 2>&1 | tee $THISDIR/cnb-build-output.txt
popd

# And commit it to the nightly-builds branch
#git checkout nightly-builds
git commit -am "Updated to `awk '/%global swift_version *./{print $3}' ./swift-lang.spec`"
git push 

# Now move it to fedorapeople
ssh fedorapeople.org "rm ~/public_html/swift-lang/*$THISVERSION*.rpm"
scp $HOME/rpmbuild/SRPMS/* fedorapeople.org:~/public_html/swift-lang
scp $HOME/rpmbuild/RPMS/x86_64/* fedorapeople.org:~/public_html/swift-lang
scp $HOME/rpmbuild/SPECS/* fedorapeople.org:~/public_html/swift-lang

