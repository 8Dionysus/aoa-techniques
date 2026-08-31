# AGENTS.md

## Applies to

This card applies to `legacy/raw/`.

## Role

`legacy/raw/` preserves exact public-safe repo-wide source packets and
pre-prune snapshots after their current route has been distilled or explicitly
held.

It is not `incoming/`, not active technique canon, and not a mechanic-local raw
archive.

## Read before editing

Read:

1. `../AGENTS.md`
2. `../INDEX.md`
3. the active route or owner route the raw packet pressures

If the packet came from a technique-tree move, also read
`../../docs/TECHNIQUE_TREE_CONTRACT.md`.
Read `README.md` only when the selected task needs its human map; do not preload unrelated maps.

## Boundaries

- Do not add secrets, private transcripts, unreduced project dumps, host
  details, or raw logs.
- Do not use this directory as quarantine for unreviewed candidate material;
  use `../../mechanics/distillation/parts/candidate-intake/` when the material
  is still candidate intake.
- Do not add active technique bundles here.
- Do not add a raw packet without naming the active route, owner route, or
  explicit hold status it pressures.
- Do not leave `../INDEX.md` stale after adding, moving, or removing raw
  material.

## Validation

Select the narrowest owner route: `source-fast` for the local owner; add `generated` for derived indexes and `advisory` only for non-blocking boundaries. See [VALIDATION.md](../../VALIDATION.md); exact order is `config/validation_lanes.json`; focused procedure stays with the nearest owner. Report checks, skips, and blockers.

## Closeout

Report the raw packet changed, the active route or owner route it maps to,
public-safe review, `../INDEX.md` update, and checks run or skipped.
