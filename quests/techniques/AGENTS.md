# AGENTS.md

## Applies to

This card applies to `quests/techniques/` and its lifecycle-state
subdirectories unless a nearer card is added later.

## Role

`quests/techniques/` holds rich `work_quest_v1` obligations for technique-layer
source alignment, harvest follow-through, and promotion-readiness work.

The lane tracks obligations. It does not promote a technique, close acceptance
evidence, or replace the public `QUESTBOOK.md` index.

## Read before editing

Read:

1. `../AGENTS.md`
2. `../../QUESTBOOK.md`
3. the narrow mechanic or technique route named by the quest

Generated quest files summarize source quest files; they do not author quest
meaning.
Read `README.md` only when the selected task needs its human map; do not preload unrelated maps.

## Boundaries

- Do not turn this lane into a generic backlog.
- Do not treat source quest existence as technique promotion.
- Do not let generated quest views become source truth.
- Do not move a quest between lifecycle directories without updating the YAML
  `state` field in the same diff.
- Do not promote a quest unless the next action, owner route, and acceptance
  evidence can be read without raw session history.

## Validation

Inherit parent validation: source-fast/generated/advisory; see [VALIDATION.md](../../VALIDATION.md) and config/validation_lanes.json.

## Closeout

Report quest files changed, lane and lifecycle state, generated quest surfaces
rebuilt or intentionally left untouched, checks run, checks skipped, and any
owner-route acceptance still needed.
