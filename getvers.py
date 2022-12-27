#!/usr/bin/env python3

import sys
import json

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

# Now we need the repos, which is the actual list of stuff that
# is needed for the build
repos = ver_dict['repos']
for key, val in repos.items():
    print(f"{key} - {val}")


