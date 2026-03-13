# minimal-latest-history-layout

This example shows a generic dual-write layout for a machine-readable summary.

## Layout

```text
runs/
  latest-check/
    summary.json
    20260313_101500-check/
      run.json
      summary.json
```

- `runs/latest-check/summary.json` is the stable latest alias.
- `runs/latest-check/20260313_101500-check/summary.json` is the history copy for one execution.

## Producer metadata

If the producer emits path metadata, keep both paths explicit:

```json
{
  "paths": {
    "run_dir": "runs/latest-check/20260313_101500-check",
    "summary_json": "runs/latest-check/summary.json",
    "history_summary_json": "runs/latest-check/20260313_101500-check/summary.json"
  }
}
```

## Reader rule

Use nested history rows first:

1. Scan `runs/latest-check/**/summary.json`.
2. If nested rows exist, accumulate only those rows.
3. If no nested rows exist, fall back to `runs/latest-check/summary.json` for legacy compatibility.

This keeps the latest alias easy to consume without letting scanners count the same run twice.
