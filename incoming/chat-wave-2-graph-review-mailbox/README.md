# chat-wave-2-graph-review-mailbox

This is a repo-native active staging wave for graph, review-loop, session-index, skill-loading, and mailbox candidates from the external chat wave pack.

It is the first active landing lane in the new chat-wave program because its candidates are cleaner and less entangled with already-landed repo families than the Wave 1 shards.

## Activation state

- `active`
- staging-first on the first pass
- no `draft-now` seed candidates remain after the first landing pass

## What this wave tracks

- landed from this wave:
  - `AOA-T-0049` / `dependency-aware-task-graph`
  - `AOA-T-0050` / `ready-work-from-blocker-graph`
  - `AOA-T-0051` / `commit-triggered-background-review`
  - `AOA-T-0052` / `review-findings-compaction`
  - `AOA-T-0053` / `local-first-session-index`
  - `AOA-T-0054` / `compaction-resilient-skill-loading`
  - `AOA-T-0055` / `requirements-design-tasks-ladder`
  - `AOA-T-0056` / `channelized-agent-mailbox`
- active seed lane:
  - none
- narrowing-only lane:
  - `markdown-definition-of-done-defaults` with a current memo in `docs/MARKDOWN_DEFINITION_OF_DONE_DEFAULTS_NARROWING_MEMO.md`
- explicit exclusions:
  - `shadow-epic-federation`
  - `typed-governance-obligation-ledger`

## Operating posture

- do not absorb `phase-synchronized-agent-handoff`; it remains in the live queue docs as a separate narrowing lane
- use tentative `agent-workflows` placement for all seed bundles on the first pass
- keep remaining narrowing work local to `seed_bundles/**` until a later operator-approved landing move
