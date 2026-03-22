# Technique Checklists

This file is generated from authoritative `TECHNIQUE.md` bundles plus the current checklist manifest payload.
Do not edit it by hand; run `python scripts/build_checklist_manifest.py`.

Use this surface when you want a bounded checklist inventory by domain and technique without opening each bundle first.

This surface stays domain-first and technique-first. It preserves checklist title, intro-presence, item count, check path, and source routing, including techniques that publish more than one checklist.

See also:
- [Technique Checklist Lift Guide](TECHNIQUE_CHECKLIST_LIFT_GUIDE.md)
- [Full checklist manifest](../generated/technique_checklist_manifest.json)
- [Min checklist manifest](../generated/technique_checklist_manifest.min.json)
- [Documentation Map](README.md)
- [KAG Source Lift Guide](KAG_SOURCE_LIFT_GUIDE.md)

## `agent-workflows`

### [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) - plan-diff-apply-verify-report (`canonical`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Review Checklist | `present` | `6` | `techniques/agent-workflows/plan-diff-apply-verify-report/checks/review-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) |

### [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) - intent-plan-dry-run-contract-chain (`canonical`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Chain Contract Checklist | `present` | `10` | `techniques/agent-workflows/intent-plan-dry-run-contract-chain/checks/chain-contract-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) |

### [AOA-T-0014](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) - tdd-slice (`canonical`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| TDD Slice Checklist | `present` | `8` | `techniques/agent-workflows/tdd-slice/checks/tdd-slice-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) |

### [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) - new-intent-rollout-checklist (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| intent-rollout-checklist | `absent` | `11` | `techniques/agent-workflows/new-intent-rollout-checklist/checks/intent-rollout-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) |

### [AOA-T-0023](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) - stateless-single-shot-agent (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Stateless Single-Shot Agent Checklist | `absent` | `7` | `techniques/agent-workflows/stateless-single-shot-agent/checks/stateless-single-shot-agent-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) |

### [AOA-T-0028](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) - confirmation-gated-mutating-action (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Confirmation Gated Mutating Action Checklist | `absent` | `6` | `techniques/agent-workflows/confirmation-gated-mutating-action/checks/confirmation-gated-mutating-action-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) |

### [AOA-T-0031](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) - shell-composable-agent-invocation (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Shell-Composable Agent Invocation Checklist | `absent` | `7` | `techniques/agent-workflows/shell-composable-agent-invocation/checks/shell-composable-agent-invocation-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) |

## `docs`

### [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) - source-of-truth-layout (`canonical`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Doc Role Checklist | `present` | `8` | `techniques/docs/source-of-truth-layout/checks/doc-role-checklist.md` | [TECHNIQUE.md](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) |

### [AOA-T-0009](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) - lightweight-status-snapshot (`canonical`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| lightweight-snapshot-checklist | `absent` | `7` | `techniques/docs/lightweight-status-snapshot/checks/lightweight-snapshot-checklist.md` | [TECHNIQUE.md](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) |

### [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) - deterministic-context-composition (`canonical`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Deterministic Context Composition Checklist | `present` | `7` | `techniques/docs/deterministic-context-composition/checks/deterministic-context-composition-checklist.md` | [TECHNIQUE.md](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) |

### [AOA-T-0016](../techniques/docs/bounded-context-map/TECHNIQUE.md) - bounded-context-map (`canonical`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Bounded Context Map Checklist | `present` | `7` | `techniques/docs/bounded-context-map/checks/bounded-context-map-checklist.md` | [TECHNIQUE.md](../techniques/docs/bounded-context-map/TECHNIQUE.md) |

### [AOA-T-0019](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) - frontmatter-metadata-spine (`canonical`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Metadata Spine Checklist | `present` | `5` | `techniques/docs/frontmatter-metadata-spine/checks/metadata-spine-checklist.md` | [TECHNIQUE.md](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) |

### [AOA-T-0021](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) - bounded-relation-lift-for-kag (`canonical`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Relation Lift Checklist | `present` | `5` | `techniques/docs/bounded-relation-lift-for-kag/checks/relation-lift-checklist.md` | [TECHNIQUE.md](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) |

### [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) - single-source-rule-distribution (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Single-Source Rule Distribution Checklist | `present` | `7` | `techniques/docs/single-source-rule-distribution/checks/single-source-rule-distribution-checklist.md` | [TECHNIQUE.md](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) |

### [AOA-T-0018](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) - markdown-technique-section-lift (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Section Lift Checklist | `present` | `5` | `techniques/docs/markdown-technique-section-lift/checks/section-lift-checklist.md` | [TECHNIQUE.md](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) |

### [AOA-T-0020](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) - evidence-note-provenance-lift (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Evidence Note Provenance Checklist | `present` | `5` | `techniques/docs/evidence-note-provenance-lift/checks/evidence-note-provenance-checklist.md` | [TECHNIQUE.md](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) |

### [AOA-T-0022](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) - risk-and-negative-effect-lift (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Caution Lift Checklist | `present` | `5` | `techniques/docs/risk-and-negative-effect-lift/checks/caution-lift-checklist.md` | [TECHNIQUE.md](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) |

### [AOA-T-0024](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) - upstream-mirroring-with-provenance (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Upstream Mirroring With Provenance Checklist | `absent` | `7` | `techniques/docs/upstream-mirroring-with-provenance/checks/upstream-mirroring-with-provenance-checklist.md` | [TECHNIQUE.md](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) |

### [AOA-T-0025](../techniques/docs/capability-spec-versioning/TECHNIQUE.md) - capability-spec-versioning (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Capability Spec Versioning Checklist | `absent` | `7` | `techniques/docs/capability-spec-versioning/checks/capability-spec-versioning-checklist.md` | [TECHNIQUE.md](../techniques/docs/capability-spec-versioning/TECHNIQUE.md) |

### [AOA-T-0027](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) - cross-agent-skill-propagation (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Cross-Agent Skill Propagation Checklist | `absent` | `7` | `techniques/docs/cross-agent-skill-propagation/checks/cross-agent-skill-propagation-checklist.md` | [TECHNIQUE.md](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) |

### [AOA-T-0029](../techniques/docs/nested-rule-loading/TECHNIQUE.md) - nested-rule-loading (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Nested Rule Loading Checklist | `absent` | `7` | `techniques/docs/nested-rule-loading/checks/nested-rule-loading-checklist.md` | [TECHNIQUE.md](../techniques/docs/nested-rule-loading/TECHNIQUE.md) |

### [AOA-T-0030](../techniques/docs/fragmented-agent-context/TECHNIQUE.md) - fragmented-agent-context (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Fragmented Agent Context Checklist | `absent` | `7` | `techniques/docs/fragmented-agent-context/checks/fragmented-agent-context-checklist.md` | [TECHNIQUE.md](../techniques/docs/fragmented-agent-context/TECHNIQUE.md) |

### [AOA-T-0033](../techniques/docs/decision-rationale-recording/TECHNIQUE.md) - decision-rationale-recording (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Decision Rationale Recording Checklist | `absent` | `10` | `techniques/docs/decision-rationale-recording/checks/decision-rationale-recording-checklist.md` | [TECHNIQUE.md](../techniques/docs/decision-rationale-recording/TECHNIQUE.md) |

### [AOA-T-0034](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md) - public-safe-artifact-sanitization (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Public Safe Artifact Sanitization Checklist | `present` | `11` | `techniques/docs/public-safe-artifact-sanitization/checks/public-safe-artifact-sanitization-checklist.md` | [TECHNIQUE.md](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md) |

## `evaluation`

### [AOA-T-0003](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) - contract-first-smoke-summary (`canonical`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Summary Contract Checklist | `present` | `7` | `techniques/evaluation/contract-first-smoke-summary/checks/summary-contract-checklist.md` | [TECHNIQUE.md](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) |

### [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) - latest-alias-plus-history-copy (`canonical`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| dual-write-history-checklist | `absent` | `8` | `techniques/evaluation/latest-alias-plus-history-copy/checks/dual-write-history-checklist.md` | [TECHNIQUE.md](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) |

### [AOA-T-0007](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) - signal-first-gate-promotion (`canonical`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| gate-promotion-checklist | `absent` | `7` | `techniques/evaluation/signal-first-gate-promotion/checks/gate-promotion-checklist.md` | [TECHNIQUE.md](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) |

### [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) - published-summary-remediation-snapshot (`canonical`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| remediation-snapshot-checklist | `absent` | `9` | `techniques/evaluation/published-summary-remediation-snapshot/checks/remediation-snapshot-checklist.md` | [TECHNIQUE.md](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) |

### [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) - telemetry-integrity-snapshot (`canonical`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| telemetry-integrity-checklist | `absent` | `9` | `techniques/evaluation/telemetry-integrity-snapshot/checks/telemetry-integrity-checklist.md` | [TECHNIQUE.md](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) |

### [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) - required-vs-optional-source-rendering (`canonical`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| required-vs-optional-rendering-checklist | `absent` | `8` | `techniques/evaluation/required-vs-optional-source-rendering/checks/required-vs-optional-rendering-checklist.md` | [TECHNIQUE.md](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) |

### [AOA-T-0015](../techniques/evaluation/contract-test-design/TECHNIQUE.md) - contract-test-design (`canonical`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Contract Test Design Checklist | `present` | `8` | `techniques/evaluation/contract-test-design/checks/contract-test-design-checklist.md` | [TECHNIQUE.md](../techniques/evaluation/contract-test-design/TECHNIQUE.md) |

### [AOA-T-0017](../techniques/evaluation/property-invariants/TECHNIQUE.md) - property-invariants (`canonical`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Property Invariants Checklist | `present` | `7` | `techniques/evaluation/property-invariants/checks/property-invariants-checklist.md` | [TECHNIQUE.md](../techniques/evaluation/property-invariants/TECHNIQUE.md) |

### [AOA-T-0032](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md) - context-report-for-ci (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Context Report For CI Checklist | `absent` | `7` | `techniques/evaluation/context-report-for-ci/checks/context-report-for-ci-checklist.md` | [TECHNIQUE.md](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md) |

## `history`

### [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) - session-capture-as-repo-artifact (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Session Capture As Repo Artifact Checklist | `absent` | `7` | `techniques/history/session-capture-as-repo-artifact/checks/session-capture-as-repo-artifact-checklist.md` | [TECHNIQUE.md](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) |

## Boundaries

- The meaning remains in the authored checklist files and source bundles.
- This surface is derived validation knowledge only.
- This surface does not become executable policy, hard-gate semantics, or scoring.
