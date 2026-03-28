# channelized-agent-mailbox checklist

- [ ] channel identity is explicit and bounded to one coordination lane
- [ ] messages can be replayed from a visible cursor, offset, or last-seen marker
- [ ] acknowledgment is explicit rather than implied by silence
- [ ] mailbox transport stays distinct from handoff authorization or stop/escalation rules
- [ ] the bundle stays smaller than a full messaging platform or orchestration product
- [ ] transcript packaging, history indexing, and witness export remain outside the contract
- [ ] the example keeps replay and ack concrete without donor-specific platform details
- [ ] channel purpose remains narrow enough that unrelated workflows do not share one mailbox
