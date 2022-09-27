#!/bin/bash
#
# The purpose of this script is to prepare a container environment
# to build Swift. Note that this script assumes you are *in* the
# container, and have already installed git and pulled down this
# repo.
# Also note that this is specific to Fedora-flavored containers.
#

dnf install -y rpm-build rpm-devel rpmdevtools vim epel-release figlet
dnf install -y 'dnf-command(config-manager)'
dnf config-manager --set-enabled epel
dnf config-manager --set-enabled powertools
# Now get the dependencies from the spec file
dnf builddep -y ./swift-lang.spec

echo Container is ready to gooooooo....
