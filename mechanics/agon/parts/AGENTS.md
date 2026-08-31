# AGENTS.md

## Applies to

This card applies to `mechanics/agon/parts/` and every descendant unless a nearer
`AGENTS.md` narrows the path.

## Role

Part directories own active Agon technique-side behavior. They do not preserve
raw wave receipts and they do not author Agon center doctrine.

## Read before editing

Read:

1. repository root `AGENTS.md`
2. `mechanics/AGENTS.md`
3. `mechanics/agon/AGENTS.md`
4. `mechanics/agon/PARTS.md`
Read `README.md` only when the selected task needs its human map; do not preload unrelated maps.

## Boundaries

- Keep each part focused on one current behavior.
- Route historical wave detail through `../PROVENANCE.md` and `../legacy/`.
- Keep generated candidate indexes subordinate to their source seeds and stop
  lines.
- Do not promote candidates into techniques from a part README.

## Validation

Select the narrowest owner route: `mechanics/part-local` for part-local work; add `source-fast` for authored routes or `generated` for projections. See [VALIDATION.md](../../../VALIDATION.md); exact order is `config/validation_lanes.json`; focused procedure stays with the nearest owner. Report checks, skips, and blockers.

## Closeout

Report the mechanic package, part, legacy surface, or helper changed;
whether source, generated, schema, example, or test surfaces moved; checks run;
checks skipped; and the next owner route.
