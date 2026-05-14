# AGENTS.md

Route card for `mechanics/recurrence/parts/`.

## Purpose

Each part owns one bounded local recurrence route for `aoa-techniques`.
Parts describe observation and closure movement around technique canon; they do
not become canonical technique bundles.

## Local law

- Keep part docs concise and owner-bounded.
- Preserve links to `PROVENANCE.md` when moving or compacting source material.
- Keep generated surfaces, manifests, live receipts, and readiness payloads as
  evidence only.
- Route execution, proof, memory, runtime, role, route, SDK carry, KAG, stats,
  and playbook meaning to the owning repository.
- Promote into `techniques/` only when the reusable practice can stand as an
  atomic technique with validation.

## Verify

Use the package and root tests after part changes:

```bash
python -m unittest discover -s mechanics/recurrence/tests
python scripts/validate_repo.py
```
