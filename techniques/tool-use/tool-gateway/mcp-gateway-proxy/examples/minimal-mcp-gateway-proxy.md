# minimal mcp-gateway-proxy

Configured upstreams:

- `git-tools`
- `docs-reader`

Gateway surface:

- caller endpoint: `gateway`
- metadata tool: `get_metadata`

Proxy behavior:

```text
caller -> gateway.call_tool("git_status", {})
caller -> gateway.call_tool("read_doc", {"path": "README.md"})
```

Visible metadata:

```json
{
  "upstreams": ["git-tools", "docs-reader"],
  "proxied_tools": ["git_status", "read_doc"]
}
```

Why this example stays bounded:

- the caller talks to one gateway surface
- metadata and tool mediation are explicit
- the example does not depend on scanner modes, lifecycle doctrine, or registry product behavior
