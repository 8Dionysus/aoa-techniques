# External Technique Candidates - Personal Ingest Wave 2

This doc records the **personal-ingest donor family** staged as a second-wave import program for `aoa-techniques`.

Use it when the question is not:

> "which landed technique should I open?"

but:

> "which bounded personal-ingest candidate should we distill next, and which ones still need narrowing or layer incubation first?"

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
  - the candidate still needs one more narrowing pass before extraction here
  - the candidate still overlaps a broader workflow and should stay separated
  - the source pattern is still auth, substrate, or scenario behavior and is not yet technique-shaped

## How To Read The Verdicts

- `future import here`
  - the pattern already looks like a plausible bounded `aoa-techniques` bundle, but still needs one more narrowing pass before drafting under `techniques/`
- `landed from this wave`
  - the candidate already completed one bounded import pass from this wave and now has a real `TECHNIQUE.md` bundle in the live corpus
- `hold because overlap`
  - the pattern is real, but the current boundary with a sibling candidate is not sharp enough yet
- `needs layer incubation before distillation here`
  - the pattern still mixes auth, runtime, role, or secret posture and needs one more clean contract pass before becoming a technique bundle
- `substrate or architecture pattern, not yet a technique`
  - the idea is still too runtime-shaped or control-plane-shaped to behave like one bounded technique bundle

## Current Summary

- launch verdict: `go`
- activation state: `active`
- `3` staged candidates with seed bundles
- `2` landed candidates
- `1` incubation hold outside the immediate landing lane
- registry mapping: `AOA-T-0070 two-stage-document-ocr-pipeline` and `AOA-T-0071 template-backed-field-extraction-after-ocr` are tracked as `landed`, the three remaining `future import here` candidates are tracked as `staged` in `support/registry.json`, and `telegram-account-auth-and-session-bridge` remains an incubation hold

## Current Wave Placement

### Wave 2A - OCR and structured receipt extraction

1. `two-stage-document-ocr-pipeline`
   - tentative domain: `agent-workflows`
   - verdict: `landed from this wave`
   - landed bundle:
     - [AOA-T-0070](../../../techniques/agent-workflows/two-stage-document-ocr-pipeline/TECHNIQUE.md)
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
     - [AOA-T-0071](../../../techniques/agent-workflows/template-backed-field-extraction-after-ocr/TECHNIQUE.md)
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
   - verdict: `future import here`
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
     - land after duplicate-group contract, threshold tuning, and review bucket semantics are explicit

4. `semantic-media-bucketing-with-vision-plus-ocr`
   - tentative domain: `agent-workflows`
   - verdict: `future import here`
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
     - land only after bucket taxonomy, confidence gates, and no-auto-delete posture are explicit

### Wave 2C - Telegram export and normalization

5. `telegram-export-normalization-to-local-store`
   - tentative domain: `agent-workflows`
   - verdict: `future import here`
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
     - land after the normalized object contract is explicit: message id, timestamp, sender, reply edge, media refs, source path

### Incubation Hold

6. `telegram-account-auth-and-session-bridge`
   - tentative domain: `agent-workflows` only after heavy narrowing
   - verdict: `needs layer incubation before distillation here`
   - donor spine:
     - `Telethon`
     - `opentele`
     - `telegram-mcp`
   - reason:
     - the current pattern still mixes account access, secret handling, session conversion, operator approval, and runtime control-plane behavior
   - what may later survive extraction:
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
4. `semantic-media-bucketing-with-vision-plus-ocr`
5. `telegram-export-normalization-to-local-store`

Keep `telegram-account-auth-and-session-bridge` out of the immediate wave.

## Bundle Seed Coverage In This Pack

Seed bundles are provided for:

- `two-stage-document-ocr-pipeline`
- `template-backed-field-extraction-after-ocr`
- `perceptual-media-dedupe-with-threshold-review`
- `semantic-media-bucketing-with-vision-plus-ocr`
- `telegram-export-normalization-to-local-store`

The auth/session bridge is documented only as an incubation hold.
