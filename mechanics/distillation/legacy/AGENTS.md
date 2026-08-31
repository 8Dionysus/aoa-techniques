# AGENTS.md

## Applies to

This card applies to preserved Distillation lineage and future raw receipts.

## Role

`legacy/` preserves accounting for raw-to-active Distillation movement. It is
not the active operating contract.

## Read before editing

Read:

1. repository root `AGENTS.md`
2. `mechanics/AGENTS.md`
3. `mechanics/distillation/AGENTS.md`
4. `mechanics/distillation/PROVENANCE.md`
Read `README.md` only when the selected task needs its human map; do not preload unrelated maps.

## Boundaries

- Do not use raw legacy files as the normal first route for current edits.
- Do not make raw legacy files the only place current active behavior lives.
- Do not create placeholder source receipts; preserve only actual source packets.
- Do not change a legacy receipt to alter current behavior.
- If a legacy source changes current behavior, update the active part first.
- Record any new raw preservation in `INDEX.md` and `DISTILLATION_LOG.md`.
- Keep raw receipts public-safe before adding them here.

## Validation

Select the narrowest owner route: `mechanics/part-local` for part-local work; add `source-fast` for authored routes or `generated` for projections. See [VALIDATION.md](../../../VALIDATION.md); exact order is `config/validation_lanes.json`; focused procedure stays with the nearest owner. Report checks, skips, and blockers.

## Closeout

Report the mechanic package, part, legacy surface, or helper changed;
whether source, generated, schema, example, or test surfaces moved; checks run;
checks skipped; and the next owner route.
