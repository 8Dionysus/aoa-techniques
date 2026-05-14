# AGENTS.md

Route card for `mechanics/growth-cycle/parts/`.

## Purpose

Each part owns one bounded local Growth-cycle route for `aoa-techniques`.
Parts describe movement around technique canon; they do not become canonical
technique bundles.

## Local law

- Keep part docs concise and owner-bounded.
- Preserve links to `PROVENANCE.md` when moving or compacting source material.
- Route executable workflow, proof, memory, runtime, role, route, and playbook
  meaning to the owning repository.
- Promote into `techniques/` only when the reusable practice can stand as an
  atomic technique with validation.

## Verify

Use the package and root tests after part changes:

```bash
python -m unittest discover -s mechanics/growth-cycle/tests
python scripts/validate_repo.py
```
