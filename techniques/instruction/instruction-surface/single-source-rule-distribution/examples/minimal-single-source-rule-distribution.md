# Minimal Single-Source Rule Distribution

This example shows one canonical rule source being propagated to two agent-facing instruction files.

## Canonical rule source

`rules/agent-guidance.md`

```md
# Shared Agent Guidance

- Prefer small, reviewable diffs.
- Treat generated instruction files as derived outputs.
- Route updates through the canonical rule source first.
```

## Managed targets

`AGENTS.md`

```md
<!-- Generated from rules/agent-guidance.md. Edit the source file instead. -->
# Shared Agent Guidance

- Prefer small, reviewable diffs.
- Treat generated instruction files as derived outputs.
- Route updates through the canonical rule source first.
```

`CLAUDE.md`

```md
<!-- Managed instruction file derived from rules/agent-guidance.md. -->
# Shared Agent Guidance

- Prefer small, reviewable diffs.
- Treat generated instruction files as derived outputs.
- Route updates through the canonical rule source first.
```

## What this proves

- one canonical source owns the shared rule content
- more than one target surface can stay aligned without copy-paste maintenance
- the target files are clearly marked as managed rather than canonical
