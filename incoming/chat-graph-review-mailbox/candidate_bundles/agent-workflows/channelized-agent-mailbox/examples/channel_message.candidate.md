# minimal example seed

Channel:
- `review/findings`

Message:
- `message_id`
- `channel`
- `payload_ref`
- `sent_at`
- `ack_state`

Replay:
- messages are read in channel order until the current ack cursor

The point of the example is that replay and acknowledgment are part of the mailbox contract itself.
