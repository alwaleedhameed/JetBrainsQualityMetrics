# Quality Metrics for Agent Trajectories

This repository is a submission for the JetBrains research internship on **Quality Metrics for Agent Trajectories**. The internship focuses on measuring and comparing the quality of coding agent trajectories (sequences of edits and tool calls) beyond simple pass/fail outcomes. The goal is to develop metrics that capture the *efficiency* and *reliability* of how an agent reaches a solution, not just whether it does.

Three tasks were completed as part of the application.

## Task 1: Trajectory Metrics CLI Tool

Implemented a Python command-line tool (`main.py`) that parses a SWE-bench trajectory JSON file and computes the number of messages per role.

```bash
python main.py <trajectory.json>
```

The tool reports system, user, assistant, and tool message counts alongside the total.

`analyze_models.py` extends this to batch-process full model evaluation runs across multiple models.

## Task 2: Top 5 Model Trajectory Analysis

Used the tool to process all 500 trajectories for each of the top five mini-SWE-agent-v2 leaderboard models (Claude 4.5 Opus high reasoning, Gemini 3 Flash high reasoning, MiniMax M2.5 high reasoning, Claude Opus 4.6, GPT-5-2 Codex) and compared them across resolve rate, API call count, and cost.

Findings are in [`task2_report.md`](task2_report.md).

## Task 3: Research Paper Summary

Summarised the paper *"Towards a Science of AI Agent Reliability"* (arXiv, pages 1–21), covering its twelve-metric reliability framework across consistency, robustness, predictability, and safety dimensions.

Summary is in [`task3_summary.md`](task3_summary.md).
