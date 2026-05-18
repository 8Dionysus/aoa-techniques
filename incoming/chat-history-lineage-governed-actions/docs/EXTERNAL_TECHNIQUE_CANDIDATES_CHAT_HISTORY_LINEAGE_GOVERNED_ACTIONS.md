# External Technique Candidates - Chat History Lineage Governed Actions

This doc records the history, lineage, telemetry, and governed-action shard staged from the external chat wave pack.

Use it when the question is not "which landed technique should I open?", but "which Wave 1C candidate already landed cleanly, which ones closed without import, and which related candidates stay explicitly excluded?"

This is a staging and decision surface.
It does not create a canonical bundle or authorize import by itself.
The first-pass landing queue is exhausted; this packet now serves as evidence
and closed-verdict accounting.

## Scope

- this shard tracks `8` source-pack candidates
- `4` are already landed
- `0` remain staged for later triage
- `2` are closed without import
- `2` are explicit exclusions
- no candidate bundles are created in this packet

## Landed From This Shard

| candidate | landed bundle | boundary kept | what stayed out |
|---|---|---|---|
| `transcript-replay-artifact` | [AOA-T-0066](../../../techniques/history/transcript-replay-artifact/TECHNIQUE.md) | replayable post-capture artifact over existing saved sessions | session capture, transcript packaging, witness export, and hosted replay-platform doctrine |
| `transcript-linked-code-lineage` | [AOA-T-0067](../../../techniques/history/transcript-linked-code-lineage/TECHNIQUE.md) | bounded code-to-evidence link from code history back to saved session artifacts | generic repo analytics, scorecards, hosted search, and retrieval-product doctrine |
| `fail-closed-evidence-gate` | [AOA-T-0068](../../../techniques/governance/approval-evidence/fail-closed-evidence-gate/TECHNIQUE.md) | fail-closed execution-boundary gate with explicit evidence output | human confirmation doctrine, broad security constitutions, and total policy-platform semantics |
| `approval-bound-durable-jobs` | [AOA-T-0069](../../../techniques/governance/approval-evidence/approval-bound-durable-jobs/TECHNIQUE.md) | durable jobs that pause and resume across one explicit approval seam | full orchestration platform, scheduler doctrine, and generic automation stacks |

No remaining staged landing candidates in Wave 1C.

## Closed Non-Import Verdicts

| candidate | why closed | next honest move |
|---|---|---|
| `agent-readiness-telemetry` | current donor evidence still reads as analytics and scorecard product behavior rather than one standalone readiness artifact or verdict contract | keep it closed in this packet; a future attempt needs a new Distillation intake and the smaller telemetry object described in [AGENT_READINESS_TELEMETRY_CLOSEOUT_MEMO.md](AGENT_READINESS_TELEMETRY_CLOSEOUT_MEMO.md) |
| `signed-trace-artifacts` | current donor evidence still reads as signed pack and trust-platform substrate rather than one standalone signed trace artifact contract | keep it closed in this packet; a future attempt needs a new Distillation intake and the smaller signed trace object described in [SIGNED_TRACE_ARTIFACTS_CLOSEOUT_MEMO.md](SIGNED_TRACE_ARTIFACTS_CLOSEOUT_MEMO.md) |

## Explicit Exclusions

| candidate | why excluded now | next honest move |
|---|---|---|
| `cross-agent-session-browser` | too close to [AOA-T-0053](../../../techniques/history/local-first-session-index/TECHNIQUE.md) plus donor app and browser product semantics | keep closed unless a new intake proves a smaller browse-only contract independent from indexing and dashboard product behavior |
| `why-retrieval-from-code` | still accessor UX over lineage evidence rather than one separate reusable technique contract | keep closed unless a new intake proves a bounded rationale-link or answerable-evidence contract independent from lineage and retrieval product behavior |

## Notes

- `transcript-replay-artifact`, `transcript-linked-code-lineage`, `fail-closed-evidence-gate`, and `approval-bound-durable-jobs` now exit the staged lane as landed `AOA-T-0066` through `AOA-T-0069`
- keep the history artifacts smaller than `AOA-T-0026`, `AOA-T-0044`, and `AOA-T-0045`
- keep telemetry and signed-trace work smaller than analytics and pack-platform doctrine
- keep governed-action candidates smaller than generic policy or security platforms
