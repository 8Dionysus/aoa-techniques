# AGENTS.md

## Guidance for `data/`

`data/` holds source-supporting or build-supporting data used by the technique canon.

Treat data changes as contract-adjacent. They may alter catalogs, reports, grouping, or downstream projections even when no Markdown changed.

Keep data public-safe and reproducible. Do not add private transcripts, personal data, secret-bearing payloads, or local-only paths.

If data is derived, document the source and rebuild path. If data is authored, keep ownership clear and avoid making generated files the source of truth.

Verify with the nearest builder or validator, then:

```bash
python scripts/validate_repo.py
python scripts/validate_semantic_agents.py
```
