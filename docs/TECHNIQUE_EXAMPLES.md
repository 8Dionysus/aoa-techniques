# Technique Examples

This file is generated from authoritative `TECHNIQUE.md` bundles plus the current example manifest payload.
Do not edit it by hand; run `python scripts/build_example_manifest.py`.

Use this surface when you want a bounded example inventory by domain and technique without opening every example body first.

This surface preserves example title, example path, body-presence, and source routing only. It does not inline full example bodies into the generated reader surface.

See also:
- [Technique Example Lift Guide](TECHNIQUE_EXAMPLE_LIFT_GUIDE.md)
- [Full example manifest](../generated/technique_example_manifest.json)
- [Min example manifest](../generated/technique_example_manifest.min.json)
- [Documentation Map](README.md)
- [KAG Source Lift Guide](KAG_SOURCE_LIFT_GUIDE.md)

## `agent-workflows`

### [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) - plan-diff-apply-verify-report (`canonical`)

| example | body | example path | source |
|---|---|---|---|
| Minimal Change Flow | `present` | `techniques/agent-workflows/plan-diff-apply-verify-report/examples/minimal-change-flow.md` | [TECHNIQUE.md](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) |

### [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) - intent-plan-dry-run-contract-chain (`canonical`)

| example | body | example path | source |
|---|---|---|---|
| Concrete Non-UI Intent Chain | `present` | `techniques/agent-workflows/intent-plan-dry-run-contract-chain/examples/concrete-non-ui-intent-chain.md` | [TECHNIQUE.md](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) |
| Minimal Intent Chain | `present` | `techniques/agent-workflows/intent-plan-dry-run-contract-chain/examples/minimal-intent-chain.md` | [TECHNIQUE.md](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) |

### [AOA-T-0014](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) - tdd-slice (`canonical`)

| example | body | example path | source |
|---|---|---|---|
| Concrete Application Handler Slice | `present` | `techniques/agent-workflows/tdd-slice/examples/concrete-application-handler-slice.md` | [TECHNIQUE.md](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) |
| Minimal TDD Slice | `present` | `techniques/agent-workflows/tdd-slice/examples/minimal-tdd-slice.md` | [TECHNIQUE.md](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) |

### [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) - new-intent-rollout-checklist (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Concrete Non-UI Intent Rollout | `present` | `techniques/agent-workflows/new-intent-rollout-checklist/examples/concrete-non-ui-intent-rollout.md` | [TECHNIQUE.md](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) |
| minimal-intent-rollout | `present` | `techniques/agent-workflows/new-intent-rollout-checklist/examples/minimal-intent-rollout.md` | [TECHNIQUE.md](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) |

### [AOA-T-0023](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) - stateless-single-shot-agent (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Confirmed Single-Step Action | `present` | `techniques/agent-workflows/stateless-single-shot-agent/examples/confirmed-single-step-action.md` | [TECHNIQUE.md](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) |
| Minimal Stateless Single-Shot Agent | `present` | `techniques/agent-workflows/stateless-single-shot-agent/examples/minimal-stateless-single-shot-agent.md` | [TECHNIQUE.md](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) |

### [AOA-T-0028](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) - confirmation-gated-mutating-action (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Concrete Confirmed Mutating Action | `present` | `techniques/agent-workflows/confirmation-gated-mutating-action/examples/concrete-confirmed-mutating-action.md` | [TECHNIQUE.md](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) |
| Minimal Confirmation Gated Mutating Action | `present` | `techniques/agent-workflows/confirmation-gated-mutating-action/examples/minimal-confirmation-gated-mutating-action.md` | [TECHNIQUE.md](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) |

## `docs`

### [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) - source-of-truth-layout (`canonical`)

| example | body | example path | source |
|---|---|---|---|
| Minimal Doc Routing | `present` | `techniques/docs/source-of-truth-layout/examples/minimal-doc-routing.md` | [TECHNIQUE.md](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) |

### [AOA-T-0009](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) - lightweight-status-snapshot (`canonical`)

| example | body | example path | source |
|---|---|---|---|
| minimal-lightweight-snapshot | `present` | `techniques/docs/lightweight-status-snapshot/examples/minimal-lightweight-snapshot.md` | [TECHNIQUE.md](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) |

### [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) - deterministic-context-composition (`canonical`)

| example | body | example path | source |
|---|---|---|---|
| Concrete Skill Doc Composition | `present` | `techniques/docs/deterministic-context-composition/examples/concrete-skill-doc-composition.md` | [TECHNIQUE.md](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) |
| Minimal Deterministic Context Composition | `present` | `techniques/docs/deterministic-context-composition/examples/minimal-deterministic-context-composition.md` | [TECHNIQUE.md](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) |

### [AOA-T-0016](../techniques/docs/bounded-context-map/TECHNIQUE.md) - bounded-context-map (`canonical`)

| example | body | example path | source |
|---|---|---|---|
| Concrete Infra Context Map | `present` | `techniques/docs/bounded-context-map/examples/concrete-infra-context-map.md` | [TECHNIQUE.md](../techniques/docs/bounded-context-map/TECHNIQUE.md) |
| Minimal Context Boundary Map | `present` | `techniques/docs/bounded-context-map/examples/minimal-context-boundary-map.md` | [TECHNIQUE.md](../techniques/docs/bounded-context-map/TECHNIQUE.md) |

### [AOA-T-0019](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) - frontmatter-metadata-spine (`canonical`)

| example | body | example path | source |
|---|---|---|---|
| Frontmatter To Catalog Entry | `present` | `techniques/docs/frontmatter-metadata-spine/examples/frontmatter-to-catalog-entry.md` | [TECHNIQUE.md](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) |

### [AOA-T-0021](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) - bounded-relation-lift-for-kag (`canonical`)

| example | body | example path | source |
|---|---|---|---|
| Direct Relation To Selection Hint | `present` | `techniques/docs/bounded-relation-lift-for-kag/examples/direct-relation-to-selection-hint.md` | [TECHNIQUE.md](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) |

### [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) - single-source-rule-distribution (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Concrete Multi-Agent Rule Sync | `present` | `techniques/docs/single-source-rule-distribution/examples/concrete-multi-agent-rule-sync.md` | [TECHNIQUE.md](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) |
| Minimal Single-Source Rule Distribution | `present` | `techniques/docs/single-source-rule-distribution/examples/minimal-single-source-rule-distribution.md` | [TECHNIQUE.md](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) |

### [AOA-T-0018](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) - markdown-technique-section-lift (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Minimal Section Lift | `present` | `techniques/docs/markdown-technique-section-lift/examples/minimal-section-lift.md` | [TECHNIQUE.md](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) |

### [AOA-T-0020](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) - evidence-note-provenance-lift (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Evidence Note To Manifest | `present` | `techniques/docs/evidence-note-provenance-lift/examples/evidence-note-to-manifest.md` | [TECHNIQUE.md](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) |

### [AOA-T-0022](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) - risk-and-negative-effect-lift (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Minimal Risk And Negative-Effect Lift | `present` | `techniques/docs/risk-and-negative-effect-lift/examples/minimal-risk-and-negative-effect-lift.md` | [TECHNIQUE.md](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) |

### [AOA-T-0024](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) - upstream-mirroring-with-provenance (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Concrete Curated Mirror With Attribution | `present` | `techniques/docs/upstream-mirroring-with-provenance/examples/concrete-curated-mirror-with-attribution.md` | [TECHNIQUE.md](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) |
| Minimal Upstream Mirroring With Provenance | `present` | `techniques/docs/upstream-mirroring-with-provenance/examples/minimal-upstream-mirroring-with-provenance.md` | [TECHNIQUE.md](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) |

### [AOA-T-0025](../techniques/docs/capability-spec-versioning/TECHNIQUE.md) - capability-spec-versioning (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Concrete Capability Upgrade With Compat Window | `present` | `techniques/docs/capability-spec-versioning/examples/concrete-capability-upgrade-with-compat-window.md` | [TECHNIQUE.md](../techniques/docs/capability-spec-versioning/TECHNIQUE.md) |
| Minimal Capability Spec Versioning | `present` | `techniques/docs/capability-spec-versioning/examples/minimal-capability-spec-versioning.md` | [TECHNIQUE.md](../techniques/docs/capability-spec-versioning/TECHNIQUE.md) |

### [AOA-T-0027](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) - cross-agent-skill-propagation (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Concrete Multi-Target Skill Propagation | `present` | `techniques/docs/cross-agent-skill-propagation/examples/concrete-multi-target-skill-propagation.md` | [TECHNIQUE.md](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) |
| Minimal Cross-Agent Skill Propagation | `present` | `techniques/docs/cross-agent-skill-propagation/examples/minimal-cross-agent-skill-propagation.md` | [TECHNIQUE.md](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) |

## `evaluation`

### [AOA-T-0003](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) - contract-first-smoke-summary (`canonical`)

| example | body | example path | source |
|---|---|---|---|
| Minimal Smoke Summary Flow | `present` | `techniques/evaluation/contract-first-smoke-summary/examples/minimal-smoke-summary-flow.md` | [TECHNIQUE.md](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) |

### [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) - latest-alias-plus-history-copy (`canonical`)

| example | body | example path | source |
|---|---|---|---|
| minimal-latest-history-layout | `present` | `techniques/evaluation/latest-alias-plus-history-copy/examples/minimal-latest-history-layout.md` | [TECHNIQUE.md](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) |
| object-store-latest-history-layout | `present` | `techniques/evaluation/latest-alias-plus-history-copy/examples/object-store-latest-history-layout.md` | [TECHNIQUE.md](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) |

### [AOA-T-0007](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) - signal-first-gate-promotion (`canonical`)

| example | body | example path | source |
|---|---|---|---|
| Concrete Repo-Validation Rollout | `present` | `techniques/evaluation/signal-first-gate-promotion/examples/concrete-repo-validation-rollout.md` | [TECHNIQUE.md](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) |
| minimal-signal-first-rollout | `present` | `techniques/evaluation/signal-first-gate-promotion/examples/minimal-signal-first-rollout.md` | [TECHNIQUE.md](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) |

### [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) - published-summary-remediation-snapshot (`canonical`)

| example | body | example path | source |
|---|---|---|---|
| minimal-remediation-snapshot | `present` | `techniques/evaluation/published-summary-remediation-snapshot/examples/minimal-remediation-snapshot.md` | [TECHNIQUE.md](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) |
| object-store-remediation-snapshot | `present` | `techniques/evaluation/published-summary-remediation-snapshot/examples/object-store-remediation-snapshot.md` | [TECHNIQUE.md](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) |

### [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) - telemetry-integrity-snapshot (`canonical`)

| example | body | example path | source |
|---|---|---|---|
| minimal-telemetry-integrity-snapshot | `present` | `techniques/evaluation/telemetry-integrity-snapshot/examples/minimal-telemetry-integrity-snapshot.md` | [TECHNIQUE.md](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) |
| object-store-telemetry-integrity-snapshot | `present` | `techniques/evaluation/telemetry-integrity-snapshot/examples/object-store-telemetry-integrity-snapshot.md` | [TECHNIQUE.md](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) |

### [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) - required-vs-optional-source-rendering (`canonical`)

| example | body | example path | source |
|---|---|---|---|
| minimal-required-vs-optional-rendering | `present` | `techniques/evaluation/required-vs-optional-source-rendering/examples/minimal-required-vs-optional-rendering.md` | [TECHNIQUE.md](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) |
| non-ui-required-vs-optional-rendering | `present` | `techniques/evaluation/required-vs-optional-source-rendering/examples/non-ui-required-vs-optional-rendering.md` | [TECHNIQUE.md](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) |

### [AOA-T-0015](../techniques/evaluation/contract-test-design/TECHNIQUE.md) - contract-test-design (`canonical`)

| example | body | example path | source |
|---|---|---|---|
| Concrete API Contract Boundary | `present` | `techniques/evaluation/contract-test-design/examples/concrete-api-contract-boundary.md` | [TECHNIQUE.md](../techniques/evaluation/contract-test-design/TECHNIQUE.md) |
| Minimal Contract Boundary | `present` | `techniques/evaluation/contract-test-design/examples/minimal-contract-boundary.md` | [TECHNIQUE.md](../techniques/evaluation/contract-test-design/TECHNIQUE.md) |

### [AOA-T-0017](../techniques/evaluation/property-invariants/TECHNIQUE.md) - property-invariants (`canonical`)

| example | body | example path | source |
|---|---|---|---|
| Concrete Config Invariant Check | `present` | `techniques/evaluation/property-invariants/examples/concrete-config-invariant-check.md` | [TECHNIQUE.md](../techniques/evaluation/property-invariants/TECHNIQUE.md) |
| Minimal Invariant Check | `present` | `techniques/evaluation/property-invariants/examples/minimal-invariant-check.md` | [TECHNIQUE.md](../techniques/evaluation/property-invariants/TECHNIQUE.md) |

## `history`

### [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) - session-capture-as-repo-artifact (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Concrete Local-First Session History | `present` | `techniques/history/session-capture-as-repo-artifact/examples/concrete-local-first-session-history.md` | [TECHNIQUE.md](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) |
| Minimal Session Capture As Repo Artifact | `present` | `techniques/history/session-capture-as-repo-artifact/examples/minimal-session-capture-as-repo-artifact.md` | [TECHNIQUE.md](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) |

## Boundaries

- The meaning remains in the authored example files and source bundles.
- This surface is derived example knowledge only.
- This surface does not become scenario graphs, executable tests, or richer step extraction.
