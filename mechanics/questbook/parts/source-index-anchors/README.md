# Source Index Anchors

This part maps the current local Questbook source and projection surfaces so
future questbook work starts from existing repo truth instead of redrafting the
Questbook model inside mechanics.

It does not change quest source state or technique status.

## Anchor Map

| Surface | Questbook relevance | Boundary |
|---|---|---|
| [QUESTBOOK.md](../../../../QUESTBOOK.md) | Human index for deferred canon-hardening, donor-refinery, generated/source alignment, and harvest obligations. | Does not become a second roadmap or full quest history. |
| [`quests/<lane>/<state>/`](../../../../quests/) | Repo-local `work_quest_v1` YAML source quest objects such as `AOA-TECH-Q-0003` through `AOA-TECH-Q-0007`, plus `quest_markdown_contract_v1` Agon requested-practice Markdown quests. | Source objects do not prove owner acceptance, closure, or technique promotion. |
| [quest schema](../../../../schemas/quest.schema.json) | Contract for source quest objects. | Does not import AoA center lane law or sibling owner truth. |
| [quest dispatch schema](../../../../schemas/quest_dispatch.schema.json) | Contract for thin dispatch projections. | Does not create routing authority. |
| [quest catalog](../../../../generated/quest_catalog.min.json) | Generated compact catalog from source quest files. | Does not author quest meaning. |
| [quest dispatch](../../../../generated/quest_dispatch.min.json) | Generated dispatch projection from source quest files. | Does not grant execution permission or owner acceptance. |

## Use

Use this map when a mechanics change needs to explain how local Questbook
surfaces relate without moving source truth into this package.

If the task changes quest source data or generated projections, use the
existing quest validators and generated-surface checks through
[AGENTS](../../../../AGENTS.md#validation).

## Stop-lines

- Do not move `QUESTBOOK.md`, root `quests/`, schemas, or generated
  projections into this package.
- Do not treat generated quest views as source truth.
- Do not use source quest existence as closure proof, owner acceptance,
  routing authority, or automatic technique promotion.
