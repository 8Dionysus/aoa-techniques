# minimal-signal-first-rollout

This example shows a generic staged promotion path from observation to strict enforcement.

## 1. Start in `signal_only`

Run one summary-producing check in observational mode:

```bash
python scripts/check_service_health.py --policy signal_only --summary-json runs/health/latest_summary.json
```

- the summary is still published when the signal is bad
- exit behavior stays non-blocking while the signal is being calibrated

## 2. Add readiness over recent history

Build a readiness summary from recent published runs:

```bash
python scripts/check_service_health_readiness.py --history-dir runs/health-history --policy report_only --summary-json runs/health-readiness/readiness_summary.json
```

The readiness layer asks whether the signal has been stable enough for a stricter rollout.

## 3. Make governance explicit

Turn readiness evidence into a formal decision:

```bash
python scripts/check_service_health_governance.py --readiness-dir runs/health-readiness --policy report_only --summary-json runs/health-governance/governance_summary.json
```

The output should be a clear `go` or `hold`, not an implicit guess.

## 4. Publish progress telemetry

Track the remaining gap:

- runs still needed
- streak still needed
- reason codes explaining why promotion is not complete yet

## 5. Promote one narrow strict surface

When governance says `go`, enable strict behavior only on one narrow surface such as a nightly job:

- nightly: strict `fail_nightly`
- pull requests: still `signal_only`
- local debugging: still observational

Diagnostics should continue to publish even if the strict nightly run goes red.
