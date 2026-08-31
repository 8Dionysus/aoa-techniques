# AGENTS.md

## Applies to

This card applies to `mechanics/release-support/legacy/` and every descendant unless a nearer
`AGENTS.md` narrows the path.

## Role

`legacy/` preserves Release Support source receipts and source-to-active
accounting. It is a provenance district, not the normal first route for current
mechanics edits.

## Read before editing

Read:

1. repository root `AGENTS.md`
2. `mechanics/AGENTS.md`
3. `mechanics/release-support/AGENTS.md`
4. `mechanics/release-support/PROVENANCE.md`
Read `README.md` only when the selected task needs its human map; do not preload unrelated maps.

## Boundaries

- Do not use raw legacy files as the normal first route for current edits.
- Do not make raw legacy files the only place current active behavior lives.
- Do not create placeholder source receipts; preserve only actual source packets.
- Start in `../README.md`, `../DIRECTION.md`, `../PARTS.md`, and `../parts/`
  for current behavior.
- Use `../PROVENANCE.md` as the active bridge into this district.
- Keep `INDEX.md`, `DISTILLATION_LOG.md`, and `raw/README.md` aligned.

## Validation

Select the narrowest owner route: `mechanics/part-local` for part-local work; add `source-fast` for authored routes or `generated` for projections. See [VALIDATION.md](../../../VALIDATION.md); exact order is `config/validation_lanes.json`; focused procedure stays with the nearest owner. Report checks, skips, and blockers.

## Closeout

Report the mechanic package, part, legacy surface, or helper changed;
whether source, generated, schema, example, or test surfaces moved; checks run;
checks skipped; and the next owner route.
