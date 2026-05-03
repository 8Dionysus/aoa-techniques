# techniques Quest Lane

Technique-layer obligations, source-alignment duties, harvest follow-through,
and promotion-readiness reminders.

## Lane Route

Use this lane when the obligation belongs to `aoa-techniques` source or
projection stewardship and can be tracked as a rich `work_quest_v1` source
object.

Current source split:

- `done`: landed local Questbook setup obligations.
- `captured`: still-open technique-layer obligations whose owner route and
  acceptance evidence are visible enough to preserve.

## Promotion Rule

Promote a quest only when the next action, owner route, and acceptance evidence
can be read without raw session history. Moving state requires moving the file
to the matching lifecycle directory and updating the YAML `state` field in the
same diff.

## Stop-lines

- Do not turn this lane into a generic backlog.
- Do not treat source quest existence as technique promotion.
- Do not let generated quest views become source truth.

