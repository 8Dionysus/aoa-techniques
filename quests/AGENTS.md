# AGENTS.md

## Applies to

This card applies to `quests/` and all descendants unless a nearer card is
added later.

## Role

`quests/` holds durable public obligations that should survive the current
diff. Source placement is lane-first and lifecycle-aware:
`quests/<lane>/<state>/<quest-file>`.

Root-level quest aliases are intentionally absent. Edit the source file in its
lane and state directory.

## Read before editing

Read root `AGENTS.md`, `QUESTBOOK.md`, `quests/README.md`, and
`mechanics/questbook/README.md` before changing quest semantics.

Use the nearest lane `AGENTS.md` for local command posture and the lane README
for human-facing lane meaning. Generated quest files summarize source quest
files; they do not author quest meaning.

## Boundaries

- Quests are not a second roadmap.
- Do not use quests as hidden memory or private task dumps.
- Do not assign owner-local commitments unless the owner route accepts them.
- Do not treat a quest as closure proof, proof verdict, routing authority, or
  technique promotion.

## Validation

Run the narrowest relevant checks first. Usual checks for this district:

```bash
python scripts/build_catalog.py
python scripts/validate_repo.py
python -m unittest tests.test_validate_repo
```

## Closeout

Report quest files changed, lane and lifecycle state, generated quest surfaces
rebuilt or left untouched, checks run, checks skipped, and any owner-route
acceptance still needed.
