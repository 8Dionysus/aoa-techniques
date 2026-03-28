---
id: AOA-T-XXXX
name: semantic-media-bucketing-with-vision-plus-ocr
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
summary: Bucket media with image-text semantics plus OCR side text so screenshots, memes, receipts, and other media classes remain reviewable under confidence gates.
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
# semantic-media-bucketing-with-vision-plus-ocr

## Intent

Provide a bounded classification route for mixed media without pretending one multimodal model should own every downstream action.

## When to use

- you need coarse media buckets
- text-heavy images matter
- confidence-aware review is acceptable

## When not to use

- duplicate grouping is the real problem
- you need identity inference or moderation policy
- the downstream action expects perfect labels

## Inputs

- image set
- bucket taxonomy
- OCR side text
- confidence thresholds

## Outputs

- bucket labels
- confidence scores
- review bucket for uncertain cases

## Core procedure

1. run semantic image-text scoring against the chosen bucket taxonomy
2. extract OCR side text when present
3. combine visual and textual signals cautiously
4. assign only bounded bucket labels
5. route low-confidence or conflicting cases into review

## Contracts

- taxonomy stays bounded and explicit
- OCR remains a side-channel, not hidden truth
- low-confidence cases remain reviewable
- the technique does not own moderation or deletion policy

## Risks

### Failure modes

- memes and screenshots collide
- OCR text overwhelms the image signal
- receipts get mis-bucketed as generic screenshots

### Negative effects

- taxonomy creep
- confidence theater from model scores

### Misuse patterns

- using bucket labels as final truth
- letting semantic scores trigger destructive actions automatically

### Detection signals

- bucket drift across very similar images
- review queue exploding because taxonomy is too vague

### Mitigations

- small taxonomy
- review bucket
- separate destructive action policy

## Validation

- golden set of memes, receipts, screenshots, and other media
- bucket confusion review
- OCR versus no-OCR ablation

## Adaptation notes

- taxonomy wording
- model choice
- OCR usage thresholds
- language handling

## Public sanitization notes

Remove open-ended assistant claims, moderation policy, and identity inference. Keep only the bounded classification contract.

## Example

See `examples/bucket_result.seed.md`.

## Checks

See `checks/checklist.seed.md`.

## Promotion history

- born across donor vision and OCR repos
- staged for personal-ingest wave 2

## Future evolution

- meme family sub-buckets
- receipt versus banking-proof seam
- taxonomy overlays
