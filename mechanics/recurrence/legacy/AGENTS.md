# AGENTS.md

## Applies to

This card applies to `mechanics/recurrence/legacy/` and every descendant unless a nearer
`AGENTS.md` narrows the path.

## Role

`legacy/` preserves Recurrence source receipts and source-to-active
accounting. It is a provenance district, not the normal first route for current
mechanics edits.

## Read before editing

Read:

1. repository root `AGENTS.md`
2. `mechanics/AGENTS.md`
3. `mechanics/recurrence/AGENTS.md`
4. `mechanics/recurrence/PROVENANCE.md`
5. `mechanics/recurrence/legacy/README.md` or the touched raw/receipt surface when present

## Boundaries

- Do not use raw legacy files as the normal first route for current edits.
- Do not make raw legacy files the only place current active behavior lives.
- Do not create placeholder source receipts; preserve only actual source packets.
- Start in `../README.md`, `../DIRECTION.md`, `../PARTS.md`, and `../parts/`
  for current behavior.
- Use `../PROVENANCE.md` as the active bridge into this district.
- Keep `INDEX.md`, `DISTILLATION_LOG.md`, and `raw/README.md` aligned.

## Validation

Run:

```bash
python -m unittest discover -s mechanics/recurrence/tests
```

## Closeout

Report the mechanic package, part, legacy surface, or helper changed;
whether source, generated, schema, example, or test surfaces moved; checks run;
checks skipped; and the next owner route.
