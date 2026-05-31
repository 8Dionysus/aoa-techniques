# Root Legacy Provenance District

Date: 2026-05-04

## Index Metadata

- Decision ID: AOA-TECH-D-0040
- Original date: 2026-05-04
- Surface classes: root/topology, legacy/provenance
- Technique axes: topology
- Mechanic parents: none
- Guard families: root surface, legacy/provenance
- Posture: accepted

## Status

Accepted

## Context

`aoa-techniques` is preparing to move from broad domain folders toward a
scalable technique tree. The repository also still has root-wide tail surfaces:
incoming wave packets, candidate material, pre-prune evidence, generated review
packets, and old route forms that may need preservation after active
distillation.

AoA mechanics already use local `legacy/` districts to preserve raw waves and
source-to-active accounting without making active mechanics carry every
historic packet. `aoa-techniques` has copied that pattern inside
`mechanics/<slug>/legacy/`, but it did not yet have a root-level district for
repo-wide preservation.

## Options

- Keep all repo-wide tail material in `incoming/` even after it stops being
  candidate quarantine.
- Preserve everything only under mechanic-local legacy directories.
- Add a root `legacy/` district for repo-wide public-safe raw, archive, and
  receipt material while keeping active technique bundles and mechanic-local
  lineage in their own homes.

## Decision

Add root `legacy/` with `raw/`, `archive/`, and `receipts/` subdirectories plus
an index and local route card.

Root legacy is a provenance and archive district. It is not a second
`incoming/`, not active technique canon, not a generated-output authority, and
not a replacement for mechanic-local legacy.

Technique tree migration should move active bundles directly from old authored
paths to new authored paths. Root legacy may preserve migration receipts and
pre-migration accounting, but active bundles should not pass through root
legacy as a staging path.

## Consequences

The tree reform can preserve history without letting old growth dictate the
new root architecture.

`incoming/` remains candidate quarantine and staging. `legacy/` becomes the
place for public-safe repo-wide history after, beside, or around active
distillation.

The tradeoff is one more root district. The guardrail is that every preserved
item must be indexed and mapped to an active route, owner route, or explicit
hold status.
