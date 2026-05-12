# Temporary Promotion Evidence Matrix-Wide Long-Pass Plan

Status: temporary working plan for a full promotion-evidence pass over the
original `82/82` promoted technique corpus; after the `AOA-T-0026` A1 closure,
`AOA-T-0036` A2 closure, and `AOA-T-0037` Stage 2 closure, the live promoted
queue is `79` bundles. This
file is not bundle authority, not a promotion verdict, not generated output,
and not durable searched-lane memory until distilled into bundle-local notes,
the external evidence ledger, the promotion readiness matrix, or a closeout
ledger.

## Operating Posture

The long pass continues the current Audit lane:

- owner repo: `aoa-techniques`
- owning mechanic: `mechanics/audit/`
- active route: `external-evidence-sprint-runbook`
- durable queue: `promotion-readiness-matrix`
- durable searched-lane memory: `external-evidence-ledger`
- bundle authority: each target `TECHNIQUE.md` plus its `notes/`

Current live constraint:

- the `AOA-T-0032` exemplar pass is already landed as adjacent searched-lane
  memory, and `AOA-T-0032` remains the single lead queue item;
- `AOA-T-0026` closed during Stage A1 with exact-fit Aider
  `.aider.chat.history.md` public artifact-family evidence and exits the live
  promoted queue through canonical review;
- `AOA-T-0036` closed during Stage A2 with exact-fit Dockform
  plan/render-before-apply evidence and exits the live promoted queue through
  canonical review;
- `AOA-T-0037` closed during Stage 2 with exact-fit Get Physics Done
  selected-runtime doctor evidence and exits the live promoted queue through
  canonical review;
- the live generated catalog currently contains `79` promoted techniques and
  `28` canonical techniques;
- this plan now targets the full promoted matrix, not only the lead
  sprint order.

## Long-Pass Goal

Move from one exemplar evidence cycle into a complete, repeatable,
matrix-wide pass over the original `82` promoted-technique queue without faking
canonical readiness. The live remaining queue after the `AOA-T-0037` Stage 2
closure is `79` promoted techniques, with `AOA-T-0026`, `AOA-T-0036`, and
`AOA-T-0037` counted as closed rows rather than remaining targets.

The pass succeeds only when every remaining promoted bundle, plus any original
queue row that exits during the pass, has one of these outcomes:

- exact-fit second evidence found and bundle-local notes updated honestly;
- adjacent lane rejected and recorded so it is not searched again casually;
- searched lane exhausted and the next honest search shape named.

Status changes are not the goal. Canonical promotion only becomes eligible when
the bundle-local `notes/canonical-readiness.md` can honestly move to
`approve for canonical promotion`.

## Complete-Scope Rule

This is an original `82/82` promoted-corpus plan with two closed canonical rows.

Do not call the pass complete while any original promoted bundle lacks one
reviewed closeout row in the final ledger, whether it remains promoted,
exits to canonical, or closes with an exhausted/adjacent lane.

At closeout, reconcile the final ledger against:

```bash
jq -r '.techniques[] | select(.status=="promoted") | .id' generated/technique_catalog.json | sort
```

The pass is incomplete if the final accounted ID set differs from generated
catalog truth.

## Current Live Promoted Accounting Table

This table is the working slot map for the full pass. Every current promoted
technique has exactly one row here. Fill the `outcome` and `durable note`
columns only after the bundle has completed the phase rhythm below and the
result has been distilled into the appropriate durable surface.

| stage | technique | domain/kind | pack or lane | outcome | durable note |
|---|---|---|---|---|---|
| Stage 1 | [AOA-T-0032 context-report-for-ci](../../../../techniques/proof/evaluation-chain/context-report-for-ci/TECHNIQUE.md) | evaluation / validation | lead queue; Pack 4 report-only proof lane | adjacent lanes recorded; remains promoted | `external-evidence-ledger` Stage 1 notes; bundle readiness gap sharpened |
| Stage 2 | [AOA-T-0005 new-intent-rollout-checklist](../../../../techniques/execution/intent-chain/new-intent-rollout-checklist/TECHNIQUE.md) | agent-workflows / workflow | Pack 1 long-gap donor lane | adjacent lanes recorded; remains promoted | `external-evidence-ledger` Stage 2 notes; intent-eval and benchmark false-positive lanes ruled out |
| Stage 2 | [AOA-T-0022 risk-and-negative-effect-lift](../../../../techniques/knowledge-lift/kag-source-lift/risk-and-negative-effect-lift/TECHNIQUE.md) | docs / lift | Pack 1 long-gap donor lane | adjacent lanes recorded; remains promoted | `external-evidence-ledger` Stage 2 notes; broad risk/framework false-positive lanes ruled out |
| Stage 2 | [AOA-T-0035 profile-preset-composition](../../../../techniques/instruction/instruction-surface/profile-preset-composition/TECHNIQUE.md) | docs / composition | Pack 3 runtime operator stack | adjacent lanes recorded; remains promoted | `external-evidence-ledger` Stage 2 notes; profile-only, option-preset, editor-profile, feature/template, overlay, and generic config-composition lanes ruled out |
| Stage 2 | [AOA-T-0037 contextual-host-doctor](../../../../techniques/execution/runtime-truth-lifecycle/contextual-host-doctor/TECHNIQUE.md) | evaluation / validation | Pack 3 runtime operator stack | exact-fit second context; exits to canonical | `external-evidence-ledger` exact-fit notes; Get Physics Done selected-runtime doctor surface closes the contextual preflight gap |
| Stage 2 | [AOA-T-0038 one-command-service-lifecycle](../../../../techniques/execution/runtime-truth-lifecycle/one-command-service-lifecycle/TECHNIQUE.md) | agent-workflows / workflow | Pack 3 runtime operator stack | pending |  |
| Stage 2 | [AOA-T-0039 baseline-first-additive-profile-benchmarks](../../../../techniques/execution/runtime-truth-lifecycle/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) | evaluation / validation | Pack 3 runtime operator stack | pending |  |
| Stage 2 | [AOA-T-0027 cross-agent-skill-propagation](../../../../techniques/instruction/instruction-surface/cross-agent-skill-propagation/TECHNIQUE.md) | docs / distribution | Pack 4 instruction-surface cluster | pending |  |
| Stage 2 | [AOA-T-0029 nested-rule-loading](../../../../techniques/instruction/instruction-surface/nested-rule-loading/TECHNIQUE.md) | docs / composition | Pack 4 instruction-surface cluster | pending |  |
| Stage 2 | [AOA-T-0030 fragmented-agent-context](../../../../techniques/instruction/instruction-surface/fragmented-agent-context/TECHNIQUE.md) | docs / composition | Pack 4 instruction-surface cluster | pending |  |
| Stage 2 | [AOA-T-0024 upstream-mirroring-with-provenance](../../../../techniques/instruction/instruction-surface/upstream-mirroring-with-provenance/TECHNIQUE.md) | docs / distribution | Pack 5 skill ecosystem and curated inputs | pending |  |
| Stage 2 | [AOA-T-0025 capability-spec-versioning](../../../../techniques/instruction/capability-registry/capability-spec-versioning/TECHNIQUE.md) | docs / artifact | Pack 5 skill ecosystem and curated inputs | pending |  |
| Stage 2 | [AOA-T-0040 skill-vs-command-boundary](../../../../techniques/instruction/capability-boundary/skill-vs-command-boundary/TECHNIQUE.md) | docs / guardrail | Pack 5 skill ecosystem and curated inputs | pending |  |
| Stage 2 | [AOA-T-0041 skill-marketplace-curation](../../../../techniques/instruction/skill-discovery/skill-marketplace-curation/TECHNIQUE.md) | docs / discovery | Pack 5 skill ecosystem and curated inputs | pending |  |
| Stage 2 | [AOA-T-0042 upstream-skill-health-checking](../../../../techniques/instruction/skill-discovery/upstream-skill-health-checking/TECHNIQUE.md) | evaluation / validation | Pack 5 skill ecosystem and curated inputs | pending |  |
| Stage 2 | [AOA-T-0043 multi-source-primary-input-provenance](../../../../techniques/instruction/capability-boundary/multi-source-primary-input-provenance/TECHNIQUE.md) | docs / guardrail | Pack 5 skill ecosystem and curated inputs | pending |  |
| Stage 2 | [AOA-T-0020 evidence-note-provenance-lift](../../../../techniques/knowledge-lift/kag-source-lift/evidence-note-provenance-lift/TECHNIQUE.md) | docs / lift | Pack 6 KAG/source-lift evidence prep | pending |  |
| Stage 2 | [AOA-T-0046 repo-doc-surface-lift](../../../../techniques/knowledge-lift/kag-source-lift/repo-doc-surface-lift/TECHNIQUE.md) | docs / lift | Pack 6 KAG/source-lift evidence prep | pending |  |
| Stage 2 | [AOA-T-0047 github-review-template-lift](../../../../techniques/knowledge-lift/kag-source-lift/github-review-template-lift/TECHNIQUE.md) | docs / lift | Pack 6 KAG/source-lift evidence prep | pending |  |
| Stage 2 | [AOA-T-0048 semantic-review-surface-lift](../../../../techniques/knowledge-lift/kag-source-lift/semantic-review-surface-lift/TECHNIQUE.md) | docs / lift | Pack 6 KAG/source-lift evidence prep | pending |  |
| Stage 2 | [AOA-T-0045 witness-trace-as-reviewable-artifact](../../../../techniques/history/history-artifacts/witness-trace-as-reviewable-artifact/TECHNIQUE.md) | history / artifact | Pack 7 history artifacts remainder | pending |  |
| Stage 2 | [AOA-T-0033 decision-rationale-recording](../../../../techniques/instruction/docs-boundary/decision-rationale-recording/TECHNIQUE.md) | docs / artifact | Pack 8 internal docs practice | pending |  |
| Stage 3 | [AOA-T-0049 dependency-aware-task-graph](../../../../techniques/execution/ready-work-graphs/dependency-aware-task-graph/TECHNIQUE.md) | agent-workflows / workflow | Pack 9 graph work coordination | pending |  |
| Stage 3 | [AOA-T-0050 ready-work-from-blocker-graph](../../../../techniques/execution/ready-work-graphs/ready-work-from-blocker-graph/TECHNIQUE.md) | agent-workflows / workflow | Pack 9 graph work coordination | pending |  |
| Stage 3 | [AOA-T-0051 commit-triggered-background-review](../../../../techniques/continuity/review-compaction/commit-triggered-background-review/TECHNIQUE.md) | agent-workflows / workflow | Pack 10 background review loop | pending |  |
| Stage 3 | [AOA-T-0052 review-findings-compaction](../../../../techniques/continuity/review-compaction/review-findings-compaction/TECHNIQUE.md) | agent-workflows / workflow | Pack 10 background review loop | pending |  |
| Stage 3 | [AOA-T-0054 compaction-resilient-skill-loading](../../../../techniques/continuity/review-compaction/compaction-resilient-skill-loading/TECHNIQUE.md) | agent-workflows / recovery | Pack 11 post-compaction skill recovery | pending |  |
| Stage 3 | [AOA-T-0055 requirements-design-tasks-ladder](../../../../techniques/execution/ready-work-graphs/requirements-design-tasks-ladder/TECHNIQUE.md) | agent-workflows / workflow | Pack 12 planning ladder | pending |  |
| Stage 3 | [AOA-T-0056 channelized-agent-mailbox](../../../../techniques/continuity/handoff-continuation/channelized-agent-mailbox/TECHNIQUE.md) | agent-workflows / handoff | Pack 13 channelized mailbox | pending |  |
| Stage 3 | [AOA-T-0057 structured-handoff-before-compaction](../../../../techniques/continuity/handoff-continuation/structured-handoff-before-compaction/TECHNIQUE.md) | agent-workflows / handoff | Pack 14 structured handoff before compaction | pending |  |
| Stage 3 | [AOA-T-0058 receipt-confirmed-handoff-packet](../../../../techniques/continuity/handoff-continuation/receipt-confirmed-handoff-packet/TECHNIQUE.md) | agent-workflows / handoff | Pack 15 receipt-confirmed handoff packet | pending |  |
| Stage 3 | [AOA-T-0059 git-verified-handoff-claims](../../../../techniques/continuity/handoff-continuation/git-verified-handoff-claims/TECHNIQUE.md) | agent-workflows / handoff | Pack 16 git-verified handoff claims | pending |  |
| Stage 3 | [AOA-T-0060 session-opening-ritual-before-work](../../../../techniques/continuity/handoff-continuation/session-opening-ritual-before-work/TECHNIQUE.md) | agent-workflows / handoff | Pack 17 session opening ritual before work | pending |  |
| Stage 3 | [AOA-T-0061 cross-repo-resource-map-bootstrap](../../../../techniques/continuity/handoff-continuation/cross-repo-resource-map-bootstrap/TECHNIQUE.md) | agent-workflows / handoff | Pack 18 cross-repo resource map bootstrap | pending |  |
| Stage 3 | [AOA-T-0062 episode-bounded-agent-loop](../../../../techniques/continuity/handoff-continuation/episode-bounded-agent-loop/TECHNIQUE.md) | agent-workflows / handoff | Pack 19 episode-bounded agent loop | pending |  |
| Stage 4 | [AOA-T-0063 versioned-agent-registry-contract](../../../../techniques/instruction/capability-registry/versioned-agent-registry-contract/TECHNIQUE.md) | docs / artifact | Pack 20 versioned agent registry contract | pending |  |
| Stage 4 | [AOA-T-0064 capability-discovery](../../../../techniques/instruction/capability-registry/capability-discovery/TECHNIQUE.md) | docs / discovery | Pack 21 capability discovery | pending |  |
| Stage 4 | [AOA-T-0065 mcp-gateway-proxy](../../../../techniques/tool-use/tool-gateway/mcp-gateway-proxy/TECHNIQUE.md) | agent-workflows / composition | Pack 22 MCP gateway proxy | pending |  |
| Stage 4 | [AOA-T-0066 transcript-replay-artifact](../../../../techniques/history/history-artifacts/transcript-replay-artifact/TECHNIQUE.md) | history / artifact | Pack 23 transcript replay artifact | pending |  |
| Stage 4 | [AOA-T-0067 transcript-linked-code-lineage](../../../../techniques/history/history-artifacts/transcript-linked-code-lineage/TECHNIQUE.md) | history / artifact | Pack 24 transcript-linked code lineage | pending |  |
| Stage 4 | [AOA-T-0068 fail-closed-evidence-gate](../../../../techniques/governance/approval-evidence/fail-closed-evidence-gate/TECHNIQUE.md) | agent-workflows / guardrail | Pack 25 fail-closed evidence gate | pending |  |
| Stage 4 | [AOA-T-0069 approval-bound-durable-jobs](../../../../techniques/governance/approval-evidence/approval-bound-durable-jobs/TECHNIQUE.md) | agent-workflows / handoff | Pack 26 approval-bound durable jobs | pending |  |
| Stage 4 | [AOA-T-0070 two-stage-document-ocr-pipeline](../../../../techniques/ingest/media-ingest/two-stage-document-ocr-pipeline/TECHNIQUE.md) | agent-workflows / ingest | Pack 27 OCR staged handoff | pending |  |
| Stage 4 | [AOA-T-0071 template-backed-field-extraction-after-ocr](../../../../techniques/ingest/media-ingest/template-backed-field-extraction-after-ocr/TECHNIQUE.md) | agent-workflows / ingest | Pack 28 post-OCR template field extraction | pending |  |
| Stage 4 | [AOA-T-0072 perceptual-media-dedupe-with-threshold-review](../../../../techniques/ingest/media-ingest/perceptual-media-dedupe-with-threshold-review/TECHNIQUE.md) | agent-workflows / ingest | Pack 29 perceptual media dedupe | pending |  |
| Stage 4 | [AOA-T-0073 semantic-media-bucketing-with-vision-plus-ocr](../../../../techniques/ingest/media-ingest/semantic-media-bucketing-with-vision-plus-ocr/TECHNIQUE.md) | agent-workflows / ingest | Pack 30 semantic media bucketing | pending |  |
| Stage 4 | [AOA-T-0074 telegram-export-normalization-to-local-store](../../../../techniques/ingest/media-ingest/telegram-export-normalization-to-local-store/TECHNIQUE.md) | agent-workflows / ingest | Pack 31 Telegram export normalization | pending |  |
| Stage 5 | [AOA-T-0075 session-donor-harvest](../../../../techniques/continuity/donor-harvest/session-donor-harvest/TECHNIQUE.md) | agent-workflows / lift | Pack 32 reviewed session harvest spine | pending |  |
| Stage 5 | [AOA-T-0077 harvest-packet-contract](../../../../techniques/continuity/donor-harvest/harvest-packet-contract/TECHNIQUE.md) | agent-workflows / handoff | Pack 32 reviewed session harvest spine | pending |  |
| Stage 5 | [AOA-T-0076 owner-layer-triage](../../../../techniques/governance/decision-routing/owner-layer-triage/TECHNIQUE.md) | agent-workflows / assessment | Pack 33 owner route fork discipline | pending |  |
| Stage 5 | [AOA-T-0078 decision-fork-cards](../../../../techniques/governance/decision-routing/decision-fork-cards/TECHNIQUE.md) | agent-workflows / assessment | Pack 33 owner route fork discipline | pending |  |
| Stage 5 | [AOA-T-0079 risk-passport-lift](../../../../techniques/governance/decision-routing/risk-passport-lift/TECHNIQUE.md) | agent-workflows / assessment | Pack 33 owner route fork discipline | pending |  |
| Stage 5 | [AOA-T-0090 nearest-wrong-target-rejection](../../../../techniques/governance/promotion-boundary/nearest-wrong-target-rejection/TECHNIQUE.md) | agent-workflows / guardrail | Pack 33 owner route fork discipline | pending |  |
| Stage 5 | [AOA-T-0080 session-drift-taxonomy](../../../../techniques/recovery/diagnosis-repair/session-drift-taxonomy/TECHNIQUE.md) | agent-workflows / assessment | Pack 34 diagnosis and repair loop | pending |  |
| Stage 5 | [AOA-T-0081 diagnosis-from-reviewed-evidence](../../../../techniques/recovery/diagnosis-repair/diagnosis-from-reviewed-evidence/TECHNIQUE.md) | agent-workflows / assessment | Pack 34 diagnosis and repair loop | pending |  |
| Stage 5 | [AOA-T-0082 repair-shape-from-diagnosis](../../../../techniques/recovery/diagnosis-repair/repair-shape-from-diagnosis/TECHNIQUE.md) | agent-workflows / recovery | Pack 34 diagnosis and repair loop | pending |  |
| Stage 5 | [AOA-T-0083 checkpoint-bound-self-repair](../../../../techniques/recovery/diagnosis-repair/checkpoint-bound-self-repair/TECHNIQUE.md) | agent-workflows / recovery | Pack 34 diagnosis and repair loop | pending |  |
| Stage 5 | [AOA-T-0084 progression-evidence-lift](../../../../techniques/continuity/donor-harvest/progression-evidence-lift/TECHNIQUE.md) | agent-workflows / lift | Pack 35 progression and quest reflection | pending |  |
| Stage 5 | [AOA-T-0085 multi-axis-quest-overlay](../../../../techniques/continuity/donor-harvest/multi-axis-quest-overlay/TECHNIQUE.md) | agent-workflows / lift | Pack 35 progression and quest reflection | pending |  |
| Stage 5 | [AOA-T-0086 automation-fit-matrix](../../../../techniques/governance/automation-readiness/automation-fit-matrix/TECHNIQUE.md) | agent-workflows / assessment | Pack 36 automation opportunity gates | pending |  |
| Stage 5 | [AOA-T-0087 human-loop-to-first-landing](../../../../techniques/governance/automation-readiness/human-loop-to-first-landing/TECHNIQUE.md) | agent-workflows / assessment | Pack 36 automation opportunity gates | pending |  |
| Stage 5 | [AOA-T-0088 approval-sensitivity-check](../../../../techniques/governance/automation-readiness/approval-sensitivity-check/TECHNIQUE.md) | agent-workflows / assessment | Pack 36 automation opportunity gates | pending |  |
| Stage 5 | [AOA-T-0089 quest-unit-promotion-review](../../../../techniques/governance/promotion-boundary/quest-unit-promotion-review/TECHNIQUE.md) | agent-workflows / assessment | Pack 37 quest promotion verdict | pending |  |
| Stage 6 | [AOA-T-0091 workspace-root-ingress-and-mutation-gate](../../../../techniques/proof/owner-truth-closeout/workspace-root-ingress-and-mutation-gate/TECHNIQUE.md) | agent-workflows / guardrail | Pack 38 workspace boundary and proof loop | pending |  |
| Stage 6 | [AOA-T-0092 audit-to-closeout-proof-loop](../../../../techniques/proof/owner-truth-closeout/audit-to-closeout-proof-loop/TECHNIQUE.md) | agent-workflows / workflow | Pack 38 workspace boundary and proof loop | pending |  |
| Stage 6 | [AOA-T-0093 recommendation-truth-vs-host-actionability](../../../../techniques/instruction/capability-boundary/recommendation-truth-vs-host-actionability/TECHNIQUE.md) | agent-workflows / guardrail | Pack 38 workspace boundary and proof loop | pending |  |
| Stage 6 | [AOA-T-0094 canonical-owner-with-validated-mirror](../../../../techniques/proof/owner-truth-closeout/canonical-owner-with-validated-mirror/TECHNIQUE.md) | docs / distribution | Pack 38 workspace boundary and proof loop | pending |  |
| Stage 6 | [AOA-T-0095 github-only-owner-endcap-with-reality-sync](../../../../techniques/proof/owner-truth-closeout/github-only-owner-endcap-with-reality-sync/TECHNIQUE.md) | agent-workflows / workflow | Pack 38 workspace boundary and proof loop | pending |  |
| Stage 6 | [AOA-T-0096 pinned-validation-matrix-before-generated-publish](../../../../techniques/proof/owner-truth-closeout/pinned-validation-matrix-before-generated-publish/TECHNIQUE.md) | agent-workflows / validation | Pack 38 workspace boundary and proof loop | pending |  |
| Stage 6 | [AOA-T-0097 degrade-reground-recover](../../../../techniques/recovery/antifragility-recovery/degrade-reground-recover/TECHNIQUE.md) | system-recovery / recovery | Pack 39 antifragility recovery fresh scaffolding | pending |  |
| Stage 6 | [AOA-T-0098 receipt-first-failure-analysis](../../../../techniques/recovery/antifragility-recovery/receipt-first-failure-analysis/TECHNIQUE.md) | validation-patterns / validation | Pack 39 antifragility recovery fresh scaffolding | pending |  |
| Stage 6 | [AOA-T-0099 isolated-service-stop-on-shared-substrate](../../../../techniques/recovery/antifragility-recovery/isolated-service-stop-on-shared-substrate/TECHNIQUE.md) | system-recovery / recovery | Pack 39 antifragility recovery fresh scaffolding | pending |  |
| Stage 6 | [AOA-T-0100 stress-receipt-reground-closeout](../../../../techniques/recovery/antifragility-recovery/stress-receipt-reground-closeout/TECHNIQUE.md) | system-recovery / recovery | Pack 39 antifragility recovery fresh scaffolding | pending |  |
| Stage 6 | [AOA-T-0101 local-pattern-adoption-gate](../../../../techniques/governance/practice-adoption-lifecycle/local-pattern-adoption-gate/TECHNIQUE.md) | agent-workflows / guardrail | Pack 40 method-growth extraction family | pending |  |
| Stage 6 | [AOA-T-0102 skill-proposal-handoff-packet](../../../../techniques/governance/promotion-boundary/skill-proposal-handoff-packet/TECHNIQUE.md) | agent-workflows / handoff | Pack 40 method-growth extraction family | pending |  |
| Stage 6 | [AOA-T-0103 adopted-practice-retention-review](../../../../techniques/governance/practice-adoption-lifecycle/adopted-practice-retention-review/TECHNIQUE.md) | agent-workflows / assessment | Pack 40 method-growth extraction family | pending |  |
| Stage 6 | [AOA-T-0104 superseded-practice-obsolescence-route](../../../../techniques/governance/practice-adoption-lifecycle/superseded-practice-obsolescence-route/TECHNIQUE.md) | agent-workflows / handoff | Pack 40 method-growth extraction family | pending |  |
| Stage 6 | [AOA-T-0105 single-missing-evidence-request](../../../../techniques/proof/review-evidence/single-missing-evidence-request/TECHNIQUE.md) | agent-workflows / guardrail | Pack 41 Agon handoff extraction family | pending |  |
| Stage 6 | [AOA-T-0106 single-scoped-evidence-reference](../../../../techniques/proof/review-evidence/single-scoped-evidence-reference/TECHNIQUE.md) | docs / artifact | Pack 41 Agon handoff extraction family | pending |  |
| Stage 6 | [AOA-T-0107 single-locus-claim-challenge](../../../../techniques/proof/review-evidence/single-locus-claim-challenge/TECHNIQUE.md) | agent-workflows / guardrail | Pack 41 Agon handoff extraction family | pending |  |

## Non-Goals

- no synthetic second context invented from `aoa-techniques` itself;
- no donor-import workflow inside this sprint;
- no widening a technique to fit a tempting external source;
- no multi-technique promotion PRs;
- no generated hand edits;
- no `TECHNIQUE_INDEX.md` or frontmatter change unless a bundle truly exits
  the queue into canonical review;
- no `aoa-evals` proof verdicts and no small-agent empirical proof claims;
- no sibling-owner authority imported into technique meaning.

## Matrix-Wide Candidate Order

The order below covers the current promoted matrix plus closed rows from the
original queue. Pack names come from `promotion-readiness-matrix/README.md`;
IDs are reconciled against generated catalog truth.

### Stage 0: Land The Exemplar Base

0. `AOA-T-0032` `context-report-for-ci`
   - current state: exemplar pass recorded adjacent context-report,
     token-budget, repo-packing, LLM-ready-docs, and CI-report lanes.
   - action: land or intentionally carry the exemplar as the first durable
     searched-lane result before starting the rest of the matrix.

### Stage 1: Lead Queue Closure

1. Pack 4 lead row: `AOA-T-0032`
2. Pack 7 lead row: `AOA-T-0026` - closed; exact-fit Aider artifact-family
   evidence found, bundle-local canonical review approved
3. Pack 3 lead row: `AOA-T-0036` - closed; exact-fit Dockform
   plan/render-before-apply evidence found, bundle-local canonical review
   approved

Purpose: prove the exemplar rhythm across three different evidence shapes:
CI-report artifact, history artifact, and runtime truth seam.

### Stage 2: Remaining Early Evidence Packs

4. Pack 1 - Long-Gap Donor Lanes: `AOA-T-0005`, `AOA-T-0022`
5. Pack 3 - Runtime Operator Stack: `AOA-T-0035`, `AOA-T-0038`, `AOA-T-0039`
6. Pack 4 - Instruction-Surface Cluster remainder: `AOA-T-0027`,
   `AOA-T-0029`, `AOA-T-0030`
7. Pack 5 - Skill Ecosystem And Curated Inputs: `AOA-T-0024`,
   `AOA-T-0025`, `AOA-T-0040`, `AOA-T-0041`, `AOA-T-0042`,
   `AOA-T-0043`
8. Pack 6 - KAG / Source-Lift Evidence Prep: `AOA-T-0020`,
   `AOA-T-0046`, `AOA-T-0047`, `AOA-T-0048`
9. Pack 7 - History Artifacts remainder: `AOA-T-0045`
10. Pack 8 - Internal Docs Practice: `AOA-T-0033`

Purpose: close the older promoted families whose blockers are mostly live
external adopter, markdown-first reuse, or long-gap donor proof.

### Stage 3: Workflow And Continuity Packs

11. Pack 9 - Graph Work Coordination: `AOA-T-0049`, `AOA-T-0050`
12. Pack 10 - Background Review Loop: `AOA-T-0051`, `AOA-T-0052`
13. Pack 11 - Post-Compaction Skill Recovery: `AOA-T-0054`
14. Pack 12 - Planning Ladder: `AOA-T-0055`
15. Pack 13 - Channelized Mailbox: `AOA-T-0056`
16. Pack 14 - Structured Handoff Before Compaction: `AOA-T-0057`
17. Pack 15 - Receipt-Confirmed Handoff Packet: `AOA-T-0058`
18. Pack 16 - Git-Verified Handoff Claims: `AOA-T-0059`
19. Pack 17 - Session Opening Ritual Before Work: `AOA-T-0060`
20. Pack 18 - Cross-Repo Resource Map Bootstrap: `AOA-T-0061`
21. Pack 19 - Episode-Bounded Agent Loop: `AOA-T-0062`

Purpose: close coordination, review, compaction, handoff, and continuation
families without collapsing them into one generic "agent workflow" proof lane.

### Stage 4: Registry, Tooling, History, Governance, And Ingest Packs

22. Pack 20 - Versioned Agent Registry Contract: `AOA-T-0063`
23. Pack 21 - Capability Discovery: `AOA-T-0064`
24. Pack 22 - MCP Gateway Proxy: `AOA-T-0065`
25. Pack 23 - Transcript Replay Artifact: `AOA-T-0066`
26. Pack 24 - Transcript-Linked Code Lineage: `AOA-T-0067`
27. Pack 25 - Fail-Closed Evidence Gate: `AOA-T-0068`
28. Pack 26 - Approval-Bound Durable Jobs: `AOA-T-0069`
29. Pack 27 - OCR Staged Handoff: `AOA-T-0070`
30. Pack 28 - Post-OCR Template Field Extraction: `AOA-T-0071`
31. Pack 29 - Perceptual Media Dedupe: `AOA-T-0072`
32. Pack 30 - Semantic Media Bucketing: `AOA-T-0073`
33. Pack 31 - Telegram Export Normalization: `AOA-T-0074`

Purpose: close single-row infrastructure and ingest packs one by one, because
each has a narrow substrate and false positives are likely.

### Stage 5: Session Harvest, Owner Routing, Repair, Progression, Automation

34. Pack 32 - Reviewed Session Harvest Spine: `AOA-T-0075`,
    `AOA-T-0077`
35. Pack 33 - Owner Route Fork Discipline: `AOA-T-0076`,
    `AOA-T-0078`, `AOA-T-0079`, `AOA-T-0090`
36. Pack 34 - Diagnosis And Repair Loop: `AOA-T-0080`,
    `AOA-T-0081`, `AOA-T-0082`, `AOA-T-0083`
37. Pack 35 - Progression And Quest Reflection: `AOA-T-0084`,
    `AOA-T-0085`
38. Pack 36 - Automation Opportunity Gates: `AOA-T-0086`,
    `AOA-T-0087`, `AOA-T-0088`
39. Pack 37 - Quest Promotion Verdict: `AOA-T-0089`

Purpose: close the internal-origin second-consumer lane without pretending
AoA-origin repetition is independent external evidence.

### Stage 6: Workspace Boundary, Recovery Scaffolding, Method-Growth, Agon

40. Pack 38 - Workspace Boundary And Proof Loop: `AOA-T-0091`,
    `AOA-T-0092`, `AOA-T-0093`, `AOA-T-0094`, `AOA-T-0095`,
    `AOA-T-0096`
41. Pack 39 - Antifragility Recovery Fresh Scaffolding: `AOA-T-0097`,
    `AOA-T-0098`, `AOA-T-0099`, `AOA-T-0100`
42. Pack 40 - Method-Growth Extraction Family: `AOA-T-0101`,
    `AOA-T-0102`, `AOA-T-0103`, `AOA-T-0104`
43. Pack 41 - Agon Handoff Extraction Family: `AOA-T-0105`,
    `AOA-T-0106`, `AOA-T-0107`

Purpose: close fresh scaffolding and internal-origin extraction families,
including missing canonical-readiness scaffolds where the matrix already says
the blocker is structure plus second-context review.

### Stage 7: Matrix-Wide Closeout

44. Reconcile all `79` current promoted IDs plus the closed `AOA-T-0026`,
    `AOA-T-0036`, and `AOA-T-0037` rows against generated catalog truth.
45. Produce one closeout ledger with:
    - all IDs accounted;
    - all exact-fit findings;
    - all adjacent-only lanes;
    - all exhausted lanes;
    - all remaining blockers;
    - all status changes, if any;
    - all generated parity surfaces touched;
    - next honest direction after the full pass.
46. Remove this temporary plan after durable state is distilled.

## Phase Rhythm

Each bundle gets the same cycle. Do not skip the contract lock just because a
search result looks promising.

### Phase 0: Branch And Scope Gate

1. Confirm current branch and intended diff.
2. List unrelated dirty surfaces and mark them out of scope.
3. Confirm `AOA-T-0032`, `AOA-T-0026`, and `AOA-T-0036` are treated as the
   landed calibration history described above, not as uncommitted branch state.
4. Do not stage `.agents/skills/**` unless the user routes that separate skill
   work into the current branch.

### Phase 1: Bundle Ingress

For the target bundle:

1. Open the nearest route cards:
   - root `AGENTS.md`
   - `mechanics/AGENTS.md`
   - `mechanics/audit/AGENTS.md`
   - `mechanics/audit/parts/AGENTS.md`
   - `techniques/AGENTS.md`
   - target trunk `AGENTS.md`
2. Open target bundle files:
   - `TECHNIQUE.md`
   - `notes/canonical-readiness.md`
   - `notes/second-context-adaptation.md` when present
   - `notes/external-origin.md` and import/review notes when present
   - `checks/`
   - `examples/`
3. Open shared audit memory:
   - `promotion-readiness-matrix/README.md`
   - `promotion-evidence-runbook/README.md`
   - `external-evidence-sprint-runbook/README.md`
   - `external-evidence-ledger/README.md`

### Phase 2: Contract Lock

Write a small working block in notes, scratch, or the active plan log naming:

1. exact evidence that counts;
2. near misses that must be rejected;
3. sibling techniques that should receive adjacent findings instead;
4. allowed editable files;
5. stop line for status/frontmatter/generated surfaces.

The contract lock must answer:

- what is the reusable object?
- what is the live second consumer supposed to prove?
- what would widen the bundle and must be rejected?
- where does the next owner route live if the evidence is a donor for a new
  technique instead?

### Phase 3: Search Lanes

Search in bounded lanes, one at a time.

For each lane:

1. name the lane before searching;
2. search current ledger first to avoid repeats;
3. use web or public source search only for live external evidence;
4. prefer primary sources:
   - public repositories;
   - official docs;
   - workflow files;
   - example artifacts;
   - release or package pages when they expose the actual workflow shape;
5. reject marketing-only claims unless they link to a real artifact or repo
   surface;
6. stop a lane when it has one clear verdict, not when it becomes exhausting
   noise.

### Phase 4: Candidate Triage

For every possible source, classify it:

- `exact-fit evidence found`;
- `adjacent but insufficient`;
- `no fit in searched lane`;
- `future donor candidate`, if it belongs to Distillation rather than Audit.

Each verdict must include:

1. source surface;
2. why it matches or fails the target contract;
3. whether it changes bundle-local evidence;
4. whether it changes shared queue meaning;
5. whether another bundle or mechanic owns the finding.

### Phase 5: Bundle-Local Update Gate

Only after exact-fit evidence lands:

1. update `notes/second-context-adaptation.md` first;
2. update `notes/canonical-readiness.md` second;
3. update `TECHNIQUE.md` only if the published technique wording, examples,
   checks, or evidence list needs honest reinforcement;
4. add `notes/adverse-effects-review.md` only if the bundle can honestly
   enter canonical approval;
5. keep status as `promoted` unless canonical review has actually approved.

If no exact-fit evidence lands:

1. update `notes/canonical-readiness.md` only if the searched lane materially
   clarifies the remaining gap;
2. update `external-evidence-ledger` with searched-lane memory;
3. do not edit `TECHNIQUE.md` for mere search failure.

### Phase 6: Shared Audit Sync

Update shared surfaces only when their meaning changed:

1. `external-evidence-ledger`
   - always update when a new real searched lane closes or a false-positive
     band is worth preserving.
2. `promotion-readiness-matrix`
   - update when blocker wording, queue order, or pack meaning changes.
3. `promotion-evidence-runbook`
   - update only when active roster, order, or worker brief changes.
4. `external-evidence-sprint-runbook`
   - update only when execution discipline changes, not for every bundle note.
5. `ROADMAP.md`
   - update only if repo-level horizon changes.
6. `CHANGELOG.md`
   - update when the pass changes public evidence posture, generated parity, or
     release-visible docs.

### Phase 7: Generated Parity

Run builders based on changed source surfaces:

1. if evidence notes changed:
   - `python scripts/build_evidence_note_manifest.py`
2. if frontmatter, technique text, or selection surfaces changed:
   - `python scripts/build_catalog.py`
   - other named builders if validation asks for them
3. never hand-edit generated files.

### Phase 8: Validation

Run checks in increasing width:

1. `git diff --check` over intended surfaces.
2. `python -m unittest tests.test_audit_mechanics_topology`
3. `python scripts/validate_nested_agents.py`
4. `python scripts/validate_repo.py`
5. `python -m unittest discover -s tests`
6. `python scripts/release_check.py` after generated surfaces or release-visible
   audit surfaces change.

If validation asks for a generated rebuild, rebuild from source and rerun the
failed check.

### Phase 9: Bundle Closeout

For each bundle, close with:

1. verdict;
2. searched lanes;
3. exact-fit or rejected surfaces;
4. files changed;
5. status/frontmatter posture;
6. validation run;
7. next honest search shape or next bundle.

### Phase 10: Commit / Push / Merge Gate

Use the repo GitHub landing workflow after each full coherent stage:

1. commit only intended files;
2. push branch;
3. open PR with changed surfaces, validation, public-safety posture, generated
   parity, and remaining risk;
4. wait for GitHub `Repo Validation`;
5. merge after green validation;
6. return to `main`, fast-forward, and confirm clean.

Suggested stage boundaries:

- Stage A0: land `AOA-T-0032` exemplar package if it is still uncommitted.
- Stage A1: `AOA-T-0026` cycle - closed by canonical review.
- Stage A2: `AOA-T-0036` cycle - closed by canonical review.
- Stage A-closeout: lead queue closeout ledger or runbook update.
- Stage B: markdown/source-lift cohort, one bundle or tight pair per PR.
- Stage C: long-gap holds, one bundle per PR.

## Bundle-Specific Contracts

### AOA-T-0032: `context-report-for-ci`

Stage 1 verdict, 2026-05-12: no exact-fit second consumer found. LogicStamp
Context, Claude Code Guide context-engineering CI drift detection, ctxloom,
Depwire, and FastPace were searched as public context-compiler, context-drift,
fragment-assembly, dependency-graph, and repo-quality report surfaces. They
remain adjacent because they own compilation, freshness checks, assembly,
graph context, governance, or quality scoring rather than the same separate
read-only CI report over already-composed context source coverage plus token
drift.

Current next search shape:

- artifact-first public workflows where CI compares an expected source or
  fragment inventory against a generated prompt/context artifact;
- token deltas are emitted in the same report;
- assembly, scoring, remediation, graph compilation, and repo-quality verdicts
  remain outside the report.

Exact evidence:

- CI-facing or CI-consumable report artifact;
- observes composed-context health after composition;
- includes source coverage, fragment inventory, token budget, token estimate, or
  token drift;
- read-only, with remediation outside the report.

Reject:

- context assembly or packing tools;
- token badges without source coverage;
- prompt cost estimation without composed-context coverage;
- eval matrices or prompt-quality scoring;
- generic workflow audit or activity summaries.

### AOA-T-0026: `session-capture-as-repo-artifact`

Stage A1 verdict: exact-fit second context found. Aider's public
`.aider.chat.history.md` surface plus committed public repository artifacts
closed the live-adopter gap without widening into memory, search, cloud
history, or instruction authority.

Exact evidence:

- AI or agent session capture stored as a project-visible artifact;
- reviewable in or beside the repository;
- local-first or repo-owned enough to survive as project history;
- not primarily search, memory, recall, or cloud conversation history.

Reject:

- transcript browsers whose main value is search;
- home-directory session stores with no project artifact contract;
- cloud chat history;
- post-capture packaging that does not prove capture-as-artifact.

### AOA-T-0036: `render-truth-before-startup`

Stage A2 verdict, closed 2026-05-12: exact-fit second context found. Dockform's
plan/render-before-apply lane renders effective Compose truth, shows the plan,
keeps secrets masked by default in full config render, and confirms before
startup without taking over lifecycle, readiness, or deployment-preview
authority.

Working lock opened 2026-05-12:

- exact-fit target: one public runtime or local-operator surface where the
  effective composed service/config truth is rendered and explicitly reviewed
  before startup as its own safety seam;
- must preserve: read-only pre-start posture, actual resolved/composed runtime
  view, local handling of sensitive full config, and handoff to later startup
  or readiness rather than replacing them;
- reject: lifecycle wrappers, readiness-only checks, `docker compose config`,
  Helm/Kustomize/template renders, dry-runs, deployment previews, or service
  previews unless the source names a distinct operator review seam over the
  resolved runtime truth before `up`/startup;
- allowed edits if exact-fit evidence lands: bundle-local
  `notes/second-context-adaptation.md`, `notes/canonical-readiness.md`, and
  only then `TECHNIQUE.md`/generated parity if canonical readiness honestly
  changes;
- allowed edits if no exact-fit evidence lands: searched-lane memory in the
  external evidence ledger and, only if the blocker gets sharper, the
  promotion readiness matrix/runbook wording;
- stop line: no `TECHNIQUE_INDEX.md`, frontmatter, or status change unless the
  bundle-local canonical-readiness note can approve promotion.

Exact evidence:

- effective runtime truth is rendered before startup;
- review is an explicit seam, not just a helper command;
- rendered output reflects composed/resolved config or service state;
- startup waits on or is shaped by that review.

Reject:

- lifecycle wrappers;
- readiness checks only;
- template render before apply when startup truth is not the object;
- deployment dry-runs that do not create a local pre-start review seam.

### AOA-T-0020: `evidence-note-provenance-lift`

Exact evidence:

- committed markdown-first corpus;
- typed note kind and note path provenance are lifted into a downstream reader
  or manifest;
- note provenance remains separate from generic graph semantics.

Reject:

- generic citations;
- vector metadata without note-kind/path discipline;
- eval-only donor repetition already known in current lineage.

### AOA-T-0046: `repo-doc-surface-lift`

Exact evidence:

- repository documentation surfaces become a bounded downstream reader,
  routing, or manifest layer;
- source docs remain authored truth;
- generated/reader surface stays subordinate and route-oriented.

Reject:

- generic documentation sites;
- docs indexes with no source-owned route contract;
- product search without provenance.

### AOA-T-0047: `github-review-template-lift`

Exact evidence:

- GitHub review templates are lifted into a downstream intake or review reader;
- template provenance and owner boundary remain explicit.

Reject:

- ordinary PR templates with no lift;
- issue forms as generic governance;
- review automation that owns verdicts rather than template intake.

### AOA-T-0048: `semantic-review-surface-lift`

Exact evidence:

- semantic review surfaces are lifted as bounded review inputs;
- review meaning remains source-linked and non-authoritative unless reviewed.

Reject:

- generic code review summaries;
- AI review products with no source-provenance boundary;
- scoring systems that replace authored review surfaces.

### AOA-T-0005: `new-intent-rollout-checklist`

Exact evidence:

- one non-origin rollout record for adding a new intent;
- checklist is used as the operating artifact, not just described.

Reject:

- generic project planning;
- roadmap tasks without intent-extension procedure;
- internal-only AoA repetition.

### AOA-T-0022: `risk-and-negative-effect-lift`

Exact evidence:

- second committed corpus reuses the exact bounded risk/negative-effect split;
- risk lift stays descriptive, not policy scoring or generated governance.

Reject:

- generic risk sections;
- security scoring or compliance frameworks;
- broad adverse-effects policy without the same note-lift contract.

## Plan Update Rules

Update this temporary file during the pass when:

- a bundle closes;
- a search lane is exhausted;
- a new exact-fit source appears;
- a false-positive band becomes worth preserving;
- a cohort boundary changes;
- validation changes the required generated parity path.

At closeout, remove this temporary file after distilling useful state into:

- bundle-local notes;
- `external-evidence-ledger`;
- `promotion-readiness-matrix`;
- `promotion-evidence-runbook` or `external-evidence-sprint-runbook` if their
  active route changed;
- `CHANGELOG.md`;
- a closeout ledger if the long pass becomes broad enough to need one.
