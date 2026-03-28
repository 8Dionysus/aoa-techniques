# chat-wave-1b-tool-proxy-runtime

This is a repo-native active staging shard for tool-proxy and bounded runtime candidates from the external chat wave pack.

It keeps the donor queue reviewable under `incoming/` while avoiding collisions with the already-landed lifecycle and readiness families in the live corpus.

## Activation state

- `active`
- registry-first on the first pass
- one landed candidate, no remaining staged landing candidates
- one narrowing-only candidate with a current memo
- no seed bundles yet

## What this shard tracks

- landed from this shard:
  - `AOA-T-0065` / `mcp-gateway-proxy`
- active seed lane:
  - none
- narrowing-only lane:
  - `preflight-reputation-check` with a current memo in `docs/PREFLIGHT_REPUTATION_CHECK_NARROWING_MEMO.md`
- explicit exclusions routed out of first-pass landing:
  - `lifecycle-managed-tool-proxy`
  - `isolated-stateful-agent-runtime`
  - `bounded-single-step-agent`
  - `confirm-before-tool-execution`
  - `review-gated-multi-agent-orchestration`
  - `recursive-orchestrator-pattern`

## Operating posture

- keep the shard as staging soil, not merge authority
- keep `preflight-reputation-check` narrowing-only until its contract is smaller than scanner and security-platform doctrine
- do not reopen `AOA-T-0023`, `AOA-T-0028`, or `AOA-T-0038`
- keep cluster-runtime and orchestration-heavy candidates out rather than widening this shard
