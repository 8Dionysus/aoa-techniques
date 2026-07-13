# Technique Reform Scout Input Homes

Status: accepted

Date: 2026-05-14

## Index Metadata

- Decision ID: AOA-TECH-D-0056
- Original date: 2026-05-14
- Surface classes: mechanic part
- Technique axes: source-lift
- Mechanic parents: none
- Guard families: part-local artifact
- Posture: accepted

## Context

After moving the generated technique-reform reports into the Distillation
`technique-reform-ingress` part, root `config/` and `data/` still carried
scout-only inputs for the same part:

- `technique_family_scout.yaml`
- `technique_topology_axes.yaml`
- `technique_kind_overlay.yaml`
- `technique_kind_overlay.csv`

These files feed family, topology, kind-ambiguity, and tree-projection review
reports. They are not frontmatter truth, not schema truth, and not automatic
remap authority. Root `config/technique_kind_registry.yaml` is different: it is
the current repo-wide `kind` registry and remains a root config contract.

## Decision

Move scout-only technique-reform inputs into the owning Distillation part:

- `mechanics/distillation/parts/technique-reform-ingress/config/`
- `mechanics/distillation/parts/technique-reform-ingress/data/`

Update builders, validators, docs, generated source maps, and tests to load the
family scout, topology axes registry, and kind overlay from the part-local
paths. Keep `config/technique_kind_registry.yaml` in root as the repo-wide kind
contract.

## Consequences

- Root `config/` stays focused on repo-wide configuration contracts.
- Root `data/` no longer holds the mechanic-local overlay; a later topology
  decision retires the empty root district instead of keeping a placeholder
  without an active repo-wide data contract.
- The technique-reform part now owns the full scout loop: input config, overlay
  data, generated reports, review packets, and landing provenance.
- Future scout-only reform inputs should be added under the
  `technique-reform-ingress` part unless they become repo-wide contracts through
  a separate decision.

## Verification

Verification was routed through the targeted owner checks and repository validation lanes.
