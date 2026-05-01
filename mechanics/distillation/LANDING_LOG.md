# Distillation Landing Log

This log records structural landings for the `aoa-techniques` Distillation
mechanic.

## 2026-05-01 - Active parts split

Changed:

- added route-local `AGENTS.md`, `DIRECTION.md`, `PARTS.md`, `PROVENANCE.md`,
  `LANDING_LOG.md`, and `ROADMAP.md`
- moved the five formerly flat distillation docs into part-local active homes
- added `parts/` and `legacy/` route cards
- preserved candidate verdicts and ledger counts without compaction
- added a decision record for the active/parts/legacy split

Verification lane:

```bash
python -m unittest tests.test_distillation_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
```

Not moved:

- no raw donor wave packet was copied into `legacy/raw/`
- no candidate verdict was promoted, dropped, or rewritten
- no technique bundle was minted by this structural pass
