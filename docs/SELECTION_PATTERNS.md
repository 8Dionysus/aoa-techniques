# Selection Patterns

This file is generated from `../generated/technique_catalog.json`, current direct `relations`, validator-backed navigation specs, and review-backed working sets.
Do not edit it by hand; run `python scripts/build_catalog.py`.

Use this surface when the flat adjacency list in `TECHNIQUE_SELECTION.md` is not enough and you want one bounded answer to:
- "What nearby technique should I inspect next, and why?"

This surface uses direct relation navigation, validator-backed starting points and common moves, and review-backed clusters only. It does not do graph search, scoring, or multi-hop reasoning.

See also:
- [Technique Selection](TECHNIQUE_SELECTION.md)
- [TECHNIQUE_INDEX](../TECHNIQUE_INDEX.md)
- [Full catalog JSON](../generated/technique_catalog.json)

## Starting Points

| domain | canonical defaults | start here |
|---|---|---|
| `agent-workflows` | [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md), [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md), [AOA-T-0014](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) | Start with the canonical workflow contract, then add narrower chain helpers only when the path gets more specialized. |
| `docs` | [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md), [AOA-T-0009](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md), [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md), [AOA-T-0016](../techniques/docs/bounded-context-map/TECHNIQUE.md), [AOA-T-0019](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md), [AOA-T-0021](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) | Start with the canonical document-role layout, then inspect the docs boundary pair or instruction-surface pair when generation and entrypoint discipline become the next bounded question. |
| `evaluation` | [AOA-T-0003](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md), [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md), [AOA-T-0007](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md), [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md), [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md), [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md), [AOA-T-0015](../techniques/evaluation/contract-test-design/TECHNIQUE.md), [AOA-T-0017](../techniques/evaluation/property-invariants/TECHNIQUE.md) | Start with the canonical summary/storage backbone, then move into remediation, integrity, or rendering policy as downstream needs appear. |

## Working Sets

### Published-summary cluster

- Techniques: [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md), [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md), [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md), [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md)
- Review: [PUBLISHED_SUMMARY_SEMANTIC_REVIEW.md](PUBLISHED_SUMMARY_SEMANTIC_REVIEW.md)
- Why grouped: Storage, remediation, integrity, and rendering policy for published summary systems.

### Evaluation-chain pair

- Techniques: [AOA-T-0003](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md), [AOA-T-0007](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md)
- Review: [EVALUATION_CHAIN_SEMANTIC_REVIEW.md](EVALUATION_CHAIN_SEMANTIC_REVIEW.md)
- Why grouped: Summary-contract production plus staged promotion from observation to narrow enforcement.

### Docs boundary pair

- Techniques: [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md), [AOA-T-0009](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md)
- Review: [DOCS_BOUNDARY_SEMANTIC_REVIEW.md](DOCS_BOUNDARY_SEMANTIC_REVIEW.md)
- Why grouped: Repository-wide document-role layout plus lightweight entrypoint snapshot discipline.

### Intent-chain pair

- Techniques: [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md), [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md)
- Review: [INTENT_CHAIN_SEMANTIC_REVIEW.md](INTENT_CHAIN_SEMANTIC_REVIEW.md)
- Why grouped: Artifact-first intent normalization and dry-run contract validation plus safe rollout of one new intent type on top of that chain.

### Instruction-surface pair

- Techniques: [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md), [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md)
- Review: [INSTRUCTION_SURFACE_SEMANTIC_REVIEW.md](INSTRUCTION_SURFACE_SEMANTIC_REVIEW.md)
- Why grouped: Fragment-first composition into one generated context artifact plus single-source distribution to multiple agent-facing instruction surfaces.

### Skill-support cluster

- Techniques: [AOA-T-0014](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md), [AOA-T-0015](../techniques/evaluation/contract-test-design/TECHNIQUE.md), [AOA-T-0017](../techniques/evaluation/property-invariants/TECHNIQUE.md), [AOA-T-0016](../techniques/docs/bounded-context-map/TECHNIQUE.md)
- Review: [SKILL_SUPPORT_SEMANTIC_REVIEW.md](SKILL_SUPPORT_SEMANTIC_REVIEW.md)
- Why grouped: Bounded test-first slicing, contract-surface validation, invariant coverage broadening, and semantic scoping for recent skill-support techniques.

### KAG/source-lift family

- Techniques: [AOA-T-0018](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md), [AOA-T-0019](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md), [AOA-T-0020](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md), [AOA-T-0021](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md), [AOA-T-0022](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md)
- Review: [KAG_SOURCE_LIFT_SEMANTIC_REVIEW.md](KAG_SOURCE_LIFT_SEMANTIC_REVIEW.md)
- Why grouped: Section lift, metadata spine, provenance lift, bounded relation lift, and markdown-first caution lift for the current reusable KAG/source-lift family.

## Common Moves

| situation | inspect next | why |
|---|---|---|
| I have a summary producer and need history/trend-safe storage | [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) | Natural next move after a stable summary contract such as `AOA-T-0003`. |
| I already publish summaries and need one remediation backlog | [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) | Use when several latest summaries should collapse into one bounded follow-up surface. |
| I already publish summaries and need one trust verdict | [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) | Use when several consumers should not duplicate integrity checks independently. |
| I need strict-vs-optional rendering policy | [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) | Use when supporting summaries should stay visible but non-fatal in one consumer. |
| I need doc-role separation | [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) | Start here when the repository needs explicit canonical homes and update-routing rules. |
| I need top-level docs to stay short | [AOA-T-0009](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) | Inspect alongside `AOA-T-0002` when entrypoint docs start duplicating operational detail. |

## Relation Notes

- `requires` means one technique usually depends on another contract already existing.
- `complements` means two techniques commonly strengthen each other without collapsing into one pattern.
- `used_together_for` means the pair commonly appears in the same operating path, even if one does not strictly depend on the other.
- `shares_contract_with` means neighboring techniques rely on the same bounded contract but still do different work.
- This surface uses direct relation hints only. It does not do graph traversal, ranking, or multi-hop inference.
