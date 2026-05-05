# object-store-remediation-snapshot

This example shows the same bounded remediation rollup when latest published summaries are stored under generic object keys.

## Source aliases

```text
published/gateway-readiness/latest/summary.json
published/gateway-governance/latest/summary.json
published/gateway-integrity/latest/summary.json
```

The helper reads only these latest alias objects. It does not scan `history/` prefixes or rebuild prior state.

## Fixed buckets

- `failing_now`
- `stale_inputs`
- `follow_up_needed`

## Per-bucket cap

Each bucket keeps at most 2 candidate items so the remediation surface stays reviewable.

## Example snapshot

```json
{
  "generated_at_utc": "2026-03-15T09:00:00Z",
  "source_count": 3,
  "truncated": false,
  "buckets": {
    "failing_now": [
      {
        "id": "gateway-readiness",
        "reason": "latest status is fail_nightly",
        "source_summary_key": "published/gateway-readiness/latest/summary.json"
      }
    ],
    "stale_inputs": [
      {
        "id": "gateway-integrity",
        "reason": "latest summary is older than freshness window",
        "source_summary_key": "published/gateway-integrity/latest/summary.json"
      }
    ],
    "follow_up_needed": [
      {
        "id": "gateway-governance",
        "reason": "governance state is hold with explicit gap remaining",
        "source_summary_key": "published/gateway-governance/latest/summary.json"
      }
    ]
  }
}
```

## Review rule

If a candidate item cannot point back to the exact published latest alias object that produced it, the remediation snapshot is too weak for operator or agent handoff.
