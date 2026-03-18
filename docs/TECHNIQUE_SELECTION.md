# Technique Selection

This file is generated from `../generated/technique_catalog.json` and the authoritative markdown frontmatter.
Do not edit it by hand; run `python scripts/build_catalog.py`.

Use this surface to make one bounded choice:
1. narrow by `domain` first
2. prefer `canonical` techniques for default use
3. use `validation_strength` as an evidence-breadth signal
4. use direct `relations` as adjacency hints, not graph traversal

See also:
- [Documentation Map](README.md)
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

### What are the current canonical defaults by domain?

| domain | canonical defaults |
|---|---|
| `agent-workflows` | [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) |
| `docs` | [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md), [AOA-T-0009](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) |
| `evaluation` | [AOA-T-0003](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md), [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md), [AOA-T-0007](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md), [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md), [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md), [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) |

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

## Browse By Domain

### `agent-workflows`

| technique | status | validation | rigor | summary |
|---|---|---|---|---|
| [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) | `canonical` | `cross_context` | `bounded` | Safe workflow for agent-driven changes using explicit planning, scoped diffs, explicit validation, and concise reporting. |
| [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) | `promoted` | `source_backed` | `strict` | Safe workflow that normalizes intent into a traceable plan, validates it with dry-run, and enforces contract checks before any real execution path exists. |
| [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) | `promoted` | `source_backed` | `bounded` | Checklist for safely adding a new intent type to an intent-plan-dry-run chain without contract drift. |

### `docs`

| technique | status | validation | rigor | summary |
|---|---|---|---|---|
| [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) | `canonical` | `cross_context` | `bounded` | Repository document role separation pattern that keeps status, plans, history, decisions, and run instructions in distinct canonical homes. |
| [AOA-T-0009](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) | `canonical` | `cross_context` | `light` | Keep top-level status documents short and link-driven, while routing detailed execution state and history to their canonical homes. |
| [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) | `promoted` | `cross_context` | `bounded` | Compose agent context from smaller fragments into a stable generated artifact with deterministic ordering and source traceability. |
| [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) | `promoted` | `cross_context` | `bounded` | Keep one canonical rule source and distribute it to multiple agent-facing instruction surfaces without turning each target into a hand-maintained source of truth. |

### `evaluation`

| technique | status | validation | rigor | summary |
|---|---|---|---|---|
| [AOA-T-0003](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) | `canonical` | `source_backed` | `strict` | Runnable smoke pattern where each smoke path emits a machine-readable summary that becomes the primary validation contract. |
| [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) | `canonical` | `cross_context` | `strict` | Dual-write summary pattern that keeps a stable latest alias, preserves nested history, and prevents double-count accumulation. |
| [AOA-T-0007](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) | `canonical` | `source_backed` | `strict` | Staged pattern for promoting an observed validation signal into strict enforcement without losing diagnostics or widening the fail surface too early. |
| [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) | `canonical` | `cross_context` | `bounded` | Read-only aggregation pattern that turns latest published summaries into a bounded remediation snapshot without replaying history or changing runtime behavior. |
| [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) | `canonical` | `cross_context` | `bounded` | Read-only integrity verdict that checks telemetry and summary-layout invariants across latest published summaries without widening the hard fail surface. |
| [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) | `canonical` | `cross_context` | `strict` | Distinguish strict required sources from tolerant optional sources so operator-facing summary surfaces remain useful without hiding true hard failures. |

## Current Catalog Audit

- `export_ready` is currently `true` for 13/13 techniques.
- For the current corpus, that uniform `true` is intentional: every tracked bundle is considered safe for Stage 1 catalog publication.
- Treat `export_ready` as the current Stage 1 catalog-publication safety floor, not as a meaningful selector yet.
- A future `export_ready: false` should mean one bounded thing only: the markdown bundle may still exist, but structured catalog publication would currently overstate its safety, trustworthiness, or stability.
