# AGENTS.md

Route card for `aoa-techniques/mechanics/experience/parts/`.

## Applies to

This card applies to Experience active parts until a nearer `AGENTS.md` narrows
the lane.

## Role

Each child directory owns one active Experience part. Part READMEs are current
operating surfaces, not raw seed archives.

## Editing Posture

- Keep part changes bounded to that part's role.
- Update `../PARTS.md` when a part is added, renamed, or retired.
- Update `../PROVENANCE.md` when source evidence changes the part's behavior.
- Do not promote a part into `techniques/` without the normal bundle evidence
  and validation path.
- Do not turn a practice note into live office, release, runtime, proof, or ToS
  authority.

## Verify

```bash
python -m unittest discover -s mechanics/experience/tests
python scripts/validate_repo.py
```
