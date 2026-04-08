---
id: AOA-T-0065
name: mcp-gateway-proxy
domain: agent-workflows
kind: composition
status: promoted
origin:
  project: lasso-security/mcp-gateway
  path: README.md + mcp_gateway/gateway.py + mcp_gateway/server.py
  note: Adapted from the open-source MCP Gateway project, which fronts configured MCP servers through one explicit proxy surface with metadata lookup and request/response sanitization rather than exposing every upstream server directly to callers.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - mcp
  - gateway
  - proxy
  - tools
summary: Front multiple configured MCP servers through one bounded gateway proxy so callers use one reviewable tool surface with explicit metadata and sanitization instead of binding directly to each upstream server.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-28
export_ready: true
relations:
  - type: complements
    target: AOA-T-0038
evidence:
  - kind: external_origin
    path: notes/external-origin.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: external_review
    path: notes/external-import-review.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# mcp-gateway-proxy

## Intent

Front multiple configured MCP servers through one bounded gateway proxy so callers can use one reviewable tool surface with explicit metadata and sanitized boundaries instead of coupling themselves directly to each upstream server.

## When to use

- more than one MCP server or tool provider must be exposed behind one caller-facing surface
- callers should discover proxied capabilities through one explicit gateway rather than through ad hoc direct bindings
- the proxy should normalize metadata lookup or capability inspection before tool calls happen
- request and response sanitization should sit at the intermediary boundary instead of being reimplemented by every caller
- the reusable object is one gateway proxy seam, not a whole security, registry, or lifecycle platform

## When not to use

- one direct MCP server is enough and a gateway adds only ceremony
- the main need is local stack startup and shutdown rather than proxy mediation
- the real center of gravity is trust scoring, reputation scanning, or broader perimeter-security doctrine
- the workflow needs registry publication, capability search policy, or marketplace curation rather than runtime proxying
- the design would only make sense as a full proxy product with dashboards, tenancy, or enterprise policy layers

## Inputs

- one configured set of upstream MCP servers or equivalent tool providers
- one gateway-owned caller-facing endpoint
- one bounded metadata or capability lookup surface for proxied tools
- one sanitization posture for tool arguments, results, or both
- optional per-upstream config that remains subordinate to the gateway seam

## Outputs

- one unified caller-facing proxy surface over the configured upstream tools
- one explicit place to inspect proxied metadata before or alongside tool calls
- lower direct coupling between callers and the upstream server set
- one reviewable boundary where sanitization and upstream mediation happen

## Core procedure

1. Choose the bounded set of upstream MCP servers or tool providers that the gateway will front.
2. Configure one gateway-owned caller-facing surface instead of exposing each upstream directly to every caller.
3. Let the gateway surface proxied tool identity or metadata through one explicit lookup path.
4. Route tool calls through the gateway so request and response handling stays mediated at one boundary.
5. Sanitize arguments, results, or both at the proxy layer before returning data to callers.
6. Keep upstream-specific lifecycle, reputation scanning, tenancy, and broader security posture outside the invariant core.
7. Split out sibling techniques if the real reusable object becomes local stack lifecycle, registry doctrine, or security scanning rather than the proxy seam itself.

## Contracts

- the gateway is an explicit intermediary rather than an invisible pass-through
- callers interact with one bounded proxy surface instead of binding directly to each upstream server
- proxied metadata or capability lookup remains visible enough for review
- request or response sanitization happens at the gateway boundary when sanitization is part of the contract
- the technique stays smaller than local stack lifecycle, registry publication, capability discovery policy, and security-scanner doctrine
- upstream servers remain upstream; the gateway does not absorb their whole runtime or product semantics

Relationship to adjacent techniques: unlike [AOA-T-0038](../one-command-service-lifecycle/TECHNIQUE.md), this technique does not own starting and stopping a local service stack; it owns the mediation seam once a proxy surface exists. Unlike [AOA-T-0042](../../evaluation/upstream-skill-health-checking/TECHNIQUE.md), it does not score or preflight external sources before surfacing them; it fronts configured upstream servers at runtime. Unlike [AOA-T-0064](../../docs/capability-discovery/TECHNIQUE.md), it does not define publication-time discovery queries over registry entries; it exposes a runtime proxy surface over already-configured upstream tools.

## Risks

### Failure modes

- the gateway quietly becomes a full security platform instead of one bounded proxy seam
- callers still depend on upstream-specific behavior, so the proxy is not a meaningful mediation layer
- sanitization is claimed but not actually enforced at the proxy boundary
- lifecycle, scan, or dashboard features crowd out the proxy contract

### Negative effects

- a gateway layer adds operational complexity compared with direct upstream access
- a single proxy surface can hide useful upstream detail if metadata is too thin
- teams may overtrust gateway mediation and skip deeper review of risky upstream servers

### Misuse patterns

- relabeling a full perimeter-security or trust platform as if it were only a gateway proxy
- widening the bundle into tenancy, policy management, or enterprise governance
- treating local lifecycle ownership as part of the same technique by default
- using the proxy surface as a replacement for registry publication or curation

### Detection signals

- reviewers cannot explain which part of the system is the proxy seam and which part is a wider product surface
- metadata lookup disappears and callers still need upstream-specific manual knowledge before every call
- scan reports, trust scores, or policy modes dominate the bundle description
- startup and shutdown mechanics sound more central than proxy mediation itself

### Mitigations

- keep the caller-facing gateway surface explicit and bounded
- make proxy metadata and mediation visible enough that reviewers can inspect what is being fronted
- treat scanning, trust, lifecycle, and registry concerns as sibling techniques unless they stay truly subordinate
- split out broader platform behavior instead of widening the proxy contract

## Validation

Verify the technique by confirming that:
- more than one upstream server or tool surface can be fronted through one gateway seam
- callers can inspect proxied metadata or capability shape without binding directly to every upstream server
- tool calls pass through the gateway rather than bypassing it
- sanitization, when claimed, is visible at the gateway boundary
- the explanation still makes sense without lifecycle doctrine, trust scoring, or registry-platform semantics

See `checks/mcp-gateway-proxy-checklist.md`.

## Adaptation notes

What can vary across projects:
- the number and type of upstream MCP servers or tool providers
- whether the gateway exposes metadata, capability inspection, or both
- the exact sanitization rules applied at the boundary
- whether the gateway is local-only or network-facing
- the exact config carrier for upstream definitions

What should stay invariant:
- one explicit proxy surface fronts the configured upstreams
- callers use the proxy seam instead of direct per-upstream bindings
- proxy mediation remains reviewable
- lifecycle, scanning, and registry concerns stay separate unless they are truly subordinate

Project-shaped details that should not be treated as invariant:
- one CLI flag such as `--scan`
- one config filename
- enterprise trust posture, marketplace feeds, or reputation services
- dashboards, tenancy features, or product packaging

## Public sanitization notes

This public bundle keeps only the reusable gateway seam: one explicit proxy fronts configured upstream tool surfaces, exposes bounded metadata, and mediates calls through a sanitizing boundary. Scanner modes, reputation analysis, enterprise policy layers, tenancy, dashboards, and broader runtime product semantics were intentionally removed or generalized.

## Example

See `examples/minimal-mcp-gateway-proxy.md`.

## Checks

See `checks/mcp-gateway-proxy-checklist.md`.

## Promotion history

- adapted from open-source `lasso-security/mcp-gateway`
- landed from the Wave 1B tool-proxy-runtime shard inside `aoa-techniques`
- promoted into `aoa-techniques` on 2026-03-28 as a bounded external-import technique for one reviewable MCP gateway proxy surface

## Future evolution

- keep lifecycle ownership separate rather than widening this bundle back into [AOA-T-0038](../one-command-service-lifecycle/TECHNIQUE.md)
- keep registry publication and discovery doctrine separate rather than folding runtime proxying into `docs` techniques
- reopen a narrower trust or preflight sibling only if it survives without scanner-platform breadth
