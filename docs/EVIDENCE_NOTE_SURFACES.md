# Evidence Note Surfaces

This file is generated from authoritative evidence-note markdown plus the current evidence note manifest payload.
Do not edit it by hand; run `python scripts/build_evidence_note_manifest.py`.

Use this surface when you need note-kind routing, note-shape awareness, or a bounded inventory of supporting note surfaces without flattening note prose into one reader layer.

This surface is note-scope first. It only exposes note kind, title, note path, note shape, owning technique, and bounded routing signals such as fixed section scopes or opaque-body handling. It does not flatten note prose, review arguments, or caution language into the reader.

See also:
- [Evidence Note Provenance Guide](EVIDENCE_NOTE_PROVENANCE_GUIDE.md)
- [Full evidence note manifest](../generated/technique_evidence_note_manifest.json)
- [Min evidence note manifest](../generated/technique_evidence_note_manifest.min.json)
- [Documentation Map](README.md)
- [KAG Source Lift Guide](KAG_SOURCE_LIFT_GUIDE.md)

## Note Scope

| note kind | title | note shape | routing signal | entries |
|---|---|---|---|---|
| `origin_evidence` | Origin Evidence | `typed_sections` | `4` fixed sections: `Technique`, `Source project`, `Evidence`, `Interpretation` | `18` |
| `second_context` | Second Context Adaptation | `typed_sections` | `7` fixed sections: `Technique`, `Target project`, `What changed`, `What stayed invariant`, `Risks introduced by adaptation`, `Evidence`, `Result` | `17` |
| `canonical_readiness` | Canonical Readiness | `typed_sections` | `7` fixed sections: `Technique`, `Verdict`, `Evidence summary`, `Default-use rationale`, `Fresh public-safety check`, `Remaining gaps`, `Recommendation` | `17` |
| `adverse_effects_review` | Adverse Effects Review | `typed_sections` | `8` fixed sections: `Technique`, `Review focus`, `Failure modes`, `Negative effects`, `Misuse patterns`, `Detection signals`, `Mitigations`, `Recommendation` | `13` |
| `external_origin` | External Origin Note | `typed_sections` | `4` fixed sections: `Source`, `What changed`, `Public-safety review`, `Review notes` | `2` |
| `external_review` | External Import Review | `typed_sections` | `8` fixed sections: `Technique`, `Verdict`, `Evidence summary`, `Boundedness check`, `Provenance readability`, `Import-path assessment`, `Remaining gaps`, `Recommendation` | `2` |
| `support_note` | Support Note | `opaque_body` | opaque note body only | `2` |

## `origin_evidence` - Origin Evidence

| title | note shape | routing signal | owning technique | note path | source |
|---|---|---|---|---|---|
| Origin Evidence | `typed_sections` | `4` typed sections | [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) | `techniques/agent-workflows/intent-plan-dry-run-contract-chain/notes/origin-evidence.md` | [Note](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/notes/origin-evidence.md) |
| Origin Evidence | `typed_sections` | `4` typed sections | [AOA-T-0014](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) | `techniques/agent-workflows/tdd-slice/notes/origin-evidence.md` | [Note](../techniques/agent-workflows/tdd-slice/notes/origin-evidence.md) |
| Origin Evidence | `typed_sections` | `4` typed sections | [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) | `techniques/agent-workflows/new-intent-rollout-checklist/notes/origin-evidence.md` | [Note](../techniques/agent-workflows/new-intent-rollout-checklist/notes/origin-evidence.md) |
| Origin Evidence | `typed_sections` | `4` typed sections | [AOA-T-0009](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) | `techniques/docs/lightweight-status-snapshot/notes/origin-evidence.md` | [Note](../techniques/docs/lightweight-status-snapshot/notes/origin-evidence.md) |
| Origin Evidence | `typed_sections` | `4` typed sections | [AOA-T-0016](../techniques/docs/bounded-context-map/TECHNIQUE.md) | `techniques/docs/bounded-context-map/notes/origin-evidence.md` | [Note](../techniques/docs/bounded-context-map/notes/origin-evidence.md) |
| Origin Evidence | `typed_sections` | `4` typed sections | [AOA-T-0018](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) | `techniques/docs/markdown-technique-section-lift/notes/origin-evidence.md` | [Note](../techniques/docs/markdown-technique-section-lift/notes/origin-evidence.md) |
| Origin Evidence | `typed_sections` | `4` typed sections | [AOA-T-0019](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) | `techniques/docs/frontmatter-metadata-spine/notes/origin-evidence.md` | [Note](../techniques/docs/frontmatter-metadata-spine/notes/origin-evidence.md) |
| Origin Evidence | `typed_sections` | `4` typed sections | [AOA-T-0020](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) | `techniques/docs/evidence-note-provenance-lift/notes/origin-evidence.md` | [Note](../techniques/docs/evidence-note-provenance-lift/notes/origin-evidence.md) |
| Origin Evidence | `typed_sections` | `4` typed sections | [AOA-T-0021](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) | `techniques/docs/bounded-relation-lift-for-kag/notes/origin-evidence.md` | [Note](../techniques/docs/bounded-relation-lift-for-kag/notes/origin-evidence.md) |
| Origin Evidence | `typed_sections` | `4` typed sections | [AOA-T-0022](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) | `techniques/docs/risk-and-negative-effect-lift/notes/origin-evidence.md` | [Note](../techniques/docs/risk-and-negative-effect-lift/notes/origin-evidence.md) |
| Origin Evidence | `typed_sections` | `4` typed sections | [AOA-T-0003](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) | `techniques/evaluation/contract-first-smoke-summary/notes/origin-evidence.md` | [Note](../techniques/evaluation/contract-first-smoke-summary/notes/origin-evidence.md) |
| Origin Evidence | `typed_sections` | `4` typed sections | [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) | `techniques/evaluation/latest-alias-plus-history-copy/notes/origin-evidence.md` | [Note](../techniques/evaluation/latest-alias-plus-history-copy/notes/origin-evidence.md) |
| Origin Evidence | `typed_sections` | `4` typed sections | [AOA-T-0007](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) | `techniques/evaluation/signal-first-gate-promotion/notes/origin-evidence.md` | [Note](../techniques/evaluation/signal-first-gate-promotion/notes/origin-evidence.md) |
| Origin Evidence | `typed_sections` | `4` typed sections | [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) | `techniques/evaluation/published-summary-remediation-snapshot/notes/origin-evidence.md` | [Note](../techniques/evaluation/published-summary-remediation-snapshot/notes/origin-evidence.md) |
| Origin Evidence | `typed_sections` | `4` typed sections | [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) | `techniques/evaluation/telemetry-integrity-snapshot/notes/origin-evidence.md` | [Note](../techniques/evaluation/telemetry-integrity-snapshot/notes/origin-evidence.md) |
| Origin Evidence | `typed_sections` | `4` typed sections | [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) | `techniques/evaluation/required-vs-optional-source-rendering/notes/origin-evidence.md` | [Note](../techniques/evaluation/required-vs-optional-source-rendering/notes/origin-evidence.md) |
| Origin Evidence | `typed_sections` | `4` typed sections | [AOA-T-0015](../techniques/evaluation/contract-test-design/TECHNIQUE.md) | `techniques/evaluation/contract-test-design/notes/origin-evidence.md` | [Note](../techniques/evaluation/contract-test-design/notes/origin-evidence.md) |
| Origin Evidence | `typed_sections` | `4` typed sections | [AOA-T-0017](../techniques/evaluation/property-invariants/TECHNIQUE.md) | `techniques/evaluation/property-invariants/notes/origin-evidence.md` | [Note](../techniques/evaluation/property-invariants/notes/origin-evidence.md) |

## `second_context` - Second Context Adaptation

| title | note shape | routing signal | owning technique | note path | source |
|---|---|---|---|---|---|
| Second Context Adaptation | `typed_sections` | `7` typed sections | [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) | `techniques/agent-workflows/plan-diff-apply-verify-report/notes/second-context-adaptation.md` | [Note](../techniques/agent-workflows/plan-diff-apply-verify-report/notes/second-context-adaptation.md) |
| Second Context Adaptation | `typed_sections` | `7` typed sections | [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) | `techniques/agent-workflows/intent-plan-dry-run-contract-chain/notes/second-context-adaptation.md` | [Note](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/notes/second-context-adaptation.md) |
| Second Context Adaptation | `typed_sections` | `7` typed sections | [AOA-T-0014](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) | `techniques/agent-workflows/tdd-slice/notes/second-context-adaptation.md` | [Note](../techniques/agent-workflows/tdd-slice/notes/second-context-adaptation.md) |
| Second Context Adaptation | `typed_sections` | `7` typed sections | [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) | `techniques/agent-workflows/new-intent-rollout-checklist/notes/second-context-adaptation.md` | [Note](../techniques/agent-workflows/new-intent-rollout-checklist/notes/second-context-adaptation.md) |
| Second Context Adaptation | `typed_sections` | `7` typed sections | [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) | `techniques/docs/source-of-truth-layout/notes/second-context-adaptation.md` | [Note](../techniques/docs/source-of-truth-layout/notes/second-context-adaptation.md) |
| Second Context Adaptation | `typed_sections` | `7` typed sections | [AOA-T-0009](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) | `techniques/docs/lightweight-status-snapshot/notes/second-context-adaptation.md` | [Note](../techniques/docs/lightweight-status-snapshot/notes/second-context-adaptation.md) |
| Second Context Adaptation | `typed_sections` | `7` typed sections | [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) | `techniques/docs/deterministic-context-composition/notes/second-context-adaptation.md` | [Note](../techniques/docs/deterministic-context-composition/notes/second-context-adaptation.md) |
| Second Context Adaptation | `typed_sections` | `7` typed sections | [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) | `techniques/docs/single-source-rule-distribution/notes/second-context-adaptation.md` | [Note](../techniques/docs/single-source-rule-distribution/notes/second-context-adaptation.md) |
| Second Context Adaptation | `typed_sections` | `7` typed sections | [AOA-T-0016](../techniques/docs/bounded-context-map/TECHNIQUE.md) | `techniques/docs/bounded-context-map/notes/second-context-adaptation.md` | [Note](../techniques/docs/bounded-context-map/notes/second-context-adaptation.md) |
| Second Context Adaptation | `typed_sections` | `7` typed sections | [AOA-T-0003](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) | `techniques/evaluation/contract-first-smoke-summary/notes/second-context-adaptation.md` | [Note](../techniques/evaluation/contract-first-smoke-summary/notes/second-context-adaptation.md) |
| Second Context Adaptation | `typed_sections` | `7` typed sections | [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) | `techniques/evaluation/latest-alias-plus-history-copy/notes/second-context-adaptation.md` | [Note](../techniques/evaluation/latest-alias-plus-history-copy/notes/second-context-adaptation.md) |
| Second Context Adaptation | `typed_sections` | `7` typed sections | [AOA-T-0007](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) | `techniques/evaluation/signal-first-gate-promotion/notes/second-context-adaptation.md` | [Note](../techniques/evaluation/signal-first-gate-promotion/notes/second-context-adaptation.md) |
| Second Context Adaptation | `typed_sections` | `7` typed sections | [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) | `techniques/evaluation/published-summary-remediation-snapshot/notes/second-context-adaptation.md` | [Note](../techniques/evaluation/published-summary-remediation-snapshot/notes/second-context-adaptation.md) |
| Second Context Adaptation | `typed_sections` | `7` typed sections | [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) | `techniques/evaluation/telemetry-integrity-snapshot/notes/second-context-adaptation.md` | [Note](../techniques/evaluation/telemetry-integrity-snapshot/notes/second-context-adaptation.md) |
| Second Context Adaptation | `typed_sections` | `7` typed sections | [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) | `techniques/evaluation/required-vs-optional-source-rendering/notes/second-context-adaptation.md` | [Note](../techniques/evaluation/required-vs-optional-source-rendering/notes/second-context-adaptation.md) |
| Second Context Adaptation | `typed_sections` | `7` typed sections | [AOA-T-0015](../techniques/evaluation/contract-test-design/TECHNIQUE.md) | `techniques/evaluation/contract-test-design/notes/second-context-adaptation.md` | [Note](../techniques/evaluation/contract-test-design/notes/second-context-adaptation.md) |
| Second Context Adaptation | `typed_sections` | `7` typed sections | [AOA-T-0017](../techniques/evaluation/property-invariants/TECHNIQUE.md) | `techniques/evaluation/property-invariants/notes/second-context-adaptation.md` | [Note](../techniques/evaluation/property-invariants/notes/second-context-adaptation.md) |

## `canonical_readiness` - Canonical Readiness

| title | note shape | routing signal | owning technique | note path | source |
|---|---|---|---|---|---|
| Canonical Readiness | `typed_sections` | `7` typed sections | [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) | `techniques/agent-workflows/plan-diff-apply-verify-report/notes/canonical-readiness.md` | [Note](../techniques/agent-workflows/plan-diff-apply-verify-report/notes/canonical-readiness.md) |
| Canonical Readiness | `typed_sections` | `7` typed sections | [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) | `techniques/agent-workflows/intent-plan-dry-run-contract-chain/notes/canonical-readiness.md` | [Note](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/notes/canonical-readiness.md) |
| Canonical Readiness | `typed_sections` | `7` typed sections | [AOA-T-0014](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) | `techniques/agent-workflows/tdd-slice/notes/canonical-readiness.md` | [Note](../techniques/agent-workflows/tdd-slice/notes/canonical-readiness.md) |
| Canonical Readiness | `typed_sections` | `7` typed sections | [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) | `techniques/agent-workflows/new-intent-rollout-checklist/notes/canonical-readiness.md` | [Note](../techniques/agent-workflows/new-intent-rollout-checklist/notes/canonical-readiness.md) |
| Canonical Readiness | `typed_sections` | `7` typed sections | [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) | `techniques/docs/source-of-truth-layout/notes/canonical-readiness.md` | [Note](../techniques/docs/source-of-truth-layout/notes/canonical-readiness.md) |
| Canonical Readiness | `typed_sections` | `7` typed sections | [AOA-T-0009](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) | `techniques/docs/lightweight-status-snapshot/notes/canonical-readiness.md` | [Note](../techniques/docs/lightweight-status-snapshot/notes/canonical-readiness.md) |
| Canonical Readiness | `typed_sections` | `7` typed sections | [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) | `techniques/docs/deterministic-context-composition/notes/canonical-readiness.md` | [Note](../techniques/docs/deterministic-context-composition/notes/canonical-readiness.md) |
| Canonical Readiness | `typed_sections` | `7` typed sections | [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) | `techniques/docs/single-source-rule-distribution/notes/canonical-readiness.md` | [Note](../techniques/docs/single-source-rule-distribution/notes/canonical-readiness.md) |
| Canonical Readiness | `typed_sections` | `7` typed sections | [AOA-T-0016](../techniques/docs/bounded-context-map/TECHNIQUE.md) | `techniques/docs/bounded-context-map/notes/canonical-readiness.md` | [Note](../techniques/docs/bounded-context-map/notes/canonical-readiness.md) |
| Canonical Readiness | `typed_sections` | `7` typed sections | [AOA-T-0003](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) | `techniques/evaluation/contract-first-smoke-summary/notes/canonical-readiness.md` | [Note](../techniques/evaluation/contract-first-smoke-summary/notes/canonical-readiness.md) |
| Canonical Readiness | `typed_sections` | `7` typed sections | [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) | `techniques/evaluation/latest-alias-plus-history-copy/notes/canonical-readiness.md` | [Note](../techniques/evaluation/latest-alias-plus-history-copy/notes/canonical-readiness.md) |
| Canonical Readiness | `typed_sections` | `7` typed sections | [AOA-T-0007](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) | `techniques/evaluation/signal-first-gate-promotion/notes/canonical-readiness.md` | [Note](../techniques/evaluation/signal-first-gate-promotion/notes/canonical-readiness.md) |
| Canonical Readiness | `typed_sections` | `7` typed sections | [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) | `techniques/evaluation/published-summary-remediation-snapshot/notes/canonical-readiness.md` | [Note](../techniques/evaluation/published-summary-remediation-snapshot/notes/canonical-readiness.md) |
| Canonical Readiness | `typed_sections` | `7` typed sections | [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) | `techniques/evaluation/telemetry-integrity-snapshot/notes/canonical-readiness.md` | [Note](../techniques/evaluation/telemetry-integrity-snapshot/notes/canonical-readiness.md) |
| Canonical Readiness | `typed_sections` | `7` typed sections | [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) | `techniques/evaluation/required-vs-optional-source-rendering/notes/canonical-readiness.md` | [Note](../techniques/evaluation/required-vs-optional-source-rendering/notes/canonical-readiness.md) |
| Canonical Readiness | `typed_sections` | `7` typed sections | [AOA-T-0015](../techniques/evaluation/contract-test-design/TECHNIQUE.md) | `techniques/evaluation/contract-test-design/notes/canonical-readiness.md` | [Note](../techniques/evaluation/contract-test-design/notes/canonical-readiness.md) |
| Canonical Readiness | `typed_sections` | `7` typed sections | [AOA-T-0017](../techniques/evaluation/property-invariants/TECHNIQUE.md) | `techniques/evaluation/property-invariants/notes/canonical-readiness.md` | [Note](../techniques/evaluation/property-invariants/notes/canonical-readiness.md) |

## `adverse_effects_review` - Adverse Effects Review

| title | note shape | routing signal | owning technique | note path | source |
|---|---|---|---|---|---|
| Adverse Effects Review | `typed_sections` | `8` typed sections | [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) | `techniques/agent-workflows/plan-diff-apply-verify-report/notes/adverse-effects-review.md` | [Note](../techniques/agent-workflows/plan-diff-apply-verify-report/notes/adverse-effects-review.md) |
| Adverse Effects Review | `typed_sections` | `8` typed sections | [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) | `techniques/agent-workflows/intent-plan-dry-run-contract-chain/notes/adverse-effects-review.md` | [Note](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/notes/adverse-effects-review.md) |
| Adverse Effects Review | `typed_sections` | `8` typed sections | [AOA-T-0014](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) | `techniques/agent-workflows/tdd-slice/notes/adverse-effects-review.md` | [Note](../techniques/agent-workflows/tdd-slice/notes/adverse-effects-review.md) |
| Adverse Effects Review | `typed_sections` | `8` typed sections | [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) | `techniques/docs/source-of-truth-layout/notes/adverse-effects-review.md` | [Note](../techniques/docs/source-of-truth-layout/notes/adverse-effects-review.md) |
| Adverse Effects Review | `typed_sections` | `8` typed sections | [AOA-T-0009](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) | `techniques/docs/lightweight-status-snapshot/notes/adverse-effects-review.md` | [Note](../techniques/docs/lightweight-status-snapshot/notes/adverse-effects-review.md) |
| Adverse Effects Review | `typed_sections` | `8` typed sections | [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) | `techniques/docs/deterministic-context-composition/notes/adverse-effects-review.md` | [Note](../techniques/docs/deterministic-context-composition/notes/adverse-effects-review.md) |
| Adverse Effects Review | `typed_sections` | `8` typed sections | [AOA-T-0003](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) | `techniques/evaluation/contract-first-smoke-summary/notes/adverse-effects-review.md` | [Note](../techniques/evaluation/contract-first-smoke-summary/notes/adverse-effects-review.md) |
| Adverse Effects Review | `typed_sections` | `8` typed sections | [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) | `techniques/evaluation/latest-alias-plus-history-copy/notes/adverse-effects-review.md` | [Note](../techniques/evaluation/latest-alias-plus-history-copy/notes/adverse-effects-review.md) |
| Adverse Effects Review | `typed_sections` | `8` typed sections | [AOA-T-0007](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) | `techniques/evaluation/signal-first-gate-promotion/notes/adverse-effects-review.md` | [Note](../techniques/evaluation/signal-first-gate-promotion/notes/adverse-effects-review.md) |
| Adverse Effects Review | `typed_sections` | `8` typed sections | [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) | `techniques/evaluation/published-summary-remediation-snapshot/notes/adverse-effects-review.md` | [Note](../techniques/evaluation/published-summary-remediation-snapshot/notes/adverse-effects-review.md) |
| Adverse Effects Review | `typed_sections` | `8` typed sections | [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) | `techniques/evaluation/telemetry-integrity-snapshot/notes/adverse-effects-review.md` | [Note](../techniques/evaluation/telemetry-integrity-snapshot/notes/adverse-effects-review.md) |
| Adverse Effects Review | `typed_sections` | `8` typed sections | [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) | `techniques/evaluation/required-vs-optional-source-rendering/notes/adverse-effects-review.md` | [Note](../techniques/evaluation/required-vs-optional-source-rendering/notes/adverse-effects-review.md) |
| Adverse Effects Review | `typed_sections` | `8` typed sections | [AOA-T-0015](../techniques/evaluation/contract-test-design/TECHNIQUE.md) | `techniques/evaluation/contract-test-design/notes/adverse-effects-review.md` | [Note](../techniques/evaluation/contract-test-design/notes/adverse-effects-review.md) |

## `external_origin` - External Origin Note

| title | note shape | routing signal | owning technique | note path | source |
|---|---|---|---|---|---|
| External Origin Note | `typed_sections` | `4` typed sections | [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) | `techniques/docs/deterministic-context-composition/notes/external-origin.md` | [Note](../techniques/docs/deterministic-context-composition/notes/external-origin.md) |
| External Origin Note | `typed_sections` | `4` typed sections | [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) | `techniques/docs/single-source-rule-distribution/notes/external-origin.md` | [Note](../techniques/docs/single-source-rule-distribution/notes/external-origin.md) |

## `external_review` - External Import Review

| title | note shape | routing signal | owning technique | note path | source |
|---|---|---|---|---|---|
| External Import Review | `typed_sections` | `8` typed sections | [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) | `techniques/docs/deterministic-context-composition/notes/external-import-review.md` | [Note](../techniques/docs/deterministic-context-composition/notes/external-import-review.md) |
| External Import Review | `typed_sections` | `8` typed sections | [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) | `techniques/docs/single-source-rule-distribution/notes/external-import-review.md` | [Note](../techniques/docs/single-source-rule-distribution/notes/external-import-review.md) |

## `support_note` - Support Note

| title | note shape | routing signal | owning technique | note path | source |
|---|---|---|---|---|---|
| Bounded Transfer | `opaque_body` | `body_markdown` only | [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) | `techniques/agent-workflows/intent-plan-dry-run-contract-chain/notes/bounded-transfer.md` | [Note](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/notes/bounded-transfer.md) |
| Rollout Failure Triage | `opaque_body` | `body_markdown` only | [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) | `techniques/agent-workflows/new-intent-rollout-checklist/notes/rollout-failure-triage.md` | [Note](../techniques/agent-workflows/new-intent-rollout-checklist/notes/rollout-failure-triage.md) |

## Boundaries

- The meaning remains in the authored note markdown.
- This surface is derived provenance and routing knowledge only.
- `adverse_effects_review` stays a typed note role, not generated caution policy or a machine-readable caution verdict engine.
- This surface does not flatten note prose, review arguments, or support-note bodies into one merged reader layer.
