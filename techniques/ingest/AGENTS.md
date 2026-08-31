# AGENTS.md

## Applies to

This card applies to `techniques/ingest/` and every descendant unless a nearer
`AGENTS.md` narrows the path.

## Role

`ingest/` stores technique bundles whose primary placement question is how
external media, documents, message exports, or source material become bounded
reviewable objects before later extraction, routing, cleanup, memory, or
automation begins.

Current `ingest` trunk: shared placement applies; local role and shelves are the delta.
## Current Shelves

Current shelves:

- `media-ingest/`: turns OCR inputs, post-OCR text, media sets, mixed media,
  and Telegram-derived messages or media into explicit handoff, field,
  grouping, bucket, or local-store objects

## Read before editing

Use shared order in [techniques/AGENTS.md](../AGENTS.md#read-before-editing); inspect `ingest` role and its target bundle.
## Trunk Rules

Placement contract: [techniques/AGENTS.md](../AGENTS.md#closeout); local `ingest` shelf and boundary delta follows.
## Boundaries

Keep the ingest object explicit:

- what source material is being normalized or grouped
- what reviewable intermediate object is produced
- what uncertainty, provenance, confidence, threshold, or resume state remains
  inspectable
- what downstream action, auth, memory, cleanup, moderation, or runtime policy
  is refused

Do not turn an ingest technique into a live connector, scraper, parser product,
OCR service, archive app, moderation policy, memory doctrine, or cleanup
automation.

Use `docs/TECHNIQUE_TREE_CONTRACT.md` before adding another shelf here.

`ingest` path placement follows the parent contract; renames need its reviewed projection and bounded receipt.
## Validation

Inherit [techniques/AGENTS.md](../AGENTS.md#validation): `source-fast`; see [VALIDATION.md](../../VALIDATION.md) and `config/validation_lanes.json`. Local `techniques/ingest/AGENTS.md`.
## Closeout

Local delta `techniques/ingest/AGENTS.md`: state placement/frontmatter/generated-reader changes or route-only guidance.
