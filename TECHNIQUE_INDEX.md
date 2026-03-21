# TECHNIQUE_INDEX

This file is the repository-wide map of public techniques.

## Canonical techniques

| id | name | domain | status | summary |
|---|---|---|---|---|
| AOA-T-0001 | plan-diff-apply-verify-report | agent-workflows | canonical | Safe workflow for agent-driven changes using explicit planning, scoped diffs, explicit validation, and concise reporting. |
| AOA-T-0004 | intent-plan-dry-run-contract-chain | agent-workflows | canonical | Safe workflow that normalizes intent into a traceable plan, validates it with dry-run, and enforces contract checks before any real execution path exists. |
| AOA-T-0014 | tdd-slice | agent-workflows | canonical | Implement a bounded behavior slice through test-first discipline, minimal implementation, and explicit refactor limits. |
| AOA-T-0002 | source-of-truth-layout | docs | canonical | Repository document role separation pattern that keeps status, plans, history, decisions, and run instructions in distinct canonical homes. |
| AOA-T-0009 | lightweight-status-snapshot | docs | canonical | Keep top-level status documents short and link-driven, while routing detailed execution state and history to their canonical homes. |
| AOA-T-0012 | deterministic-context-composition | docs | canonical | Compose agent context from smaller fragments into a stable generated artifact with deterministic ordering and source traceability. |
| AOA-T-0003 | contract-first-smoke-summary | evaluation | canonical | Runnable smoke pattern where each smoke path emits a machine-readable summary that becomes the primary validation contract. |
| AOA-T-0006 | latest-alias-plus-history-copy | evaluation | canonical | Dual-write summary pattern that keeps a stable latest alias, preserves nested history, and prevents double-count accumulation. |
| AOA-T-0007 | signal-first-gate-promotion | evaluation | canonical | Staged pattern for promoting an observed validation signal into strict enforcement without losing diagnostics or widening the fail surface too early. |
| AOA-T-0008 | published-summary-remediation-snapshot | evaluation | canonical | Read-only aggregation pattern that turns latest published summaries into a bounded remediation snapshot without replaying history or changing runtime behavior. |
| AOA-T-0010 | telemetry-integrity-snapshot | evaluation | canonical | Read-only integrity verdict that checks telemetry and summary-layout invariants across latest published summaries without widening the hard fail surface. |
| AOA-T-0011 | required-vs-optional-source-rendering | evaluation | canonical | Distinguish strict required sources from tolerant optional sources so operator-facing summary surfaces remain useful without hiding true hard failures. |
| AOA-T-0015 | contract-test-design | evaluation | canonical | Make a boundary explicit by defining expected inputs, outputs, and verification around the contract rather than around hidden internals. |

## Promoted techniques

| id | name | domain | status | summary |
|---|---|---|---|---|
| AOA-T-0005 | new-intent-rollout-checklist | agent-workflows | promoted | Checklist for safely adding a new intent type to an intent-plan-dry-run chain without contract drift. |
| AOA-T-0013 | single-source-rule-distribution | docs | promoted | Keep one canonical rule source and distribute it to multiple agent-facing instruction surfaces without turning each target into a hand-maintained source of truth. |
| AOA-T-0016 | bounded-context-map | docs | promoted | Reduce semantic drift by naming bounded contexts, separating responsibilities, and making handoff interfaces visible for docs and scoping work. |
| AOA-T-0017 | property-invariants | evaluation | promoted | Express stable system or domain truths as invariant-oriented tests or checks so broad behavior is constrained beyond a small handpicked example set. |
| AOA-T-0018 | markdown-technique-section-lift | docs | promoted | Lift stable technique markdown sections into derived section-level units while keeping the bundle markdown authoritative. |
| AOA-T-0019 | frontmatter-metadata-spine | docs | promoted | Treat bounded frontmatter and derived catalog outputs as a metadata spine for bundle routing without replacing markdown meaning or growing schema past current needs. |
| AOA-T-0020 | evidence-note-provenance-lift | docs | promoted | Use typed evidence note kinds and note paths as bounded provenance handles in derived manifests without flattening them into a note graph. |
| AOA-T-0021 | bounded-relation-lift-for-kag | docs | promoted | Lift small typed direct relations into bounded edge hints for derived consumers without turning them into graph semantics. |
| AOA-T-0022 | risk-and-negative-effect-lift | docs | promoted | Lift richer `Risks` language into bounded caution-oriented lookup and reuse without turning caution into metadata, scoring, or generated policy. |

## Deprecated techniques

| id | name | replacement | note |
|---|---|---|---|
| - | - | - | - |

## Notes

- `canonical` means recommended by default.
- `promoted` means reusable and public-safe, but not yet the main default.
- `deprecated` means historically preserved, but no longer preferred.
