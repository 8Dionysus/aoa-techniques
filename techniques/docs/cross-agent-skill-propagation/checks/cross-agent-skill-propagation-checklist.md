# Cross-Agent Skill Propagation Checklist

- Name one canonical skill or rule source explicitly.
- Make at least two agent-facing targets receive the same shared core.
- Treat target files as managed or derived outputs.
- Keep target-specific wrappers minimal and destination-focused.
- Re-apply propagation from the canonical source when shared meaning changes.
- Avoid making any managed target the new source of truth.
- Keep runtime role semantics, MCP propagation, nested loading, and marketplace curation out of the contract.
