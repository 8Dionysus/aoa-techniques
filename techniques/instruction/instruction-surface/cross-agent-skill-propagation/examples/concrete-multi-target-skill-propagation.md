# Concrete Multi-Target Skill Propagation

This example shows one canonical shared rule core moving cleanly into several managed agent-facing targets.

## Canonical source

`rules/shared-agent-skill.md`

```md
# Shared Agent Skill Core

- Prefer small, reviewable diffs.
- Keep shared guidance in one canonical source.
- Treat target instruction files as managed outputs.
- Re-apply propagation after every shared-source change.
```

## Managed targets

`AGENTS.md`

```md
<!-- Managed output derived from rules/shared-agent-skill.md. -->
# Shared Agent Skill Core

- Prefer small, reviewable diffs.
- Keep shared guidance in one canonical source.
- Treat target instruction files as managed outputs.
- Re-apply propagation after every shared-source change.
```

`CLAUDE.md`

```md
<!-- Managed output derived from rules/shared-agent-skill.md. -->
# Shared Agent Skill Core

- Prefer small, reviewable diffs.
- Keep shared guidance in one canonical source.
- Treat target instruction files as managed outputs.
- Re-apply propagation after every shared-source change.
```

`GEMINI.md`

```md
<!-- Managed output derived from rules/shared-agent-skill.md. -->
# Shared Agent Skill Core

- Prefer small, reviewable diffs.
- Keep shared guidance in one canonical source.
- Treat target instruction files as managed outputs.
- Re-apply propagation after every shared-source change.
```

## What this proves

- one canonical source can keep several agent-facing targets synchronized
- the targets remain derived outputs instead of competing sources of truth
- the technique stays bounded to propagation, not to role generation, MCP propagation, or marketplace policy
