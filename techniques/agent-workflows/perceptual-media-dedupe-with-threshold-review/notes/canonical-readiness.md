# Canonical Readiness

## Technique
- id: AOA-T-0072
- name: perceptual-media-dedupe-with-threshold-review

## Verdict
- bounded defer for now

## Evidence summary

- external origin: the imported technique has a bounded donor contract and explicit exclusions around delete policy, semantic taxonomy, ranking doctrine, and donor runtime detail
- second context: `aoa-techniques` now records the same duplicate-grouping seam as a documentation-first adaptation with one example and one checklist
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- validation strength: the bundle now carries one checklist, one example, a clean external-origin note, and one documentation-first second context, but it still lacks a live adopter beyond the donor dedupe family

## Default-use rationale

- this is the right promoted default when the main problem is grouping near-duplicate media while keeping borderline matches visible and later file actions separate
- it remains narrower than a later semantic bucketing technique because it does not assign media taxonomy
- it also remains narrower than cleanup automation because it stops at duplicate grouping and review signals rather than preserve or delete decisions

## Fresh public-safety check

- review date: 2026-03-28
- result: pass
- sanitization still holds: the bundle keeps only the reusable duplicate-grouping seam and excludes donor CLI behavior, delete defaults, ANN backend detail, and cleanup governance
- public reuse check: the example, checklist, and adaptation notes remain understandable without hidden donor-repo context

## Remaining gaps

- the smallest remaining gap is still one live second context beyond the donor and documentation-first adaptation
- specifically, the bundle still needs another public repository or surface family that keeps perceptual duplicate grouping explicit through thresholds and review buckets before later cleanup actions begin

## Recommendation

- keep `AOA-T-0072` `promoted`
- defer canonical promotion until another live adopter confirms that the reviewable duplicate-grouping contract survives outside the donor dedupe family
