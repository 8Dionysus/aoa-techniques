# external-origin seed - channelized-agent-mailbox

## Donor spine

- agentralabs/agentic-comm

## Bounded pattern extracted

- Use persistent named channels with replay and acknowledgment so communication remains bounded and inspectable.

## What stays out

- full multi-agent platform doctrine
- generic messaging stacks
- orchestration policy
- donor product semantics

## Why narrower than the donor

- this seed isolates one mailbox transport contract
- it leaves broader communication platforms and orchestration behavior behind
- it does not claim the donor repo should be imported wholesale

## Expected evidence package if landed later

- `TECHNIQUE.md`
- `notes/external-origin.md`
- one minimal example or checklist
- release-path generated surfaces only after source markdown is accepted
