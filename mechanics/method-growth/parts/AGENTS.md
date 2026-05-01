# AGENTS.md

Route card for `aoa-techniques/mechanics/method-growth/parts/`.

## Applies to

This card applies to Method-growth active parts until a nearer `AGENTS.md`
narrows the lane.

## Role

Each child directory owns one active Method-growth part. Part READMEs are
current operating surfaces, not raw adoption-wave archives.

## Editing Posture

- Keep part changes bounded to that part's role.
- Update `../PARTS.md` when a part is added, renamed, or retired.
- Update `../PROVENANCE.md` when source evidence changes the part's behavior.
- Do not promote a part into `techniques/` without the normal bundle evidence
  and validation path.
- Do not treat technique-to-skill handoff as skill acceptance.

## Verify

```bash
python -m unittest tests.test_method_growth_mechanics_topology
python scripts/validate_repo.py
```
