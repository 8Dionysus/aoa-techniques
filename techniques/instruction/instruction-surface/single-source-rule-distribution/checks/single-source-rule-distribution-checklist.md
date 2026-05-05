# Single-Source Rule Distribution Checklist

Use this checklist to validate whether a repository really follows `single-source-rule-distribution`.

- One canonical rule source is named explicitly.
- At least two agent-facing instruction surfaces receive the shared rule core.
- Target files are treated as managed or derived outputs.
- Contributors can tell they should edit the canonical source first, not the target files.
- Re-applying the distribution step does not duplicate shared instructions in target surfaces.
- Target-specific formatting stays minimal and does not change the shared rule intent.
- MCP propagation, skills propagation, nested loading, or other wider behavior are not silently bundled into the same technique contract.
