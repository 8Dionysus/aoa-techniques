# AGENTS.md

## Applies to

This card applies to the Distillation mechanics package and every nested path
under it until a nearer `AGENTS.md` narrows the lane.

## Role

This package owns the technique-side Distillation route inside
`aoa-techniques`. It turns donor pressure, cross-layer notes, and long-gap
material into reusable-practice candidates, holds, or import paths.

It does not own AoA center doctrine, skill execution, eval verdicts, routing
policy, role contracts, memory semantics, runtime behavior, ToS canon, or final
technique promotion.

## Source split

- `README.md`, `DIRECTION.md`, `PARTS.md`, and `parts/` own current active
  route.
- `PROVENANCE.md` is the active-first bridge back to donor and legacy evidence.
- `legacy/` preserves distillation accounting and is the place for future
  pre-prune receipts.
- `parts/candidate-intake/` owns active public-safe incoming packet quarantine;
  closed packet roots move to `legacy/archive/closed-incoming-packets/`.
- Archived incoming wave packets and sibling-repo donor notes are evidence
  surfaces; they do not become active law by appearing here.

## Read before editing

1. Repository root `AGENTS.md`
2. `mechanics/AGENTS.md`
Read `README.md` only when the selected task needs its human map; do not preload unrelated maps.
Nested parts also read this package's `PARTS.md` before the target local card.

## Boundaries

- Keep candidate ledgers distinct from promoted technique bundles.
- If a candidate becomes a stable reusable practice with inputs, outputs, risks,
  and validation, route it into `techniques/` through the normal bundle path.
- If a ledger is compacted, preserve the pre-pruned accounting in `legacy/raw/`
  or point to an explicit preserved source.
- Keep external donor wording sanitized and narrower than the donor's total
  worldview.
- Keep sibling-repo routes as provenance, not owner transfer.

Inherited mechanics boundary: do not override stronger sources; see [mechanics/AGENTS.md](../AGENTS.md#boundaries); local role remains above.

## Validation

Inherit [../AGENTS.md](../AGENTS.md#validation): `mechanics/part-local`; see [VALIDATION.md](../../VALIDATION.md) and `config/validation_lanes.json`. Local `mechanics/distillation/AGENTS.md`: package practice/owner stop-line.
## Closeout

Report which active parts changed, whether any legacy source was moved or
distilled, which validation ran, what was not moved, and where the next
Distillation pass should resume.
