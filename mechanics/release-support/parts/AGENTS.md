# AGENTS.md

Route card for `mechanics/release-support/parts/`.

## Purpose

Each part owns one bounded local release-support route for `aoa-techniques`.
Parts describe movement around technique canon; they do not become canonical
technique bundles or release authority.

## Local law

- Keep part docs concise and owner-bounded.
- Preserve links to `PROVENANCE.md` when moving or compacting source material.
- Keep release claims, public claims, proof, runtime, routing, SDK, stats,
  profile projection, and owner acceptance with their owning repositories.
- Promote into `techniques/` only when the reusable practice can stand as an
  atomic technique with validation.

## Verify

Use the package and root tests after part changes:

```bash
python -m unittest discover -s mechanics/release-support/tests
python scripts/validate_repo.py
```
