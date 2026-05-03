# Questbook Lane-first Source Store

Status: accepted

Date: 2026-05-03

## Context

`mechanics/questbook/` now explains local Questbook pressure, but the root
`quests/` source store was still flat. That left `aoa-techniques` out of step
with the AoA Questbook pattern where quest placement is lane-first and
lifecycle-aware.

AoA center owns common Questbook law. This repo owns only the local technique
obligation store and the generated projections derived from it.

## Decision

Move local quest sources into `quests/<lane>/<state>/`.

- `AOA-TECH-Q-*` rich YAML work quests live in the `techniques` lane.
- `AOT-Q-AGON-*` requested-practice Markdown quests live in the `agon` lane.
- YAML quest objects carry `lane` and must match both lane and state path.
- Markdown quest objects must carry `quest_markdown_contract_v1`.
- Root-level quest aliases remain absent.

Keep `QUESTBOOK.md` as the public human index. Keep
`generated/quest_catalog.min.json` and `generated/quest_dispatch.min.json` as
derived read models, not source authority.

## Consequences

- Agents can route from obligation to owner lane before reading lifecycle
  state.
- Closed and open technique obligations no longer sit in one flat folder.
- Agon requested-practice follow-through is preserved without becoming
  technique promotion.
- Local validators now enforce lane/state placement and strict Markdown quest
  reviewability.

## Verification

Verify with:

```bash
python scripts/build_catalog.py
python scripts/validate_repo.py
python -m unittest tests.test_validate_repo tests.test_questbook_mechanics_topology tests.test_growth_cycle_mechanics_topology
python -m unittest discover -s tests
```

