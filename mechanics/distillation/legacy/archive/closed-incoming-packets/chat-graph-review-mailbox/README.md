# chat-graph-review-mailbox

This is a repo-native evidence packet for graph, review-loop, session-index,
skill-loading, and mailbox candidates from the external chat wave pack.

It preserves the first-pass landing trail and the closed non-import verdicts. It is
not an active landing lane.

## Activation state

- `evidence-only`
- first-pass landing queue exhausted
- no `draft-now` seed candidates remain after the first landing pass
- no active non-landed tail remains in this packet

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
- seed lane:
  - none
- closed non-import:
  - `markdown-definition-of-done-defaults` with final rationale in `docs/MARKDOWN_DEFINITION_OF_DONE_DEFAULTS_CLOSEOUT_MEMO.md`
- explicit exclusions:
  - `shadow-epic-federation`
  - `typed-governance-obligation-ledger`

## Operating posture

- do not absorb `phase-synchronized-agent-handoff`; it is outside this closed packet
- use the landed `techniques/**/TECHNIQUE.md` bundles for current technique meaning
- do not recreate packet-local `candidate_bundles/**` for already landed techniques
- any future attempt for `markdown-definition-of-done-defaults` must start as a new Distillation intake with fresh evidence
