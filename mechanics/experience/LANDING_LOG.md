# Experience Landing Log

This log records structural landings for the `aoa-techniques` Experience
mechanic.

## 2026-05-01 - Active Parts Split

Changed:

- added route-local `AGENTS.md`, `DIRECTION.md`, `PARTS.md`, `PROVENANCE.md`,
  `LANDING_LOG.md`, and `ROADMAP.md`
- moved seven formerly flat Experience surfaces into part-local active homes
- added `parts/` route cards
- preserved Experience seed wording without promoting any part into a technique
  bundle or runtime authority

Verification lane:

```bash
python -m unittest tests.test_experience_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
```

Not moved:

- no raw wave receipt was copied into `legacy/raw/`
- no Experience surface was promoted into `techniques/`
- no live office, release, runtime, or Tree-of-Sophia authority was claimed

## 2026-05-03 - Legacy Scaffold Bridge

- Added `legacy/` scaffold files for source-to-active accounting.
- Kept raw inventory empty because the pre-split Experience seed surfaces were
  compact active material already distilled into part-local homes.
- Updated provenance to point to the scaffold instead of treating legacy as an
  absent later add-on.
