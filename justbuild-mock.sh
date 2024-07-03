#!/bin/bash

SECONDS=0

MYDIR=$PWD

START_TS=`date`

BUILD=fedora-rawhide-`uname -m`
#BUILD=alma+epel-8-`uname -m`
#BUILD=fedora-38-`uname -m`

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

# Now tell us how long it took
hours=$((SECONDS / 3600))
minutes=$(( (SECONDS % 3600) / 60 ))
seconds=$((SECONDS % 60))

# Print the elapsed time
echo "Elapsed Time: $hours hour(s) $minutes minute(s) $seconds second(s)"

