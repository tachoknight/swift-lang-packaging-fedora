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

dnf update -y
dnf install -y rpm-build rpm-devel rpmdevtools vim 
dnf install -y 'dnf-command(config-manager)'

# For debugging
dnf install -y llvm-symbolizer

# And get the version
VERSION=`grep VERSION_ID /etc/os-release | cut -d '=' -f 2`
echo Version is $VERSION

if [[ $FLAVOR == "Oracle"* ]]; then
	# Oracle does it differently
        dnf install -y epel-release
        dnf config-manager --set-enabled ol8_codeready_builder
elif [[ $FLAVOR == "Fedora"* ]]; then
	# Good ol' Fedora
        echo Oh, working with Fedora are we?
	dnf install -y figlet lolcat toilet

	# DNF5 is apparently in Fedora 41 and later
	if [ "$VERSION" -ge 41 ]; then
		dnf5 install -y 'dnf5-command(builddep)'
	fi
else
	# This should cover all the other flavors, like CentOS,
	# Rocky, AlmaLinux, etc.
        dnf install -y epel-release
        dnf config-manager --set-enabled epel
        dnf config-manager --set-enabled powertools

		# Enable CRB for CentOS-Stream
		/usr/bin/crb enable
fi

# Colorful silliness
if [ $(which lolcat) ]; then
  LOLCAT="lolcat"
else
  LOLCAT="cat"
fi

dnf install -y the_silver_searcher tig | $LOLCAT

# Now get the dependencies from the spec file
dnf builddep -y ./swift-lang.spec | $LOLCAT

# And we always want the line numbers in vim
echo "set nu" > ~/.vimrc | $LOLCAT

echo Container is ready to gooooooo.... | $LOLCAT
