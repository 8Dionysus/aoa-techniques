---
id: AOA-T-0056
name: channelized-agent-mailbox
domain: agent-workflows
status: promoted
origin:
  project: agentralabs/agentic-comm
  path: README.md + GUIDE.md + crates/agentic-comm/src/channel.rs + docs/public/SCENARIOS-AGENTIC-COMM.md
  note: Adapted from the open-source AgenticComm project, which uses persistent named channels, ordered messages, replay, and explicit acknowledgment to keep multi-agent communication inspectable without requiring a hosted messaging stack.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - communication
  - mailbox
  - channel
  - replay
summary: Keep agent communication inside durable named channels with ordered replay and explicit acknowledgment so coordination survives session gaps without widening into a full messaging platform or handoff-governance stack.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-28
export_ready: true
relations: []
evidence:
  - kind: external_origin
    path: notes/external-origin.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: external_review
    path: notes/external-import-review.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# channelized-agent-mailbox

## Intent

Keep agent communication inside durable named channels with ordered replay and explicit acknowledgment so teams can coordinate across session gaps without turning the mailbox into full platform doctrine, transcript history, or handoff authorization.

## When to use

- agents need one durable communication surface that survives beyond a single transient session
- messages should be replayed in visible order rather than recovered from memory or ad hoc logs
- receivers need explicit acknowledgment state instead of implicit assumptions that a message was handled
- the reusable object is one bounded mailbox transport surface, not a full orchestration or messaging product

## When not to use

- the real need is a handoff contract that decides when the next agent is allowed to continue
- the main artifact should be transcript packaging, history indexing, or witness export after the conversation is over
- the design would require full pub/sub governance, federation, analytics, or messaging-platform policy to make sense
- replay order and acknowledgment are not real requirements for the workflow

## Inputs

- one named channel identifier
- one bounded message payload or payload reference
- one sender and one intended reader or reader set
- optional replay cursor or last-seen marker
- optional acknowledgment signal that stays visible after receipt

## Outputs

- one durable mailbox channel with ordered messages
- one replayable message sequence for that channel
- one explicit acknowledgment state per handled message or cursor
- one inspectable communication surface that stays separate from later handoff or policy layers

## Core procedure

1. Create or select one named channel for the bounded coordination lane.
2. Append messages to that channel in visible sequence order instead of scattering them across transient logs.
3. Let receivers replay messages from a named cursor or last-seen position when they reconnect or resume work.
4. Record acknowledgment explicitly when a receiver has handled a message or advanced the mailbox cursor.
5. Keep channel purpose narrow enough that replay order and ack semantics remain understandable in review.
6. Route handoff permission, stop rules, escalation, analytics, and broader messaging-platform behavior to sibling surfaces instead of widening the mailbox contract.
7. Reopen a different technique when topics, federation, routing policy, or workflow governance become the real center of gravity.

## Contracts

- channels are named explicitly and remain stable enough for replay
- message order is reviewable through a visible sequence or cursor surface
- replay starts from an explicit cursor, offset, or equivalent last-seen marker rather than hidden memory
- acknowledgment is explicit and inspectable instead of being implied by silence
- mailbox transport stays smaller than a full messaging platform, orchestration stack, or handoff-governance contract
- transcript packaging, history indexing, and handoff authorization remain separate sibling concerns

Relationship to adjacent techniques: unlike [AOA-T-0044](../../history/versionable-session-transcripts/TECHNIQUE.md), this technique owns live mailbox transport with replay and acknowledgment rather than post-capture transcript packaging. Unlike [AOA-T-0053](../../history/local-first-session-index/TECHNIQUE.md), it keeps active channel traffic inspectable but does not build a derived search index over saved history. It also stays smaller than the live `phase-synchronized-agent-handoff` narrowing lane because it does not decide when a receiving agent is permitted to continue, stop, return, or escalate.

## Risks

### Failure modes

- ack state drifts away from what receivers actually handled
- replay cursors skip or repeat messages because the cursor is hidden or ambiguous
- unrelated workflows share one channel and destroy the bounded review surface
- platform breadth leaks in until the mailbox stops being one small transport contract

### Negative effects

- durable mailboxes can create more communication ceremony than a small task actually needs
- operators may overtrust an ack bit and stop checking what the receiver truly did
- long-lived channels can accumulate noise if retention and channel purpose stay vague

### Misuse patterns

- treating every agent handoff as if mailbox delivery already granted permission to continue work
- widening the bundle into pub/sub governance, federation, analytics, or chat-product semantics
- using channel history as a substitute for transcript packaging, witness export, or project memory

### Detection signals

- messages cannot be replayed from a stable cursor or sequence position
- reviewers cannot tell whether a message was acknowledged, merely read, or never handled
- channel names drift toward catch-all buckets like `general` or `everything`
- design discussions focus more on broker features, fan-out policy, or dashboards than on one bounded mailbox seam

### Mitigations

- keep channel names tied to one bounded coordination lane
- keep replay cursors and ack state explicit in the surface or artifact
- split handoff authorization, transcript export, and analytics into sibling techniques
- reset or split channels when message purpose stops being reviewable

## Validation

Verify the technique by confirming that:
- a receiver can replay messages from a visible last-seen cursor or equivalent sequence marker
- acknowledgment state is explicit and distinguishable from unread or unhandled messages
- channel naming is bounded enough that unrelated work does not collapse into one mailbox
- the example still makes sense without platform-specific messaging features
- the bundle stays smaller than handoff governance, transcript history, and full messaging-platform doctrine

See `checks/channelized-agent-mailbox-checklist.md`.

## Adaptation notes

What can vary across projects:
- channel naming conventions
- message schema or payload-reference shape
- replay cursor format
- acknowledgment granularity
- whether the mailbox surface is CLI, file-backed, or another local transport shell

What should stay invariant:
- named channels remain the mailbox unit
- replay order stays visible
- acknowledgment stays explicit
- the mailbox remains a bounded transport surface rather than workflow governance

Project-shaped details that should not be treated as invariant:
- one `.acomm` file format or one storage backend
- one MCP server, CLI, or SDK package
- pub/sub wildcard matching, federation, encryption, or affect semantics
- dashboard, metrics, or productized multi-agent coordination features

## Public sanitization notes

This import narrows the donor repository to one bounded pattern: durable named-channel mailbox transport with ordered replay and explicit acknowledgment. Pub/sub topic policy, broadcast fan-out, federation, trust and consent layers, analytics, benchmark claims, installation flows, and broader multi-agent product semantics were intentionally left out of the public contract.

## Example

See `examples/minimal-channelized-agent-mailbox.md`.

## Checks

See `checks/channelized-agent-mailbox-checklist.md`.

## Promotion history

- adapted from open-source `agentralabs/agentic-comm`
- staged through the chat wave 2 graph-review-mailbox lane inside `aoa-techniques`
- promoted into `aoa-techniques` on 2026-03-28 as a bounded external-import technique for named-channel mailbox transport with replay and explicit acknowledgment

## Future evolution

- keep handoff packet and continuation-permission doctrine separate instead of widening this bundle into cross-agent authorization
- keep transcript packaging and history indexing separate instead of treating mailbox history as the post-capture artifact family
- add a stronger second live context if another public workflow surface uses a bounded named-channel mailbox with replay and acknowledgment in practice
