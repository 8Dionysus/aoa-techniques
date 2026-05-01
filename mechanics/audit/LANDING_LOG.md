# Audit Landing Log

This log records structural landings for the `aoa-techniques` Audit mechanic.

## 2026-05-01 - Active parts split

Changed:

- added route-local `AGENTS.md`, `DIRECTION.md`, `PARTS.md`, `PROVENANCE.md`,
  `LANDING_LOG.md`, and `ROADMAP.md`
- moved the four formerly flat audit docs into part-local active homes
- added `parts/` and `legacy/` route cards
- preserved promotion posture, readiness counts, evidence lanes, and status
  boundaries without changing bundle state
- added a decision record for the Audit active/parts/legacy split

Verification lane:

```bash
python -m unittest tests.test_audit_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
```

Not moved:

- no technique status changed
- no evidence verdict changed
- no generated promotion surface became authority
- no raw pre-prune receipt was added because no audit ledger was shortened
