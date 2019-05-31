import os
import sys
import json
import re

# Load Variables
event_type = os.environ.get("GITHUB_EVENT_NAME")
event_path = os.environ.get("GITHUB_EVENT_PATH")

# Check to ensure that this is a push event
if event_type != "push":
    exit(1)

# Load the push event file
with open(event_path, 'r') as f:
    github_event_string = f.read()

github_event_json = json.loads(github_event_string)

# load up the changes
changed_files = []
for commit in github_event_json["commits"]:
    changed_files.extend(commit["added"])
    changed_files.extend(commit["modified"])
    changed_files.extend(commit["removed"])

# find if any of the changes match the pattern.
does_match = False
for pattern in sys.argv:
    if does_match:
        break

    for fname in changed_files:
        if re.match(pattern, fname):
            does_match = True
            break

if does_match:
    exit(0)
else:
    exit(1)