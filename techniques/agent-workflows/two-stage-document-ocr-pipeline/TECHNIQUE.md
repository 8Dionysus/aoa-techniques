---
id: AOA-T-0070
name: two-stage-document-ocr-pipeline
domain: agent-workflows
status: promoted
origin:
  project: PaddleOCR + docTR
  path: README.md
  note: Adapted from the open-source PaddleOCR and docTR projects, which keep document OCR as an explicit detect/layout plus recognize flow before downstream extraction or app-specific interpretation.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - ocr
  - documents
  - handoff
  - confidence
summary: Stage OCR as detect or layout -> recognize -> structured handoff so downstream extraction stays reviewable, interchangeable, and confidence-aware instead of collapsing OCR and field logic into one opaque step.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-28
export_ready: true
relations: []
evidence:
  - kind: external_origin
    path: notes/external-origin.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: external_review
    path: notes/external-import-review.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# two-stage-document-ocr-pipeline

## Intent

Turn screenshots, scans, or document images into a bounded OCR handoff by keeping text-region detection or layout analysis separate from text recognition before any field extraction, parsing, or application-specific logic starts.

## When to use

- a later stage needs OCR output as an explicit intermediate object rather than hidden inside end-to-end extraction
- layout ambiguity matters and should stay reviewable
- OCR engines may change over time while the downstream handoff contract should stay stable
- low-confidence spans or region-level uncertainty need to remain visible before extraction or review
- the reusable object is staged OCR handoff, not a full receipt parser, document-understanding stack, or app automation flow

## When not to use

- the source is already structured and OCR is unnecessary
- the real reusable object is post-OCR field extraction rather than OCR staging
- the workflow only makes sense as one end-to-end product pipeline with domain-specific business logic fused into OCR
- the main need is model-serving, benchmarking, or framework packaging rather than one reviewable OCR contract

## Inputs

- one image, page, screenshot, or bounded document slice
- optional crop, page, or region boundaries
- optional language, script, or locale hints
- one OCR stage that can expose region or layout handles before recognition

## Outputs

- one structured OCR handoff object with recognized text units
- one bounded set of region, line, or layout handles that preserve where text came from
- explicit low-confidence spans or segments
- one downstream-ready surface for later extraction without donor-specific runtime code

## Core procedure

1. Detect text-bearing regions or derive a bounded layout view before treating recognition as complete.
2. Recognize text per region, line, or equivalent bounded segment.
3. Normalize a minimal structured handoff that preserves source references, recognized text, and confidence.
4. Mark low-confidence spans explicitly instead of silently flattening uncertainty away.
5. Pass only the OCR handoff forward to downstream extraction or review.
6. Keep engine choice, serving posture, and app-specific extraction logic outside the invariant contract.
7. Split out a sibling technique if the real reusable object becomes template extraction, semantic bucketing, or automation over the OCR results.

## Contracts

- OCR staging stays separate from downstream field extraction and app logic
- region, line, or layout ambiguity remains visible enough for review
- low-confidence spans remain explicit
- the handoff stays small enough that OCR engines can change without rewriting the whole workflow contract
- the technique does not widen into model-serving doctrine, benchmarking, framework packaging, or receipt-specific schema law
- downstream systems consume one structured OCR handoff rather than donor-specific runtime internals

Relationship to adjacent techniques: unlike a later template or heuristic extraction technique, this bundle stops at OCR handoff rather than asserting merchant, amount, date, or field semantics. Unlike semantic media bucketing or dedupe techniques, it stays on document text extraction rather than media taxonomy or duplicate review.

## Risks

### Failure modes

- skewed, cropped, or noisy inputs lose important text regions before recognition
- multi-column or receipt-like layouts flatten incorrectly into one text stream
- downstream consumers treat a clean-looking OCR result as if it were certain ground truth
- low-confidence spans disappear during normalization

### Negative effects

- premature normalization can hide ambiguity that later field extraction needed to see
- a small OCR handoff can feel less convenient than one fused end-to-end extractor
- teams may overfit downstream logic to one donor engine if the handoff shape is not kept generic

### Misuse patterns

- treating OCR output as final truth instead of a bounded intermediate object
- widening the technique into receipt parsing, invoice schema doctrine, or end-to-end document automation
- silently deleting region or confidence metadata because downstream code prefers plain text

### Detection signals

- downstream amount, date, or merchant extraction fails unexpectedly after OCR looked superficially clean
- reviewers cannot recover where a text span came from in the source image
- engine-specific output details leak into the invariant handoff contract

### Mitigations

- preserve region or layout handles with the recognized text
- keep low-confidence spans explicit in the handoff
- treat OCR output as reviewable intermediate evidence rather than final structured truth
- keep extraction, bucketing, and automation as separate layers

## Validation

Verify the technique by confirming that:
- OCR handoff remains distinct from downstream extraction logic
- region or layout references survive into the handoff
- low-confidence spans remain visible
- the handoff shape can be consumed without donor-specific runtime code
- the description still makes sense without model-serving, benchmarking, or app-specific automation doctrine

See `checks/two-stage-document-ocr-pipeline-checklist.md`.

## Adaptation notes

What can vary across projects:
- the OCR engine or engine pair
- the exact region, line, or layout representation
- language packs or locale hints
- storage paths for source images and OCR handoff artifacts
- whether the downstream consumer is a template extractor, reviewer, or another bounded processor

What should stay invariant:
- OCR remains staged as detect/layout then recognize
- confidence and ambiguity remain visible
- the output is one structured OCR handoff rather than fused business logic
- engine-specific runtime behavior stays outside the invariant core

Project-shaped details that should not be treated as invariant:
- benchmark claims
- serving topology
- receipt-only or invoice-only schema assumptions
- LLM wrapper posture or agent-control rhetoric

## Public sanitization notes

This public bundle keeps only the reusable staged OCR contract: text-bearing regions or layout are surfaced before recognition, uncertainty stays visible, and downstream extraction consumes one structured handoff. Donor-specific serving posture, framework packaging, benchmark claims, and app-specific document logic were intentionally removed or generalized.

## Example

See `examples/minimal-two-stage-document-ocr-pipeline.md`.

## Checks

See `checks/two-stage-document-ocr-pipeline-checklist.md`.

## Promotion history

- adapted from open-source `PaddleOCR` and `docTR`
- landed from `personal-ingest-wave-2`
- promoted into `aoa-techniques` on 2026-03-28 as a bounded external-import technique for staged OCR handoff

## Future evolution

- keep template-backed extraction separate unless a narrower bridge seam proves reusable
- split out receipt-specific or form-specific extraction siblings only if their field semantics survive independently
- add a stronger second live context if another public workflow keeps OCR staging explicit before later extraction or review
