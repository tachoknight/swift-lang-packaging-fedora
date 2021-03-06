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
# Now do the actual build
mock --clean -r fedora-32-x86_64 --spec=swift-lang.spec --sources=../SOURCES --resultdir=$MYDIR/mock-results --buildsrpm --rebuild --rpmbuild-opts=--noclean --no-cleanup-after 2>&1 | tee $MYDIR/mock-results/build-output-f32.txt
mock --scrub all fedora-32-x86_64
mock --clean -r fedora-rawhide-x86_64 --spec=swift-lang.spec --sources=../SOURCES --resultdir=$MYDIR/mock-results --buildsrpm --rebuild --rpmbuild-opts=--noclean --no-cleanup-after 2>&1 | tee $MYDIR/mock-results/build-output-rawhide.txt
mock --scrub all fedora-rawhide-x86_64
mock --clean -r epel-8-x86_64 --spec=swift-lang.spec --sources=../SOURCES --resultdir=$MYDIR/mock-results --buildsrpm --rebuild --rpmbuild-opts=--noclean --no-cleanup-after 2>&1 | tee $MYDIR/mock-results/build-output-epel8.txt
mock --scrub all epel-8-x86_64
popd

echo Started:_____$START_TS
echo Ended:_______`date`
