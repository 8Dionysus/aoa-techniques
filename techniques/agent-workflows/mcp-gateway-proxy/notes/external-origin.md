# External Origin Note

Use this note when a technique is adapted from an external open-source or public documentation source.
It complements `TECHNIQUE.md` and records provenance, adaptation boundaries, and public-safety review.

## Source

- source_repo: `https://github.com/lasso-security/mcp-gateway`
- source_license: `MIT`
- inspired_by: not used in this import
- adapted_from: `README.md`, `mcp_gateway/gateway.py`, and `mcp_gateway/server.py`

## What changed

- what_changed: narrowed the donor to one bounded seam: front configured MCP servers through one explicit gateway proxy with metadata lookup and mediated tool calls
- invariant core kept: one gateway surface fronts multiple upstream servers, proxied tools stay reviewable through explicit metadata, and request or response handling can be sanitized at the proxy boundary
- project-shaped details removed or generalized: scanner modes, reputation analysis, enterprise trust posture, dashboards, tenancy, deployment packaging, and broader runtime product semantics

## Public-safety review

- secrets or tokens removed: none from the donor surfaces used for this import
- private paths, URLs, or IDs removed: deployment-specific endpoints, internal trust backends, and product packaging details were omitted
- environment-specific assumptions generalized: the public technique does not depend on one config filename, one hosting topology, or one enterprise runtime
- remaining public-safety concerns: the main risks are drift into local lifecycle doctrine on one side and drift into scanner or security-platform doctrine on the other

## Review notes

- why this adaptation is reusable here: many tool-heavy agent systems need one explicit proxy seam in front of several upstream MCP servers without importing a whole runtime or security platform
- primary evidence used: the donor README frames the project as a secure gateway for MCP servers, `gateway.py` dynamically exposes proxied tools plus gateway-owned metadata, and `server.py` shows the per-upstream proxy wrapper plus request and response sanitization
- limits or follow-up review concerns: lifecycle ownership, scanner posture, trust scoring, and wider product semantics remain intentionally outside this import
