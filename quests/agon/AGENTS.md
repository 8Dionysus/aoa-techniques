# AGENTS.md

## Applies to

This card applies to `quests/agon/` and its lifecycle-state subdirectories
unless a nearer card is added later.

## Role

`quests/agon/` holds Agon requested-practice obligations and candidate
follow-through whose owner route belongs to `mechanics/agon/`.

The lane keeps requested practice visible without turning it into live move
law, arena authority, verdict authority, owner acceptance, or canonical
technique status.

## Read before editing

Read:

1. `../AGENTS.md`
2. `../../QUESTBOOK.md`
3. `../../mechanics/agon/AGENTS.md`
4. the Agon part or candidate surface named by the quest

Markdown quest sources in this lane use `quest_markdown_contract_v1`.
Read `README.md` only when the selected task needs its human map; do not preload unrelated maps.

## Boundaries

- Do not use Agon quests to define live move law, arena authority, verdicts, or
  owner acceptance.
- Do not promote requested-only candidates through this lane.
- Do not collapse Agon candidate follow-through into root roadmap history.
- Do not remove required Markdown quest sections or leave them empty.
- Do not treat generated quest views as source truth.

## Validation

Inherit parent validation: source-fast/generated/advisory; see [VALIDATION.md](../../VALIDATION.md) and config/validation_lanes.json.

## Closeout

Report quest files changed, Agon owner route, lifecycle state, generated quest
surfaces rebuilt or intentionally left untouched, checks run, checks skipped,
and any Agon acceptance still needed.
