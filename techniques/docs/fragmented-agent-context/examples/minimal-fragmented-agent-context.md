# Minimal Fragmented Agent Context

This example shows fragment-first authoring before any generated aggregate exists.

## Fragment set

`docs/agent-context/review.md`

```md
Always summarize the intended change before editing tracked files.
```

`docs/agent-context/validation.md`

```md
State the exact validation commands you actually ran.
```

## Why this already helps

- each fragment owns one narrow topic
- contributors can update one area without reopening a giant shared context file
- deterministic assembly can be added later, but fragment ownership is already clear
