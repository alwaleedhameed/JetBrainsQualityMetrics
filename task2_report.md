# Task 2 Report: Trajectory Analysis of Top-5 mini-SWE-agent-v2 Models

## Methodology

Trajectories were accesed via the SWE-bench experiments repository for the five highest-ranked mini-SWE-agent-v2 submissions on the SWE-bench verified leaderboard (500 instances each). Aggregate statistics were drawn from `per_instance_details.json`; message-role breakdowns were computed from the downloaded `.traj.json` files using the implemented tool from Task 1. However, stats for the gpt-5-2 codex model were unavailable as no per instance json was found within the nested repo, so using metadata numbers.

---

### 1. General Stats & Pass/Fail Fatal Flaw

The top four models are within only 1.2 percentage points of each other (75.6–76.8%), comparing them with the binary pass/fail comparisons is nearly meaningless at this tier. GPT-5-2-high trails slightly at 72.8%. This compression confirms that trajectory-level metrics are necessary to meaningfully distinguish agents that appear equivalent on outcome alone unlike the approach from the swe-bench paper.

| Model | Resolved | Mean API Calls | Mean Cost |
|---|---|---|---|
| claude-4-5-opus-high | 384/500 (76.8%) | 32.9 | $0.754 |
| minimax-2-5-high | 379/500 (75.8%) | 60.5 | $0.073 |
| gemini-3-flash-high | 379/500 (75.8%) | 56.1 | $0.356 |
| claude-4-6-opus | 378/500 (75.6%) | 28.9 | $0.552 |
| gpt-5-2-high | 364/500 (72.8%) | 35.0 | $0.474 |

### 2. Claude Models Solve Tasks in Half the Steps

Claude models (opus-high: 32.9 calls, 4-6-opus: 28.9 calls) go through tasks using roughly half the API calls of Gemini Flash (56.1) and MiniMax (60.5), despite producing comparable outcomes which is a direct signal of thrashing. Gemini and MiniMax appear to explore more broadly before converging, while Claude models converge faster to the final outcome.

### 3. Consistency 

Gemini Flash statistically exhibits a relatively tight spread (56.1 mean vs. 54 median), indicating stable, predictable trajectory length regardless of task. Claude 4-6 Opus shows a wider gap (28.9 mean vs. 23 median), suggesting that while it is typically concise, a subset of tasks causes significant step inflation which is pattern worth isolating to understand what task properties trigger extended reasoning.

### 4. Cost Efficiency Does Not Follow Resolve Rate

MiniMax achieves near-identical resolve rate to Claude opus-high (75.8% vs. 76.8%) at roughly one-tenth the per-instance cost ($0.073 vs. $0.754). However, this comes at the cost of double the API calls (60.5 vs. 32.9). This suggests MiniMax compensates for cheaper but less capable per-call reasoning with more iterations. Nonetheless, it still comes out at roughly over 5 times the value with this comparison.

## Summary

Despite near-identical resolve rates, the five models exhibit fundamentally different trajectory profiles. Claude models are efficient but occasionally take untraceable leaps, Gemini is consistent but verbose, and MiniMax is cost-effective but step-heavy. These differences, invisible to pass/fail metrics, are precisely the signals that trajectory-quality metrics are designed to surface that went unmentioned in the SWE-bench paper.
