# Personal Media Ingest

This root is the repo-native evidence packet for the personal-ingest donor
family inside `incoming/`.

## Current State

- activation state: `evidence-only`
- launch verdict: `go`
- current wave split: `5 landed / 0 staged / 1 closed-no-import`
- next separate landing candidate: none; the first-pass landing queue is exhausted
- final non-import verdict: `telegram-account-auth-and-session-bridge`
- no active non-landed tail remains in this packet

This wave does **not** assume merge authority.
It does **not** claim these candidates are already canonical.
It keeps donor intake, candidate bundles, and Codex handoff instructions explicit and separate.

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
- staged in this packet:
  - none; all first-pass landing candidates are now landed
- closed non-import outside the landing lane:
  - `telegram-account-auth-and-session-bridge` with final rationale in `docs/TELEGRAM_ACCOUNT_AUTH_AND_SESSION_BRIDGE_CLOSEOUT_MEMO.md`

## Main surfaces

- `docs/EXTERNAL_TECHNIQUE_CANDIDATES_PERSONAL_MEDIA_INGEST.md`
  - intake and decision surface for the personal-ingest donor family
- `docs/PERSONAL_MEDIA_INGEST_PLANTING_ORDER.md`
  - wave order, launch verdict, and stop conditions
- `support/manifest.json`
  - repo-native wave metadata and activation state
- `support/registry.json`
  - authoritative machine-readable candidate queue for this wave
- `support/CODEX_HANDOFF.md`
  - Codex-facing operator path
The old packet-local seed bundles were removed after their landed counterparts
became real `techniques/**/TECHNIQUE.md` bundles. Current technique meaning now
lives only in the canonical bundles.

## Operator intent

Use this wave when the question is:

> "Which bounded personal-ingest candidate already landed, and why was the
> auth/session bridge closed out?"

Do **not** use this wave as if it authorizes direct merge.
The staging surfaces are evidence and final packet verdicts. Canonical status
still belongs to the repo's normal review path.
