# Technique Selection

This file is generated from `../generated/technique_catalog.json` and the authoritative markdown frontmatter.
Do not edit it by hand; run `python scripts/build_catalog.py`.

Use this surface to make one bounded choice:
1. narrow by `domain` first
2. prefer `canonical` techniques for default use
3. use `validation_strength` as an evidence-breadth signal
4. use direct `relations` as adjacency hints, not graph traversal

See also:
- [Start Here](START_HERE.md)
- [Technique Selection Guide](TECHNIQUE_SELECTION_GUIDE.md)
- [TECHNIQUE_INDEX](../TECHNIQUE_INDEX.md)
- [CANONICAL_RUBRIC](CANONICAL_RUBRIC.md)
- [Full catalog JSON](../generated/technique_catalog.json)
- [Min catalog JSON](../generated/technique_catalog.min.json)

If you still need repo-level orientation before choosing a technique, open `START_HERE.md` first.

## Quick Questions

### I need an evaluation pattern. Where do I start?

| technique | validation | summary |
|---|---|---|
| [AOA-T-0003](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) | `source_backed` | Runnable smoke pattern where each smoke path emits a machine-readable summary that becomes the primary validation contract. |
| [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) | `cross_context` | Dual-write summary pattern that keeps a stable latest alias, preserves nested history, and prevents double-count accumulation. |
| [AOA-T-0007](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) | `source_backed` | Staged pattern for promoting an observed validation signal into strict enforcement without losing diagnostics or widening the fail surface too early. |
| [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) | `cross_context` | Read-only aggregation pattern that turns latest published summaries into a bounded remediation snapshot without replaying history or changing runtime behavior. |
| [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) | `cross_context` | Read-only integrity verdict that checks telemetry and summary-layout invariants across latest published summaries without widening the hard fail surface. |
| [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) | `cross_context` | Distinguish strict required sources from tolerant optional sources so operator-facing summary surfaces remain useful without hiding true hard failures. |
| [AOA-T-0015](../techniques/evaluation/contract-test-design/TECHNIQUE.md) | `cross_context` | Make a boundary explicit by defining expected inputs, outputs, and verification around the contract rather than around hidden internals. |
| [AOA-T-0017](../techniques/evaluation/property-invariants/TECHNIQUE.md) | `cross_context` | Express stable system or domain truths as invariant-oriented tests or checks so broad behavior is constrained beyond a small handpicked example set. |

### What are the current canonical defaults by domain?

| domain | canonical defaults |
|---|---|
| `agent-workflows` | [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md), [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md), [AOA-T-0014](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) |
| `docs` | [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md), [AOA-T-0009](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md), [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md), [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md), [AOA-T-0016](../techniques/docs/bounded-context-map/TECHNIQUE.md), [AOA-T-0018](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md), [AOA-T-0019](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md), [AOA-T-0021](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md), [AOA-T-0034](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md) |
| `evaluation` | [AOA-T-0003](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md), [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md), [AOA-T-0007](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md), [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md), [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md), [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md), [AOA-T-0015](../techniques/evaluation/contract-test-design/TECHNIQUE.md), [AOA-T-0017](../techniques/evaluation/property-invariants/TECHNIQUE.md) |
| `history` | - |

### If I choose one technique, what nearby techniques usually go with it?

- [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md): `complements` [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md), [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md)
- [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md): `complements` [AOA-T-0009](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md)
- [AOA-T-0003](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md): `used_together_for` [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md), [AOA-T-0007](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md)
- [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md): `complements` [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md); `used_together_for` [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md)
- [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md): `requires` [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md); `complements` [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md)
- [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md): `requires` [AOA-T-0003](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md); `used_together_for` [AOA-T-0007](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md); `shares_contract_with` [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md), [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md)
- [AOA-T-0007](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md): `requires` [AOA-T-0003](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md), [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md)
- [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md): `requires` [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md); `complements` [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md), [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md)
- [AOA-T-0009](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md): `complements` [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md)
- [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md): `requires` [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md); `complements` [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md), [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md)
- [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md): `complements` [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md), [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md)
- [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md): none
- [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md): `complements` [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md)
- [AOA-T-0014](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md): `complements` [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md)
- [AOA-T-0015](../techniques/evaluation/contract-test-design/TECHNIQUE.md): `complements` [AOA-T-0003](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md), [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md)
- [AOA-T-0016](../techniques/docs/bounded-context-map/TECHNIQUE.md): `complements` [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md), [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md)
- [AOA-T-0017](../techniques/evaluation/property-invariants/TECHNIQUE.md): `complements` [AOA-T-0007](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md), [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md)
- [AOA-T-0018](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md): `complements` [AOA-T-0019](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md)
- [AOA-T-0019](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md): `complements` [AOA-T-0018](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md); `used_together_for` [AOA-T-0020](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md), [AOA-T-0021](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md)
- [AOA-T-0020](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md): `requires` [AOA-T-0019](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md)
- [AOA-T-0021](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md): `requires` [AOA-T-0019](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md)
- [AOA-T-0022](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md): `complements` [AOA-T-0018](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md)
- [AOA-T-0023](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md): `complements` [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md)
- [AOA-T-0024](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md): `complements` [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md)
- [AOA-T-0025](../techniques/docs/capability-spec-versioning/TECHNIQUE.md): `complements` [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md)
- [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md): `complements` [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md)
- [AOA-T-0027](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md): `complements` [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md)
- [AOA-T-0028](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md): `complements` [AOA-T-0023](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md)
- [AOA-T-0029](../techniques/docs/nested-rule-loading/TECHNIQUE.md): `complements` [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md)
- [AOA-T-0030](../techniques/docs/fragmented-agent-context/TECHNIQUE.md): `complements` [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md)
- [AOA-T-0031](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md): `complements` [AOA-T-0023](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md)
- [AOA-T-0032](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md): `complements` [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md)
- [AOA-T-0033](../techniques/docs/decision-rationale-recording/TECHNIQUE.md): none
- [AOA-T-0034](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md): none
- [AOA-T-0035](../techniques/docs/profile-preset-composition/TECHNIQUE.md): `complements` [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md)
- [AOA-T-0036](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md): `complements` [AOA-T-0035](../techniques/docs/profile-preset-composition/TECHNIQUE.md)
- [AOA-T-0037](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md): `complements` [AOA-T-0036](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md)
- [AOA-T-0038](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md): `complements` [AOA-T-0036](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md), [AOA-T-0037](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md)
- [AOA-T-0039](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md): `complements` [AOA-T-0035](../techniques/docs/profile-preset-composition/TECHNIQUE.md)
- [AOA-T-0040](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md): `complements` [AOA-T-0027](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md)
- [AOA-T-0041](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md): `complements` [AOA-T-0024](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md)
- [AOA-T-0042](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md): `complements` [AOA-T-0041](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md)
- [AOA-T-0043](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md): `complements` [AOA-T-0020](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md), [AOA-T-0021](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md)
- [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md): `complements` [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md)
- [AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md): `complements` [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md), [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md)
- [AOA-T-0046](../techniques/docs/repo-doc-surface-lift/TECHNIQUE.md): `complements` [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md), [AOA-T-0009](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md)
- [AOA-T-0047](../techniques/docs/github-review-template-lift/TECHNIQUE.md): `complements` [AOA-T-0019](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md)
- [AOA-T-0048](../techniques/docs/semantic-review-surface-lift/TECHNIQUE.md): `complements` [AOA-T-0018](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md)

## Browse By Domain

### `agent-workflows`

| technique | status | validation | rigor | summary |
|---|---|---|---|---|
| [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) | `canonical` | `cross_context` | `bounded` | Safe workflow for agent-driven changes using explicit planning, scoped diffs, explicit validation, and concise reporting. |
| [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) | `canonical` | `cross_context` | `strict` | Safe workflow that normalizes intent into a traceable plan, validates it with dry-run, and enforces contract checks before any real execution path exists. |
| [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) | `promoted` | `source_backed` | `bounded` | Checklist for safely adding a new intent type to an intent-plan-dry-run chain without contract drift. |
| [AOA-T-0014](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) | `canonical` | `cross_context` | `bounded` | Implement a bounded behavior slice through test-first discipline, minimal implementation, and explicit refactor limits. |
| [AOA-T-0023](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) | `promoted` | `source_backed` | `bounded` | Keep shell-side agent work mostly stateless and bounded to one confirmed step per invocation so runs stay composable, reviewable, and low-memory by default. |
| [AOA-T-0028](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) | `promoted` | `source_backed` | `bounded` | Require one explicit confirmation seam before a read or plan flow crosses into a mutating action so the action stays reviewable without widening into a multi-step autonomous loop. |
| [AOA-T-0031](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) | `promoted` | `source_backed` | `bounded` | Make agent runs composable as shell-side one-shot tools through explicit stdin, stdout, files, and pipes without widening into generic shell advice or autonomous loops. |
| [AOA-T-0036](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md) | `promoted` | `source_backed` | `bounded` | Render the actual composed runtime truth before startup so operators review the effective service and config view instead of relying only on declared profiles. |
| [AOA-T-0038](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) | `promoted` | `source_backed` | `bounded` | Start and stop a bounded local service stack through one explicit lifecycle entrypoint so prerequisite checks, visible runtime status, and clean shutdown stay reviewable without widening into generic launcher or platform doctrine. |

### `docs`

| technique | status | validation | rigor | summary |
|---|---|---|---|---|
| [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) | `canonical` | `cross_context` | `bounded` | Repository document role separation pattern that keeps status, plans, history, decisions, and run instructions in distinct canonical homes. |
| [AOA-T-0009](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) | `canonical` | `cross_context` | `light` | Keep top-level status documents short and link-driven, while routing detailed execution state and history to their canonical homes. |
| [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) | `canonical` | `cross_context` | `bounded` | Compose agent context from smaller fragments into a stable generated artifact with deterministic ordering and source traceability. |
| [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) | `canonical` | `cross_context` | `bounded` | Keep one canonical rule source and distribute it to multiple agent-facing instruction surfaces without turning each target into a hand-maintained source of truth. |
| [AOA-T-0016](../techniques/docs/bounded-context-map/TECHNIQUE.md) | `canonical` | `cross_context` | `bounded` | Reduce semantic drift by naming bounded contexts, separating responsibilities, and making handoff interfaces visible for docs and scoping work. |
| [AOA-T-0018](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) | `canonical` | `cross_context` | `bounded` | Lift stable technique markdown sections into derived section-level units while keeping the bundle markdown authoritative. |
| [AOA-T-0019](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) | `canonical` | `cross_context` | `bounded` | Treat bounded frontmatter and derived catalog outputs as a metadata spine for bundle routing without replacing markdown meaning or growing schema past current needs. |
| [AOA-T-0020](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) | `promoted` | `source_backed` | `bounded` | Use typed evidence note kinds and note paths as bounded provenance handles in derived manifests without flattening them into a note graph. |
| [AOA-T-0021](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) | `canonical` | `cross_context` | `bounded` | Lift small typed direct relations into bounded edge hints for derived consumers without turning them into graph semantics. |
| [AOA-T-0022](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) | `promoted` | `source_backed` | `bounded` | Lift richer `Risks` language into bounded caution-oriented lookup and reuse without turning caution into metadata, scoring, or generated policy. |
| [AOA-T-0024](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) | `promoted` | `source_backed` | `bounded` | Mirror upstream-owned content into a curated local collection through an explicit source manifest and preserved provenance so the local copy stays reviewable without pretending to be the canonical source. |
| [AOA-T-0025](../techniques/docs/capability-spec-versioning/TECHNIQUE.md) | `promoted` | `source_backed` | `bounded` | Keep agent-facing capability contracts in a versioned, reviewable spec so capability changes stay explicit and reusable without turning the spec into routing or registry policy. |
| [AOA-T-0027](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) | `promoted` | `source_backed` | `bounded` | Keep one canonical skill or rule source and propagate it to multiple agent-facing targets without turning each target into a hand-maintained source of truth. |
| [AOA-T-0029](../techniques/docs/nested-rule-loading/TECHNIQUE.md) | `promoted` | `source_backed` | `bounded` | Load hierarchical rule layers with explicit precedence so nested additions stay subordinate to one canonical source of ownership. |
| [AOA-T-0030](../techniques/docs/fragmented-agent-context/TECHNIQUE.md) | `promoted` | `source_backed` | `bounded` | Keep agent context in bounded fragments before deterministic assembly so modular authoring stays reviewable without collapsing into the final generated artifact. |
| [AOA-T-0033](../techniques/docs/decision-rationale-recording/TECHNIQUE.md) | `promoted` | `source_backed` | `bounded` | Keep one meaningful decision in a reviewable note with context, options, rationale, and consequences while staying out of source-of-truth governance and architecture taxonomy. |
| [AOA-T-0034](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md) | `canonical` | `cross_context` | `bounded` | Turn sensitive technical material into a shareable artifact by removing, redacting, or generalizing details while preserving the lesson and staying distinct from approval gating or execution planning. |
| [AOA-T-0035](../techniques/docs/profile-preset-composition/TECHNIQUE.md) | `promoted` | `source_backed` | `bounded` | Compose small reusable profiles into named presets so runtime posture stays reviewable without flattening composition into one opaque config or launcher doctrine. |
| [AOA-T-0040](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md) | `promoted` | `source_backed` | `bounded` | Separate reusable skill meaning from user-facing command invocation so shared capability stays portable without collapsing into slash-command syntax or command-specific workflow policy. |
| [AOA-T-0041](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) | `promoted` | `source_backed` | `bounded` | Curate a local discoverability layer over upstream-owned skill sources so selection stays editorial and reviewable without pretending the catalog owns sync, capability meaning, or registry policy. |
| [AOA-T-0043](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md) | `promoted` | `source_backed` | `bounded` | Mark primary versus supporting source inputs explicitly when bridging multiple source surfaces so downstream readers and synthesis keep provenance priority visible without turning the bridge into graph semantics or ranking doctrine. |
| [AOA-T-0046](../techniques/docs/repo-doc-surface-lift/TECHNIQUE.md) | `promoted` | `source_backed` | `bounded` | Lift one bounded set of authoritative repo docs and status files into derived routing knowledge without replacing the authored docs or widening into a docs taxonomy. |
| [AOA-T-0047](../techniques/docs/github-review-template-lift/TECHNIQUE.md) | `promoted` | `source_backed` | `bounded` | Lift authored GitHub issue and pull-request review templates into derived intake knowledge without turning templates into workflow automation or policy scoring. |
| [AOA-T-0048](../techniques/docs/semantic-review-surface-lift/TECHNIQUE.md) | `promoted` | `source_backed` | `bounded` | Lift authored semantic-review docs into derived boundary-review knowledge without creating automatic semantic verdicts. |

### `evaluation`

| technique | status | validation | rigor | summary |
|---|---|---|---|---|
| [AOA-T-0003](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) | `canonical` | `source_backed` | `strict` | Runnable smoke pattern where each smoke path emits a machine-readable summary that becomes the primary validation contract. |
| [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) | `canonical` | `cross_context` | `strict` | Dual-write summary pattern that keeps a stable latest alias, preserves nested history, and prevents double-count accumulation. |
| [AOA-T-0007](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) | `canonical` | `source_backed` | `strict` | Staged pattern for promoting an observed validation signal into strict enforcement without losing diagnostics or widening the fail surface too early. |
| [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) | `canonical` | `cross_context` | `bounded` | Read-only aggregation pattern that turns latest published summaries into a bounded remediation snapshot without replaying history or changing runtime behavior. |
| [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) | `canonical` | `cross_context` | `bounded` | Read-only integrity verdict that checks telemetry and summary-layout invariants across latest published summaries without widening the hard fail surface. |
| [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) | `canonical` | `cross_context` | `strict` | Distinguish strict required sources from tolerant optional sources so operator-facing summary surfaces remain useful without hiding true hard failures. |
| [AOA-T-0015](../techniques/evaluation/contract-test-design/TECHNIQUE.md) | `canonical` | `cross_context` | `bounded` | Make a boundary explicit by defining expected inputs, outputs, and verification around the contract rather than around hidden internals. |
| [AOA-T-0017](../techniques/evaluation/property-invariants/TECHNIQUE.md) | `canonical` | `cross_context` | `bounded` | Express stable system or domain truths as invariant-oriented tests or checks so broad behavior is constrained beyond a small handpicked example set. |
| [AOA-T-0032](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md) | `promoted` | `source_backed` | `bounded` | Emit CI-facing reports for context composition, source coverage, token-estimate drift, and related composition checks without turning the report surface into the composition technique itself. |
| [AOA-T-0037](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md) | `promoted` | `source_backed` | `bounded` | Run selector-aware host-readiness checks before startup so environment drift becomes visible for the chosen runtime without widening into generic monitoring or lifecycle control. |
| [AOA-T-0039](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) | `promoted` | `source_backed` | `bounded` | Benchmark one stable baseline profile first, then compare additive profiles against the same measurement surface and artifact shape so richer profiles stay additive and off the default path. |
| [AOA-T-0042](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md) | `promoted` | `source_backed` | `bounded` | Check upstream-owned skill sources for availability and manifest-readiness before surfacing them as selectable inputs so broken entries stay visible and reviewable without widening into generic monitoring, registry governance, or security doctrine. |

### `history`

| technique | status | validation | rigor | summary |
|---|---|---|---|---|
| [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) | `promoted` | `source_backed` | `bounded` | Capture AI coding sessions as versioned repo artifacts so project history stays searchable, reviewable, and reusable without turning session logs into memory or instruction policy. |
| [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) | `promoted` | `source_backed` | `bounded` | Package already-saved AI session transcripts as readable, versionable Markdown artifacts so review, handoff, and selective sharing stay possible without reopening capture semantics or turning transcript history into memory or instruction authority. |
| [AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) | `promoted` | `source_backed` | `bounded` | Preserve a bounded witness trace as a reviewable artifact with step visibility, state-delta notes, and human-readable summary so a nontrivial run can be inspected before any writeback or promotion without creating a new memory-object kind. |

## Current Catalog Audit

- `export_ready` is currently `true` for 48/48 techniques.
- For the current corpus, that uniform `true` is intentional: every tracked bundle is considered safe for Stage 1 catalog publication.
- Treat `export_ready` as the current Stage 1 catalog-publication safety floor, not as a meaningful selector yet.
- A future `export_ready: false` should mean one bounded thing only: the markdown bundle may still exist, but structured catalog publication would currently overstate its safety, trustworthiness, or stability.
