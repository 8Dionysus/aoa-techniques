# AGENTS.md

## Applies to

This card applies to the Agon mechanics package and every nested path under it
until a nearer `AGENTS.md` narrows the lane.

## Role

This package owns the technique-side Agon route inside `aoa-techniques`.
It stages and constrains requested practice candidates, but it does not own Agon
doctrine, arena behavior, skill execution, proof verdicts, memory, routing, or
ToS canon.

## Source split

- `README.md`, `DIRECTION.md`, `PARTS.md`, and `parts/` own current active route.
- `PROVENANCE.md` is the active-first bridge to preserved wave sources.
- `legacy/` preserves raw Wave IV and Wave XV landing receipts.
- Part-local `config/`, `generated/`, `schemas/`, `examples/`, `scripts/`,
  `tests/`, and recurrence manifests own current Agon technical artifacts.

## Read before editing

1. Repository root `AGENTS.md`
2. `mechanics/AGENTS.md`
Read `README.md` only when the selected task needs its human map; do not preload unrelated maps.

## Boundaries

- Do not edit raw wave receipts to change current behavior.
- If a raw source changes current behavior, update the relevant active part
  first, then update `PROVENANCE.md`, `legacy/INDEX.md`, and `LANDING_LOG.md`.
- Keep requested candidates distinct from promoted technique bundles.
- Keep cross-repo boundaries explicit in every new route.

## Validation

Inherit [../AGENTS.md](../AGENTS.md#validation): `mechanics/part-local`; see [VALIDATION.md](../../VALIDATION.md) and `config/validation_lanes.json`. Local `mechanics/agon/AGENTS.md`: package practice/owner stop-line.
## Closeout

Report which active parts changed, whether any legacy source was moved or
distilled, which validation ran, what was not moved, and where the next Agon
pass should resume.
