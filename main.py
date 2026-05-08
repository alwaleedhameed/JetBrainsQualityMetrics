import json
import sys

with open(sys.argv[1]) as f:
    data = json.load(f)

messages = data["messages"]

counts = {
    "system": 0,
    "user": 0,
    "assistant": 0,
    "tool": 0
}

for msg in messages:
    role = msg.get("role")
    if role in counts:
        counts[role] += 1

total = sum(counts.values())

print(f"System messages:    {counts['system']}")
print(f"User messages:      {counts['user']}")
print(f"Assistant messages: {counts['assistant']}")
print(f"Tool messages:      {counts['tool']}")
print("======================")
print(f"Total messages:     {total}")