# Second Context Adaptation

## Technique
- id: AOA-T-0065
- name: mcp-gateway-proxy

## Target project
- name: aoa-techniques
- environment: public technique repository with authored bundle contracts, generated routing surfaces, and validator-backed markdown discipline
- runtime: documentation-first corpus that records one bounded proxy seam rather than shipping the donor gateway implementation or scanner stack

## What changed

- paths: the donor ships a real MCP gateway and proxy wrapper; this adaptation keeps the generic caller-facing proxy seam without requiring one runtime package or one gateway binary
- services: scanner modes, reputation checks, dashboards, and broader enterprise product surfaces were removed from the reusable contract
- dependencies: the adaptation depends on configured upstream servers plus one caller-facing proxy surface, not on the donor deployment or security stack
- operating assumptions: contributors should read the technique as runtime mediation over configured upstream tool surfaces, not as a full security gateway platform

## What stayed invariant

- contract: callers meet one explicit gateway seam instead of binding directly to each upstream server
- validation logic: proxied metadata and mediated tool calls remain visible enough for review
- safety rules: proxy mediation stays separate from lifecycle doctrine, registry doctrine, and scanner-product breadth

## Risks introduced by adaptation

- the pattern can collapse into [AOA-T-0038](../one-command-service-lifecycle/TECHNIQUE.md) if repositories let startup and shutdown mechanics overshadow the proxy seam
- the public bundle could drift into [AOA-T-0042](../../evaluation/upstream-skill-health-checking/TECHNIQUE.md) if source trust or scanner verdicts become the main story
- teams may over-associate MCP proxying with marketplace or registry discovery if publication-time and runtime-time surfaces are not kept distinct

## Evidence

- the donor README presents the gateway as one surface in front of multiple MCP servers and describes metadata exposure plus request and response sanitization
- `gateway.py` dynamically registers proxied tool and prompt behavior while also exposing gateway-owned metadata
- `server.py` wraps individual upstream servers, caches surfaced capabilities, and mediates calls through a sanitizing layer
- those same sources also show why scanner posture and broader security semantics should remain sibling concerns instead of widening the proxy contract itself

## Result

- works as a documentation-first second context and preserves one bounded runtime proxy seam without carrying over the donor's scanner, product, or deployment breadth
