#!/usr/bin/env python3

import sys
import json

# probably want: ./getvers.py ~/rpmbuild/BUILD/swift-source/swift/utils/update_checkout/update-checkout-config.json release/5.9
if len(sys.argv) != 3:
    print("args: path to json file, version of swift")
    sys.exit()

print(f"Gonna check {sys.argv[1]} for {sys.argv[2]}")

try:
    f = open(sys.argv[1])
except OSError as e:
    print(f"Hmm, no good reading {sys.argv[1]}: {e.errno} - {e.strerror}")
    sys.exit()

# Now convert to json...
j = json.load(f)

# The rest of this is _very_ specific to the update-checkout-config.json
# file

# First we need the branch schemes
bs = j['branch-schemes']
# Now let's get the one we were asked about
ver_dict = bs.get(sys.argv[2])
if not ver_dict:
    print(f"Couldn't find {sys.argv[2]} in the dictionary")
    sys.exit()

# We're gonna see if the item is referenced in the spec file
with open('swift-lang.spec', 'r') as file:
    spec_file_contents = file.read()

# Now we need the repos, which is the actual list of stuff that
# is needed for the build
repos = ver_dict['repos']
for key, val in repos.items():
    print(f"{key} - {val}")
    if key in spec_file_contents:
        print(f"\tFound {key} in spec file")
    else:
        print(f"\t!!!! DID NOT find {key} in spec file !!!!")
    
print(f"*** There are {len(repos)} parts to worry about ***")
