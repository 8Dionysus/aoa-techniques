# Split Mechanics Surfaces From General Docs

Status: accepted
Date: 2026-05-01

## Index Metadata

- Decision ID: AOA-TECH-D-0013
- Original date: 2026-05-01
- Surface classes: mechanic package
- Technique axes: mechanic bridge
- Mechanic parents: none
- Guard families: mechanic topology
- Posture: accepted

## Context

`aoa-techniques` had a large set of mechanics-shaped files mixed into the flat
`docs/` directory. They described donor intake, promotion readiness, adoption,
mastery, Agon/recurrence bridges, experience precedents, release-support
surfaces, and stress-program routes.

Those files were not ordinary docs and were not canonical technique bundles.
They encoded movement grammar: how practice candidates are captured, refined,
reviewed, handed off, and bounded by owner stop-lines. Keeping them in the same
flat surface as selection guides, review guides, and generated-reader docs made
the repository harder to navigate and obscured the role of mechanics in the AoA
ecosystem.

## Decision

Create `mechanics/` as a first-class owner-local surface for reusable practice
motion around technique canon, and align its top-level package names with the
cross-project AoA mechanics vocabulary rather than only with local document
clusters.

The initial split groups existing surfaces into cross-mechanic packages:

- `mechanics/distillation/`
- `mechanics/audit/`
- `mechanics/method-growth/`
- `mechanics/growth-cycle/`
- `mechanics/agon/`
- `mechanics/recurrence/`
- `mechanics/experience/`
- `mechanics/release-support/`
- `mechanics/antifragility/`

The repository keeps `docs/` for orientation, review doctrine, selection
guidance, release guidance, and generated-reader interpretation. Published
practice units remain under `techniques/`.

## Consequences

- Future mechanics-shaped material should land under the nearest cross-project
  mechanic first, with a package README and explicit stop-lines.
- Repo-local mechanics can exist, but only when they are explicitly justified
  against the cross-project mechanic map.
- Existing path references, tests, manifests, and quest surfaces must point at
  the new mechanics paths.
- Mechanics may stage or constrain promotion, but they do not become promotion
  authority on their own.
- If a mechanics surface matures into a reusable practice bundle, it should move
  through the normal technique review path into `techniques/`.
