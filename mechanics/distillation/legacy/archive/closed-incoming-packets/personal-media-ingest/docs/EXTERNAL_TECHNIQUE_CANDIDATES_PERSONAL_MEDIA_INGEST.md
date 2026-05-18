# External Technique Candidates - Personal Media Ingest

This doc records the **personal-ingest donor family** staged as a second-wave import program for `aoa-techniques`.

Use it when the question is not:

> "which landed technique should I open?"

but:

> "which bounded personal-ingest candidate already landed, and which one closed without import?"

This is an intake and decision surface.
It does **not** change technique status, create a canonical bundle, or authorize import by itself.

## Scope

- this doc tracks the `6` personal-ingest donor-derived candidates staged in this pack
- it keeps **all** candidates inside the current repo-owned domain map by using tentative `agent-workflows` placement only
- it avoids schema growth, new domains, and generated-surface expansion until a candidate is actually landed
- it treats donor repositories as **origin soil**, not as canon or vendored implementation

## Doctrine Seam

- if something is already a reusable, bounded, public-safe technique, its canonical home is `aoa-techniques`
- neighboring repos may incubate the live workflow, auth posture, memory writeback, or scenario method, but they do not become the long-term owner of the reusable technique canon
- these verdicts therefore do **not** mean "another repo should own the technique instead"
- they mean one of four narrower things:
  - the technique looks like a good next-wave import here
  - the candidate was closed because it still overlaps a broader workflow
  - the source pattern was closed because it is still auth, substrate, or scenario behavior instead of a bounded technique

## How To Read The Verdicts

- `landed from this wave`
  - the candidate already completed one bounded import pass from this wave and now has a real `TECHNIQUE.md` bundle in the live corpus
- `closed-no-import`
  - the pattern remains useful evidence, but this packet no longer owns an active import lane for it
- `substrate or architecture pattern, not technique-shaped`
  - the idea is still too runtime-shaped or control-plane-shaped to behave like one bounded technique bundle

## Current Summary

- launch verdict: `go`
- activation state: `evidence-only`
- `0` staged candidates with candidate bundles
- `5` landed candidates
- `1` closed-no-import candidate outside the landing lane
- registry mapping: `AOA-T-0070 two-stage-document-ocr-pipeline`, `AOA-T-0071 template-backed-field-extraction-after-ocr`, `AOA-T-0072 perceptual-media-dedupe-with-threshold-review`, `AOA-T-0073 semantic-media-bucketing-with-vision-plus-ocr`, and `AOA-T-0074 telegram-export-normalization-to-local-store` are tracked as `landed`, and `telegram-account-auth-and-session-bridge` is tracked as `closed-no-import`
- closeout memo: [TELEGRAM_ACCOUNT_AUTH_AND_SESSION_BRIDGE_CLOSEOUT_MEMO.md](TELEGRAM_ACCOUNT_AUTH_AND_SESSION_BRIDGE_CLOSEOUT_MEMO.md)

## Current Wave Placement

### Wave 2A - OCR and structured receipt extraction

1. `two-stage-document-ocr-pipeline`
   - tentative domain: `agent-workflows`
   - verdict: `landed from this wave`
   - landed bundle:
     - [AOA-T-0070](../../../../../../../techniques/ingest/media-ingest/two-stage-document-ocr-pipeline/TECHNIQUE.md)
   - donor spine:
     - `PaddleOCR`
     - `docTR`
   - extracted pattern:
     - keep OCR as an explicit staged route: detect/layout -> recognize -> structured handoff
   - keep out:
     - model-serving doctrine
     - benchmark theater
     - framework-specific runtime packaging
     - LLM wrapper posture
   - next move:
     - keep Pack 27 proof work separate until a second live adopter exists beyond the donor OCR pair plus this repo-local adaptation

2. `template-backed-field-extraction-after-ocr`
   - tentative domain: `agent-workflows`
   - verdict: `landed from this wave`
   - landed bundle:
     - [AOA-T-0071](../../../../../../../techniques/ingest/media-ingest/template-backed-field-extraction-after-ocr/TECHNIQUE.md)
   - donor spine:
     - `invoice2data`
     - `receiptparser`
     - `receipt-parser-legacy`
   - extracted pattern:
     - normalize structured fields after OCR through explicit templates, heuristics, and fallback review paths
   - keep out:
     - invoice-only schema assumptions as universal law
     - locale-locked merchant logic
     - donor-specific parser code as canon
   - next move:
     - keep Pack 28 proof work separate until a second live adopter exists beyond the donor parser family plus this repo-local adaptation

### Wave 2B - media clustering and pruning

3. `perceptual-media-dedupe-with-threshold-review`
   - tentative domain: `agent-workflows`
   - verdict: `landed from this wave`
   - landed bundle:
     - [AOA-T-0072](../../../../../../../techniques/ingest/media-ingest/perceptual-media-dedupe-with-threshold-review/TECHNIQUE.md)
   - donor spine:
     - `imagededup`
     - `imgdupes`
   - extracted pattern:
     - detect near-duplicate images through perceptual similarity and route uncertain matches into review instead of silent deletion
   - keep out:
     - bulk-delete behavior
     - one-threshold-fits-all claims
     - ranking or quality-scoring doctrine
   - next move:
     - keep Pack 29 proof work separate until a second live adopter exists beyond the donor dedupe family plus this repo-local adaptation

4. `semantic-media-bucketing-with-vision-plus-ocr`
   - tentative domain: `agent-workflows`
   - verdict: `landed from this wave`
   - landed bundle:
     - [AOA-T-0073](../../../../../../../techniques/ingest/media-ingest/semantic-media-bucketing-with-vision-plus-ocr/TECHNIQUE.md)
   - donor spine:
     - `CLIP`
     - `PaddleOCR`
   - extracted pattern:
     - combine image-text semantics and OCR text to separate memes, receipts, screenshots, and other media buckets with confidence-aware review
   - keep out:
     - open-ended multimodal assistant claims
     - hidden moderation policy
     - identity or face inference
   - next move:
     - keep Pack 30 proof work separate until a second live adopter exists beyond the donor classification family plus this repo-local adaptation

### Wave 2C - Telegram export and normalization

5. `telegram-export-normalization-to-local-store`
   - tentative domain: `agent-workflows`
   - verdict: `landed from this wave`
   - landed bundle:
     - [AOA-T-0074](../../../../../../../techniques/ingest/media-ingest/telegram-export-normalization-to-local-store/TECHNIQUE.md)
   - donor spine:
     - `Telethon`
     - `TDLib`
     - `opentele`
     - `Chatistics`
     - `tg-archive`
     - `telegram-mcp`
   - extracted pattern:
     - turn Telegram messages and media into a local, resumable, provenance-preserving normalized store without collapsing auth posture into memory or agent autonomy
   - keep out:
     - session-secret storage policy
     - auth bootstrap doctrine
     - agent-control rhetoric
     - automatic memory writeback
   - next move:
     - keep Pack 31 proof work separate until a second live adopter exists beyond the donor Telegram family plus this repo-local adaptation

### Closed Non-Import

6. `telegram-account-auth-and-session-bridge`
   - tentative domain: `agent-workflows` only after heavy narrowing
   - verdict: `closed-no-import`
   - closeout memo:
     - [TELEGRAM_ACCOUNT_AUTH_AND_SESSION_BRIDGE_CLOSEOUT_MEMO.md](TELEGRAM_ACCOUNT_AUTH_AND_SESSION_BRIDGE_CLOSEOUT_MEMO.md)
   - donor spine:
     - `Telethon`
     - `opentele`
     - `telegram-mcp`
   - reason:
     - the current pattern still mixes account access, secret handling, session conversion, operator approval, and runtime control-plane behavior
   - what would need fresh evidence before a new intake:
     - one bounded session-bridge contract
     - one approval-gated auth handoff pattern
   - what must stay out:
     - secret storage policy
     - live runtime control
     - remote agent authority
     - general Telegram ops doctrine

## Recommended Landing Order

1. `two-stage-document-ocr-pipeline`
   - landed as `AOA-T-0070`
2. `template-backed-field-extraction-after-ocr`
   - landed as `AOA-T-0071`
3. `perceptual-media-dedupe-with-threshold-review`
   - landed as `AOA-T-0072`
4. `semantic-media-bucketing-with-vision-plus-ocr`
   - landed as `AOA-T-0073`
5. `telegram-export-normalization-to-local-store`
   - landed as `AOA-T-0074`

Keep `telegram-account-auth-and-session-bridge` out of the immediate wave.
Use [TELEGRAM_ACCOUNT_AUTH_AND_SESSION_BRIDGE_CLOSEOUT_MEMO.md](TELEGRAM_ACCOUNT_AUTH_AND_SESSION_BRIDGE_CLOSEOUT_MEMO.md) as the final packet rationale.

## Retired Bundle Seed Coverage

Seed bundles were provided for:

- `two-stage-document-ocr-pipeline`
- `template-backed-field-extraction-after-ocr`
- `perceptual-media-dedupe-with-threshold-review`
- `semantic-media-bucketing-with-vision-plus-ocr`
- `telegram-export-normalization-to-local-store`

Those packet-local seed bundles were removed after the corresponding canonical
bundles landed as `AOA-T-0070` through `AOA-T-0074`.

The auth/session bridge is documented only as a closed non-import verdict.
