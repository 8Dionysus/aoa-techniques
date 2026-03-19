# Origin Evidence

## Technique
- id: AOA-T-0021
- name: bounded-relation-lift-for-kag

## Source project
- name: aoa-techniques
- source files:
  - `generated/technique_catalog.json`
  - `docs/TECHNIQUE_SELECTION.md`
  - `docs/SELECTION_PATTERNS.md`
  - `docs/BOUNDED_RELATION_LIFT_GUIDE.md`

## Evidence
- `generated/technique_catalog.json` already carries the current direct typed relation layer as derived metadata
- `docs/TECHNIQUE_SELECTION.md` and `docs/SELECTION_PATTERNS.md` already use those relations for bounded navigation rather than for graph inference
- `docs/BOUNDED_RELATION_LIFT_GUIDE.md` explicitly keeps relation rationale, weighting, and multi-hop semantics out of the current edge layer

## Interpretation
- the repository already proves that a small direct-edge vocabulary can help navigation without turning into a graph platform
- the reusable technique is the bounded relation lift itself, not any promise of future graph behavior
