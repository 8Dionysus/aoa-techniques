# mcp-gateway-proxy checklist

- [ ] more than one upstream MCP server or tool surface is actually being fronted through the gateway seam
- [ ] callers use one explicit proxy surface instead of binding directly to every upstream server
- [ ] metadata or capability lookup is visible enough to inspect what the proxy fronts
- [ ] tool calls route through the gateway rather than bypassing it
- [ ] argument or result sanitization stays at the proxy boundary when sanitization is claimed
- [ ] the example stays smaller than local lifecycle, registry publication, or security-scanner doctrine
- [ ] dashboards, trust scores, and enterprise policy layers are not treated as the invariant core
- [ ] the public wording remains reusable and sanitized
