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

### [AOA-T-0023](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) - stateless-single-shot-agent (`canonical`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Stateless Single-Shot Agent Checklist | `absent` | `7` | `techniques/agent-workflows/stateless-single-shot-agent/checks/stateless-single-shot-agent-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) |

### [AOA-T-0028](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) - confirmation-gated-mutating-action (`canonical`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Confirmation Gated Mutating Action Checklist | `absent` | `6` | `techniques/agent-workflows/confirmation-gated-mutating-action/checks/confirmation-gated-mutating-action-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) |

### [AOA-T-0031](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) - shell-composable-agent-invocation (`canonical`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Shell-Composable Agent Invocation Checklist | `absent` | `7` | `techniques/agent-workflows/shell-composable-agent-invocation/checks/shell-composable-agent-invocation-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) |

### [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) - new-intent-rollout-checklist (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| intent-rollout-checklist | `absent` | `11` | `techniques/agent-workflows/new-intent-rollout-checklist/checks/intent-rollout-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) |

### [AOA-T-0036](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md) - render-truth-before-startup (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Render Truth Before Startup Checklist | `absent` | `10` | `techniques/agent-workflows/render-truth-before-startup/checks/render-truth-before-startup-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md) |

### [AOA-T-0038](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) - one-command-service-lifecycle (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| One-Command Service Lifecycle Checklist | `absent` | `10` | `techniques/agent-workflows/one-command-service-lifecycle/checks/one-command-service-lifecycle-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) |

### [AOA-T-0049](../techniques/agent-workflows/dependency-aware-task-graph/TECHNIQUE.md) - dependency-aware-task-graph (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| dependency-aware-task-graph checklist | `present` | `8` | `techniques/agent-workflows/dependency-aware-task-graph/checks/dependency-aware-task-graph-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/dependency-aware-task-graph/TECHNIQUE.md) |

### [AOA-T-0050](../techniques/agent-workflows/ready-work-from-blocker-graph/TECHNIQUE.md) - ready-work-from-blocker-graph (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| ready-work-from-blocker-graph checklist | `present` | `8` | `techniques/agent-workflows/ready-work-from-blocker-graph/checks/ready-work-from-blocker-graph-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/ready-work-from-blocker-graph/TECHNIQUE.md) |

### [AOA-T-0051](../techniques/agent-workflows/commit-triggered-background-review/TECHNIQUE.md) - commit-triggered-background-review (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| commit-triggered-background-review checklist | `present` | `8` | `techniques/agent-workflows/commit-triggered-background-review/checks/commit-triggered-background-review-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/commit-triggered-background-review/TECHNIQUE.md) |

### [AOA-T-0052](../techniques/agent-workflows/review-findings-compaction/TECHNIQUE.md) - review-findings-compaction (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| review-findings-compaction checklist | `present` | `8` | `techniques/agent-workflows/review-findings-compaction/checks/review-findings-compaction-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/review-findings-compaction/TECHNIQUE.md) |

### [AOA-T-0054](../techniques/agent-workflows/compaction-resilient-skill-loading/TECHNIQUE.md) - compaction-resilient-skill-loading (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| compaction-resilient-skill-loading checklist | `absent` | `8` | `techniques/agent-workflows/compaction-resilient-skill-loading/checks/compaction-resilient-skill-loading-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/compaction-resilient-skill-loading/TECHNIQUE.md) |

### [AOA-T-0055](../techniques/agent-workflows/requirements-design-tasks-ladder/TECHNIQUE.md) - requirements-design-tasks-ladder (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| requirements-design-tasks-ladder checklist | `absent` | `8` | `techniques/agent-workflows/requirements-design-tasks-ladder/checks/requirements-design-tasks-ladder-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/requirements-design-tasks-ladder/TECHNIQUE.md) |

### [AOA-T-0056](../techniques/agent-workflows/channelized-agent-mailbox/TECHNIQUE.md) - channelized-agent-mailbox (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| channelized-agent-mailbox checklist | `absent` | `8` | `techniques/agent-workflows/channelized-agent-mailbox/checks/channelized-agent-mailbox-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/channelized-agent-mailbox/TECHNIQUE.md) |

### [AOA-T-0057](../techniques/agent-workflows/structured-handoff-before-compaction/TECHNIQUE.md) - structured-handoff-before-compaction (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| structured-handoff-before-compaction checklist | `absent` | `8` | `techniques/agent-workflows/structured-handoff-before-compaction/checks/structured-handoff-before-compaction-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/structured-handoff-before-compaction/TECHNIQUE.md) |

### [AOA-T-0058](../techniques/agent-workflows/receipt-confirmed-handoff-packet/TECHNIQUE.md) - receipt-confirmed-handoff-packet (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| receipt-confirmed-handoff-packet checklist | `absent` | `8` | `techniques/agent-workflows/receipt-confirmed-handoff-packet/checks/receipt-confirmed-handoff-packet-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/receipt-confirmed-handoff-packet/TECHNIQUE.md) |

### [AOA-T-0059](../techniques/agent-workflows/git-verified-handoff-claims/TECHNIQUE.md) - git-verified-handoff-claims (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| git-verified-handoff-claims checklist | `absent` | `8` | `techniques/agent-workflows/git-verified-handoff-claims/checks/git-verified-handoff-claims-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/git-verified-handoff-claims/TECHNIQUE.md) |

### [AOA-T-0060](../techniques/agent-workflows/session-opening-ritual-before-work/TECHNIQUE.md) - session-opening-ritual-before-work (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| session-opening-ritual-before-work checklist | `absent` | `8` | `techniques/agent-workflows/session-opening-ritual-before-work/checks/session-opening-ritual-before-work-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/session-opening-ritual-before-work/TECHNIQUE.md) |

### [AOA-T-0061](../techniques/agent-workflows/cross-repo-resource-map-bootstrap/TECHNIQUE.md) - cross-repo-resource-map-bootstrap (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| cross-repo-resource-map-bootstrap checklist | `absent` | `8` | `techniques/agent-workflows/cross-repo-resource-map-bootstrap/checks/cross-repo-resource-map-bootstrap-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/cross-repo-resource-map-bootstrap/TECHNIQUE.md) |

### [AOA-T-0062](../techniques/agent-workflows/episode-bounded-agent-loop/TECHNIQUE.md) - episode-bounded-agent-loop (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| episode-bounded-agent-loop checklist | `absent` | `8` | `techniques/agent-workflows/episode-bounded-agent-loop/checks/episode-bounded-agent-loop-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/episode-bounded-agent-loop/TECHNIQUE.md) |

### [AOA-T-0065](../techniques/agent-workflows/mcp-gateway-proxy/TECHNIQUE.md) - mcp-gateway-proxy (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| mcp-gateway-proxy checklist | `absent` | `8` | `techniques/agent-workflows/mcp-gateway-proxy/checks/mcp-gateway-proxy-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/mcp-gateway-proxy/TECHNIQUE.md) |

### [AOA-T-0068](../techniques/agent-workflows/fail-closed-evidence-gate/TECHNIQUE.md) - fail-closed-evidence-gate (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| fail-closed-evidence-gate checklist | `absent` | `8` | `techniques/agent-workflows/fail-closed-evidence-gate/checks/fail-closed-evidence-gate-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/fail-closed-evidence-gate/TECHNIQUE.md) |

### [AOA-T-0069](../techniques/agent-workflows/approval-bound-durable-jobs/TECHNIQUE.md) - approval-bound-durable-jobs (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| approval-bound-durable-jobs checklist | `absent` | `8` | `techniques/agent-workflows/approval-bound-durable-jobs/checks/approval-bound-durable-jobs-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/approval-bound-durable-jobs/TECHNIQUE.md) |

### [AOA-T-0070](../techniques/agent-workflows/two-stage-document-ocr-pipeline/TECHNIQUE.md) - two-stage-document-ocr-pipeline (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| two-stage-document-ocr-pipeline checklist | `absent` | `6` | `techniques/agent-workflows/two-stage-document-ocr-pipeline/checks/two-stage-document-ocr-pipeline-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/two-stage-document-ocr-pipeline/TECHNIQUE.md) |

### [AOA-T-0071](../techniques/agent-workflows/template-backed-field-extraction-after-ocr/TECHNIQUE.md) - template-backed-field-extraction-after-ocr (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| template-backed-field-extraction-after-ocr checklist | `absent` | `6` | `techniques/agent-workflows/template-backed-field-extraction-after-ocr/checks/template-backed-field-extraction-after-ocr-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/template-backed-field-extraction-after-ocr/TECHNIQUE.md) |

### [AOA-T-0072](../techniques/agent-workflows/perceptual-media-dedupe-with-threshold-review/TECHNIQUE.md) - perceptual-media-dedupe-with-threshold-review (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| perceptual-media-dedupe-with-threshold-review checklist | `absent` | `6` | `techniques/agent-workflows/perceptual-media-dedupe-with-threshold-review/checks/perceptual-media-dedupe-with-threshold-review-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/perceptual-media-dedupe-with-threshold-review/TECHNIQUE.md) |

### [AOA-T-0073](../techniques/agent-workflows/semantic-media-bucketing-with-vision-plus-ocr/TECHNIQUE.md) - semantic-media-bucketing-with-vision-plus-ocr (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| semantic-media-bucketing-with-vision-plus-ocr checklist | `absent` | `6` | `techniques/agent-workflows/semantic-media-bucketing-with-vision-plus-ocr/checks/semantic-media-bucketing-with-vision-plus-ocr-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/semantic-media-bucketing-with-vision-plus-ocr/TECHNIQUE.md) |

### [AOA-T-0074](../techniques/agent-workflows/telegram-export-normalization-to-local-store/TECHNIQUE.md) - telegram-export-normalization-to-local-store (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| telegram-export-normalization-to-local-store checklist | `absent` | `6` | `techniques/agent-workflows/telegram-export-normalization-to-local-store/checks/telegram-export-normalization-to-local-store-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/telegram-export-normalization-to-local-store/TECHNIQUE.md) |

### [AOA-T-0075](../techniques/agent-workflows/session-donor-harvest/TECHNIQUE.md) - session-donor-harvest (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| session-donor-harvest checklist | `absent` | `8` | `techniques/agent-workflows/session-donor-harvest/checks/session-donor-harvest-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/session-donor-harvest/TECHNIQUE.md) |

### [AOA-T-0076](../techniques/agent-workflows/owner-layer-triage/TECHNIQUE.md) - owner-layer-triage (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| owner-layer-triage checklist | `absent` | `8` | `techniques/agent-workflows/owner-layer-triage/checks/owner-layer-triage-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/owner-layer-triage/TECHNIQUE.md) |

### [AOA-T-0077](../techniques/agent-workflows/harvest-packet-contract/TECHNIQUE.md) - harvest-packet-contract (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| harvest-packet-contract checklist | `absent` | `7` | `techniques/agent-workflows/harvest-packet-contract/checks/harvest-packet-contract-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/harvest-packet-contract/TECHNIQUE.md) |

### [AOA-T-0078](../techniques/agent-workflows/decision-fork-cards/TECHNIQUE.md) - decision-fork-cards (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| decision-fork-cards checklist | `absent` | `8` | `techniques/agent-workflows/decision-fork-cards/checks/decision-fork-cards-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/decision-fork-cards/TECHNIQUE.md) |

### [AOA-T-0079](../techniques/agent-workflows/risk-passport-lift/TECHNIQUE.md) - risk-passport-lift (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| risk-passport-lift checklist | `absent` | `7` | `techniques/agent-workflows/risk-passport-lift/checks/risk-passport-lift-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/risk-passport-lift/TECHNIQUE.md) |

### [AOA-T-0080](../techniques/agent-workflows/session-drift-taxonomy/TECHNIQUE.md) - session-drift-taxonomy (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| session-drift-taxonomy checklist | `absent` | `7` | `techniques/agent-workflows/session-drift-taxonomy/checks/session-drift-taxonomy-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/session-drift-taxonomy/TECHNIQUE.md) |

### [AOA-T-0081](../techniques/agent-workflows/diagnosis-from-reviewed-evidence/TECHNIQUE.md) - diagnosis-from-reviewed-evidence (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| diagnosis-from-reviewed-evidence checklist | `absent` | `7` | `techniques/agent-workflows/diagnosis-from-reviewed-evidence/checks/diagnosis-from-reviewed-evidence-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/diagnosis-from-reviewed-evidence/TECHNIQUE.md) |

### [AOA-T-0082](../techniques/agent-workflows/repair-shape-from-diagnosis/TECHNIQUE.md) - repair-shape-from-diagnosis (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| repair-shape-from-diagnosis checklist | `absent` | `7` | `techniques/agent-workflows/repair-shape-from-diagnosis/checks/repair-shape-from-diagnosis-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/repair-shape-from-diagnosis/TECHNIQUE.md) |

### [AOA-T-0083](../techniques/agent-workflows/checkpoint-bound-self-repair/TECHNIQUE.md) - checkpoint-bound-self-repair (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| checkpoint-bound-self-repair checklist | `absent` | `7` | `techniques/agent-workflows/checkpoint-bound-self-repair/checks/checkpoint-bound-self-repair-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/checkpoint-bound-self-repair/TECHNIQUE.md) |

### [AOA-T-0084](../techniques/agent-workflows/progression-evidence-lift/TECHNIQUE.md) - progression-evidence-lift (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| progression-evidence-lift checklist | `absent` | `7` | `techniques/agent-workflows/progression-evidence-lift/checks/progression-evidence-lift-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/progression-evidence-lift/TECHNIQUE.md) |

### [AOA-T-0085](../techniques/agent-workflows/multi-axis-quest-overlay/TECHNIQUE.md) - multi-axis-quest-overlay (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| multi-axis-quest-overlay checklist | `absent` | `6` | `techniques/agent-workflows/multi-axis-quest-overlay/checks/multi-axis-quest-overlay-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/multi-axis-quest-overlay/TECHNIQUE.md) |

### [AOA-T-0086](../techniques/agent-workflows/automation-fit-matrix/TECHNIQUE.md) - automation-fit-matrix (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| automation-fit-matrix checklist | `absent` | `7` | `techniques/agent-workflows/automation-fit-matrix/checks/automation-fit-matrix-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/automation-fit-matrix/TECHNIQUE.md) |

### [AOA-T-0087](../techniques/agent-workflows/human-loop-to-seed-lift/TECHNIQUE.md) - human-loop-to-seed-lift (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| human-loop-to-seed-lift checklist | `absent` | `7` | `techniques/agent-workflows/human-loop-to-seed-lift/checks/human-loop-to-seed-lift-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/human-loop-to-seed-lift/TECHNIQUE.md) |

### [AOA-T-0088](../techniques/agent-workflows/approval-sensitivity-check/TECHNIQUE.md) - approval-sensitivity-check (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| approval-sensitivity-check checklist | `absent` | `7` | `techniques/agent-workflows/approval-sensitivity-check/checks/approval-sensitivity-check-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/approval-sensitivity-check/TECHNIQUE.md) |

### [AOA-T-0089](../techniques/agent-workflows/quest-unit-promotion-review/TECHNIQUE.md) - quest-unit-promotion-review (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| quest-unit-promotion-review checklist | `absent` | `7` | `techniques/agent-workflows/quest-unit-promotion-review/checks/quest-unit-promotion-review-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/quest-unit-promotion-review/TECHNIQUE.md) |

### [AOA-T-0090](../techniques/agent-workflows/nearest-wrong-target-rejection/TECHNIQUE.md) - nearest-wrong-target-rejection (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| nearest-wrong-target-rejection checklist | `absent` | `7` | `techniques/agent-workflows/nearest-wrong-target-rejection/checks/nearest-wrong-target-rejection-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/nearest-wrong-target-rejection/TECHNIQUE.md) |

### [AOA-T-0091](../techniques/agent-workflows/workspace-root-ingress-and-mutation-gate/TECHNIQUE.md) - workspace-root-ingress-and-mutation-gate (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| workspace-root-ingress-and-mutation-gate checklist | `absent` | `7` | `techniques/agent-workflows/workspace-root-ingress-and-mutation-gate/checks/workspace-root-ingress-and-mutation-gate-checklist.md` | [TECHNIQUE.md](../techniques/agent-workflows/workspace-root-ingress-and-mutation-gate/TECHNIQUE.md) |

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

### [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) - single-source-rule-distribution (`canonical`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Single-Source Rule Distribution Checklist | `present` | `7` | `techniques/docs/single-source-rule-distribution/checks/single-source-rule-distribution-checklist.md` | [TECHNIQUE.md](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) |

### [AOA-T-0016](../techniques/docs/bounded-context-map/TECHNIQUE.md) - bounded-context-map (`canonical`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Bounded Context Map Checklist | `present` | `7` | `techniques/docs/bounded-context-map/checks/bounded-context-map-checklist.md` | [TECHNIQUE.md](../techniques/docs/bounded-context-map/TECHNIQUE.md) |

### [AOA-T-0018](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) - markdown-technique-section-lift (`canonical`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Section Lift Checklist | `present` | `6` | `techniques/docs/markdown-technique-section-lift/checks/section-lift-checklist.md` | [TECHNIQUE.md](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) |

### [AOA-T-0019](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) - frontmatter-metadata-spine (`canonical`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Metadata Spine Checklist | `present` | `5` | `techniques/docs/frontmatter-metadata-spine/checks/metadata-spine-checklist.md` | [TECHNIQUE.md](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) |

### [AOA-T-0021](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) - bounded-relation-lift-for-kag (`canonical`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Relation Lift Checklist | `present` | `5` | `techniques/docs/bounded-relation-lift-for-kag/checks/relation-lift-checklist.md` | [TECHNIQUE.md](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) |

### [AOA-T-0034](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md) - public-safe-artifact-sanitization (`canonical`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Public Safe Artifact Sanitization Checklist | `present` | `13` | `techniques/docs/public-safe-artifact-sanitization/checks/public-safe-artifact-sanitization-checklist.md` | [TECHNIQUE.md](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md) |

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
| Decision Rationale Recording Checklist | `absent` | `12` | `techniques/docs/decision-rationale-recording/checks/decision-rationale-recording-checklist.md` | [TECHNIQUE.md](../techniques/docs/decision-rationale-recording/TECHNIQUE.md) |

### [AOA-T-0035](../techniques/docs/profile-preset-composition/TECHNIQUE.md) - profile-preset-composition (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Profile Preset Composition Checklist | `absent` | `12` | `techniques/docs/profile-preset-composition/checks/profile-preset-composition-checklist.md` | [TECHNIQUE.md](../techniques/docs/profile-preset-composition/TECHNIQUE.md) |

### [AOA-T-0040](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md) - skill-vs-command-boundary (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Skill Vs Command Boundary Checklist | `absent` | `9` | `techniques/docs/skill-vs-command-boundary/checks/skill-vs-command-boundary-checklist.md` | [TECHNIQUE.md](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md) |

### [AOA-T-0041](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) - skill-marketplace-curation (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Skill Marketplace Curation Checklist | `absent` | `9` | `techniques/docs/skill-marketplace-curation/checks/skill-marketplace-curation-checklist.md` | [TECHNIQUE.md](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) |

### [AOA-T-0043](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md) - multi-source-primary-input-provenance (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| multi-source-primary-input-provenance Checklist | `absent` | `11` | `techniques/docs/multi-source-primary-input-provenance/checks/multi-source-primary-input-provenance-checklist.md` | [TECHNIQUE.md](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md) |

### [AOA-T-0046](../techniques/docs/repo-doc-surface-lift/TECHNIQUE.md) - repo-doc-surface-lift (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Repo Doc Surface Lift Checklist | `present` | `7` | `techniques/docs/repo-doc-surface-lift/checks/repo-doc-surface-lift-checklist.md` | [TECHNIQUE.md](../techniques/docs/repo-doc-surface-lift/TECHNIQUE.md) |

### [AOA-T-0047](../techniques/docs/github-review-template-lift/TECHNIQUE.md) - github-review-template-lift (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| GitHub Review Template Lift Checklist | `present` | `6` | `techniques/docs/github-review-template-lift/checks/github-review-template-lift-checklist.md` | [TECHNIQUE.md](../techniques/docs/github-review-template-lift/TECHNIQUE.md) |

### [AOA-T-0048](../techniques/docs/semantic-review-surface-lift/TECHNIQUE.md) - semantic-review-surface-lift (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Semantic Review Surface Lift Checklist | `present` | `7` | `techniques/docs/semantic-review-surface-lift/checks/semantic-review-surface-lift-checklist.md` | [TECHNIQUE.md](../techniques/docs/semantic-review-surface-lift/TECHNIQUE.md) |

### [AOA-T-0063](../techniques/docs/versioned-agent-registry-contract/TECHNIQUE.md) - versioned-agent-registry-contract (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| versioned-agent-registry-contract checklist | `absent` | `8` | `techniques/docs/versioned-agent-registry-contract/checks/versioned-agent-registry-contract-checklist.md` | [TECHNIQUE.md](../techniques/docs/versioned-agent-registry-contract/TECHNIQUE.md) |

### [AOA-T-0064](../techniques/docs/capability-discovery/TECHNIQUE.md) - capability-discovery (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| capability-discovery checklist | `absent` | `8` | `techniques/docs/capability-discovery/checks/capability-discovery-checklist.md` | [TECHNIQUE.md](../techniques/docs/capability-discovery/TECHNIQUE.md) |

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

### [AOA-T-0037](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md) - contextual-host-doctor (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Contextual Host Doctor Checklist | `absent` | `10` | `techniques/evaluation/contextual-host-doctor/checks/contextual-host-doctor-checklist.md` | [TECHNIQUE.md](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md) |

### [AOA-T-0039](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) - baseline-first-additive-profile-benchmarks (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Baseline First Additive Profile Benchmarks Checklist | `absent` | `10` | `techniques/evaluation/baseline-first-additive-profile-benchmarks/checks/baseline-first-additive-profile-benchmarks-checklist.md` | [TECHNIQUE.md](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) |

### [AOA-T-0042](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md) - upstream-skill-health-checking (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Upstream Skill Health Checking Checklist | `absent` | `10` | `techniques/evaluation/upstream-skill-health-checking/checks/upstream-skill-health-checking-checklist.md` | [TECHNIQUE.md](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md) |

## `history`

### [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) - versionable-session-transcripts (`canonical`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Versionable Session Transcripts Checklist | `absent` | `9` | `techniques/history/versionable-session-transcripts/checks/versionable-session-transcripts-checklist.md` | [TECHNIQUE.md](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) |

### [AOA-T-0053](../techniques/history/local-first-session-index/TECHNIQUE.md) - local-first-session-index (`canonical`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| local-first-session-index checklist | `absent` | `8` | `techniques/history/local-first-session-index/checks/local-first-session-index-checklist.md` | [TECHNIQUE.md](../techniques/history/local-first-session-index/TECHNIQUE.md) |

### [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) - session-capture-as-repo-artifact (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Session Capture As Repo Artifact Checklist | `absent` | `7` | `techniques/history/session-capture-as-repo-artifact/checks/session-capture-as-repo-artifact-checklist.md` | [TECHNIQUE.md](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) |

### [AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) - witness-trace-as-reviewable-artifact (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| Witness Trace As Reviewable Artifact Checklist | `absent` | `9` | `techniques/history/witness-trace-as-reviewable-artifact/checks/witness-trace-as-reviewable-artifact-checklist.md` | [TECHNIQUE.md](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) |

### [AOA-T-0066](../techniques/history/transcript-replay-artifact/TECHNIQUE.md) - transcript-replay-artifact (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| transcript-replay-artifact checklist | `absent` | `8` | `techniques/history/transcript-replay-artifact/checks/transcript-replay-artifact-checklist.md` | [TECHNIQUE.md](../techniques/history/transcript-replay-artifact/TECHNIQUE.md) |

### [AOA-T-0067](../techniques/history/transcript-linked-code-lineage/TECHNIQUE.md) - transcript-linked-code-lineage (`promoted`)

| checklist | intro | items | check path | source |
|---|---|---|---|---|
| transcript-linked-code-lineage checklist | `absent` | `8` | `techniques/history/transcript-linked-code-lineage/checks/transcript-linked-code-lineage-checklist.md` | [TECHNIQUE.md](../techniques/history/transcript-linked-code-lineage/TECHNIQUE.md) |

## Boundaries

- The meaning remains in the authored checklist files and source bundles.
- This surface is derived validation knowledge only.
- This surface does not become executable policy, hard-gate semantics, or scoring.
