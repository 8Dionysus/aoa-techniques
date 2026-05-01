# AGENTS.md

Route card for `aoa-techniques/mechanics/audit/parts/`.

## Applies to

This card applies to Audit active parts until a nearer `AGENTS.md` narrows the
lane.

## Role

Each child directory owns one active Audit part. Part READMEs are current
operating surfaces, not raw archives.

## Editing posture

- Keep part changes bounded to that part's role.
- Update `../PARTS.md` when a part is added, renamed, or retired.
- Update `../PROVENANCE.md` when source evidence changes the part's behavior.
- Preserve pre-prune source accounting in `../legacy/raw/` before shortening a
  ledger or runbook.
- Do not change technique status from inside a part without bundle-local
  canonical evidence and the normal validation path.

## Verify

```bash
python -m unittest tests.test_audit_mechanics_topology
python scripts/validate_repo.py
```
