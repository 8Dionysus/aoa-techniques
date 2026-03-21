# Second Context Adaptation

## Technique
- id: AOA-T-0025
- name: capability-spec-versioning

## Target project
- name: aoa-techniques
- environment: public technique repository with authored bundle contracts, review notes, generated routing surfaces, and validator-backed markdown discipline
- runtime: documentation-first corpus that records capability-contract meaning rather than shipping the donor runtime system

## What changed
- paths: the donor expresses capability specs inside a Ruby framework; this adaptation presents the same contract as a portable docs pattern without depending on the donor code layout
- services: provider registration, agent stores, and execution-history systems are removed from the reusable contract
- dependencies: the adaptation depends on one reviewable capability spec and explicit versioning, not on the donor runtime stack
- operating assumptions: contributors should read the technique as a public contract pattern for agent-facing capabilities, not as installation guidance for the donor product

## What stayed invariant
- contract: one named capability remains explicit through a versioned spec
- validation logic: inputs, outputs, and invariants stay reviewable at the spec layer before implementation drift accumulates
- safety rules: implementations stay subordinate, and the bundle does not widen into orchestration or registry semantics

## Risks introduced by adaptation
- the pattern can become vague if repositories copy the idea of a versioned capability but never record meaningful compatibility notes
- some teams may mistake a capability spec for a routing or registry object once the runtime system grows around it

## Evidence
- the donor `README.md` now explicitly describes a capability system with rich specification and versioning
- the same public README shows capability specifications, providers, composition, and retrieval as first-class concepts instead of burying capability meaning only in runtime code
- this imported technique narrows that public donor surface to one reusable contract: versioned capability specification as the reviewable capability boundary

## Result
- works as a documentation-first second context and preserves the bounded core without carrying over donor-specific orchestration, persistence, or learning breadth
