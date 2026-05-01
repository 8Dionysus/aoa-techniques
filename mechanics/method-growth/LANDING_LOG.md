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
