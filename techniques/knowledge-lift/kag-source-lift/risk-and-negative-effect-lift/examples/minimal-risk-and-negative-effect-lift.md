# Minimal Risk And Negative-Effect Lift

This example shows how a richer `Risks` section can support bounded caution lookup without creating a new caution metadata or scoring surface.

## Source bundle excerpt

```md
## Risks

### Failure modes
- the summary surface can look complete even when a source silently stopped updating

### Negative effects
- operators can trust the report too early because it still renders cleanly

### Misuse patterns
- teams start treating the pattern as a generic health score instead of one bounded check

### Detection signals
- the report keeps rendering but freshness counters stop changing

### Mitigations
- route the reader back to the source checks and tighten the bounded contract
```

## Bounded caution-lift usage

```md
Review prompt for this technique:
- Open `## Risks` first when you need to understand hidden downside before reuse.
- Check `Failure modes` and `Detection signals` together for false-success risk.
- Read `Mitigations` before widening the pattern into a new environment.
```

## Anti-drift rule

If a team needs caution IDs, scores, or generated caution outputs to answer the review question, this bounded lift is no longer the right technique.
