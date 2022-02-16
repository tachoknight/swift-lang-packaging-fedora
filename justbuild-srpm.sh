#!/bin/bash


echo Bulding SRPM | figlet

MYDIR=$PWD

START_TS=`date`

# Make sure we're up to date (works best in containers)
dnf -y update

rm -rf $HOME/rpmbuild
rm $MYDIR/build-output.txt
mkdir -p $HOME/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
cp $PWD/*.patch $HOME/rpmbuild/SOURCES
#cp $PWD/*.conf $HOME/rpmbuild/SOURCES
cp $PWD/swift-lang.spec $HOME/rpmbuild/SPECS

pushd $HOME/rpmbuild/SPECS
spectool -g -R ./swift-lang.spec
# Now do the actual build
rpmbuild -bs ./swift-lang.spec 2>&1 | tee $MYDIR/build-output.txt
popd

echo Started:_____$START_TS
echo Ended:_______`date`
