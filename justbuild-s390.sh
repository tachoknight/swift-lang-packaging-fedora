#!/bin/bash

MYDIR=$PWD

START_TS=`date`

rm -rf $HOME/rpmbuild
rm -rf $MYDIR/mock-results
mkdir -p $HOME/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
cp $PWD/*.patch $HOME/rpmbuild/SOURCES
cp $PWD/swift-lang.spec $HOME/rpmbuild/SPECS

pushd $HOME/rpmbuild/SPECS
spectool -g -R ./swift-lang.spec
# Now do the actual build
#mock --init --clean -r fedora-31-s390x --spec=swift-lang.spec --sources=../SOURCES --resultdir=$MYDIR/mock-results --buildsrpm --rebuild --rpmbuild-opts=--noclean --no-cleanup-after 2>&1 
mock --init --clean -r fedora-31-s390x --spec=swift-lang.spec --sources=../SOURCES --resultdir=$MYDIR/mock-results --buildsrpm 
pushd $MYDIR/mock-results
mock -r fedora-31-s390x rebuild ./swift-lang-5.2.2-1.fc31.src.rpm
popd

echo Started:_____$START_TS
echo Ended:_______`date`
