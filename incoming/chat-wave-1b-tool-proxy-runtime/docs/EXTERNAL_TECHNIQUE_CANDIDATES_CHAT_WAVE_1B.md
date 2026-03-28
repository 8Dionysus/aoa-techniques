# External Technique Candidates - Chat Wave 1B

This doc records the tool-proxy and bounded runtime shard staged from the external chat wave pack.

Use it when the question is not "which landed technique should I open?", but "which Wave 1B candidate already landed cleanly, which one stays narrowing-only, and which related candidates stay explicitly excluded?"

This is a staging and decision surface.
It does not create a canonical bundle or authorize import by itself.

## Scope

- this shard tracks `8` source-pack candidates
- `1` is already landed
- `0` remain staged for later triage
- `1` is narrowing-only
- `6` are explicit first-pass exclusions
- no seed bundles are created here yet

## Landed From This Shard

| candidate | landed bundle | boundary kept | what stayed out |
|---|---|---|---|---|
| `mcp-gateway-proxy` | [AOA-T-0065](../../../techniques/agent-workflows/mcp-gateway-proxy/TECHNIQUE.md) | one explicit gateway proxy in front of configured MCP servers with bounded metadata lookup and mediated calls | scanner modes, reputation scoring, lifecycle doctrine, and broader gateway-product semantics |

No remaining staged landing candidates in Wave 1B.

## Narrowing-Only Lane

| candidate | why not landed yet | next honest move |
|---|---|---|
| `preflight-reputation-check` | current donor evidence still reads as scanner-mode and security-product behavior rather than one standalone bounded verdict contract | keep it narrowing-only and reopen only if [PREFLIGHT_REPUTATION_CHECK_NARROWING_MEMO.md](PREFLIGHT_REPUTATION_CHECK_NARROWING_MEMO.md) can be satisfied by a smaller preflight risk-check contract |

## Explicit Exclusions

| candidate | why excluded now | next honest move |
|---|---|---|
| `lifecycle-managed-tool-proxy` | lifecycle ownership collapses into [AOA-T-0038](../../../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) plus proxy-specific startup detail rather than one new smaller contract | reopen only if a proxy-owned lifecycle seam survives independently from general local stack lifecycle |
| `isolated-stateful-agent-runtime` | still cluster and sandbox platform doctrine rather than one bounded technique object | reopen only if a smaller runtime-slot contract survives without Kubernetes or product-platform breadth |
| `bounded-single-step-agent` | already covered by `AOA-T-0023 stateless-single-shot-agent` | leave closed unless a new contract survives outside the single-shot fast path |
| `confirm-before-tool-execution` | already covered by `AOA-T-0028 confirmation-gated-mutating-action` | leave closed unless a narrower tool-only confirmation seam appears |
| `review-gated-multi-agent-orchestration` | still broad orchestration doctrine rather than one bounded reusable object | keep excluded until one smaller governed seam stands alone |
| `recursive-orchestrator-pattern` | still architecture-shaped and not technique-bounded | keep excluded unless a smaller reusable contract can be named without the orchestration stack |

## Notes

- `mcp-gateway-proxy` now exits the staged lane as landed `AOA-T-0065`
- keep `preflight-reputation-check` narrowing-only until a smaller risk-check contract survives independently of scanner-platform semantics
- keep lifecycle-managed proxy work separate from the already-landed lifecycle family
- do not let the first pass widen into sandbox platform, scanner product, or orchestration worldview
