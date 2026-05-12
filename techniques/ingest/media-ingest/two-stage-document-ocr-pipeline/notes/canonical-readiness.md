# Canonical Readiness

## Technique
- id: AOA-T-0070
- name: two-stage-document-ocr-pipeline

## Verdict
- approve for canonical promotion

## Evidence summary

- external origin: the imported technique has a bounded donor contract and explicit exclusions around serving posture, benchmark claims, packaging, and document-specific extraction doctrine
- second context: `aoa-techniques` now records the same staged OCR seam as a documentation-first adaptation with one example and one checklist
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- `JaidedAI/EasyOCR` provides exact-fit public reinforcement beyond the donor OCR family: the public README exposes OCR results as bounding box, recognized text, and confidence tuples; the implementation keeps `detect()` and `recognize()` as separate methods; `readtext()` derives text regions first and passes those region lists into recognition; dictionary and JSON output modes preserve boxes, text, and confidence as one structured result surface
- EasyOCR's current public source is Apache-2.0 licensed at commit `363afb184047ce452e436f4224f3098422df872e`; inspected files include `README.md` (`d7e7853811a65d0373c5dc77d2c91402c963d0fa`), `easyocr/easyocr.py` (`c08fe0388ddcfdd7d027ad68a16fb9079b5e9267`), `custom_model.md` (`3dead0b050ccaee5d24314b38f1025fc5fa67e1f`), `trainer/craft/README.md` (`823c83dc679a50196e4185ed5d4eb480d9bdc19f`), and `releasenotes.md` (`4c72a2f8da70e1af1a406eddd326b2d7e556cc6e`)
- adjacent OCR lanes were checked and kept out of the canonical proof: OCRmyPDF is primarily searchable-PDF layering, Tesseract.js is OCR engine packaging rather than an explicit staged handoff contract, Surya widens into layout analysis, table recognition, and GPL-licensed document understanding, and PaddleOCR/docTR remain donor-family evidence rather than an independent second context
- validation strength: the bundle now carries one checklist, one example, a clean external-origin note, a documentation-first second context, and public cross-context reinforcement that repeats the bounded staged OCR handoff outside the donor family

## Default-use rationale

- this is the right canonical default when the main problem is keeping OCR output reviewable and interchangeable before later extraction or parsing begins
- it remains narrower than any later template-backed field extraction technique because it stops at OCR handoff rather than asserting field semantics
- it also remains narrower than multimodal bucketing or media-review techniques because it stays on staged document text extraction rather than taxonomy or dedupe behavior
- it is now strong enough as a canonical default because the second public context repeats the key shape: detect text-bearing regions, recognize bounded segments, preserve source boxes and confidence, and leave later extraction or review as a separate consumer

## Fresh public-safety check

- review date: 2026-05-12
- result: pass
- sanitization still holds: the bundle keeps only the reusable staged OCR seam and excludes donor-specific serving, packaging, and business-logic detail
- public reuse check: the example, checklist, and adaptation notes remain understandable without hidden donor-repo context; the inspected EasyOCR source is public and Apache-2.0 licensed, and no source code, model weights, sample images, private documents, credentials, runtime paths, benchmark claims, app-specific extraction schemas, or deployment instructions were copied into the technique

## Remaining gaps

- no blocker remains for canonical status
- future sources can reinforce the default, but they must preserve the narrow boundary: visible region or layout handles, recognized text, confidence or uncertainty, one structured OCR handoff, and a stop-line before field extraction, semantic bucketing, automation, model serving, benchmarking, or full document-understanding systems

## Recommendation

- move `AOA-T-0070` to `canonical`
- add an adverse-effects review to preserve the boundary between staged OCR handoff, later field extraction, media bucketing, searchable-PDF generation, OCR serving, benchmark doctrine, and full document-understanding stacks
