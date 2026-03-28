# Canonical Readiness

## Technique
- id: AOA-T-0065
- name: mcp-gateway-proxy

## Verdict
- bounded defer for now

## Evidence summary
- external origin: the imported technique has a bounded donor contract and explicit exclusions around scanner posture, trust scoring, dashboards, lifecycle doctrine, and registry semantics
- second context: `aoa-techniques` now records the same proxy seam as a documentation-first adaptation with one example and one checklist
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- validation strength: the bundle now carries one checklist, one example, a clean external-origin note, and one documentation-first second context, but it still lacks a live adopter beyond the donor gateway family

## Default-use rationale
- this is the right promoted default when the main problem is fronting several configured MCP servers through one explicit proxy seam instead of binding callers directly to each upstream surface
- it remains narrower than [AOA-T-0038](../one-command-service-lifecycle/TECHNIQUE.md) because it does not own starting or stopping the runtime stack
- it also remains narrower than [AOA-T-0042](../../evaluation/upstream-skill-health-checking/TECHNIQUE.md) because it does not score or preflight upstream trust or readiness before publication

## Fresh public-safety check
- review date: 2026-03-28
- result: pass
- sanitization still holds: the bundle keeps only the reusable proxy seam and excludes donor-specific scanner posture, dashboards, tenancy, and deployment guidance
- public reuse check: the example, checklist, and adaptation notes remain understandable without hidden donor-repo context

## Remaining gaps
- the smallest remaining gap is still one live second context beyond the donor and documentation-first adaptation
- specifically, the bundle still needs another public repository or surface family that uses one bounded gateway proxy seam without widening into security-platform or runtime-product doctrine

## Recommendation
- keep `AOA-T-0065` `promoted`
- defer canonical promotion until another live adopter confirms that the proxy seam survives outside the donor gateway family
