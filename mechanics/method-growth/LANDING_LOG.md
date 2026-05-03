# Method-Growth Landing Log

This log records structural landings for the `aoa-techniques` Method-growth
mechanic.

## 2026-05-01 - Active Parts Split

Changed:

- added route-local `AGENTS.md`, `DIRECTION.md`, `PARTS.md`, `PROVENANCE.md`,
  `LANDING_LOG.md`, and `ROADMAP.md`
- moved five formerly flat Method-growth surfaces into part-local active homes
- added `parts/` route cards
- preserved v0.7 downstream adoption-wave wording without promoting any part
  into a technique bundle

Verification lane:

```bash
python -m unittest tests.test_method_growth_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
```

Not moved:

- no raw wave receipt was copied into `legacy/raw/`
- no adoption surface was promoted into `techniques/`
- no technique-to-skill handoff was treated as skill acceptance

## 2026-05-03 - Legacy Scaffold Bridge

- Added `legacy/` scaffold files for source-to-active accounting.
- Kept raw inventory empty because the pre-split adoption surfaces were compact
  active material already distilled into part-local homes.
- Updated provenance to point to the scaffold instead of treating legacy as an
  absent later add-on.
