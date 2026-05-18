# External Technique Candidates - Chat Graph Review Mailbox

This doc records the graph, review, and mailbox wave staged from the external
chat wave pack.

Use it when the question is not "which landed technique should I open?", but
"which Wave 2 candidate landed, which one closed without import, and which
ones stay explicitly excluded?"

This is a staging and decision surface.
It does not create a canonical bundle or authorize import by itself.

## Scope

- this wave tracks `11` candidates from the source pack
- `8` are already landed
- `0` are active draft-now seed lanes
- `1` is closed without import
- `2` are explicit exclusions
- `phase-synchronized-agent-handoff` is intentionally not tracked here and remains in the live external narrowing lane

## Landed From This Wave

| candidate | landed bundle | boundary kept | what stayed out |
|---|---|---|---|
| `dependency-aware-task-graph` | [AOA-T-0049](../../../../../../../techniques/execution/ready-work-graphs/dependency-aware-task-graph/TECHNIQUE.md) | explicit dependency graph as a working surface for bounded coding tasks | full PM system, memory substrate, tracker product doctrine, broad orchestration semantics |
| `ready-work-from-blocker-graph` | [AOA-T-0050](../../../../../../../techniques/execution/ready-work-graphs/ready-work-from-blocker-graph/TECHNIQUE.md) | derive a blocker-aware ready frontier from an existing graph | graph authoring, ranking doctrine, tracker product semantics, broad orchestration semantics |
| `commit-triggered-background-review` | [AOA-T-0051](../../../../../../../techniques/continuity/review-compaction/commit-triggered-background-review/TECHNIQUE.md) | trigger asynchronous review after a visible commit and preserve findings as an artifact | auto-fix loops, autonomous merge, queue product semantics, full CI governance |
| `review-findings-compaction` | [AOA-T-0052](../../../../../../../techniques/continuity/review-compaction/review-findings-compaction/TECHNIQUE.md) | verify and consolidate current findings against live code | trigger logic, remediation loops, backlog policy, generic issue management |
| `local-first-session-index` | [AOA-T-0053](../../../../../../../techniques/history/history-artifacts/local-first-session-index/TECHNIQUE.md) | local searchable index over already-saved session artifacts with stable source references | session capture, transcript packaging, dashboard doctrine, cloud memory or hosted sync posture |
| `compaction-resilient-skill-loading` | [AOA-T-0054](../../../../../../../techniques/continuity/review-compaction/compaction-resilient-skill-loading/TECHNIQUE.md) | re-seed a bounded skills-availability surface after compaction so needed skills can be reloaded from canonical sources | full context reconstruction, prompt stuffing, marketplace or install doctrine |
| `requirements-design-tasks-ladder` | [AOA-T-0055](../../../../../../../techniques/execution/ready-work-graphs/requirements-design-tasks-ladder/TECHNIQUE.md) | keep requirements, design, and tasks visibly separate before implementation | full methodology import, template ecosystems, planning religion |
| `channelized-agent-mailbox` | [AOA-T-0056](../../../../../../../techniques/continuity/handoff-continuation/channelized-agent-mailbox/TECHNIQUE.md) | durable named-channel mailbox with replay and explicit acknowledgment | handoff authorization, transcript history, full messaging-platform doctrine |

## Active Seed Lane

No remaining `draft-now` seed candidates in Wave 2.

## Closed Non-Import Verdict

| candidate | why closed | next honest move |
|---|---|---|
| `markdown-definition-of-done-defaults` | current donor evidence still reads as config UX plus task-manager integration rather than one standalone markdown technique contract | keep it closed in this packet; a future attempt needs a new Distillation intake and the smaller default-checklist contract described in [MARKDOWN_DEFINITION_OF_DONE_DEFAULTS_CLOSEOUT_MEMO.md](MARKDOWN_DEFINITION_OF_DONE_DEFAULTS_CLOSEOUT_MEMO.md) |

## Explicit Exclusions

| candidate | why excluded now | next honest move |
|---|---|---|
| `shadow-epic-federation` | still system-shaped and too wide for a bounded first-pass technique | keep closed unless a new intake proves one smaller federation seam |
| `typed-governance-obligation-ledger` | still governance-architecture heavy rather than one reviewable artifact contract | keep closed unless a new intake isolates one smaller obligation or violation artifact |

## Notes

- keep `phase-synchronized-agent-handoff` in the live queue docs only
- use this packet to track landed boundaries and closed verdicts, not to prepare duplicate seed bundles
- keep mailbox and handoff semantics separate so Wave 3 can own handoff contracts later
