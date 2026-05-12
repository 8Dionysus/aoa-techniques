# Adverse Effects Review

## Technique
- id: AOA-T-0071
- name: template-backed-field-extraction-after-ocr

## Review focus
- promotion from `promoted` to `canonical` after exact-fit public reinforcement from `kotaro-kinoshita/yomitoku`
- confirm that the bundle remains one post-OCR field-extraction contract, not an OCR engine, layout analyzer, schema product, LLM extraction service, receipt or invoice application, locale doctrine, bookkeeping workflow, or full document-understanding stack

## Failure modes
- OCR handoff text is incomplete or misordered, but field extraction emits a clean object that hides the upstream defect
- a template or heuristic matches the wrong nearby value, such as subtotal instead of total or issue date instead of transaction date
- missing fields become empty strings, defaults, or nulls without review posture, making absence look intentional
- conflicting candidates are collapsed too early because the extractor prefers the first match, highest amount, or nearest label without preserving alternatives
- field-evidence references are dropped, so reviewers cannot trace merchant, date, amount, or currency values back to OCR text, cells, boxes, or source snippets

## Negative effects
- explicit field schemas and evidence metadata add maintenance overhead for small one-off documents
- template packs can grow into quiet local doctrine if nobody reviews why each field exists
- downstream systems may over-trust a bounded field object as final accounting truth
- schema, regex, or locale choices can encode regional assumptions that look universal when moved into a public technique
- a strong external extractor example can tempt contributors to import OCR, layout, LLM, model-serving, or licensing concerns into a smaller post-OCR seam

## Misuse patterns
- using this bundle as a substitute for [two-stage-document-ocr-pipeline](../../two-stage-document-ocr-pipeline/TECHNIQUE.md) when the actual problem is text-region detection, recognition, confidence, or OCR handoff shape
- treating one receipt, invoice, or form template as universal document law
- replacing missing or conflicting markers with guessed values because downstream code expects every field to be present
- widening the field object into bookkeeping, reimbursement, tax, duplicate handling, storage, cleanup, or ingestion automation
- copying a donor product's schema language, model setup, app flow, or license posture into the invariant technique

## Detection signals
- extracted fields have values but no source snippets, raw text, OCR handles, cell ids, bounding boxes, or equivalent evidence references
- the output cannot distinguish absent, low-confidence, conflicting, and confidently extracted fields
- examples center full OCR setup, LLM prompts, accounting export, or app workflow more than the post-OCR field contract
- adding a new merchant, invoice family, locale, or form forces broad changes to the technique instead of local template or heuristic changes
- reviewers cannot explain why the field set is small enough to review

## Mitigations
- keep OCR staging upstream and consume only the explicit OCR or layout handoff
- keep the field set small, named, and reviewable before extraction starts
- preserve source evidence or confidence where review may need to inspect a chosen value
- emit missing and conflicting results explicitly instead of backfilling defaults
- keep templates, heuristics, regexes, and schema hints local to the bounded field family
- route unresolved cases into review and stop before bookkeeping or ingestion automation begins

## Recommendation
- safe to promote as a canonical agent-workflow ingest technique when OCR-derived text is already available, target fields are explicit, templates or heuristics stay visible, and missing or conflicting results remain reviewable
- keep future revisions narrow: do not absorb OCR engines, layout analyzers, LLM extraction services, model setup, schema products, locale policy, accounting flows, duplicate handling, storage automation, cleanup actions, or total document-understanding product behavior into this bundle
