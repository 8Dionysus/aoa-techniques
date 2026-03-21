# Canonical Readiness

## Technique
- id: AOA-T-0013
- name: single-source-rule-distribution

## Verdict
- bounded defer for now

## Evidence summary
- external origin: the imported technique has a bounded donor contract and explicit exclusions around nested loading, MCP propagation, skills propagation, and other product-width behavior
- second context: the repo-local adaptation note shows the contract clearly enough to remain reusable, but it still reads as a sketch rather than a live multi-target reuse proof
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- validation strength: the bundle includes a checklist, two public-safe examples, and a clean separation from `AOA-T-0012`, but it still lacks live multi-target reuse beyond the current repository narrative

## Default-use rationale
- this is the right default when one canonical rule source must fan out to multiple managed instruction targets without turning those targets into canonical homes
- it remains narrower than `AOA-T-0012`, which composes many fragments into one generated artifact rather than distributing one shared rule core to multiple targets
- the current wording is strong enough for reuse, but not yet strong enough to justify canonical default status without evidence that the shared core survives real multi-target re-application

## Fresh public-safety check
- review date: 2026-03-20
- result: pass
- sanitization still holds: the bundle keeps the reusable one-source-to-many-target pattern and excludes donor-specific orchestration behavior
- public reuse check: the current bundle remains understandable without donor-repo access or hidden local automation

## Remaining gaps
- the smallest remaining gap is live multi-target reuse beyond the current adaptation sketch
- specifically, the bundle still needs a real managed target flow showing one source update propagating cleanly to multiple instruction surfaces more than once

## Recommendation
- keep `AOA-T-0013` `promoted`
- defer canonical promotion until a live multi-target reuse context exists beyond the current repo-local adaptation sketch
