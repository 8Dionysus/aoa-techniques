# TECHNIQUE_INDEX

This file is the repository-wide map of public techniques.

## Canonical techniques

| id | name | domain | status | summary |
|---|---|---|---|---|
| AOA-T-0001 | plan-diff-apply-verify-report | agent-workflows | canonical | Change protocol for safe, reviewable agent operations |
| AOA-T-0002 | source-of-truth-layout | docs | canonical | Repository document role separation to reduce drift |

## Promoted techniques

| id | name | domain | status | summary |
|---|---|---|---|---|
| AOA-T-0003 | contract-first-smoke-summary | evaluation | promoted | Runnable smoke pattern with machine-readable summary as the primary validation contract |
| AOA-T-0004 | intent-plan-dry-run-contract-chain | agent-workflows | promoted | Safe workflow that normalizes intent into a traceable plan, validates it with dry-run, and enforces contract checks |
| AOA-T-0005 | new-intent-rollout-checklist | agent-workflows | promoted | Checklist for safely adding a new intent type to an intent-plan-dry-run chain without contract drift |
| AOA-T-0006 | latest-alias-plus-history-copy | evaluation | promoted | Dual-write summary pattern that keeps a stable latest alias, preserves nested history, and prevents double-count accumulation |
| AOA-T-0007 | signal-first-gate-promotion | evaluation | promoted | Staged pattern for promoting an observed validation signal into strict enforcement without losing diagnostics or widening the fail surface too early |
| AOA-T-0008 | published-summary-remediation-snapshot | evaluation | promoted | Read-only aggregation of latest published summaries into a bounded remediation snapshot without history recomputation |
| AOA-T-0009 | lightweight-status-snapshot | docs | promoted | Keep top-level status documents short and link-driven while detailed execution state lives in canonical docs |
| AOA-T-0010 | telemetry-integrity-snapshot | evaluation | promoted | Read-only integrity verdict over latest published summaries, telemetry counters, and summary-layout invariants |
| AOA-T-0011 | required-vs-optional-source-rendering | evaluation | promoted | Keep required summary sources strict while optional enrichments degrade to warnings or not-available states |

## Deprecated techniques

| id | name | replacement | note |
|---|---|---|---|
| - | - | - | - |

## Notes

- `canonical` means recommended by default.
- `promoted` means reusable and public-safe, but not yet the main default.
- `deprecated` means historically preserved, but no longer preferred.
