# Canonical Readiness

## Technique
- id: AOA-T-0013
- name: single-source-rule-distribution

## Verdict
- bounded defer for now

## Evidence summary
- external origin: the imported technique has a bounded donor contract and explicit exclusions around nested loading, MCP propagation, skills propagation, and other product-width behavior, and that donor still reads cleanly against the current `ruler` public surface
- second context: merged `aoa-skills@b1b3fc7b330f2fecc5412c0444bc108b4aecc67c` now provides a first live one-source -> many-target donor path through `docs/BRIDGE_SPEC.md`, committed consumer skills, and explicit drift-control tooling
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- donor intake refinement: current seeded donor review now records `agents-md` as an overlap hold against `AOA-T-0012` and `n-skills` as the adjacent `AOA-T-0024 upstream-mirroring-with-provenance` import rather than synthetic proof for this bundle
- validation strength: the bundle includes a checklist, two public-safe examples, a clean separation from `AOA-T-0012`, one bounded external origin, and one real sibling-repo donor, but it still lacks a second independent live instruction-distribution context beyond `aoa-skills`

## Default-use rationale
- this is the right default when one canonical rule source must fan out to multiple managed instruction targets without turning those targets into canonical homes
- it remains narrower than `AOA-T-0012`, which composes many fragments into one generated artifact rather than distributing one shared rule core to multiple targets
- the current wording is strong enough for reuse, but not yet strong enough to justify canonical default status without evidence that the shared core survives a second independent multi-target re-application beyond the first `aoa-skills` donor

## Fresh public-safety check
- review date: 2026-03-21
- result: pass
- sanitization still holds: the bundle keeps the reusable one-source-to-many-target pattern and excludes donor-specific orchestration behavior
- public reuse check: the current bundle remains understandable without donor-repo access or hidden local automation

## Remaining gaps
- the smallest remaining gap is still one second independent live instruction-distribution context beyond the first `aoa-skills` donor
- specifically, the bundle still needs another managed target flow showing one source update propagating cleanly to multiple instruction surfaces in a second repo or surface family such as `aoa-agents`
- another external-import-only review, overlap-heavy composition tool, or provenance-mirroring tool does not satisfy that remaining live-evidence gap on its own

## Recommendation
- keep `AOA-T-0013` `promoted`
- defer canonical promotion until a second live multi-target reuse context exists beyond the current `aoa-skills` donor
