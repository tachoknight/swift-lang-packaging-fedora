#!/bin/bash

THISDIR=/home/rolson/rpmdev/swift-lang

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

rm -rf /home/rolson/rpmbuild
rm $THISDIR/cnb-build-output.txt
mkdir -p /home/rolson/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
cp $THISDIR/*.patch /home/rolson/rpmbuild/SOURCES
cp $THISDIR/*.conf /home/rolson/rpmbuild/SOURCES
cp $THISDIR/swift-lang.spec /home/rolson/rpmbuild/SPECS

pushd /home/rolson/rpmbuild/SPECS
spectool -g -R ./swift-lang.spec
# Get the dependencies
dnf builddep -y ./swift-lang.spec
# Now do the actual build
rpmbuild -ba ./swift-lang.spec 2>&1 | tee $THISDIR/cnb-build-output.txt
popd

# And commit it to the nightly-builds branch
#git checkout nightly-builds
#git commit -am "Updated to `awk '/%global swifttag *./{print $3}' ./swift-lang.spec`"
#git push fedorapeople

# Now move it to fedorapeople
ssh fedorapeople.org "rm ~/public_html/swift-lang/*$THISVERSION*.rpm"
scp /home/rolson/rpmbuild/SRPMS/* fedorapeople.org:~/public_html/swift-lang
scp /home/rolson/rpmbuild/RPMS/x86_64/* fedorapeople.org:~/public_html/swift-lang
scp /home/rolson/rpmbuild/SPECS/* fedorapeople.org:~/public_html/swift-lang
