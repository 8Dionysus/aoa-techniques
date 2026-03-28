# Chat Wave 2 - Planting Order

This note is for operator-guided staging inside `aoa-techniques`.

## Hard rules

- keep all Wave 2 seed bundles under `seed_bundles/agent-workflows/` on the first pass
- do not assign `AOA-T-XXXX` ids from worker-owned wave tasks yet
- do not absorb `phase-synchronized-agent-handoff`; leave it in the live queue docs
- do not edit `TECHNIQUE_INDEX.md`, `generated/**`, or repo-wide queue docs from worker-owned tasks

## Landed first

1. `dependency-aware-task-graph` is now landed as `AOA-T-0049` by the main agent
2. `ready-work-from-blocker-graph` is now landed as `AOA-T-0050` by the main agent
3. `commit-triggered-background-review` is now landed as `AOA-T-0051` by the main agent
4. `review-findings-compaction` is now landed as `AOA-T-0052` by the main agent
5. `local-first-session-index` is now landed as `AOA-T-0053` by the main agent
6. `compaction-resilient-skill-loading` is now landed as `AOA-T-0054` by the main agent
7. `requirements-design-tasks-ladder` is now landed as `AOA-T-0055` by the main agent
8. `channelized-agent-mailbox` is now landed as `AOA-T-0056` by the main agent

## Preferred sequence

### Worker 3

9. `markdown-definition-of-done-defaults` remains narrowing-only; see `docs/MARKDOWN_DEFINITION_OF_DONE_DEFAULTS_NARROWING_MEMO.md`

## Explicit exclusions to leave closed

- `shadow-epic-federation`
- `typed-governance-obligation-ledger`

## Stop conditions

Stop and restage instead of forcing a seed if:

- the candidate collapses into methodology or platform doctrine
- the seed needs a new domain or schema just to stay coherent
- the candidate is really a mailbox transport for Wave 3 handoffs rather than a distinct mailbox technique
- the seed no longer stays smaller than an existing docs or history technique
