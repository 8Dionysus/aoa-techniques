# chat-tool-proxy-runtime

This is a repo-native evidence packet for tool-proxy and bounded runtime
candidates from the external chat wave pack.

It keeps the donor verdicts reviewable under `incoming/` while avoiding
collisions with the already-landed lifecycle and readiness families in the live
corpus. It is not an active landing lane.

## Activation state

- `evidence-only`
- registry-first on the first pass
- one landed candidate, no remaining staged landing candidates
- one closed non-import candidate with a closeout memo
- no active non-landed tail remains in this packet
- no candidate bundles in this packet

## What this shard tracks

- landed from this shard:
  - `AOA-T-0065` / `mcp-gateway-proxy`
- seed lane:
  - none
- closed non-import:
  - `preflight-reputation-check` with final rationale in `docs/PREFLIGHT_REPUTATION_CHECK_CLOSEOUT_MEMO.md`
- explicit exclusions routed out of first-pass landing:
  - `lifecycle-managed-tool-proxy`
  - `isolated-stateful-agent-runtime`
  - `bounded-single-step-agent`
  - `confirm-before-tool-execution`
  - `review-gated-multi-agent-orchestration`
  - `recursive-orchestrator-pattern`

## Operating posture

- keep the packet as evidence, not merge authority
- keep `preflight-reputation-check` closed unless fresh evidence proves a smaller atom than scanner and security-platform doctrine
- do not revisit `AOA-T-0023`, `AOA-T-0028`, or `AOA-T-0038` from this packet
- keep cluster-runtime and orchestration-heavy candidates out rather than widening this shard
- any future attempt for a closed candidate must start as a new Distillation intake with fresh evidence
