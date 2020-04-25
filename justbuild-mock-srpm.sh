#!/bin/bash

MYDIR=$PWD

START_TS=`date`

rm -rf $HOME/rpmbuild
rm -rf $MYDIR/mock-results
mkdir $MYDIR/mock-results
mkdir -p $HOME/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
cp $PWD/*.patch $HOME/rpmbuild/SOURCES
cp $PWD/swift-lang.spec $HOME/rpmbuild/SPECS

pushd $HOME/rpmbuild/SPECS
spectool -g -R ./swift-lang.spec
# Now do the actual build of the SRPM
mock --clean -r fedora-rawhide-x86_64 --spec=swift-lang.spec --sources=../SOURCES --resultdir=$MYDIR/mock-results --buildsrpm 
popd

echo Started:_____$START_TS
echo Ended:_______`date`
