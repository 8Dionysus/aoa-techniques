# Concrete Multi-Agent Rule Sync

This example shows one canonical instruction source distributing the same shared rule core to several managed agent-facing targets.

## Canonical rule source

`rules/shared-agent-guidance.md`

```md
# Shared Agent Guidance

- Prefer small, reviewable diffs.
- Route shared instruction changes through this file first.
- Treat generated instruction targets as managed outputs.
- Re-run distribution after changing the canonical rule source.
```

## Managed targets

`AGENTS.md`

```md
<!-- Managed output derived from rules/shared-agent-guidance.md. -->
# Shared Agent Guidance

- Prefer small, reviewable diffs.
- Route shared instruction changes through this file first.
- Treat generated instruction targets as managed outputs.
- Re-run distribution after changing the canonical rule source.
```

`CLAUDE.md`

```md
<!-- Managed output derived from rules/shared-agent-guidance.md. -->
# Shared Agent Guidance

- Prefer small, reviewable diffs.
- Route shared instruction changes through this file first.
- Treat generated instruction targets as managed outputs.
- Re-run distribution after changing the canonical rule source.
```

`GEMINI.md`

```md
<!-- Managed output derived from rules/shared-agent-guidance.md. -->
# Shared Agent Guidance

- Prefer small, reviewable diffs.
- Route shared instruction changes through this file first.
- Treat generated instruction targets as managed outputs.
- Re-run distribution after changing the canonical rule source.
```

## Distribution contract

- `rules/shared-agent-guidance.md` is the only canonical location for the shared rule core.
- The target files may add minimal destination-specific wrappers, but they do not become separate sources of truth.
- Re-applying the distribution step must refresh all managed targets without duplicating or silently reshaping the shared rules.
- Review starts with the canonical source diff and uses the target files only to confirm synchronized distribution.

## What this proves

- one canonical rule source can keep several agent-facing instruction targets aligned
- the pattern stays bounded to one-source fan-out rather than many-fragment composition into one artifact
- target-specific wrappers can stay minimal without changing the shared rule intent
- contributors can tell that edits belong in the canonical source, not in each managed target
