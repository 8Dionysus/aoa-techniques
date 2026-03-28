# Promotion Readiness Matrix

This doc records the current bundle-by-bundle promotion queue for the `promoted` corpus in `aoa-techniques`.

Use it when the question is not "which repo-wide closure wave should open next?", but "which promoted bundle can be honestly strengthened next, and what proof is still missing before `promoted -> canonical` is real?"

This doc complements [Deep Audit Roadmap](DEEP_AUDIT_ROADMAP.md) and [Long-Gap Canon Design](LONG_GAP_CANON_DESIGN.md).
Bundle meaning still lives in each `TECHNIQUE.md` and `notes/canonical-readiness.md`.
For the current actionable first wave, open [Promotion Wave A Runbook](PROMOTION_WAVE_A_RUNBOOK.md).

## Current Posture

- current promoted corpus: `43` techniques
- current approve-now queue: none
- closest current queue item: [AOA-T-0032](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md), because it now leads the remaining active Wave A set and has the clearest report-only contract among the still-promoted bundles
- latest graduation: [AOA-T-0023](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) moved to `canonical` on 2026-03-23 after follow-up review from the bounded `qqqa` origin plus GitHub Copilot CLI's programmatic fast path as a second public shell-side context
- dominant blocker: most promoted bundles already have examples, checks, second-context adaptation, and canonical-readiness notes; the missing proof is usually one more live downstream adopter beyond the donor or documentation-first adaptation
- fresh extraction watch: [AOA-T-0046](../techniques/docs/repo-doc-surface-lift/TECHNIQUE.md), [AOA-T-0047](../techniques/docs/github-review-template-lift/TECHNIQUE.md), and [AOA-T-0048](../techniques/docs/semantic-review-surface-lift/TECHNIQUE.md) are earlier than the rest and still need second-context plus canonical-readiness scaffolding before canonical discussion is honest

## Wave A Pass 1 Snapshot

- exact-fit reinforcement confirmed:
  - [AOA-T-0018](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md)
    - `aoa-routing` confirms that source-owned section surfaces are real `expand` targets beyond the already-landed downstream evidence in `aoa-skills` and `aoa-evals`
- adjacent or insufficient on the current local search lanes:
  - [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md)
  - [AOA-T-0023](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md)
  - [AOA-T-0032](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md)
  - [AOA-T-0034](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md)
  - [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md)
- no second independent local runtime consumer found in the searched lane:
  - [AOA-T-0036](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md)

This snapshot is about the current local sweep only.
It narrows the next search space and closes false-positive local lanes, but it does not replace later donor searches where those still remain honest.
`AOA-T-0018` has since exited this matrix through a separate follow-up canonical review.
`AOA-T-0013` has since exited this matrix through a separate follow-up canonical review after independent public reinforcement from `dyoshikawa/rulesync` and `EmberAGI/arbitrum-vibekit`.
`AOA-T-0034` has since exited this matrix through a separate follow-up canonical review after an exact-fit second-consumer pass around `Truth-Zeeker-AI-Public`.
`AOA-T-0023` has since exited this matrix through a separate follow-up canonical review after GitHub Copilot CLI's programmatic one-prompt path closed the missing external fast-path gap.

## Readiness Lanes

| lane | count | meaning |
|---|---:|---|
| `long-gap donor lane` | `2` | Needs one explicit new external or source-family proof surface. Repo-local wording work will not close the gap. |
| `cross-context review-refresh lane` | `0` | No active promoted bundle remains in this lane right now; `AOA-T-0018` already exited through follow-up canonical review. |
| `second-corpus evidence-prep lane` | `1` | Needs another live markdown-first corpus, not just another note or example inside this repo. |
| `external live-adopter lane` | `28` | Already has donor intake, documentation-first adaptation, and canonical-readiness review; still needs another real adopter outside the donor repo. |
| `internal-origin second-consumer lane` | `9` | Internal or origin-lineage bundle needs another downstream consumer plus sibling-boundary reinforcement. |
| `fresh extraction lane` | `3` | Has origin evidence only. The next step is second-context plus canonical-readiness scaffolding, not promotion debate. |

## Swarm Rule

- main agent owns wave boundaries, bundle-level verdict discipline, shared docs, any later `TECHNIQUE_INDEX.md` edits, generated-surface sync, and final `python scripts/release_check.py`
- each worker owns one technique bundle at a time and stays inside its `TECHNIQUE.md`, `notes/`, `checks/`, and `examples/`
- workers do not edit `TECHNIQUE_INDEX.md`, generated surfaces, or repo-wide review docs while evidence-gathering is still in flight
- a status flip only becomes eligible after the bundle's own `notes/canonical-readiness.md` can honestly move from `defer for now` to `approve for canonical promotion`

## Pack Matrix

### Pack 1 - Long-Gap Donor Lanes

Shared blocker: each bundle still needs a specific new live proof surface, and another repo-local wording pass would be fake closure.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) | Strong companion checklist to canonical [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md), but still origin-heavy. | One non-origin shared intent-chain rollout record showing the checklist used to add a new intent in practice. |
| [AOA-T-0022](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) | Exact five-part `Risks` contract has one strong donor, not repeated reuse. | One second committed corpus reusing the same five-part `Risks` split without widening into generated policy or scoring. |

### Pack 2 - Shell-Agent Fast Path

Shared blocker: one live adopter beyond donor plus documentation-first adaptation.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0028](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) | Boundary sibling that keeps mutation behind one explicit confirmation seam. | One public workflow surface where the confirmation seam really gates mutation in practice. |
| [AOA-T-0031](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) | Composability sibling focused on stdin, stdout, files, and pipes. | One public workflow surface where one-shot invocation stays pipe/file/stdin-first in real use. |

### Pack 3 - Runtime Operator Stack

Shared blocker: one more live consumer is needed so the stack reads as a portable operator family, not one donor lineage plus repo-local adaptation.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0035](../techniques/docs/profile-preset-composition/TECHNIQUE.md) | Docs-side runtime composition contract with clear sibling boundaries. | One second downstream consumer using reviewable profile and preset layering. |
| [AOA-T-0036](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md) | Strong operator contract and current lead candidate for this pack. | One second live context proving render-review before startup as a real operator step. |
| [AOA-T-0037](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md) | Selector-aware preflight sibling. | One second live context proving preflight stays separate from render review and lifecycle control. |
| [AOA-T-0038](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) | Lifecycle sibling with clear exclusions around launcher doctrine. | One second live operator surface using one-entrypoint lifecycle ownership in practice. |
| [AOA-T-0039](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) | Evaluation sibling that stays additive rather than policy-shaped. | One second downstream consumer proving baseline-first additive comparison stays bounded. |

### Pack 4 - Instruction-Surface Cluster

Shared blocker: the cluster already reads coherently beside canonical [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md), but each promoted sibling still needs one more live contract outside donor documentation.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0027](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) | Managed-target propagation sibling. | One second repo or surface family using shared-skill propagation as a real managed-target fan-out. |
| [AOA-T-0029](../techniques/docs/nested-rule-loading/TECHNIQUE.md) | Hierarchical loading sibling with bounded precedence rules. | One second repo or surface family using the same layered rule hierarchy in practice. |
| [AOA-T-0030](../techniques/docs/fragmented-agent-context/TECHNIQUE.md) | Fragment-authoring sibling to canonical composition. | One second repo where fragment-first authoring is a real source-layer practice. |
| [AOA-T-0032](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md) | Report-only sibling to canonical composition, not the composition engine itself. | One second repo or surface family using the same CI-facing context report as a real artifact. |

`AOA-T-0013` now anchors the canonical local-source fan-out default for this cluster, while the promoted siblings below keep their narrower blockers.

### Pack 5 - Skill Ecosystem And Curated Inputs

Shared blocker: each bundle needs another live consumer so the family stays editorial, source-owned, and bounded rather than ecosystem-specific.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0024](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) | Mirror-plus-provenance contract is clear, but still donor-shaped. | One second curated mirror context preserving upstream ownership and explicit provenance. |
| [AOA-T-0025](../techniques/docs/capability-spec-versioning/TECHNIQUE.md) | Versioned capability contract stays bounded, but has only one live lineage. | One second public agent-facing surface using a versioned capability spec as a real contract. |
| [AOA-T-0040](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md) | Reusable ownership split between shared skill meaning and user-facing command syntax. | One second live context proving the same skill/command split outside the current plugin-oriented lineage. |
| [AOA-T-0041](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) | Editorial discovery layer is clean, but still thinly proven. | One second live context proving curated discoverability stays bounded and does not drift into registry or installer behavior. |
| [AOA-T-0042](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md) | Pre-surface readiness verdict is bounded, but still ecosystem-specific. | One second downstream consumer using the same pre-surface readiness boundary. |
| [AOA-T-0043](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md) | Provenance-ordering bridge rule is strong, but still needs another bridge shape. | One second public bridge surface proving the same primary-versus-supporting input ordering. |

### Pack 6 - KAG / Source-Lift Evidence Prep

Shared blocker: the remaining promoted family members still need more live markdown-first reuse, not more abstraction inside `aoa-techniques`.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0020](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) | Exact note-kind and note-path lift is still donor-family-shaped. | One second live markdown-first corpus beyond the current `aoa-evals` donor surface. |
| [AOA-T-0046](../techniques/docs/repo-doc-surface-lift/TECHNIQUE.md) | Fresh extraction with origin evidence only. | First second-context adaptation plus canonical-readiness review after one non-origin repo-doc routing consumer exists. |
| [AOA-T-0047](../techniques/docs/github-review-template-lift/TECHNIQUE.md) | Fresh extraction with origin evidence only. | First second-context adaptation plus canonical-readiness review after one non-origin template-intake consumer exists. |
| [AOA-T-0048](../techniques/docs/semantic-review-surface-lift/TECHNIQUE.md) | Fresh extraction with origin evidence only. | First second-context adaptation plus canonical-readiness review after one non-origin semantic-review reader or consumer exists. |

### Pack 7 - History Artifacts

Shared blocker: the family is coherent across capture, transcript packaging, local indexing, and witness artifacts, but still needs one more live artifact-first consumer beyond donor plus repo-local adaptation.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) | Foundational history technique and current lead candidate for the domain. | One second repo or surface family using local-first session capture as a real history-artifact layer. |
| [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) | Post-capture transcript-packaging sibling. | One second repo or surface family treating transcript packaging as a reviewable artifact layer. |
| [AOA-T-0053](../techniques/history/local-first-session-index/TECHNIQUE.md) | Post-capture local-index sibling that keeps searchable lookup derivative and local-first. | One second repo or surface family using a local searchable index over already-saved session artifacts without widening into dashboard, memory, or capture doctrine. |
| [AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) | Structured witness-trace sibling with a clear boundary from transcript packaging. | One second downstream consumer outside the current witness/compost pilot lineage. |

### Pack 8 - Internal Docs Practice

Shared blocker: each bundle is internally strong, but still needs another live consumer so it reads as a default pattern rather than one good local practice.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0033](../techniques/docs/decision-rationale-recording/TECHNIQUE.md) | Single-decision note contract is bounded and useful, but still narrow. | One second live consumer proving the same one-decision record pattern in practice. |

### Pack 9 - Graph Work Coordination

Shared blocker: the donor and repo-local adaptation both show the graph as a bounded coordination surface, but one more live adopter is still needed so it reads as a reusable workflow pattern rather than one tracker lineage plus one import.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0049](../techniques/agent-workflows/dependency-aware-task-graph/TECHNIQUE.md) | Explicit blocker-aware graph contract with clear exclusions around memory, tracker product breadth, and project-management doctrine. | One second public workflow surface where real task dependencies determine ready work in practice without widening into a full tracker or memory system. |
| [AOA-T-0050](../techniques/agent-workflows/ready-work-from-blocker-graph/TECHNIQUE.md) | Frontier-derivation sibling that keeps blocker truth ahead of ranking or tracker policy. | One second public workflow surface where blocker-free state determines the next honest work queue without widening into project-management or ranking doctrine. |

### Pack 10 - Background Review Loop

Shared blocker: the donor and repo-local adaptation both show a clean post-commit review artifact seam, but one more live adopter is still needed so the pattern reads as reusable workflow infrastructure rather than one review product lineage plus one import.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0051](../techniques/agent-workflows/commit-triggered-background-review/TECHNIQUE.md) | Commit-bound asynchronous review sibling with clear exclusions around fix loops, queue UI, and CI governance. | One second public workflow surface where commits trigger bounded asynchronous review artifacts without widening into remediation, merge automation, or full CI policy. |
| [AOA-T-0052](../techniques/agent-workflows/review-findings-compaction/TECHNIQUE.md) | Findings-hygiene sibling that verifies and consolidates current review output before action. | One second public workflow surface where repeated or stale findings are revalidated and consolidated without widening into backlog policy, remediation, or generic issue management. |

### Pack 11 - Post-Compaction Skill Recovery

Shared blocker: the donor and repo-local adaptation both show a bounded post-compaction recovery seam, but one more live adopter is still needed so the pattern reads as reusable workflow recovery rather than one plugin lineage plus one import.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0054](../techniques/agent-workflows/compaction-resilient-skill-loading/TECHNIQUE.md) | Post-compaction skill-availability recovery sibling with clear exclusions around full context reconstruction, marketplace discovery, and install doctrine. | One second public workflow surface where compaction triggers bounded skill rediscovery or reload from canonical sources without widening into general context restoration, memory recall, or plugin product semantics. |

### Pack 12 - Planning Ladder

Shared blocker: the donor and repo-local adaptation both show a bounded requirement -> design -> tasks seam, but one more live adopter is still needed so the pattern reads as reusable planning structure rather than one methodology lineage plus one import.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0055](../techniques/agent-workflows/requirements-design-tasks-ladder/TECHNIQUE.md) | Pre-execution planning sibling that keeps requirements, design, and tasks visibly separate with clear exclusions around templates, steering, and full methodology doctrine. | One second public workflow surface where requirement, design, and task layers remain visibly distinct before implementation without widening into a full spec-driven methodology stack. |

### Pack 13 - Channelized Mailbox

Shared blocker: the donor and repo-local adaptation both show a bounded named-channel mailbox seam, but one more live adopter is still needed so the pattern reads as reusable coordination infrastructure rather than one messaging repository lineage plus one import.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0056](../techniques/agent-workflows/channelized-agent-mailbox/TECHNIQUE.md) | Durable mailbox sibling that keeps named channels, ordered replay, and explicit acknowledgment visible with clear exclusions around handoff governance and full messaging-platform doctrine. | One second public workflow surface where named channels, replay, and explicit acknowledgment survive session gaps in practice without widening into orchestration policy, transcript history, or messaging-platform breadth. |

### Pack 14 - Structured Handoff Before Compaction

Shared blocker: the donor pair and repo-local adaptation both show a bounded pre-compaction handoff seam, but one more live adopter is still needed so the pattern reads as reusable continuation infrastructure rather than one episode-orchestrator lineage plus one import.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0057](../techniques/agent-workflows/structured-handoff-before-compaction/TECHNIQUE.md) | Pre-compaction handoff sibling that keeps one explicit continuation packet visible with clear exclusions around transcript packaging, mailbox delivery, and broad phase governance. | One second public workflow surface where a structured handoff packet is written and read before context loss in practice without widening into transcript doctrine, delivery protocol, or orchestration governance. |

### Pack 15 - Receipt-Confirmed Handoff Packet

Shared blocker: the donor family and repo-local adaptation both show a bounded handoff-acceptance seam, but one more live adopter is still needed so the pattern reads as reusable continuation infrastructure rather than one snapshot-framework lineage plus one import.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0058](../techniques/agent-workflows/receipt-confirmed-handoff-packet/TECHNIQUE.md) | Handoff-acceptance sibling that keeps receipt explicit and continuation gated with clear exclusions around packet authoring, mailbox transport, and broader approval workflow doctrine. | One second public workflow surface where a receiving side explicitly records acceptance of a handoff packet before continuation without widening into queue governance, mailbox platforms, or broad approval policy. |

### Pack 16 - Git-Verified Handoff Claims

Shared blocker: the donor family and repo-local adaptation both show a bounded handoff-verification seam, but one more live adopter is still needed so the pattern reads as reusable continuation infrastructure rather than one overnight-agent lineage plus one import.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0059](../techniques/agent-workflows/git-verified-handoff-claims/TECHNIQUE.md) | Handoff-verification sibling that keeps concrete claims anchored to visible git evidence with clear exclusions around packet authoring, witness artifacts, and generic code-review doctrine. | One second public workflow surface where handoff claims are explicitly checked against recent repo state before continuation without widening into full review workflows, provenance systems, or orchestrator doctrine. |

### Pack 17 - Session Opening Ritual Before Work

Shared blocker: the donor family and repo-local adaptation both show a bounded session-opening seam, but one more live adopter is still needed so the pattern reads as reusable continuation infrastructure rather than one overnight-agent lineage plus one import.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0060](../techniques/agent-workflows/session-opening-ritual-before-work/TECHNIQUE.md) | Session-start sibling that keeps one visible pre-mutation read-and-verify ritual explicit with clear exclusions around task picking, startup test doctrine, and full boot or orchestration stacks. | One second public workflow surface where resumed sessions visibly re-read current context and verify baseline state before the first edit without widening into task routing, startup test suites, or mission-governance doctrine. |

### Pack 18 - Cross-Repo Resource Map Bootstrap

Shared blocker: the donor family and repo-local adaptation both show a bounded cross-repo startup seam, but one more live adopter is still needed so the pattern reads as reusable continuation infrastructure rather than one workspace-platform lineage plus one import.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0061](../techniques/agent-workflows/cross-repo-resource-map-bootstrap/TECHNIQUE.md) | Cross-repo bootstrap sibling that keeps one task-bounded repo-and-resource map explicit with clear exclusions around semantic context mapping, infrastructure inventory, and workspace-platform doctrine. | One second public workflow surface where multi-repo continuation begins from an explicit repo-and-resource startup map without widening into architecture inventories, topology stacks, or full workspace-platform doctrine. |

### Pack 19 - Episode-Bounded Agent Loop

Shared blocker: the donor family and repo-local adaptation both show a bounded episode-loop seam, but one more live adopter is still needed so the pattern reads as reusable continuation infrastructure rather than one overnight-agent lineage plus one import.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0062](../techniques/agent-workflows/episode-bounded-agent-loop/TECHNIQUE.md) | Episode-loop sibling that keeps longer work divided into explicit checkpointed slices with clear exclusions around startup ritual, handoff packet structure, and full autonomous-platform doctrine. | One second public workflow surface where longer work is segmented into checkpointed episodes with explicit continue, stop, or escalate decisions without widening into supervision stacks, budget systems, or total autonomous workflow governance. |

### Pack 20 - Versioned Agent Registry Contract

Shared blocker: the donor family and repo-local adaptation both show a bounded registry-entry seam, but one more live adopter is still needed so the pattern reads as reusable publication infrastructure rather than one directory-platform lineage plus one import.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0063](../techniques/docs/versioned-agent-registry-contract/TECHNIQUE.md) | Registry-entry sibling that keeps named versioned publication records explicit with clear exclusions around discovery policy, trust services, and registry product doctrine. | One second public workflow surface where named versioned registry entries remain explicit and reviewable without widening into marketplace curation, search policy, or directory-platform semantics. |

### Pack 21 - Capability Discovery

Shared blocker: the donor family and repo-local adaptation both show a bounded discovery-query seam, but one more live adopter is still needed so the pattern reads as reusable lookup infrastructure rather than one directory-platform lineage plus one import.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0064](../techniques/docs/capability-discovery/TECHNIQUE.md) | Discovery-query sibling that keeps capability lookup explicit through bounded fields, match rules, and result shape with clear exclusions around ranking, trust policy, and registry product doctrine. | One second public workflow surface where published capability records are discovered through explicit bounded queries without widening into marketplace curation, graph semantics, or directory-platform semantics. |

### Pack 22 - MCP Gateway Proxy

Shared blocker: the donor family and repo-local adaptation both show a bounded runtime proxy seam, but one more live adopter is still needed so the pattern reads as reusable gateway mediation rather than one gateway-product lineage plus one import.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0065](../techniques/agent-workflows/mcp-gateway-proxy/TECHNIQUE.md) | Runtime-proxy sibling that keeps one explicit gateway seam in front of configured MCP servers with clear exclusions around scanner modes, lifecycle doctrine, and registry or product semantics. | One second public workflow surface where several configured tool servers are fronted through one explicit proxy seam with visible metadata and mediated calls, without widening into enterprise security or runtime-platform doctrine. |

### Pack 23 - Transcript Replay Artifact

Shared blocker: the donor family and repo-local adaptation both show a bounded post-capture replay seam, but one more live adopter is still needed so the pattern reads as reusable session-history replay rather than one viewer-product lineage plus one import.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0066](../techniques/history/transcript-replay-artifact/TECHNIQUE.md) | Replay-artifact sibling that keeps post-capture session replay explicit with clear exclusions around transcript packaging, witness export, and hosted viewer-platform doctrine. | One second public workflow surface where already-saved sessions are replayed as bounded review artifacts without widening into hosted sharing, dashboard products, or replay-platform semantics. |

### Pack 24 - Transcript-Linked Code Lineage

Shared blocker: the donor family and repo-local adaptation both show a bounded code-to-evidence provenance seam, but one more live adopter is still needed so the pattern reads as reusable lineage infrastructure rather than one analytics-product lineage plus one import.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0067](../techniques/history/transcript-linked-code-lineage/TECHNIQUE.md) | Provenance-link sibling that keeps code anchors tied to saved session evidence with clear exclusions around dashboards, scorecards, and retrieval-product doctrine. | One second public workflow surface where code review or blame can reopen saved session evidence through stable code-to-evidence links without widening into analytics dashboards or hosted search product behavior. |

### Pack 25 - Fail-Closed Evidence Gate

Shared blocker: the donor family and repo-local adaptation both show a bounded execution-boundary gate seam, but one more live adopter is still needed so the pattern reads as reusable fail-closed control rather than one policy-platform lineage plus one import.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0068](../techniques/agent-workflows/fail-closed-evidence-gate/TECHNIQUE.md) | Execution-gate sibling that keeps explicit allow versus blocked side effects plus reviewable evidence with clear exclusions around human confirmation, durable-job orchestration, and total policy-platform doctrine. | One second public workflow surface where non-allow outcomes truly block side effects and leave reviewable evidence without widening into full governance, trust, or platform-policy semantics. |

### Pack 26 - Approval-Bound Durable Jobs

Shared blocker: the donor family and repo-local adaptation both show a bounded durable-job seam, but one more live adopter is still needed so the pattern reads as reusable approval-bound continuity rather than one orchestration-platform lineage plus one import.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0069](../techniques/agent-workflows/approval-bound-durable-jobs/TECHNIQUE.md) | Durable-job sibling that keeps checkpoint, pause, approval, and resume explicit with clear exclusions around scheduler products, queue platforms, and broad orchestration doctrine. | One second public workflow surface where longer-running work survives across an explicit approval seam and resumes from durable state without widening into scheduler platforms or orchestration-product semantics. |

## Suggested Wave Order

1. `Wave A - evidence-prep leaders`
   - `AOA-T-0032`, `AOA-T-0026`, `AOA-T-0036`
   - goal: close the smallest honest blocker for the strongest current candidates without flipping status yet
2. `Wave B - pack proof waves`
   - shell-agent fast path
   - runtime operator stack
   - instruction-surface cluster
   - history artifacts
   - goal: secure one more live adopter per coherent pack, then reopen bundle-local canonical reviews
3. `Wave C - fresh extraction follow-through`
   - `AOA-T-0046`, `AOA-T-0047`, `AOA-T-0048`
   - goal: add second-context and canonical-readiness scaffolding only after a real non-origin consumer exists
4. `Wave D - narrow status-transition PRs`
   - open one `promoted -> canonical` PR per technique only after that bundle's own `canonical-readiness.md` can honestly switch to `approve for canonical promotion`

## Notes

- This matrix is a maintainer-facing queue, not a replacement for bundle-local evidence notes.
- `promoted` is still the correct status for every bundle listed here today.
- If a future wave changes a bundle's status, update the bundle first, then `TECHNIQUE_INDEX.md`, then regenerate and validate shared surfaces.
