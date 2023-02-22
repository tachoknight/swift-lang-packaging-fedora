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
nohup koji build --scratch rawhide $SRPM_FILE &
sleep 60s
echo f$FEDORA_VERSION | figlet -c -f mini | lolcat
nohup koji build --scratch f$FEDORA_VERSION $SRPM_FILE &
sleep 10s
# Now the previous version of Fedora
let "FEDORA_VERSION -= 1"
echo f$FEDORA_VERSION | figlet -c -f mini | lolcat
nohup koji build --scratch f$FEDORA_VERSION $SRPM_FILE &
sleep 10s
# And the next version
let "FEDORA_VERSION += 2"
echo f$FEDORA_VERSION | figlet -c -f mini | lolcat
nohup koji build --scratch f$FEDORA_VERSION $SRPM_FILE &
sleep 10s
# And the EPEL versions...
echo epel9 | figlet -c -f mini | lolcat
nohup koji build --scratch epel9 $SRPM_FILE &
sleep 10s
echo epel8 | figlet -c -f mini | lolcat
nohup koji build --scratch epel8 $SRPM_FILE &
sleep 10s

popd

echo Started:_____$START_TS
echo Ended:_______`date`
