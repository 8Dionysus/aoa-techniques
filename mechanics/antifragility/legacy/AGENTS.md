# AGENTS.md

## Applies to

This card applies to `mechanics/antifragility/legacy/` and every descendant unless a nearer
`AGENTS.md` narrows the path.

## Role

This lane preserves pre-split antifragility source material. It is source
lineage, not the active operating route.

## Read before editing

Read:

1. repository root `AGENTS.md`
2. `mechanics/AGENTS.md`
3. `mechanics/antifragility/AGENTS.md`
4. `mechanics/antifragility/PROVENANCE.md`
5. `mechanics/antifragility/legacy/README.md` or the touched raw/receipt surface when present

## Boundaries

- Do not use raw legacy files as the normal first route for current edits.
- Do not make raw legacy files the only place current active behavior lives.
- Do not create placeholder source receipts; preserve only actual source packets.
- Keep raw donor or wave material in `raw/`.
- Use `INDEX.md` and `DISTILLATION_LOG.md` to explain how source material moved
  into active parts.
- Do not edit raw files to make them read like current law; add active distills
  or provenance notes instead.

## Validation

After legacy changes, run:

```bash
python -m unittest discover -s mechanics/antifragility/tests
python scripts/validate_repo.py
```

## Closeout

Report the mechanic package, part, legacy surface, or helper changed;
whether source, generated, schema, example, or test surfaces moved; checks run;
checks skipped; and the next owner route.
