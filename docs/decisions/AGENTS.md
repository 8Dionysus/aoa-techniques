# AGENTS.md

## Applies to

This card applies to `docs/decisions/` and all descendants unless a nearer
`AGENTS.md` narrows the path.

## Role

`docs/decisions/` holds decision records for meaningful `aoa-techniques`
structure, ownership, workflow, route-law, validator, public-contract, and
topology choices.

Decision records explain why a path was chosen. Current source surfaces define
what the repository now does.

## Read before editing

`docs/ROOT_SURFACE_LAW.md`, this file, and `TEMPLATE.md`.

Also read the source surfaces that the decision affects, such as root docs,
mechanic package cards, generated-source builders, validators, tests, or
technique contracts.

`indexes/index_contract.yaml`.
Read `README.md` only when the selected task needs its human map; do not preload unrelated maps.

## Boundaries

- Do not treat this district as stronger than its source surfaces.
- Do not use a decision record to duplicate a roadmap, changelog, landing log,
  runbook, generated manifest, or mechanic ledger.
- Keep options, rationale, consequences, source surfaces, and follow-up route
  explicit.
- Route mechanic-local truth to `mechanics/<slug>/`.
- Route technique meaning to `techniques/**/TECHNIQUE.md`.
- Route sibling-owner truth to the owning AoA repository.
- Keep `modeled_surfaces` in `indexes/index_contract.yaml` as a top-level list
  of normalized repo-relative paths under `docs/decisions/`; do not use it for
  root non-record Markdown.

## Validation

Select the narrowest owner route: `source-fast` for source routes; add `generated` for declared projections. See [VALIDATION.md](../../VALIDATION.md); exact order is `config/validation_lanes.json`; focused procedure stays with the nearest owner. Report checks, skips, and blockers.

## Closeout

Report the decision records changed, the source surfaces consulted, whether the
record explains why rather than replacing current law, which generated mirrors
were rebuilt or checked, and which validators ran.
