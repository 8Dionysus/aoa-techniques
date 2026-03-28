# Personal Ingest Wave 2 - Planting Order

This note is for operator-guided planting inside `aoa-techniques`.

## Current launch state

- activation state: `active`
- launch verdict: `go`
- current landed bundle count: `2`
- next separate landing PR should start with `perceptual-media-dedupe-with-threshold-review`

## Hard rules

- land **one** technique candidate at a time
- keep all candidates in the existing `agent-workflows` domain unless a later review proves otherwise
- do not create a new schema, new domain, or new generated surface family for this wave
- do not vendor donor code into the canonical bundle just to accelerate drafting
- do not convert auth/session/bootstrap doctrine into a technique prematurely
- do not auto-promote any candidate beyond the smallest honest maturity claim

## Preferred sequence

### Stage 1
- `two-stage-document-ocr-pipeline`
- landed as `AOA-T-0070`

Why first:
- smallest boundary
- cleanest donor seam
- easiest to keep public-safe
- opens the OCR family without forcing receipt-specific heuristics yet

### Stage 2
- `template-backed-field-extraction-after-ocr`
- landed as `AOA-T-0071`

Why second:
- naturally depends on Stage 1 outputs
- sharper once OCR handoff boundaries are explicit
- strongest applied candidate for receipts and screen proofs

### Stage 3
- `perceptual-media-dedupe-with-threshold-review`
- next active landing target for this wave

Why third:
- bounded and reviewable
- avoids multimodal classification complexity
- useful for meme and screenshot cleanup immediately

### Stage 4
- `semantic-media-bucketing-with-vision-plus-ocr`

Why fourth:
- stronger after dedupe exists
- bucket taxonomy gets cleaner once near-duplicates are handled first
- still needs stricter confidence posture than Stage 3

### Stage 5
- `telegram-export-normalization-to-local-store`

Why fifth:
- richest donor pool
- highest auth/provenance sensitivity
- benefits from the earlier OCR/media contracts already being explicit

## Explicit stop conditions

Stop and restage instead of landing if:

- the bundle needs a new domain just to stay coherent
- the wording collapses into app-specific automation rather than one reusable technique
- the technique silently assumes secret storage or account access policy
- the pattern is really a skill, playbook, memory object, or runtime module
- the candidate cannot say clearly:
  - what bounded pattern was extracted
  - what stays out
  - why it stays narrower than its donors

## Operator approval seams

Require explicit operator approval before:

- assigning a real `AOA-T-XXXX` id
- moving a seed bundle from `incoming/.../seed_bundles/` into `techniques/`
- changing `TECHNIQUE_INDEX.md`
- regenerating shared surfaces through the repo release path
