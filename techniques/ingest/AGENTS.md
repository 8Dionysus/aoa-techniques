# AGENTS.md

Guidance for coding agents and humans working under `techniques/ingest/`.

## Purpose

`ingest/` stores technique bundles whose primary placement question is how
external media, documents, message exports, or source material become bounded
reviewable objects before later extraction, routing, cleanup, memory, or
automation begins.

This is a tree trunk, not a frontmatter domain. Technique bundles here may keep
their existing `domain` and `kind` values when the reviewed move is only path
architecture.

## Current scope

Accepted pilot shelves:

- `media-ingest/`: turns OCR inputs, post-OCR text, media sets, mixed media,
  and Telegram-derived messages or media into explicit handoff, field,
  grouping, bucket, or local-store objects

## Domain rules

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

## Boundary

Use `docs/TECHNIQUE_TREE_CONTRACT.md` before adding another shelf here.

Do not add `tree_path` frontmatter merely because a bundle lives under this
trunk. Do not rename trunks or shelves without a reviewed projection and a
bounded migration receipt.

## Validation

After changing ingest techniques, run:

- `python scripts/validate_nested_agents.py`
- `python scripts/validate_repo.py`

Run `python scripts/release_check.py` when generated catalogs or reader
surfaces changed.
