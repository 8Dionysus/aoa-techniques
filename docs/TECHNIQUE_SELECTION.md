# Technique Selection

This file is generated from `../generated/technique_catalog.json` and the authoritative markdown frontmatter.
Do not edit it by hand; run `python scripts/build_catalog.py`.

Use this surface to make one bounded choice:
1. narrow by `domain` first
2. prefer `canonical` techniques for default use
3. use `validation_strength` as an evidence-breadth signal
4. use direct `relations` as adjacency hints, not graph traversal

See also:
- [TECHNIQUE_INDEX](../TECHNIQUE_INDEX.md)
- [CANONICAL_RUBRIC](CANONICAL_RUBRIC.md)
- [Full catalog JSON](../generated/technique_catalog.json)
- [Min catalog JSON](../generated/technique_catalog.min.json)

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

### What are the current canonical defaults by domain?

| domain | canonical defaults |
|---|---|
| `agent-workflows` | [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md), [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md), [AOA-T-0014](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) |
| `docs` | [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md), [AOA-T-0009](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md), [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md), [AOA-T-0016](../techniques/docs/bounded-context-map/TECHNIQUE.md), [AOA-T-0019](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) |
| `evaluation` | [AOA-T-0003](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md), [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md), [AOA-T-0007](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md), [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md), [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md), [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md), [AOA-T-0015](../techniques/evaluation/contract-test-design/TECHNIQUE.md) |

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

## Browse By Domain

### `agent-workflows`

| technique | status | validation | rigor | summary |
|---|---|---|---|---|
| [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) | `canonical` | `cross_context` | `bounded` | Safe workflow for agent-driven changes using explicit planning, scoped diffs, explicit validation, and concise reporting. |
| [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) | `canonical` | `cross_context` | `strict` | Safe workflow that normalizes intent into a traceable plan, validates it with dry-run, and enforces contract checks before any real execution path exists. |
| [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) | `promoted` | `source_backed` | `bounded` | Checklist for safely adding a new intent type to an intent-plan-dry-run chain without contract drift. |
| [AOA-T-0014](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) | `canonical` | `cross_context` | `bounded` | Implement a bounded behavior slice through test-first discipline, minimal implementation, and explicit refactor limits. |

### `docs`

| technique | status | validation | rigor | summary |
|---|---|---|---|---|
| [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) | `canonical` | `cross_context` | `bounded` | Repository document role separation pattern that keeps status, plans, history, decisions, and run instructions in distinct canonical homes. |
| [AOA-T-0009](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) | `canonical` | `cross_context` | `light` | Keep top-level status documents short and link-driven, while routing detailed execution state and history to their canonical homes. |
| [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) | `canonical` | `cross_context` | `bounded` | Compose agent context from smaller fragments into a stable generated artifact with deterministic ordering and source traceability. |
| [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) | `promoted` | `cross_context` | `bounded` | Keep one canonical rule source and distribute it to multiple agent-facing instruction surfaces without turning each target into a hand-maintained source of truth. |
| [AOA-T-0016](../techniques/docs/bounded-context-map/TECHNIQUE.md) | `canonical` | `cross_context` | `bounded` | Reduce semantic drift by naming bounded contexts, separating responsibilities, and making handoff interfaces visible for docs and scoping work. |
| [AOA-T-0018](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) | `promoted` | `source_backed` | `bounded` | Lift stable technique markdown sections into derived section-level units while keeping the bundle markdown authoritative. |
| [AOA-T-0019](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) | `canonical` | `cross_context` | `bounded` | Treat bounded frontmatter and derived catalog outputs as a metadata spine for bundle routing without replacing markdown meaning or growing schema past current needs. |
| [AOA-T-0020](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) | `promoted` | `source_backed` | `bounded` | Use typed evidence note kinds and note paths as bounded provenance handles in derived manifests without flattening them into a note graph. |
| [AOA-T-0021](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) | `promoted` | `source_backed` | `bounded` | Lift small typed direct relations into bounded edge hints for derived consumers without turning them into graph semantics. |
| [AOA-T-0022](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) | `promoted` | `source_backed` | `bounded` | Lift richer `Risks` language into bounded caution-oriented lookup and reuse without turning caution into metadata, scoring, or generated policy. |

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
| [AOA-T-0017](../techniques/evaluation/property-invariants/TECHNIQUE.md) | `promoted` | `source_backed` | `bounded` | Express stable system or domain truths as invariant-oriented tests or checks so broad behavior is constrained beyond a small handpicked example set. |

## Current Catalog Audit

- `export_ready` is currently `true` for 22/22 techniques.
- For the current corpus, that uniform `true` is intentional: every tracked bundle is considered safe for Stage 1 catalog publication.
- Treat `export_ready` as the current Stage 1 catalog-publication safety floor, not as a meaningful selector yet.
- A future `export_ready: false` should mean one bounded thing only: the markdown bundle may still exist, but structured catalog publication would currently overstate its safety, trustworthiness, or stability.
