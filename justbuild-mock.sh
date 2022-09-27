#!/bin/bash

MYDIR=$PWD

START_TS=`date`

#BUILD=fedora-rawhide-`uname -i`
BUILD=alma+epel-8-`uname -m`
#BUILD=fedora-36-`uname -i`

rm -rf $HOME/rpmbuild
rm -rf $MYDIR/mock-results
mkdir $MYDIR/mock-results
mkdir -p $HOME/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
cp $PWD/*.patch $HOME/rpmbuild/SOURCES
cp $PWD/swift-lang.spec $HOME/rpmbuild/SPECS

#echo Cleaning $BUILD
mock -r $BUILD --scrub=all

pushd $HOME/rpmbuild/SPECS
echo Now getting the sources...
spectool -g -R ./swift-lang.spec
# Now do the actual build
echo Now gonna hopefully build it
#mock --clean -r $BUILD --enablerepo=local --spec=swift-lang.spec --sources=../SOURCES --resultdir=$MYDIR/mock-results --buildsrpm --rebuild --rpmbuild-opts=--noclean --no-cleanup-after 2>&1 | tee $MYDIR/mock-results/build-output.txt
mock --clean -r $BUILD --spec=swift-lang.spec --sources=../SOURCES --resultdir=$MYDIR/mock-results --buildsrpm --rebuild --rpmbuild-opts=--noclean --no-cleanup-after 2>&1 | tee $MYDIR/mock-results/build-output.txt
popd

echo Started:_____$START_TS
echo Ended:_______`date`
