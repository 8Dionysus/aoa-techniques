# Canonical Readiness

## Technique
- id: AOA-T-0064
- name: capability-discovery

## Verdict
- bounded defer for now

## Evidence summary
- external origin: the imported technique has a bounded donor contract and explicit exclusions around ranking, semantic linkage, trust filters, and registry runtime breadth
- second context: `aoa-techniques` now records the same contract as a documentation-first adaptation with one example and one checklist
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- validation strength: the bundle now carries one checklist, one example, a clean external-origin note, and one documentation-first second context, but it still lacks a live adopter beyond the donor repository

## Default-use rationale
- this is the right promoted default when the main problem is making capability lookup explicit and reviewable over already-published entries instead of hiding discovery semantics in server code or registry product behavior
- it remains narrower than [AOA-T-0063](../versioned-agent-registry-contract/TECHNIQUE.md) because it does not publish the entry contract, and it remains narrower than [AOA-T-0041](../skill-marketplace-curation/TECHNIQUE.md) because it does not curate or rank discovery

## Fresh public-safety check
- review date: 2026-03-28
- result: pass
- sanitization still holds: the bundle keeps only the reusable discovery-query contract and excludes donor-specific network, ranking, trust, and runtime details
- public reuse check: the example, checklist, and adaptation notes remain understandable without hidden donor-repo context

## Remaining gaps
- the smallest remaining gap is still one live second context beyond the donor and documentation-first adaptation
- specifically, the bundle still needs another public repository or surface family that uses explicit bounded discovery queries as a real lookup surface rather than only as imported documentation

## Recommendation
- keep `AOA-T-0064` `promoted`
- defer canonical promotion until another live adopter confirms that the discovery-query contract survives outside the donor repository
