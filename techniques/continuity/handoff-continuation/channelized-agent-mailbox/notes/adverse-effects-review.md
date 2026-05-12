# Adverse Effects Review

## Technique

- id: AOA-T-0056
- name: channelized-agent-mailbox

## Review focus

- current role: canonical default for keeping one durable agent mailbox or thread lane replayable and explicitly acknowledged across session gaps
- current watch seam: preserve the bounded mailbox contract without turning delivery, read state, or ACK rows into handoff authorization, transcript history, trust policy, encryption doctrine, queue governance, or a full messaging platform

## Failure modes

- channel or thread identity drifts, so replay no longer names one bounded coordination lane
- replay cursors, sync state, or thread logs miss messages or duplicate them without visible dedup logic
- ACK state records receipt or local handling but is misread as remote delivery proof
- receivers acknowledge messages before actually handling the work
- mailbox history becomes the only handoff packet, hiding stop lines, verification state, or continuation permission

## Negative effects

- simple coordination can become too ceremonial when a direct note would suffice
- long-lived mailboxes can accumulate stale messages and slow recovery
- visible ACK bits can create false confidence if reviewers stop reading the actual work
- channelized traffic can leak into product messaging, analytics, federation, encryption, or trust concerns that belong elsewhere

## Misuse patterns

- treating mailbox delivery as permission for the next agent to continue
- using ACK state as proof that a task was completed correctly
- collapsing unrelated work into one catch-all channel or thread
- replacing transcript packaging, local history indexing, or witness export with live mailbox logs
- importing a full broker, relay, encryption, or agent-platform stack when the reusable move only needs a bounded mailbox seam

## Detection signals

- reviewers cannot tell which message sequence a receiver replayed
- messages have ACKs but no visible evidence of the receiver's actual handling
- channel or thread names become generic buckets like `general`, `all`, or `agent-chat`
- implementation debate shifts from mailbox replay and acknowledgment to relay topology, trust tiers, dashboards, adapters, federation, or product delivery guarantees
- session continuation claims cite the mailbox alone without a separate handoff or verification surface

## Mitigations

- keep each mailbox or thread tied to one bounded coordination lane
- distinguish local handled/read ACK state from remote delivery confirmation
- require replay from visible message IDs, thread logs, cursors, or sync state
- route handoff authorization, transcript capture, history indexing, trust policy, and messaging-platform behavior to sibling techniques or owning repositories
- split or retire channels when their purpose stops being reviewable

## Recommendation

- move `AOA-T-0056` to `canonical` and use this note as the watch surface for ACK-overtrust, mailbox-as-handoff, replay ambiguity, catch-all channel drift, and messaging-platform expansion
