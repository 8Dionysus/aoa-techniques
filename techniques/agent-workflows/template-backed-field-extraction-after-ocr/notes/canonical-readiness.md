# Canonical Readiness

## Technique
- id: AOA-T-0071
- name: template-backed-field-extraction-after-ocr

## Verdict
- bounded defer for now

## Evidence summary

- external origin: the imported technique has a bounded donor contract and explicit exclusions around OCR-stage ownership, locale lock-in, bookkeeping automation, and donor parser implementation
- second context: `aoa-techniques` now records the same post-OCR extraction seam as a documentation-first adaptation with one example and one checklist
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- validation strength: the bundle now carries one checklist, one example, a clean external-origin note, and one documentation-first second context, but it still lacks a live adopter beyond the donor parser family

## Default-use rationale

- this is the right promoted default when the main problem is turning OCR-derived text into a small explicit field object without hiding uncertainty inside a parser implementation
- it remains narrower than [AOA-T-0070](../two-stage-document-ocr-pipeline/TECHNIQUE.md) because it starts after OCR handoff already exists
- it also remains narrower than later ingestion or taxonomy techniques because it owns only bounded field extraction plus review fallback

## Fresh public-safety check

- review date: 2026-03-28
- result: pass
- sanitization still holds: the bundle keeps only the reusable post-OCR extraction seam and excludes donor parser code, locale lock-in, and bookkeeping or ingestion detail
- public reuse check: the example, checklist, and adaptation notes remain understandable without hidden donor-repo context

## Remaining gaps

- the smallest remaining gap is still one live second context beyond the donor and documentation-first adaptation
- specifically, the bundle still needs another public repository or surface family that keeps post-OCR field extraction explicit through templates or heuristics before later ingestion or automation begins

## Recommendation

- keep `AOA-T-0071` `promoted`
- defer canonical promotion until another live adopter confirms that the post-OCR extraction contract survives outside the donor parser family
