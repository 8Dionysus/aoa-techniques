# AGENTS.md

Route card for `aoa-techniques/mechanics/distillation/parts/`.

## Applies to

This card applies to Distillation active parts until a nearer `AGENTS.md`
narrows the lane.

## Role

Each child directory owns one active Distillation part. Part READMEs are current
operating surfaces, not raw donor archives.

## Editing posture

- Keep part changes bounded to that part's role.
- Update `../PARTS.md` when a part is added, renamed, or retired.
- Update `../PROVENANCE.md` when source evidence changes the part's behavior.
- Preserve pre-prune source accounting in `../legacy/raw/` before shortening a
  ledger.
- Do not promote a candidate into `techniques/` from inside a part without the
  normal bundle evidence and validation path.

## Verify

```bash
python -m unittest tests.test_distillation_mechanics_topology
python scripts/validate_repo.py
```
