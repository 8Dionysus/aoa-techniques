# Root Legacy Index

This index maps root-level legacy material to the active route or owner route
that now carries the work.

Current root legacy inventory: four receipts.

## Inventory

| Path | Kind | Active route or owner route | Status | Notes |
|---|---|---|---|---|
| `legacy/receipts/2026-05-04-review-compaction-tree-pilot.md` | `receipt` | `techniques/continuity/review-compaction/` plus `docs/TECHNIQUE_TREE_CONTRACT.md` | `landed` | First accepted technique tree path migration receipt for `AOA-T-0051`, `AOA-T-0052`, and `AOA-T-0054`. |
| `legacy/receipts/2026-05-04-handoff-continuation-tree-pilot.md` | `receipt` | `techniques/continuity/handoff-continuation/` plus `docs/TECHNIQUE_TREE_CONTRACT.md` | `landed` | Second accepted technique tree path migration receipt for `AOA-T-0056` through `AOA-T-0062`. |
| `legacy/receipts/2026-05-04-media-ingest-tree-pilot.md` | `receipt` | `techniques/ingest/media-ingest/` plus `docs/TECHNIQUE_TREE_CONTRACT.md` | `landed` | Third accepted technique tree path migration receipt for `AOA-T-0070` through `AOA-T-0074`. |
| `legacy/receipts/2026-05-04-diagnosis-repair-tree-pilot.md` | `receipt` | `techniques/recovery/diagnosis-repair/` plus `docs/TECHNIQUE_TREE_CONTRACT.md` | `landed` | Fourth accepted technique tree path migration receipt for `AOA-T-0080` through `AOA-T-0083`. |

## Accounting Rule

Every future entry must name:

- the preserved path under `legacy/`
- whether it is `raw`, `archive`, or `receipt` material
- the active route, owner route, or explicit hold status
- why it belongs in root legacy instead of `incoming/`,
  `mechanics/<slug>/legacy/`, `generated/`, `reports/`, `docs/decisions/`, or
  an active technique bundle

Do not add placeholder receipts. Empty inventory is preferable to false
provenance.
