# AGENTS.md

## Applies to

This card applies to the Audit mechanics package and every nested path under it
until a nearer `AGENTS.md` narrows the lane.

## Role

This package owns the technique-side Audit route inside `aoa-techniques`. It
keeps promotion pressure, evidence gaps, searched lanes, and canonical readiness
legible enough to choose the next honest move.

It does not own proof doctrine, eval authority, technique status flips without
bundle-local evidence, skill execution, routing, role contracts, memory
semantics, or runtime behavior.

## Source split

- `README.md`, `DIRECTION.md`, `PARTS.md`, and `parts/` own current active
  route.
- `PROVENANCE.md` is the active-first bridge back to pre-split evidence.
- `legacy/` preserves audit accounting and is the place for future raw
  receipts.

## Read before editing

1. Repository root `AGENTS.md`
2. `mechanics/AGENTS.md`
Read `README.md` only when the selected task needs its human map; do not preload unrelated maps.

## Boundaries

- Keep readiness queues distinct from bundle-local canonical evidence.
- If audit evidence changes a bundle's status readiness, update the bundle-local
  notes first, then shared queue surfaces.
- Do not let an external evidence lane become a donor-import workflow; route new
  extraction back to Distillation.
- Do not issue proof verdicts from this package. Audit may name blockers,
  searched lanes, and readiness posture.
- Generated artifacts remain evidence, not authority.

## Validation

Select the narrowest owner route: `mechanics/part-local` for part-local work; add `source-fast` for authored routes or `generated` for projections. See [VALIDATION.md](../../VALIDATION.md); exact order is `config/validation_lanes.json`; focused procedure stays with the nearest owner. Report checks, skips, and blockers.

## Closeout

Report which active parts changed, whether any legacy source was moved, which
validation ran, what was not moved, and where the next Audit pass should
resume.
