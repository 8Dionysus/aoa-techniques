# Minimal channelized-agent-mailbox

Channel:

- `review/findings`

Messages:

- `sequence=14`, `sender=review-agent`, `payload_ref=review-2026-03-28.md`
- `sequence=15`, `sender=review-agent`, `payload_ref=review-2026-03-28-followup.md`

Replay:

- `fix-agent` reconnects with `last_seen=13`
- it replays messages `14` and `15` in order

Acknowledgment:

- after handling both messages, `fix-agent` records `acked_through=15`

The mailbox contract is the visible named channel, ordered replay, and explicit ack state. It does not decide whether a later handoff is approved or what remediation policy follows.
