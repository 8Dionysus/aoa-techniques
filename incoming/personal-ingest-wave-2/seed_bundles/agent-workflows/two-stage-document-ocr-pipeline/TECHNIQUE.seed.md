---
id: AOA-T-XXXX
name: two-stage-document-ocr-pipeline
domain: agent-workflows
status: draft-seed
origin: personal-ingest-wave-2
note: seed bundle staged for operator-guided external import
owners:
  - 8Dionysus
tags:
  - reusable
  - public
  - agent-friendly
  - personal-ingest
summary: Stage OCR as detect/layout -> recognize -> structured handoff so downstream extraction stays interchangeable and reviewable.
maturity_score: 1
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: donor_soil
export_ready: false
relations: []
evidence:
  - kind: external_origin
    path: notes/external-origin.seed.md
---
# two-stage-document-ocr-pipeline

## Intent

Turn raw screenshots, scans, or document images into a reviewable OCR handoff without collapsing OCR, extraction, and application-specific logic into one opaque step.

## When to use

- you need OCR output that can feed later field extraction
- layout ambiguity matters
- you want the OCR layer to stay replaceable

## When not to use

- you already have structured source data
- the flow is really template extraction rather than OCR staging
- you need end-to-end app automation rather than a bounded OCR technique

## Inputs

- document or screenshot image(s)
- optional crop or page boundaries
- optional language or locale hints

## Outputs

- recognized text units
- layout or region handles
- confidence-aware handoff surface for later extraction

## Core procedure

1. detect or segment text-bearing regions
2. recognize text per region or line
3. normalize a minimal structured handoff format
4. mark low-confidence spans explicitly
5. route only the OCR handoff forward, not donor-specific runtime behavior

## Contracts

- OCR output stays separate from field extraction logic
- low-confidence spans remain visible
- the technique does not assume one specific OCR engine forever
- layout ambiguity is preserved rather than silently flattened

## Risks

### Failure modes

- cropped or skewed screenshots lose key fields
- multi-column or receipt layouts flatten incorrectly

### Negative effects

- false confidence from clean-looking OCR text
- premature normalization erases evidence of ambiguity

### Misuse patterns

- treating OCR output as ground truth
- hiding OCR uncertainty before extraction

### Detection signals

- sudden merchant/date/amount gaps downstream
- field extractors overfitting to broken OCR text

### Mitigations

- keep region handles
- emit low-confidence spans
- preserve source reference for review

## Validation

- run on mixed screenshots and scans
- check that low-confidence spans remain visible
- confirm downstream extractor can consume the handoff without donor-specific code

## Adaptation notes

- OCR engine choice
- language packs
- device screenshot conventions
- storage paths

## Public sanitization notes

Remove donor-specific deployment, benchmarks, and framework packaging. Keep only the staged OCR contract.

## Example

See `examples/minimal_pipeline.seed.md`.

## Checks

See `checks/checklist.seed.md`.

## Promotion history

- born in donor OCR/document repos
- staged for personal-ingest wave 2

## Future evolution

- receipt-specific OCR variants
- screen-text versus paper-text calibration
- review bucket instrumentation
