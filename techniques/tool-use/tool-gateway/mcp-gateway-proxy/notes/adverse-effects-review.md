# Adverse Effects Review

## Technique
- id: AOA-T-0065
- name: mcp-gateway-proxy

## Review focus
- promotion from `promoted` to `canonical` after exact-fit public reinforcement from `smart-mcp-proxy/mcpproxy-go`
- failure cases where one MCP gateway proxy seam is mistaken for lifecycle management, search ranking, security quarantine, registry governance, product UI, or a full MCP platform

## Failure modes
- the gateway becomes an opaque tunnel and reviewers cannot inspect proxied tool metadata before calls
- callers still rely on upstream-specific direct bindings, so the proxy is only another endpoint and not a meaningful mediation boundary
- sanitization is claimed from a source that only forwards calls and does not inspect, filter, redact, or bound arguments and results
- runtime lifecycle, upstream restart, Docker isolation, OAuth, or management commands become more central than the caller-facing proxy seam
- BM25 ranking, routing modes, retrieve-tools policy, or recommendation behavior is treated as part of the gateway invariant

## Negative effects
- a unified proxy can hide upstream-specific risk if metadata and call provenance are too thin
- proxy success can encourage teams to skip reviewing risky upstream servers
- product-rich gateway sources can pull the technique toward dashboards, quarantine governance, telemetry, installers, or enterprise policy faster than the atomic move can support
- a gateway adds operational complexity compared with direct upstream access, especially for small tool sets

## Misuse patterns
- importing tray apps, web dashboards, package repositories, UI behavior, or release channels as if they were part of the technique
- treating Docker isolation, process supervision, upstream health checks, OAuth, token management, or restart commands as required gateway-proxy behavior
- using the proxy as a substitute for registry publication, capability discovery, marketplace curation, or trust-policy review
- treating sensitive-data detection, quarantine, scanner plugins, RBAC, or audit dashboards as proof that every upstream tool is safe
- folding tool ranking, context-window optimization, or routing-mode selection into the same technique

## Detection signals
- review prose cannot name the caller-facing proxy surface separately from the broader product or runtime
- metadata lookup disappears and callers need upstream-specific manual knowledge before each call
- proxy examples focus on management UI, install flow, OAuth setup, or Docker lifecycle instead of visible capability metadata and mediated tool calls
- search quality, quarantine status, or dashboard state dominates the explanation
- source evidence supports aggregation but not argument/result inspection, yet the bundle starts overclaiming sanitization

## Mitigations
- keep one explicit caller-facing gateway seam as the invariant center
- require visible proxied metadata, capability shape, or server-scoped tool names before treating a source as strong evidence
- keep mediated call paths distinct from registry publication, discovery ranking, and local service lifecycle
- record partial support when a source proves only aggregation or routing, and reserve full canonical support for evidence with mediation and boundary inspection
- split routing modes, tool ranking, quarantine governance, lifecycle orchestration, OAuth, UI/dashboard behavior, and MCP platform governance into sibling surfaces if they become the actual reusable object

## Recommendation
- safe to promote as a canonical tool-use technique when the implementation keeps gateway mediation, proxied metadata, and argument/result boundary review smaller than lifecycle, registry, ranking, quarantine, UI, or platform governance
- use this note as the watch surface for proxy-product creep, lifecycle creep, search/ranking creep, security-platform creep, registry creep, and sanitization overclaim
