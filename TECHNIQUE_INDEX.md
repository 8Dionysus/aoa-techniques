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
| AOA-T-0016 | bounded-context-map | docs | canonical | Reduce semantic drift by naming bounded contexts, separating responsibilities, and making handoff interfaces visible for docs and scoping work. |
| AOA-T-0019 | frontmatter-metadata-spine | docs | canonical | Treat bounded frontmatter and derived catalog outputs as a metadata spine for bundle routing without replacing markdown meaning or growing schema past current needs. |
| AOA-T-0021 | bounded-relation-lift-for-kag | docs | canonical | Lift small typed direct relations into bounded edge hints for derived consumers without turning them into graph semantics. |
| AOA-T-0003 | contract-first-smoke-summary | evaluation | canonical | Runnable smoke pattern where each smoke path emits a machine-readable summary that becomes the primary validation contract. |
| AOA-T-0006 | latest-alias-plus-history-copy | evaluation | canonical | Dual-write summary pattern that keeps a stable latest alias, preserves nested history, and prevents double-count accumulation. |
| AOA-T-0007 | signal-first-gate-promotion | evaluation | canonical | Staged pattern for promoting an observed validation signal into strict enforcement without losing diagnostics or widening the fail surface too early. |
| AOA-T-0008 | published-summary-remediation-snapshot | evaluation | canonical | Read-only aggregation pattern that turns latest published summaries into a bounded remediation snapshot without replaying history or changing runtime behavior. |
| AOA-T-0010 | telemetry-integrity-snapshot | evaluation | canonical | Read-only integrity verdict that checks telemetry and summary-layout invariants across latest published summaries without widening the hard fail surface. |
| AOA-T-0011 | required-vs-optional-source-rendering | evaluation | canonical | Distinguish strict required sources from tolerant optional sources so operator-facing summary surfaces remain useful without hiding true hard failures. |
| AOA-T-0015 | contract-test-design | evaluation | canonical | Make a boundary explicit by defining expected inputs, outputs, and verification around the contract rather than around hidden internals. |
| AOA-T-0017 | property-invariants | evaluation | canonical | Express stable system or domain truths as invariant-oriented tests or checks so broad behavior is constrained beyond a small handpicked example set. |

## Promoted techniques

| id | name | domain | status | summary |
|---|---|---|---|---|
| AOA-T-0005 | new-intent-rollout-checklist | agent-workflows | promoted | Checklist for safely adding a new intent type to an intent-plan-dry-run chain without contract drift. |
| AOA-T-0023 | stateless-single-shot-agent | agent-workflows | promoted | Keep shell-side agent work mostly stateless and bounded to one confirmed step per invocation so runs stay composable, reviewable, and low-memory by default. |
| AOA-T-0028 | confirmation-gated-mutating-action | agent-workflows | promoted | Require one explicit confirmation seam before a read or plan flow crosses into a mutating action so the action stays reviewable without widening into a multi-step autonomous loop. |
| AOA-T-0031 | shell-composable-agent-invocation | agent-workflows | promoted | Make agent runs composable as shell-side one-shot tools through explicit stdin, stdout, files, and pipes without widening into generic shell advice or autonomous loops. |
| AOA-T-0036 | render-truth-before-startup | agent-workflows | promoted | Render the actual composed runtime truth before startup so operators review the effective service and config view instead of relying only on declared profiles. |
| AOA-T-0038 | one-command-service-lifecycle | agent-workflows | promoted | Start and stop a bounded local service stack through one explicit lifecycle entrypoint so prerequisite checks, visible runtime status, and clean shutdown stay reviewable without widening into generic launcher or platform doctrine. |
| AOA-T-0013 | single-source-rule-distribution | docs | promoted | Keep one canonical rule source and distribute it to multiple agent-facing instruction surfaces without turning each target into a hand-maintained source of truth. |
| AOA-T-0018 | markdown-technique-section-lift | docs | promoted | Lift stable technique markdown sections into derived section-level units while keeping the bundle markdown authoritative. |
| AOA-T-0020 | evidence-note-provenance-lift | docs | promoted | Use typed evidence note kinds and note paths as bounded provenance handles in derived manifests without flattening them into a note graph. |
| AOA-T-0022 | risk-and-negative-effect-lift | docs | promoted | Lift richer `Risks` language into bounded caution-oriented lookup and reuse without turning caution into metadata, scoring, or generated policy. |
| AOA-T-0027 | cross-agent-skill-propagation | docs | promoted | Keep one canonical skill or rule source and propagate it to multiple agent-facing targets without turning each target into a hand-maintained source of truth. |
| AOA-T-0024 | upstream-mirroring-with-provenance | docs | promoted | Mirror upstream-owned content into a curated local collection through an explicit source manifest and preserved provenance so the local copy stays reviewable without pretending to be the canonical source. |
| AOA-T-0025 | capability-spec-versioning | docs | promoted | Keep agent-facing capability contracts in a versioned, reviewable spec so capability changes stay explicit and reusable without turning the spec into routing or registry policy. |
| AOA-T-0029 | nested-rule-loading | docs | promoted | Load hierarchical rule layers with explicit precedence so nested additions stay subordinate to one canonical source of ownership. |
| AOA-T-0030 | fragmented-agent-context | docs | promoted | Keep agent context in bounded fragments before deterministic assembly so modular authoring stays reviewable without collapsing into the final generated artifact. |
| AOA-T-0033 | decision-rationale-recording | docs | promoted | Keep one meaningful decision in a reviewable note with context, options, rationale, and consequences while staying out of source-of-truth governance and architecture taxonomy. |
| AOA-T-0034 | public-safe-artifact-sanitization | docs | promoted | Turn sensitive technical material into a shareable artifact by removing, redacting, or generalizing details while preserving the lesson and staying distinct from approval gating or execution planning. |
| AOA-T-0035 | profile-preset-composition | docs | promoted | Compose small reusable profiles into named presets so runtime posture stays reviewable without flattening composition into one opaque config or launcher doctrine. |
| AOA-T-0040 | skill-vs-command-boundary | docs | promoted | Separate reusable skill meaning from user-facing command invocation so shared capability stays portable without collapsing into slash-command syntax or command-specific workflow policy. |
| AOA-T-0041 | skill-marketplace-curation | docs | promoted | Curate a local discoverability layer over upstream-owned skill sources so selection stays editorial and reviewable without pretending the catalog owns sync, capability meaning, or registry policy. |
| AOA-T-0043 | multi-source-primary-input-provenance | docs | promoted | Mark primary versus supporting source inputs explicitly when bridging multiple source surfaces so downstream readers and synthesis keep provenance priority visible without turning the bridge into graph semantics or ranking doctrine. |
| AOA-T-0032 | context-report-for-ci | evaluation | promoted | Emit CI-facing reports for context composition, source coverage, token-estimate drift, and related composition checks without turning the report surface into the composition technique itself. |
| AOA-T-0037 | contextual-host-doctor | evaluation | promoted | Run selector-aware host-readiness checks before startup so environment drift becomes visible for the chosen runtime without widening into generic monitoring or lifecycle control. |
| AOA-T-0039 | baseline-first-additive-profile-benchmarks | evaluation | promoted | Benchmark one stable baseline profile first, then compare additive profiles against the same measurement surface and artifact shape so richer profiles stay additive and off the default path. |
| AOA-T-0042 | upstream-skill-health-checking | evaluation | promoted | Check upstream-owned skill sources for availability and manifest-readiness before surfacing them as selectable inputs so broken entries stay visible and reviewable without widening into generic monitoring, registry governance, or security doctrine. |
| AOA-T-0026 | session-capture-as-repo-artifact | history | promoted | Capture AI coding sessions as versioned repo artifacts so project history stays searchable, reviewable, and reusable without turning session logs into memory or instruction policy. |
| AOA-T-0044 | versionable-session-transcripts | history | promoted | Package already-saved AI session transcripts as readable, versionable Markdown artifacts so review, handoff, and selective sharing stay possible without reopening capture semantics or turning transcript history into memory or instruction authority. |
| AOA-T-0045 | witness-trace-as-reviewable-artifact | history | promoted | Preserve a bounded witness trace as a reviewable artifact with step visibility, state-delta notes, and human-readable summary so a nontrivial run can be inspected before any writeback or promotion without creating a new memory-object kind. |

## Deprecated techniques

| id | name | replacement | note |
|---|---|---|---|
| - | - | - | - |

## Notes

- `canonical` means recommended by default.
- `promoted` means reusable and public-safe, but not yet the main default.
- `deprecated` means historically preserved, but no longer preferred.
