# RPG Landing Log

## 2026-05-03 - Candidate Mechanics Surface

Landed a local RPG mechanics package as candidate-only technique-layer
pressure.

Included:

- package route surfaces: `README.md`, `DIRECTION.md`, `PARTS.md`,
  `PROVENANCE.md`, `LANDING_LOG.md`, and `ROADMAP.md`
- active part maps for source-boundary, feat-progression, quest-overlay, and
  owner-handoff anchors
- legacy scaffold files for source-to-active accounting with an empty raw
  inventory
- root mechanics map and request-receipt visibility
- topology tests for package presence, stop-lines, and owner handoffs

Explicitly not included:

- local raw receipts, because no local pre-split RPG receipt was found
- direct `ORQ-RPG-TECHNIQUES-*` acceptance or landing
- runtime ledger state, role canon, skill truth, playbook choreography, proof
  verdict, quest closure, memory canon, routing authority, universal scoring,
  owner acceptance, or automatic technique promotion

## 2026-05-03 - Legacy Scaffold Bridge

- Added `legacy/` scaffold files for source-to-active accounting.
- Kept raw inventory empty because no local pre-split RPG receipt is preserved.
- Updated provenance to point to the scaffold instead of treating legacy as an
  absent later add-on.

## Verification Route

Use:

```bash
python -m unittest tests.test_rpg_mechanics_topology tests.test_mechanics_request_receipts
python scripts/validate_nested_agents.py
python scripts/validate_repo.py
python -m unittest discover -s tests
git diff --check
```
