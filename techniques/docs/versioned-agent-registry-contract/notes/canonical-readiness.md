# Canonical Readiness

## Technique
- id: AOA-T-0063
- name: versioned-agent-registry-contract

## Verdict
- bounded defer for now

## Evidence summary
- external origin: the imported technique has a bounded donor contract and explicit exclusions around discovery queries, semantic linkage, trust services, and registry runtime breadth
- second context: `aoa-techniques` now records the same contract as a documentation-first adaptation with one example and one checklist
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- validation strength: the bundle now carries one checklist, one example, a clean external-origin note, and one documentation-first second context, but it still lacks a live adopter beyond the donor repository

## Default-use rationale
- this is the right promoted default when the main problem is making a registry-facing capability entry explicit and versioned instead of hiding publication meaning in runtime or directory internals
- it remains narrower than [AOA-T-0025](../capability-spec-versioning/TECHNIQUE.md) because it owns the publication contract for a registry entry rather than the full capability spec, and it remains narrower than [AOA-T-0041](../skill-marketplace-curation/TECHNIQUE.md) because it does not curate discovery or selection

## Fresh public-safety check
- review date: 2026-03-28
- result: pass
- sanitization still holds: the bundle keeps only the reusable entry contract and excludes donor-specific network, query, signature, and runtime details
- public reuse check: the example, checklist, and adaptation notes remain understandable without hidden donor-repo context

## Remaining gaps
- the smallest remaining gap is still one live second context beyond the donor and documentation-first adaptation
- specifically, the bundle still needs another public repository or surface family that uses a versioned registry-entry contract as a real publication surface rather than only as imported documentation

## Recommendation
- keep `AOA-T-0063` `promoted`
- defer canonical promotion until another live adopter confirms that the registry-entry contract survives outside the donor repository
