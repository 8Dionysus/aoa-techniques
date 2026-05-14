# AGENTS.md

Route card for `mechanics/questbook/parts/`.

## Purpose

Each part owns one bounded local Questbook route for `aoa-techniques`. Parts
describe movement around technique canon; they do not become canonical
technique bundles, quest source truth, or cross-owner authority.

## Local law

- Keep part docs concise and owner-bounded.
- Preserve links to `PROVENANCE.md` when moving, staging, or compacting source
  material.
- Keep source quest truth in lane-first `quests/`, generated projections in
  `generated/`, and technique meaning in `techniques/**/TECHNIQUE.md`.
- Keep proof, memory, routing, playbook choreography, RPG reading, runtime, and
  owner acceptance with their owning repositories or surfaces.
- Promote into `techniques/` only when the reusable practice can stand as an
  atomic technique with validation.

## Verify

Use the package and root tests after part changes:

```bash
python -m unittest discover -s mechanics/questbook/tests
python scripts/validate_repo.py
```
