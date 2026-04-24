# AGENTS.md

## Guidance for `reports/`

`reports/` contains readouts about technique coverage, drift, validation, or publication posture.

Reports are diagnostic surfaces. They may point to evidence and gaps, but they do not own technique meaning and must not outrank source-authored bundles.

Keep report language bounded: say what was measured, what was not measured, and what command or source produced the readout.

Do not convert a report into a proof claim that belongs in `aoa-evals` or a workflow claim that belongs in `aoa-skills`.

Verify with the report generator when present, then:

```bash
python scripts/validate_repo.py
python scripts/validate_semantic_agents.py
```
