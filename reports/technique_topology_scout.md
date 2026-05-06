# Technique Topology Scout

This file is generated from the topology axis registry, wave1 family overlay, and generated catalog.
Do not edit it by hand; run `python scripts/build_topology_scout.py`.

This projection is scout-only, non-authoritative, and weaker than bundle frontmatter. It must not be treated as schema truth, frontmatter truth, or automatic remap authority.

Use this report to inspect likely capability, substrate, execution, and risk contours before proposing schema, template, or frontmatter migration.

## Scout Scope

- Techniques covered: `107`
- Frontmatter truth axes: `domain`, `kind`
- Scout axes: `capability_class`, `substrate`, `execution_profile`, `risk_posture`

## `capability_class` Counts

| value | count |
|---|---:|
| `choose` | `33` |
| `communicate` | `3` |
| `compare` | `10` |
| `coordinate` | `11` |
| `handoff` | `12` |
| `interpret` | `8` |
| `learn-from-artifact` | `3` |
| `mutate` | `12` |
| `observe` | `36` |
| `plan` | `21` |
| `read` | `47` |
| `recover` | `10` |
| `summarize` | `16` |
| `transform` | `25` |
| `validate` | `21` |
| `write` | `23` |

## `substrate` Counts

| value | count |
|---|---:|
| `api` | `1` |
| `code` | `4` |
| `config` | `15` |
| `conversation` | `59` |
| `data` | `18` |
| `docs` | `37` |
| `graph-adjacent-artifacts` | `5` |
| `history` | `26` |
| `human-approval-surfaces` | `31` |
| `instructions` | `18` |
| `media` | `6` |
| `memory-adjacent-artifacts` | `13` |
| `runtime-state` | `12` |
| `shell` | `6` |
| `tests` | `19` |
| `tool-surfaces` | `63` |
| `ui` | `13` |

## `execution_profile` Counts

| value | count |
|---|---:|
| `medium-agent` | `21` |
| `orchestration-required` | `53` |
| `small-agent` | `33` |

## `risk_posture` Counts

| value | count |
|---|---:|
| `approval-required` | `14` |
| `degraded-mode` | `15` |
| `external-evidence` | `8` |
| `irreversible` | `2` |
| `mutating` | `25` |
| `public-share` | `12` |
| `read-only` | `65` |
| `security-sensitive` | `10` |

## Technique Projection

| technique | domain | kind | family | capability | substrate | execution | risk |
|---|---|---|---|---|---|---|---|
| [AOA-T-0001](../techniques/execution/agent-workflows-core/plan-diff-apply-verify-report/TECHNIQUE.md) | `agent-workflows` | `workflow` | `agent-workflows-core` | `plan`, `mutate` | `conversation`, `tool-surfaces`, `tests`, `human-approval-surfaces` | `orchestration-required` | `mutating` |
| [AOA-T-0004](../techniques/execution/intent-chain/intent-plan-dry-run-contract-chain/TECHNIQUE.md) | `agent-workflows` | `workflow` | `intent-chain` | `plan`, `transform`, `validate` | `conversation`, `tool-surfaces` | `medium-agent` | `read-only` |
| [AOA-T-0014](../techniques/execution/agent-workflows-core/tdd-slice/TECHNIQUE.md) | `agent-workflows` | `workflow` | `agent-workflows-core` | `plan`, `mutate` | `conversation`, `tool-surfaces`, `code`, `tests` | `orchestration-required` | `mutating` |
| [AOA-T-0023](../techniques/execution/agent-workflows-core/stateless-single-shot-agent/TECHNIQUE.md) | `agent-workflows` | `workflow` | `agent-workflows-core` | `plan` | `conversation`, `tool-surfaces`, `shell`, `memory-adjacent-artifacts` | `medium-agent` | `read-only` |
| [AOA-T-0028](../techniques/execution/agent-workflows-core/confirmation-gated-mutating-action/TECHNIQUE.md) | `agent-workflows` | `guardrail` | `agent-workflows-core` | `choose`, `read`, `plan` | `conversation`, `tool-surfaces`, `shell`, `ui` | `small-agent` | `read-only`, `approval-required` |
| [AOA-T-0031](../techniques/execution/agent-workflows-core/shell-composable-agent-invocation/TECHNIQUE.md) | `agent-workflows` | `composition` | `agent-workflows-core` | `coordinate`, `transform` | `conversation`, `tool-surfaces`, `shell` | `medium-agent` | `read-only` |
| [AOA-T-0005](../techniques/execution/intent-chain/new-intent-rollout-checklist/TECHNIQUE.md) | `agent-workflows` | `workflow` | `intent-chain` | `plan`, `validate` | `conversation`, `tool-surfaces` | `medium-agent` | `read-only` |
| [AOA-T-0036](../techniques/execution/runtime-truth-lifecycle/render-truth-before-startup/TECHNIQUE.md) | `agent-workflows` | `composition` | `runtime-truth-lifecycle` | `coordinate`, `transform`, `mutate` | `conversation`, `tool-surfaces`, `instructions`, `config` | `orchestration-required` | `mutating` |
| [AOA-T-0038](../techniques/execution/runtime-truth-lifecycle/one-command-service-lifecycle/TECHNIQUE.md) | `agent-workflows` | `workflow` | `runtime-truth-lifecycle` | `plan`, `observe`, `interpret` | `conversation`, `tool-surfaces`, `docs`, `shell` | `orchestration-required` | `mutating` |
| [AOA-T-0049](../techniques/execution/ready-work-graphs/dependency-aware-task-graph/TECHNIQUE.md) | `agent-workflows` | `workflow` | `ready-work-graphs` | `plan`, `read`, `communicate` | `conversation`, `tool-surfaces`, `memory-adjacent-artifacts`, `graph-adjacent-artifacts` | `medium-agent` | `read-only` |
| [AOA-T-0050](../techniques/execution/ready-work-graphs/ready-work-from-blocker-graph/TECHNIQUE.md) | `agent-workflows` | `workflow` | `ready-work-graphs` | `plan`, `read`, `choose` | `conversation`, `tool-surfaces`, `memory-adjacent-artifacts`, `graph-adjacent-artifacts` | `medium-agent` | `read-only` |
| [AOA-T-0051](../techniques/continuity/review-compaction/commit-triggered-background-review/TECHNIQUE.md) | `agent-workflows` | `workflow` | `review-compaction` | `plan`, `observe`, `write` | `conversation`, `tool-surfaces`, `history`, `human-approval-surfaces` | `medium-agent` | `read-only` |
| [AOA-T-0052](../techniques/continuity/review-compaction/review-findings-compaction/TECHNIQUE.md) | `agent-workflows` | `workflow` | `review-compaction` | `plan`, `observe`, `validate` | `conversation`, `tool-surfaces`, `code`, `tests` | `medium-agent` | `read-only` |
| [AOA-T-0054](../techniques/continuity/review-compaction/compaction-resilient-skill-loading/TECHNIQUE.md) | `agent-workflows` | `recovery` | `review-compaction` | `recover`, `read`, `summarize` | `conversation`, `tool-surfaces`, `instructions`, `human-approval-surfaces` | `orchestration-required` | `read-only`, `degraded-mode` |
| [AOA-T-0055](../techniques/execution/ready-work-graphs/requirements-design-tasks-ladder/TECHNIQUE.md) | `agent-workflows` | `workflow` | `ready-work-graphs` | `plan`, `read`, `write` | `conversation`, `tool-surfaces`, `code`, `ui` | `medium-agent` | `read-only` |
| [AOA-T-0056](../techniques/continuity/handoff-continuation/channelized-agent-mailbox/TECHNIQUE.md) | `agent-workflows` | `handoff` | `handoff-continuation` | `handoff` | `conversation`, `tool-surfaces`, `history` | `small-agent` | `read-only` |
| [AOA-T-0057](../techniques/continuity/handoff-continuation/structured-handoff-before-compaction/TECHNIQUE.md) | `agent-workflows` | `handoff` | `handoff-continuation` | `handoff`, `plan`, `write` | `conversation`, `tool-surfaces`, `history`, `memory-adjacent-artifacts` | `small-agent` | `read-only` |
| [AOA-T-0058](../techniques/continuity/handoff-continuation/receipt-confirmed-handoff-packet/TECHNIQUE.md) | `agent-workflows` | `handoff` | `handoff-continuation` | `handoff` | `conversation`, `tool-surfaces`, `ui`, `human-approval-surfaces` | `small-agent` | `read-only` |
| [AOA-T-0059](../techniques/continuity/handoff-continuation/git-verified-handoff-claims/TECHNIQUE.md) | `agent-workflows` | `handoff` | `handoff-continuation` | `handoff`, `observe`, `plan` | `conversation`, `tool-surfaces`, `history`, `memory-adjacent-artifacts` | `small-agent` | `read-only` |
| [AOA-T-0060](../techniques/continuity/handoff-continuation/session-opening-ritual-before-work/TECHNIQUE.md) | `agent-workflows` | `handoff` | `handoff-continuation` | `handoff`, `observe`, `read` | `conversation`, `tool-surfaces`, `history` | `orchestration-required` | `mutating` |
| [AOA-T-0061](../techniques/continuity/handoff-continuation/cross-repo-resource-map-bootstrap/TECHNIQUE.md) | `agent-workflows` | `handoff` | `handoff-continuation` | `handoff`, `observe`, `read` | `conversation`, `tool-surfaces`, `history` | `small-agent` | `read-only` |
| [AOA-T-0062](../techniques/continuity/handoff-continuation/episode-bounded-agent-loop/TECHNIQUE.md) | `agent-workflows` | `handoff` | `handoff-continuation` | `handoff`, `mutate`, `validate` | `conversation`, `tool-surfaces`, `instructions`, `runtime-state` | `orchestration-required` | `mutating` |
| [AOA-T-0065](../techniques/agent-workflows/mcp-gateway-proxy/TECHNIQUE.md) | `agent-workflows` | `composition` | `tool-gateway` | `coordinate`, `transform`, `observe` | `conversation`, `tool-surfaces`, `config`, `data` | `orchestration-required` | `public-share`, `approval-required`, `external-evidence` |
| [AOA-T-0068](../techniques/governance/approval-evidence/fail-closed-evidence-gate/TECHNIQUE.md) | `agent-workflows` | `guardrail` | `approval-evidence` | `choose`, `mutate` | `conversation`, `tool-surfaces`, `runtime-state`, `human-approval-surfaces` | `orchestration-required` | `mutating`, `approval-required` |
| [AOA-T-0069](../techniques/governance/approval-evidence/approval-bound-durable-jobs/TECHNIQUE.md) | `agent-workflows` | `handoff` | `approval-evidence` | `handoff`, `choose`, `validate` | `conversation`, `tool-surfaces`, `human-approval-surfaces` | `small-agent` | `read-only`, `approval-required` |
| [AOA-T-0070](../techniques/ingest/media-ingest/two-stage-document-ocr-pipeline/TECHNIQUE.md) | `agent-workflows` | `ingest` | `media-ingest` | `read`, `transform`, `mutate` | `conversation`, `tool-surfaces`, `docs`, `media` | `orchestration-required` | `mutating` |
| [AOA-T-0071](../techniques/ingest/media-ingest/template-backed-field-extraction-after-ocr/TECHNIQUE.md) | `agent-workflows` | `ingest` | `media-ingest` | `read`, `transform`, `write` | `conversation`, `tool-surfaces`, `data`, `media` | `orchestration-required` | `read-only` |
| [AOA-T-0072](../techniques/ingest/media-ingest/perceptual-media-dedupe-with-threshold-review/TECHNIQUE.md) | `agent-workflows` | `ingest` | `media-ingest` | `read`, `transform` | `conversation`, `tool-surfaces`, `media`, `human-approval-surfaces` | `orchestration-required` | `read-only` |
| [AOA-T-0073](../techniques/ingest/media-ingest/semantic-media-bucketing-with-vision-plus-ocr/TECHNIQUE.md) | `agent-workflows` | `ingest` | `media-ingest` | `read`, `transform`, `choose` | `conversation`, `tool-surfaces`, `media`, `ui` | `orchestration-required` | `read-only`, `approval-required` |
| [AOA-T-0074](../techniques/ingest/media-ingest/telegram-export-normalization-to-local-store/TECHNIQUE.md) | `agent-workflows` | `ingest` | `media-ingest` | `read`, `transform`, `observe` | `conversation`, `tool-surfaces`, `docs`, `data` | `orchestration-required` | `security-sensitive` |
| [AOA-T-0075](../techniques/continuity/donor-harvest/session-donor-harvest/TECHNIQUE.md) | `agent-workflows` | `lift` | `donor-harvest` | `transform`, `summarize`, `write` | `conversation`, `tool-surfaces`, `history`, `memory-adjacent-artifacts` | `small-agent` | `read-only`, `external-evidence` |
| [AOA-T-0076](../techniques/governance/decision-routing/owner-layer-triage/TECHNIQUE.md) | `agent-workflows` | `assessment` | `decision-routing` | `compare`, `choose`, `observe` | `conversation`, `tool-surfaces`, `memory-adjacent-artifacts` | `medium-agent` | `read-only` |
| [AOA-T-0077](../techniques/continuity/donor-harvest/harvest-packet-contract/TECHNIQUE.md) | `agent-workflows` | `handoff` | `donor-harvest` | `handoff`, `recover`, `learn-from-artifact` | `conversation`, `tool-surfaces`, `history`, `human-approval-surfaces` | `small-agent` | `read-only`, `degraded-mode`, `external-evidence` |
| [AOA-T-0078](../techniques/governance/decision-routing/decision-fork-cards/TECHNIQUE.md) | `agent-workflows` | `assessment` | `decision-routing` | `compare`, `choose`, `observe` | `conversation`, `tool-surfaces`, `history`, `runtime-state` | `orchestration-required` | `mutating` |
| [AOA-T-0079](../techniques/governance/decision-routing/risk-passport-lift/TECHNIQUE.md) | `agent-workflows` | `assessment` | `decision-routing` | `compare`, `choose`, `observe` | `conversation`, `tool-surfaces`, `runtime-state` | `orchestration-required` | `mutating`, `approval-required` |
| [AOA-T-0080](../techniques/recovery/diagnosis-repair/session-drift-taxonomy/TECHNIQUE.md) | `agent-workflows` | `assessment` | `diagnosis-repair` | `compare`, `choose`, `recover` | `conversation`, `tool-surfaces`, `history` | `medium-agent` | `read-only`, `degraded-mode` |
| [AOA-T-0081](../techniques/recovery/diagnosis-repair/diagnosis-from-reviewed-evidence/TECHNIQUE.md) | `agent-workflows` | `assessment` | `diagnosis-repair` | `compare`, `choose`, `read` | `conversation`, `tool-surfaces`, `history`, `human-approval-surfaces` | `medium-agent` | `read-only`, `degraded-mode` |
| [AOA-T-0082](../techniques/recovery/diagnosis-repair/repair-shape-from-diagnosis/TECHNIQUE.md) | `agent-workflows` | `recovery` | `diagnosis-repair` | `recover`, `plan`, `write` | `conversation`, `tool-surfaces`, `history`, `human-approval-surfaces` | `orchestration-required` | `mutating`, `degraded-mode` |
| [AOA-T-0083](../techniques/recovery/diagnosis-repair/checkpoint-bound-self-repair/TECHNIQUE.md) | `agent-workflows` | `recovery` | `diagnosis-repair` | `recover`, `observe`, `choose` | `conversation`, `tool-surfaces`, `tests`, `human-approval-surfaces` | `orchestration-required` | `read-only`, `approval-required`, `degraded-mode` |
| [AOA-T-0084](../techniques/continuity/donor-harvest/progression-evidence-lift/TECHNIQUE.md) | `agent-workflows` | `lift` | `donor-harvest` | `transform`, `summarize`, `learn-from-artifact` | `conversation`, `tool-surfaces`, `data`, `history` | `small-agent` | `read-only`, `external-evidence` |
| [AOA-T-0085](../techniques/continuity/donor-harvest/multi-axis-quest-overlay/TECHNIQUE.md) | `agent-workflows` | `lift` | `donor-harvest` | `transform`, `summarize`, `choose` | `conversation`, `tool-surfaces` | `orchestration-required` | `security-sensitive`, `external-evidence` |
| [AOA-T-0086](../techniques/governance/automation-readiness/automation-fit-matrix/TECHNIQUE.md) | `agent-workflows` | `assessment` | `automation-governance` | `compare`, `choose`, `validate` | `conversation`, `tool-surfaces`, `human-approval-surfaces` | `medium-agent` | `read-only`, `approval-required` |
| [AOA-T-0087](../techniques/governance/automation-readiness/human-loop-to-seed-lift/TECHNIQUE.md) | `agent-workflows` | `assessment` | `automation-governance` | `compare`, `choose`, `read` | `conversation`, `tool-surfaces`, `history` | `medium-agent` | `read-only`, `degraded-mode` |
| [AOA-T-0088](../techniques/governance/automation-readiness/approval-sensitivity-check/TECHNIQUE.md) | `agent-workflows` | `assessment` | `automation-governance` | `compare`, `choose`, `read` | `conversation`, `tool-surfaces`, `ui`, `human-approval-surfaces` | `orchestration-required` | `mutating`, `approval-required`, `degraded-mode` |
| [AOA-T-0089](../techniques/governance/promotion-boundary/quest-unit-promotion-review/TECHNIQUE.md) | `agent-workflows` | `assessment` | `automation-governance` | `compare`, `choose`, `observe` | `conversation`, `tool-surfaces`, `memory-adjacent-artifacts`, `human-approval-surfaces` | `medium-agent` | `read-only` |
| [AOA-T-0090](../techniques/governance/promotion-boundary/nearest-wrong-target-rejection/TECHNIQUE.md) | `agent-workflows` | `guardrail` | `automation-governance` | `choose` | `conversation`, `tool-surfaces`, `human-approval-surfaces` | `small-agent` | `read-only` |
| [AOA-T-0091](../techniques/proof/owner-truth-closeout/workspace-root-ingress-and-mutation-gate/TECHNIQUE.md) | `agent-workflows` | `guardrail` | `owner-truth-closeout` | `choose` | `conversation`, `tool-surfaces`, `history`, `memory-adjacent-artifacts` | `small-agent` | `read-only`, `approval-required` |
| [AOA-T-0092](../techniques/proof/owner-truth-closeout/audit-to-closeout-proof-loop/TECHNIQUE.md) | `agent-workflows` | `workflow` | `owner-truth-closeout` | `plan`, `validate` | `conversation`, `tool-surfaces`, `media`, `human-approval-surfaces` | `medium-agent` | `read-only` |
| [AOA-T-0093](../techniques/instruction/capability-boundary/recommendation-truth-vs-host-actionability/TECHNIQUE.md) | `agent-workflows` | `guardrail` | `capability-boundary` | `choose`, `observe`, `plan` | `conversation`, `tool-surfaces`, `runtime-state` | `orchestration-required` | `security-sensitive` |
| [AOA-T-0095](../techniques/proof/owner-truth-closeout/github-only-owner-endcap-with-reality-sync/TECHNIQUE.md) | `agent-workflows` | `workflow` | `owner-truth-closeout` | `plan`, `observe`, `validate` | `conversation`, `tool-surfaces` | `medium-agent` | `read-only` |
| [AOA-T-0096](../techniques/proof/owner-truth-closeout/pinned-validation-matrix-before-generated-publish/TECHNIQUE.md) | `agent-workflows` | `validation` | `owner-truth-closeout` | `validate`, `observe`, `read` | `conversation`, `tool-surfaces`, `tests`, `ui` | `orchestration-required` | `mutating`, `public-share` |
| [AOA-T-0101](../techniques/governance/practice-adoption-lifecycle/local-pattern-adoption-gate/TECHNIQUE.md) | `agent-workflows` | `guardrail` | `automation-governance` | `choose`, `recover`, `communicate` | `conversation`, `tool-surfaces`, `data`, `ui` | `orchestration-required` | `public-share`, `approval-required`, `degraded-mode` |
| [AOA-T-0102](../techniques/governance/promotion-boundary/skill-proposal-handoff-packet/TECHNIQUE.md) | `agent-workflows` | `handoff` | `automation-governance` | `handoff`, `learn-from-artifact` | `conversation`, `tool-surfaces`, `data`, `human-approval-surfaces` | `small-agent` | `read-only` |
| [AOA-T-0103](../techniques/governance/practice-adoption-lifecycle/adopted-practice-retention-review/TECHNIQUE.md) | `agent-workflows` | `assessment` | `automation-governance` | `compare`, `choose`, `recover` | `conversation`, `tool-surfaces`, `data`, `human-approval-surfaces` | `medium-agent` | `read-only`, `degraded-mode` |
| [AOA-T-0104](../techniques/governance/practice-adoption-lifecycle/superseded-practice-obsolescence-route/TECHNIQUE.md) | `agent-workflows` | `handoff` | `automation-governance` | `handoff`, `choose` | `conversation`, `tool-surfaces`, `data`, `history` | `orchestration-required` | `irreversible` |
| [AOA-T-0105](../techniques/proof/review-evidence/single-missing-evidence-request/TECHNIQUE.md) | `agent-workflows` | `guardrail` | `review-evidence` | `choose`, `mutate`, `validate` | `conversation`, `tool-surfaces`, `data`, `human-approval-surfaces` | `orchestration-required` | `mutating` |
| [AOA-T-0107](../techniques/proof/review-evidence/single-locus-claim-challenge/TECHNIQUE.md) | `agent-workflows` | `guardrail` | `review-evidence` | `choose`, `plan`, `mutate` | `conversation`, `tool-surfaces`, `human-approval-surfaces` | `orchestration-required` | `mutating` |
| [AOA-T-0002](../techniques/instruction/docs-boundary/source-of-truth-layout/TECHNIQUE.md) | `docs` | `artifact` | `docs-boundary` | `write`, `read`, `plan` | `docs`, `instructions`, `ui`, `history` | `small-agent` | `read-only` |
| [AOA-T-0009](../techniques/instruction/docs-boundary/lightweight-status-snapshot/TECHNIQUE.md) | `docs` | `artifact` | `docs-boundary` | `write`, `summarize` | `docs`, `history` | `small-agent` | `read-only` |
| [AOA-T-0012](../techniques/instruction/instruction-surface/deterministic-context-composition/TECHNIQUE.md) | `docs` | `composition` | `instruction-surface` | `coordinate`, `transform`, `observe` | `docs`, `instructions` | `medium-agent` | `read-only` |
| [AOA-T-0013](../techniques/instruction/instruction-surface/single-source-rule-distribution/TECHNIQUE.md) | `docs` | `distribution` | `instruction-surface` | `coordinate`, `observe`, `read` | `docs`, `instructions` | `orchestration-required` | `read-only` |
| [AOA-T-0016](../techniques/proof/skill-support/bounded-context-map/TECHNIQUE.md) | `docs` | `artifact` | `skill-support` | `write`, `observe`, `handoff` | `docs`, `instructions`, `ui` | `small-agent` | `read-only` |
| [AOA-T-0018](../techniques/knowledge-lift/kag-source-lift/markdown-technique-section-lift/TECHNIQUE.md) | `docs` | `lift` | `kag-source-lift` | `transform`, `summarize`, `read` | `docs`, `config` | `orchestration-required` | `security-sensitive` |
| [AOA-T-0019](../techniques/knowledge-lift/kag-source-lift/frontmatter-metadata-spine/TECHNIQUE.md) | `docs` | `lift` | `kag-source-lift` | `transform`, `summarize`, `read` | `docs`, `config`, `data` | `small-agent` | `read-only` |
| [AOA-T-0021](../techniques/knowledge-lift/kag-source-lift/bounded-relation-lift-for-kag/TECHNIQUE.md) | `docs` | `lift` | `kag-source-lift` | `transform`, `summarize`, `read` | `docs`, `graph-adjacent-artifacts` | `small-agent` | `read-only` |
| [AOA-T-0034](../techniques/instruction/docs-boundary/public-safe-artifact-sanitization/TECHNIQUE.md) | `docs` | `guardrail` | `docs-boundary` | `choose`, `plan`, `write` | `docs`, `human-approval-surfaces` | `orchestration-required` | `public-share`, `approval-required` |
| [AOA-T-0020](../techniques/knowledge-lift/kag-source-lift/evidence-note-provenance-lift/TECHNIQUE.md) | `docs` | `lift` | `kag-source-lift` | `transform`, `summarize`, `read` | `docs`, `config`, `graph-adjacent-artifacts` | `small-agent` | `read-only` |
| [AOA-T-0022](../techniques/knowledge-lift/kag-source-lift/risk-and-negative-effect-lift/TECHNIQUE.md) | `docs` | `lift` | `kag-source-lift` | `transform`, `summarize`, `read` | `docs`, `data` | `small-agent` | `read-only` |
| [AOA-T-0024](../techniques/instruction/instruction-surface/upstream-mirroring-with-provenance/TECHNIQUE.md) | `docs` | `distribution` | `instruction-surface` | `coordinate`, `observe`, `read` | `docs`, `instructions`, `config`, `human-approval-surfaces` | `orchestration-required` | `read-only`, `external-evidence` |
| [AOA-T-0025](../techniques/instruction/capability-registry/capability-spec-versioning/TECHNIQUE.md) | `docs` | `artifact` | `capability-registry` | `write`, `mutate` | `docs`, `config`, `data`, `tool-surfaces` | `orchestration-required` | `mutating` |
| [AOA-T-0027](../techniques/instruction/instruction-surface/cross-agent-skill-propagation/TECHNIQUE.md) | `docs` | `distribution` | `instruction-surface` | `coordinate`, `observe`, `read` | `docs`, `instructions` | `orchestration-required` | `read-only`, `approval-required` |
| [AOA-T-0029](../techniques/instruction/instruction-surface/nested-rule-loading/TECHNIQUE.md) | `docs` | `composition` | `instruction-surface` | `coordinate`, `transform`, `observe` | `docs`, `instructions` | `medium-agent` | `read-only` |
| [AOA-T-0030](../techniques/instruction/instruction-surface/fragmented-agent-context/TECHNIQUE.md) | `docs` | `composition` | `instruction-surface` | `coordinate`, `transform`, `observe` | `docs`, `instructions`, `human-approval-surfaces` | `orchestration-required` | `security-sensitive` |
| [AOA-T-0033](../techniques/instruction/docs-boundary/decision-rationale-recording/TECHNIQUE.md) | `docs` | `artifact` | `docs-boundary` | `write`, `read`, `interpret` | `docs`, `instructions`, `human-approval-surfaces` | `small-agent` | `read-only` |
| [AOA-T-0035](../techniques/instruction/instruction-surface/profile-preset-composition/TECHNIQUE.md) | `docs` | `composition` | `instruction-surface` | `coordinate`, `transform`, `observe` | `docs`, `instructions`, `config`, `runtime-state` | `medium-agent` | `read-only` |
| [AOA-T-0040](../techniques/instruction/capability-boundary/skill-vs-command-boundary/TECHNIQUE.md) | `docs` | `guardrail` | `capability-boundary` | `choose`, `interpret`, `write` | `docs`, `shell`, `tool-surfaces` | `orchestration-required` | `public-share` |
| [AOA-T-0041](../techniques/instruction/skill-discovery/skill-marketplace-curation/TECHNIQUE.md) | `docs` | `discovery` | `skill-discovery` | `read`, `choose`, `interpret` | `docs`, `config`, `data`, `tool-surfaces` | `orchestration-required` | `mutating`, `external-evidence` |
| [AOA-T-0043](../techniques/instruction/capability-boundary/multi-source-primary-input-provenance/TECHNIQUE.md) | `docs` | `guardrail` | `capability-boundary` | `choose`, `observe`, `read` | `docs`, `graph-adjacent-artifacts`, `tool-surfaces` | `small-agent` | `read-only` |
| [AOA-T-0046](../techniques/knowledge-lift/kag-source-lift/repo-doc-surface-lift/TECHNIQUE.md) | `docs` | `lift` | `kag-source-lift` | `transform`, `summarize`, `observe` | `docs` | `orchestration-required` | `security-sensitive` |
| [AOA-T-0047](../techniques/knowledge-lift/kag-source-lift/github-review-template-lift/TECHNIQUE.md) | `docs` | `lift` | `kag-source-lift` | `transform`, `summarize`, `read` | `docs`, `config`, `conversation`, `human-approval-surfaces` | `orchestration-required` | `security-sensitive` |
| [AOA-T-0048](../techniques/knowledge-lift/kag-source-lift/semantic-review-surface-lift/TECHNIQUE.md) | `docs` | `lift` | `kag-source-lift` | `transform`, `summarize`, `observe` | `docs`, `config`, `human-approval-surfaces` | `orchestration-required` | `security-sensitive` |
| [AOA-T-0063](../techniques/instruction/capability-registry/versioned-agent-registry-contract/TECHNIQUE.md) | `docs` | `artifact` | `capability-registry` | `write`, `read`, `interpret` | `docs`, `config`, `data`, `tool-surfaces` | `orchestration-required` | `public-share` |
| [AOA-T-0064](../techniques/instruction/capability-registry/capability-discovery/TECHNIQUE.md) | `docs` | `discovery` | `capability-registry` | `read`, `choose`, `interpret` | `docs`, `config`, `data`, `tool-surfaces` | `orchestration-required` | `mutating`, `public-share` |
| [AOA-T-0094](../techniques/proof/owner-truth-closeout/canonical-owner-with-validated-mirror/TECHNIQUE.md) | `docs` | `distribution` | `owner-truth-closeout` | `coordinate`, `read`, `validate` | `docs`, `tests`, `config`, `data` | `orchestration-required` | `read-only` |
| [AOA-T-0106](../techniques/proof/review-evidence/single-scoped-evidence-reference/TECHNIQUE.md) | `docs` | `artifact` | `review-evidence` | `write`, `read`, `validate` | `docs`, `human-approval-surfaces` | `small-agent` | `read-only` |
| [AOA-T-0003](../techniques/proof/evaluation-chain/contract-first-smoke-summary/TECHNIQUE.md) | `evaluation` | `validation` | `evaluation-chain` | `validate`, `read`, `summarize` | `tests` | `small-agent` | `read-only` |
| [AOA-T-0006](../techniques/proof/published-summary/latest-alias-plus-history-copy/TECHNIQUE.md) | `evaluation` | `artifact` | `published-summary` | `write`, `mutate`, `summarize` | `tests`, `history` | `orchestration-required` | `mutating`, `public-share` |
| [AOA-T-0007](../techniques/proof/evaluation-chain/signal-first-gate-promotion/TECHNIQUE.md) | `evaluation` | `guardrail` | `evaluation-chain` | `choose`, `observe` | `tests` | `orchestration-required` | `approval-required`, `irreversible` |
| [AOA-T-0008](../techniques/proof/published-summary/published-summary-remediation-snapshot/TECHNIQUE.md) | `evaluation` | `lift` | `published-summary` | `transform`, `summarize`, `read` | `tests`, `media`, `history`, `runtime-state` | `orchestration-required` | `mutating`, `public-share` |
| [AOA-T-0010](../techniques/proof/published-summary/telemetry-integrity-snapshot/TECHNIQUE.md) | `evaluation` | `validation` | `published-summary` | `validate`, `observe`, `read` | `tests`, `ui` | `orchestration-required` | `mutating`, `public-share` |
| [AOA-T-0011](../techniques/proof/published-summary/required-vs-optional-source-rendering/TECHNIQUE.md) | `evaluation` | `guardrail` | `published-summary` | `choose`, `observe`, `read` | `tests`, `ui` | `orchestration-required` | `mutating`, `public-share`, `degraded-mode` |
| [AOA-T-0015](../techniques/proof/skill-support/contract-test-design/TECHNIQUE.md) | `evaluation` | `validation` | `skill-support` | `validate` | `tests` | `small-agent` | `read-only` |
| [AOA-T-0017](../techniques/proof/skill-support/property-invariants/TECHNIQUE.md) | `evaluation` | `validation` | `skill-support` | `validate` | `tests` | `small-agent` | `read-only` |
| [AOA-T-0032](../techniques/proof/evaluation-chain/context-report-for-ci/TECHNIQUE.md) | `evaluation` | `validation` | `evaluation-chain` | `validate`, `observe`, `read` | `tests`, `instructions` | `small-agent` | `read-only` |
| [AOA-T-0037](../techniques/execution/runtime-truth-lifecycle/contextual-host-doctor/TECHNIQUE.md) | `evaluation` | `validation` | `runtime-truth-lifecycle` | `validate`, `observe`, `read` | `tests`, `docs`, `instructions`, `shell` | `orchestration-required` | `mutating` |
| [AOA-T-0039](../techniques/execution/runtime-truth-lifecycle/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) | `evaluation` | `validation` | `runtime-truth-lifecycle` | `validate`, `observe`, `write` | `tests`, `instructions`, `runtime-state` | `small-agent` | `read-only` |
| [AOA-T-0042](../techniques/instruction/skill-discovery/upstream-skill-health-checking/TECHNIQUE.md) | `evaluation` | `validation` | `skill-discovery` | `validate`, `observe`, `read` | `tests`, `docs`, `config`, `data` | `orchestration-required` | `security-sensitive`, `external-evidence` |
| [AOA-T-0097](../techniques/recovery/antifragility-recovery/degrade-reground-recover/TECHNIQUE.md) | `system-recovery` | `recovery` | `antifragility-recovery` | `recover`, `read` | `runtime-state` | `orchestration-required` | `read-only`, `degraded-mode` |
| [AOA-T-0099](../techniques/recovery/antifragility-recovery/isolated-service-stop-on-shared-substrate/TECHNIQUE.md) | `system-recovery` | `recovery` | `antifragility-recovery` | `recover`, `mutate`, `communicate` | `runtime-state`, `api`, `ui` | `orchestration-required` | `mutating`, `public-share`, `degraded-mode` |
| [AOA-T-0100](../techniques/recovery/antifragility-recovery/stress-receipt-reground-closeout/TECHNIQUE.md) | `system-recovery` | `recovery` | `antifragility-recovery` | `recover`, `read`, `choose` | `runtime-state`, `human-approval-surfaces` | `orchestration-required` | `read-only`, `degraded-mode` |
| [AOA-T-0098](../techniques/recovery/antifragility-recovery/receipt-first-failure-analysis/TECHNIQUE.md) | `validation-patterns` | `validation` | `antifragility-recovery` | `validate`, `read`, `mutate` | `tests`, `human-approval-surfaces` | `orchestration-required` | `mutating`, `degraded-mode` |
| [AOA-T-0044](../techniques/history/history-artifacts/versionable-session-transcripts/TECHNIQUE.md) | `history` | `artifact` | `history-artifacts` | `write`, `read`, `choose` | `history`, `docs`, `instructions`, `memory-adjacent-artifacts` | `orchestration-required` | `security-sensitive` |
| [AOA-T-0053](../techniques/history/history-artifacts/local-first-session-index/TECHNIQUE.md) | `history` | `artifact` | `history-artifacts` | `write`, `read`, `interpret` | `history`, `docs`, `data`, `ui` | `small-agent` | `read-only` |
| [AOA-T-0026](../techniques/history/history-artifacts/session-capture-as-repo-artifact/TECHNIQUE.md) | `history` | `artifact` | `history-artifacts` | `write` | `history`, `instructions`, `memory-adjacent-artifacts`, `human-approval-surfaces` | `small-agent` | `read-only` |
| [AOA-T-0045](../techniques/history/history-artifacts/witness-trace-as-reviewable-artifact/TECHNIQUE.md) | `history` | `artifact` | `history-artifacts` | `write`, `observe`, `read` | `history`, `memory-adjacent-artifacts`, `human-approval-surfaces` | `small-agent` | `read-only` |
| [AOA-T-0066](../techniques/history/history-artifacts/transcript-replay-artifact/TECHNIQUE.md) | `history` | `artifact` | `history-artifacts` | `write`, `observe`, `read` | `history`, `docs`, `conversation`, `runtime-state` | `small-agent` | `read-only` |
| [AOA-T-0067](../techniques/history/history-artifacts/transcript-linked-code-lineage/TECHNIQUE.md) | `history` | `artifact` | `history-artifacts` | `write`, `interpret` | `history`, `code`, `docs`, `memory-adjacent-artifacts` | `small-agent` | `read-only` |

## Boundaries

- This projection is scout-only, non-authoritative, and weaker than bundle frontmatter. It must not be treated as schema truth, frontmatter truth, or automatic remap authority.
- This projection may guide review packs, but bundle frontmatter remains stronger.
- A later migration must still read bundle meaning directly before changing schema, templates, validators, or frontmatter.
