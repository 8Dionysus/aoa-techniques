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

## 2026-05-03 - Root roadmap audit history preserved

Changed:

- preserved the former root closure-audit `ROADMAP.md` at
  `legacy/raw/ROOT_CLOSURE_AUDIT_ROADMAP_2026-05-03.md`
- kept current root `ROADMAP.md` focused on repo-level direction, horizons, and
  update rules
- updated Audit provenance and legacy accounting so the old audit baseline stays
  findable without remaining root authority

Not changed:

- no technique status changed
- no promotion queue or evidence verdict changed
- no active Audit part became root authority

## 2026-05-03 - Wave 0 Matrix Expansion

Changed:

- categorized all newer promoted bundles `AOA-T-0075` through `AOA-T-0104` in
  the promotion-readiness matrix
- moved the `v0.4 matrix-expansion lane` from `30` open rows to `0`
- raised the `internal-origin second-consumer lane` to include the session
  harvest, route-fork, diagnosis, progression, automation, quest, workspace
  boundary, and Method-growth extraction families
- raised the `fresh extraction lane` to include the recovery-wave bundles that
  still lack canonical-readiness notes

Verification lane:

```bash
python -m unittest tests.test_audit_mechanics_topology
python -m unittest tests.test_roadmap_parity
python scripts/validate_repo.py
python -m unittest discover -s tests
```

Not changed:

- no technique status changed
- no bundle-local canonical-readiness verdict changed
- no generated promotion-readiness surface became authority
