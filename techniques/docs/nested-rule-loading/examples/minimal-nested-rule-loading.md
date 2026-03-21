# Minimal Nested Rule Loading

Use one canonical parent source and one nested child layer with explicit precedence.

## Canonical parent

`rules/shared-rule-core.md`

```md
# Shared Rule Core

- Prefer small, reviewable diffs.
- Keep shared meaning in one canonical source.
- Treat nested layers as subordinate additions.
- Re-run loading when precedence rules change.
```

## Nested child layer

`rules/projects/alpha/nested-rules.md`

```md
<!-- Nested output derived from rules/shared-rule-core.md plus scoped child additions. -->
# Shared Rule Core

- Prefer small, reviewable diffs.
- Keep shared meaning in one canonical source.
- Treat nested layers as subordinate additions.
- Re-run loading when precedence rules change.

## Project-specific addition

- Allow one scoped override for alpha-only terminology.
```

## What this proves

- the canonical source still owns the shared rule meaning
- the nested layer stays subordinate and scoped
- precedence is explicit rather than accidental
