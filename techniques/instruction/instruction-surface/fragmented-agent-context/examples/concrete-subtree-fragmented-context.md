# Concrete Subtree Fragmented Context

This example keeps subtree-specific guidance close to the surfaces it explains, but still stops short of deterministic assembly.

## Fragment layout

`frontend/agents/context.md`

```md
Prefer intentional UI changes over generic layout churn.
```

`docs/agents/context.md`

```md
Keep public-safe wording explicit and avoid internal-only URLs.
```

`tests/agents/context.md`

```md
Run focused regression checks when a change touches generated surfaces.
```

## Review behavior

- each fragment sits near its local ownership boundary
- a reviewer can explain why a fragment belongs in that subtree
- the repository can later compose these fragments, but the authoring contract is already usable on its own
