# minimal-telemetry-integrity-snapshot

This example shows a compact integrity verdict built from latest published summaries.

## Latest sources

```text
runs/nightly-readiness/readiness_summary.json
runs/nightly-governance/governance_summary.json
runs/nightly-progress/progress_summary.json
runs/nightly-transition/transition_summary.json
runs/nightly-remediation/remediation_summary.json
runs/nightly-manual-cadence/cadence_brief.json
```

The first five are required. `manual-cadence` is optional and only used for extra consistency checks.

## Example snapshot

```json
{
  "integrity_status": "attention",
  "reason_codes": [
    "telemetry_counters_nonzero",
    "anti_double_count_invariant_broken"
  ],
  "observed": {
    "telemetry_ok": false,
    "dual_write_ok": false,
    "anti_double_count_ok": false,
    "utc_guardrail_status": "not_available"
  }
}
```

## Interpretation rule

The snapshot tells operators whether the published summaries are trustworthy enough to interpret. It does not itself replay history, repair data, or create a new hard gate.
