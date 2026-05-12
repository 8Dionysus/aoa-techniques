# Second Context Adaptation

## Technique
- id: AOA-T-0071
- name: template-backed-field-extraction-after-ocr

## Target project
- name: aoa-techniques
- environment: public technique repository with authored bundle contracts, generated routing surfaces, and validator-backed markdown discipline
- runtime: documentation-first corpus that records the bounded post-OCR extraction pattern rather than shipping donor parser code, locale packs, or ingestion workflows
- source: `https://github.com/kotaro-kinoshita/yomitoku`
- license: CC BY-NC-SA 4.0
- inspected commit: `51a51f4ce21d8a0b34998be1a9f03dfb50fa6925`
- inspected surfaces: `README_EN.md`, `docs/extractor.en.md`, `src/yomitoku/extractor/schema.py`, `src/yomitoku/extractor/rule_pipeline.py`, `tests/test_extractor.py`, and `pyproject.toml`
- result: exact-fit public reinforcement beyond the invoice2data, receiptparser, and receipt-parser-legacy donor family

## What changed

- donor parser families were reduced to one portable post-OCR extraction contract rather than one invoice or receipt application stack
- locale-specific rules, parser implementations, and ingestion helpers were removed from the reusable public bundle
- OCR-stage ownership was kept out so the adaptation starts from one upstream OCR handoff instead of raw image processing
- the bundle was reduced to one technique doc, one checklist, one example, and four bounded evidence notes
- the 2026-05-12 canonical review now records YomiToku as live second-context reinforcement because its public extractor turns OCR and layout analysis output into schema-defined fields through explicit rule methods, preserves source metadata and confidence, and emits `not_found` for misses

## What stayed invariant

- OCR handoff remains the upstream input
- field targets remain explicit and bounded
- templates or heuristics remain reviewable aids rather than hidden parser law
- missing or conflicting values stay visible instead of being guessed away
- source evidence can stay attached through raw text, cell ids, bounding boxes, source labels, and confidence when review needs to inspect why a value was chosen

## Risks introduced by adaptation

- the technique can collapse into an end-to-end parser if later users stop separating OCR staging from field extraction
- teams may over-associate the technique with one donor template family if interchangeable extraction rules are not kept explicit
- output can look cleaner than the underlying evidence if field-evidence references are dropped too early
- YomiToku also includes OCR, layout analysis, LLM extraction, model setup, and commercial-use boundaries; those are external product details, not invariant requirements for this technique

## Evidence

- invoice2data's README shows structured extraction over OCR or PDF text through YAML or JSON templates and explicit output fields
- receiptparser's README shows configurable receipt extraction through YAML configuration and explicit structured values such as company, date, and amount
- receipt-parser-legacy's README frames the reusable core as extracting shop, date, and total from scanned receipts after OCR-derived text exists
- YomiToku repeats the same post-OCR field seam outside that donor family: YAML schemas define field names, structures, value types, normalization, and matching aids; rule-based extraction uses `cell_id`, `bbox`, key text, paragraph text, and regex in a visible fallback order; scalar and table outputs preserve normalized value plus raw text, cell ids, bounding boxes, source, and confidence; misses return `source: not_found` and low confidence rather than hiding absence

## Result

- works as a documentation-first second context and, after YomiToku review, as cross-context reinforcement for canonical status without carrying over locale lock-in, donor parser code, OCR engine setup, LLM extraction, commercial-license posture, or bookkeeping automation
