# Personal Ingest Wave 2

This root is the repo-native staging wave for the personal-ingest donor family inside `incoming/`.

## Current State

- activation state: `active`
- launch verdict: `go`
- current wave split: `5 landed / 0 staged / 1 incubation hold`
- next separate landing candidate: none; the first-pass landing queue is exhausted
- immediate exclusion from the landing lane: `telegram-account-auth-and-session-bridge`
- one incubation-hold candidate with a current memo

This wave does **not** assume merge authority.
It does **not** claim these candidates are already canonical.
It keeps donor intake, seed bundles, and Codex handoff instructions explicit and separate.

## Why this shape

The current `aoa-techniques` repo distinguishes:

- donor intake and refinement posture
- external import runbook
- template-based technique drafting
- one-technique-at-a-time landing

This wave follows that posture instead of pretending the candidates are already landed.

## What This Wave Tracks

- landed from this wave:
  - `AOA-T-0070 two-stage-document-ocr-pipeline`
  - `AOA-T-0071 template-backed-field-extraction-after-ocr`
  - `AOA-T-0072 perceptual-media-dedupe-with-threshold-review`
  - `AOA-T-0073 semantic-media-bucketing-with-vision-plus-ocr`
  - `AOA-T-0074 telegram-export-normalization-to-local-store`
- still staged in this wave:
  - none; all first-pass landing candidates are now landed
- incubation hold outside the landing lane:
  - `telegram-account-auth-and-session-bridge` with a current memo in `docs/TELEGRAM_ACCOUNT_AUTH_AND_SESSION_BRIDGE_NARROWING_MEMO.md`

## Main surfaces

- `docs/EXTERNAL_TECHNIQUE_CANDIDATES_PERSONAL_INGEST_WAVE_2.md`
  - intake and decision surface for the personal-ingest donor family
- `docs/PERSONAL_INGEST_WAVE_2_PLANTING_ORDER.md`
  - wave order, launch verdict, and stop conditions
- `support/manifest.json`
  - repo-native wave metadata and activation state
- `support/registry.json`
  - authoritative machine-readable candidate queue for this wave
- `support/CODEX_HANDOFF.md`
  - Codex-facing operator path
- `seed_bundles/agent-workflows/*`
  - seed technique bundles, not yet canonical bundles

## Operator intent

Use this wave when the question is:

> "Which bounded personal-ingest technique candidate should we distill next, and how do we let Codex plant it without losing control?"

Do **not** use this wave as if it authorizes direct merge.
The staging surfaces are soil and scaffolding.
Canonical status still belongs to the repo's normal review path.
