# AGENTS.md

## Applies to

This card applies to Experience active parts until a nearer `AGENTS.md` narrows
the lane.

## Role

Each child directory owns one active Experience part. Part READMEs are current
operating surfaces, not raw seed archives.

## Read before editing

Read:

1. repository root `AGENTS.md`
2. `mechanics/AGENTS.md`
3. `mechanics/experience/AGENTS.md`
4. `mechanics/experience/PARTS.md`
5. the touched part README, schema, example, script, report, or test

## Boundaries

- Keep part changes bounded to that part's role.
- Update `../PARTS.md` when a part is added, renamed, or retired.
- Update `../PROVENANCE.md` when source evidence changes the part's behavior.
- Do not promote a part into `techniques/` without the normal bundle evidence
  and validation path.
- Do not turn a practice note into live office, release, runtime, proof, or ToS
  authority.

## Validation

```bash
python -m unittest discover -s mechanics/experience/tests
python scripts/validate_repo.py
```

## Closeout

Report the mechanic package, part, legacy surface, or helper changed;
whether source, generated, schema, example, or test surfaces moved; checks run;
checks skipped; and the next owner route.
