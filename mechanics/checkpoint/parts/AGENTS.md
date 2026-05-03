# AGENTS.md

Route card for `mechanics/checkpoint/parts/`.

## Purpose

Each part owns one bounded local checkpoint route for `aoa-techniques`. Parts
describe movement around technique canon; they do not become canonical
technique bundles or checkpoint implementation authority.

## Local law

- Keep part docs concise and owner-bounded.
- Preserve links to `PROVENANCE.md` when moving, staging, or compacting source
  material.
- Keep controls, protocol, actor posture, memory, proof, runtime, routing,
  stats, seed lineage, and owner acceptance with their owning repositories.
- Promote into `techniques/` only when the reusable practice can stand as an
  atomic technique with validation.

## Verify

Use the package and root tests after part changes:

```bash
python -m unittest tests.test_checkpoint_mechanics_topology
python scripts/validate_repo.py
```
