# AGENTS.md

Route card for `mechanics/antifragility/parts/`.

## Purpose

Each part owns one bounded local antifragility route for `aoa-techniques`.
Parts describe movement around technique canon; they do not become canonical
technique bundles, proof verdicts, health scores, or cleanup authority.

## Local law

- Keep part docs concise and owner-bounded.
- Preserve links to `PROVENANCE.md` when moving or compacting source material.
- Keep doctrine, via negativa, fragile-pattern source truth, proof, memory,
  stats, playbooks, routing, runtime recovery, and owner cleanup with their
  owning repositories.
- Promote into `techniques/` only when the reusable practice can stand as an
  atomic technique with validation.

## Verify

Use the package and root tests after part changes:

```bash
python -m unittest discover -s mechanics/antifragility/tests
python scripts/validate_repo.py
```
