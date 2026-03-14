# TECHNIQUE_INDEX

This file is the repository-wide map of public techniques.

## Canonical techniques

| id | name | domain | status | summary |
|---|---|---|---|---|
| AOA-T-0001 | plan-diff-apply-verify-report | agent-workflows | canonical | Safe workflow for agent-driven changes using explicit planning, scoped diffs, explicit validation, and concise reporting. |
| AOA-T-0002 | source-of-truth-layout | docs | canonical | Repository document role separation pattern that keeps status, plans, history, decisions, and run instructions in distinct canonical homes. |

## Promoted techniques

| id | name | domain | status | summary |
|---|---|---|---|---|
| AOA-T-0003 | contract-first-smoke-summary | evaluation | promoted | Runnable smoke pattern where each smoke path emits a machine-readable summary that becomes the primary validation contract. |
| AOA-T-0004 | intent-plan-dry-run-contract-chain | agent-workflows | promoted | Safe workflow that normalizes intent into a traceable plan, validates it with dry-run, and enforces contract checks before any real execution path exists. |
| AOA-T-0005 | new-intent-rollout-checklist | agent-workflows | promoted | Checklist for safely adding a new intent type to an intent-plan-dry-run chain without contract drift. |
| AOA-T-0006 | latest-alias-plus-history-copy | evaluation | promoted | Dual-write summary pattern that keeps a stable latest alias, preserves nested history, and prevents double-count accumulation. |
| AOA-T-0007 | signal-first-gate-promotion | evaluation | promoted | Staged pattern for promoting an observed validation signal into strict enforcement without losing diagnostics or widening the fail surface too early. |
| AOA-T-0008 | published-summary-remediation-snapshot | evaluation | promoted | Read-only aggregation pattern that turns latest published summaries into a bounded remediation snapshot without replaying history or changing runtime behavior. |
| AOA-T-0009 | lightweight-status-snapshot | docs | promoted | Keep top-level status documents short and link-driven, while routing detailed execution state and history to their canonical homes. |
| AOA-T-0010 | telemetry-integrity-snapshot | evaluation | promoted | Read-only integrity verdict that checks telemetry and summary-layout invariants across latest published summaries without widening the hard fail surface. |
| AOA-T-0011 | required-vs-optional-source-rendering | evaluation | promoted | Distinguish strict required sources from tolerant optional sources so operator-facing summary surfaces remain useful without hiding true hard failures. |
| AOA-T-0012 | deterministic-context-composition | docs | promoted | Compose agent context from smaller fragments into a stable generated artifact with deterministic ordering and source traceability. |

## Deprecated techniques

| id | name | replacement | note |
|---|---|---|---|
| - | - | - | - |

## Notes

- `canonical` means recommended by default.
- `promoted` means reusable and public-safe, but not yet the main default.
- `deprecated` means historically preserved, but no longer preferred.
