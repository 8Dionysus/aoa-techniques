# Adverse Effects Review

## Technique
- id: AOA-T-0013
- name: single-source-rule-distribution

## Review focus
- current role: canonical default for one local canonical rule source fanning out to multiple managed agent-facing instruction targets
- current watch seam: keep the bundle narrow as local-source instruction fan-out without widening into fragment composition, skill propagation, nested loading, provenance mirroring, or general agent-config orchestration

## Failure modes
- teams start hand-editing target instruction files anyway, so the canonical source still exists on paper while real authority quietly splits across outputs
- canonical pressure widens the technique into all agent configuration propagation, including skills, MCP, or nested loading, instead of keeping the current instruction-surface contract explicit
- synchronized-looking outputs hide wrapper drift or target-specific shadow logic until the shared rule core no longer means the same thing across targets

## Negative effects
- a clean fan-out path can create false confidence that every target still carries the same rule intent even when wrappers or exclusions already diverged
- making this the default can encourage teams to add managed distribution where they only have one target or no clear source-of-truth discipline yet
- successful multi-target refresh tooling can pull review attention away from the canonical source and toward generated outputs

## Misuse patterns
- using `AOA-T-0013` for one-source -> one-target sync or for generic generated-context composition that belongs to `AOA-T-0012`
- treating cross-agent skill propagation, nested rule loading, or upstream mirroring as if they are the same contract instead of routing to `AOA-T-0027`, `AOA-T-0029`, or `AOA-T-0024`
- letting target-specific wrappers, overrides, or exceptions accumulate until each managed file becomes a semi-canonical source in disguise

## Detection signals
- reviewers spend more time explaining target-specific differences than verifying one shared canonical rule source
- source updates no longer re-apply cleanly and start requiring hand-fixes across multiple managed targets
- pull requests edit generated target files directly without routing the change back through the canonical source
- consumers cite target files as the rule authority instead of the local source that is supposed to own the shared content

## Mitigations
- keep the canonical source explicit, keep managed targets marked as derived, and route every shared-rule change back through the source before re-applying distribution
- split adjacent behavior into sibling techniques instead of letting skills propagation, nested loading, provenance mirroring, or fragment composition accumulate inside this bundle
- keep parity or diff review focused on proving source-to-target synchronization, not on treating generated targets as the primary review surface
- revisit canonical status if the bundle starts being used mainly for one-target sync, product-width orchestration, or wrapper-heavy target customization

## Recommendation
- keep current `canonical` status and use this note as the watch surface for target drift, wrapper creep, and sibling-boundary widening around the instruction-surface cluster
