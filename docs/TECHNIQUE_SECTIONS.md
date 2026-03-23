# Technique Sections

This file is generated from authoritative `TECHNIQUE.md` bundles plus the current section manifest payload.
Do not edit it by hand; run `python scripts/build_section_manifest.py`.

Use this surface when you need one bounded answer to which techniques expose a given lifted section heading without opening every bundle first.

This surface is heading-first. It stays bounded to exactly `SECTION_LIFT_HEADINGS`, preserves their fixed order, and only exposes technique, section order, and source routing. It does not dump section markdown, invent section IDs, or act like search or graph behavior.

See also:
- [Technique Section Lift Guide](TECHNIQUE_SECTION_LIFT_GUIDE.md)
- [Full section manifest](../generated/technique_section_manifest.json)
- [Min section manifest](../generated/technique_section_manifest.min.json)
- [Documentation Map](README.md)
- [KAG Source Lift Guide](KAG_SOURCE_LIFT_GUIDE.md)

## Section Scope

| order | heading | bounded role |
|---|---|---|
| `1` | `Intent` | Lift the authored `Intent` section into heading-first routing only. |
| `2` | `When to use` | Lift the authored `When to use` section into heading-first routing only. |
| `3` | `When not to use` | Lift the authored `When not to use` section into heading-first routing only. |
| `4` | `Inputs` | Lift the authored `Inputs` section into heading-first routing only. |
| `5` | `Outputs` | Lift the authored `Outputs` section into heading-first routing only. |
| `6` | `Core procedure` | Lift the authored `Core procedure` section into heading-first routing only. |
| `7` | `Contracts` | Lift the authored `Contracts` section into heading-first routing only. |
| `8` | `Risks` | Lift the authored `Risks` section into heading-first routing only. |
| `9` | `Validation` | Lift the authored `Validation` section into heading-first routing only. |
| `10` | `Adaptation notes` | Lift the authored `Adaptation notes` section into heading-first routing only. |

## `Intent`

| technique | domain | status | section order | source |
|---|---|---|---|---|
| [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) - plan-diff-apply-verify-report | `agent-workflows` | `canonical` | `1` | [TECHNIQUE.md](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) |
| [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) - intent-plan-dry-run-contract-chain | `agent-workflows` | `canonical` | `1` | [TECHNIQUE.md](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) |
| [AOA-T-0014](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) - tdd-slice | `agent-workflows` | `canonical` | `1` | [TECHNIQUE.md](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) |
| [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) - new-intent-rollout-checklist | `agent-workflows` | `promoted` | `1` | [TECHNIQUE.md](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) |
| [AOA-T-0023](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) - stateless-single-shot-agent | `agent-workflows` | `promoted` | `1` | [TECHNIQUE.md](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) |
| [AOA-T-0028](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) - confirmation-gated-mutating-action | `agent-workflows` | `promoted` | `1` | [TECHNIQUE.md](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) |
| [AOA-T-0031](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) - shell-composable-agent-invocation | `agent-workflows` | `promoted` | `1` | [TECHNIQUE.md](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) |
| [AOA-T-0036](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md) - render-truth-before-startup | `agent-workflows` | `promoted` | `1` | [TECHNIQUE.md](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md) |
| [AOA-T-0038](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) - one-command-service-lifecycle | `agent-workflows` | `promoted` | `1` | [TECHNIQUE.md](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) |
| [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) - source-of-truth-layout | `docs` | `canonical` | `1` | [TECHNIQUE.md](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) |
| [AOA-T-0009](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) - lightweight-status-snapshot | `docs` | `canonical` | `1` | [TECHNIQUE.md](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) |
| [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) - deterministic-context-composition | `docs` | `canonical` | `1` | [TECHNIQUE.md](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) |
| [AOA-T-0016](../techniques/docs/bounded-context-map/TECHNIQUE.md) - bounded-context-map | `docs` | `canonical` | `1` | [TECHNIQUE.md](../techniques/docs/bounded-context-map/TECHNIQUE.md) |
| [AOA-T-0019](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) - frontmatter-metadata-spine | `docs` | `canonical` | `1` | [TECHNIQUE.md](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) |
| [AOA-T-0021](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) - bounded-relation-lift-for-kag | `docs` | `canonical` | `1` | [TECHNIQUE.md](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) |
| [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) - single-source-rule-distribution | `docs` | `promoted` | `1` | [TECHNIQUE.md](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) |
| [AOA-T-0018](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) - markdown-technique-section-lift | `docs` | `promoted` | `1` | [TECHNIQUE.md](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) |
| [AOA-T-0020](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) - evidence-note-provenance-lift | `docs` | `promoted` | `1` | [TECHNIQUE.md](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) |
| [AOA-T-0022](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) - risk-and-negative-effect-lift | `docs` | `promoted` | `1` | [TECHNIQUE.md](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) |
| [AOA-T-0024](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) - upstream-mirroring-with-provenance | `docs` | `promoted` | `1` | [TECHNIQUE.md](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) |
| [AOA-T-0025](../techniques/docs/capability-spec-versioning/TECHNIQUE.md) - capability-spec-versioning | `docs` | `promoted` | `1` | [TECHNIQUE.md](../techniques/docs/capability-spec-versioning/TECHNIQUE.md) |
| [AOA-T-0027](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) - cross-agent-skill-propagation | `docs` | `promoted` | `1` | [TECHNIQUE.md](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) |
| [AOA-T-0029](../techniques/docs/nested-rule-loading/TECHNIQUE.md) - nested-rule-loading | `docs` | `promoted` | `1` | [TECHNIQUE.md](../techniques/docs/nested-rule-loading/TECHNIQUE.md) |
| [AOA-T-0030](../techniques/docs/fragmented-agent-context/TECHNIQUE.md) - fragmented-agent-context | `docs` | `promoted` | `1` | [TECHNIQUE.md](../techniques/docs/fragmented-agent-context/TECHNIQUE.md) |
| [AOA-T-0033](../techniques/docs/decision-rationale-recording/TECHNIQUE.md) - decision-rationale-recording | `docs` | `promoted` | `1` | [TECHNIQUE.md](../techniques/docs/decision-rationale-recording/TECHNIQUE.md) |
| [AOA-T-0034](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md) - public-safe-artifact-sanitization | `docs` | `promoted` | `1` | [TECHNIQUE.md](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md) |
| [AOA-T-0035](../techniques/docs/profile-preset-composition/TECHNIQUE.md) - profile-preset-composition | `docs` | `promoted` | `1` | [TECHNIQUE.md](../techniques/docs/profile-preset-composition/TECHNIQUE.md) |
| [AOA-T-0040](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md) - skill-vs-command-boundary | `docs` | `promoted` | `1` | [TECHNIQUE.md](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md) |
| [AOA-T-0041](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) - skill-marketplace-curation | `docs` | `promoted` | `1` | [TECHNIQUE.md](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) |
| [AOA-T-0043](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md) - multi-source-primary-input-provenance | `docs` | `promoted` | `1` | [TECHNIQUE.md](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md) |
| [AOA-T-0003](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) - contract-first-smoke-summary | `evaluation` | `canonical` | `1` | [TECHNIQUE.md](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) |
| [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) - latest-alias-plus-history-copy | `evaluation` | `canonical` | `1` | [TECHNIQUE.md](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) |
| [AOA-T-0007](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) - signal-first-gate-promotion | `evaluation` | `canonical` | `1` | [TECHNIQUE.md](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) |
| [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) - published-summary-remediation-snapshot | `evaluation` | `canonical` | `1` | [TECHNIQUE.md](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) |
| [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) - telemetry-integrity-snapshot | `evaluation` | `canonical` | `1` | [TECHNIQUE.md](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) |
| [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) - required-vs-optional-source-rendering | `evaluation` | `canonical` | `1` | [TECHNIQUE.md](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) |
| [AOA-T-0015](../techniques/evaluation/contract-test-design/TECHNIQUE.md) - contract-test-design | `evaluation` | `canonical` | `1` | [TECHNIQUE.md](../techniques/evaluation/contract-test-design/TECHNIQUE.md) |
| [AOA-T-0017](../techniques/evaluation/property-invariants/TECHNIQUE.md) - property-invariants | `evaluation` | `canonical` | `1` | [TECHNIQUE.md](../techniques/evaluation/property-invariants/TECHNIQUE.md) |
| [AOA-T-0032](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md) - context-report-for-ci | `evaluation` | `promoted` | `1` | [TECHNIQUE.md](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md) |
| [AOA-T-0037](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md) - contextual-host-doctor | `evaluation` | `promoted` | `1` | [TECHNIQUE.md](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md) |
| [AOA-T-0039](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) - baseline-first-additive-profile-benchmarks | `evaluation` | `promoted` | `1` | [TECHNIQUE.md](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) |
| [AOA-T-0042](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md) - upstream-skill-health-checking | `evaluation` | `promoted` | `1` | [TECHNIQUE.md](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md) |
| [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) - session-capture-as-repo-artifact | `history` | `promoted` | `1` | [TECHNIQUE.md](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) |
| [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) - versionable-session-transcripts | `history` | `promoted` | `1` | [TECHNIQUE.md](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) |
| [AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) - witness-trace-as-reviewable-artifact | `history` | `promoted` | `1` | [TECHNIQUE.md](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) |

## `When to use`

| technique | domain | status | section order | source |
|---|---|---|---|---|
| [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) - plan-diff-apply-verify-report | `agent-workflows` | `canonical` | `2` | [TECHNIQUE.md](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) |
| [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) - intent-plan-dry-run-contract-chain | `agent-workflows` | `canonical` | `2` | [TECHNIQUE.md](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) |
| [AOA-T-0014](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) - tdd-slice | `agent-workflows` | `canonical` | `2` | [TECHNIQUE.md](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) |
| [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) - new-intent-rollout-checklist | `agent-workflows` | `promoted` | `2` | [TECHNIQUE.md](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) |
| [AOA-T-0023](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) - stateless-single-shot-agent | `agent-workflows` | `promoted` | `2` | [TECHNIQUE.md](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) |
| [AOA-T-0028](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) - confirmation-gated-mutating-action | `agent-workflows` | `promoted` | `2` | [TECHNIQUE.md](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) |
| [AOA-T-0031](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) - shell-composable-agent-invocation | `agent-workflows` | `promoted` | `2` | [TECHNIQUE.md](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) |
| [AOA-T-0036](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md) - render-truth-before-startup | `agent-workflows` | `promoted` | `2` | [TECHNIQUE.md](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md) |
| [AOA-T-0038](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) - one-command-service-lifecycle | `agent-workflows` | `promoted` | `2` | [TECHNIQUE.md](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) |
| [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) - source-of-truth-layout | `docs` | `canonical` | `2` | [TECHNIQUE.md](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) |
| [AOA-T-0009](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) - lightweight-status-snapshot | `docs` | `canonical` | `2` | [TECHNIQUE.md](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) |
| [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) - deterministic-context-composition | `docs` | `canonical` | `2` | [TECHNIQUE.md](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) |
| [AOA-T-0016](../techniques/docs/bounded-context-map/TECHNIQUE.md) - bounded-context-map | `docs` | `canonical` | `2` | [TECHNIQUE.md](../techniques/docs/bounded-context-map/TECHNIQUE.md) |
| [AOA-T-0019](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) - frontmatter-metadata-spine | `docs` | `canonical` | `2` | [TECHNIQUE.md](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) |
| [AOA-T-0021](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) - bounded-relation-lift-for-kag | `docs` | `canonical` | `2` | [TECHNIQUE.md](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) |
| [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) - single-source-rule-distribution | `docs` | `promoted` | `2` | [TECHNIQUE.md](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) |
| [AOA-T-0018](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) - markdown-technique-section-lift | `docs` | `promoted` | `2` | [TECHNIQUE.md](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) |
| [AOA-T-0020](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) - evidence-note-provenance-lift | `docs` | `promoted` | `2` | [TECHNIQUE.md](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) |
| [AOA-T-0022](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) - risk-and-negative-effect-lift | `docs` | `promoted` | `2` | [TECHNIQUE.md](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) |
| [AOA-T-0024](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) - upstream-mirroring-with-provenance | `docs` | `promoted` | `2` | [TECHNIQUE.md](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) |
| [AOA-T-0025](../techniques/docs/capability-spec-versioning/TECHNIQUE.md) - capability-spec-versioning | `docs` | `promoted` | `2` | [TECHNIQUE.md](../techniques/docs/capability-spec-versioning/TECHNIQUE.md) |
| [AOA-T-0027](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) - cross-agent-skill-propagation | `docs` | `promoted` | `2` | [TECHNIQUE.md](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) |
| [AOA-T-0029](../techniques/docs/nested-rule-loading/TECHNIQUE.md) - nested-rule-loading | `docs` | `promoted` | `2` | [TECHNIQUE.md](../techniques/docs/nested-rule-loading/TECHNIQUE.md) |
| [AOA-T-0030](../techniques/docs/fragmented-agent-context/TECHNIQUE.md) - fragmented-agent-context | `docs` | `promoted` | `2` | [TECHNIQUE.md](../techniques/docs/fragmented-agent-context/TECHNIQUE.md) |
| [AOA-T-0033](../techniques/docs/decision-rationale-recording/TECHNIQUE.md) - decision-rationale-recording | `docs` | `promoted` | `2` | [TECHNIQUE.md](../techniques/docs/decision-rationale-recording/TECHNIQUE.md) |
| [AOA-T-0034](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md) - public-safe-artifact-sanitization | `docs` | `promoted` | `2` | [TECHNIQUE.md](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md) |
| [AOA-T-0035](../techniques/docs/profile-preset-composition/TECHNIQUE.md) - profile-preset-composition | `docs` | `promoted` | `2` | [TECHNIQUE.md](../techniques/docs/profile-preset-composition/TECHNIQUE.md) |
| [AOA-T-0040](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md) - skill-vs-command-boundary | `docs` | `promoted` | `2` | [TECHNIQUE.md](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md) |
| [AOA-T-0041](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) - skill-marketplace-curation | `docs` | `promoted` | `2` | [TECHNIQUE.md](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) |
| [AOA-T-0043](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md) - multi-source-primary-input-provenance | `docs` | `promoted` | `2` | [TECHNIQUE.md](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md) |
| [AOA-T-0003](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) - contract-first-smoke-summary | `evaluation` | `canonical` | `2` | [TECHNIQUE.md](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) |
| [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) - latest-alias-plus-history-copy | `evaluation` | `canonical` | `2` | [TECHNIQUE.md](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) |
| [AOA-T-0007](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) - signal-first-gate-promotion | `evaluation` | `canonical` | `2` | [TECHNIQUE.md](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) |
| [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) - published-summary-remediation-snapshot | `evaluation` | `canonical` | `2` | [TECHNIQUE.md](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) |
| [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) - telemetry-integrity-snapshot | `evaluation` | `canonical` | `2` | [TECHNIQUE.md](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) |
| [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) - required-vs-optional-source-rendering | `evaluation` | `canonical` | `2` | [TECHNIQUE.md](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) |
| [AOA-T-0015](../techniques/evaluation/contract-test-design/TECHNIQUE.md) - contract-test-design | `evaluation` | `canonical` | `2` | [TECHNIQUE.md](../techniques/evaluation/contract-test-design/TECHNIQUE.md) |
| [AOA-T-0017](../techniques/evaluation/property-invariants/TECHNIQUE.md) - property-invariants | `evaluation` | `canonical` | `2` | [TECHNIQUE.md](../techniques/evaluation/property-invariants/TECHNIQUE.md) |
| [AOA-T-0032](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md) - context-report-for-ci | `evaluation` | `promoted` | `2` | [TECHNIQUE.md](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md) |
| [AOA-T-0037](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md) - contextual-host-doctor | `evaluation` | `promoted` | `2` | [TECHNIQUE.md](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md) |
| [AOA-T-0039](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) - baseline-first-additive-profile-benchmarks | `evaluation` | `promoted` | `2` | [TECHNIQUE.md](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) |
| [AOA-T-0042](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md) - upstream-skill-health-checking | `evaluation` | `promoted` | `2` | [TECHNIQUE.md](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md) |
| [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) - session-capture-as-repo-artifact | `history` | `promoted` | `2` | [TECHNIQUE.md](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) |
| [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) - versionable-session-transcripts | `history` | `promoted` | `2` | [TECHNIQUE.md](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) |
| [AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) - witness-trace-as-reviewable-artifact | `history` | `promoted` | `2` | [TECHNIQUE.md](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) |

## `When not to use`

| technique | domain | status | section order | source |
|---|---|---|---|---|
| [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) - plan-diff-apply-verify-report | `agent-workflows` | `canonical` | `3` | [TECHNIQUE.md](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) |
| [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) - intent-plan-dry-run-contract-chain | `agent-workflows` | `canonical` | `3` | [TECHNIQUE.md](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) |
| [AOA-T-0014](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) - tdd-slice | `agent-workflows` | `canonical` | `3` | [TECHNIQUE.md](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) |
| [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) - new-intent-rollout-checklist | `agent-workflows` | `promoted` | `3` | [TECHNIQUE.md](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) |
| [AOA-T-0023](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) - stateless-single-shot-agent | `agent-workflows` | `promoted` | `3` | [TECHNIQUE.md](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) |
| [AOA-T-0028](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) - confirmation-gated-mutating-action | `agent-workflows` | `promoted` | `3` | [TECHNIQUE.md](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) |
| [AOA-T-0031](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) - shell-composable-agent-invocation | `agent-workflows` | `promoted` | `3` | [TECHNIQUE.md](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) |
| [AOA-T-0036](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md) - render-truth-before-startup | `agent-workflows` | `promoted` | `3` | [TECHNIQUE.md](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md) |
| [AOA-T-0038](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) - one-command-service-lifecycle | `agent-workflows` | `promoted` | `3` | [TECHNIQUE.md](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) |
| [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) - source-of-truth-layout | `docs` | `canonical` | `3` | [TECHNIQUE.md](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) |
| [AOA-T-0009](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) - lightweight-status-snapshot | `docs` | `canonical` | `3` | [TECHNIQUE.md](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) |
| [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) - deterministic-context-composition | `docs` | `canonical` | `3` | [TECHNIQUE.md](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) |
| [AOA-T-0016](../techniques/docs/bounded-context-map/TECHNIQUE.md) - bounded-context-map | `docs` | `canonical` | `3` | [TECHNIQUE.md](../techniques/docs/bounded-context-map/TECHNIQUE.md) |
| [AOA-T-0019](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) - frontmatter-metadata-spine | `docs` | `canonical` | `3` | [TECHNIQUE.md](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) |
| [AOA-T-0021](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) - bounded-relation-lift-for-kag | `docs` | `canonical` | `3` | [TECHNIQUE.md](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) |
| [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) - single-source-rule-distribution | `docs` | `promoted` | `3` | [TECHNIQUE.md](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) |
| [AOA-T-0018](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) - markdown-technique-section-lift | `docs` | `promoted` | `3` | [TECHNIQUE.md](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) |
| [AOA-T-0020](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) - evidence-note-provenance-lift | `docs` | `promoted` | `3` | [TECHNIQUE.md](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) |
| [AOA-T-0022](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) - risk-and-negative-effect-lift | `docs` | `promoted` | `3` | [TECHNIQUE.md](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) |
| [AOA-T-0024](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) - upstream-mirroring-with-provenance | `docs` | `promoted` | `3` | [TECHNIQUE.md](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) |
| [AOA-T-0025](../techniques/docs/capability-spec-versioning/TECHNIQUE.md) - capability-spec-versioning | `docs` | `promoted` | `3` | [TECHNIQUE.md](../techniques/docs/capability-spec-versioning/TECHNIQUE.md) |
| [AOA-T-0027](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) - cross-agent-skill-propagation | `docs` | `promoted` | `3` | [TECHNIQUE.md](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) |
| [AOA-T-0029](../techniques/docs/nested-rule-loading/TECHNIQUE.md) - nested-rule-loading | `docs` | `promoted` | `3` | [TECHNIQUE.md](../techniques/docs/nested-rule-loading/TECHNIQUE.md) |
| [AOA-T-0030](../techniques/docs/fragmented-agent-context/TECHNIQUE.md) - fragmented-agent-context | `docs` | `promoted` | `3` | [TECHNIQUE.md](../techniques/docs/fragmented-agent-context/TECHNIQUE.md) |
| [AOA-T-0033](../techniques/docs/decision-rationale-recording/TECHNIQUE.md) - decision-rationale-recording | `docs` | `promoted` | `3` | [TECHNIQUE.md](../techniques/docs/decision-rationale-recording/TECHNIQUE.md) |
| [AOA-T-0034](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md) - public-safe-artifact-sanitization | `docs` | `promoted` | `3` | [TECHNIQUE.md](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md) |
| [AOA-T-0035](../techniques/docs/profile-preset-composition/TECHNIQUE.md) - profile-preset-composition | `docs` | `promoted` | `3` | [TECHNIQUE.md](../techniques/docs/profile-preset-composition/TECHNIQUE.md) |
| [AOA-T-0040](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md) - skill-vs-command-boundary | `docs` | `promoted` | `3` | [TECHNIQUE.md](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md) |
| [AOA-T-0041](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) - skill-marketplace-curation | `docs` | `promoted` | `3` | [TECHNIQUE.md](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) |
| [AOA-T-0043](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md) - multi-source-primary-input-provenance | `docs` | `promoted` | `3` | [TECHNIQUE.md](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md) |
| [AOA-T-0003](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) - contract-first-smoke-summary | `evaluation` | `canonical` | `3` | [TECHNIQUE.md](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) |
| [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) - latest-alias-plus-history-copy | `evaluation` | `canonical` | `3` | [TECHNIQUE.md](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) |
| [AOA-T-0007](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) - signal-first-gate-promotion | `evaluation` | `canonical` | `3` | [TECHNIQUE.md](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) |
| [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) - published-summary-remediation-snapshot | `evaluation` | `canonical` | `3` | [TECHNIQUE.md](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) |
| [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) - telemetry-integrity-snapshot | `evaluation` | `canonical` | `3` | [TECHNIQUE.md](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) |
| [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) - required-vs-optional-source-rendering | `evaluation` | `canonical` | `3` | [TECHNIQUE.md](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) |
| [AOA-T-0015](../techniques/evaluation/contract-test-design/TECHNIQUE.md) - contract-test-design | `evaluation` | `canonical` | `3` | [TECHNIQUE.md](../techniques/evaluation/contract-test-design/TECHNIQUE.md) |
| [AOA-T-0017](../techniques/evaluation/property-invariants/TECHNIQUE.md) - property-invariants | `evaluation` | `canonical` | `3` | [TECHNIQUE.md](../techniques/evaluation/property-invariants/TECHNIQUE.md) |
| [AOA-T-0032](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md) - context-report-for-ci | `evaluation` | `promoted` | `3` | [TECHNIQUE.md](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md) |
| [AOA-T-0037](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md) - contextual-host-doctor | `evaluation` | `promoted` | `3` | [TECHNIQUE.md](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md) |
| [AOA-T-0039](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) - baseline-first-additive-profile-benchmarks | `evaluation` | `promoted` | `3` | [TECHNIQUE.md](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) |
| [AOA-T-0042](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md) - upstream-skill-health-checking | `evaluation` | `promoted` | `3` | [TECHNIQUE.md](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md) |
| [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) - session-capture-as-repo-artifact | `history` | `promoted` | `3` | [TECHNIQUE.md](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) |
| [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) - versionable-session-transcripts | `history` | `promoted` | `3` | [TECHNIQUE.md](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) |
| [AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) - witness-trace-as-reviewable-artifact | `history` | `promoted` | `3` | [TECHNIQUE.md](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) |

## `Inputs`

| technique | domain | status | section order | source |
|---|---|---|---|---|
| [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) - plan-diff-apply-verify-report | `agent-workflows` | `canonical` | `4` | [TECHNIQUE.md](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) |
| [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) - intent-plan-dry-run-contract-chain | `agent-workflows` | `canonical` | `4` | [TECHNIQUE.md](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) |
| [AOA-T-0014](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) - tdd-slice | `agent-workflows` | `canonical` | `4` | [TECHNIQUE.md](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) |
| [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) - new-intent-rollout-checklist | `agent-workflows` | `promoted` | `4` | [TECHNIQUE.md](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) |
| [AOA-T-0023](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) - stateless-single-shot-agent | `agent-workflows` | `promoted` | `4` | [TECHNIQUE.md](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) |
| [AOA-T-0028](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) - confirmation-gated-mutating-action | `agent-workflows` | `promoted` | `4` | [TECHNIQUE.md](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) |
| [AOA-T-0031](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) - shell-composable-agent-invocation | `agent-workflows` | `promoted` | `4` | [TECHNIQUE.md](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) |
| [AOA-T-0036](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md) - render-truth-before-startup | `agent-workflows` | `promoted` | `4` | [TECHNIQUE.md](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md) |
| [AOA-T-0038](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) - one-command-service-lifecycle | `agent-workflows` | `promoted` | `4` | [TECHNIQUE.md](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) |
| [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) - source-of-truth-layout | `docs` | `canonical` | `4` | [TECHNIQUE.md](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) |
| [AOA-T-0009](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) - lightweight-status-snapshot | `docs` | `canonical` | `4` | [TECHNIQUE.md](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) |
| [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) - deterministic-context-composition | `docs` | `canonical` | `4` | [TECHNIQUE.md](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) |
| [AOA-T-0016](../techniques/docs/bounded-context-map/TECHNIQUE.md) - bounded-context-map | `docs` | `canonical` | `4` | [TECHNIQUE.md](../techniques/docs/bounded-context-map/TECHNIQUE.md) |
| [AOA-T-0019](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) - frontmatter-metadata-spine | `docs` | `canonical` | `4` | [TECHNIQUE.md](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) |
| [AOA-T-0021](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) - bounded-relation-lift-for-kag | `docs` | `canonical` | `4` | [TECHNIQUE.md](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) |
| [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) - single-source-rule-distribution | `docs` | `promoted` | `4` | [TECHNIQUE.md](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) |
| [AOA-T-0018](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) - markdown-technique-section-lift | `docs` | `promoted` | `4` | [TECHNIQUE.md](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) |
| [AOA-T-0020](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) - evidence-note-provenance-lift | `docs` | `promoted` | `4` | [TECHNIQUE.md](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) |
| [AOA-T-0022](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) - risk-and-negative-effect-lift | `docs` | `promoted` | `4` | [TECHNIQUE.md](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) |
| [AOA-T-0024](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) - upstream-mirroring-with-provenance | `docs` | `promoted` | `4` | [TECHNIQUE.md](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) |
| [AOA-T-0025](../techniques/docs/capability-spec-versioning/TECHNIQUE.md) - capability-spec-versioning | `docs` | `promoted` | `4` | [TECHNIQUE.md](../techniques/docs/capability-spec-versioning/TECHNIQUE.md) |
| [AOA-T-0027](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) - cross-agent-skill-propagation | `docs` | `promoted` | `4` | [TECHNIQUE.md](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) |
| [AOA-T-0029](../techniques/docs/nested-rule-loading/TECHNIQUE.md) - nested-rule-loading | `docs` | `promoted` | `4` | [TECHNIQUE.md](../techniques/docs/nested-rule-loading/TECHNIQUE.md) |
| [AOA-T-0030](../techniques/docs/fragmented-agent-context/TECHNIQUE.md) - fragmented-agent-context | `docs` | `promoted` | `4` | [TECHNIQUE.md](../techniques/docs/fragmented-agent-context/TECHNIQUE.md) |
| [AOA-T-0033](../techniques/docs/decision-rationale-recording/TECHNIQUE.md) - decision-rationale-recording | `docs` | `promoted` | `4` | [TECHNIQUE.md](../techniques/docs/decision-rationale-recording/TECHNIQUE.md) |
| [AOA-T-0034](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md) - public-safe-artifact-sanitization | `docs` | `promoted` | `4` | [TECHNIQUE.md](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md) |
| [AOA-T-0035](../techniques/docs/profile-preset-composition/TECHNIQUE.md) - profile-preset-composition | `docs` | `promoted` | `4` | [TECHNIQUE.md](../techniques/docs/profile-preset-composition/TECHNIQUE.md) |
| [AOA-T-0040](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md) - skill-vs-command-boundary | `docs` | `promoted` | `4` | [TECHNIQUE.md](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md) |
| [AOA-T-0041](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) - skill-marketplace-curation | `docs` | `promoted` | `4` | [TECHNIQUE.md](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) |
| [AOA-T-0043](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md) - multi-source-primary-input-provenance | `docs` | `promoted` | `4` | [TECHNIQUE.md](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md) |
| [AOA-T-0003](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) - contract-first-smoke-summary | `evaluation` | `canonical` | `4` | [TECHNIQUE.md](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) |
| [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) - latest-alias-plus-history-copy | `evaluation` | `canonical` | `4` | [TECHNIQUE.md](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) |
| [AOA-T-0007](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) - signal-first-gate-promotion | `evaluation` | `canonical` | `4` | [TECHNIQUE.md](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) |
| [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) - published-summary-remediation-snapshot | `evaluation` | `canonical` | `4` | [TECHNIQUE.md](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) |
| [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) - telemetry-integrity-snapshot | `evaluation` | `canonical` | `4` | [TECHNIQUE.md](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) |
| [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) - required-vs-optional-source-rendering | `evaluation` | `canonical` | `4` | [TECHNIQUE.md](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) |
| [AOA-T-0015](../techniques/evaluation/contract-test-design/TECHNIQUE.md) - contract-test-design | `evaluation` | `canonical` | `4` | [TECHNIQUE.md](../techniques/evaluation/contract-test-design/TECHNIQUE.md) |
| [AOA-T-0017](../techniques/evaluation/property-invariants/TECHNIQUE.md) - property-invariants | `evaluation` | `canonical` | `4` | [TECHNIQUE.md](../techniques/evaluation/property-invariants/TECHNIQUE.md) |
| [AOA-T-0032](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md) - context-report-for-ci | `evaluation` | `promoted` | `4` | [TECHNIQUE.md](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md) |
| [AOA-T-0037](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md) - contextual-host-doctor | `evaluation` | `promoted` | `4` | [TECHNIQUE.md](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md) |
| [AOA-T-0039](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) - baseline-first-additive-profile-benchmarks | `evaluation` | `promoted` | `4` | [TECHNIQUE.md](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) |
| [AOA-T-0042](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md) - upstream-skill-health-checking | `evaluation` | `promoted` | `4` | [TECHNIQUE.md](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md) |
| [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) - session-capture-as-repo-artifact | `history` | `promoted` | `4` | [TECHNIQUE.md](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) |
| [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) - versionable-session-transcripts | `history` | `promoted` | `4` | [TECHNIQUE.md](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) |
| [AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) - witness-trace-as-reviewable-artifact | `history` | `promoted` | `4` | [TECHNIQUE.md](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) |

## `Outputs`

| technique | domain | status | section order | source |
|---|---|---|---|---|
| [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) - plan-diff-apply-verify-report | `agent-workflows` | `canonical` | `5` | [TECHNIQUE.md](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) |
| [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) - intent-plan-dry-run-contract-chain | `agent-workflows` | `canonical` | `5` | [TECHNIQUE.md](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) |
| [AOA-T-0014](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) - tdd-slice | `agent-workflows` | `canonical` | `5` | [TECHNIQUE.md](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) |
| [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) - new-intent-rollout-checklist | `agent-workflows` | `promoted` | `5` | [TECHNIQUE.md](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) |
| [AOA-T-0023](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) - stateless-single-shot-agent | `agent-workflows` | `promoted` | `5` | [TECHNIQUE.md](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) |
| [AOA-T-0028](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) - confirmation-gated-mutating-action | `agent-workflows` | `promoted` | `5` | [TECHNIQUE.md](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) |
| [AOA-T-0031](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) - shell-composable-agent-invocation | `agent-workflows` | `promoted` | `5` | [TECHNIQUE.md](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) |
| [AOA-T-0036](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md) - render-truth-before-startup | `agent-workflows` | `promoted` | `5` | [TECHNIQUE.md](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md) |
| [AOA-T-0038](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) - one-command-service-lifecycle | `agent-workflows` | `promoted` | `5` | [TECHNIQUE.md](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) |
| [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) - source-of-truth-layout | `docs` | `canonical` | `5` | [TECHNIQUE.md](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) |
| [AOA-T-0009](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) - lightweight-status-snapshot | `docs` | `canonical` | `5` | [TECHNIQUE.md](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) |
| [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) - deterministic-context-composition | `docs` | `canonical` | `5` | [TECHNIQUE.md](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) |
| [AOA-T-0016](../techniques/docs/bounded-context-map/TECHNIQUE.md) - bounded-context-map | `docs` | `canonical` | `5` | [TECHNIQUE.md](../techniques/docs/bounded-context-map/TECHNIQUE.md) |
| [AOA-T-0019](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) - frontmatter-metadata-spine | `docs` | `canonical` | `5` | [TECHNIQUE.md](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) |
| [AOA-T-0021](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) - bounded-relation-lift-for-kag | `docs` | `canonical` | `5` | [TECHNIQUE.md](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) |
| [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) - single-source-rule-distribution | `docs` | `promoted` | `5` | [TECHNIQUE.md](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) |
| [AOA-T-0018](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) - markdown-technique-section-lift | `docs` | `promoted` | `5` | [TECHNIQUE.md](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) |
| [AOA-T-0020](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) - evidence-note-provenance-lift | `docs` | `promoted` | `5` | [TECHNIQUE.md](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) |
| [AOA-T-0022](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) - risk-and-negative-effect-lift | `docs` | `promoted` | `5` | [TECHNIQUE.md](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) |
| [AOA-T-0024](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) - upstream-mirroring-with-provenance | `docs` | `promoted` | `5` | [TECHNIQUE.md](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) |
| [AOA-T-0025](../techniques/docs/capability-spec-versioning/TECHNIQUE.md) - capability-spec-versioning | `docs` | `promoted` | `5` | [TECHNIQUE.md](../techniques/docs/capability-spec-versioning/TECHNIQUE.md) |
| [AOA-T-0027](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) - cross-agent-skill-propagation | `docs` | `promoted` | `5` | [TECHNIQUE.md](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) |
| [AOA-T-0029](../techniques/docs/nested-rule-loading/TECHNIQUE.md) - nested-rule-loading | `docs` | `promoted` | `5` | [TECHNIQUE.md](../techniques/docs/nested-rule-loading/TECHNIQUE.md) |
| [AOA-T-0030](../techniques/docs/fragmented-agent-context/TECHNIQUE.md) - fragmented-agent-context | `docs` | `promoted` | `5` | [TECHNIQUE.md](../techniques/docs/fragmented-agent-context/TECHNIQUE.md) |
| [AOA-T-0033](../techniques/docs/decision-rationale-recording/TECHNIQUE.md) - decision-rationale-recording | `docs` | `promoted` | `5` | [TECHNIQUE.md](../techniques/docs/decision-rationale-recording/TECHNIQUE.md) |
| [AOA-T-0034](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md) - public-safe-artifact-sanitization | `docs` | `promoted` | `5` | [TECHNIQUE.md](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md) |
| [AOA-T-0035](../techniques/docs/profile-preset-composition/TECHNIQUE.md) - profile-preset-composition | `docs` | `promoted` | `5` | [TECHNIQUE.md](../techniques/docs/profile-preset-composition/TECHNIQUE.md) |
| [AOA-T-0040](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md) - skill-vs-command-boundary | `docs` | `promoted` | `5` | [TECHNIQUE.md](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md) |
| [AOA-T-0041](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) - skill-marketplace-curation | `docs` | `promoted` | `5` | [TECHNIQUE.md](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) |
| [AOA-T-0043](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md) - multi-source-primary-input-provenance | `docs` | `promoted` | `5` | [TECHNIQUE.md](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md) |
| [AOA-T-0003](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) - contract-first-smoke-summary | `evaluation` | `canonical` | `5` | [TECHNIQUE.md](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) |
| [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) - latest-alias-plus-history-copy | `evaluation` | `canonical` | `5` | [TECHNIQUE.md](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) |
| [AOA-T-0007](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) - signal-first-gate-promotion | `evaluation` | `canonical` | `5` | [TECHNIQUE.md](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) |
| [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) - published-summary-remediation-snapshot | `evaluation` | `canonical` | `5` | [TECHNIQUE.md](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) |
| [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) - telemetry-integrity-snapshot | `evaluation` | `canonical` | `5` | [TECHNIQUE.md](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) |
| [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) - required-vs-optional-source-rendering | `evaluation` | `canonical` | `5` | [TECHNIQUE.md](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) |
| [AOA-T-0015](../techniques/evaluation/contract-test-design/TECHNIQUE.md) - contract-test-design | `evaluation` | `canonical` | `5` | [TECHNIQUE.md](../techniques/evaluation/contract-test-design/TECHNIQUE.md) |
| [AOA-T-0017](../techniques/evaluation/property-invariants/TECHNIQUE.md) - property-invariants | `evaluation` | `canonical` | `5` | [TECHNIQUE.md](../techniques/evaluation/property-invariants/TECHNIQUE.md) |
| [AOA-T-0032](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md) - context-report-for-ci | `evaluation` | `promoted` | `5` | [TECHNIQUE.md](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md) |
| [AOA-T-0037](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md) - contextual-host-doctor | `evaluation` | `promoted` | `5` | [TECHNIQUE.md](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md) |
| [AOA-T-0039](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) - baseline-first-additive-profile-benchmarks | `evaluation` | `promoted` | `5` | [TECHNIQUE.md](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) |
| [AOA-T-0042](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md) - upstream-skill-health-checking | `evaluation` | `promoted` | `5` | [TECHNIQUE.md](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md) |
| [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) - session-capture-as-repo-artifact | `history` | `promoted` | `5` | [TECHNIQUE.md](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) |
| [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) - versionable-session-transcripts | `history` | `promoted` | `5` | [TECHNIQUE.md](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) |
| [AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) - witness-trace-as-reviewable-artifact | `history` | `promoted` | `5` | [TECHNIQUE.md](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) |

## `Core procedure`

| technique | domain | status | section order | source |
|---|---|---|---|---|
| [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) - plan-diff-apply-verify-report | `agent-workflows` | `canonical` | `6` | [TECHNIQUE.md](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) |
| [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) - intent-plan-dry-run-contract-chain | `agent-workflows` | `canonical` | `6` | [TECHNIQUE.md](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) |
| [AOA-T-0014](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) - tdd-slice | `agent-workflows` | `canonical` | `6` | [TECHNIQUE.md](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) |
| [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) - new-intent-rollout-checklist | `agent-workflows` | `promoted` | `6` | [TECHNIQUE.md](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) |
| [AOA-T-0023](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) - stateless-single-shot-agent | `agent-workflows` | `promoted` | `6` | [TECHNIQUE.md](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) |
| [AOA-T-0028](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) - confirmation-gated-mutating-action | `agent-workflows` | `promoted` | `6` | [TECHNIQUE.md](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) |
| [AOA-T-0031](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) - shell-composable-agent-invocation | `agent-workflows` | `promoted` | `6` | [TECHNIQUE.md](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) |
| [AOA-T-0036](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md) - render-truth-before-startup | `agent-workflows` | `promoted` | `6` | [TECHNIQUE.md](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md) |
| [AOA-T-0038](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) - one-command-service-lifecycle | `agent-workflows` | `promoted` | `6` | [TECHNIQUE.md](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) |
| [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) - source-of-truth-layout | `docs` | `canonical` | `6` | [TECHNIQUE.md](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) |
| [AOA-T-0009](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) - lightweight-status-snapshot | `docs` | `canonical` | `6` | [TECHNIQUE.md](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) |
| [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) - deterministic-context-composition | `docs` | `canonical` | `6` | [TECHNIQUE.md](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) |
| [AOA-T-0016](../techniques/docs/bounded-context-map/TECHNIQUE.md) - bounded-context-map | `docs` | `canonical` | `6` | [TECHNIQUE.md](../techniques/docs/bounded-context-map/TECHNIQUE.md) |
| [AOA-T-0019](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) - frontmatter-metadata-spine | `docs` | `canonical` | `6` | [TECHNIQUE.md](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) |
| [AOA-T-0021](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) - bounded-relation-lift-for-kag | `docs` | `canonical` | `6` | [TECHNIQUE.md](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) |
| [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) - single-source-rule-distribution | `docs` | `promoted` | `6` | [TECHNIQUE.md](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) |
| [AOA-T-0018](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) - markdown-technique-section-lift | `docs` | `promoted` | `6` | [TECHNIQUE.md](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) |
| [AOA-T-0020](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) - evidence-note-provenance-lift | `docs` | `promoted` | `6` | [TECHNIQUE.md](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) |
| [AOA-T-0022](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) - risk-and-negative-effect-lift | `docs` | `promoted` | `6` | [TECHNIQUE.md](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) |
| [AOA-T-0024](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) - upstream-mirroring-with-provenance | `docs` | `promoted` | `6` | [TECHNIQUE.md](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) |
| [AOA-T-0025](../techniques/docs/capability-spec-versioning/TECHNIQUE.md) - capability-spec-versioning | `docs` | `promoted` | `6` | [TECHNIQUE.md](../techniques/docs/capability-spec-versioning/TECHNIQUE.md) |
| [AOA-T-0027](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) - cross-agent-skill-propagation | `docs` | `promoted` | `6` | [TECHNIQUE.md](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) |
| [AOA-T-0029](../techniques/docs/nested-rule-loading/TECHNIQUE.md) - nested-rule-loading | `docs` | `promoted` | `6` | [TECHNIQUE.md](../techniques/docs/nested-rule-loading/TECHNIQUE.md) |
| [AOA-T-0030](../techniques/docs/fragmented-agent-context/TECHNIQUE.md) - fragmented-agent-context | `docs` | `promoted` | `6` | [TECHNIQUE.md](../techniques/docs/fragmented-agent-context/TECHNIQUE.md) |
| [AOA-T-0033](../techniques/docs/decision-rationale-recording/TECHNIQUE.md) - decision-rationale-recording | `docs` | `promoted` | `6` | [TECHNIQUE.md](../techniques/docs/decision-rationale-recording/TECHNIQUE.md) |
| [AOA-T-0034](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md) - public-safe-artifact-sanitization | `docs` | `promoted` | `6` | [TECHNIQUE.md](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md) |
| [AOA-T-0035](../techniques/docs/profile-preset-composition/TECHNIQUE.md) - profile-preset-composition | `docs` | `promoted` | `6` | [TECHNIQUE.md](../techniques/docs/profile-preset-composition/TECHNIQUE.md) |
| [AOA-T-0040](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md) - skill-vs-command-boundary | `docs` | `promoted` | `6` | [TECHNIQUE.md](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md) |
| [AOA-T-0041](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) - skill-marketplace-curation | `docs` | `promoted` | `6` | [TECHNIQUE.md](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) |
| [AOA-T-0043](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md) - multi-source-primary-input-provenance | `docs` | `promoted` | `6` | [TECHNIQUE.md](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md) |
| [AOA-T-0003](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) - contract-first-smoke-summary | `evaluation` | `canonical` | `6` | [TECHNIQUE.md](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) |
| [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) - latest-alias-plus-history-copy | `evaluation` | `canonical` | `6` | [TECHNIQUE.md](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) |
| [AOA-T-0007](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) - signal-first-gate-promotion | `evaluation` | `canonical` | `6` | [TECHNIQUE.md](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) |
| [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) - published-summary-remediation-snapshot | `evaluation` | `canonical` | `6` | [TECHNIQUE.md](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) |
| [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) - telemetry-integrity-snapshot | `evaluation` | `canonical` | `6` | [TECHNIQUE.md](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) |
| [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) - required-vs-optional-source-rendering | `evaluation` | `canonical` | `6` | [TECHNIQUE.md](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) |
| [AOA-T-0015](../techniques/evaluation/contract-test-design/TECHNIQUE.md) - contract-test-design | `evaluation` | `canonical` | `6` | [TECHNIQUE.md](../techniques/evaluation/contract-test-design/TECHNIQUE.md) |
| [AOA-T-0017](../techniques/evaluation/property-invariants/TECHNIQUE.md) - property-invariants | `evaluation` | `canonical` | `6` | [TECHNIQUE.md](../techniques/evaluation/property-invariants/TECHNIQUE.md) |
| [AOA-T-0032](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md) - context-report-for-ci | `evaluation` | `promoted` | `6` | [TECHNIQUE.md](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md) |
| [AOA-T-0037](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md) - contextual-host-doctor | `evaluation` | `promoted` | `6` | [TECHNIQUE.md](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md) |
| [AOA-T-0039](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) - baseline-first-additive-profile-benchmarks | `evaluation` | `promoted` | `6` | [TECHNIQUE.md](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) |
| [AOA-T-0042](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md) - upstream-skill-health-checking | `evaluation` | `promoted` | `6` | [TECHNIQUE.md](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md) |
| [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) - session-capture-as-repo-artifact | `history` | `promoted` | `6` | [TECHNIQUE.md](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) |
| [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) - versionable-session-transcripts | `history` | `promoted` | `6` | [TECHNIQUE.md](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) |
| [AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) - witness-trace-as-reviewable-artifact | `history` | `promoted` | `6` | [TECHNIQUE.md](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) |

## `Contracts`

| technique | domain | status | section order | source |
|---|---|---|---|---|
| [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) - plan-diff-apply-verify-report | `agent-workflows` | `canonical` | `7` | [TECHNIQUE.md](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) |
| [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) - intent-plan-dry-run-contract-chain | `agent-workflows` | `canonical` | `7` | [TECHNIQUE.md](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) |
| [AOA-T-0014](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) - tdd-slice | `agent-workflows` | `canonical` | `7` | [TECHNIQUE.md](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) |
| [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) - new-intent-rollout-checklist | `agent-workflows` | `promoted` | `7` | [TECHNIQUE.md](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) |
| [AOA-T-0023](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) - stateless-single-shot-agent | `agent-workflows` | `promoted` | `7` | [TECHNIQUE.md](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) |
| [AOA-T-0028](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) - confirmation-gated-mutating-action | `agent-workflows` | `promoted` | `7` | [TECHNIQUE.md](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) |
| [AOA-T-0031](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) - shell-composable-agent-invocation | `agent-workflows` | `promoted` | `7` | [TECHNIQUE.md](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) |
| [AOA-T-0036](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md) - render-truth-before-startup | `agent-workflows` | `promoted` | `7` | [TECHNIQUE.md](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md) |
| [AOA-T-0038](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) - one-command-service-lifecycle | `agent-workflows` | `promoted` | `7` | [TECHNIQUE.md](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) |
| [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) - source-of-truth-layout | `docs` | `canonical` | `7` | [TECHNIQUE.md](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) |
| [AOA-T-0009](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) - lightweight-status-snapshot | `docs` | `canonical` | `7` | [TECHNIQUE.md](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) |
| [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) - deterministic-context-composition | `docs` | `canonical` | `7` | [TECHNIQUE.md](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) |
| [AOA-T-0016](../techniques/docs/bounded-context-map/TECHNIQUE.md) - bounded-context-map | `docs` | `canonical` | `7` | [TECHNIQUE.md](../techniques/docs/bounded-context-map/TECHNIQUE.md) |
| [AOA-T-0019](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) - frontmatter-metadata-spine | `docs` | `canonical` | `7` | [TECHNIQUE.md](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) |
| [AOA-T-0021](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) - bounded-relation-lift-for-kag | `docs` | `canonical` | `7` | [TECHNIQUE.md](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) |
| [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) - single-source-rule-distribution | `docs` | `promoted` | `7` | [TECHNIQUE.md](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) |
| [AOA-T-0018](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) - markdown-technique-section-lift | `docs` | `promoted` | `7` | [TECHNIQUE.md](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) |
| [AOA-T-0020](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) - evidence-note-provenance-lift | `docs` | `promoted` | `7` | [TECHNIQUE.md](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) |
| [AOA-T-0022](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) - risk-and-negative-effect-lift | `docs` | `promoted` | `7` | [TECHNIQUE.md](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) |
| [AOA-T-0024](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) - upstream-mirroring-with-provenance | `docs` | `promoted` | `7` | [TECHNIQUE.md](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) |
| [AOA-T-0025](../techniques/docs/capability-spec-versioning/TECHNIQUE.md) - capability-spec-versioning | `docs` | `promoted` | `7` | [TECHNIQUE.md](../techniques/docs/capability-spec-versioning/TECHNIQUE.md) |
| [AOA-T-0027](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) - cross-agent-skill-propagation | `docs` | `promoted` | `7` | [TECHNIQUE.md](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) |
| [AOA-T-0029](../techniques/docs/nested-rule-loading/TECHNIQUE.md) - nested-rule-loading | `docs` | `promoted` | `7` | [TECHNIQUE.md](../techniques/docs/nested-rule-loading/TECHNIQUE.md) |
| [AOA-T-0030](../techniques/docs/fragmented-agent-context/TECHNIQUE.md) - fragmented-agent-context | `docs` | `promoted` | `7` | [TECHNIQUE.md](../techniques/docs/fragmented-agent-context/TECHNIQUE.md) |
| [AOA-T-0033](../techniques/docs/decision-rationale-recording/TECHNIQUE.md) - decision-rationale-recording | `docs` | `promoted` | `7` | [TECHNIQUE.md](../techniques/docs/decision-rationale-recording/TECHNIQUE.md) |
| [AOA-T-0034](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md) - public-safe-artifact-sanitization | `docs` | `promoted` | `7` | [TECHNIQUE.md](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md) |
| [AOA-T-0035](../techniques/docs/profile-preset-composition/TECHNIQUE.md) - profile-preset-composition | `docs` | `promoted` | `7` | [TECHNIQUE.md](../techniques/docs/profile-preset-composition/TECHNIQUE.md) |
| [AOA-T-0040](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md) - skill-vs-command-boundary | `docs` | `promoted` | `7` | [TECHNIQUE.md](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md) |
| [AOA-T-0041](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) - skill-marketplace-curation | `docs` | `promoted` | `7` | [TECHNIQUE.md](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) |
| [AOA-T-0043](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md) - multi-source-primary-input-provenance | `docs` | `promoted` | `7` | [TECHNIQUE.md](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md) |
| [AOA-T-0003](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) - contract-first-smoke-summary | `evaluation` | `canonical` | `7` | [TECHNIQUE.md](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) |
| [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) - latest-alias-plus-history-copy | `evaluation` | `canonical` | `7` | [TECHNIQUE.md](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) |
| [AOA-T-0007](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) - signal-first-gate-promotion | `evaluation` | `canonical` | `7` | [TECHNIQUE.md](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) |
| [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) - published-summary-remediation-snapshot | `evaluation` | `canonical` | `7` | [TECHNIQUE.md](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) |
| [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) - telemetry-integrity-snapshot | `evaluation` | `canonical` | `7` | [TECHNIQUE.md](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) |
| [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) - required-vs-optional-source-rendering | `evaluation` | `canonical` | `7` | [TECHNIQUE.md](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) |
| [AOA-T-0015](../techniques/evaluation/contract-test-design/TECHNIQUE.md) - contract-test-design | `evaluation` | `canonical` | `7` | [TECHNIQUE.md](../techniques/evaluation/contract-test-design/TECHNIQUE.md) |
| [AOA-T-0017](../techniques/evaluation/property-invariants/TECHNIQUE.md) - property-invariants | `evaluation` | `canonical` | `7` | [TECHNIQUE.md](../techniques/evaluation/property-invariants/TECHNIQUE.md) |
| [AOA-T-0032](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md) - context-report-for-ci | `evaluation` | `promoted` | `7` | [TECHNIQUE.md](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md) |
| [AOA-T-0037](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md) - contextual-host-doctor | `evaluation` | `promoted` | `7` | [TECHNIQUE.md](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md) |
| [AOA-T-0039](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) - baseline-first-additive-profile-benchmarks | `evaluation` | `promoted` | `7` | [TECHNIQUE.md](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) |
| [AOA-T-0042](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md) - upstream-skill-health-checking | `evaluation` | `promoted` | `7` | [TECHNIQUE.md](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md) |
| [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) - session-capture-as-repo-artifact | `history` | `promoted` | `7` | [TECHNIQUE.md](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) |
| [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) - versionable-session-transcripts | `history` | `promoted` | `7` | [TECHNIQUE.md](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) |
| [AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) - witness-trace-as-reviewable-artifact | `history` | `promoted` | `7` | [TECHNIQUE.md](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) |

## `Risks`

| technique | domain | status | section order | source |
|---|---|---|---|---|
| [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) - plan-diff-apply-verify-report | `agent-workflows` | `canonical` | `8` | [TECHNIQUE.md](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) |
| [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) - intent-plan-dry-run-contract-chain | `agent-workflows` | `canonical` | `8` | [TECHNIQUE.md](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) |
| [AOA-T-0014](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) - tdd-slice | `agent-workflows` | `canonical` | `8` | [TECHNIQUE.md](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) |
| [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) - new-intent-rollout-checklist | `agent-workflows` | `promoted` | `8` | [TECHNIQUE.md](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) |
| [AOA-T-0023](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) - stateless-single-shot-agent | `agent-workflows` | `promoted` | `8` | [TECHNIQUE.md](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) |
| [AOA-T-0028](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) - confirmation-gated-mutating-action | `agent-workflows` | `promoted` | `8` | [TECHNIQUE.md](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) |
| [AOA-T-0031](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) - shell-composable-agent-invocation | `agent-workflows` | `promoted` | `8` | [TECHNIQUE.md](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) |
| [AOA-T-0036](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md) - render-truth-before-startup | `agent-workflows` | `promoted` | `8` | [TECHNIQUE.md](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md) |
| [AOA-T-0038](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) - one-command-service-lifecycle | `agent-workflows` | `promoted` | `8` | [TECHNIQUE.md](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) |
| [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) - source-of-truth-layout | `docs` | `canonical` | `8` | [TECHNIQUE.md](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) |
| [AOA-T-0009](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) - lightweight-status-snapshot | `docs` | `canonical` | `8` | [TECHNIQUE.md](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) |
| [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) - deterministic-context-composition | `docs` | `canonical` | `8` | [TECHNIQUE.md](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) |
| [AOA-T-0016](../techniques/docs/bounded-context-map/TECHNIQUE.md) - bounded-context-map | `docs` | `canonical` | `8` | [TECHNIQUE.md](../techniques/docs/bounded-context-map/TECHNIQUE.md) |
| [AOA-T-0019](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) - frontmatter-metadata-spine | `docs` | `canonical` | `8` | [TECHNIQUE.md](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) |
| [AOA-T-0021](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) - bounded-relation-lift-for-kag | `docs` | `canonical` | `8` | [TECHNIQUE.md](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) |
| [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) - single-source-rule-distribution | `docs` | `promoted` | `8` | [TECHNIQUE.md](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) |
| [AOA-T-0018](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) - markdown-technique-section-lift | `docs` | `promoted` | `8` | [TECHNIQUE.md](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) |
| [AOA-T-0020](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) - evidence-note-provenance-lift | `docs` | `promoted` | `8` | [TECHNIQUE.md](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) |
| [AOA-T-0022](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) - risk-and-negative-effect-lift | `docs` | `promoted` | `8` | [TECHNIQUE.md](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) |
| [AOA-T-0024](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) - upstream-mirroring-with-provenance | `docs` | `promoted` | `8` | [TECHNIQUE.md](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) |
| [AOA-T-0025](../techniques/docs/capability-spec-versioning/TECHNIQUE.md) - capability-spec-versioning | `docs` | `promoted` | `8` | [TECHNIQUE.md](../techniques/docs/capability-spec-versioning/TECHNIQUE.md) |
| [AOA-T-0027](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) - cross-agent-skill-propagation | `docs` | `promoted` | `8` | [TECHNIQUE.md](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) |
| [AOA-T-0029](../techniques/docs/nested-rule-loading/TECHNIQUE.md) - nested-rule-loading | `docs` | `promoted` | `8` | [TECHNIQUE.md](../techniques/docs/nested-rule-loading/TECHNIQUE.md) |
| [AOA-T-0030](../techniques/docs/fragmented-agent-context/TECHNIQUE.md) - fragmented-agent-context | `docs` | `promoted` | `8` | [TECHNIQUE.md](../techniques/docs/fragmented-agent-context/TECHNIQUE.md) |
| [AOA-T-0033](../techniques/docs/decision-rationale-recording/TECHNIQUE.md) - decision-rationale-recording | `docs` | `promoted` | `8` | [TECHNIQUE.md](../techniques/docs/decision-rationale-recording/TECHNIQUE.md) |
| [AOA-T-0034](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md) - public-safe-artifact-sanitization | `docs` | `promoted` | `8` | [TECHNIQUE.md](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md) |
| [AOA-T-0035](../techniques/docs/profile-preset-composition/TECHNIQUE.md) - profile-preset-composition | `docs` | `promoted` | `8` | [TECHNIQUE.md](../techniques/docs/profile-preset-composition/TECHNIQUE.md) |
| [AOA-T-0040](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md) - skill-vs-command-boundary | `docs` | `promoted` | `8` | [TECHNIQUE.md](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md) |
| [AOA-T-0041](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) - skill-marketplace-curation | `docs` | `promoted` | `8` | [TECHNIQUE.md](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) |
| [AOA-T-0043](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md) - multi-source-primary-input-provenance | `docs` | `promoted` | `8` | [TECHNIQUE.md](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md) |
| [AOA-T-0003](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) - contract-first-smoke-summary | `evaluation` | `canonical` | `8` | [TECHNIQUE.md](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) |
| [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) - latest-alias-plus-history-copy | `evaluation` | `canonical` | `8` | [TECHNIQUE.md](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) |
| [AOA-T-0007](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) - signal-first-gate-promotion | `evaluation` | `canonical` | `8` | [TECHNIQUE.md](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) |
| [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) - published-summary-remediation-snapshot | `evaluation` | `canonical` | `8` | [TECHNIQUE.md](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) |
| [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) - telemetry-integrity-snapshot | `evaluation` | `canonical` | `8` | [TECHNIQUE.md](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) |
| [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) - required-vs-optional-source-rendering | `evaluation` | `canonical` | `8` | [TECHNIQUE.md](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) |
| [AOA-T-0015](../techniques/evaluation/contract-test-design/TECHNIQUE.md) - contract-test-design | `evaluation` | `canonical` | `8` | [TECHNIQUE.md](../techniques/evaluation/contract-test-design/TECHNIQUE.md) |
| [AOA-T-0017](../techniques/evaluation/property-invariants/TECHNIQUE.md) - property-invariants | `evaluation` | `canonical` | `8` | [TECHNIQUE.md](../techniques/evaluation/property-invariants/TECHNIQUE.md) |
| [AOA-T-0032](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md) - context-report-for-ci | `evaluation` | `promoted` | `8` | [TECHNIQUE.md](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md) |
| [AOA-T-0037](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md) - contextual-host-doctor | `evaluation` | `promoted` | `8` | [TECHNIQUE.md](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md) |
| [AOA-T-0039](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) - baseline-first-additive-profile-benchmarks | `evaluation` | `promoted` | `8` | [TECHNIQUE.md](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) |
| [AOA-T-0042](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md) - upstream-skill-health-checking | `evaluation` | `promoted` | `8` | [TECHNIQUE.md](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md) |
| [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) - session-capture-as-repo-artifact | `history` | `promoted` | `8` | [TECHNIQUE.md](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) |
| [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) - versionable-session-transcripts | `history` | `promoted` | `8` | [TECHNIQUE.md](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) |
| [AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) - witness-trace-as-reviewable-artifact | `history` | `promoted` | `8` | [TECHNIQUE.md](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) |

## `Validation`

| technique | domain | status | section order | source |
|---|---|---|---|---|
| [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) - plan-diff-apply-verify-report | `agent-workflows` | `canonical` | `9` | [TECHNIQUE.md](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) |
| [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) - intent-plan-dry-run-contract-chain | `agent-workflows` | `canonical` | `9` | [TECHNIQUE.md](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) |
| [AOA-T-0014](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) - tdd-slice | `agent-workflows` | `canonical` | `9` | [TECHNIQUE.md](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) |
| [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) - new-intent-rollout-checklist | `agent-workflows` | `promoted` | `9` | [TECHNIQUE.md](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) |
| [AOA-T-0023](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) - stateless-single-shot-agent | `agent-workflows` | `promoted` | `9` | [TECHNIQUE.md](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) |
| [AOA-T-0028](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) - confirmation-gated-mutating-action | `agent-workflows` | `promoted` | `9` | [TECHNIQUE.md](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) |
| [AOA-T-0031](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) - shell-composable-agent-invocation | `agent-workflows` | `promoted` | `9` | [TECHNIQUE.md](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) |
| [AOA-T-0036](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md) - render-truth-before-startup | `agent-workflows` | `promoted` | `9` | [TECHNIQUE.md](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md) |
| [AOA-T-0038](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) - one-command-service-lifecycle | `agent-workflows` | `promoted` | `9` | [TECHNIQUE.md](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) |
| [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) - source-of-truth-layout | `docs` | `canonical` | `9` | [TECHNIQUE.md](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) |
| [AOA-T-0009](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) - lightweight-status-snapshot | `docs` | `canonical` | `9` | [TECHNIQUE.md](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) |
| [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) - deterministic-context-composition | `docs` | `canonical` | `9` | [TECHNIQUE.md](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) |
| [AOA-T-0016](../techniques/docs/bounded-context-map/TECHNIQUE.md) - bounded-context-map | `docs` | `canonical` | `9` | [TECHNIQUE.md](../techniques/docs/bounded-context-map/TECHNIQUE.md) |
| [AOA-T-0019](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) - frontmatter-metadata-spine | `docs` | `canonical` | `9` | [TECHNIQUE.md](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) |
| [AOA-T-0021](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) - bounded-relation-lift-for-kag | `docs` | `canonical` | `9` | [TECHNIQUE.md](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) |
| [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) - single-source-rule-distribution | `docs` | `promoted` | `9` | [TECHNIQUE.md](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) |
| [AOA-T-0018](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) - markdown-technique-section-lift | `docs` | `promoted` | `9` | [TECHNIQUE.md](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) |
| [AOA-T-0020](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) - evidence-note-provenance-lift | `docs` | `promoted` | `9` | [TECHNIQUE.md](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) |
| [AOA-T-0022](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) - risk-and-negative-effect-lift | `docs` | `promoted` | `9` | [TECHNIQUE.md](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) |
| [AOA-T-0024](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) - upstream-mirroring-with-provenance | `docs` | `promoted` | `9` | [TECHNIQUE.md](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) |
| [AOA-T-0025](../techniques/docs/capability-spec-versioning/TECHNIQUE.md) - capability-spec-versioning | `docs` | `promoted` | `9` | [TECHNIQUE.md](../techniques/docs/capability-spec-versioning/TECHNIQUE.md) |
| [AOA-T-0027](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) - cross-agent-skill-propagation | `docs` | `promoted` | `9` | [TECHNIQUE.md](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) |
| [AOA-T-0029](../techniques/docs/nested-rule-loading/TECHNIQUE.md) - nested-rule-loading | `docs` | `promoted` | `9` | [TECHNIQUE.md](../techniques/docs/nested-rule-loading/TECHNIQUE.md) |
| [AOA-T-0030](../techniques/docs/fragmented-agent-context/TECHNIQUE.md) - fragmented-agent-context | `docs` | `promoted` | `9` | [TECHNIQUE.md](../techniques/docs/fragmented-agent-context/TECHNIQUE.md) |
| [AOA-T-0033](../techniques/docs/decision-rationale-recording/TECHNIQUE.md) - decision-rationale-recording | `docs` | `promoted` | `9` | [TECHNIQUE.md](../techniques/docs/decision-rationale-recording/TECHNIQUE.md) |
| [AOA-T-0034](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md) - public-safe-artifact-sanitization | `docs` | `promoted` | `9` | [TECHNIQUE.md](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md) |
| [AOA-T-0035](../techniques/docs/profile-preset-composition/TECHNIQUE.md) - profile-preset-composition | `docs` | `promoted` | `9` | [TECHNIQUE.md](../techniques/docs/profile-preset-composition/TECHNIQUE.md) |
| [AOA-T-0040](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md) - skill-vs-command-boundary | `docs` | `promoted` | `9` | [TECHNIQUE.md](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md) |
| [AOA-T-0041](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) - skill-marketplace-curation | `docs` | `promoted` | `9` | [TECHNIQUE.md](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) |
| [AOA-T-0043](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md) - multi-source-primary-input-provenance | `docs` | `promoted` | `9` | [TECHNIQUE.md](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md) |
| [AOA-T-0003](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) - contract-first-smoke-summary | `evaluation` | `canonical` | `9` | [TECHNIQUE.md](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) |
| [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) - latest-alias-plus-history-copy | `evaluation` | `canonical` | `9` | [TECHNIQUE.md](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) |
| [AOA-T-0007](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) - signal-first-gate-promotion | `evaluation` | `canonical` | `9` | [TECHNIQUE.md](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) |
| [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) - published-summary-remediation-snapshot | `evaluation` | `canonical` | `9` | [TECHNIQUE.md](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) |
| [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) - telemetry-integrity-snapshot | `evaluation` | `canonical` | `9` | [TECHNIQUE.md](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) |
| [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) - required-vs-optional-source-rendering | `evaluation` | `canonical` | `9` | [TECHNIQUE.md](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) |
| [AOA-T-0015](../techniques/evaluation/contract-test-design/TECHNIQUE.md) - contract-test-design | `evaluation` | `canonical` | `9` | [TECHNIQUE.md](../techniques/evaluation/contract-test-design/TECHNIQUE.md) |
| [AOA-T-0017](../techniques/evaluation/property-invariants/TECHNIQUE.md) - property-invariants | `evaluation` | `canonical` | `9` | [TECHNIQUE.md](../techniques/evaluation/property-invariants/TECHNIQUE.md) |
| [AOA-T-0032](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md) - context-report-for-ci | `evaluation` | `promoted` | `9` | [TECHNIQUE.md](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md) |
| [AOA-T-0037](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md) - contextual-host-doctor | `evaluation` | `promoted` | `9` | [TECHNIQUE.md](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md) |
| [AOA-T-0039](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) - baseline-first-additive-profile-benchmarks | `evaluation` | `promoted` | `9` | [TECHNIQUE.md](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) |
| [AOA-T-0042](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md) - upstream-skill-health-checking | `evaluation` | `promoted` | `9` | [TECHNIQUE.md](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md) |
| [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) - session-capture-as-repo-artifact | `history` | `promoted` | `9` | [TECHNIQUE.md](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) |
| [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) - versionable-session-transcripts | `history` | `promoted` | `9` | [TECHNIQUE.md](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) |
| [AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) - witness-trace-as-reviewable-artifact | `history` | `promoted` | `9` | [TECHNIQUE.md](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) |

## `Adaptation notes`

| technique | domain | status | section order | source |
|---|---|---|---|---|
| [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) - plan-diff-apply-verify-report | `agent-workflows` | `canonical` | `10` | [TECHNIQUE.md](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) |
| [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) - intent-plan-dry-run-contract-chain | `agent-workflows` | `canonical` | `10` | [TECHNIQUE.md](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) |
| [AOA-T-0014](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) - tdd-slice | `agent-workflows` | `canonical` | `10` | [TECHNIQUE.md](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) |
| [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) - new-intent-rollout-checklist | `agent-workflows` | `promoted` | `10` | [TECHNIQUE.md](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) |
| [AOA-T-0023](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) - stateless-single-shot-agent | `agent-workflows` | `promoted` | `10` | [TECHNIQUE.md](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) |
| [AOA-T-0028](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) - confirmation-gated-mutating-action | `agent-workflows` | `promoted` | `10` | [TECHNIQUE.md](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) |
| [AOA-T-0031](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) - shell-composable-agent-invocation | `agent-workflows` | `promoted` | `10` | [TECHNIQUE.md](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) |
| [AOA-T-0036](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md) - render-truth-before-startup | `agent-workflows` | `promoted` | `10` | [TECHNIQUE.md](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md) |
| [AOA-T-0038](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) - one-command-service-lifecycle | `agent-workflows` | `promoted` | `10` | [TECHNIQUE.md](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) |
| [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) - source-of-truth-layout | `docs` | `canonical` | `10` | [TECHNIQUE.md](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) |
| [AOA-T-0009](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) - lightweight-status-snapshot | `docs` | `canonical` | `10` | [TECHNIQUE.md](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) |
| [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) - deterministic-context-composition | `docs` | `canonical` | `10` | [TECHNIQUE.md](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) |
| [AOA-T-0016](../techniques/docs/bounded-context-map/TECHNIQUE.md) - bounded-context-map | `docs` | `canonical` | `10` | [TECHNIQUE.md](../techniques/docs/bounded-context-map/TECHNIQUE.md) |
| [AOA-T-0019](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) - frontmatter-metadata-spine | `docs` | `canonical` | `10` | [TECHNIQUE.md](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) |
| [AOA-T-0021](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) - bounded-relation-lift-for-kag | `docs` | `canonical` | `10` | [TECHNIQUE.md](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) |
| [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) - single-source-rule-distribution | `docs` | `promoted` | `10` | [TECHNIQUE.md](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) |
| [AOA-T-0018](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) - markdown-technique-section-lift | `docs` | `promoted` | `10` | [TECHNIQUE.md](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) |
| [AOA-T-0020](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) - evidence-note-provenance-lift | `docs` | `promoted` | `10` | [TECHNIQUE.md](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) |
| [AOA-T-0022](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) - risk-and-negative-effect-lift | `docs` | `promoted` | `10` | [TECHNIQUE.md](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) |
| [AOA-T-0024](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) - upstream-mirroring-with-provenance | `docs` | `promoted` | `10` | [TECHNIQUE.md](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) |
| [AOA-T-0025](../techniques/docs/capability-spec-versioning/TECHNIQUE.md) - capability-spec-versioning | `docs` | `promoted` | `10` | [TECHNIQUE.md](../techniques/docs/capability-spec-versioning/TECHNIQUE.md) |
| [AOA-T-0027](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) - cross-agent-skill-propagation | `docs` | `promoted` | `10` | [TECHNIQUE.md](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) |
| [AOA-T-0029](../techniques/docs/nested-rule-loading/TECHNIQUE.md) - nested-rule-loading | `docs` | `promoted` | `10` | [TECHNIQUE.md](../techniques/docs/nested-rule-loading/TECHNIQUE.md) |
| [AOA-T-0030](../techniques/docs/fragmented-agent-context/TECHNIQUE.md) - fragmented-agent-context | `docs` | `promoted` | `10` | [TECHNIQUE.md](../techniques/docs/fragmented-agent-context/TECHNIQUE.md) |
| [AOA-T-0033](../techniques/docs/decision-rationale-recording/TECHNIQUE.md) - decision-rationale-recording | `docs` | `promoted` | `10` | [TECHNIQUE.md](../techniques/docs/decision-rationale-recording/TECHNIQUE.md) |
| [AOA-T-0034](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md) - public-safe-artifact-sanitization | `docs` | `promoted` | `10` | [TECHNIQUE.md](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md) |
| [AOA-T-0035](../techniques/docs/profile-preset-composition/TECHNIQUE.md) - profile-preset-composition | `docs` | `promoted` | `10` | [TECHNIQUE.md](../techniques/docs/profile-preset-composition/TECHNIQUE.md) |
| [AOA-T-0040](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md) - skill-vs-command-boundary | `docs` | `promoted` | `10` | [TECHNIQUE.md](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md) |
| [AOA-T-0041](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) - skill-marketplace-curation | `docs` | `promoted` | `10` | [TECHNIQUE.md](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) |
| [AOA-T-0043](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md) - multi-source-primary-input-provenance | `docs` | `promoted` | `10` | [TECHNIQUE.md](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md) |
| [AOA-T-0003](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) - contract-first-smoke-summary | `evaluation` | `canonical` | `10` | [TECHNIQUE.md](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) |
| [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) - latest-alias-plus-history-copy | `evaluation` | `canonical` | `10` | [TECHNIQUE.md](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) |
| [AOA-T-0007](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) - signal-first-gate-promotion | `evaluation` | `canonical` | `10` | [TECHNIQUE.md](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) |
| [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) - published-summary-remediation-snapshot | `evaluation` | `canonical` | `10` | [TECHNIQUE.md](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) |
| [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) - telemetry-integrity-snapshot | `evaluation` | `canonical` | `10` | [TECHNIQUE.md](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) |
| [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) - required-vs-optional-source-rendering | `evaluation` | `canonical` | `10` | [TECHNIQUE.md](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) |
| [AOA-T-0015](../techniques/evaluation/contract-test-design/TECHNIQUE.md) - contract-test-design | `evaluation` | `canonical` | `10` | [TECHNIQUE.md](../techniques/evaluation/contract-test-design/TECHNIQUE.md) |
| [AOA-T-0017](../techniques/evaluation/property-invariants/TECHNIQUE.md) - property-invariants | `evaluation` | `canonical` | `10` | [TECHNIQUE.md](../techniques/evaluation/property-invariants/TECHNIQUE.md) |
| [AOA-T-0032](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md) - context-report-for-ci | `evaluation` | `promoted` | `10` | [TECHNIQUE.md](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md) |
| [AOA-T-0037](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md) - contextual-host-doctor | `evaluation` | `promoted` | `10` | [TECHNIQUE.md](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md) |
| [AOA-T-0039](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) - baseline-first-additive-profile-benchmarks | `evaluation` | `promoted` | `10` | [TECHNIQUE.md](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) |
| [AOA-T-0042](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md) - upstream-skill-health-checking | `evaluation` | `promoted` | `10` | [TECHNIQUE.md](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md) |
| [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) - session-capture-as-repo-artifact | `history` | `promoted` | `10` | [TECHNIQUE.md](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) |
| [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) - versionable-session-transcripts | `history` | `promoted` | `10` | [TECHNIQUE.md](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) |
| [AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) - witness-trace-as-reviewable-artifact | `history` | `promoted` | `10` | [TECHNIQUE.md](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) |

## Boundaries

- The meaning remains in the authored `TECHNIQUE.md` bundles.
- This surface is for section routing and lookup only.
- This surface does not become section scoring, a section-ID layer, or search or graph behavior.
