---
id: AOA-T-XXXX
name: episode-bounded-agent-loop
domain: agent-workflows
status: draft-seed
origin: chat-wave-3-handoff-bounded-continuation
note: seed bundle staged for operator-guided chat wave 3 landing
owners:
  - 8Dionysus
tags:
  - reusable
  - public
  - agent-friendly
  - chat-wave
  - handoff-bounded-continuation
summary: Bound longer agent work into explicit episodes with checkpoints and stop rules so continuation remains reviewable.
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
# episode-bounded-agent-loop

## Intent

Break a longer run into explicit episodes with checkpoints and stop conditions so progress can continue without slipping into an unbounded autonomous loop.

## When to use

- the work cannot finish in one bounded pass
- checkpoints are needed between episodes
- stop conditions matter as much as progress

## When not to use

- one bounded single-shot pass is enough
- the loop would become a general autonomous agent system
- there is no meaningful checkpoint between episodes

## Inputs

- current episode goal
- checkpoint criteria
- stop or escalation rules

## Outputs

- bounded episode result
- checkpoint artifact
- explicit continue, stop, or escalate decision

## Core procedure

1. define the current episode goal
2. execute only until the checkpoint or stop rule
3. produce a checkpoint artifact
4. decide explicitly whether to continue, stop, or escalate
5. open the next episode only from that visible checkpoint

## Contracts

- each episode has a bounded goal
- checkpoints are explicit
- stop or escalation rules remain visible
- the technique stays smaller than total autonomous agent doctrine

## Risks

### Failure modes

- episodes are too large to review safely
- checkpoint rules are too vague to stop the loop

### Negative effects

- the loop slowly becomes open-ended autonomy
- progress claims lose grounding without checkpoint artifacts

### Misuse patterns

- treating every long task as permission for unbounded continuation
- skipping checkpoint review to save time

### Detection signals

- episodes have no clear end condition
- continuation happens without a visible checkpoint artifact

### Mitigations

- keep episode goals short and explicit
- require checkpoint artifacts
- make stop and escalation rules part of the contract

## Validation

- confirm every episode ends at a checkpoint or stop rule
- confirm continuation decisions are explicit
- verify the seed stays smaller than an autonomous loop platform

## Adaptation notes

- episode length
- checkpoint artifact shape
- escalation path
- continuation approvals

## Public sanitization notes

Remove donor-specific agent system language. Keep only the bounded episode-and-checkpoint loop contract.

## Example

See `examples/episode_checkpoint.seed.md`.

## Checks

See `checks/checklist.seed.md`.

## Promotion history

- staged from the chat wave 3 continuation cluster

## Future evolution

- checkpoint scorecards
- episode replay notes
- bounded escalation packets
