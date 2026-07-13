# Media-Ingest Tree Pilot Receipt

Date: 2026-05-04

## Status

Landed.

## Scope

This receipt preserves the third authored path migration for the technique tree
pilot.

Reviewed packet:
`mechanics/distillation/parts/technique-reform-ingress/reviews/media-ingest-direct-read-migration-review.md`

Tree contract:
`docs/TECHNIQUE_TREE_CONTRACT.md`

## Moves

| Technique | Old path | New path |
|---|---|---|
| `AOA-T-0070` | `techniques/agent-workflows/two-stage-document-ocr-pipeline/` | `techniques/ingest/media-ingest/two-stage-document-ocr-pipeline/` |
| `AOA-T-0071` | `techniques/agent-workflows/template-backed-field-extraction-after-ocr/` | `techniques/ingest/media-ingest/template-backed-field-extraction-after-ocr/` |
| `AOA-T-0072` | `techniques/agent-workflows/perceptual-media-dedupe-with-threshold-review/` | `techniques/ingest/media-ingest/perceptual-media-dedupe-with-threshold-review/` |
| `AOA-T-0073` | `techniques/agent-workflows/semantic-media-bucketing-with-vision-plus-ocr/` | `techniques/ingest/media-ingest/semantic-media-bucketing-with-vision-plus-ocr/` |
| `AOA-T-0074` | `techniques/agent-workflows/telegram-export-normalization-to-local-store/` | `techniques/ingest/media-ingest/telegram-export-normalization-to-local-store/` |

## Preservation Rule

Active technique bundles moved directly from old authored homes to new authored
homes. They did not pass through root `legacy/`.

Root legacy preserves only this migration accounting.

## Invariants

- Keep bundle IDs unchanged.
- Keep `domain`, `kind`, `status`, owners, evidence, relations, checklists,
  examples, notes, and public-safety posture unchanged.
- Do not add `tree_path` frontmatter.
- Do not move any other shelf in this wave.
- Do not treat `media-ingest` as global ingest canon beyond this validated
  pilot.
- Keep the five leaf bundles separate rather than merging them into one ingest
  pipeline.
- Keep `telegram-account-auth-and-session-bridge` outside the migrated shelf.

## Validation

- the release lane passed after rebuilding generated surfaces,
  running the full unittest suite, validating nested `AGENTS.md` coverage, and
  validating repository parity.
