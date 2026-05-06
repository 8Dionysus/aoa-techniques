# minimal example seed

Packet:
- `packet_id`
- `summary`
- `next_owner`

Receipt:
- `packet_id`
- `receiver`
- `acknowledged_at`
- `ack_state`

The point of the example is that continuation waits for an explicit receipt object, not just message delivery.
