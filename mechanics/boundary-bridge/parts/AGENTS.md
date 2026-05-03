# AGENTS.md

Route card for `mechanics/boundary-bridge/parts/`.

## Purpose

Each part owns one bounded local boundary-bridge route for `aoa-techniques`.
Parts describe movement around technique canon; they do not become canonical
technique bundles or cross-owner authority.

## Local law

- Keep part docs concise and owner-bounded.
- Preserve links to `PROVENANCE.md` when moving, staging, or compacting source
  material.
- Keep ToS meaning, KAG projection truth, route behavior, memory, proof,
  scenario choreography, compatibility, runtime, public projection, and owner
  acceptance with their owning repositories.
- Promote into `techniques/` only when the reusable practice can stand as an
  atomic technique with validation.

## Verify

Use the package and root tests after part changes:

```bash
python -m unittest tests.test_boundary_bridge_mechanics_topology
python scripts/validate_repo.py
```
