import json
import sys
from pathlib import Path
from statistics import mean, median

from main import count_messages

TOPMODELS = {
    "claude-4-5-opus-high": "experiments/evaluation/bash-only/20260217_mini-v2.0.0_claude-4-5-opus-high",
    "minimax-2-5-high":     "experiments/evaluation/bash-only/20260217_mini-v2.0.0_minimax-2-5-high",
    "gemini-3-flash-high":  "experiments/evaluation/bash-only/20260217_mini-v2.0.0_gemini-3-flash-high",
    "claude-4-6-opus":      "experiments/evaluation/bash-only/20260217_mini-v2.0.0_claude-4-6-opus",
    "gpt-5-2-codex":        "experiments/evaluation/bash-only/20260219_mini-v2.0.0_gpt-5-2-codex",
}

def analyze_traj_file(path):
    data = json.loads(path.read_text())
    messages = data.get("messages", [])
    if not messages:
        return None
    counts = count_messages(messages)
    counts["total"] = sum(counts.values())
    return counts
    
def analyze_model(name, base_path):
    base = Path(base_path)
    trajs_dir = base / "trajs"
    details_path = base / "per_instance_details.json"

    print(f"\n{'='*55}")
    print(f"  {name}")
    print(f"{'='*55}")

    if details_path.exists():
        details = json.loads(details_path.read_text())
        total = len(details)
        resolved = sum(1 for val in details.values() if val.get("resolved"))
        api_calls = [val["api_calls"] for val in details.values() if "api_calls" in val]
        costs = [val["cost"] for val in details.values() if "cost" in val]

        print(f"\n  Aggregate ({total} instances):")
        print(f"    Resolved:           {resolved}/{total} ({resolved/total*100:.1f}%)")
        if api_calls:
            print(f"    API calls — mean:   {mean(api_calls):.1f}  median: {median(api_calls):.1f}  max: {max(api_calls)}")
        if costs:
            print(f"    Cost     — mean:   ${mean(costs):.4f}  total: ${sum(costs):.2f}")
    else:
        print("  (per_instance_details.json not found)")

    if trajs_dir.exists():
        traj_files = list(trajs_dir.glob("**/*.traj")) + list(trajs_dir.glob("**/*.traj.json"))
        if traj_files:
            all_counts = [c for f in traj_files if (c := analyze_traj_file(f)) is not None]
            if all_counts:
                n = len(all_counts)
                for role in ("system", "user", "assistant", "tool", "total"):
                    vals = [c[role] for c in all_counts]
                    print(f"\n  {role.capitalize()} messages ({n} trajs):")
                    print(f"    mean: {mean(vals):.1f}   median: {median(vals):.1f}   max: {max(vals)}")
        else:
            print("\n  No trajectory files found (still downloading?)")
    else:
        print("\n  trajs/ folder not found (still downloading?)")

def main():
    if len(sys.argv) > 1:
        name = sys.argv[1]
        if name not in TOPMODELS:
            print(f"Unknown model. Available: {list(TOPMODELS.keys())}")
            sys.exit(1)
        models = {name: TOPMODELS[name]}
    else:
        models = TOPMODELS

    for name, path in models.items():
        analyze_model(name, path)
    print()

if __name__ == "__main__":
    main()
