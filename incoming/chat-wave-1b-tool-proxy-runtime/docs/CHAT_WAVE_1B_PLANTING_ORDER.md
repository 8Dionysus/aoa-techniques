# Chat Wave 1B - Planting Order

This note is for operator-guided staging inside `aoa-techniques`.

## Hard rules

- keep Wave 1B registry-only on the first pass
- do not create seed bundles here yet
- do not reopen landed single-shot, confirmation-gated, or lifecycle techniques
- keep orchestration-heavy exclusions closed

## Landed first

1. `mcp-gateway-proxy` is now landed as `AOA-T-0065` by the main agent

## Preferred sequence

2. `preflight-reputation-check` remains narrowing-only; see `docs/PREFLIGHT_REPUTATION_CHECK_NARROWING_MEMO.md`

Why this order:

- the gateway proxy was the cleanest anchor
- the reputation-check seam still needs tighter scoping than the proxy itself
- lifecycle-managed proxy collapses into the already-landed lifecycle family on the first pass
- isolated runtime still has the highest risk of widening into platform doctrine

Current exclusion verdicts:

- keep `lifecycle-managed-tool-proxy` out of `techniques/` for now
- keep `isolated-stateful-agent-runtime` out of `techniques/` for now
- keep `docs/PREFLIGHT_REPUTATION_CHECK_NARROWING_MEMO.md` as the active reopen gate for the only remaining non-excluded candidate

## Explicit exclusions to leave closed

- `lifecycle-managed-tool-proxy`
- `isolated-stateful-agent-runtime`
- `bounded-single-step-agent`
- `confirm-before-tool-execution`
- `review-gated-multi-agent-orchestration`
- `recursive-orchestrator-pattern`

## Stop conditions

Stop and leave the shard staged if:

- a candidate needs platform or cluster doctrine to make sense
- the contract collapses into scanner or security governance
- the candidate no longer stays smaller than `AOA-T-0038`
