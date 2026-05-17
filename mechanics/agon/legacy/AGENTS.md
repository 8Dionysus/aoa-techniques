# AGENTS.md

## Applies to

This card applies to `mechanics/agon/legacy/` and every descendant unless a nearer
`AGENTS.md` narrows the path.

## Role

`legacy/` preserves Agon wave source receipts that are too historical or heavy
for the active route. It is not a trash archive and not the normal first route
for current edits.

## Read before editing

Read:

1. repository root `AGENTS.md`
2. `mechanics/AGENTS.md`
3. `mechanics/agon/AGENTS.md`
4. `mechanics/agon/PROVENANCE.md`
5. `mechanics/agon/legacy/README.md` or the touched raw/receipt surface when present

## Boundaries

- Do not use raw legacy files as the normal first route for current edits.
- Do not make raw legacy files the only place current active behavior lives.
- Do not create placeholder source receipts; preserve only actual source packets.
- Do not delete raw wave receipts after distillation.
- When a raw source affects current behavior, update the active part first.
- Keep `INDEX.md` and `DISTILLATION_LOG.md` aligned with any new preserved
  source.

## Validation

Run the owning Agon checks when legacy changes affect active candidate routes
or validation posture:

```bash
python -m unittest discover -s mechanics/agon/tests
python scripts/validate_repo.py
```

## Closeout

Report the mechanic package, part, legacy surface, or helper changed;
whether source, generated, schema, example, or test surfaces moved; checks run;
checks skipped; and the next owner route.
