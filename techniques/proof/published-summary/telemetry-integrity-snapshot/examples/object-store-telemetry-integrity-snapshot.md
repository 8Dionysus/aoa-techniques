# object-store-telemetry-integrity-snapshot

This example shows a diagnostic integrity verdict over latest published summaries stored as generic object keys.

## Latest sources

```text
published/nightly-readiness/latest/summary.json
published/nightly-governance/latest/summary.json
published/nightly-progress/latest/summary.json
published/nightly-transition/latest/summary.json
published/nightly-remediation/latest/summary.json
published/nightly-cadence/latest/brief.json
```

The first five are required. `published/nightly-cadence/latest/brief.json` is optional and only used for extra consistency checks.

## Example snapshot

```json
{
  "integrity_status": "attention",
  "reason_codes": [
    "telemetry_counters_nonzero",
    "anti_double_count_invariant_broken"
  ],
  "observed": {
    "required_sources_ok": true,
    "telemetry_ok": false,
    "dual_write_ok": false,
    "anti_double_count_ok": false,
    "cadence_consistency_status": "not_available"
  },
  "source_keys": {
    "readiness": "published/nightly-readiness/latest/summary.json",
    "remediation": "published/nightly-remediation/latest/summary.json",
    "cadence": "published/nightly-cadence/latest/brief.json"
  }
}
```

## Interpretation rule

The snapshot tells downstream consumers whether the published summaries are trustworthy enough to interpret. It does not itself repair broken artifacts or become the enforcement gate.
