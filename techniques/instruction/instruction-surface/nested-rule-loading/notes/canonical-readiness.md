# Canonical Readiness

## Technique
- id: AOA-T-0029
- name: nested-rule-loading

## Verdict
- bounded defer for now

## Evidence summary
- external origin: the imported technique has a bounded donor contract and explicit exclusions around MCP propagation, skills propagation, installer breadth, and other product-width detail
- second context: `aoa-techniques` now records the same contract as a documentation-first adaptation with examples and a checklist
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- validation strength: the bundle now carries one checklist, two examples, a clean external-origin note, and one documentation-first second context, but it still lacks a live adopter beyond the donor repository

## Default-use rationale
- this is the right promoted default when a repository needs hierarchical rule layers with explicit precedence and one-way ownership
- it remains narrower than `AOA-T-0013`, which keeps the broader one-canonical-rule-source-to-many-managed-targets instruction-surface distribution story in focus
- it stays distinct from `AOA-T-0027`, which is about managed-target propagation of a shared skill or rule core rather than nested loading

## Fresh public-safety check
- review date: 2026-03-21
- result: pass
- sanitization still holds: the bundle keeps the reusable nested-loading contract and excludes donor-specific orchestration behavior
- public reuse check: the examples, checklist, and adaptation notes remain understandable without hidden donor-repo context

## Remaining gaps
- the smallest remaining gap is still one live second context beyond the donor and documentation-first adaptation
- specifically, the bundle still needs another public repository or surface family that uses the same nested-loading contract as a real layered rule hierarchy rather than only as imported documentation

## Recommendation
- keep `AOA-T-0029` `promoted`
- defer canonical promotion until another live adopter confirms that the nested-loading contract survives outside the donor repository
