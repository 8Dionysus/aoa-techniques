# Root Legacy Index

This index maps root-level legacy material to the active route or owner route
that now carries the work.

Current root legacy inventory: ten receipts.

## Inventory

| Path | Kind | Active route or owner route | Status | Notes |
|---|---|---|---|---|
| `legacy/receipts/2026-05-04-review-compaction-tree-pilot.md` | `receipt` | `techniques/continuity/review-compaction/` plus `docs/TECHNIQUE_TREE_CONTRACT.md` | `landed` | First accepted technique tree path migration receipt for `AOA-T-0051`, `AOA-T-0052`, and `AOA-T-0054`. |
| `legacy/receipts/2026-05-04-handoff-continuation-tree-pilot.md` | `receipt` | `techniques/continuity/handoff-continuation/` plus `docs/TECHNIQUE_TREE_CONTRACT.md` | `landed` | Second accepted technique tree path migration receipt for `AOA-T-0056` through `AOA-T-0062`. |
| `legacy/receipts/2026-05-04-media-ingest-tree-pilot.md` | `receipt` | `techniques/ingest/media-ingest/` plus `docs/TECHNIQUE_TREE_CONTRACT.md` | `landed` | Third accepted technique tree path migration receipt for `AOA-T-0070` through `AOA-T-0074`. |
| `legacy/receipts/2026-05-04-diagnosis-repair-tree-pilot.md` | `receipt` | `techniques/recovery/diagnosis-repair/` plus `docs/TECHNIQUE_TREE_CONTRACT.md` | `landed` | Fourth accepted technique tree path migration receipt for `AOA-T-0080` through `AOA-T-0083`. |
| `legacy/receipts/2026-05-04-instruction-surface-tree-pilot.md` | `receipt` | `techniques/instruction/instruction-surface/` plus `docs/TECHNIQUE_TREE_CONTRACT.md` | `landed` | Fifth accepted technique tree path migration receipt for `AOA-T-0012`, `AOA-T-0013`, `AOA-T-0024`, `AOA-T-0027`, `AOA-T-0029`, `AOA-T-0030`, and `AOA-T-0035`. |
| `legacy/receipts/2026-05-04-kag-source-lift-tree-pilot.md` | `receipt` | `techniques/knowledge-lift/kag-source-lift/` plus `docs/TECHNIQUE_TREE_CONTRACT.md` | `landed` | Sixth accepted technique tree path migration receipt for `AOA-T-0018`, `AOA-T-0019`, `AOA-T-0020`, `AOA-T-0021`, `AOA-T-0022`, `AOA-T-0046`, `AOA-T-0047`, and `AOA-T-0048`. |
| `legacy/receipts/2026-05-04-docs-boundary-tree-pilot.md` | `receipt` | `techniques/instruction/docs-boundary/` plus `docs/TECHNIQUE_TREE_CONTRACT.md` | `landed` | Seventh accepted technique tree path migration receipt for `AOA-T-0002`, `AOA-T-0009`, `AOA-T-0034`, and `AOA-T-0033`. |
| `legacy/receipts/2026-05-04-capability-registry-tree-pilot.md` | `receipt` | `techniques/instruction/capability-registry/` plus `docs/TECHNIQUE_TREE_CONTRACT.md` | `landed` | Eighth accepted technique tree path migration receipt for `AOA-T-0025`, `AOA-T-0063`, and `AOA-T-0064`. |
| `legacy/receipts/2026-05-04-capability-boundary-tree-pilot.md` | `receipt` | `techniques/instruction/capability-boundary/` plus `docs/TECHNIQUE_TREE_CONTRACT.md` | `landed` | Ninth accepted technique tree path migration receipt for `AOA-T-0040`, `AOA-T-0043`, and `AOA-T-0093`. |
| `legacy/receipts/2026-05-05-skill-discovery-tree-pilot.md` | `receipt` | `techniques/instruction/skill-discovery/` plus `docs/TECHNIQUE_TREE_CONTRACT.md` | `landed` | Tenth accepted technique tree path migration receipt for `AOA-T-0041` and `AOA-T-0042`. |

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
