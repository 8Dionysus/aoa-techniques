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

### [AOA-T-0023](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) - stateless-single-shot-agent (`canonical`)

| example | body | example path | source |
|---|---|---|---|
| Confirmed Single-Step Action | `present` | `techniques/agent-workflows/stateless-single-shot-agent/examples/confirmed-single-step-action.md` | [TECHNIQUE.md](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) |
| Minimal Stateless Single-Shot Agent | `present` | `techniques/agent-workflows/stateless-single-shot-agent/examples/minimal-stateless-single-shot-agent.md` | [TECHNIQUE.md](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) |

### [AOA-T-0028](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) - confirmation-gated-mutating-action (`canonical`)

| example | body | example path | source |
|---|---|---|---|
| Concrete Confirmed Mutating Action | `present` | `techniques/agent-workflows/confirmation-gated-mutating-action/examples/concrete-confirmed-mutating-action.md` | [TECHNIQUE.md](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) |
| Minimal Confirmation Gated Mutating Action | `present` | `techniques/agent-workflows/confirmation-gated-mutating-action/examples/minimal-confirmation-gated-mutating-action.md` | [TECHNIQUE.md](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) |

### [AOA-T-0031](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) - shell-composable-agent-invocation (`canonical`)

| example | body | example path | source |
|---|---|---|---|
| Concrete Pipe-First Agent Invocation | `present` | `techniques/agent-workflows/shell-composable-agent-invocation/examples/concrete-pipe-first-agent-invocation.md` | [TECHNIQUE.md](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) |
| Concrete Shell Composable Agent Invocation | `present` | `techniques/agent-workflows/shell-composable-agent-invocation/examples/concrete-shell-composable-agent-invocation.md` | [TECHNIQUE.md](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) |
| Minimal Shell-Composable Agent Invocation | `present` | `techniques/agent-workflows/shell-composable-agent-invocation/examples/minimal-shell-composable-agent-invocation.md` | [TECHNIQUE.md](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) |

### [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) - new-intent-rollout-checklist (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Concrete Non-UI Intent Rollout | `present` | `techniques/agent-workflows/new-intent-rollout-checklist/examples/concrete-non-ui-intent-rollout.md` | [TECHNIQUE.md](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) |
| minimal-intent-rollout | `present` | `techniques/agent-workflows/new-intent-rollout-checklist/examples/minimal-intent-rollout.md` | [TECHNIQUE.md](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) |

### [AOA-T-0036](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md) - render-truth-before-startup (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Minimal Render Truth Before Startup | `present` | `techniques/agent-workflows/render-truth-before-startup/examples/minimal-render-truth-before-startup.md` | [TECHNIQUE.md](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md) |

### [AOA-T-0038](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) - one-command-service-lifecycle (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Minimal One-Command Service Lifecycle | `present` | `techniques/agent-workflows/one-command-service-lifecycle/examples/minimal-one-command-service-lifecycle.md` | [TECHNIQUE.md](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) |

### [AOA-T-0049](../techniques/agent-workflows/dependency-aware-task-graph/TECHNIQUE.md) - dependency-aware-task-graph (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Minimal dependency-aware-task-graph example | `present` | `techniques/agent-workflows/dependency-aware-task-graph/examples/minimal-dependency-aware-task-graph.md` | [TECHNIQUE.md](../techniques/agent-workflows/dependency-aware-task-graph/TECHNIQUE.md) |

### [AOA-T-0050](../techniques/agent-workflows/ready-work-from-blocker-graph/TECHNIQUE.md) - ready-work-from-blocker-graph (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Minimal ready-work-from-blocker-graph example | `present` | `techniques/agent-workflows/ready-work-from-blocker-graph/examples/minimal-ready-work-from-blocker-graph.md` | [TECHNIQUE.md](../techniques/agent-workflows/ready-work-from-blocker-graph/TECHNIQUE.md) |

### [AOA-T-0051](../techniques/agent-workflows/commit-triggered-background-review/TECHNIQUE.md) - commit-triggered-background-review (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Minimal commit-triggered-background-review example | `present` | `techniques/agent-workflows/commit-triggered-background-review/examples/minimal-commit-triggered-background-review.md` | [TECHNIQUE.md](../techniques/agent-workflows/commit-triggered-background-review/TECHNIQUE.md) |

### [AOA-T-0052](../techniques/agent-workflows/review-findings-compaction/TECHNIQUE.md) - review-findings-compaction (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Minimal review-findings-compaction example | `present` | `techniques/agent-workflows/review-findings-compaction/examples/minimal-review-findings-compaction.md` | [TECHNIQUE.md](../techniques/agent-workflows/review-findings-compaction/TECHNIQUE.md) |

### [AOA-T-0054](../techniques/agent-workflows/compaction-resilient-skill-loading/TECHNIQUE.md) - compaction-resilient-skill-loading (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Minimal compaction-resilient skill loading | `present` | `techniques/agent-workflows/compaction-resilient-skill-loading/examples/minimal-compaction-resilient-skill-loading.md` | [TECHNIQUE.md](../techniques/agent-workflows/compaction-resilient-skill-loading/TECHNIQUE.md) |

### [AOA-T-0055](../techniques/agent-workflows/requirements-design-tasks-ladder/TECHNIQUE.md) - requirements-design-tasks-ladder (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Minimal requirements-design-tasks ladder | `present` | `techniques/agent-workflows/requirements-design-tasks-ladder/examples/minimal-requirements-design-tasks-ladder.md` | [TECHNIQUE.md](../techniques/agent-workflows/requirements-design-tasks-ladder/TECHNIQUE.md) |

### [AOA-T-0056](../techniques/agent-workflows/channelized-agent-mailbox/TECHNIQUE.md) - channelized-agent-mailbox (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Minimal channelized-agent-mailbox | `present` | `techniques/agent-workflows/channelized-agent-mailbox/examples/minimal-channelized-agent-mailbox.md` | [TECHNIQUE.md](../techniques/agent-workflows/channelized-agent-mailbox/TECHNIQUE.md) |

### [AOA-T-0057](../techniques/agent-workflows/structured-handoff-before-compaction/TECHNIQUE.md) - structured-handoff-before-compaction (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| minimal structured handoff before compaction | `present` | `techniques/agent-workflows/structured-handoff-before-compaction/examples/minimal-structured-handoff-before-compaction.md` | [TECHNIQUE.md](../techniques/agent-workflows/structured-handoff-before-compaction/TECHNIQUE.md) |

### [AOA-T-0058](../techniques/agent-workflows/receipt-confirmed-handoff-packet/TECHNIQUE.md) - receipt-confirmed-handoff-packet (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| minimal receipt-confirmed handoff packet | `present` | `techniques/agent-workflows/receipt-confirmed-handoff-packet/examples/minimal-receipt-confirmed-handoff-packet.md` | [TECHNIQUE.md](../techniques/agent-workflows/receipt-confirmed-handoff-packet/TECHNIQUE.md) |

### [AOA-T-0059](../techniques/agent-workflows/git-verified-handoff-claims/TECHNIQUE.md) - git-verified-handoff-claims (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| minimal git-verified handoff claims | `present` | `techniques/agent-workflows/git-verified-handoff-claims/examples/minimal-git-verified-handoff-claims.md` | [TECHNIQUE.md](../techniques/agent-workflows/git-verified-handoff-claims/TECHNIQUE.md) |

### [AOA-T-0060](../techniques/agent-workflows/session-opening-ritual-before-work/TECHNIQUE.md) - session-opening-ritual-before-work (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| minimal session-opening ritual before work | `present` | `techniques/agent-workflows/session-opening-ritual-before-work/examples/minimal-session-opening-ritual-before-work.md` | [TECHNIQUE.md](../techniques/agent-workflows/session-opening-ritual-before-work/TECHNIQUE.md) |

### [AOA-T-0061](../techniques/agent-workflows/cross-repo-resource-map-bootstrap/TECHNIQUE.md) - cross-repo-resource-map-bootstrap (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| minimal cross-repo resource-map bootstrap | `present` | `techniques/agent-workflows/cross-repo-resource-map-bootstrap/examples/minimal-cross-repo-resource-map-bootstrap.md` | [TECHNIQUE.md](../techniques/agent-workflows/cross-repo-resource-map-bootstrap/TECHNIQUE.md) |

### [AOA-T-0062](../techniques/agent-workflows/episode-bounded-agent-loop/TECHNIQUE.md) - episode-bounded-agent-loop (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| minimal episode-bounded agent loop | `present` | `techniques/agent-workflows/episode-bounded-agent-loop/examples/minimal-episode-bounded-agent-loop.md` | [TECHNIQUE.md](../techniques/agent-workflows/episode-bounded-agent-loop/TECHNIQUE.md) |

### [AOA-T-0065](../techniques/agent-workflows/mcp-gateway-proxy/TECHNIQUE.md) - mcp-gateway-proxy (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| minimal mcp-gateway-proxy | `present` | `techniques/agent-workflows/mcp-gateway-proxy/examples/minimal-mcp-gateway-proxy.md` | [TECHNIQUE.md](../techniques/agent-workflows/mcp-gateway-proxy/TECHNIQUE.md) |

### [AOA-T-0068](../techniques/agent-workflows/fail-closed-evidence-gate/TECHNIQUE.md) - fail-closed-evidence-gate (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| minimal fail-closed-evidence-gate | `present` | `techniques/agent-workflows/fail-closed-evidence-gate/examples/minimal-fail-closed-evidence-gate.md` | [TECHNIQUE.md](../techniques/agent-workflows/fail-closed-evidence-gate/TECHNIQUE.md) |

### [AOA-T-0069](../techniques/agent-workflows/approval-bound-durable-jobs/TECHNIQUE.md) - approval-bound-durable-jobs (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| minimal approval-bound-durable-jobs | `present` | `techniques/agent-workflows/approval-bound-durable-jobs/examples/minimal-approval-bound-durable-jobs.md` | [TECHNIQUE.md](../techniques/agent-workflows/approval-bound-durable-jobs/TECHNIQUE.md) |

### [AOA-T-0070](../techniques/agent-workflows/two-stage-document-ocr-pipeline/TECHNIQUE.md) - two-stage-document-ocr-pipeline (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| minimal-two-stage-document-ocr-pipeline | `present` | `techniques/agent-workflows/two-stage-document-ocr-pipeline/examples/minimal-two-stage-document-ocr-pipeline.md` | [TECHNIQUE.md](../techniques/agent-workflows/two-stage-document-ocr-pipeline/TECHNIQUE.md) |

### [AOA-T-0071](../techniques/agent-workflows/template-backed-field-extraction-after-ocr/TECHNIQUE.md) - template-backed-field-extraction-after-ocr (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| minimal-template-backed-field-extraction-after-ocr | `present` | `techniques/agent-workflows/template-backed-field-extraction-after-ocr/examples/minimal-template-backed-field-extraction-after-ocr.md` | [TECHNIQUE.md](../techniques/agent-workflows/template-backed-field-extraction-after-ocr/TECHNIQUE.md) |

### [AOA-T-0072](../techniques/agent-workflows/perceptual-media-dedupe-with-threshold-review/TECHNIQUE.md) - perceptual-media-dedupe-with-threshold-review (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| minimal-perceptual-media-dedupe-with-threshold-review | `present` | `techniques/agent-workflows/perceptual-media-dedupe-with-threshold-review/examples/minimal-perceptual-media-dedupe-with-threshold-review.md` | [TECHNIQUE.md](../techniques/agent-workflows/perceptual-media-dedupe-with-threshold-review/TECHNIQUE.md) |

### [AOA-T-0073](../techniques/agent-workflows/semantic-media-bucketing-with-vision-plus-ocr/TECHNIQUE.md) - semantic-media-bucketing-with-vision-plus-ocr (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| minimal-semantic-media-bucketing-with-vision-plus-ocr | `present` | `techniques/agent-workflows/semantic-media-bucketing-with-vision-plus-ocr/examples/minimal-semantic-media-bucketing-with-vision-plus-ocr.md` | [TECHNIQUE.md](../techniques/agent-workflows/semantic-media-bucketing-with-vision-plus-ocr/TECHNIQUE.md) |

### [AOA-T-0074](../techniques/agent-workflows/telegram-export-normalization-to-local-store/TECHNIQUE.md) - telegram-export-normalization-to-local-store (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| minimal-telegram-export-normalization-to-local-store | `present` | `techniques/agent-workflows/telegram-export-normalization-to-local-store/examples/minimal-telegram-export-normalization-to-local-store.md` | [TECHNIQUE.md](../techniques/agent-workflows/telegram-export-normalization-to-local-store/TECHNIQUE.md) |

### [AOA-T-0075](../techniques/agent-workflows/session-donor-harvest/TECHNIQUE.md) - session-donor-harvest (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| minimal session-donor-harvest | `present` | `techniques/agent-workflows/session-donor-harvest/examples/minimal-session-donor-harvest.md` | [TECHNIQUE.md](../techniques/agent-workflows/session-donor-harvest/TECHNIQUE.md) |

### [AOA-T-0076](../techniques/agent-workflows/owner-layer-triage/TECHNIQUE.md) - owner-layer-triage (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| minimal owner-layer-triage | `present` | `techniques/agent-workflows/owner-layer-triage/examples/minimal-owner-layer-triage.md` | [TECHNIQUE.md](../techniques/agent-workflows/owner-layer-triage/TECHNIQUE.md) |

### [AOA-T-0077](../techniques/agent-workflows/harvest-packet-contract/TECHNIQUE.md) - harvest-packet-contract (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| minimal harvest-packet-contract | `present` | `techniques/agent-workflows/harvest-packet-contract/examples/minimal-harvest-packet-contract.md` | [TECHNIQUE.md](../techniques/agent-workflows/harvest-packet-contract/TECHNIQUE.md) |

### [AOA-T-0078](../techniques/agent-workflows/decision-fork-cards/TECHNIQUE.md) - decision-fork-cards (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| minimal decision-fork-cards | `present` | `techniques/agent-workflows/decision-fork-cards/examples/minimal-decision-fork-cards.md` | [TECHNIQUE.md](../techniques/agent-workflows/decision-fork-cards/TECHNIQUE.md) |

### [AOA-T-0079](../techniques/agent-workflows/risk-passport-lift/TECHNIQUE.md) - risk-passport-lift (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| minimal risk-passport-lift | `present` | `techniques/agent-workflows/risk-passport-lift/examples/minimal-risk-passport-lift.md` | [TECHNIQUE.md](../techniques/agent-workflows/risk-passport-lift/TECHNIQUE.md) |

### [AOA-T-0080](../techniques/agent-workflows/session-drift-taxonomy/TECHNIQUE.md) - session-drift-taxonomy (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| minimal session-drift-taxonomy | `present` | `techniques/agent-workflows/session-drift-taxonomy/examples/minimal-session-drift-taxonomy.md` | [TECHNIQUE.md](../techniques/agent-workflows/session-drift-taxonomy/TECHNIQUE.md) |

### [AOA-T-0081](../techniques/agent-workflows/diagnosis-from-reviewed-evidence/TECHNIQUE.md) - diagnosis-from-reviewed-evidence (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| minimal diagnosis-from-reviewed-evidence | `present` | `techniques/agent-workflows/diagnosis-from-reviewed-evidence/examples/minimal-diagnosis-from-reviewed-evidence.md` | [TECHNIQUE.md](../techniques/agent-workflows/diagnosis-from-reviewed-evidence/TECHNIQUE.md) |

### [AOA-T-0082](../techniques/agent-workflows/repair-shape-from-diagnosis/TECHNIQUE.md) - repair-shape-from-diagnosis (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| minimal repair-shape-from-diagnosis | `present` | `techniques/agent-workflows/repair-shape-from-diagnosis/examples/minimal-repair-shape-from-diagnosis.md` | [TECHNIQUE.md](../techniques/agent-workflows/repair-shape-from-diagnosis/TECHNIQUE.md) |

### [AOA-T-0083](../techniques/agent-workflows/checkpoint-bound-self-repair/TECHNIQUE.md) - checkpoint-bound-self-repair (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| minimal checkpoint-bound-self-repair | `present` | `techniques/agent-workflows/checkpoint-bound-self-repair/examples/minimal-checkpoint-bound-self-repair.md` | [TECHNIQUE.md](../techniques/agent-workflows/checkpoint-bound-self-repair/TECHNIQUE.md) |

### [AOA-T-0084](../techniques/agent-workflows/progression-evidence-lift/TECHNIQUE.md) - progression-evidence-lift (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| minimal progression-evidence-lift | `present` | `techniques/agent-workflows/progression-evidence-lift/examples/minimal-progression-evidence-lift.md` | [TECHNIQUE.md](../techniques/agent-workflows/progression-evidence-lift/TECHNIQUE.md) |

### [AOA-T-0085](../techniques/agent-workflows/multi-axis-quest-overlay/TECHNIQUE.md) - multi-axis-quest-overlay (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| minimal multi-axis-quest-overlay | `present` | `techniques/agent-workflows/multi-axis-quest-overlay/examples/minimal-multi-axis-quest-overlay.md` | [TECHNIQUE.md](../techniques/agent-workflows/multi-axis-quest-overlay/TECHNIQUE.md) |

### [AOA-T-0086](../techniques/agent-workflows/automation-fit-matrix/TECHNIQUE.md) - automation-fit-matrix (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| minimal automation-fit-matrix | `present` | `techniques/agent-workflows/automation-fit-matrix/examples/minimal-automation-fit-matrix.md` | [TECHNIQUE.md](../techniques/agent-workflows/automation-fit-matrix/TECHNIQUE.md) |

### [AOA-T-0087](../techniques/agent-workflows/human-loop-to-seed-lift/TECHNIQUE.md) - human-loop-to-seed-lift (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| minimal human-loop-to-seed-lift | `present` | `techniques/agent-workflows/human-loop-to-seed-lift/examples/minimal-human-loop-to-seed-lift.md` | [TECHNIQUE.md](../techniques/agent-workflows/human-loop-to-seed-lift/TECHNIQUE.md) |

### [AOA-T-0088](../techniques/agent-workflows/approval-sensitivity-check/TECHNIQUE.md) - approval-sensitivity-check (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| minimal approval-sensitivity-check | `present` | `techniques/agent-workflows/approval-sensitivity-check/examples/minimal-approval-sensitivity-check.md` | [TECHNIQUE.md](../techniques/agent-workflows/approval-sensitivity-check/TECHNIQUE.md) |

### [AOA-T-0089](../techniques/agent-workflows/quest-unit-promotion-review/TECHNIQUE.md) - quest-unit-promotion-review (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| minimal quest-unit-promotion-review | `present` | `techniques/agent-workflows/quest-unit-promotion-review/examples/minimal-quest-unit-promotion-review.md` | [TECHNIQUE.md](../techniques/agent-workflows/quest-unit-promotion-review/TECHNIQUE.md) |

### [AOA-T-0090](../techniques/agent-workflows/nearest-wrong-target-rejection/TECHNIQUE.md) - nearest-wrong-target-rejection (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| minimal nearest-wrong-target-rejection | `present` | `techniques/agent-workflows/nearest-wrong-target-rejection/examples/minimal-nearest-wrong-target-rejection.md` | [TECHNIQUE.md](../techniques/agent-workflows/nearest-wrong-target-rejection/TECHNIQUE.md) |

### [AOA-T-0091](../techniques/agent-workflows/workspace-root-ingress-and-mutation-gate/TECHNIQUE.md) - workspace-root-ingress-and-mutation-gate (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| minimal workspace-root-ingress-and-mutation-gate | `present` | `techniques/agent-workflows/workspace-root-ingress-and-mutation-gate/examples/minimal-workspace-root-ingress-and-mutation-gate.md` | [TECHNIQUE.md](../techniques/agent-workflows/workspace-root-ingress-and-mutation-gate/TECHNIQUE.md) |

### [AOA-T-0092](../techniques/agent-workflows/audit-to-closeout-proof-loop/TECHNIQUE.md) - audit-to-closeout-proof-loop (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Minimal audit-to-closeout-proof-loop example | `present` | `techniques/agent-workflows/audit-to-closeout-proof-loop/examples/minimal-audit-to-closeout-proof-loop.md` | [TECHNIQUE.md](../techniques/agent-workflows/audit-to-closeout-proof-loop/TECHNIQUE.md) |

### [AOA-T-0093](../techniques/agent-workflows/recommendation-truth-vs-host-actionability/TECHNIQUE.md) - recommendation-truth-vs-host-actionability (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| minimal recommendation-truth-vs-host-actionability | `present` | `techniques/agent-workflows/recommendation-truth-vs-host-actionability/examples/minimal-recommendation-truth-vs-host-actionability.md` | [TECHNIQUE.md](../techniques/agent-workflows/recommendation-truth-vs-host-actionability/TECHNIQUE.md) |

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

### [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) - single-source-rule-distribution (`canonical`)

| example | body | example path | source |
|---|---|---|---|
| Concrete Multi-Agent Rule Sync | `present` | `techniques/docs/single-source-rule-distribution/examples/concrete-multi-agent-rule-sync.md` | [TECHNIQUE.md](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) |
| Minimal Single-Source Rule Distribution | `present` | `techniques/docs/single-source-rule-distribution/examples/minimal-single-source-rule-distribution.md` | [TECHNIQUE.md](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) |

### [AOA-T-0016](../techniques/docs/bounded-context-map/TECHNIQUE.md) - bounded-context-map (`canonical`)

| example | body | example path | source |
|---|---|---|---|
| Concrete Infra Context Map | `present` | `techniques/docs/bounded-context-map/examples/concrete-infra-context-map.md` | [TECHNIQUE.md](../techniques/docs/bounded-context-map/TECHNIQUE.md) |
| Minimal Context Boundary Map | `present` | `techniques/docs/bounded-context-map/examples/minimal-context-boundary-map.md` | [TECHNIQUE.md](../techniques/docs/bounded-context-map/TECHNIQUE.md) |

### [AOA-T-0018](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) - markdown-technique-section-lift (`canonical`)

| example | body | example path | source |
|---|---|---|---|
| Minimal Section Lift | `present` | `techniques/docs/markdown-technique-section-lift/examples/minimal-section-lift.md` | [TECHNIQUE.md](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) |

### [AOA-T-0019](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) - frontmatter-metadata-spine (`canonical`)

| example | body | example path | source |
|---|---|---|---|
| Frontmatter To Catalog Entry | `present` | `techniques/docs/frontmatter-metadata-spine/examples/frontmatter-to-catalog-entry.md` | [TECHNIQUE.md](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) |

### [AOA-T-0021](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) - bounded-relation-lift-for-kag (`canonical`)

| example | body | example path | source |
|---|---|---|---|
| Direct Relation To Selection Hint | `present` | `techniques/docs/bounded-relation-lift-for-kag/examples/direct-relation-to-selection-hint.md` | [TECHNIQUE.md](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) |

### [AOA-T-0034](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md) - public-safe-artifact-sanitization (`canonical`)

| example | body | example path | source |
|---|---|---|---|
| Scenario | `present` | `techniques/docs/public-safe-artifact-sanitization/examples/minimal-public-safe-artifact-sanitization.md` | [TECHNIQUE.md](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md) |

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

### [AOA-T-0029](../techniques/docs/nested-rule-loading/TECHNIQUE.md) - nested-rule-loading (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Concrete Hierarchical Rule Loading | `present` | `techniques/docs/nested-rule-loading/examples/concrete-hierarchical-rule-loading.md` | [TECHNIQUE.md](../techniques/docs/nested-rule-loading/TECHNIQUE.md) |
| Minimal Nested Rule Loading | `present` | `techniques/docs/nested-rule-loading/examples/minimal-nested-rule-loading.md` | [TECHNIQUE.md](../techniques/docs/nested-rule-loading/TECHNIQUE.md) |

### [AOA-T-0030](../techniques/docs/fragmented-agent-context/TECHNIQUE.md) - fragmented-agent-context (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Concrete Fragment-First Assembly | `present` | `techniques/docs/fragmented-agent-context/examples/concrete-fragment-first-assembly.md` | [TECHNIQUE.md](../techniques/docs/fragmented-agent-context/TECHNIQUE.md) |
| Concrete Subtree Fragmented Context | `present` | `techniques/docs/fragmented-agent-context/examples/concrete-subtree-fragmented-context.md` | [TECHNIQUE.md](../techniques/docs/fragmented-agent-context/TECHNIQUE.md) |
| Minimal Fragmented Agent Context | `present` | `techniques/docs/fragmented-agent-context/examples/minimal-fragmented-agent-context.md` | [TECHNIQUE.md](../techniques/docs/fragmented-agent-context/TECHNIQUE.md) |

### [AOA-T-0033](../techniques/docs/decision-rationale-recording/TECHNIQUE.md) - decision-rationale-recording (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Minimal Decision Rationale Note | `present` | `techniques/docs/decision-rationale-recording/examples/minimal-decision-rationale-note.md` | [TECHNIQUE.md](../techniques/docs/decision-rationale-recording/TECHNIQUE.md) |

### [AOA-T-0035](../techniques/docs/profile-preset-composition/TECHNIQUE.md) - profile-preset-composition (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Minimal Profile Preset Composition | `present` | `techniques/docs/profile-preset-composition/examples/minimal-profile-preset-composition.md` | [TECHNIQUE.md](../techniques/docs/profile-preset-composition/TECHNIQUE.md) |

### [AOA-T-0040](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md) - skill-vs-command-boundary (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Minimal Skill Vs Command Boundary | `present` | `techniques/docs/skill-vs-command-boundary/examples/minimal-skill-vs-command-boundary.md` | [TECHNIQUE.md](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md) |

### [AOA-T-0041](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) - skill-marketplace-curation (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Minimal Skill Marketplace Curation | `present` | `techniques/docs/skill-marketplace-curation/examples/minimal-skill-marketplace-curation.md` | [TECHNIQUE.md](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) |

### [AOA-T-0043](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md) - multi-source-primary-input-provenance (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Minimal Multi-Source Primary Input Provenance | `present` | `techniques/docs/multi-source-primary-input-provenance/examples/minimal-multi-source-primary-input-provenance.md` | [TECHNIQUE.md](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md) |

### [AOA-T-0046](../techniques/docs/repo-doc-surface-lift/TECHNIQUE.md) - repo-doc-surface-lift (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Minimal Repo Doc Surface Lift | `present` | `techniques/docs/repo-doc-surface-lift/examples/minimal-repo-doc-surface-lift.md` | [TECHNIQUE.md](../techniques/docs/repo-doc-surface-lift/TECHNIQUE.md) |

### [AOA-T-0047](../techniques/docs/github-review-template-lift/TECHNIQUE.md) - github-review-template-lift (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Minimal GitHub Review Template Lift | `present` | `techniques/docs/github-review-template-lift/examples/minimal-github-review-template-lift.md` | [TECHNIQUE.md](../techniques/docs/github-review-template-lift/TECHNIQUE.md) |

### [AOA-T-0048](../techniques/docs/semantic-review-surface-lift/TECHNIQUE.md) - semantic-review-surface-lift (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Minimal Semantic Review Surface Lift | `present` | `techniques/docs/semantic-review-surface-lift/examples/minimal-semantic-review-surface-lift.md` | [TECHNIQUE.md](../techniques/docs/semantic-review-surface-lift/TECHNIQUE.md) |

### [AOA-T-0063](../techniques/docs/versioned-agent-registry-contract/TECHNIQUE.md) - versioned-agent-registry-contract (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| minimal versioned agent-registry contract | `present` | `techniques/docs/versioned-agent-registry-contract/examples/minimal-versioned-agent-registry-contract.md` | [TECHNIQUE.md](../techniques/docs/versioned-agent-registry-contract/TECHNIQUE.md) |

### [AOA-T-0064](../techniques/docs/capability-discovery/TECHNIQUE.md) - capability-discovery (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| minimal capability discovery | `present` | `techniques/docs/capability-discovery/examples/minimal-capability-discovery.md` | [TECHNIQUE.md](../techniques/docs/capability-discovery/TECHNIQUE.md) |

### [AOA-T-0094](../techniques/docs/canonical-owner-with-validated-mirror/TECHNIQUE.md) - canonical-owner-with-validated-mirror (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Minimal Canonical Owner With Validated Mirror | `present` | `techniques/docs/canonical-owner-with-validated-mirror/examples/minimal-canonical-owner-with-validated-mirror.md` | [TECHNIQUE.md](../techniques/docs/canonical-owner-with-validated-mirror/TECHNIQUE.md) |

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

### [AOA-T-0032](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md) - context-report-for-ci (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Concrete Context Composition CI Report | `present` | `techniques/evaluation/context-report-for-ci/examples/concrete-context-composition-ci-report.md` | [TECHNIQUE.md](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md) |
| Minimal Context Report For CI | `present` | `techniques/evaluation/context-report-for-ci/examples/minimal-context-report-for-ci.md` | [TECHNIQUE.md](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md) |

### [AOA-T-0037](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md) - contextual-host-doctor (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Minimal Contextual Host Doctor | `present` | `techniques/evaluation/contextual-host-doctor/examples/minimal-contextual-host-doctor.md` | [TECHNIQUE.md](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md) |

### [AOA-T-0039](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) - baseline-first-additive-profile-benchmarks (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Minimal Baseline First Additive Profile Benchmarks | `present` | `techniques/evaluation/baseline-first-additive-profile-benchmarks/examples/minimal-baseline-first-additive-profile-benchmarks.md` | [TECHNIQUE.md](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) |

### [AOA-T-0042](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md) - upstream-skill-health-checking (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Minimal Upstream Skill Health Checking | `present` | `techniques/evaluation/upstream-skill-health-checking/examples/minimal-upstream-skill-health-checking.md` | [TECHNIQUE.md](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md) |

## `history`

### [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) - versionable-session-transcripts (`canonical`)

| example | body | example path | source |
|---|---|---|---|
| Minimal Versionable Session Transcripts | `present` | `techniques/history/versionable-session-transcripts/examples/minimal-versionable-session-transcripts.md` | [TECHNIQUE.md](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) |

### [AOA-T-0053](../techniques/history/local-first-session-index/TECHNIQUE.md) - local-first-session-index (`canonical`)

| example | body | example path | source |
|---|---|---|---|
| Minimal local-first session index | `present` | `techniques/history/local-first-session-index/examples/minimal-local-first-session-index.md` | [TECHNIQUE.md](../techniques/history/local-first-session-index/TECHNIQUE.md) |

### [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) - session-capture-as-repo-artifact (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Concrete Local-First Session History | `present` | `techniques/history/session-capture-as-repo-artifact/examples/concrete-local-first-session-history.md` | [TECHNIQUE.md](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) |
| Minimal Session Capture As Repo Artifact | `present` | `techniques/history/session-capture-as-repo-artifact/examples/minimal-session-capture-as-repo-artifact.md` | [TECHNIQUE.md](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) |

### [AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) - witness-trace-as-reviewable-artifact (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| Minimal Witness Trace As Reviewable Artifact | `present` | `techniques/history/witness-trace-as-reviewable-artifact/examples/minimal-witness-trace-as-reviewable-artifact.md` | [TECHNIQUE.md](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) |

### [AOA-T-0066](../techniques/history/transcript-replay-artifact/TECHNIQUE.md) - transcript-replay-artifact (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| minimal transcript-replay-artifact | `present` | `techniques/history/transcript-replay-artifact/examples/minimal-transcript-replay-artifact.md` | [TECHNIQUE.md](../techniques/history/transcript-replay-artifact/TECHNIQUE.md) |

### [AOA-T-0067](../techniques/history/transcript-linked-code-lineage/TECHNIQUE.md) - transcript-linked-code-lineage (`promoted`)

| example | body | example path | source |
|---|---|---|---|
| minimal transcript-linked-code-lineage | `present` | `techniques/history/transcript-linked-code-lineage/examples/minimal-transcript-linked-code-lineage.md` | [TECHNIQUE.md](../techniques/history/transcript-linked-code-lineage/TECHNIQUE.md) |

## Boundaries

- The meaning remains in the authored example files and source bundles.
- This surface is derived example knowledge only.
- This surface does not become scenario graphs, executable tests, or richer step extraction.
