# minimal-remediation-snapshot

This example shows a portable remediation snapshot built from a small set of latest published summaries.

## Source aliases

```text
runs/gateway-sla/latest_summary.json
runs/gateway-readiness/latest_summary.json
runs/gateway-integrity/latest_summary.json
```

The snapshot reads only these latest aliases. It does not scan nested history directories or recompute prior runs.

## Fixed buckets

- `failing_now`
- `stale_inputs`
- `follow_up_needed`

## Per-bucket cap

Each bucket keeps at most 2 candidate items so the remediation surface stays reviewable.

## Example snapshot

```json
{
  "generated_at_utc": "2026-03-14T09:00:00Z",
  "source_count": 3,
  "truncated": false,
  "buckets": {
    "failing_now": [
      {
        "id": "gateway-sla",
        "reason": "latest status is fail_nightly",
        "source_summary_path": "runs/gateway-sla/latest_summary.json"
      }
    ],
    "stale_inputs": [
      {
        "id": "gateway-integrity",
        "reason": "latest summary is older than freshness window",
        "source_summary_path": "runs/gateway-integrity/latest_summary.json"
      }
    ],
    "follow_up_needed": [
      {
        "id": "gateway-readiness",
        "reason": "governance state is hold with explicit gap remaining",
        "source_summary_path": "runs/gateway-readiness/latest_summary.json"
      }
    ]
  }
}
```

## Review rule

If a candidate item cannot point back to the exact latest summary path that produced it, the remediation snapshot is too weak for operator or agent handoff.
