# Minimal Multi-Source Primary Input Provenance

When combining inputs from multiple sources, name the one that should lead.

```md
# Bridge Notes

- primary source: `source-a`
- supporting source: `source-b`
- supporting source: `source-c`

The summary below should preserve `source-a` as the primary input when readers cite or synthesize this bridge.

If `source-b` conflicts with `source-a`, keep the conflict visible and mark it for review instead of silently re-ranking the sources.
```

The important behavior is bounded:

- the primary input stays visible
- supporting inputs stay visible
- supporting inputs can add context or challenge the reading without quietly replacing the primary anchor
- downstream readers do not need graph semantics to preserve the order
- this step does not rank sources, infer trust, silently override the primary input, or turn the bridge into a graph
