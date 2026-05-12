# Adverse Effects Review

## Technique
- id: AOA-T-0070
- name: two-stage-document-ocr-pipeline

## Review focus
- promotion from `promoted` to `canonical` after exact-fit public reinforcement from `JaidedAI/EasyOCR`
- confirm that the bundle remains one staged OCR handoff contract, not a searchable-PDF product, model-serving recipe, OCR benchmark, template-backed field extractor, semantic media bucketer, receipt parser, or full document-understanding stack

## Failure modes
- detection misses text-bearing regions before recognition starts, so downstream extraction receives a clean-looking but incomplete handoff
- recognition output is flattened into plain text and loses bounding boxes, layout handles, or confidence
- low-confidence spans are normalized away before a reviewer or downstream extractor can inspect uncertainty
- multi-column pages, skewed scans, screenshots, receipts, or mixed scripts produce region order that looks plausible but is semantically wrong
- an engine-specific result shape leaks into the invariant handoff and makes later engine replacement expensive

## Negative effects
- staged handoff adds a small intermediate artifact where a fused end-to-end extractor may feel faster
- preserving boxes and confidence can create storage and review overhead for very simple images
- reviewers may over-trust numeric confidence if they treat OCR as final truth rather than intermediate evidence
- public OCR examples can tempt contributors to import installation, model weights, training, serving, language-pack, or benchmark details into a technique that only needs a handoff seam

## Misuse patterns
- using this bundle as a substitute for [template-backed-field-extraction-after-ocr](../../template-backed-field-extraction-after-ocr/TECHNIQUE.md) when the actual need is field semantics after OCR already exists
- using this bundle as a substitute for [semantic-media-bucketing-with-vision-plus-ocr](../../semantic-media-bucketing-with-vision-plus-ocr/TECHNIQUE.md) when the actual need is media classification with OCR as side evidence
- converting every OCR result into one plain text stream and deleting region or confidence metadata because downstream code prefers convenience
- treating one OCR engine's API, detector, recognizer, training pipeline, benchmark result, or serving topology as part of the canonical technique

## Detection signals
- reviewers cannot trace a recognized text span back to a source region, line, bounding box, or layout handle
- downstream field extraction claims merchant, amount, date, table, or class semantics before the OCR handoff is inspected
- examples center model setup, server deployment, benchmark scores, or language-pack management more than the detect/layout -> recognize -> handoff contract
- low-confidence or conflicting spans disappear from the output object
- an engine swap requires rewriting downstream extraction because the handoff was donor-specific instead of generic

## Mitigations
- preserve region, line, bounding box, or layout handles with recognized text
- carry confidence or explicit uncertainty markers into the handoff and keep low-confidence spans visible
- keep field extraction, template matching, media bucketing, review queues, and automation as separate downstream consumers
- document engine-specific APIs as examples only, not as invariant handoff law
- test the smallest handoff shape by checking that a downstream consumer can inspect source reference, text, and confidence without donor-specific runtime code

## Recommendation
- safe to promote as a canonical agent-workflow ingest technique when OCR remains staged as detect/layout first, recognition second, and one structured handoff with source references and confidence before downstream extraction or review
- keep future revisions narrow: do not absorb searchable-PDF generation, OCR serving, model training, benchmark doctrine, receipt or invoice schema law, template extraction, semantic media bucketing, deletion/cleanup policy, or total document-understanding product behavior into this bundle
