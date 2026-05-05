# object-store-latest-history-layout

This example shows the same dual-write contract when published summaries live under generic object keys rather than local filesystem paths.

## Object keys

```text
published/gateway-readiness/latest/summary.json
published/gateway-readiness/history/2026-03-15T09-15-00Z/summary.json
published/gateway-readiness/history/2026-03-15T09-15-00Z/run.json
```

- `published/gateway-readiness/latest/summary.json` is the stable latest alias object.
- `published/gateway-readiness/history/2026-03-15T09-15-00Z/summary.json` is the immutable history copy for one execution.

## Producer metadata

If the producer emits path metadata, keep both object keys explicit:

```json
{
  "paths": {
    "latest_summary_key": "published/gateway-readiness/latest/summary.json",
    "history_summary_key": "published/gateway-readiness/history/2026-03-15T09-15-00Z/summary.json",
    "run_manifest_key": "published/gateway-readiness/history/2026-03-15T09-15-00Z/run.json"
  }
}
```

## Reader rule

1. Scan `published/gateway-readiness/history/*/summary.json`.
2. If history objects exist, accumulate only those objects.
3. Use the latest alias only for direct current-state consumers or explicit legacy fallback.

The storage medium changed, but the anti-double-count rule did not.
