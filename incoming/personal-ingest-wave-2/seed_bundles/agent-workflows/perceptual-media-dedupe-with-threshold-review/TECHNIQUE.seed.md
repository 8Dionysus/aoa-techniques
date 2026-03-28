---
id: AOA-T-XXXX
name: perceptual-media-dedupe-with-threshold-review
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
summary: Group near-duplicate media through perceptual similarity and route uncertain matches into review instead of silent deletion or one-threshold dogma.
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
# perceptual-media-dedupe-with-threshold-review

## Intent

Make image cleanup reviewable and bounded when screenshots, memes, or photos contain duplicates, crops, or slight edits.

## When to use

- you need to deduplicate screenshots or memes
- near-duplicates matter
- review buckets are acceptable

## When not to use

- exact hashes alone are enough
- you need semantic classification rather than duplicate grouping
- the workflow assumes auto-delete with no review

## Inputs

- image set
- similarity thresholds
- optional grouping strategy

## Outputs

- duplicate groups
- uncertain groups
- review bucket

## Core procedure

1. compute perceptual similarity handles
2. form candidate duplicate groups
3. separate high-confidence duplicate groups from uncertain groups
4. emit review bucket instead of deleting uncertain matches
5. only apply follow-up file actions outside the technique

## Contracts

- this technique groups and flags duplicates; it does not own file deletion policy
- thresholds remain explicit and tunable
- uncertain matches stay visible
- grouping remains reviewable

## Risks

### Failure modes

- edited memes collapse into wrong groups
- cropped screenshots become false duplicates

### Negative effects

- aggressive cleanup removes meaningful variants
- operators over-trust one threshold

### Misuse patterns

- auto-deleting all grouped images
- using duplicate groups as semantic labels

### Detection signals

- high duplicate counts with obvious false matches
- loss of variant images users expected to keep

### Mitigations

- review bucket
- separate action policy
- threshold calibration by media family

## Validation

- small corpus with exact dupes, crops, and edited variants
- manual spot-check of uncertain groups
- threshold sensitivity test

## Adaptation notes

- hash or embedding family
- thresholds by media type
- storage layout

## Public sanitization notes

Remove bulk-delete posture and donor-specific CLI usage. Keep the bounded grouping-and-review contract.

## Example

See `examples/duplicate_group.seed.md`.

## Checks

See `checks/checklist.seed.md`.

## Promotion history

- born in donor dedupe tools
- staged for personal-ingest wave 2

## Future evolution

- video frame dedupe
- sidecar duplicate manifests
- cross-device screenshot cleanup
