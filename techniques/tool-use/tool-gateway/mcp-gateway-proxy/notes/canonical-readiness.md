# Canonical Readiness

## Technique
- id: AOA-T-0065
- name: mcp-gateway-proxy

## Verdict
- approve for canonical promotion

## Evidence summary
- external origin: the imported technique has a bounded donor contract and explicit exclusions around scanner posture, trust scoring, dashboards, lifecycle doctrine, and registry semantics
- second context: `aoa-techniques` now records the same proxy seam as a documentation-first adaptation with one example and one checklist
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- `smart-mcp-proxy/mcpproxy-go` provides exact-fit public reinforcement beyond the donor gateway family: MCPProxy exposes one MCP endpoint for clients, connects to multiple configured upstream MCP servers, indexes tool metadata from connected servers, names upstream tools with a `server:tool` format, mediates tool execution through built-in `call_tool_*` variants, records audit-oriented intent and activity detail, and can scan tool-call arguments and responses for sensitive-data patterns at the proxy boundary
- `TBXark/mcp-proxy` was checked as a supporting shape: it is a simpler MIT-licensed proxy that aggregates multiple configured MCP servers behind a single HTTP proxy surface, but it keeps per-server route keys and does not carry the same bounded tool-call mediation story as the primary evidence
- validation strength: the bundle now carries one checklist, one example, a clean external-origin note, a documentation-first second context, and public cross-context reinforcement for the same gateway-proxy contract

## Default-use rationale
- this is the right canonical default when the main problem is fronting several configured MCP servers through one explicit proxy seam instead of binding callers directly to each upstream surface
- it remains narrower than [AOA-T-0038](../../../../execution/runtime-truth-lifecycle/one-command-service-lifecycle/TECHNIQUE.md) because it does not own starting or stopping the runtime stack
- it also remains narrower than [AOA-T-0042](../../../../instruction/skill-discovery/upstream-skill-health-checking/TECHNIQUE.md) because it does not score or preflight upstream trust or readiness before publication
- it is now strong enough as a canonical default because MCPProxy repeats the same proxy-over-upstreams shape in a separate live project while still letting this bundle reject MCPProxy's wider product concerns: BM25 ranking policy, quarantine governance, Docker isolation, tray or web UI, OAuth, lifecycle management, activity-log product behavior, and full security-platform doctrine

## Fresh public-safety check
- review date: 2026-05-12
- result: pass
- sanitization still holds: the bundle keeps only the reusable proxy seam and excludes donor-specific scanner posture, dashboards, tenancy, and deployment guidance
- public reuse check: the example, checklist, and adaptation notes remain understandable without hidden donor-repo context; the inspected `smart-mcp-proxy/mcpproxy-go` and `TBXark/mcp-proxy` sources are MIT licensed and no source code, credentials, private endpoints, deployment secrets, tray/UI behavior, or local runtime setup was copied into the technique

## Remaining gaps
- no blocker remains for canonical status
- future gateway sources can reinforce the default, but they must preserve the narrow boundary: one explicit caller-facing proxy surface, multiple configured upstream tool servers, visible metadata or capability inspection, mediated tool calls, and any argument/result sanitization kept at the proxy boundary rather than widened into product governance

## Recommendation
- move `AOA-T-0065` to `canonical`
- add an adverse-effects review to preserve the boundary between the gateway proxy seam, local runtime lifecycle, upstream health checks, registry discovery, ranking/search policy, security quarantine, UI/product behavior, and enterprise MCP platform governance
