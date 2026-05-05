# Canonical Readiness

## Technique
- id: AOA-T-0013
- name: single-source-rule-distribution

## Verdict
- approve for canonical promotion

## Evidence summary
- external origin: the imported technique keeps `ruler` as a bounded origin donor with explicit exclusions around nested loading, MCP propagation, skills propagation, and other product-width behavior
- first live downstream context: merged `aoa-skills@b1b3fc7b330f2fecc5412c0444bc108b4aecc67c` provides a first live one-source -> many-target donor path through `docs/BRIDGE_SPEC.md`, committed consumer skills, and explicit drift-control tooling
- independent public reinforcement: `dyoshikawa/rulesync` exposes a bounded unified-rule-source -> many-target instruction-generation path, and `EmberAGI/arbitrum-vibekit` uses `.rulesync/` as a committed source-of-truth layer for generated `.claude/` and `.cursor/` instruction surfaces
- external review: the first import review passed and the bounded external-intake package still reads cleanly
- validation strength: the bundle now has a checklist, two public-safe examples, a clean separation from `AOA-T-0012`, one bounded external origin, one live sibling-repo donor in `aoa-skills`, and one independent public instruction-distribution path through `rulesync` plus a live `.rulesync` consumer, so the contract now reads as repeated one-source -> many-target reuse rather than one donor lineage

## Default-use rationale
- this is the right default when one canonical rule source must fan out to multiple managed instruction targets without turning those targets into canonical homes
- it remains narrower than `AOA-T-0012`, which composes many fragments into one generated artifact rather than distributing one shared rule core to multiple targets
- it also remains narrower than `AOA-T-0027`, `AOA-T-0029`, and `AOA-T-0024`, which own managed skill propagation, hierarchical rule precedence, and upstream mirroring with provenance rather than local canonical-source fan-out
- the current evidence now shows that the shared rule core survives beyond the first `aoa-skills` bridge lineage, so the bundle reads as the natural default for local-source -> many-target instruction distribution inside the instruction-surface cluster

## Fresh public-safety check
- review date: 2026-03-23
- result: pass
- sanitization still holds: the bundle keeps the reusable one-source-to-many-target pattern and excludes donor-specific orchestration behavior
- public reuse check: the current bundle remains understandable without donor-repo access or hidden local automation

## Remaining gaps
- no blocking promotion gap remains as long as the bundle stays bounded to one local canonical rule source fanning out to multiple managed instruction targets
- future review should keep watching for drift into `AOA-T-0012` fragment composition, `AOA-T-0027` managed skill propagation, `AOA-T-0029` nested loading, or `AOA-T-0024` upstream mirroring
- canonical use still assumes at least two real managed targets, explicit derived-target ownership, and reviewable source-to-target parity rather than manual copied rule blocks

## Recommendation
- promote `AOA-T-0013` to `canonical`
- use `AOA-T-0013` as the default instruction-surface technique when one canonical local rule source must refresh multiple managed agent-facing instruction targets without turning those targets into canonical homes
