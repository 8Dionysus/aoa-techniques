# Questbook Landing Log

This ledger records structural landings for `mechanics/questbook/`. It is not
a roadmap and not a quest source or technique status source.

## 2026-05-03

- Added the local Questbook mechanic package as candidate-only practice
  pressure.
- Created active route files: `AGENTS.md`, `README.md`, `DIRECTION.md`,
  `PARTS.md`, `PROVENANCE.md`, `LANDING_LOG.md`, and `ROADMAP.md`.
- Created active parts:
  - `parts/source-index-anchors/README.md`
  - `parts/technique-obligation-anchors/README.md`
  - `parts/harvest-promotion-anchors/README.md`
- Updated `mechanics/README.md`, `mechanics/AGENTS.md`, and
  `mechanics/REQUEST_RECEIPTS.md` so questbook is discoverable without
  claiming a direct `ORQ-QUESTBOOK-TECHNIQUES-*` lane.
- Added topology tests and a decision note for the candidate-only Questbook
  landing.

## Verification Route

Use:

```bash
python -m unittest tests.test_questbook_mechanics_topology tests.test_mechanics_request_receipts tests.test_validate_repo
python scripts/validate_repo.py
python -m unittest discover -s tests
```
