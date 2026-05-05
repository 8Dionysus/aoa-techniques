# Canonical Readiness

## Technique
- id: AOA-T-0027
- name: cross-agent-skill-propagation

## Verdict
- bounded defer for now

## Evidence summary
- external origin: the imported technique has a bounded donor contract and explicit exclusions around marketplace curation, runtime role semantics, MCP propagation, nested loading, and other product-width detail
- second context: `aoa-techniques` now records the same contract as a documentation-first adaptation with examples and a checklist
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- validation strength: the bundle now carries one checklist, two examples, a clean external-origin note, and one documentation-first second context, but it still lacks a live adopter beyond the donor repository

## Default-use rationale
- this is the right promoted default when one shared skill or rule core must reach multiple agent-facing targets without turning each target into a canonical home
- it remains narrower than `AOA-T-0013`, which keeps the broader one-canonical-rule-source-to-many-managed-targets instruction-surface distribution story in focus
- it also stays distinct from `AOA-T-0024`, which is about upstream mirroring with provenance rather than local skill or rule propagation

## Fresh public-safety check
- review date: 2026-03-21
- result: pass
- sanitization still holds: the bundle keeps the reusable propagation contract and excludes donor-specific orchestration behavior
- public reuse check: the examples, checklist, and adaptation notes remain understandable without hidden donor-repo context

## Remaining gaps
- the smallest remaining gap is still one live second context beyond the donor and documentation-first adaptation
- specifically, the bundle still needs another public repository or surface family that uses the same shared-skill propagation contract as a real managed-target fan-out rather than only as imported documentation

## Recommendation
- keep `AOA-T-0027` `promoted`
- defer canonical promotion until another live adopter confirms that the shared-skill propagation contract survives outside the donor repository
