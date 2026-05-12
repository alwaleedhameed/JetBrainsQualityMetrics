import json
import sys

def extract_messages(data):
    if isinstance(data, list):
        return data[0]["transcripts"][0]["messages"]
    return data["messages"]

def count_messages(messages):
    counts = {"system": 0, "user": 0, "assistant": 0, "tool": 0}
    for msg in messages:
        role = msg.get("role")
        if role in counts:
            counts[role] += 1
    return counts

def analyze_file(path):
    with open(path) as f:
        data = json.load(f)
    messages = extract_messages(data)
    return count_messages(messages)

if __name__ == "__main__":
    counts = analyze_file(sys.argv[1])
    total = sum(counts.values())
    print(f"System messages:    {counts['system']}")
    print(f"User messages:      {counts['user']}")
    print(f"Assistant messages: {counts['assistant']}")
    print(f"Tool messages:      {counts['tool']}")
    print("======================")
    print(f"Total messages:     {total}")
