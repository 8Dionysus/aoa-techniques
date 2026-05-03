# Boundary Bridge Landing Log

This ledger records structural landings for `mechanics/boundary-bridge/`. It
is not a roadmap and not a technique status source.

## 2026-05-03

- Added the local Boundary-bridge mechanic package as candidate-only practice
  pressure.
- Created active route files: `AGENTS.md`, `README.md`, `DIRECTION.md`,
  `PARTS.md`, `PROVENANCE.md`, `LANDING_LOG.md`, and `ROADMAP.md`.
- Created active parts:
  - `parts/owner-boundary-anchors/README.md`
  - `parts/derived-projection-anchors/README.md`
  - `parts/proof-claim-anchors/README.md`
- Updated `mechanics/README.md`, `mechanics/AGENTS.md`, and
  `mechanics/REQUEST_RECEIPTS.md` so boundary-bridge is discoverable without
  claiming a direct `ORQ-BRIDGE-TECHNIQUES-*` lane.
- Added topology tests and a decision note for the candidate-only
  boundary-bridge landing.

## Verification Route

Use:

```bash
python -m unittest tests.test_boundary_bridge_mechanics_topology tests.test_mechanics_request_receipts tests.test_validate_repo
python scripts/validate_repo.py
python -m unittest discover -s tests
```
