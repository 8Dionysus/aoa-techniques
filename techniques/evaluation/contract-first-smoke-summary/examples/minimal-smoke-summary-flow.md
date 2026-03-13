# Minimal Smoke Summary Flow

This example shows a generic smoke path that publishes a machine-readable summary instead of relying on console logs as the main contract.

## Scenario

A repository has a smoke script that checks whether a local service can start and respond to one request.

## Flow

1. Run the smoke entrypoint.
2. Create normal run artifacts.
3. Write `smoke_summary.json` with an explicit status.
4. Exit with `0` when the summary contract is satisfied.
5. Exit non-zero when the contract fails.
6. Upload or read the same summary in CI, dashboards, or agent tooling.

## Example summary shape

```json
{
  "checked_at_utc": "2026-03-13T12:00:00Z",
  "ok": true,
  "status": "ok",
  "observed": {
    "request_count": 1,
    "latency_ms": 120
  },
  "violations": []
}
```

## Anti-drift rule

If downstream tooling must parse console logs to understand whether the smoke run passed, the summary contract is not strong enough yet.
