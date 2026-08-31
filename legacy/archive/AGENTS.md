# AGENTS.md

## Applies to

This card applies to `legacy/archive/`.

## Role

`legacy/archive/` preserves retired public-safe repo-wide surfaces whose active
route now lives elsewhere.

It is for auditability after a root, docs-root, incoming, or other repo-wide
tail surface stops being current. It is not a second current docs tree.

## Read before editing

Read:

1. `../AGENTS.md`
2. `../INDEX.md`
3. the current source surface that replaces the archived material

For the archived root-agent reference, also read `AGENTS_ROOT_REFERENCE.md`
before moving or summarizing it.
Read `README.md` only when the selected task needs its human map; do not preload unrelated maps.

## Boundaries

- Do not archive active source files without updating links, route docs, and
  `../INDEX.md`.
- Do not use this directory for mechanic-local lineage; use
  `../../mechanics/<slug>/legacy/` when one mechanic owns the history.
- Do not treat archived generated output as stronger than the generator or
  authored source.
- Do not store unreviewed candidate intake here; use
  `../../mechanics/distillation/parts/candidate-intake/`.
- Do not add archive material without naming the active replacement route or
  explicit hold status.

## Validation

Select the narrowest owner route: `source-fast` for the local owner; add `generated` for derived indexes and `advisory` only for non-blocking boundaries. See [VALIDATION.md](../../VALIDATION.md); exact order is `config/validation_lanes.json`; focused procedure stays with the nearest owner. Report checks, skips, and blockers.

## Closeout

Report archive files changed, the current replacement route, links updated,
`../INDEX.md` update, public-safe review, and checks run or skipped.
