# Second Context Adaptation

## Technique
- id: AOA-T-0027
- name: cross-agent-skill-propagation

## Target project
- name: aoa-techniques
- environment: public library repository with technique bundles, generated catalog surfaces, and explicit provenance-note discipline
- runtime: documentation-first repository that records the propagation pattern rather than shipping the donor distribution engine itself

## What changed

- paths: the donor uses one canonical source directory plus managed agent-facing targets; this adaptation presents a generic source-to-target propagation pattern that can fit other curated collections
- services: no MCP propagation, installer integration, or registry generator is required in this repository
- dependencies: the adaptation depends on declared source ownership, repeatable propagation, and adjacent managed targets, not on the donor CLI
- operating assumptions: contributors should treat managed targets as derived outputs and keep local wrapper notes visibly separate

## What stayed invariant

- contract: one canonical skill or rule source declares the shared meaning
- validation logic: managed targets remain traceable to that source through repeatable propagation
- safety rules: local copies stay subordinate to the canonical source and do not silently become new canonical homes

## Risks introduced by adaptation

- the pattern can become vague if a project copies managed targets but drops the canonical source as the actual propagation authority
- some repositories may keep target files but stop treating the source as the real contract owner

## Evidence

- the donor `README.md` describes one canonical source plus automatic distribution to multiple agent-facing outputs
- the public tests show repeated application without duplicating shared instructions in managed targets
- this imported technique narrows those behaviors into one reusable docs pattern for skill or rule propagation with managed outputs

## Result

- works as a documentation-first second context and preserves the bounded core without carrying over donor-specific product breadth
