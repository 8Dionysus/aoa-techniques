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

Read root `AGENTS.md`, `QUESTBOOK.md`, and `mechanics/questbook/AGENTS.md`
before changing quest semantics.

Use the nearest lane `AGENTS.md` for local route posture; consult its README
only when human-facing lane meaning is relevant. Generated quest files summarize source quest
files; they do not author quest meaning.
Read `README.md` only when the selected task needs its human map; do not preload unrelated maps.

## Boundaries

- Quests are not a second roadmap.
- Do not use quests as hidden memory or private task dumps.
- Do not assign owner-local commitments unless the owner route accepts them.
- Do not treat a quest as closure proof, proof verdict, routing authority, or
  technique promotion.

## Validation

Select the narrowest owner route: `source-fast` for the local owner; add `generated` for derived indexes and `advisory` only for non-blocking boundaries. See [VALIDATION.md](../VALIDATION.md); exact order is `config/validation_lanes.json`; focused procedure stays with the nearest owner. Report checks, skips, and blockers.

## Closeout

Report quest files changed, lane and lifecycle state, generated quest surfaces
rebuilt or left untouched, checks run, checks skipped, and any owner-route
acceptance still needed.
