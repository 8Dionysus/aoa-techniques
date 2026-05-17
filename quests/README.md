# Quest District

This directory holds tracked `aoa-techniques` obligations that should survive
the current diff.

It is not a private scratchpad and not a second roadmap. Program direction
belongs in [`ROADMAP.md`](../ROADMAP.md). The public human index is
[`QUESTBOOK.md`](../QUESTBOOK.md). Local Questbook mechanics start in
[`mechanics/questbook`](../mechanics/questbook/README.md).

Quest sources live in lane-first lifecycle directories. Top-level
`AOA-TECH-Q-*` or `AOT-Q-*` aliases are intentionally absent; route directly to
`quests/<lane>/<state>/<quest-file>`.

## Lanes

| Lane | Use |
|---|---|
| [`techniques/`](techniques/) | Rich `work_quest_v1` obligations for the technique layer, source alignment, harvest, and promotion-readiness follow-through. |
| [`agon/`](agon/) | Agon requested-practice obligations and candidate follow-through. |

Agent edits start in [quests/AGENTS](AGENTS.md), then the nearest lane card:
[techniques/AGENTS](techniques/AGENTS.md) or [agon/AGENTS](agon/AGENTS.md).

## Lifecycle States

Each lane may contain:

| State | Use |
|---|---|
| `captured/` | Public-safe obligation exists, but route shaping is not complete. |
| `triaged/` | Route-bearing obligation with enough shape to split, promote, or close. |
| `ready/` | Next owner action is clear and bounded. |
| `active/` | Currently being advanced by an owner route. |
| `blocked/` | Waiting on a named dependency or owner decision. |
| `reanchor/` | Old route no longer matches; choose a new owner, band, or evidence path. |
| `done/` | Landed with enough public evidence to leave the active index. |
| `dropped/` | Intentionally closed without landing, with a visible reason. |

## File Families

| Family | Meaning | Guardrail |
|---|---|---|
| `techniques/<state>/AOA-TECH-Q-*.yaml` | Rich repo-local quest objects. | YAML `lane` and `state` must match the path. |
| `agon/<state>/AOT-Q-AGON-*.md` | Agon requested-practice quest notes. | Must carry `quest_markdown_contract_v1`. |
| `generated/quest_*.json` | Read models built from source quest files. | Rebuild with repo generators; do not edit by hand. |

## Use This Directory When

- a technique-layer obligation must survive beyond the current PR
- generated/source alignment needs a durable reminder
- donor, review, or harvest pressure has survived enough review to track
- an Agon requested-practice candidate needs public follow-through
