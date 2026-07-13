# Questbook Lane-first Source Store

Status: accepted

Date: 2026-05-03

## Index Metadata

- Decision ID: AOA-TECH-D-0032
- Original date: 2026-05-03
- Surface classes: mechanic package, quest/lane
- Technique axes: mechanic bridge
- Mechanic parents: questbook
- Guard families: mechanic topology, questbook
- Posture: accepted

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

Verification was routed through the targeted owner checks and repository validation lanes.

