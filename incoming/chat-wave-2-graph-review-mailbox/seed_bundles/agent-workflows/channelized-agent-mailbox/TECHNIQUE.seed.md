---
id: AOA-T-XXXX
name: channelized-agent-mailbox
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
summary: Use persistent named channels with replay and acknowledgment so agent communication stays bounded and inspectable.
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
# channelized-agent-mailbox

## Intent

Provide a bounded mailbox surface with named channels, replay, and acknowledgment so communication survives beyond one transient session without becoming a full platform doctrine.

## When to use

- communication needs durable channels
- replay matters for bounded review or handoff
- acknowledgment should be explicit

## When not to use

- the problem is really a handoff contract rather than mailbox transport
- the surface would become a full chat or orchestration platform
- replay and ack are not real requirements

## Inputs

- named channel identifier
- message payload
- optional ack and replay cursor state

## Outputs

- channel message log
- replayable message sequence
- explicit ack state

## Core procedure

1. route messages into a named channel
2. preserve bounded replay order
3. require explicit acknowledgment when the consumer handles a message
4. keep channel semantics separate from handoff contract semantics
5. avoid widening into full communication platform policy

## Contracts

- channels are named and durable enough for replay
- replay order stays visible
- acknowledgment is explicit
- the technique stays smaller than a full messaging framework

## Risks

### Failure modes

- ack state drifts from actual message handling
- channel replay mixes unrelated work contexts

### Negative effects

- mailbox semantics get confused with handoff approval semantics
- the surface grows into a platform stack

### Misuse patterns

- using the mailbox to hide workflow policy
- treating every handoff as just another message

### Detection signals

- messages lack stable channel or replay identifiers
- ack state cannot be audited

### Mitigations

- keep channel names and replay cursors explicit
- separate mailbox transport from handoff packet rules
- keep channel purpose bounded

## Validation

- confirm messages can be replayed in order
- confirm ack state is explicit
- verify the seed stays smaller than a full communication platform

## Adaptation notes

- channel naming
- message schema
- replay cursor shape
- ack storage

## Public sanitization notes

Remove donor-specific platform and product UX language. Keep only the bounded mailbox contract.

## Example

See `examples/channel_message.seed.md`.

## Checks

See `checks/checklist.seed.md`.

## Promotion history

- staged from the chat wave 2 mailbox cluster

## Future evolution

- bounded retention rules
- channel partitioning notes
- mailbox-to-handoff bridges kept as separate siblings
