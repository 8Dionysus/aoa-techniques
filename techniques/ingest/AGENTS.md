# AGENTS.md

## Applies to

This card applies to `techniques/ingest/` and every descendant unless a nearer
`AGENTS.md` narrows the path.

## Role

`ingest/` stores technique bundles whose primary placement question is how
external media, documents, message exports, or source material become bounded
reviewable objects before later extraction, routing, cleanup, memory, or
automation begins.

This is a tree trunk, not a frontmatter domain. Technique bundles here may keep
their existing `domain` and `kind` values when the reviewed move is only path
architecture.

## Current Shelves

Current shelves:

- `media-ingest/`: turns OCR inputs, post-OCR text, media sets, mixed media,
  and Telegram-derived messages or media into explicit handoff, field,
  grouping, bucket, or local-store objects

## Read before editing

Read:

1. repository root `AGENTS.md`
2. `techniques/AGENTS.md`
3. `docs/TECHNIQUE_TREE_CONTRACT.md`
4. `docs/TECHNIQUE_TOPOLOGY_CONTRACT.md`
5. the target bundle `TECHNIQUE.md` and local notes/checks/examples

## Trunk Rules

Keep this card as tree route guidance for the trunk. Technique bundle meaning
stays in each `TECHNIQUE.md`; path placement alone does not change frontmatter
truth or owner authority.

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

Do not add `tree_path` frontmatter merely because a bundle lives under this
trunk. Do not rename trunks or shelves without a reviewed projection and a
bounded migration receipt.

## Validation

After changing ingest techniques, run:

- `python scripts/validate_nested_agents.py`
- `python scripts/validate_repo.py`

Run `python scripts/release_check.py` when generated catalogs or reader
surfaces changed.

## Closeout

Report the trunk, shelf, and bundle paths changed; whether path,
frontmatter, generated catalogs, or reader surfaces changed; checks run; checks
skipped; and any remaining owner-route risk.
