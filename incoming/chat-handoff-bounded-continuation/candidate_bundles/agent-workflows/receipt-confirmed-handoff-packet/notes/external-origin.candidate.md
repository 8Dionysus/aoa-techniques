# external-origin seed - receipt-confirmed-handoff-packet

## Donor spine

- jeremiah-k/agor
- ax-platform/ax-platform-mcp

## Bounded pattern extracted

- Require the receiving side to acknowledge a handoff packet before continuation.

## What stays out

- generic messaging platforms
- queueing systems
- broad mailbox doctrine
- donor platform semantics

## Why narrower than the donors

- this seed isolates one transfer-receipt contract
- it leaves messaging platforms and broader workflow stacks behind
- it does not claim the donor repos should be imported wholesale

## Expected evidence package if landed later

- `TECHNIQUE.md`
- `notes/external-origin.md`
- one minimal example or checklist
- release-path generated surfaces only after source markdown is accepted
