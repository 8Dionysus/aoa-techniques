# Minimal Cross-Agent Skill Propagation

Use one canonical rule source and propagate the same shared core to several managed agent-facing targets.

## Canonical source

`rules/shared-agent-guidance.md`

```md
# Shared Agent Guidance

- Prefer small, reviewable diffs.
- Treat agent-facing target files as managed outputs.
- Route shared instruction changes through the canonical source first.
- Re-apply propagation after editing the source.
```

## Managed targets

`AGENTS.md`

```md
<!-- Managed output derived from rules/shared-agent-guidance.md. -->
# Shared Agent Guidance

- Prefer small, reviewable diffs.
- Treat agent-facing target files as managed outputs.
- Route shared instruction changes through the canonical source first.
- Re-apply propagation after editing the source.
```

`CLAUDE.md`

```md
<!-- Managed output derived from rules/shared-agent-guidance.md. -->
# Shared Agent Guidance

- Prefer small, reviewable diffs.
- Treat agent-facing target files as managed outputs.
- Route shared instruction changes through the canonical source first.
- Re-apply propagation after editing the source.
```

## What this proves

- one canonical skill or rule source can fan out to multiple agent-facing targets
- managed targets can stay aligned without copy-paste maintenance
- the shared core remains readable even when wrapper text is destination-specific
