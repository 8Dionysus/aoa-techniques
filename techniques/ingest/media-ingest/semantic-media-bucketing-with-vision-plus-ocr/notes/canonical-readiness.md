# Canonical Readiness

## Technique
- id: AOA-T-0073
- name: semantic-media-bucketing-with-vision-plus-ocr

## Verdict
- approve for canonical promotion

## Evidence summary

- external origin: the imported technique has a bounded donor contract and explicit exclusions around duplicate grouping, OCR extraction ownership, moderation policy, identity inference, and donor serving detail
- second context: `aoa-techniques` now records the same media-bucketing seam as a documentation-first adaptation with one example and one checklist
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- `end1989/ai-image-classification` provides exact-fit public reinforcement beyond the original donor READMEs and repo-local documentation-first adaptation: its media sorter exposes an explicit label taxonomy that includes screenshot, meme, receipt, document, work, food, people, nature, and other-style buckets; computes CLIP image embeddings and scores them against configured labels; stores classification labels and confidence; keeps configurable review and auto-move thresholds; extracts OCR text and confidence as a separate result; uses OCR text only to boost label confidence for text-heavy categories such as receipts, chats, and work material; exposes a review band for confidence between `review` and `auto_move`; records user corrections separately; and keeps file movement plus undo in action/file-manager surfaces rather than making the classification itself a delete or archive verdict
- the inspected source is MIT licensed at commit `e3f3500bf274e802d669ed38403b7637b0897366` with commit date `2026-02-09T22:12:35-07:00`; inspected files include `README.md` (`df0270a5ad3ab834004e338bfe4cb662ac868a90`), `LICENSE` (`47305393d09ff9d598e4883c455a8a6fea1283f1`), `docs/ARCHITECTURE.md` (`7899634051c6305f13601b62e9668ebe4f8c2cfb`), `docs/03_phase2_ocr_nsfw_routing.md` (`da4fb316540b84be538c7769114311d30eaf20d0`), `config/config.yaml` (`2a09c666c05db13c7e42a4eb0e1aed46ed2ca756`), `config/config_loader.py` (`802e26252b6008d1be928c538a90b0ea547954b9`), `pipeline/classify.py` (`09ffe3d0133720af2ecd895f97e46622492da86e`), `pipeline/ocr.py` (`65a4214cce477f033823f5cbafad4e55b5e57791`), `backend/database.py` (`f0b0ff89d28955c6a54bb54d322eca2062e45686`), and `pipeline/actions.py` (`62d635599c266465797bda70d3b25ef052f5c9bf`)
- adjacent lanes were checked and kept out of the canonical proof: `chintan-projects/photo-triage-agent` supports photo triage pressure but does not show the same OCR-side-channel confidence seam; `Aditya-Vasipalli/screensort` / Fragmenta supports screenshot categories plus OCR but widens into intent extraction, calendar actions, structured data extraction, and Notion tasks; receipt-only extraction projects collapse into domain schema extraction rather than mixed-media bucketing; broad SaaS/file-classifier products route into cleanup, cloud storage, or action policy
- validation strength: the bundle now carries one checklist, one example, a clean external-origin note, a documentation-first second context, an import review, and live public cross-context reinforcement that repeats bounded semantic media bucketing outside the original donor README family

## Default-use rationale

- this is the right canonical default when the main problem is assigning a small explicit media taxonomy while keeping low-confidence or conflicting items visible for review
- it remains narrower than [AOA-T-0072](../../perceptual-media-dedupe-with-threshold-review/TECHNIQUE.md) because it does not group duplicates
- it also remains narrower than [AOA-T-0070](../../two-stage-document-ocr-pipeline/TECHNIQUE.md) because it uses OCR only as side text rather than owning OCR staging itself
- it is now strong enough as a canonical default because the second public context repeats the key shape: visual semantics score a bounded taxonomy, OCR can adjust text-heavy categories without becoming truth, confidence bands determine review versus later action eligibility, corrections remain visible, and file actions stay outside the classification contract

## Fresh public-safety check

- review date: 2026-05-12
- result: pass
- sanitization still holds: the bundle keeps only the reusable media-bucketing seam and excludes donor model-serving detail, moderation claims, identity inference, face/person analysis, auto-move policy, deletion, archive policy, UI/product flow, local database schema, and downstream action policy
- public reuse check: the example, checklist, and adaptation notes remain understandable without hidden donor-repo context; `end1989/ai-image-classification` is cited only as public evidence, and the technique does not copy its Python source, EasyOCR implementation, UI, database schema, NSFW module, face detection, file-manager behavior, or auto-organization product workflow

## Remaining gaps

- no blocker remains for canonical status
- future sources can reinforce the default, but they must preserve the narrow boundary: bounded media set, explicit taxonomy, visual semantic scoring, OCR as side-channel, confidence or review thresholds, and a stop-line before duplicate grouping, OCR extraction ownership, moderation, identity inference, file deletion, archive policy, auto-routing, or full media-management products

## Recommendation

- move `AOA-T-0073` to `canonical`
- add an adverse-effects review to preserve the boundary between semantic media bucketing, OCR side text, review thresholds, correction/review loops, moderation, identity inference, duplicate grouping, and later file actions
