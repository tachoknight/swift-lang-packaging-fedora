#!/bin/bash
#
# The purpose of this script is to build the SRPM
# and then send it to Koji for scratch builds so
# all the various flavors can be tested to see if
# they build correctly
#

START_TS=`date`

export MYDIR=$PWD
# Our current version of Fedora
export FEDORA_VERSION=`rpm -E %fedora`

#<<comment
echo Gonna submit scratch builds | figlet -c -f pagga | lolcat
echo DID YOU LOG INTO KOJI FIRST? | figlet -c -f future | lolcat
echo Building SRPM first...

rm -rf $HOME/rpmbuild
rm $MYDIR/build-output.txt
mkdir -p $HOME/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
cp $MYDIR/*.patch $HOME/rpmbuild/SOURCES
cp $MYDIR/swift-lang.spec $HOME/rpmbuild/SPECS

pushd $HOME/rpmbuild/SPECS
spectool -g -R ./swift-lang.spec
# Now do the actual build
rpmbuild -bs ./swift-lang.spec 2>&1 | tee $MYDIR/build-output.txt
#comment

# Now submit them
echo Submitting to Koji | figlet -c -f future | lolcat
export SRPM_FILE=`find $HOME/rpmbuild/SRPMS -name swift-lang\*`
echo rawhide | figlet -c -f mini | lolcat
koji build --nowait --scratch rawhide $SRPM_FILE 
echo f$FEDORA_VERSION | figlet -c -f mini | lolcat
koji build --nowait --scratch f$FEDORA_VERSION $SRPM_FILE
# Now the previous version of Fedora
let "FEDORA_VERSION -= 1"
echo f$FEDORA_VERSION | figlet -c -f mini | lolcat
koji build --nowait --scratch f$FEDORA_VERSION $SRPM_FILE
# And the next version
let "FEDORA_VERSION += 2"
echo f$FEDORA_VERSION | figlet -c -f mini | lolcat
koji build --scratch --nowait f$FEDORA_VERSION $SRPM_FILE
# And the EPEL versions...
echo epel9 | figlet -c -f mini | lolcat
koji build --nowait --scratch epel9 $SRPM_FILE
echo epel8 | figlet -c -f mini | lolcat
koji build --scratch --nowait epel8 $SRPM_FILE 

popd

echo Check status at https://koji.fedoraproject.org/koji/tasks?owner=tachoknight&state=active&view=tree&method=all&order=-id

echo Started:_____$START_TS
echo Ended:_______`date`
