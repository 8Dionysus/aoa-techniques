# Direct Relation To Selection Hint

This example shows how a bounded direct relation can help a generated navigation surface without turning the repository into a graph engine.

## Source frontmatter excerpt

```yaml
relations:
  - type: requires
    target: AOA-T-0019
```

## Derived selection hint

```md
- [AOA-T-0021](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md): `requires` [AOA-T-0019](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md)
```

## Why this stays bounded

- the edge says only that one direct contract depends on another existing contract
- it does not explain the full rationale
- it does not imply multi-hop traversal, scoring, or graph truth

## Anti-drift rule

If the selection surface must infer extra edges or hidden rationale to stay useful, the relation lift has widened beyond direct adjacency.
