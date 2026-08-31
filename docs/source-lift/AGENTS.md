# AGENTS.md

## Applies to

This card applies to `docs/source-lift/` and all source-lift guide surfaces in
this district.

## Role

`docs/source-lift/` holds authored contracts for KAG-friendly source-lift
families and their bounded exports.

It does not own generated Markdown readers, generated JSON, technique bundle
meaning, KAG substrate authority, graph behavior, scoring, or sibling-repo
truth.

## Read before editing

Read root `AGENTS.md`, `docs/AGENTS.md`, `docs/ROOT_SURFACE_LAW.md`,
`docs/guardrails/THEMATIC_DISTRICT_PROTOCOL.md` before changing source-lift
contracts.

For generated reader output, also read `docs/readers/AGENTS.md` and the
matching reader guide for the family being moved or regenerated.

## Boundaries

- Keep authored source-lift contracts here and generated Markdown readers under
  `docs/readers/`.
- Keep generated JSON under `generated/`.
- Keep technique meaning in `techniques/**/TECHNIQUE.md` and bundle-local
  notes, checks, and examples.
- Do not turn source-lift guides into KAG graph doctrine, selection engines,
  execution policy, or proof verdicts.
- When moving a source-lift guide, update the builder/test links that generate
  the reader companion.

## Validation

Select the narrowest owner route: `source-fast` for source routes; add `generated` for declared projections. See [VALIDATION.md](../../VALIDATION.md); exact order is `config/validation_lanes.json`; focused procedure stays with the nearest owner. Report checks, skips, and blockers.

## Closeout

Report which source-lift family changed, which generated readers were rebuilt,
which JSON manifests stayed fresh, and whether any flat `docs/*.md` pressure
remains.
