---
id: AOA-T-0073
name: semantic-media-bucketing-with-vision-plus-ocr
domain: agent-workflows
status: promoted
origin:
  project: CLIP + PaddleOCR
  path: README.md
  note: Adapted from open-source multimodal classification and OCR projects that expose image-text semantic matching plus OCR-derived text, while this bundle keeps only the bounded media-bucketing contract.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - media
  - taxonomy
  - vision
  - ocr
summary: Bucket mixed media through bounded visual semantics plus OCR side text so screenshots, memes, receipts, and other media classes remain reviewable under explicit confidence gates instead of widening into open-ended multimodal automation.
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

# semantic-media-bucketing-with-vision-plus-ocr

## Intent

Provide one bounded classification route for mixed media by combining visual semantics with OCR side text so screenshots, memes, receipts, and other coarse media classes stay reviewable under confidence gates instead of being treated as final truth.

## When to use

- a media set needs coarse bucket labels before later routing or review
- text-heavy images matter and OCR can sharpen classification
- the bucket taxonomy can stay small and explicit
- confidence-aware review is acceptable for low-signal or conflicting cases
- the reusable seam is media bucketing, not duplicate grouping, moderation, or downstream automation

## When not to use

- duplicate grouping is the real problem and taxonomy is unnecessary
- the workflow needs identity inference, moderation policy, or face recognition
- downstream actions expect perfect labels with no review seam
- the bucket set is too open-ended to remain bounded and reviewable

## Inputs

- one bounded media set
- one explicit bucket taxonomy
- one visual semantic model or equivalent scoring surface
- optional OCR side text from text-bearing images
- confidence thresholds or threshold bands

## Outputs

- one bounded bucket label per classified item
- one confidence signal for the bucket assignment
- one review bucket for low-confidence or conflicting cases
- optional notes showing whether OCR side text influenced the final label

## Core procedure

1. Score each item against the bounded bucket taxonomy through a visual semantic surface.
2. Extract OCR side text when text-bearing media may sharpen the classification.
3. Combine visual and textual signals cautiously instead of letting either channel behave as hidden final truth.
4. Assign only the explicit bounded bucket labels.
5. Route low-confidence or conflicting items into review instead of forcing a definitive class.
6. Keep moderation, deletion, and downstream automation outside the invariant contract.
7. Split out a sibling technique if the real reusable object becomes duplicate grouping, OCR extraction, or one domain-specific routing stack.

## Contracts

- taxonomy stays bounded and explicit
- OCR remains a side-channel, not hidden truth
- low-confidence or conflicting cases remain reviewable
- the technique does not own moderation, deletion, or downstream action policy
- the bundle stays smaller than open-ended multimodal assistant behavior, media-management platforms, or identity inference
- downstream systems receive bucket labels plus review signals rather than donor model internals

Relationship to adjacent techniques: unlike [AOA-T-0072](../perceptual-media-dedupe-with-threshold-review/TECHNIQUE.md), this bundle classifies media into coarse semantic buckets rather than grouping likely duplicates. Unlike [AOA-T-0070](../two-stage-document-ocr-pipeline/TECHNIQUE.md), it does not own OCR staging as a reusable handoff and only uses OCR as an optional side-channel for classification. Unlike [AOA-T-0071](../template-backed-field-extraction-after-ocr/TECHNIQUE.md), it does not extract structured fields from OCR text.

## Risks

### Failure modes

- memes and screenshots collide in the same bucket
- OCR text overwhelms the visual signal
- receipts are mis-bucketed as generic screenshots
- vague taxonomy wording creates unstable classifications

### Negative effects

- taxonomy creep turns one bounded classifier into a loose media ontology
- confidence scores can create false certainty
- downstream systems may over-trust bucket labels as final truth

### Misuse patterns

- using bucket labels as final truth for destructive actions
- letting semantic scores trigger deletion, moderation, or routing automatically
- widening the technique into identity inference or open-ended multimodal assistance

### Detection signals

- bucket drift across very similar images
- the review queue explodes because taxonomy is too vague
- OCR-heavy items flip labels unpredictably when text changes slightly

### Mitigations

- keep the taxonomy small and explicit
- use a review bucket for low-confidence or conflicting cases
- preserve OCR as a bounded side-channel rather than final authority
- keep destructive action policy separate from classification

## Validation

Verify the technique by confirming that:
- the golden set includes memes, receipts, screenshots, and an `other` class
- bucket labels stay inside the bounded taxonomy
- low-confidence or conflicting cases route into review
- OCR versus no-OCR comparisons do not silently widen the contract into OCR-first truth
- moderation, deletion, and identity inference remain outside the technique

See `checks/semantic-media-bucketing-with-vision-plus-ocr-checklist.md`.

## Adaptation notes

What can vary across projects:
- taxonomy wording
- visual model choice
- OCR usage thresholds
- language handling
- confidence bands and review thresholds

What should stay invariant:
- taxonomy remains bounded
- visual semantics remain primary and OCR stays side-channel
- low-confidence cases remain reviewable
- the output is a classification surface rather than a downstream action verdict

Project-shaped details that should not be treated as invariant:
- donor prompt phrasing or zero-shot label engineering
- moderation rules
- face or identity inference
- delete, archive, or auto-routing policy

## Public sanitization notes

This public bundle keeps only the reusable classification seam: a bounded taxonomy is scored through visual semantics, OCR may contribute side text, uncertainty remains visible, and later actions stay outside the technique. Open-ended assistant claims, moderation policy, identity inference, and donor model-serving detail were intentionally removed or generalized.

## Example

See `examples/minimal-semantic-media-bucketing-with-vision-plus-ocr.md`.

## Checks

See `checks/semantic-media-bucketing-with-vision-plus-ocr-checklist.md`.

## Promotion history

- adapted from open-source `CLIP` and `PaddleOCR`
- landed from `personal-ingest-wave-2`
- promoted into `aoa-techniques` on 2026-03-28 as a bounded external-import technique for confidence-aware mixed-media bucketing

## Future evolution

- keep duplicate grouping and OCR extraction separate unless narrower bridge seams prove reusable
- split receipt-versus-proof or meme-family overlays only if those contracts survive independently
- add a stronger second live context if another public workflow keeps semantic bucketing explicit before later routing or cleanup actions
