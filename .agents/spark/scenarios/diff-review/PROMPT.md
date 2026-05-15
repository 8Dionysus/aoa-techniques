# Spark Prompt: diff-review

```text
You are running a standalone Spark diff-review session.

Read:
- root AGENTS.md
- .agents/AGENTS.md
- .agents/spark/AGENTS.md
- .agents/spark/registry.json
- .agents/spark/scenarios/diff-review/README.md
- the provided diff or pull request context

Task:
Review the diff for bugs, drift, missed checks, source-of-truth confusion,
generated parity gaps, public-safety problems, and scope creep.

Rules:
- findings first
- cite exact files or lines when available
- do not edit
- finish as done-or-handoff

Return:
- findings by severity
- checks run or skipped
- approval posture or handoff packet
```
