# Spark Prompt: test-factory

```text
You are running a standalone Spark test-factory session.

Read:
- root AGENTS.md
- .agents/AGENTS.md
- .agents/spark/AGENTS.md
- .agents/spark/registry.json
- .agents/spark/scenarios/test-factory/README.md
- the source contract named by the user

Task:
Add a small set of tests for the named existing contract.

Rules:
- test only a source-backed contract
- keep one test family
- avoid broad refactors
- run targeted tests before any broad test runner
- finish as done-or-handoff

Return:
- source contract read
- tests added or changed
- validation run
- skipped checks
- remaining risk
```
