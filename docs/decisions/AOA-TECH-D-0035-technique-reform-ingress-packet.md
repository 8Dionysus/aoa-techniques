# Technique Reform Ingress Packet

Date: 2026-05-03

## Index Metadata

- Decision ID: AOA-TECH-D-0035
- Original date: 2026-05-03
- Surface classes: docs route
- Technique axes: source-lift
- Mechanic parents: none
- Guard families: docs route
- Posture: accepted

## Status

Accepted.

## Context

`aoa-techniques` now has an explicit atom contract, topology contract, kind
registry, family scout seed, generated family reports, and kind ambiguity
audit. The Agon candidate handoff added a fresh pressure point: several useful
candidate labels are real topology cues but not valid current `kind` values.

Without an ingress packet, the next classification reform could jump straight
from scattered evidence into schema changes, broad frontmatter migration, or
new kind values.

## Decision

Create `mechanics/distillation/parts/technique-reform-ingress/` as the
Distillation-owned entry packet for future technique classification reform.

The part gathers the current corpus contour, the authoritative topology
contracts, scout reports, kind ambiguity evidence, and Agon frontier evidence
into one route. It makes the first reform pass a bounded ingress problem rather
than a schema migration by default.

## Alternatives

- Put this only in `docs/TECHNIQUE_TOPOLOGY_CONTRACT.md`.
  Rejected because the topology contract is law and design doctrine; this packet
  is a movement surface for entering a future reform pass.
- Put this only in root `ROADMAP.md`.
  Rejected because the roadmap should name direction and triggers, not carry
  reform checklists and evidence routing.
- Start directly with schema or template changes.
  Rejected because the current evidence supports scout/generated projections
  first, not required bundle-wide fields.

## Consequences

- Future classification reform has one entry route before touching schema,
  templates, validators, or bulk frontmatter.
- Distillation remains the movement layer; authored docs, config, schema,
  generated surfaces, and bundle meaning still own their respective truths.
- `family`, `capability_class`, `substrate`, `execution_profile`, and
  `risk_posture` can be prepared as reviewed/scout projections before becoming
  required frontmatter.
- Agon handoff cues remain evidence for topology pressure, not authority to add
  new `kind` values.
- The ingress route prevents generated evidence from remapping bundle meaning
  automatically.

## Verification

Expected checks:

Verification was routed through the targeted owner checks and repository validation lanes.
