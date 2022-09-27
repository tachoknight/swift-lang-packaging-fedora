#!/bin/bash
#
# The purpose of this script is to prepare a container environment
# to build Swift. Note that this script assumes you are *in* the
# container, and have already installed git and pulled down this
# repo.
# Also note that this is specific to Fedora-flavored containers.
#

# Which flavor are we using, because some require different things
FLAVOR=`( lsb_release -ds || cat /etc/*release || uname -om ) 2>/dev/null | head -n1`
echo Working with $FLAVOR

dnf install -y rpm-build rpm-devel rpmdevtools vim epel-release
dnf install -y 'dnf-command(config-manager)'

# Oracle does it differently
if [[ $FLAVOR == "Oracle"* ]]; then
	dnf config-manager --set-enabled ol8_codeready_builder
else
	dnf config-manager --set-enabled epel
	dnf config-manager --set-enabled powertools
fi

# Now get the dependencies from the spec file
dnf builddep -y ./swift-lang.spec

echo Container is ready to gooooooo....
