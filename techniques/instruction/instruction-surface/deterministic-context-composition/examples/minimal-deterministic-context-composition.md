# Minimal Deterministic Context Composition

This example shows a small fragment set that composes into one stable generated context artifact.

## Source fragments

`security.agents.md`

```md
<!-- priority: 10 -->
Always confirm destructive actions before execution.
```

`workflow.agents.md`

```md
Plan before apply.
State validation clearly in the final report.
```

## Generated context artifact

```md
<!-- Generated file. Edit source fragments instead. -->
<!-- source: security.agents.md priority=10 -->
Always confirm destructive actions before execution.
<!-- /source: security.agents.md -->
<!-- source: workflow.agents.md priority=0 -->
Plan before apply.
State validation clearly in the final report.
<!-- /source: workflow.agents.md -->
```

## Deterministic behavior

- the higher-priority fragment surfaces first
- the output keeps explicit source annotations
- contributors update fragment files rather than editing the generated artifact directly
