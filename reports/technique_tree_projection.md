# Technique Tree Projection

This file is generated from the technique tree contract, family shelf review, wave1 family overlay, and generated catalog.
Do not edit it by hand; run `python scripts/build_tree_projection.py`.

This projection is non-authoritative and weaker than authored bundle meaning. It is a placement review surface only; it must not be treated as frontmatter truth, schema truth, or automatic path migration authority.

Use this projection to review future trunk and shelf placement before any directory move.

## Projection Scope

- Techniques covered: `107`
- Frontmatter truth axes: `domain`, `kind`
- Target path shape: `techniques/<trunk>/<shelf>/<technique-slug>/TECHNIQUE.md`

## Review Status Counts

| review status | count |
|---|---:|
| `pilot-candidate` | `34` |
| `candidate` | `41` |
| `boundary-watch` | `22` |
| `split-review-needed` | `9` |
| `singleton-hold` | `1` |
| `unassigned-hold` | `0` |

## Trunk Counts

| trunk | count |
|---|---:|
| `continuity` | `14` |
| `execution` | `14` |
| `governance` | `14` |
| `history` | `6` |
| `ingest` | `5` |
| `instruction` | `19` |
| `knowledge-lift` | `8` |
| `proof` | `18` |
| `recovery` | `8` |
| `tool-use` | `1` |

## Shelf Counts

| shelf | count |
|---|---:|
| `agent-workflows-core` | `5` |
| `antifragility-recovery` | `4` |
| `approval-evidence` | `2` |
| `automation-governance` | `9` |
| `capability-boundary` | `3` |
| `capability-registry` | `3` |
| `decision-routing` | `3` |
| `diagnosis-repair` | `4` |
| `docs-boundary` | `4` |
| `donor-harvest` | `4` |
| `evaluation-chain` | `3` |
| `handoff-continuation` | `7` |
| `history-artifacts` | `6` |
| `instruction-surface` | `7` |
| `intent-chain` | `2` |
| `kag-source-lift` | `8` |
| `media-ingest` | `5` |
| `owner-truth-closeout` | `5` |
| `published-summary` | `4` |
| `ready-work-graphs` | `3` |
| `review-compaction` | `3` |
| `review-evidence` | `3` |
| `runtime-truth-lifecycle` | `4` |
| `skill-discovery` | `2` |
| `skill-support` | `3` |
| `tool-gateway` | `1` |

## Technique Projection

| technique | current path | family | proposed trunk | proposed shelf | review status | proposed future path |
|---|---|---|---|---|---|---|
| [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) | `techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md` | `agent-workflows-core` | `execution` | `agent-workflows-core` | `candidate` | `techniques/execution/agent-workflows-core/plan-diff-apply-verify-report/TECHNIQUE.md` |
| [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) | `techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md` | `intent-chain` | `execution` | `intent-chain` | `candidate` | `techniques/execution/intent-chain/intent-plan-dry-run-contract-chain/TECHNIQUE.md` |
| [AOA-T-0014](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) | `techniques/agent-workflows/tdd-slice/TECHNIQUE.md` | `agent-workflows-core` | `execution` | `agent-workflows-core` | `candidate` | `techniques/execution/agent-workflows-core/tdd-slice/TECHNIQUE.md` |
| [AOA-T-0023](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) | `techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md` | `agent-workflows-core` | `execution` | `agent-workflows-core` | `candidate` | `techniques/execution/agent-workflows-core/stateless-single-shot-agent/TECHNIQUE.md` |
| [AOA-T-0028](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) | `techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md` | `agent-workflows-core` | `execution` | `agent-workflows-core` | `candidate` | `techniques/execution/agent-workflows-core/confirmation-gated-mutating-action/TECHNIQUE.md` |
| [AOA-T-0031](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) | `techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md` | `agent-workflows-core` | `execution` | `agent-workflows-core` | `candidate` | `techniques/execution/agent-workflows-core/shell-composable-agent-invocation/TECHNIQUE.md` |
| [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) | `techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md` | `intent-chain` | `execution` | `intent-chain` | `candidate` | `techniques/execution/intent-chain/new-intent-rollout-checklist/TECHNIQUE.md` |
| [AOA-T-0036](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md) | `techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md` | `runtime-truth-lifecycle` | `execution` | `runtime-truth-lifecycle` | `boundary-watch` | `techniques/execution/runtime-truth-lifecycle/render-truth-before-startup/TECHNIQUE.md` |
| [AOA-T-0038](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) | `techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md` | `runtime-truth-lifecycle` | `execution` | `runtime-truth-lifecycle` | `boundary-watch` | `techniques/execution/runtime-truth-lifecycle/one-command-service-lifecycle/TECHNIQUE.md` |
| [AOA-T-0049](../techniques/agent-workflows/dependency-aware-task-graph/TECHNIQUE.md) | `techniques/agent-workflows/dependency-aware-task-graph/TECHNIQUE.md` | `ready-work-graphs` | `execution` | `ready-work-graphs` | `candidate` | `techniques/execution/ready-work-graphs/dependency-aware-task-graph/TECHNIQUE.md` |
| [AOA-T-0050](../techniques/agent-workflows/ready-work-from-blocker-graph/TECHNIQUE.md) | `techniques/agent-workflows/ready-work-from-blocker-graph/TECHNIQUE.md` | `ready-work-graphs` | `execution` | `ready-work-graphs` | `candidate` | `techniques/execution/ready-work-graphs/ready-work-from-blocker-graph/TECHNIQUE.md` |
| [AOA-T-0051](../techniques/continuity/review-compaction/commit-triggered-background-review/TECHNIQUE.md) | `techniques/continuity/review-compaction/commit-triggered-background-review/TECHNIQUE.md` | `review-compaction` | `continuity` | `review-compaction` | `pilot-candidate` | `techniques/continuity/review-compaction/commit-triggered-background-review/TECHNIQUE.md` |
| [AOA-T-0052](../techniques/continuity/review-compaction/review-findings-compaction/TECHNIQUE.md) | `techniques/continuity/review-compaction/review-findings-compaction/TECHNIQUE.md` | `review-compaction` | `continuity` | `review-compaction` | `pilot-candidate` | `techniques/continuity/review-compaction/review-findings-compaction/TECHNIQUE.md` |
| [AOA-T-0054](../techniques/continuity/review-compaction/compaction-resilient-skill-loading/TECHNIQUE.md) | `techniques/continuity/review-compaction/compaction-resilient-skill-loading/TECHNIQUE.md` | `review-compaction` | `continuity` | `review-compaction` | `pilot-candidate` | `techniques/continuity/review-compaction/compaction-resilient-skill-loading/TECHNIQUE.md` |
| [AOA-T-0055](../techniques/agent-workflows/requirements-design-tasks-ladder/TECHNIQUE.md) | `techniques/agent-workflows/requirements-design-tasks-ladder/TECHNIQUE.md` | `ready-work-graphs` | `execution` | `ready-work-graphs` | `candidate` | `techniques/execution/ready-work-graphs/requirements-design-tasks-ladder/TECHNIQUE.md` |
| [AOA-T-0056](../techniques/agent-workflows/channelized-agent-mailbox/TECHNIQUE.md) | `techniques/agent-workflows/channelized-agent-mailbox/TECHNIQUE.md` | `handoff-continuation` | `continuity` | `handoff-continuation` | `pilot-candidate` | `techniques/continuity/handoff-continuation/channelized-agent-mailbox/TECHNIQUE.md` |
| [AOA-T-0057](../techniques/agent-workflows/structured-handoff-before-compaction/TECHNIQUE.md) | `techniques/agent-workflows/structured-handoff-before-compaction/TECHNIQUE.md` | `handoff-continuation` | `continuity` | `handoff-continuation` | `pilot-candidate` | `techniques/continuity/handoff-continuation/structured-handoff-before-compaction/TECHNIQUE.md` |
| [AOA-T-0058](../techniques/agent-workflows/receipt-confirmed-handoff-packet/TECHNIQUE.md) | `techniques/agent-workflows/receipt-confirmed-handoff-packet/TECHNIQUE.md` | `handoff-continuation` | `continuity` | `handoff-continuation` | `pilot-candidate` | `techniques/continuity/handoff-continuation/receipt-confirmed-handoff-packet/TECHNIQUE.md` |
| [AOA-T-0059](../techniques/agent-workflows/git-verified-handoff-claims/TECHNIQUE.md) | `techniques/agent-workflows/git-verified-handoff-claims/TECHNIQUE.md` | `handoff-continuation` | `continuity` | `handoff-continuation` | `pilot-candidate` | `techniques/continuity/handoff-continuation/git-verified-handoff-claims/TECHNIQUE.md` |
| [AOA-T-0060](../techniques/agent-workflows/session-opening-ritual-before-work/TECHNIQUE.md) | `techniques/agent-workflows/session-opening-ritual-before-work/TECHNIQUE.md` | `handoff-continuation` | `continuity` | `handoff-continuation` | `pilot-candidate` | `techniques/continuity/handoff-continuation/session-opening-ritual-before-work/TECHNIQUE.md` |
| [AOA-T-0061](../techniques/agent-workflows/cross-repo-resource-map-bootstrap/TECHNIQUE.md) | `techniques/agent-workflows/cross-repo-resource-map-bootstrap/TECHNIQUE.md` | `handoff-continuation` | `continuity` | `handoff-continuation` | `pilot-candidate` | `techniques/continuity/handoff-continuation/cross-repo-resource-map-bootstrap/TECHNIQUE.md` |
| [AOA-T-0062](../techniques/agent-workflows/episode-bounded-agent-loop/TECHNIQUE.md) | `techniques/agent-workflows/episode-bounded-agent-loop/TECHNIQUE.md` | `handoff-continuation` | `continuity` | `handoff-continuation` | `pilot-candidate` | `techniques/continuity/handoff-continuation/episode-bounded-agent-loop/TECHNIQUE.md` |
| [AOA-T-0065](../techniques/agent-workflows/mcp-gateway-proxy/TECHNIQUE.md) | `techniques/agent-workflows/mcp-gateway-proxy/TECHNIQUE.md` | `tool-gateway` | `tool-use` | `tool-gateway` | `singleton-hold` | `techniques/tool-use/tool-gateway/mcp-gateway-proxy/TECHNIQUE.md` |
| [AOA-T-0068](../techniques/agent-workflows/fail-closed-evidence-gate/TECHNIQUE.md) | `techniques/agent-workflows/fail-closed-evidence-gate/TECHNIQUE.md` | `approval-evidence` | `governance` | `approval-evidence` | `boundary-watch` | `techniques/governance/approval-evidence/fail-closed-evidence-gate/TECHNIQUE.md` |
| [AOA-T-0069](../techniques/agent-workflows/approval-bound-durable-jobs/TECHNIQUE.md) | `techniques/agent-workflows/approval-bound-durable-jobs/TECHNIQUE.md` | `approval-evidence` | `governance` | `approval-evidence` | `boundary-watch` | `techniques/governance/approval-evidence/approval-bound-durable-jobs/TECHNIQUE.md` |
| [AOA-T-0070](../techniques/agent-workflows/two-stage-document-ocr-pipeline/TECHNIQUE.md) | `techniques/agent-workflows/two-stage-document-ocr-pipeline/TECHNIQUE.md` | `media-ingest` | `ingest` | `media-ingest` | `pilot-candidate` | `techniques/ingest/media-ingest/two-stage-document-ocr-pipeline/TECHNIQUE.md` |
| [AOA-T-0071](../techniques/agent-workflows/template-backed-field-extraction-after-ocr/TECHNIQUE.md) | `techniques/agent-workflows/template-backed-field-extraction-after-ocr/TECHNIQUE.md` | `media-ingest` | `ingest` | `media-ingest` | `pilot-candidate` | `techniques/ingest/media-ingest/template-backed-field-extraction-after-ocr/TECHNIQUE.md` |
| [AOA-T-0072](../techniques/agent-workflows/perceptual-media-dedupe-with-threshold-review/TECHNIQUE.md) | `techniques/agent-workflows/perceptual-media-dedupe-with-threshold-review/TECHNIQUE.md` | `media-ingest` | `ingest` | `media-ingest` | `pilot-candidate` | `techniques/ingest/media-ingest/perceptual-media-dedupe-with-threshold-review/TECHNIQUE.md` |
| [AOA-T-0073](../techniques/agent-workflows/semantic-media-bucketing-with-vision-plus-ocr/TECHNIQUE.md) | `techniques/agent-workflows/semantic-media-bucketing-with-vision-plus-ocr/TECHNIQUE.md` | `media-ingest` | `ingest` | `media-ingest` | `pilot-candidate` | `techniques/ingest/media-ingest/semantic-media-bucketing-with-vision-plus-ocr/TECHNIQUE.md` |
| [AOA-T-0074](../techniques/agent-workflows/telegram-export-normalization-to-local-store/TECHNIQUE.md) | `techniques/agent-workflows/telegram-export-normalization-to-local-store/TECHNIQUE.md` | `media-ingest` | `ingest` | `media-ingest` | `pilot-candidate` | `techniques/ingest/media-ingest/telegram-export-normalization-to-local-store/TECHNIQUE.md` |
| [AOA-T-0075](../techniques/agent-workflows/session-donor-harvest/TECHNIQUE.md) | `techniques/agent-workflows/session-donor-harvest/TECHNIQUE.md` | `donor-harvest` | `continuity` | `donor-harvest` | `candidate` | `techniques/continuity/donor-harvest/session-donor-harvest/TECHNIQUE.md` |
| [AOA-T-0076](../techniques/agent-workflows/owner-layer-triage/TECHNIQUE.md) | `techniques/agent-workflows/owner-layer-triage/TECHNIQUE.md` | `decision-routing` | `governance` | `decision-routing` | `candidate` | `techniques/governance/decision-routing/owner-layer-triage/TECHNIQUE.md` |
| [AOA-T-0077](../techniques/agent-workflows/harvest-packet-contract/TECHNIQUE.md) | `techniques/agent-workflows/harvest-packet-contract/TECHNIQUE.md` | `donor-harvest` | `continuity` | `donor-harvest` | `candidate` | `techniques/continuity/donor-harvest/harvest-packet-contract/TECHNIQUE.md` |
| [AOA-T-0078](../techniques/agent-workflows/decision-fork-cards/TECHNIQUE.md) | `techniques/agent-workflows/decision-fork-cards/TECHNIQUE.md` | `decision-routing` | `governance` | `decision-routing` | `candidate` | `techniques/governance/decision-routing/decision-fork-cards/TECHNIQUE.md` |
| [AOA-T-0079](../techniques/agent-workflows/risk-passport-lift/TECHNIQUE.md) | `techniques/agent-workflows/risk-passport-lift/TECHNIQUE.md` | `decision-routing` | `governance` | `decision-routing` | `candidate` | `techniques/governance/decision-routing/risk-passport-lift/TECHNIQUE.md` |
| [AOA-T-0080](../techniques/agent-workflows/session-drift-taxonomy/TECHNIQUE.md) | `techniques/agent-workflows/session-drift-taxonomy/TECHNIQUE.md` | `diagnosis-repair` | `recovery` | `diagnosis-repair` | `pilot-candidate` | `techniques/recovery/diagnosis-repair/session-drift-taxonomy/TECHNIQUE.md` |
| [AOA-T-0081](../techniques/agent-workflows/diagnosis-from-reviewed-evidence/TECHNIQUE.md) | `techniques/agent-workflows/diagnosis-from-reviewed-evidence/TECHNIQUE.md` | `diagnosis-repair` | `recovery` | `diagnosis-repair` | `pilot-candidate` | `techniques/recovery/diagnosis-repair/diagnosis-from-reviewed-evidence/TECHNIQUE.md` |
| [AOA-T-0082](../techniques/agent-workflows/repair-shape-from-diagnosis/TECHNIQUE.md) | `techniques/agent-workflows/repair-shape-from-diagnosis/TECHNIQUE.md` | `diagnosis-repair` | `recovery` | `diagnosis-repair` | `pilot-candidate` | `techniques/recovery/diagnosis-repair/repair-shape-from-diagnosis/TECHNIQUE.md` |
| [AOA-T-0083](../techniques/agent-workflows/checkpoint-bound-self-repair/TECHNIQUE.md) | `techniques/agent-workflows/checkpoint-bound-self-repair/TECHNIQUE.md` | `diagnosis-repair` | `recovery` | `diagnosis-repair` | `pilot-candidate` | `techniques/recovery/diagnosis-repair/checkpoint-bound-self-repair/TECHNIQUE.md` |
| [AOA-T-0084](../techniques/agent-workflows/progression-evidence-lift/TECHNIQUE.md) | `techniques/agent-workflows/progression-evidence-lift/TECHNIQUE.md` | `donor-harvest` | `continuity` | `donor-harvest` | `candidate` | `techniques/continuity/donor-harvest/progression-evidence-lift/TECHNIQUE.md` |
| [AOA-T-0085](../techniques/agent-workflows/multi-axis-quest-overlay/TECHNIQUE.md) | `techniques/agent-workflows/multi-axis-quest-overlay/TECHNIQUE.md` | `donor-harvest` | `continuity` | `donor-harvest` | `candidate` | `techniques/continuity/donor-harvest/multi-axis-quest-overlay/TECHNIQUE.md` |
| [AOA-T-0086](../techniques/agent-workflows/automation-fit-matrix/TECHNIQUE.md) | `techniques/agent-workflows/automation-fit-matrix/TECHNIQUE.md` | `automation-governance` | `governance` | `automation-governance` | `split-review-needed` | `techniques/governance/automation-governance/automation-fit-matrix/TECHNIQUE.md` |
| [AOA-T-0087](../techniques/agent-workflows/human-loop-to-seed-lift/TECHNIQUE.md) | `techniques/agent-workflows/human-loop-to-seed-lift/TECHNIQUE.md` | `automation-governance` | `governance` | `automation-governance` | `split-review-needed` | `techniques/governance/automation-governance/human-loop-to-seed-lift/TECHNIQUE.md` |
| [AOA-T-0088](../techniques/agent-workflows/approval-sensitivity-check/TECHNIQUE.md) | `techniques/agent-workflows/approval-sensitivity-check/TECHNIQUE.md` | `automation-governance` | `governance` | `automation-governance` | `split-review-needed` | `techniques/governance/automation-governance/approval-sensitivity-check/TECHNIQUE.md` |
| [AOA-T-0089](../techniques/agent-workflows/quest-unit-promotion-review/TECHNIQUE.md) | `techniques/agent-workflows/quest-unit-promotion-review/TECHNIQUE.md` | `automation-governance` | `governance` | `automation-governance` | `split-review-needed` | `techniques/governance/automation-governance/quest-unit-promotion-review/TECHNIQUE.md` |
| [AOA-T-0090](../techniques/agent-workflows/nearest-wrong-target-rejection/TECHNIQUE.md) | `techniques/agent-workflows/nearest-wrong-target-rejection/TECHNIQUE.md` | `automation-governance` | `governance` | `automation-governance` | `split-review-needed` | `techniques/governance/automation-governance/nearest-wrong-target-rejection/TECHNIQUE.md` |
| [AOA-T-0091](../techniques/agent-workflows/workspace-root-ingress-and-mutation-gate/TECHNIQUE.md) | `techniques/agent-workflows/workspace-root-ingress-and-mutation-gate/TECHNIQUE.md` | `owner-truth-closeout` | `proof` | `owner-truth-closeout` | `boundary-watch` | `techniques/proof/owner-truth-closeout/workspace-root-ingress-and-mutation-gate/TECHNIQUE.md` |
| [AOA-T-0092](../techniques/agent-workflows/audit-to-closeout-proof-loop/TECHNIQUE.md) | `techniques/agent-workflows/audit-to-closeout-proof-loop/TECHNIQUE.md` | `owner-truth-closeout` | `proof` | `owner-truth-closeout` | `boundary-watch` | `techniques/proof/owner-truth-closeout/audit-to-closeout-proof-loop/TECHNIQUE.md` |
| [AOA-T-0093](../techniques/agent-workflows/recommendation-truth-vs-host-actionability/TECHNIQUE.md) | `techniques/agent-workflows/recommendation-truth-vs-host-actionability/TECHNIQUE.md` | `capability-boundary` | `instruction` | `capability-boundary` | `boundary-watch` | `techniques/instruction/capability-boundary/recommendation-truth-vs-host-actionability/TECHNIQUE.md` |
| [AOA-T-0095](../techniques/agent-workflows/github-only-owner-endcap-with-reality-sync/TECHNIQUE.md) | `techniques/agent-workflows/github-only-owner-endcap-with-reality-sync/TECHNIQUE.md` | `owner-truth-closeout` | `proof` | `owner-truth-closeout` | `boundary-watch` | `techniques/proof/owner-truth-closeout/github-only-owner-endcap-with-reality-sync/TECHNIQUE.md` |
| [AOA-T-0096](../techniques/agent-workflows/pinned-validation-matrix-before-generated-publish/TECHNIQUE.md) | `techniques/agent-workflows/pinned-validation-matrix-before-generated-publish/TECHNIQUE.md` | `owner-truth-closeout` | `proof` | `owner-truth-closeout` | `boundary-watch` | `techniques/proof/owner-truth-closeout/pinned-validation-matrix-before-generated-publish/TECHNIQUE.md` |
| [AOA-T-0101](../techniques/agent-workflows/local-pattern-adoption-gate/TECHNIQUE.md) | `techniques/agent-workflows/local-pattern-adoption-gate/TECHNIQUE.md` | `automation-governance` | `governance` | `automation-governance` | `split-review-needed` | `techniques/governance/automation-governance/local-pattern-adoption-gate/TECHNIQUE.md` |
| [AOA-T-0102](../techniques/agent-workflows/skill-proposal-handoff-packet/TECHNIQUE.md) | `techniques/agent-workflows/skill-proposal-handoff-packet/TECHNIQUE.md` | `automation-governance` | `governance` | `automation-governance` | `split-review-needed` | `techniques/governance/automation-governance/skill-proposal-handoff-packet/TECHNIQUE.md` |
| [AOA-T-0103](../techniques/agent-workflows/adopted-practice-retention-review/TECHNIQUE.md) | `techniques/agent-workflows/adopted-practice-retention-review/TECHNIQUE.md` | `automation-governance` | `governance` | `automation-governance` | `split-review-needed` | `techniques/governance/automation-governance/adopted-practice-retention-review/TECHNIQUE.md` |
| [AOA-T-0104](../techniques/agent-workflows/superseded-practice-obsolescence-route/TECHNIQUE.md) | `techniques/agent-workflows/superseded-practice-obsolescence-route/TECHNIQUE.md` | `automation-governance` | `governance` | `automation-governance` | `split-review-needed` | `techniques/governance/automation-governance/superseded-practice-obsolescence-route/TECHNIQUE.md` |
| [AOA-T-0105](../techniques/agent-workflows/single-missing-evidence-request/TECHNIQUE.md) | `techniques/agent-workflows/single-missing-evidence-request/TECHNIQUE.md` | `review-evidence` | `proof` | `review-evidence` | `boundary-watch` | `techniques/proof/review-evidence/single-missing-evidence-request/TECHNIQUE.md` |
| [AOA-T-0107](../techniques/agent-workflows/single-locus-claim-challenge/TECHNIQUE.md) | `techniques/agent-workflows/single-locus-claim-challenge/TECHNIQUE.md` | `review-evidence` | `proof` | `review-evidence` | `boundary-watch` | `techniques/proof/review-evidence/single-locus-claim-challenge/TECHNIQUE.md` |
| [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) | `techniques/docs/source-of-truth-layout/TECHNIQUE.md` | `docs-boundary` | `instruction` | `docs-boundary` | `candidate` | `techniques/instruction/docs-boundary/source-of-truth-layout/TECHNIQUE.md` |
| [AOA-T-0009](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) | `techniques/docs/lightweight-status-snapshot/TECHNIQUE.md` | `docs-boundary` | `instruction` | `docs-boundary` | `candidate` | `techniques/instruction/docs-boundary/lightweight-status-snapshot/TECHNIQUE.md` |
| [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) | `techniques/docs/deterministic-context-composition/TECHNIQUE.md` | `instruction-surface` | `instruction` | `instruction-surface` | `pilot-candidate` | `techniques/instruction/instruction-surface/deterministic-context-composition/TECHNIQUE.md` |
| [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) | `techniques/docs/single-source-rule-distribution/TECHNIQUE.md` | `instruction-surface` | `instruction` | `instruction-surface` | `pilot-candidate` | `techniques/instruction/instruction-surface/single-source-rule-distribution/TECHNIQUE.md` |
| [AOA-T-0016](../techniques/docs/bounded-context-map/TECHNIQUE.md) | `techniques/docs/bounded-context-map/TECHNIQUE.md` | `skill-support` | `proof` | `skill-support` | `candidate` | `techniques/proof/skill-support/bounded-context-map/TECHNIQUE.md` |
| [AOA-T-0018](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) | `techniques/docs/markdown-technique-section-lift/TECHNIQUE.md` | `kag-source-lift` | `knowledge-lift` | `kag-source-lift` | `pilot-candidate` | `techniques/knowledge-lift/kag-source-lift/markdown-technique-section-lift/TECHNIQUE.md` |
| [AOA-T-0019](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) | `techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md` | `kag-source-lift` | `knowledge-lift` | `kag-source-lift` | `pilot-candidate` | `techniques/knowledge-lift/kag-source-lift/frontmatter-metadata-spine/TECHNIQUE.md` |
| [AOA-T-0021](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) | `techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md` | `kag-source-lift` | `knowledge-lift` | `kag-source-lift` | `pilot-candidate` | `techniques/knowledge-lift/kag-source-lift/bounded-relation-lift-for-kag/TECHNIQUE.md` |
| [AOA-T-0034](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md) | `techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md` | `docs-boundary` | `instruction` | `docs-boundary` | `candidate` | `techniques/instruction/docs-boundary/public-safe-artifact-sanitization/TECHNIQUE.md` |
| [AOA-T-0020](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) | `techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md` | `kag-source-lift` | `knowledge-lift` | `kag-source-lift` | `pilot-candidate` | `techniques/knowledge-lift/kag-source-lift/evidence-note-provenance-lift/TECHNIQUE.md` |
| [AOA-T-0022](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) | `techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md` | `kag-source-lift` | `knowledge-lift` | `kag-source-lift` | `pilot-candidate` | `techniques/knowledge-lift/kag-source-lift/risk-and-negative-effect-lift/TECHNIQUE.md` |
| [AOA-T-0024](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) | `techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md` | `instruction-surface` | `instruction` | `instruction-surface` | `pilot-candidate` | `techniques/instruction/instruction-surface/upstream-mirroring-with-provenance/TECHNIQUE.md` |
| [AOA-T-0025](../techniques/docs/capability-spec-versioning/TECHNIQUE.md) | `techniques/docs/capability-spec-versioning/TECHNIQUE.md` | `capability-registry` | `instruction` | `capability-registry` | `boundary-watch` | `techniques/instruction/capability-registry/capability-spec-versioning/TECHNIQUE.md` |
| [AOA-T-0027](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) | `techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md` | `instruction-surface` | `instruction` | `instruction-surface` | `pilot-candidate` | `techniques/instruction/instruction-surface/cross-agent-skill-propagation/TECHNIQUE.md` |
| [AOA-T-0029](../techniques/docs/nested-rule-loading/TECHNIQUE.md) | `techniques/docs/nested-rule-loading/TECHNIQUE.md` | `instruction-surface` | `instruction` | `instruction-surface` | `pilot-candidate` | `techniques/instruction/instruction-surface/nested-rule-loading/TECHNIQUE.md` |
| [AOA-T-0030](../techniques/docs/fragmented-agent-context/TECHNIQUE.md) | `techniques/docs/fragmented-agent-context/TECHNIQUE.md` | `instruction-surface` | `instruction` | `instruction-surface` | `pilot-candidate` | `techniques/instruction/instruction-surface/fragmented-agent-context/TECHNIQUE.md` |
| [AOA-T-0033](../techniques/docs/decision-rationale-recording/TECHNIQUE.md) | `techniques/docs/decision-rationale-recording/TECHNIQUE.md` | `docs-boundary` | `instruction` | `docs-boundary` | `candidate` | `techniques/instruction/docs-boundary/decision-rationale-recording/TECHNIQUE.md` |
| [AOA-T-0035](../techniques/docs/profile-preset-composition/TECHNIQUE.md) | `techniques/docs/profile-preset-composition/TECHNIQUE.md` | `instruction-surface` | `instruction` | `instruction-surface` | `pilot-candidate` | `techniques/instruction/instruction-surface/profile-preset-composition/TECHNIQUE.md` |
| [AOA-T-0040](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md) | `techniques/docs/skill-vs-command-boundary/TECHNIQUE.md` | `capability-boundary` | `instruction` | `capability-boundary` | `boundary-watch` | `techniques/instruction/capability-boundary/skill-vs-command-boundary/TECHNIQUE.md` |
| [AOA-T-0041](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) | `techniques/docs/skill-marketplace-curation/TECHNIQUE.md` | `skill-discovery` | `instruction` | `skill-discovery` | `boundary-watch` | `techniques/instruction/skill-discovery/skill-marketplace-curation/TECHNIQUE.md` |
| [AOA-T-0043](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md) | `techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md` | `capability-boundary` | `instruction` | `capability-boundary` | `boundary-watch` | `techniques/instruction/capability-boundary/multi-source-primary-input-provenance/TECHNIQUE.md` |
| [AOA-T-0046](../techniques/docs/repo-doc-surface-lift/TECHNIQUE.md) | `techniques/docs/repo-doc-surface-lift/TECHNIQUE.md` | `kag-source-lift` | `knowledge-lift` | `kag-source-lift` | `pilot-candidate` | `techniques/knowledge-lift/kag-source-lift/repo-doc-surface-lift/TECHNIQUE.md` |
| [AOA-T-0047](../techniques/docs/github-review-template-lift/TECHNIQUE.md) | `techniques/docs/github-review-template-lift/TECHNIQUE.md` | `kag-source-lift` | `knowledge-lift` | `kag-source-lift` | `pilot-candidate` | `techniques/knowledge-lift/kag-source-lift/github-review-template-lift/TECHNIQUE.md` |
| [AOA-T-0048](../techniques/docs/semantic-review-surface-lift/TECHNIQUE.md) | `techniques/docs/semantic-review-surface-lift/TECHNIQUE.md` | `kag-source-lift` | `knowledge-lift` | `kag-source-lift` | `pilot-candidate` | `techniques/knowledge-lift/kag-source-lift/semantic-review-surface-lift/TECHNIQUE.md` |
| [AOA-T-0063](../techniques/docs/versioned-agent-registry-contract/TECHNIQUE.md) | `techniques/docs/versioned-agent-registry-contract/TECHNIQUE.md` | `capability-registry` | `instruction` | `capability-registry` | `boundary-watch` | `techniques/instruction/capability-registry/versioned-agent-registry-contract/TECHNIQUE.md` |
| [AOA-T-0064](../techniques/docs/capability-discovery/TECHNIQUE.md) | `techniques/docs/capability-discovery/TECHNIQUE.md` | `capability-registry` | `instruction` | `capability-registry` | `boundary-watch` | `techniques/instruction/capability-registry/capability-discovery/TECHNIQUE.md` |
| [AOA-T-0094](../techniques/docs/canonical-owner-with-validated-mirror/TECHNIQUE.md) | `techniques/docs/canonical-owner-with-validated-mirror/TECHNIQUE.md` | `owner-truth-closeout` | `proof` | `owner-truth-closeout` | `boundary-watch` | `techniques/proof/owner-truth-closeout/canonical-owner-with-validated-mirror/TECHNIQUE.md` |
| [AOA-T-0106](../techniques/docs/single-scoped-evidence-reference/TECHNIQUE.md) | `techniques/docs/single-scoped-evidence-reference/TECHNIQUE.md` | `review-evidence` | `proof` | `review-evidence` | `boundary-watch` | `techniques/proof/review-evidence/single-scoped-evidence-reference/TECHNIQUE.md` |
| [AOA-T-0003](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) | `techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md` | `evaluation-chain` | `proof` | `evaluation-chain` | `candidate` | `techniques/proof/evaluation-chain/contract-first-smoke-summary/TECHNIQUE.md` |
| [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) | `techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md` | `published-summary` | `proof` | `published-summary` | `candidate` | `techniques/proof/published-summary/latest-alias-plus-history-copy/TECHNIQUE.md` |
| [AOA-T-0007](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) | `techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md` | `evaluation-chain` | `proof` | `evaluation-chain` | `candidate` | `techniques/proof/evaluation-chain/signal-first-gate-promotion/TECHNIQUE.md` |
| [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) | `techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md` | `published-summary` | `proof` | `published-summary` | `candidate` | `techniques/proof/published-summary/published-summary-remediation-snapshot/TECHNIQUE.md` |
| [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) | `techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md` | `published-summary` | `proof` | `published-summary` | `candidate` | `techniques/proof/published-summary/telemetry-integrity-snapshot/TECHNIQUE.md` |
| [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) | `techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md` | `published-summary` | `proof` | `published-summary` | `candidate` | `techniques/proof/published-summary/required-vs-optional-source-rendering/TECHNIQUE.md` |
| [AOA-T-0015](../techniques/evaluation/contract-test-design/TECHNIQUE.md) | `techniques/evaluation/contract-test-design/TECHNIQUE.md` | `skill-support` | `proof` | `skill-support` | `candidate` | `techniques/proof/skill-support/contract-test-design/TECHNIQUE.md` |
| [AOA-T-0017](../techniques/evaluation/property-invariants/TECHNIQUE.md) | `techniques/evaluation/property-invariants/TECHNIQUE.md` | `skill-support` | `proof` | `skill-support` | `candidate` | `techniques/proof/skill-support/property-invariants/TECHNIQUE.md` |
| [AOA-T-0032](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md) | `techniques/evaluation/context-report-for-ci/TECHNIQUE.md` | `evaluation-chain` | `proof` | `evaluation-chain` | `candidate` | `techniques/proof/evaluation-chain/context-report-for-ci/TECHNIQUE.md` |
| [AOA-T-0037](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md) | `techniques/evaluation/contextual-host-doctor/TECHNIQUE.md` | `runtime-truth-lifecycle` | `execution` | `runtime-truth-lifecycle` | `boundary-watch` | `techniques/execution/runtime-truth-lifecycle/contextual-host-doctor/TECHNIQUE.md` |
| [AOA-T-0039](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) | `techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md` | `runtime-truth-lifecycle` | `execution` | `runtime-truth-lifecycle` | `boundary-watch` | `techniques/execution/runtime-truth-lifecycle/baseline-first-additive-profile-benchmarks/TECHNIQUE.md` |
| [AOA-T-0042](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md) | `techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md` | `skill-discovery` | `instruction` | `skill-discovery` | `boundary-watch` | `techniques/instruction/skill-discovery/upstream-skill-health-checking/TECHNIQUE.md` |
| [AOA-T-0097](../techniques/system-recovery/degrade-reground-recover/TECHNIQUE.md) | `techniques/system-recovery/degrade-reground-recover/TECHNIQUE.md` | `antifragility-recovery` | `recovery` | `antifragility-recovery` | `candidate` | `techniques/recovery/antifragility-recovery/degrade-reground-recover/TECHNIQUE.md` |
| [AOA-T-0099](../techniques/system-recovery/isolated-service-stop-on-shared-substrate/TECHNIQUE.md) | `techniques/system-recovery/isolated-service-stop-on-shared-substrate/TECHNIQUE.md` | `antifragility-recovery` | `recovery` | `antifragility-recovery` | `candidate` | `techniques/recovery/antifragility-recovery/isolated-service-stop-on-shared-substrate/TECHNIQUE.md` |
| [AOA-T-0100](../techniques/system-recovery/stress-receipt-reground-closeout/TECHNIQUE.md) | `techniques/system-recovery/stress-receipt-reground-closeout/TECHNIQUE.md` | `antifragility-recovery` | `recovery` | `antifragility-recovery` | `candidate` | `techniques/recovery/antifragility-recovery/stress-receipt-reground-closeout/TECHNIQUE.md` |
| [AOA-T-0098](../techniques/validation-patterns/receipt-first-failure-analysis/TECHNIQUE.md) | `techniques/validation-patterns/receipt-first-failure-analysis/TECHNIQUE.md` | `antifragility-recovery` | `recovery` | `antifragility-recovery` | `candidate` | `techniques/recovery/antifragility-recovery/receipt-first-failure-analysis/TECHNIQUE.md` |
| [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) | `techniques/history/versionable-session-transcripts/TECHNIQUE.md` | `history-artifacts` | `history` | `history-artifacts` | `candidate` | `techniques/history/history-artifacts/versionable-session-transcripts/TECHNIQUE.md` |
| [AOA-T-0053](../techniques/history/local-first-session-index/TECHNIQUE.md) | `techniques/history/local-first-session-index/TECHNIQUE.md` | `history-artifacts` | `history` | `history-artifacts` | `candidate` | `techniques/history/history-artifacts/local-first-session-index/TECHNIQUE.md` |
| [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) | `techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md` | `history-artifacts` | `history` | `history-artifacts` | `candidate` | `techniques/history/history-artifacts/session-capture-as-repo-artifact/TECHNIQUE.md` |
| [AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) | `techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md` | `history-artifacts` | `history` | `history-artifacts` | `candidate` | `techniques/history/history-artifacts/witness-trace-as-reviewable-artifact/TECHNIQUE.md` |
| [AOA-T-0066](../techniques/history/transcript-replay-artifact/TECHNIQUE.md) | `techniques/history/transcript-replay-artifact/TECHNIQUE.md` | `history-artifacts` | `history` | `history-artifacts` | `candidate` | `techniques/history/history-artifacts/transcript-replay-artifact/TECHNIQUE.md` |
| [AOA-T-0067](../techniques/history/transcript-linked-code-lineage/TECHNIQUE.md) | `techniques/history/transcript-linked-code-lineage/TECHNIQUE.md` | `history-artifacts` | `history` | `history-artifacts` | `candidate` | `techniques/history/history-artifacts/transcript-linked-code-lineage/TECHNIQUE.md` |

## Boundaries

- This projection is non-authoritative and weaker than authored bundle meaning. It is a placement review surface only; it must not be treated as frontmatter truth, schema truth, or automatic path migration authority.
- This projection can choose review targets, but bundle directories remain unmoved.
- A later migration must read bundle meaning directly, choose one bounded pilot subtree, and update links, generated surfaces, validators, docs, and decision records together.
- `family` remains scout-only; `domain` and `kind` remain current frontmatter truth.
