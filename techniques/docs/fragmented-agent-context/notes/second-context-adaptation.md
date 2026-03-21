# Second Context Adaptation

## Technique
- id: AOA-T-0030
- name: fragmented-agent-context

## Target project
- name: aoa-techniques
- environment: public library repository with technique bundles, generated catalog surfaces, and explicit provenance-note discipline
- runtime: documentation-first repository that records the fragment-first authoring pattern rather than shipping the donor composition engine itself

## What changed

- paths: the donor uses smaller markdown fragments that can later compose into one generated context artifact; this adaptation keeps only the fragment-first authoring layer and presents it as a generic modular-source pattern
- services: no deterministic generator, JSON report command, or CI stack is required in this repository
- dependencies: the adaptation depends on bounded fragment scope, legible placement, and fragment-first editing rather than on one donor CLI
- operating assumptions: contributors should review fragment ownership directly and treat any later aggregate artifact as a separate downstream concern

## What stayed invariant

- contract: context is authored in smaller bounded fragments before any aggregate output is trusted
- validation logic: fragment scope and ownership remain visible to reviewers
- safety rules: fragments stay canonical and do not silently give way to a generated aggregate as the editable source of truth

## Risks introduced by adaptation

- the pattern can become vague if a project keeps many small files but loses the bounded scope that makes the fragments meaningful
- some repositories may over-fragment the context layer and create route friction without clearer ownership

## Evidence

- the donor README describes smaller context fragments as the scalable authoring layer
- the donor feature surface separates fragment authoring from composition, reporting, and migration helpers
- this imported technique narrows those behaviors into one reusable docs pattern for modular context sources before deterministic assembly

## Result

- works as a documentation-first second context and preserves the bounded core without carrying over donor-specific generator breadth
