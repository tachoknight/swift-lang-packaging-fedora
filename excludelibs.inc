# This file contains the list of libraries
# that should not be exposed outside of the
# swift package

%global __provides_exclude ^(libLTO[.]so.*)$
%global __requires_exclude ^(libLTO[.]so.*)$
%global __provides_exclude ^(libclang_rt.*.so.*)$
%global __requires_exclude ^(libclang_rt.*.so.*)$
%global __provides_exclude ^(liblldb[.]so.*)$
%global __requires_exclude ^(liblldb[.]so.*)$
