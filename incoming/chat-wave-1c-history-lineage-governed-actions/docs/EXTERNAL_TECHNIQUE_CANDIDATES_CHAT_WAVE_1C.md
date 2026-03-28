# External Technique Candidates - Chat Wave 1C

This doc records the history, lineage, telemetry, and governed-action shard staged from the external chat wave pack.

Use it when the question is not "which landed technique should I open?", but "which Wave 1C candidate already landed cleanly, which ones stay narrowing-only, and which related candidates stay explicitly excluded?"

This is a staging and decision surface.
It does not create a canonical bundle or authorize import by itself.

## Scope

- this shard tracks `8` source-pack candidates
- `4` are already landed
- `0` remain staged for later triage
- `2` are narrowing-only
- `2` are explicit exclusions
- no seed bundles are created here yet

## Landed From This Shard

| candidate | landed bundle | boundary kept | what stayed out |
|---|---|---|---|
| `transcript-replay-artifact` | [AOA-T-0066](../../../techniques/history/transcript-replay-artifact/TECHNIQUE.md) | replayable post-capture artifact over existing saved sessions | session capture, transcript packaging, witness export, and hosted replay-platform doctrine |
| `transcript-linked-code-lineage` | [AOA-T-0067](../../../techniques/history/transcript-linked-code-lineage/TECHNIQUE.md) | bounded code-to-evidence link from code history back to saved session artifacts | generic repo analytics, scorecards, hosted search, and retrieval-product doctrine |
| `fail-closed-evidence-gate` | [AOA-T-0068](../../../techniques/agent-workflows/fail-closed-evidence-gate/TECHNIQUE.md) | fail-closed execution-boundary gate with explicit evidence output | human confirmation doctrine, broad security constitutions, and total policy-platform semantics |
| `approval-bound-durable-jobs` | [AOA-T-0069](../../../techniques/agent-workflows/approval-bound-durable-jobs/TECHNIQUE.md) | durable jobs that pause and resume across one explicit approval seam | full orchestration platform, scheduler doctrine, and generic automation stacks |

No remaining staged landing candidates in Wave 1C.

## Narrowing-Only Lane

| candidate | why not landed yet | next honest move |
|---|---|---|
| `agent-readiness-telemetry` | current donor evidence still reads as analytics and scorecard product behavior rather than one standalone readiness artifact or verdict contract | keep it narrowing-only and reopen only if [AGENT_READINESS_TELEMETRY_NARROWING_MEMO.md](AGENT_READINESS_TELEMETRY_NARROWING_MEMO.md) can be satisfied by a smaller telemetry object |
| `signed-trace-artifacts` | current donor evidence still reads as signed pack and trust-platform substrate rather than one standalone signed trace artifact contract | keep it narrowing-only and reopen only if [SIGNED_TRACE_ARTIFACTS_NARROWING_MEMO.md](SIGNED_TRACE_ARTIFACTS_NARROWING_MEMO.md) can be satisfied by a smaller signed trace object |

## Explicit Exclusions

| candidate | why excluded now | next honest move |
|---|---|---|
| `cross-agent-session-browser` | too close to [AOA-T-0053](../../../techniques/history/local-first-session-index/TECHNIQUE.md) plus donor app and browser product semantics | reopen only if a smaller browse-only contract survives independently from indexing and dashboard product behavior |
| `why-retrieval-from-code` | still accessor UX over lineage evidence rather than one separate reusable technique contract | reopen only if a bounded rationale-link or answerable-evidence contract survives independently from lineage and retrieval product behavior |

## Notes

- `transcript-replay-artifact`, `transcript-linked-code-lineage`, `fail-closed-evidence-gate`, and `approval-bound-durable-jobs` now exit the staged lane as landed `AOA-T-0066` through `AOA-T-0069`
- keep the history artifacts smaller than `AOA-T-0026`, `AOA-T-0044`, and `AOA-T-0045`
- keep telemetry and signed-trace work smaller than analytics and pack-platform doctrine
- keep governed-action candidates smaller than generic policy or security platforms
