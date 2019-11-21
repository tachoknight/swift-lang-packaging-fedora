#!/bin/bash

MYDIR=$PWD

START_TS=`date`

rm -rf /home/tachoknight/rpmbuild
rm $MYDIR/build-output.txt
mkdir -p /home/tachoknight/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
cp $PWD/*.patch /home/tachoknight/rpmbuild/SOURCES
cp $PWD/*.conf /home/tachoknight/rpmbuild/SOURCES
cp $PWD/swift-lang.spec /home/tachoknight/rpmbuild/SPECS

pushd /home/tachoknight/rpmbuild/SPECS
spectool -g -R ./swift-lang.spec
# Now do the actual build
mock -r fedora-31-s390x --spec=swift-lang.spec --sources=../SOURCES --resultdir=../RPMS --buildsrpm
#rpmbuild -ba ./swift-lang.spec 2>&1 | tee $MYDIR/build-output.txt
popd

echo Started:_____$START_TS
echo Ended:_______`date`
