# chat-wave-1c-history-lineage-governed-actions

This is a repo-native active staging shard for history, code-lineage, telemetry, and governed-action candidates from the external chat wave pack.

It keeps the queue reviewable under `incoming/` while respecting the already-landed history artifact family and existing confirmation-boundary techniques.

## Activation state

- `active`
- registry-first on the first pass
- four landed candidates, no remaining staged landing candidates
- two narrowing-only candidates with current memos
- no seed bundles yet

## What this shard tracks

- landed from this shard:
  - `AOA-T-0066` / `transcript-replay-artifact`
  - `AOA-T-0067` / `transcript-linked-code-lineage`
  - `AOA-T-0068` / `fail-closed-evidence-gate`
  - `AOA-T-0069` / `approval-bound-durable-jobs`
- active seed lane:
  - none
- narrowing-only lane:
  - `agent-readiness-telemetry` with a current memo in `docs/AGENT_READINESS_TELEMETRY_NARROWING_MEMO.md`
  - `signed-trace-artifacts` with a current memo in `docs/SIGNED_TRACE_ARTIFACTS_NARROWING_MEMO.md`
- explicit exclusions routed out of first-pass landing:
  - `cross-agent-session-browser`
  - `why-retrieval-from-code`

## Operating posture

- keep the shard as staging soil, not merge authority
- keep telemetry and signed-trace work in narrowing-only state until they are smaller than analytics or pack-platform doctrine
- do not reopen the landed Wave C history family
- do not turn governed actions into a broad policy stack on the first pass
