# AGENTS.md

## Guidance for `mechanics/distillation/parts/technique-reform-ingress/reports/`

This directory contains generated scout readouts for the Technique Reform
Ingress part: kind counts, family scout output, kind ambiguity audit, topology
scout output, and tree projection output.

Reports are diagnostic surfaces. They may point to evidence and gaps, but they
do not own technique meaning and must not outrank source-authored bundles,
frontmatter, or active Distillation review packets.

Keep report language bounded: say what was measured, what was not measured, and
what command or source produced the readout.

Do not convert a report into a proof claim that belongs in `aoa-evals` or a workflow claim that belongs in `aoa-skills`.

Verify with the report generator when present, then:

```bash
python scripts/validate_repo.py
python scripts/validate_semantic_agents.py
```
