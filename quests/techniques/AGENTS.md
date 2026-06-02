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
2. `../README.md`
3. `README.md`
4. `../../QUESTBOOK.md`
5. `../../mechanics/questbook/README.md`
6. the narrow mechanic or technique route named by the quest

Generated quest files summarize source quest files; they do not author quest
meaning.

## Boundaries

- Do not turn this lane into a generic backlog.
- Do not treat source quest existence as technique promotion.
- Do not let generated quest views become source truth.
- Do not move a quest between lifecycle directories without updating the YAML
  `state` field in the same diff.
- Do not promote a quest unless the next action, owner route, and acceptance
  evidence can be read without raw session history.

## Validation

Run the narrowest relevant checks first. Usual checks for this lane:

```bash
python scripts/build_questbook_projection.py --check
python -m unittest tests.test_validate_repo_questbook_intelligence
python scripts/ci_gate.py --mode source-fast
```

## Closeout

Report quest files changed, lane and lifecycle state, generated quest surfaces
rebuilt or intentionally left untouched, checks run, checks skipped, and any
owner-route acceptance still needed.
