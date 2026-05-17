# AGENTS.md

## Applies to

This card applies to Distillation active parts until a nearer `AGENTS.md`
narrows the lane.

## Role

Each child directory owns one active Distillation part. Part READMEs are current
operating surfaces, not raw donor archives.

## Read before editing

Read:

1. repository root `AGENTS.md`
2. `mechanics/AGENTS.md`
3. `mechanics/distillation/AGENTS.md`
4. `mechanics/distillation/PARTS.md`
5. the touched part README, schema, example, script, report, or test

## Boundaries

- Keep part changes bounded to that part's role.
- Update `../PARTS.md` when a part is added, renamed, or retired.
- Update `../PROVENANCE.md` when source evidence changes the part's behavior.
- Preserve pre-prune source accounting in `../legacy/raw/` before shortening a
  ledger.
- Do not promote a candidate into `techniques/` from inside a part without the
  normal bundle evidence and validation path.

## Validation

```bash
python -m unittest discover -s mechanics/distillation/tests
python scripts/validate_repo.py
```

## Closeout

Report the mechanic package, part, legacy surface, or helper changed;
whether source, generated, schema, example, or test surfaces moved; checks run;
checks skipped; and the next owner route.
