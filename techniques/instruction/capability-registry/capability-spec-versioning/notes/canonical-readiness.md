# Canonical Readiness

## Technique
- id: AOA-T-0025
- name: capability-spec-versioning

## Verdict
- bounded defer for now

## Evidence summary
- external origin: the imported technique has a bounded donor contract and explicit exclusions around plan-and-execute orchestration, persistence, execution-history learning, and registry breadth
- second context: `aoa-techniques` now records the same contract as a documentation-first adaptation with examples and a checklist
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- validation strength: the bundle now carries one checklist, two examples, a clean external-origin note, and one documentation-first second context, but it still lacks a live adopter beyond the donor repository

## Default-use rationale
- this is the right promoted default when the main problem is keeping one agent-facing capability contract explicit and versioned instead of hiding it in provider code or runtime glue
- it remains narrower than workflow or routing techniques because it only owns the contract surface, not execution sequencing, registry lifecycle, or dispatch policy

## Fresh public-safety check
- review date: 2026-03-21
- result: pass
- sanitization still holds: the bundle keeps only the reusable capability-spec contract and excludes donor-specific runtime, CLI, persistence, and learning detail
- public reuse check: the examples, checklist, and adaptation notes remain understandable without hidden donor-repo context

## Remaining gaps
- the smallest remaining gap is still one live second context beyond the donor and documentation-first adaptation
- specifically, the bundle still needs another public repository or surface family that uses a versioned capability spec as a real agent-facing contract rather than only as imported documentation

## Recommendation
- keep `AOA-T-0025` `promoted`
- defer canonical promotion until another live adopter confirms that the versioned capability-contract pattern survives outside the donor repository
