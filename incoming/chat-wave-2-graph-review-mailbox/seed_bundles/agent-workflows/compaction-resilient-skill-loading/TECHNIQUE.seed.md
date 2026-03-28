---
id: AOA-T-XXXX
name: compaction-resilient-skill-loading
domain: agent-workflows
status: draft-seed
origin: chat-wave-2-graph-review-mailbox
note: seed bundle staged for operator-guided chat wave 2 landing
owners:
  - 8Dionysus
tags:
  - reusable
  - public
  - agent-friendly
  - chat-wave
  - graph-review-mailbox
summary: Preserve or reload skill availability after session compaction so bounded capability context survives context loss.
maturity_score: 1
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: donor_soil
export_ready: false
relations: []
evidence:
  - kind: external_origin
    path: notes/external-origin.seed.md
---
# compaction-resilient-skill-loading

## Intent

Keep skill availability stable across session compaction so bounded capability context can be restored without reintroducing full context composition doctrine.

## When to use

- compaction or context loss is expected
- skill availability matters after compaction
- the recovery path should be explicit and reviewable

## When not to use

- the problem is general context composition across the whole repo
- skills are not a real source layer
- the flow would silently stuff arbitrary prompt text back in

## Inputs

- canonical skill source or manifest
- compaction event or reduced context state
- reload or reinjection trigger

## Outputs

- restored skill availability
- explicit record of which skills were reloaded
- bounded capability context after compaction

## Core procedure

1. detect or name the compaction boundary
2. identify the canonical skill source to restore from
3. reload or reattach only the required skill set
4. keep the restored set explicit and reviewable
5. separate skill recovery from broader context composition

## Contracts

- canonical skill sources stay authoritative
- compaction recovery is explicit
- restored skill availability stays smaller than full context reconstruction
- the technique does not turn every prompt fragment into a skill

## Risks

### Failure modes

- the wrong skill set is restored after compaction
- compaction recovery becomes silent prompt stuffing

### Negative effects

- operators lose track of which skills are active
- the technique drifts into general context doctrine

### Misuse patterns

- treating any repeated instruction as a skill
- rebuilding the whole context instead of bounded skill availability

### Detection signals

- restored skills cannot be traced back to a canonical source
- post-compaction capability state is opaque

### Mitigations

- keep the skill source explicit
- log the restored skill set
- limit the recovery surface to bounded skills only

## Validation

- confirm the same bounded skill set can be restored after compaction
- confirm restored skills map back to a source file or manifest
- verify the seed stays smaller than general context composition

## Adaptation notes

- compaction trigger
- skill manifest shape
- restore strategy
- audit logging

## Public sanitization notes

Remove donor-specific session product semantics. Keep only the bounded skill recovery contract.

## Example

See `examples/skill_reload.seed.md`.

## Checks

See `checks/checklist.seed.md`.

## Promotion history

- staged from the chat wave 2 skill-loading cluster

## Future evolution

- restore diffs
- partial skill set recovery
- compaction audit notes
