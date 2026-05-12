# Canonical Readiness

## Technique
- id: AOA-T-0071
- name: template-backed-field-extraction-after-ocr

## Verdict
- approve for canonical promotion

## Evidence summary

- external origin: the imported technique has a bounded donor contract and explicit exclusions around OCR-stage ownership, locale lock-in, bookkeeping automation, and donor parser implementation
- second context: `aoa-techniques` now records the same post-OCR extraction seam as a documentation-first adaptation with one example and one checklist
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- `kotaro-kinoshita/yomitoku` provides exact-fit public reinforcement beyond the donor parser family: `YomiToku Extractor` defines target fields in a YAML schema, runs rule-based extraction through explicit `cell_id`, `bbox`, `description`, and `regex` methods, preserves `raw_text`, source, cell ids, bounding boxes, and confidence in JSON output, and marks failed scalar or table extraction with `source: not_found` and low confidence instead of silently filling a value
- YomiToku's inspected public source is CC BY-NC-SA 4.0 licensed at commit `51a51f4ce21d8a0b34998be1a9f03dfb50fa6925`; it is used as evidence only, with no source code, schema text, model weights, sample images, or commercial-use posture imported into this technique. Inspected files include `README_EN.md` (`4b02e28ffacf6adb148c79771cde44eb02784432`), `docs/extractor.en.md` (`49f6b3619a69af2fcc2ba9ad91b97e62ac4666ce`), `src/yomitoku/extractor/schema.py` (`8b17116c3211f3fdf9d4e3ebd132b46b1269b472`), `src/yomitoku/extractor/rule_pipeline.py` (`be4c2196fa6a0e5c823854c540ea7bb142042d6f`), `tests/test_extractor.py` (`d37ce0f05ab015cd42d4c20c5c9b728ec0d5b8c1`), and `pyproject.toml` (`faa59ba5a0cf1563ec5966e36e0b674532be8c3d`)
- adjacent lanes were checked and kept out of the canonical proof: `codebywiam/invoice-ocr` and `nzregs/receipt-api` show regex or heuristic field extraction after OCR, but they are application-shaped invoice or receipt APIs with weaker schema and review metadata boundaries; YomiToku is the narrower primary proof because the schema, extraction method priority, source metadata, confidence, and not-found posture are all explicit
- validation strength: the bundle now carries one checklist, one example, a clean external-origin note, a documentation-first second context, and public cross-context reinforcement that repeats bounded post-OCR field extraction outside the donor parser family

## Default-use rationale

- this is the right canonical default when the main problem is turning OCR-derived text into a small explicit field object without hiding uncertainty inside a parser implementation
- it remains narrower than [AOA-T-0070](../../two-stage-document-ocr-pipeline/TECHNIQUE.md) because it starts after OCR handoff already exists
- it also remains narrower than later ingestion or taxonomy techniques because it owns only bounded field extraction plus review fallback
- it is now strong enough as a canonical default because the second public context repeats the key shape: a named schema determines the fields, visible rules or hints select values, output preserves source evidence and confidence, and missing results remain visible

## Fresh public-safety check

- review date: 2026-05-12
- result: pass
- sanitization still holds: the bundle keeps only the reusable post-OCR extraction seam and excludes donor parser code, locale lock-in, and bookkeeping or ingestion detail
- public reuse check: the example, checklist, and adaptation notes remain understandable without hidden donor-repo context; YomiToku is cited only as public evidence, and the technique does not copy its code, schemas, model files, sample documents, Japanese-document specialization, LLM-server setup, commercial-license boundary, or product workflow

## Remaining gaps

- no blocker remains for canonical status
- future sources can reinforce the default, but they must preserve the narrow boundary: upstream OCR or layout output, one explicit field set, visible template or heuristic selection, source evidence or confidence, explicit missing or conflicting results, and a stop-line before locale doctrine, accounting automation, model serving, or total document-understanding products

## Recommendation

- move `AOA-T-0071` to `canonical`
- add an adverse-effects review to preserve the boundary between post-OCR field extraction, OCR staging, document schemas, locale policy, bookkeeping automation, LLM extraction products, and full document-understanding stacks
