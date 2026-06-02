# Thematic District Protocol

This protocol keeps `docs/` readable as the technique canon grows.

`docs/` root may hold current repo doctrine, route contracts, active reader
maps, generated-reader interpretation, and release guidance. It must not become
a flat archive of every migration breadcrumb, review packet, family ledger, or
mechanic-local operating note.

## Current Districts

| District | Role |
|---|---|
| `docs/guardrails/` | checkable docs guardrails, current-surface index, AGENTS mesh law, and route-shape validation posture |
| `docs/decisions/` | decision records explaining why a structural, ownership, workflow, route-law, validator, or topology choice was made |
| `docs/review/` | active review, maturity, semantic-review, and caution contracts for technique canon interpretation |
| `docs/selection/` | active selection, kind, handoff, and capsule guide contracts |
| `docs/source-lift/` | authored KAG/source-lift contracts whose generated readers and JSON outputs live elsewhere |
| `docs/validation/` | active validation lane topology, command authority, and validator inventory |
| `docs/readers/` | generated Markdown reader companions whose authored contracts stay in a current docs district |
| `legacy/` | repo-wide public-safe raw, archive, and migration receipt material after active distillation |
| `mechanics/<slug>/` | mechanic-owned runbooks, reviews, parts, landing logs, provenance, and mechanic-local legacy |
| `generated/` | reproducible generated JSON and compact machine-facing companions |
| `techniques/**/` | authored technique bundle truth |

Do not create a new docs district just because a file is awkward. Add a docs
district only when it has a durable role, local route guidance, tests or
validation pressure, and a clear owner boundary.

## Flat Docs Rule

A flat `docs/*.md` file must be able to answer why it is current route guidance
or active repo doctrine.

Allowed flat-doc roles:

- docs-local agent route card
- human docs map
- repo-owned self-serve entrypoint
- root/docs placement law
- active technique-canon contract
- active generated reader companion whose builder and validator keep it derived,
  until its family has a named `docs/readers/` district
- release route
- explicit compatibility reference named by a stronger route card

If the file is historical evidence, movement accounting, a mechanic packet, a
review ledger, a raw receipt, a retired route, or a stale baseline, it needs a
named owner home rather than equal standing in flat `docs/`.

## Reader Companion Rule

Generated Markdown reader companions may stay under `docs/` only while all of
these are true:

- the source remains authored markdown, config, schema, or generated JSON owned
  elsewhere
- the file says it is generated or derived when appropriate
- a builder or validator can reproduce or check it
- the reader routes back to source truth instead of replacing it
- [Current Surface Index](CURRENT_SURFACE_INDEX.md) names its role
- when moved under `docs/readers/`, the reader has local route guidance and
  links relative to that district

Generated JSON belongs in `generated/`. Generated Markdown readers are not source authority
just because humans can read them.

## Review Guide Rule

Review, maturity, semantic-review, and shadow/caution guide contracts belong in
`docs/review/` once the family has more than one active guide.

The district keeps review contracts discoverable without making them equal to
atom, topology, or tree law in flat `docs/`. Review packets themselves still
belong with the owning mechanic, generated readers still belong under
`docs/readers/`, and generated manifests still belong under `generated/`.

## Selection Guide Rule

Selection, kind, handoff, and capsule guide contracts belong in
`docs/selection/` once those guides form a real chooser and compact-use family.

The district keeps selector contracts discoverable without making them equal to
atom, topology, or tree law in flat `docs/`. Generated reader companions still
belong under `docs/readers/`, and generated JSON still belongs under
`generated/`.

## Source-Lift Guide Rule

KAG/source-lift guide contracts belong in `docs/source-lift/` once more than one
family exists.

The district keeps repeated section/checklist/example/evidence-note guidance
out of flat `docs/` while preserving active authored contracts. Generated
reader companions still belong under `docs/readers/`, and generated JSON still
belongs under `generated/`.

## Split Rule

When a current contract also carries old migration accounting, split by role:

- current law stays in the active contract
- migration receipts go to `legacy/receipts/` or the owning mechanic ledger
- full review trails stay in the owning mechanic review surface
- durable rationale stays in `docs/decisions/`
- generated parity stays with builders and validators

The active contract should point to the evidence trail; it should not become the
evidence trail.

## Promotion Rule

A historical or mechanic-owned surface may influence current law only through an
explicit promotion path:

1. name the surviving current source surface
2. preserve provenance in the owner route
3. update links and generated mirrors when they are consumers
4. update tests or validators that enforce the route
5. record a decision when future maintainers need to know why

## Check Route

Use [AGENTS](AGENTS.md) for local owner checks and
[`config/validation_lanes.json`](../../config/validation_lanes.json) for full
lane command authority. At minimum, docs-topology changes should keep
[Current Surface Index](CURRENT_SURFACE_INDEX.md) aligned with flat docs files.
