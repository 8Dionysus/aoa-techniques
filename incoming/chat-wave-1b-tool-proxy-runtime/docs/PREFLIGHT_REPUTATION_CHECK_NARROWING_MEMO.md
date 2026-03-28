# Narrowing Memo - preflight-reputation-check

This memo records the current narrowing result for the remaining Wave 1B candidate `preflight-reputation-check`.

It is a staging note only.
It does not create a canonical bundle or authorize import by itself.

## Candidate chosen

- `preflight-reputation-check`
- donor: `lasso-security/mcp-gateway`

## Overlap watch

- [AOA-T-0042](../../../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md)
- [AOA-T-0065](../../../techniques/agent-workflows/mcp-gateway-proxy/TECHNIQUE.md)

## Boundary statement

The current donor evidence does not yet expose one standalone reviewable reputation-check contract.

What is public today is a mixed scanner cluster:

- the donor README presents `--scan` as part of a wider secure-gateway product posture
- the scan path mixes package or source reputation hints with broader malicious-behavior checks
- the surrounding explanation still treats scanning as one mode inside a larger gateway and security surface
- the live bounded proxy seam is cleaner than the risk-scoring seam

That is useful product behavior, but it is not yet one sharply bounded technique in the `aoa-techniques` sense.

The narrowest plausible extraction target is:

- a pre-load source-risk verdict that runs before a proxied tool surface is trusted

Even that smaller target is not stable enough yet, because the donor still presents it mainly as scanner-platform behavior rather than as one reusable readiness or risk-check contract smaller than [AOA-T-0042](../../../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md).

## What stays out

- generic security governance and trust-platform doctrine
- vulnerability or malicious-behavior scanner breadth
- runtime proxy semantics already covered by [AOA-T-0065](../../../techniques/agent-workflows/mcp-gateway-proxy/TECHNIQUE.md)
- registry or marketplace policy
- speculative claims that reputation scanning is already one cleanly bounded public contract

## Evidence snapshot

- the donor README frames scanning as a security mode of the gateway rather than as an isolated readiness technique
- the scan path combines reputation-style checks with broader malicious-description and risk analysis
- the same donor keeps scanner posture close to runtime proxy product behavior instead of showing a distinct standalone contract
- the already-landed [AOA-T-0042](../../../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md) is still the cleaner bounded readiness sibling for now

## Verdict

- keep `preflight-reputation-check` in the `narrowing-only` lane
- do not create a bundle yet
- do not assign a technique ID yet

## Honest reopen trigger

Reopen this candidate only if the donor or a second public context can say, in plain language:

- what the bounded source-risk object is
- which checks belong to that object and which broader scanner behavior stays out
- how the verdict stays smaller than proxy doctrine and smaller than generic security governance
- why the reusable center is a preflight risk check rather than a scanner product mode

## Files touched or proposed

- touched: this memo
- touched: Wave 1B staging docs and registry to link the memo and keep the narrowing lane honest
- not proposed yet: no `TECHNIQUE.md`, no bundle-local example, no checklist seed, no note package

## Whether operator approval is needed

- no operator approval needed to keep this candidate in narrowing-only state
- operator approval is required before any future move from this memo into a real technique bundle
