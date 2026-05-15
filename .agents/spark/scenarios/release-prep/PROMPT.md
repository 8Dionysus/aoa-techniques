# Spark Prompt: release-prep

```text
You are running a standalone Spark release-prep session.

Read:
- root AGENTS.md
- .agents/AGENTS.md
- .agents/spark/AGENTS.md
- .agents/spark/registry.json
- .agents/spark/scenarios/release-prep/README.md
- the release surface named by the user

Task:
Check release readiness: changed surfaces, validation, public claims,
generated parity, owner routes, rollback shape, and remaining risks.

Rules:
- do not publish, tag, push, or merge unless explicitly asked
- keep public claims supportable
- finish as done-or-handoff

Return:
- release scope
- checks run
- blocking risks
- public claim risks
- next owner route
```
