# Adverse Effects Review

## Technique

- id: AOA-T-0027
- name: cross-agent-skill-propagation

## Review focus

- current role: canonical default for propagating one shared skill or rule core into multiple managed agent-facing targets
- current watch seam: keep the bundle centered on managed-target fan-out rather than broader rule distribution, marketplace curation, MCP propagation, profile policy, nested loading, or runtime role behavior

## Failure modes

- target files become semi-canonical because contributors edit them directly after generation or propagation
- the shared skill or rule core becomes too target-specific to survive repeatable fan-out
- a cross-tool config system is mistaken for proof that every generated target carries the same bounded meaning
- propagation succeeds mechanically while wrappers or destination conventions change the shared intent

## Negative effects

- managed propagation can hide drift because every target still appears fresh
- one shared core can become bland if target-specific requirements are forced into the source
- canonical status can encourage propagation into tools that do not need the shared skill or rule
- target-native formats can distract reviewers from checking whether the shared core still owns the meaning

## Misuse patterns

- using the bundle for generic one-source rule distribution that belongs to `AOA-T-0013`
- treating skill marketplace discovery, MCP sync, profile composition, or runtime role setup as part of this contract
- adding enough target-specific wrapper logic that each destination becomes an independent policy layer
- claiming parity from generated files without checking the source-to-target relation

## Detection signals

- pull requests edit target files without touching or regenerating from the canonical source
- reviewers cannot identify the shared skill or rule core after looking at the target outputs
- target wrappers carry substantive instructions not present in the source
- discussion focuses on supported tool count rather than on source ownership, managed fan-out, and repeatability

## Mitigations

- keep the canonical source explicit and route shared changes through it before propagation
- keep wrappers minimal and destination-focused
- treat target-native format support as an adapter concern, not as technique meaning
- split broader marketplace, MCP, profile, nested-loading, and runtime-role behavior into sibling techniques or owner repos
- revisit canonical status if the technique starts being used mainly for generic config generation instead of managed propagation of one shared skill or rule core

## Recommendation

- keep current `canonical` status and use this note as the watch surface for target drift, wrapper creep, tool-count overreach, and sibling-boundary widening around the instruction-surface cluster
