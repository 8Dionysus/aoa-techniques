# Spark Prompt: candidate-scout

```text
You are running a standalone Spark candidate-scout session.

Read:
- root AGENTS.md
- .agents/AGENTS.md
- .agents/spark/AGENTS.md
- .agents/spark/registry.json
- .agents/spark/scenarios/candidate-scout/README.md
- mechanics/README.md when the source is mechanic-local
- the donor, legacy, or candidate source named by the user

Task:
Map raw or mechanic-local material to likely active homes, candidate routes,
owner questions, portability risks, or no-op findings.

Rules:
- scout only
- preserve provenance
- do not promote into canon
- do not rewrite active doctrine unless explicitly requested
- finish as done-or-handoff

Return:
- sources read
- likely active homes
- rejected or risky material
- validation implication
- handoff packet if deeper distillation is needed
```
