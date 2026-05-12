# Adverse Effects Review

## Technique
- id: AOA-T-0025
- name: capability-spec-versioning

## Review focus
- current role: canonical default for keeping one agent-facing capability contract explicit, versioned, and reviewable at the spec layer
- current watch seam: keep the bundle centered on capability contract versioning rather than registry lifecycle, routing policy, orchestration, provider implementation detail, or protocol-platform breadth

## Failure modes
- version numbers change without compatibility review, making versions decorative rather than contractual
- implementation behavior drifts while the spec remains unchanged and still appears authoritative
- capability docs absorb provider, registry, or orchestration details until the stable contract is hard to find
- clients or downstream readers treat the spec as proof that every optional capability can safely be used without checking declared support

## Negative effects
- canonical status can add spec ceremony to unstable prototypes that need experimentation more than versioned contracts
- contract wording can slow iteration if every implementation detail is forced through the spec surface
- a strong spec can make unsupported or partially supported implementations look more compatible than they are
- versioned specs can tempt teams to solve routing or registry problems in the wrong file

## Misuse patterns
- widening the capability spec into registry product doctrine, marketplace discovery, or plan orchestration
- changing versions as release labels without naming contract-level compatibility effects
- burying invariants behind provider-specific code examples
- treating one protocol's agent card, capability declaration, or implementation shape as universal schema law

## Detection signals
- reviewers cannot explain what a version change means without reading implementation diffs
- compatibility notes disappear while version fields keep changing
- capability docs spend more space on routing, registry storage, provider adapters, or execution history than on inputs, outputs, and invariants
- downstream consumers call optional capability paths without validating declared support first

## Mitigations
- keep the spec small enough to name purpose, version, inputs, outputs, and invariants in reviewable language
- require compatibility notes when version changes affect consumers
- keep implementations, providers, and protocol adapters subordinate to the contract
- split registry lifecycle, routing, orchestration, discovery, and compatibility-matrix policy into sibling techniques
- revisit canonical status if versioning becomes release branding rather than a real contract seam

## Recommendation
- keep current `canonical` status and use this note as the watch surface for version ceremony, spec/implementation drift, registry overreach, and hidden optional-capability assumptions
