# Second Context Adaptation

## Technique
- id: AOA-T-0029
- name: nested-rule-loading

## Target project
- name: aoa-techniques
- environment: public library repository with technique bundles, generated catalog surfaces, and explicit provenance-note discipline
- runtime: documentation-first repository that records the nested-loading pattern rather than shipping the donor loader itself

## What changed

- paths: the donor supports layered rule loading with explicit precedence; this adaptation presents that hierarchy as a generic public technique with one canonical source and subordinate nested layers
- services: no MCP propagation, installer integration, or skills propagation is required in this repository
- dependencies: the adaptation depends on declared source ownership, nested layer precedence, and repeatable loading, not on the donor CLI breadth
- operating assumptions: contributors should treat nested layers as scoped additions and keep local wrapper notes visibly separate

## What stayed invariant

- contract: one canonical source owns the shared meaning
- validation logic: nested layers remain subordinate to the canonical source through explicit precedence
- safety rules: local nested layers do not silently become new canonical homes

## Risks introduced by adaptation

- the pattern can become vague if a project adds nested layers but drops the canonical source as the actual ownership authority
- some repositories may keep layered files but stop treating precedence as part of the real contract

## Evidence

- the donor `README.md` describes hierarchical rule behavior with explicit precedence in the broader rule system
- the public contract can be narrowed to nested loading without carrying over the rest of the donor breadth
- this imported technique keeps the core at hierarchy plus precedence, which is reusable across repositories that layer rule sources

## Result

- works as a documentation-first second context and preserves the bounded core without carrying over donor-specific product breadth
