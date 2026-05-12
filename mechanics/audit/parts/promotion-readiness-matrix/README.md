# Promotion Readiness Matrix

This doc records the current bundle-by-bundle promotion queue for the `promoted` corpus in `aoa-techniques`.

Use it when the question is not "which repo-wide closure wave should open next?", but "which promoted bundle can be honestly strengthened next, and what proof is still missing before `promoted -> canonical` is real?"

This doc complements [Roadmap](../../../../ROADMAP.md) and [Long-Gap Canon Design](../../../distillation/parts/long-gap-reentry/README.md).
Bundle meaning still lives in each `TECHNIQUE.md` and `notes/canonical-readiness.md`.
For the current actionable first wave, open [Promotion Evidence Runbook](../promotion-evidence-runbook/README.md).

## Current Posture

- current promoted corpus: `56` techniques
- matrix categorization status: `56` promoted techniques are explicitly categorized in the pack matrix below; Wave 0 matrix expansion is closed for `AOA-T-0075` through `AOA-T-0107`
- current approve-now queue: none
- closest current queue item: [AOA-T-0032](../../../../techniques/proof/evaluation-chain/context-report-for-ci/TECHNIQUE.md), because it now leads the remaining active Wave A set and has the clearest report-only contract among the still-promoted bundles
- latest graduation wave: [AOA-T-0062](../../../../techniques/continuity/handoff-continuation/episode-bounded-agent-loop/TECHNIQUE.md) moved to `canonical` on 2026-05-12 after exact-fit public reinforcement from Cloudflare's long-running Agents guide: durable plans split long-running work into ordered steps, execute one step at a time, checkpoint and recover state, schedule the next step only after completion, mark failed steps without silent continuation, and keep re-planning plus human oversight as review boundaries, while keeping Durable Objects, Workers, schedules, fibers, Workflows, sub-agent RPC, proof gates, context compression, and total platform lifecycle governance outside the bundle
- prior graduation wave: [AOA-T-0061](../../../../techniques/continuity/handoff-continuation/cross-repo-resource-map-bootstrap/TECHNIQUE.md) moved to `canonical` on 2026-05-12 after exact-fit public reinforcement from `calltelemetry/openclaw-linear-plugin`'s multi-repo dispatch map: configured repo keys and paths, issue or label selected repo sets, named per-repo worktree paths, injected project context, and first-read `CLAUDE.md` / `AGENTS.md` guidance, while keeping issue routing, model selection, worktree lifecycle, audit loops, semantic context maps, infrastructure inventories, and workspace-platform governance outside the bundle
- prior graduation wave: [AOA-T-0060](../../../../techniques/continuity/handoff-continuation/session-opening-ritual-before-work/TECHNIQUE.md) moved to `canonical` on 2026-05-12 after exact-fit public reinforcement from `anthropics/cwc-long-running-agents`' `Always start here` convention: read `PROGRESS.md` before anything else, then run `git log --oneline -10` and a smoke/build/test baseline check before work, while keeping handoff authoring, git-claim verification, startup test doctrine, task routing, and long-running-harness governance outside the bundle
- prior graduation wave: [AOA-T-0057](../../../../techniques/continuity/handoff-continuation/structured-handoff-before-compaction/TECHNIQUE.md) moved to `canonical` on 2026-05-12 after exact-fit public reinforcement from `anthropics/cwc-long-running-agents`' structured `PROGRESS.md` restart convention plus `openclaw-memory-kit`'s compaction memoryFlush and bootstrap handoff path, while keeping transcript packaging, mailbox receipt, git verification, memory search, hook policy, cron memory, and long-running-harness doctrine outside the bundle
- latest evidence pass: [AOA-T-0059](../../../../techniques/continuity/handoff-continuation/git-verified-handoff-claims/TECHNIQUE.md) remains `promoted` after the 2026-05-12 Pack 16 search ruled out `confab-framework`, `LifeOS`, `session-handoff`, Mimir, SLOPE, and `cwc-long-running-agents` lanes as adjacent or partial rather than clean proof of receiver-side verified/mismatched/unverifiable handoff-claim outcomes against git evidence before continuation
- latest evidence pass: [AOA-T-0058](../../../../techniques/continuity/handoff-continuation/receipt-confirmed-handoff-packet/TECHNIQUE.md) remains `promoted` after the 2026-05-12 Pack 15 search ruled out `cmux` request ACKs, Gas Town handoff mail/session cycling/escalation ACKs, and exact phrase GitHub code-search lanes as adjacent rather than proof of receiver-side acceptance of a specific handoff packet before continuation
- prior graduation wave: [AOA-T-0056](../../../../techniques/continuity/handoff-continuation/channelized-agent-mailbox/TECHNIQUE.md) moved to `canonical` on 2026-05-12 after exact-fit public reinforcement from `mycel`'s AI-agent mailbox, thread identity, replayable thread log, sync cursor, outbox retry, read/delivery state, and explicit local ACK rows, while keeping ACK semantics separate from remote delivery proof and handoff authorization
- prior graduation wave: [AOA-T-0055](../../../../techniques/execution/ready-work-graphs/requirements-design-tasks-ladder/TECHNIQUE.md) moved to `canonical` on 2026-05-12 after exact-fit public reinforcement from SpecForge-Agent's requirement, design, and task artifact sequence before implementation, with GitHub Spec Kit used as supporting boundary evidence rather than methodology import
- prior graduation wave: [AOA-T-0054](../../../../techniques/continuity/review-compaction/compaction-resilient-skill-loading/TECHNIQUE.md) moved to `canonical` on 2026-05-12 after exact-fit public reinforcement from Claude Code's official skill content lifecycle, including post-compaction reattachment and re-invocation from canonical skill sources
- prior graduation wave: [AOA-T-0051](../../../../techniques/continuity/review-compaction/commit-triggered-background-review/TECHNIQUE.md) and [AOA-T-0052](../../../../techniques/continuity/review-compaction/review-findings-compaction/TECHNIQUE.md) moved to `canonical` on 2026-05-12 after exact-fit public reinforcement from Qodo / PR-Agent's push-triggered review updates, persistent review comments, visible findings, incremental update behavior, and per-commit findings added/resolved audit trail
- prior graduation wave: [AOA-T-0049](../../../../techniques/execution/ready-work-graphs/dependency-aware-task-graph/TECHNIQUE.md) and [AOA-T-0050](../../../../techniques/execution/ready-work-graphs/ready-work-from-blocker-graph/TECHNIQUE.md) moved to `canonical` on 2026-05-12 after exact-fit public reinforcement from Taskwarrior's dependency, blocked / blocking, unblocked, cycle-prevention, and prerequisite-completion behavior
- prior graduation wave: [AOA-T-0033](../../../../techniques/instruction/docs-boundary/decision-rationale-recording/TECHNIQUE.md) moved to `canonical` on 2026-05-12 after exact-fit public reinforcement from MADR's one-decision record template and own decision-record practice
- prior graduation wave: [AOA-T-0045](../../../../techniques/history/history-artifacts/witness-trace-as-reviewable-artifact/TECHNIQUE.md) moved to `canonical` on 2026-05-12 after exact-fit public reinforcement from Maida / AgentDbg's local run trace contract
- prior graduation wave: [AOA-T-0024](../../../../techniques/instruction/instruction-surface/upstream-mirroring-with-provenance/TECHNIQUE.md), [AOA-T-0025](../../../../techniques/instruction/capability-registry/capability-spec-versioning/TECHNIQUE.md), [AOA-T-0040](../../../../techniques/instruction/capability-boundary/skill-vs-command-boundary/TECHNIQUE.md), [AOA-T-0041](../../../../techniques/instruction/skill-discovery/skill-marketplace-curation/TECHNIQUE.md), and [AOA-T-0043](../../../../techniques/instruction/capability-boundary/multi-source-primary-input-provenance/TECHNIQUE.md) moved to `canonical` on 2026-05-12 after exact-fit public reinforcement from managedcode/dotnet-skills, A2A Agent Card, Claude Code skills, VoltAgent awesome-agent-skills, and StableNexus source-method surfaces
- prior graduation wave: [AOA-T-0027](../../../../techniques/instruction/instruction-surface/cross-agent-skill-propagation/TECHNIQUE.md), [AOA-T-0029](../../../../techniques/instruction/instruction-surface/nested-rule-loading/TECHNIQUE.md), and [AOA-T-0030](../../../../techniques/instruction/instruction-surface/fragmented-agent-context/TECHNIQUE.md) moved to `canonical` on 2026-05-12 after exact-fit public reinforcement from ai-rulez's managed skill/rule fan-out, Claude Code's layered memory/rules precedence, and Cline Rules' fragment-first rule/context source layer
- prior graduation wave: [AOA-T-0038](../../../../techniques/execution/runtime-truth-lifecycle/one-command-service-lifecycle/TECHNIQUE.md) and [AOA-T-0039](../../../../techniques/execution/runtime-truth-lifecycle/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) moved to `canonical` on 2026-05-12 after exact-fit public reinforcement from Metaflow Devstack's one-entrypoint local lifecycle surface and LOCOMO / OpenClaw's baseline-first additive benchmark surface
- prior graduation wave: [AOA-T-0037](../../../../techniques/execution/runtime-truth-lifecycle/contextual-host-doctor/TECHNIQUE.md) moved to `canonical` on 2026-05-12 after exact-fit public reinforcement from Get Physics Done's selected-runtime `gpd doctor` readiness surface
- earlier same-day graduation wave: [AOA-T-0036](../../../../techniques/execution/runtime-truth-lifecycle/render-truth-before-startup/TECHNIQUE.md) moved to `canonical` on 2026-05-12 after exact-fit public reinforcement from Dockform's plan/render-before-apply operator seam
- earlier same-day graduation wave: [AOA-T-0026](../../../../techniques/history/history-artifacts/session-capture-as-repo-artifact/TECHNIQUE.md) moved to `canonical` on 2026-05-12 after exact-fit public reinforcement from Aider's `.aider.chat.history.md` session-artifact family and committed public repository examples
- earlier graduation wave: [AOA-T-0028](../../../../techniques/execution/agent-workflows-core/confirmation-gated-mutating-action/TECHNIQUE.md), [AOA-T-0031](../../../../techniques/execution/agent-workflows-core/shell-composable-agent-invocation/TECHNIQUE.md), [AOA-T-0044](../../../../techniques/history/history-artifacts/versionable-session-transcripts/TECHNIQUE.md), and [AOA-T-0053](../../../../techniques/history/history-artifacts/local-first-session-index/TECHNIQUE.md) moved to `canonical` on 2026-03-28 after exact-fit public reinforcement from GitHub Copilot coding-agent approvals, OpenAI Codex CLI `codex exec`, `claude-code-log`, and `coding-agent-search (cass)`
- dominant blocker: most promoted bundles already have examples, checks, second-context adaptation, and canonical-readiness notes; the missing proof is usually one more live downstream adopter beyond the donor or documentation-first adaptation
- fresh extraction watch: [AOA-T-0048](../../../../techniques/knowledge-lift/kag-source-lift/semantic-review-surface-lift/TECHNIQUE.md), [AOA-T-0097](../../../../techniques/recovery/antifragility-recovery/degrade-reground-recover/TECHNIQUE.md), [AOA-T-0098](../../../../techniques/recovery/antifragility-recovery/receipt-first-failure-analysis/TECHNIQUE.md), [AOA-T-0099](../../../../techniques/recovery/antifragility-recovery/isolated-service-stop-on-shared-substrate/TECHNIQUE.md), [AOA-T-0100](../../../../techniques/recovery/antifragility-recovery/stress-receipt-reground-closeout/TECHNIQUE.md), [AOA-T-0105](../../../../techniques/proof/review-evidence/single-missing-evidence-request/TECHNIQUE.md), [AOA-T-0106](../../../../techniques/proof/review-evidence/single-scoped-evidence-reference/TECHNIQUE.md), and [AOA-T-0107](../../../../techniques/proof/review-evidence/single-locus-claim-challenge/TECHNIQUE.md) still need second-context evidence before canonical discussion is honest
- latest evidence-prep follow-through: [AOA-T-0046](../../../../techniques/knowledge-lift/kag-source-lift/repo-doc-surface-lift/TECHNIQUE.md) and [AOA-T-0047](../../../../techniques/knowledge-lift/kag-source-lift/github-review-template-lift/TECHNIQUE.md) gained first second-context support on 2026-05-12 from `nuxt-content/nuxt-llms` and GitHub's issue / pull request template surfaces, but remain `promoted` while stronger default-use evidence is still missing

## Manual-first questbook pilot lane

The March 31 manual-first questbook pilot closed `AOA-TECH-Q-0002` by carrying one
surviving donor and promotion debt forward without widening technique bodies.

- The active narrowing lane stays visible in [Cross-Layer Technique Candidates](../../../distillation/parts/cross-layer-candidate-ledger/README.md) as `phase-synchronized-agent-handoff`, rather than being promoted into a premature technique import.
- The proof-alignment follow-through moved outward to the sibling source/proof quests `AOA-SK-Q-0002` and `AOA-EV-Q-0002`, instead of bloating this matrix into a cross-repo backlog.
- This matrix keeps readiness and donor signals readable, while `QUESTBOOK.md` carries only the deferred obligations that survive the bounded review.

## Wave A Pass 1 Snapshot

- exact-fit reinforcement confirmed:
  - [AOA-T-0018](../../../../techniques/knowledge-lift/kag-source-lift/markdown-technique-section-lift/TECHNIQUE.md)
    - `aoa-routing` confirms that source-owned section surfaces are real `expand` targets beyond the already-landed downstream evidence in `aoa-skills` and `aoa-evals`
- adjacent or insufficient on the current local search lanes:
  - [AOA-T-0013](../../../../techniques/instruction/instruction-surface/single-source-rule-distribution/TECHNIQUE.md)
  - [AOA-T-0023](../../../../techniques/execution/agent-workflows-core/stateless-single-shot-agent/TECHNIQUE.md)
  - [AOA-T-0032](../../../../techniques/proof/evaluation-chain/context-report-for-ci/TECHNIQUE.md)
  - [AOA-T-0034](../../../../techniques/instruction/docs-boundary/public-safe-artifact-sanitization/TECHNIQUE.md)
- no second independent local runtime consumer found in the searched lane:
  - [AOA-T-0036](../../../../techniques/execution/runtime-truth-lifecycle/render-truth-before-startup/TECHNIQUE.md)

This snapshot is about the current local sweep only.
It narrows the next search space and closes false-positive local lanes, but it does not replace later donor searches where those still remain honest.
`AOA-T-0018` has since exited this matrix through a separate follow-up canonical review.
`AOA-T-0013` has since exited this matrix through a separate follow-up canonical review after independent public reinforcement from `dyoshikawa/rulesync` and `EmberAGI/arbitrum-vibekit`.
`AOA-T-0034` has since exited this matrix through a separate follow-up canonical review after an exact-fit second-consumer pass around `Truth-Zeeker-AI-Public`.
`AOA-T-0023` has since exited this matrix through a separate follow-up canonical review after GitHub Copilot CLI's programmatic one-prompt path closed the missing external fast-path gap.
`AOA-T-0026` has since exited this matrix through a separate follow-up canonical review after Aider's public `.aider.chat.history.md` artifact family closed the missing capture-as-artifact gap.
`AOA-T-0036` has since exited this matrix through a separate follow-up canonical review after Dockform's plan/render-before-apply surface closed the missing render-truth review seam without widening into lifecycle, readiness, or deployment-preview authority.

## Readiness Lanes

| lane | count | meaning |
|---|---:|---|
| `long-gap donor lane` | `2` | Needs one explicit new external or source-family proof surface. Repo-local wording work will not close the gap. |
| `cross-context review-refresh lane` | `0` | No active promoted bundle remains in this lane right now; `AOA-T-0018` already exited through follow-up canonical review. |
| `second-corpus evidence-prep lane` | `1` | Needs another live markdown-first corpus, not just another note or example inside this repo. |
| `external live-adopter lane` | `13` | Already has donor intake, documentation-first adaptation, and canonical-readiness review; still needs another real adopter outside the donor repo. |
| `internal-origin second-consumer lane` | `34` | Internal or origin-lineage bundle needs another downstream consumer plus sibling-boundary reinforcement. |
| `fresh extraction lane` | `8` | Has origin evidence only, lacks second-context evidence, or is missing canonical-readiness scaffolding. The next step is second-context plus canonical-readiness work, not promotion debate. |
| `v0.4 matrix-expansion lane` | `0` | Wave 0 is now categorized below. Reopen only when generated promotion readiness shows a newer promoted bundle outside the pack matrix. |

## Swarm Rule

- main agent owns wave boundaries, bundle-level verdict discipline, shared docs, any later `TECHNIQUE_INDEX.md` edits, generated-surface sync, and final `python scripts/release_check.py`
- before that final release-check path, install local validator deps with `python -m pip install -r requirements-dev.txt`
- each worker owns one technique bundle at a time and stays inside its `TECHNIQUE.md`, `notes/`, `checks/`, and `examples/`
- workers do not edit `TECHNIQUE_INDEX.md`, generated surfaces, or repo-wide review docs while evidence-gathering is still in flight
- a status flip only becomes eligible after the bundle's own `notes/canonical-readiness.md` can honestly move from `defer for now` to `approve for canonical promotion`

## Pack Matrix

### Pack 1 - Long-Gap Donor Lanes

Shared blocker: each bundle still needs a specific new live proof surface, and another repo-local wording pass would be fake closure.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0005](../../../../techniques/execution/intent-chain/new-intent-rollout-checklist/TECHNIQUE.md) | Strong companion checklist to canonical [AOA-T-0004](../../../../techniques/execution/intent-chain/intent-plan-dry-run-contract-chain/TECHNIQUE.md), but still origin-heavy; the 2026-05-12 Stage 2 pass ruled out generic intent-classification, chatbot eval, and IBN benchmark lanes as adjacent. | One non-origin shared intent-chain rollout record showing the checklist used to add a new intent in practice. |
| [AOA-T-0022](../../../../techniques/knowledge-lift/kag-source-lift/risk-and-negative-effect-lift/TECHNIQUE.md) | Exact five-part `Risks` contract has one strong donor, not repeated reuse; the 2026-05-12 Stage 2 pass ruled out exact-heading public code search, sibling contrast surfaces, and broad AI risk frameworks as adjacent. | One second committed corpus reusing the same five-part `Risks` split without widening into generated policy or scoring. |

### Pack 2 - Shell-Agent Fast Path

Pack 2 is now closed: [AOA-T-0028](../../../../techniques/execution/agent-workflows-core/confirmation-gated-mutating-action/TECHNIQUE.md) exited to `canonical` after GitHub Copilot's public coding-agent approval surfaces confirmed that mutation stays behind one explicit operator gate, and [AOA-T-0031](../../../../techniques/execution/agent-workflows-core/shell-composable-agent-invocation/TECHNIQUE.md) exited to `canonical` after OpenAI Codex CLI confirmed a real stdin/stdout/file-first one-shot `codex exec` path.

### Pack 3 - Runtime Operator Stack

Shared blocker: the remaining row still needs one more live consumer without collapsing profile composition into the now-canonical runtime truth siblings.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0035](../../../../techniques/instruction/instruction-surface/profile-preset-composition/TECHNIQUE.md) | Docs-side runtime composition contract with clear sibling boundaries; the 2026-05-12 Stage 2 pass ruled out profile-only, option-preset, editor-profile, feature/template, overlay, and generic config-composition lanes as adjacent. | One second downstream consumer using reviewable module -> profile -> preset layering with preset-first resolution, first-appearance dedupe, and inspection before startup. |

`AOA-T-0037` has since exited this matrix through a separate follow-up canonical review after Get Physics Done's selected-runtime `gpd doctor` readiness surface closed the missing preflight proof gap without widening into render, lifecycle, permission, plan, build, smoke, or monitoring authority.
`AOA-T-0038` has since exited this matrix through a separate follow-up canonical review after Metaflow Devstack closed the missing one-entrypoint local lifecycle proof gap without widening into generic launcher, install wizard, deployment, or platform doctrine.
`AOA-T-0039` has since exited this matrix through a separate follow-up canonical review after LOCOMO / OpenClaw closed the missing baseline-first additive benchmark proof gap without widening into product scoring, benchmark-suite governance, or rolling baseline policy.

### Pack 4 - Instruction-Surface Cluster Residual

The instruction-surface promotion pass closed [AOA-T-0027](../../../../techniques/instruction/instruction-surface/cross-agent-skill-propagation/TECHNIQUE.md), [AOA-T-0029](../../../../techniques/instruction/instruction-surface/nested-rule-loading/TECHNIQUE.md), and [AOA-T-0030](../../../../techniques/instruction/instruction-surface/fragmented-agent-context/TECHNIQUE.md) as canonical rows after exact-fit public reinforcement from ai-rulez, Claude Code, and Cline. The residual Pack 4 row is now the report-only proof sibling below.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0032](../../../../techniques/proof/evaluation-chain/context-report-for-ci/TECHNIQUE.md) | Report-only sibling to canonical composition, not the composition engine itself; the latest public agent-markdown, prompt-eval CI, context-packing, token-budget, LLM-ready-docs, prompt-cost, context-compiler, context-drift, fragment-assembly, dependency-graph, and repo-quality lanes remain adjacent because they emit PR checks, eval matrices, before/after prompt reports, repo activity summaries, token/cost telemetry, packed-context outputs, badges, documentation conversion, generated context bundles, configuration drift checks, graph reports, or quality scores rather than the same read-only composition coverage-and-drift artifact. | One second repo or surface family using the same CI-facing context report as a read-only composition coverage/drift artifact rather than PR policy checks, prompt eval reports, activity summaries, token badges, repo-packing outputs, prompt cost estimates, LLM-ready-doc generation, context compilation, fragment assembly, graph context, or repo-quality scoring. |

`AOA-T-0013`, `AOA-T-0027`, `AOA-T-0029`, and `AOA-T-0030` now anchor distinct canonical instruction-surface defaults; `AOA-T-0032` remains promoted because it still needs a second exact-fit CI-facing composition report.

### Pack 5 - Skill Ecosystem And Curated Inputs

Pack 5 is now mostly closed. [AOA-T-0024](../../../../techniques/instruction/instruction-surface/upstream-mirroring-with-provenance/TECHNIQUE.md), [AOA-T-0025](../../../../techniques/instruction/capability-registry/capability-spec-versioning/TECHNIQUE.md), [AOA-T-0040](../../../../techniques/instruction/capability-boundary/skill-vs-command-boundary/TECHNIQUE.md), [AOA-T-0041](../../../../techniques/instruction/skill-discovery/skill-marketplace-curation/TECHNIQUE.md), and [AOA-T-0043](../../../../techniques/instruction/capability-boundary/multi-source-primary-input-provenance/TECHNIQUE.md) exited through canonical review after exact-fit public reinforcement. The residual blocker stays only on source-readiness health checking.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0042](../../../../techniques/instruction/skill-discovery/upstream-skill-health-checking/TECHNIQUE.md) | Pre-surface readiness verdict is bounded, but the 2026-05-12 Pack 5 search found only adjacent manifest/doctor, registry-update, and security-risk surfaces. | One second downstream consumer using the same source availability plus minimal manifest-readiness boundary before catalog or selector surfacing, without widening into install/update management, security scoring, registry governance, or generic monitoring. |

Closed Pack 5 rows: `AOA-T-0024`, `AOA-T-0025`, `AOA-T-0040`, `AOA-T-0041`, and `AOA-T-0043`.

### Pack 6 - KAG / Source-Lift Evidence Prep

Shared blocker: the remaining promoted family members still need more live markdown-first reuse, not more abstraction inside `aoa-techniques`.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0020](../../../../techniques/knowledge-lift/kag-source-lift/evidence-note-provenance-lift/TECHNIQUE.md) | Exact note-kind and note-path lift is still donor-family-shaped; the 2026-05-12 Pack 6 pass ruled out Agent Loom as adjacent because it has typed markdown records and paths but no accepted derived note-kind/path provenance manifest. | One second live markdown-first corpus beyond the current `aoa-evals` donor surface that lifts typed note kind and path into a derived reader or manifest. |
| [AOA-T-0046](../../../../techniques/knowledge-lift/kag-source-lift/repo-doc-surface-lift/TECHNIQUE.md) | First second-context support recorded from `nuxt-content/nuxt-llms`; still promoted because the external proof is framework `llms.txt` reader generation rather than another repo-owned route manifest. | One more non-origin repo-owned docs route manifest or reader proving that the bounded source-doc set stays explicit outside framework-specific LLM docs generation. |
| [AOA-T-0047](../../../../techniques/knowledge-lift/kag-source-lift/github-review-template-lift/TECHNIQUE.md) | First second-context support recorded from GitHub issue and pull request template behavior; still promoted because the external proof is platform-native intake rendering rather than a review-specific template manifest. | One public review-specific template manifest or intake reader that inventories authored templates without owning approval, triage, or review state. |
| [AOA-T-0048](../../../../techniques/knowledge-lift/kag-source-lift/semantic-review-surface-lift/TECHNIQUE.md) | Fresh extraction with origin evidence only; the 2026-05-12 Pack 6 pass ruled out AI review, code review summary, quality-report, and scoring lanes as adjacent. | First second-context adaptation plus canonical-readiness review after one non-origin authored semantic-review or boundary-review reader exists. |

### Pack 7 - History Artifacts

Pack 7 is closed. [AOA-T-0045](../../../../techniques/history/history-artifacts/witness-trace-as-reviewable-artifact/TECHNIQUE.md) moved to `canonical` after Maida / AgentDbg showed exact-fit public reinforcement for one local run trace artifact with run metadata, ordered events, state updates, tool and LLM calls, error and loop-warning evidence, redaction/truncation, and a human-readable timeline / summary panel.

### Pack 8 - Internal Docs Practice

Pack 8 is closed. [AOA-T-0033](../../../../techniques/instruction/docs-boundary/decision-rationale-recording/TECHNIQUE.md) moved to `canonical` after MADR showed exact-fit public reinforcement for one decision record with context/problem, considered options, chosen outcome with justification, and accepted consequences.

### Pack 9 - Graph Work Coordination

Pack 9 is closed. [AOA-T-0049](../../../../techniques/execution/ready-work-graphs/dependency-aware-task-graph/TECHNIQUE.md) and [AOA-T-0050](../../../../techniques/execution/ready-work-graphs/ready-work-from-blocker-graph/TECHNIQUE.md) moved to `canonical` after Taskwarrior showed exact-fit public reinforcement for dependency edges, cycle prevention, blocked / blocking state, unblocked reports, and prerequisite-completion behavior without requiring the technique to absorb Taskwarrior's urgency, scheduling, context, sync, or broader task-management surface.

### Pack 10 - Background Review Loop

Pack 10 is closed. [AOA-T-0051](../../../../techniques/continuity/review-compaction/commit-triggered-background-review/TECHNIQUE.md) and [AOA-T-0052](../../../../techniques/continuity/review-compaction/review-findings-compaction/TECHNIQUE.md) moved to `canonical` after Qodo / PR-Agent showed exact-fit public reinforcement for push-triggered review updates, persistent review comments, visible findings, incremental update behavior, and per-commit findings added/resolved audit trail without requiring either technique to absorb auto-fix, auto-approval, merge policy, chat, broad CI, or PR-governance behavior.

### Pack 11 - Post-Compaction Skill Recovery

Pack 11 is closed. [AOA-T-0054](../../../../techniques/continuity/review-compaction/compaction-resilient-skill-loading/TECHNIQUE.md) moved to `canonical` after Claude Code's official skills lifecycle showed exact-fit public reinforcement for invoked skills carried across auto-compaction within budget, re-attached after summary, and explicitly re-invokable when full content needs restoration without widening into memory recall, marketplace discovery, installer flow, arbitrary prompt-history replay, or full context reconstruction.

### Pack 12 - Planning Ladder

Pack 12 is closed. [AOA-T-0055](../../../../techniques/execution/ready-work-graphs/requirements-design-tasks-ladder/TECHNIQUE.md) moved to `canonical` after SpecForge-Agent showed exact-fit public reinforcement for a `requirements.md` -> `design.md` -> `tasks.md` planning ladder before implementation. GitHub Spec Kit also shows a visible `spec.md` -> `plan.md` -> `tasks.md` spine, but the bundle keeps that as boundary support rather than importing full SDD, command, constitution, hook, research, approval, agent-platform, memory, or implementation doctrine.

### Pack 13 - Channelized Mailbox

Pack 13 is closed. [AOA-T-0056](../../../../techniques/continuity/handoff-continuation/channelized-agent-mailbox/TECHNIQUE.md) moved to `canonical` after `mycel` showed exact-fit public reinforcement for an AI-agent mailbox with stable message identity, thread identity as a bounded lane, ordered thread logs, per-relay sync cursors, local outbox retry, read and delivery state, and explicit local ACK rows keyed by logical message ID. `MCP Agent Mail` was inspected as a close adjacent mailbox/ack surface, but its license rider keeps it out of the clean primary evidence role for this public canonical proof. The bundle keeps ACK state separate from remote delivery confirmation, handoff authorization, transcript history, trust policy, encryption, adapters, and full messaging-platform doctrine.

### Pack 14 - Structured Handoff Before Compaction

Pack 14 is closed. [AOA-T-0057](../../../../techniques/continuity/handoff-continuation/structured-handoff-before-compaction/TECHNIQUE.md) moved to `canonical` after `anthropics/cwc-long-running-agents` showed exact-fit public reinforcement for agent-maintained `PROGRESS.md` handoff notes that are read before restart, kept current after work items, and backed by git checkpoints because fresh sessions and context-window summaries lose detail. `openclaw-memory-kit` supports the compaction-specific boundary with a `memoryFlush` prompt that writes `memory/handoff.md` before compression and a bootstrap path that reads the handoff after wake-up or compaction. Codex and Hermes issue threads were inspected only as adjacent pressure, not primary proof. The bundle keeps structured continuation packets separate from transcript packaging, mailbox receipt, git verification, memory search, cron memory, hook policy, session databases, and full long-running-agent harnesses.

### Pack 15 - Receipt-Confirmed Handoff Packet

Shared blocker: the donor family and repo-local adaptation both show a bounded handoff-acceptance seam, but one more live adopter is still needed so the pattern reads as reusable continuation infrastructure rather than one snapshot-framework lineage plus one import.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0058](../../../../techniques/continuity/handoff-continuation/receipt-confirmed-handoff-packet/TECHNIQUE.md) | Handoff-acceptance sibling that keeps receipt explicit and continuation gated with clear exclusions around packet authoring, mailbox transport, and broader approval workflow doctrine. The 2026-05-12 Pack 15 pass ruled out `cmux` request ACKs, Gas Town handoff mail/session cycling/escalation ACKs, and exact phrase GitHub code-search lanes as adjacent. | One second public workflow surface where a receiving side explicitly records acceptance of a specific handoff packet before continuation without widening into queue governance, mailbox platforms, request/delivery ACKs, session auto-prime, escalation acknowledgment, or broad approval policy. |

### Pack 16 - Git-Verified Handoff Claims

Shared blocker: the donor family and repo-local adaptation both show a bounded handoff-verification seam, but one more live adopter is still needed so the pattern reads as reusable continuation infrastructure rather than one overnight-agent lineage plus one import.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0059](../../../../techniques/continuity/handoff-continuation/git-verified-handoff-claims/TECHNIQUE.md) | Handoff-verification sibling that keeps concrete claims anchored to visible git evidence with clear exclusions around packet authoring, witness artifacts, and generic code-review doctrine. The 2026-05-12 Pack 16 pass ruled out broad claim gates, outbound handoff capture, pickup git-status checks, decision-record handoff summaries, compaction state, and progress-plus-git-checkpoint lanes as adjacent or partial. | One second public workflow surface where inbound handoff claims are explicitly checked against recent git evidence and recorded as verified, mismatched, or unverifiable before continuation without widening into full review workflows, provenance systems, generic claim hygiene, outbound handoff generation, or orchestrator doctrine. |

### Pack 17 - Session Opening Ritual Before Work

Pack 17 is closed. [AOA-T-0060](../../../../techniques/continuity/handoff-continuation/session-opening-ritual-before-work/TECHNIQUE.md) moved to `canonical` after `anthropics/cwc-long-running-agents` showed exact-fit public reinforcement for a pre-mutation opening ritual: read `PROGRESS.md` before doing anything else, run `git log --oneline -10`, and run a project smoke/build/test baseline check before work without requiring this bundle to absorb handoff authoring, detailed git-claim verification, task picking, baseline test doctrine, evaluator loops, or full harness governance.

### Pack 18 - Cross-Repo Resource Map Bootstrap

Pack 18 is closed. [AOA-T-0061](../../../../techniques/continuity/handoff-continuation/cross-repo-resource-map-bootstrap/TECHNIQUE.md) moved to `canonical` after `calltelemetry/openclaw-linear-plugin` showed exact-fit public reinforcement for a bounded cross-repo startup map: a configured `repos` map, issue-body or label selected repo sets, named per-repo worktree paths, project context injected into worker and audit prompts, and first-read `CLAUDE.md` / `AGENTS.md` guidance without requiring this bundle to absorb issue routing, model selection, worktree lifecycle, audit loops, semantic context maps, infrastructure inventories, or full workspace-platform governance.

### Pack 19 - Episode-Bounded Agent Loop

Pack 19 is closed. [AOA-T-0062](../../../../techniques/continuity/handoff-continuation/episode-bounded-agent-loop/TECHNIQUE.md) moved to `canonical` after Cloudflare's long-running Agents guide showed exact-fit public reinforcement for durable step-bounded agent work: plans break goals into ordered steps, execution runs one step at a time, checkpoint and plan state survive recovery, completed steps schedule the next step, failed steps do not silently advance, and re-planning plus human oversight stay visible review boundaries. Ax and Assay were inspected as adjacent pressure for context checkpointing and proof-gated episodes, but stayed out of the primary proof because they do not own the narrow long-running work episode loop.

### Pack 20 - Versioned Agent Registry Contract

Shared blocker: the donor family and repo-local adaptation both show a bounded registry-entry seam, but one more live adopter is still needed so the pattern reads as reusable publication infrastructure rather than one directory-platform lineage plus one import.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0063](../../../../techniques/instruction/capability-registry/versioned-agent-registry-contract/TECHNIQUE.md) | Registry-entry sibling that keeps named versioned publication records explicit with clear exclusions around discovery policy, trust services, and registry product doctrine. | One second public workflow surface where named versioned registry entries remain explicit and reviewable without widening into marketplace curation, search policy, or directory-platform semantics. |

### Pack 21 - Capability Discovery

Shared blocker: the donor family and repo-local adaptation both show a bounded discovery-query seam, but one more live adopter is still needed so the pattern reads as reusable lookup infrastructure rather than one directory-platform lineage plus one import.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0064](../../../../techniques/instruction/capability-registry/capability-discovery/TECHNIQUE.md) | Discovery-query sibling that keeps capability lookup explicit through bounded fields, match rules, and result shape with clear exclusions around ranking, trust policy, and registry product doctrine. | One second public workflow surface where published capability records are discovered through explicit bounded queries without widening into marketplace curation, graph semantics, or directory-platform semantics. |

### Pack 22 - MCP Gateway Proxy

Shared blocker: the donor family and repo-local adaptation both show a bounded runtime proxy seam, but one more live adopter is still needed so the pattern reads as reusable gateway mediation rather than one gateway-product lineage plus one import.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0065](../../../../techniques/tool-use/tool-gateway/mcp-gateway-proxy/TECHNIQUE.md) | Runtime-proxy sibling that keeps one explicit gateway seam in front of configured MCP servers with clear exclusions around scanner modes, lifecycle doctrine, and registry or product semantics. | One second public workflow surface where several configured tool servers are fronted through one explicit proxy seam with visible metadata and mediated calls, without widening into enterprise security or runtime-platform doctrine. |

### Pack 23 - Transcript Replay Artifact

Shared blocker: the donor family and repo-local adaptation both show a bounded post-capture replay seam, but one more live adopter is still needed so the pattern reads as reusable session-history replay rather than one viewer-product lineage plus one import.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0066](../../../../techniques/history/history-artifacts/transcript-replay-artifact/TECHNIQUE.md) | Replay-artifact sibling that keeps post-capture session replay explicit with clear exclusions around transcript packaging, witness export, and hosted viewer-platform doctrine. | One second public workflow surface where already-saved sessions are replayed as bounded review artifacts without widening into hosted sharing, dashboard products, or replay-platform semantics. |

### Pack 24 - Transcript-Linked Code Lineage

Shared blocker: the donor family and repo-local adaptation both show a bounded code-to-evidence provenance seam, but one more live adopter is still needed so the pattern reads as reusable lineage infrastructure rather than one analytics-product lineage plus one import.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0067](../../../../techniques/history/history-artifacts/transcript-linked-code-lineage/TECHNIQUE.md) | Provenance-link sibling that keeps code anchors tied to saved session evidence with clear exclusions around dashboards, scorecards, and retrieval-product doctrine. | One second public workflow surface where code review or blame can reopen saved session evidence through stable code-to-evidence links without widening into analytics dashboards or hosted search product behavior. |

### Pack 25 - Fail-Closed Evidence Gate

Shared blocker: the donor family and repo-local adaptation both show a bounded execution-boundary gate seam, but one more live adopter is still needed so the pattern reads as reusable fail-closed control rather than one policy-platform lineage plus one import.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0068](../../../../techniques/governance/approval-evidence/fail-closed-evidence-gate/TECHNIQUE.md) | Execution-gate sibling that keeps explicit allow versus blocked side effects plus reviewable evidence with clear exclusions around human confirmation, durable-job orchestration, and total policy-platform doctrine. | One second public workflow surface where non-allow outcomes truly block side effects and leave reviewable evidence without widening into full governance, trust, or platform-policy semantics. |

### Pack 26 - Approval-Bound Durable Jobs

Shared blocker: the donor family and repo-local adaptation both show a bounded durable-job seam, but one more live adopter is still needed so the pattern reads as reusable approval-bound continuity rather than one orchestration-platform lineage plus one import.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0069](../../../../techniques/governance/approval-evidence/approval-bound-durable-jobs/TECHNIQUE.md) | Durable-job sibling that keeps checkpoint, pause, approval, and resume explicit with clear exclusions around scheduler products, queue platforms, and broad orchestration doctrine. | One second public workflow surface where longer-running work survives across an explicit approval seam and resumes from durable state without widening into scheduler platforms or orchestration-product semantics. |

### Pack 27 - OCR Staged Handoff

Shared blocker: the donor OCR pair and repo-local adaptation both show a bounded OCR staging seam, but one more live adopter is still needed so the pattern reads as reusable document-processing infrastructure rather than one donor family plus one import.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0070](../../../../techniques/ingest/media-ingest/two-stage-document-ocr-pipeline/TECHNIQUE.md) | OCR-staging sibling that keeps detect or layout and recognize explicit before downstream extraction with clear exclusions around serving posture, benchmark doctrine, and receipt-specific field logic. | One second public workflow surface where OCR remains an explicit staged handoff with visible confidence and region references before later extraction or review without widening into a full document-understanding or automation stack. |

### Pack 28 - Post-OCR Template Field Extraction

Shared blocker: the donor parser family and repo-local adaptation both show a bounded post-OCR extraction seam, but one more live adopter is still needed so the pattern reads as reusable field-extraction infrastructure rather than one parser family plus one import.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0071](../../../../techniques/ingest/media-ingest/template-backed-field-extraction-after-ocr/TECHNIQUE.md) | Post-OCR extraction sibling that keeps one bounded field object explicit through templates or heuristics with clear exclusions around OCR-stage ownership, locale doctrine, and bookkeeping automation. | One second public workflow surface where OCR-derived text becomes a bounded field object through visible templates or heuristics with explicit missing or conflicting fields, without widening into receipt schema law, locale policy, or end-to-end document automation. |

### Pack 29 - Perceptual Media Dedupe

Shared blocker: the donor dedupe family and repo-local adaptation both show a bounded near-duplicate grouping seam, but one more live adopter is still needed so the pattern reads as reusable media-review infrastructure rather than one dedupe-tool family plus one import.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0072](../../../../techniques/ingest/media-ingest/perceptual-media-dedupe-with-threshold-review/TECHNIQUE.md) | Media-dedupe sibling that keeps perceptual grouping and review buckets explicit with clear exclusions around cleanup policy, semantic taxonomy, and quality-ranking doctrine. | One second public workflow surface where near-duplicate media are grouped through explicit thresholds and review buckets before later cleanup actions, without widening into semantic classification, archive policy, or bulk-delete automation. |

### Pack 30 - Semantic Media Bucketing

Shared blocker: the donor classification family and repo-local adaptation both show a bounded media-taxonomy seam, but one more live adopter is still needed so the pattern reads as reusable classification infrastructure rather than one multimodal donor family plus one import.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0073](../../../../techniques/ingest/media-ingest/semantic-media-bucketing-with-vision-plus-ocr/TECHNIQUE.md) | Media-bucketing sibling that keeps bounded taxonomy, OCR side text, and review gates explicit with clear exclusions around duplicate grouping, moderation policy, identity inference, and downstream action doctrine. | One second public workflow surface where mixed media are bucketed through bounded visual semantics plus OCR side text under explicit confidence gates before later routing or cleanup actions, without widening into moderation, identity inference, or open-ended multimodal automation. |

### Pack 31 - Telegram Export Normalization

Shared blocker: the donor Telegram family and repo-local adaptation both show a bounded source-normalization seam, but one more live adopter is still needed so the pattern reads as reusable local-storage infrastructure rather than one Telegram tooling family plus one import.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0074](../../../../techniques/ingest/media-ingest/telegram-export-normalization-to-local-store/TECHNIQUE.md) | Telegram-normalization sibling that keeps stable local objects, media references, provenance, and resume state explicit with clear exclusions around auth bootstrap, session conversion, and memory doctrine. | One second public workflow surface where Telegram-derived messages and media become a resumable local object store with visible provenance before later routing, recall, or memory actions, without widening into auth policy, session bridging, or archive-product doctrine. |

### Pack 32 - Reviewed Session Harvest Spine

Shared blocker: the session-harvest family is internally coherent and already source-backed, but still needs another live consumer so harvest packets read as portable post-session practice rather than one AoA skill-lineage export.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0075](../../../../techniques/continuity/donor-harvest/session-donor-harvest/TECHNIQUE.md) | Strong donor extraction contract for reviewed session artifacts, with explicit candidate units and evidence anchors. | One second live workflow where a reviewed artifact produces a bounded donor pack that later owner placement can consume without reopening live session memory. |
| [AOA-T-0077](../../../../techniques/continuity/donor-harvest/harvest-packet-contract/TECHNIQUE.md) | Packet spine is useful beside session donor harvest, but still origin-lineage shaped. | One second consumer that reads a `HARVEST_PACKET` as a bounded handoff into routing, diagnosis, repair, progression, or quest work without letting the packet become memory canon or routing authority. |

### Pack 33 - Owner Route Fork Discipline

Shared blocker: these bundles keep adjacent owner targets and branch choices distinct, but still need another downstream use where the rejection and fork discipline changes the outcome of real work.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0076](../../../../techniques/governance/decision-routing/owner-layer-triage/TECHNIQUE.md) | Central owner-placement primitive for one bounded reusable unit, already reinforced by several mechanics anchors. | One second non-origin owner-placement pass where a candidate chooses one primary owner, one next artifact, and one nearest wrong target. |
| [AOA-T-0078](../../../../techniques/governance/decision-routing/decision-fork-cards/TECHNIQUE.md) | Fork-card shape is clear, but still session-harvest-family heavy. | One live route where materially different next choices are captured as fork cards with gains, costs, owner targets, and stop conditions before action. |
| [AOA-T-0079](../../../../techniques/governance/decision-routing/risk-passport-lift/TECHNIQUE.md) | Risk passport keeps branch risk readable, but still needs an independent route choosing or rejecting work because of the passport. | One second workflow where route selection or defer posture depends on an explicit risk passport rather than a vague risk paragraph. |
| [AOA-T-0090](../../../../techniques/governance/promotion-boundary/nearest-wrong-target-rejection/TECHNIQUE.md) | Strong boundary companion to owner-layer triage and quest promotion. | One second owner-boundary review where explicitly rejecting the nearest wrong target prevents misplaced technique, skill, playbook, proof, memory, or route promotion. |

### Pack 34 - Diagnosis And Repair Loop

Shared blocker: diagnosis and repair are already split cleanly, but the family needs another reviewed failure route proving the order matters outside the originating session-repair skill line.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0080](../../../../techniques/recovery/diagnosis-repair/session-drift-taxonomy/TECHNIQUE.md) | Drift labels give diagnosis a bounded input layer without becoming full cause analysis. | One second reviewed friction case where taxonomy labels improve later diagnosis without becoming a repair plan. |
| [AOA-T-0081](../../../../techniques/recovery/diagnosis-repair/diagnosis-from-reviewed-evidence/TECHNIQUE.md) | Diagnosis packet separates symptoms, probable causes, owner hints, and unknowns. | One second reviewed evidence packet where diagnosis is produced before repair and remains read-only until a separate repair shape lands. |
| [AOA-T-0082](../../../../techniques/recovery/diagnosis-repair/repair-shape-from-diagnosis/TECHNIQUE.md) | Repair shaping stays smaller than rollout and starts only after diagnosis. | One second route where a diagnosis produces the smallest owner-facing repair artifact plus validation plan instead of general self-improvement prose. |
| [AOA-T-0083](../../../../techniques/recovery/diagnosis-repair/checkpoint-bound-self-repair/TECHNIQUE.md) | Checkpoint posture protects meaningful repair with approval, rollback, health check, iteration limit, and log visibility. | One second repair route where checkpoint posture governs the repair before mutation and catches overreach without widening into autonomous self-modification. |

### Pack 35 - Progression And Quest Reflection

Shared blocker: the progression family is useful as a reader layer, but still needs one independent context proving it improves legibility without granting rank, proof, route authority, or owner acceptance.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0084](../../../../techniques/continuity/donor-harvest/progression-evidence-lift/TECHNIQUE.md) | Multi-axis progression delta stays descriptive, evidence-backed, and smaller than a universal score. | One second reviewed session or route where explicit axes, holds, downgrades, or small unlock hints improve future work without becoming authority. |
| [AOA-T-0085](../../../../techniques/continuity/donor-harvest/multi-axis-quest-overlay/TECHNIQUE.md) | Quest or RPG reflection remains adjunct over a progression base. | One second reader surface where quest-shaped reflection improves legibility while the underlying owner truth, proof, and memory seams remain elsewhere. |

### Pack 36 - Automation Opportunity Gates

Shared blocker: the automation family names fit, first landing, and approval burden well, but still needs another recurring manual route where the matrix blocks or redirects premature automation.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0086](../../../../techniques/agent-workflows/automation-fit-matrix/TECHNIQUE.md) | Fit matrix converts automation desire into evidence-backed readiness posture. | One second recurring route where determinism, proof posture, reversibility, or approval sensitivity changes the automation verdict. |
| [AOA-T-0087](../../../../techniques/agent-workflows/human-loop-to-first-landing/TECHNIQUE.md) | First-landing verdict keeps skill, playbook seed, technique candidate, repair quest, and defer outcomes distinct. | One second automation-facing route where a recurring human loop lands in the smallest honest next artifact instead of becoming hidden scheduling pressure. |
| [AOA-T-0088](../../../../techniques/agent-workflows/approval-sensitivity-check/TECHNIQUE.md) | Approval burden check downgrades seed-ready enthusiasm when checkpoint posture is missing. | One second automation candidate where rollback, self-change, or approval sensitivity forces checkpoint-required posture before any seed claim. |

### Pack 37 - Quest Promotion Verdict

Shared blocker: the quest verdict is clear, but still needs one repeated reviewed unit outside the originating quest-harvest skill line before canonical promotion is honest.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0089](../../../../techniques/governance/promotion-boundary/quest-unit-promotion-review/TECHNIQUE.md) | Good final verdict technique for one repeated reviewed quest-shaped unit. | One second repeated quest unit where the review keeps, defers, or promotes the unit with one owner target and one reason rather than collapsing repetition into generic reuse pressure. |

### Pack 38 - Workspace Boundary And Proof Loop

Shared blocker: these bundles are strong internal boundary tools for public repo work, but each still needs another owner-surface use beyond the current AoA workspace lineage.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0091](../../../../techniques/proof/owner-truth-closeout/workspace-root-ingress-and-mutation-gate/TECHNIQUE.md) | Workspace ingress plus mutation guard is already used in live AoA work, but remains workspace-lineage heavy. | One second federated or multi-root workspace where ingress and guard evidence prevents route confusion or unsafe mutation before edits. |
| [AOA-T-0092](../../../../techniques/proof/owner-truth-closeout/audit-to-closeout-proof-loop/TECHNIQUE.md) | Strong bridge from audit findings to live-confirmed closeout proof. | One second audit-remediation route where proof-backed closeout rests on named evidence instead of audit wording alone. |
| [AOA-T-0093](../../../../techniques/instruction/capability-boundary/recommendation-truth-vs-host-actionability/TECHNIQUE.md) | Useful boundary between correct recommendation and executable host action. | One second host or tool context where a true recommendation remains visible even though host actionability is blocked or routed elsewhere. |
| [AOA-T-0094](../../../../techniques/proof/owner-truth-closeout/canonical-owner-with-validated-mirror/TECHNIQUE.md) | Clean canonical-owner plus validated-mirror docs contract. | One second cross-repo mirror where explicit parity validation preserves owner metadata and vocabulary without making the mirror source truth. |
| [AOA-T-0095](../../../../techniques/proof/owner-truth-closeout/github-only-owner-endcap-with-reality-sync/TECHNIQUE.md) | GitHub-only owner endcap is clear for remote-owned issues and PRs. | One second remote-only owner route where merged GitHub anchors rebind staging state and prevent local seed truth from outliving reality. |
| [AOA-T-0096](../../../../techniques/proof/owner-truth-closeout/pinned-validation-matrix-before-generated-publish/TECHNIQUE.md) | Pinned validation protects generated publish from local/CI ref drift. | One second generated-publish route where workflow-pinned refs are checked before publication and catch a merge-readiness overclaim. |

### Pack 39 - Antifragility Recovery Fresh Scaffolding

Shared blocker: the recovery-wave bundles have strong technique bodies but currently fail generated promotion-readiness because their canonical-readiness notes are missing. The next move is scaffolding and second-context review, not promotion debate.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0097](../../../../techniques/recovery/antifragility-recovery/degrade-reground-recover/TECHNIQUE.md) | Recovery contract is useful, but canonical-readiness scaffolding is missing. | Add bundle-local canonical-readiness and second-context review, then seek one second degraded-mode use that regrounds against stronger sources without hidden repair theater. |
| [AOA-T-0098](../../../../techniques/recovery/antifragility-recovery/receipt-first-failure-analysis/TECHNIQUE.md) | Receipt-first failure reading is promising, but readiness scaffolding is missing. | Add bundle-local canonical-readiness and second-context review, then seek one second failure route that starts from receipts and separates facts from hypotheses. |
| [AOA-T-0099](../../../../techniques/recovery/antifragility-recovery/isolated-service-stop-on-shared-substrate/TECHNIQUE.md) | Isolated stop contract is bounded, but readiness scaffolding is missing. | Add bundle-local canonical-readiness and second-context review, then seek one second shared-substrate stop where target absence and substrate continuity are both verified. |
| [AOA-T-0100](../../../../techniques/recovery/antifragility-recovery/stress-receipt-reground-closeout/TECHNIQUE.md) | Stress closeout contract is promising, but readiness scaffolding is missing. | Add bundle-local canonical-readiness and second-context review, then seek one second stress event that records, regrounds, routes owners, and closes out from reviewed evidence. |

### Pack 40 - Method-Growth Extraction Family

Shared blocker: Method-growth extraction produced clean technique bundles, but they remain new internal-origin practice and need live reuse outside the extraction branch before canonical promotion is honest.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0101](../../../../techniques/governance/practice-adoption-lifecycle/local-pattern-adoption-gate/TECHNIQUE.md) | Good local adoption guardrail with explicit consent, compatibility, rollback, and retention watch. | One second local adoption route where upstream usefulness is held short of adoption until owner consent, compatibility, rollback, and retention are explicit. |
| [AOA-T-0102](../../../../techniques/governance/promotion-boundary/skill-proposal-handoff-packet/TECHNIQUE.md) | Clean technique-to-skill handoff packet that does not imply skill acceptance. | One second route where a technique-side review emits a bounded skill proposal and `aoa-skills` acceptance remains separate. |
| [AOA-T-0103](../../../../techniques/governance/practice-adoption-lifecycle/adopted-practice-retention-review/TECHNIQUE.md) | Retention review keeps adopted practice active only while evidence, usefulness, drift, and rollback stay visible. | One second adopted-practice review where keep, revise, quarantine, or retire posture changes because retention evidence is explicit. |
| [AOA-T-0104](../../../../techniques/governance/practice-adoption-lifecycle/superseded-practice-obsolescence-route/TECHNIQUE.md) | Obsolescence route preserves owner receipt, retained lesson, and provenance during supersession or deprecation review. | One second practice replacement where supersede, merge, reanchor, defer, drop, or deprecation review happens without losing provenance. |

### Pack 41 - Agon Handoff Extraction Family

Shared blocker: Agon handoff extraction produced a clean first technique bundle,
but it remains source-lineage heavy and needs a second live context before
canonical promotion is honest.

| technique | current posture | next honest promotion trigger |
|---|---|---|
| [AOA-T-0105](../../../../techniques/proof/review-evidence/single-missing-evidence-request/TECHNIQUE.md) | Good one-object evidence-request guardrail with clear boundaries from proof, evaluation, and Agon law. | One second review context where asking for exactly one missing evidence object narrows review without broad research, verdict overclaim, or proof theater. |
| [AOA-T-0106](../../../../techniques/proof/review-evidence/single-scoped-evidence-reference/TECHNIQUE.md) | Good one-reference artifact with clear boundaries from proof, evaluation adequacy, source-truth transfer, and Agon law. | One second docs, code-review, or generated-output context where offering exactly one scoped reference improves review without proof-by-link or source laundering. |
| [AOA-T-0107](../../../../techniques/proof/review-evidence/single-locus-claim-challenge/TECHNIQUE.md) | Good one-claim pressure guardrail with clear boundaries from proof, tone, adjudication, actor eligibility, and Agon law. | One second review context where challenging exactly one vulnerable claim locus improves review without broad debate, hidden verdict, or tone-as-evidence drift. |

## Suggested Wave Order

Closed wave:

- `Wave 0 - v0.4 matrix expansion` is complete for `AOA-T-0075` through
  `AOA-T-0107`; the rows above categorize every newer promoted bundle without
  changing status.

1. `Wave A - evidence-prep leaders`
   - `AOA-T-0032`
   - recently closed: `AOA-T-0026`, `AOA-T-0036`
   - goal: close the smallest honest blocker for the strongest current candidates without flipping status before bundle-local approval
2. `Wave B - pack proof waves`
   - shell-agent fast path
   - runtime operator stack
   - instruction-surface cluster
   - history artifacts
   - goal: secure one more live adopter per coherent pack, then reopen bundle-local canonical reviews
3. `Wave C - fresh extraction follow-through`
   - `AOA-T-0048`, `AOA-T-0097`,
     `AOA-T-0098`, `AOA-T-0099`, `AOA-T-0100`, `AOA-T-0105`,
     `AOA-T-0106`, `AOA-T-0107`
   - goal: add second-context and canonical-readiness scaffolding only after a real non-origin consumer exists
4. `Wave D - narrow status-transition PRs`
   - open one `promoted -> canonical` PR per technique only after that bundle's own `canonical-readiness.md` can honestly switch to `approve for canonical promotion`

## Notes

- This matrix is a maintainer-facing queue, not a replacement for bundle-local evidence notes.
- `promoted` is still the correct status for every bundle listed here today.
- If a future wave changes a bundle's status, update the bundle first, then `TECHNIQUE_INDEX.md`, then regenerate and validate shared surfaces.
