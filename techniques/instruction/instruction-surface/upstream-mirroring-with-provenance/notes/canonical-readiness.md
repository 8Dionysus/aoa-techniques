# Canonical Readiness

## Technique
- id: AOA-T-0024
- name: upstream-mirroring-with-provenance

## Verdict
- bounded defer for now

## Evidence summary
- external origin: the imported technique has a bounded donor contract and explicit exclusions around marketplace policy, registry generation, installer behavior, and other product-width detail
- second context: `aoa-techniques` now records the same contract as a documentation-first adaptation with examples and a checklist
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- validation strength: the bundle now carries one checklist, two examples, a clean external-origin note, and one documentation-first second context, but it still lacks a live adopter beyond the donor repo

## Default-use rationale
- this is the right promoted default when a local collection wants to mirror upstream-owned content with explicit provenance instead of silently claiming the mirrored copy as a new canonical source
- it remains narrower than `AOA-T-0013`, which starts when the canonical source is already local and the main problem is fan-out to many managed instruction targets
- it also remains distinct from `AOA-T-0020`, which is about typed note-kind provenance in derived manifests rather than mirrored content plus adjacent attribution

## Fresh public-safety check
- review date: 2026-03-21
- result: pass
- sanitization still holds: the bundle keeps only the reusable mirroring-plus-provenance contract and excludes marketplace, installer, and registry detail
- public reuse check: the public examples, checklist, and adaptation notes remain understandable without hidden donor-repo context

## Remaining gaps
- the smallest remaining gap is still one live second context beyond the donor and documentation-first adaptation
- specifically, the bundle still needs another public repository or collection proving that manifest-driven upstream mirroring plus adjacent provenance works outside the donor repo

## Recommendation
- keep `AOA-T-0024` `promoted`
- defer canonical promotion until another live adopter confirms that the mirroring-plus-provenance contract survives outside the donor repository
