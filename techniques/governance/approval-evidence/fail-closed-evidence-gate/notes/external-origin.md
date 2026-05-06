# External Origin Note

Use this note when a technique is adapted from an external open-source or public documentation source.
It complements `TECHNIQUE.md` and records provenance, adaptation boundaries, and public-safety review.

## Source

- source_repo: `https://github.com/Clyra-AI/gait`
- source_license: `Apache-2.0`
- inspired_by: not used in this import
- adapted_from: `README.md`, `docs/agent_integration_boundary.md`, and `docs/mcp_capability_matrix.md`

## What changed

- what_changed: narrowed the donor to one bounded seam: a verdict boundary sits directly before execution, non-allow blocks side effects, and one evidence artifact survives the verdict
- invariant core kept: execution fails closed unless allow is explicit, and the blocked or allowed path remains reviewable through evidence output
- project-shaped details removed or generalized: broader policy constitution, pack and callpack families, trust products, CI regression systems, and wider governance-platform semantics

## Public-safety review

- secrets or tokens removed: none from the donor surfaces used for this import
- private paths, URLs, or IDs removed: donor environment wiring, trust backends, and product-specific service names were omitted
- environment-specific assumptions generalized: the public technique does not depend on one MCP integration mode, one CLI binary, or one evidence-pack container
- remaining public-safety concerns: the main risks are drift into human confirmation doctrine on one side and drift into broad policy-platform semantics on the other

## Review notes

- why this adaptation is reusable here: many agent systems need one bounded gate that truly blocks mutation on non-allow while still leaving a reviewable evidence trail
- primary evidence used: the donor README and integration docs repeatedly state that the verdict service must sit before tool execution and that non-allow outcomes must not execute side effects, while the capability matrix shows explicit verify or proxy surfaces around that boundary
- limits or follow-up review concerns: durable jobs, signed traces, pack formats, and wider governance or trust semantics remain intentionally outside this import
