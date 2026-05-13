# External Evidence Ledger

This ledger records the current search memory for external-evidence work over the remaining `promoted` queue.

Use it when the question is not "what is the whole promotion queue?", but "which external lanes have already been checked, what was adjacent-only, and where should the next honest search start?"

This ledger complements [Promotion Readiness Matrix](../promotion-readiness-matrix/README.md), [Promotion Evidence Runbook](../promotion-evidence-runbook/README.md), and [External Evidence Sprint Runbook](../external-evidence-sprint-runbook/README.md).
It does not replace bundle-local `notes/`.

## Recording Rules

- log only real searched lanes, not hopeful ideas
- record adjacent fits when they would otherwise tempt a later false-positive rerun
- keep exact-fit closure notes short and point back to the bundle-local evidence when that becomes the real source
- expand this ledger when a new lane search happens or a bundle exits the queue

## Recent Closure Precedents

These are the most useful recent examples of what honest queue closure looked like.

| technique | closure surface | what it proved |
|---|---|---|
| [AOA-T-0018](../../../../techniques/knowledge-lift/kag-source-lift/markdown-technique-section-lift/TECHNIQUE.md) | `aoa-routing` after existing `aoa-skills` and `aoa-evals` downstream use | Markdown-first section surfaces are real `expand` targets in more than one downstream repo. |
| [AOA-T-0013](../../../../techniques/instruction/instruction-surface/single-source-rule-distribution/TECHNIQUE.md) | `dyoshikawa/rulesync` plus `EmberAGI/arbitrum-vibekit` | One-source instruction distribution can survive beyond the donor lineage as a real multi-target pattern. |
| [AOA-T-0034](../../../../techniques/instruction/docs-boundary/public-safe-artifact-sanitization/TECHNIQUE.md) | `Truth-Zeeker-AI-Public` | Public-safe sanitization is a real second-consumer surface, not just a prerequisite inside origin repos. |
| [AOA-T-0023](../../../../techniques/execution/agent-workflows-core/stateless-single-shot-agent/TECHNIQUE.md) | GitHub Copilot CLI's programmatic one-prompt fast path | A real shell-side single-shot operator path exists beyond donor documentation and local adaptation. |
| [AOA-T-0028](../../../../techniques/execution/agent-workflows-core/confirmation-gated-mutating-action/TECHNIQUE.md) | GitHub Copilot agent-mode terminal-command confirmation plus GitHub Copilot CLI tool approvals | Public coding-agent surfaces keep mutation behind one explicit operator approval seam instead of hiding it inside generic autonomy. |
| [AOA-T-0031](../../../../techniques/execution/agent-workflows-core/shell-composable-agent-invocation/TECHNIQUE.md) | OpenAI Codex CLI `codex exec` | A real stdin/stdout/file-first one-shot operator path exists beyond donor documentation and local adaptation. |
| [AOA-T-0026](../../../../techniques/history/history-artifacts/session-capture-as-repo-artifact/TECHNIQUE.md) | Aider plus committed public `.aider.chat.history.md` artifacts | Local AI coding session capture can survive as a project-visible Markdown artifact beyond the donor product family. |
| [AOA-T-0036](../../../../techniques/execution/runtime-truth-lifecycle/render-truth-before-startup/TECHNIQUE.md) | Dockform plan/render-before-apply plus masked full Compose render | Effective local runtime truth can be rendered, reviewed, and confirmed before startup without becoming lifecycle, readiness, deployment-preview, or secret-publication authority. |
| [AOA-T-0038](../../../../techniques/execution/runtime-truth-lifecycle/one-command-service-lifecycle/TECHNIQUE.md) | Metaflow Devstack | One local operator entrypoint can select services, resolve dependencies, start the local stack, wait through follow-through, expose the operator shell path, and tear the stack down without becoming generic launcher doctrine. |
| [AOA-T-0039](../../../../techniques/execution/runtime-truth-lifecycle/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) | LOCOMO / OpenClaw benchmark harness | Baseline and additive profile backends can reuse the same corpus, runner, artifact family, parallel path, and summary surface without turning comparison into product scoring or benchmark governance. |
| [AOA-T-0027](../../../../techniques/instruction/instruction-surface/cross-agent-skill-propagation/TECHNIQUE.md) | ai-rulez | A shared rules/context/skills source layer can generate multiple managed native agent-tool targets without turning target files into independent authorities or widening into marketplace, MCP, or profile policy. |
| [AOA-T-0029](../../../../techniques/instruction/instruction-surface/nested-rule-loading/TECHNIQUE.md) | Claude Code memory and rules | Parent, nested, user, project, and path-scoped rule layers can load through explicit hierarchy and priority without becoming multi-target fan-out or hidden prompt-control doctrine. |
| [AOA-T-0030](../../../../techniques/instruction/instruction-surface/fragmented-agent-context/TECHNIQUE.md) | Cline Rules | Agent-facing rules and project context can stay authored as topic-specific markdown fragments before any combined runtime context consumes them. |
| [AOA-T-0024](../../../../techniques/instruction/instruction-surface/upstream-mirroring-with-provenance/TECHNIQUE.md) | managedcode/dotnet-skills | Upstream-owned skill and agent sources can be fetched and pinned separately from catalog import, copied verbatim, and paired with sibling local metadata without making mirrored markdown the local canonical source. |
| [AOA-T-0025](../../../../techniques/instruction/capability-registry/capability-spec-versioning/TECHNIQUE.md) | A2A Agent Card | Agent-facing capability contracts can stay discoverable, versioned, capability-declared, and client-validated before optional operations are used. |
| [AOA-T-0040](../../../../techniques/instruction/capability-boundary/skill-vs-command-boundary/TECHNIQUE.md) | Claude Code skills | Reusable `SKILL.md` capability bodies, supporting files, direct invocation, automatic loading, and invocation-control fields keep skill meaning distinct from user-facing command timing and session controls. |
| [AOA-T-0041](../../../../techniques/instruction/skill-discovery/skill-marketplace-curation/TECHNIQUE.md) | VoltAgent awesome-agent-skills | A curated public skill collection can add editorial discoverability through sections, descriptions, and outbound source links without owning underlying skill meaning, installer behavior, or registry governance. |
| [AOA-T-0043](../../../../techniques/instruction/capability-boundary/multi-source-primary-input-provenance/TECHNIQUE.md) | StableNexus Research Desk methodology | A public bridge-style method can keep one primary source-document card distinct from supporting sources while separating external material, interpretation, and implications. |
| [AOA-T-0046](../../../../techniques/knowledge-lift/kag-source-lift/repo-doc-surface-lift/TECHNIQUE.md) | `nuxt-content/nuxt-llms` plus 8Dionysus public route map | A bounded docs reader and a repo-owned route-map manifest can point back to authored docs/status surfaces without becoming docs taxonomy, status policy, release authority, or sibling-owner truth. |
| [AOA-T-0044](../../../../techniques/history/history-artifacts/versionable-session-transcripts/TECHNIQUE.md) | `claude-code-log` | Already-saved session transcripts can survive as portable Markdown review artifacts beyond the donor product family. |
| [AOA-T-0045](../../../../techniques/history/history-artifacts/witness-trace-as-reviewable-artifact/TECHNIQUE.md) | Maida / AgentDbg | A local-first agent debugger can persist one run as `run.json` plus ordered `events.jsonl`, including LLM calls, tool calls, errors, state updates, loop-warning evidence, redaction/truncation, and a human-readable timeline / summary panel without turning the trace into memory writeback or promotion policy. |
| [AOA-T-0033](../../../../techniques/instruction/docs-boundary/decision-rationale-recording/TECHNIQUE.md) | Markdown Architectural Decision Records | A public decision-record practice can preserve one decision with context/problem, considered options, chosen outcome with justification, and accepted consequences without turning the note into source-of-truth governance, architecture taxonomy, or decision-log tooling ownership. |
| [AOA-T-0049](../../../../techniques/execution/ready-work-graphs/dependency-aware-task-graph/TECHNIQUE.md) | Taskwarrior | A public task workflow can keep dependency edges explicit, reject cycles, derive `BLOCKED` / `BLOCKING` state, and unblock downstream work when prerequisites complete without turning the graph into memory, dispatch, or project-management doctrine. |
| [AOA-T-0050](../../../../techniques/execution/ready-work-graphs/ready-work-from-blocker-graph/TECHNIQUE.md) | Taskwarrior | A public task workflow can surface blocked, blocking, and unblocked work so blocker-free state determines the next eligible frontier before urgency, scheduling, context, sync, or broader task-management behavior. |
| [AOA-T-0051](../../../../techniques/continuity/review-compaction/commit-triggered-background-review/TECHNIQUE.md) | Qodo / PR-Agent | A public review workflow can refresh review output after PR push or commit-like events, preserve visible findings as persistent review comments, and keep review artifacts distinct from auto-fix, auto-approval, merge, or CI-governance behavior. |
| [AOA-T-0052](../../../../techniques/continuity/review-compaction/review-findings-compaction/TECHNIQUE.md) | Qodo / PR-Agent | A public review workflow can update one current findings surface across repeated commits, keep added/resolved findings visible by commit, and fold previous suggestions into bounded history without becoming backlog, remediation, or merge policy. |
| [AOA-T-0054](../../../../techniques/continuity/review-compaction/compaction-resilient-skill-loading/TECHNIQUE.md) | Claude Code skills lifecycle | A public agent skill system can carry invoked skills across auto-compaction within a budget, re-attach recent skill invocations after summary, and allow explicit re-invocation after compaction without becoming long-term memory, marketplace, installer, or full prompt-restoration doctrine. |
| [AOA-T-0055](../../../../techniques/execution/ready-work-graphs/requirements-design-tasks-ladder/TECHNIQUE.md) | SpecForge-Agent plus GitHub Spec Kit boundary check | A public agent workflow can keep requirements, design, and task artifacts distinct before implementation, with design derived from approved requirements and tasks derived from design plus requirements, without making the technique absorb full SDD, command, approval, memory, or implementation doctrine. |
| [AOA-T-0056](../../../../techniques/continuity/handoff-continuation/channelized-agent-mailbox/TECHNIQUE.md) | `mycel` plus MCP Agent Mail license-bound adjacent check | A public AI-agent mailbox can keep stable message identity, bounded thread lanes, ordered replay, sync cursor, outbox retry, read/delivery state, and explicit local ACK rows without making ACKs remote delivery proof or absorbing handoff authorization, transcript history, trust policy, encryption, adapters, or messaging-platform doctrine. |
| [AOA-T-0057](../../../../techniques/continuity/handoff-continuation/structured-handoff-before-compaction/TECHNIQUE.md) | `cwc-long-running-agents` plus `openclaw-memory-kit` | A public long-running agent harness and a public OpenClaw memory kit both keep a structured progress or handoff packet visible before restart, compaction, or wake-up without making the packet a transcript, mailbox, git-verification, memory-search, hook-policy, cron-memory, or harness-governance system. |
| [AOA-T-0069](../../../../techniques/governance/approval-evidence/approval-bound-durable-jobs/TECHNIQUE.md) | `pydantic/pydantic-ai` plus LangGraph boundary check | A public agent framework can end an agent run on deferred approvals or external calls, preserve pending-call identity, resume with saved message history and deferred results, and pair that with durable execution support without making the technique a scheduler or workflow-platform doctrine. |
| [AOA-T-0070](../../../../techniques/ingest/media-ingest/two-stage-document-ocr-pipeline/TECHNIQUE.md) | `JaidedAI/EasyOCR` | A public OCR library can keep detection and recognition separately visible, return bounding boxes, recognized text, and confidence as one structured result, and leave downstream extraction or review outside the OCR handoff contract. |
| [AOA-T-0071](../../../../techniques/ingest/media-ingest/template-backed-field-extraction-after-ocr/TECHNIQUE.md) | `kotaro-kinoshita/yomitoku` | A public document extractor can use schema-defined field targets, visible rule methods, source metadata, confidence, and not-found posture to turn OCR/layout output into bounded fields without becoming OCR staging, LLM extraction, or accounting automation. |
| [AOA-T-0072](../../../../techniques/ingest/media-ingest/perceptual-media-dedupe-with-threshold-review/TECHNIQUE.md) | `qarmin/czkawka` | A public media dedupe tool can keep perceptual similarity, explicit threshold tuning, reviewable grouped output, and default-off deletion separate from semantic media taxonomy, ranking, archive policy, and cleanup automation. |
| [AOA-T-0073](../../../../techniques/ingest/media-ingest/semantic-media-bucketing-with-vision-plus-ocr/TECHNIQUE.md) | `end1989/ai-image-classification` | A public offline media sorter can keep configured mixed-media labels, CLIP scoring, OCR side-text confidence, review thresholds, user correction, and separated file actions visible without turning bucketing into moderation, identity inference, duplicate grouping, or cleanup policy. |
| [AOA-T-0074](../../../../techniques/ingest/media-ingest/telegram-export-normalization-to-local-store/TECHNIQUE.md) | `3bl3gamer/tg_history_dumper` | A public Telegram history dumper can preserve messages as local JSON Lines, media as message-linked files, related peers as JSONL side surfaces, and last-message-id continuation without turning normalization into auth, session, archive presentation, search, or memory doctrine. |
| [AOA-T-0075](../../../../techniques/continuity/donor-harvest/session-donor-harvest/TECHNIQUE.md) | `aoa-sdk` checkpoint-closeout bridge plus LangSmith reviewed-run curation | A live SDK control-plane consumer can reread reviewed artifacts and checkpoint-review carry into bounded donor candidates, while public reviewed-run curation supports the same pressure to turn reviewed traces into bounded downstream records without making them memory or final routing truth. |
| [AOA-T-0077](../../../../techniques/continuity/donor-harvest/harvest-packet-contract/TECHNIQUE.md) | `aoa-sdk` `HARVEST_PACKET` consumer plus LangSmith reviewed-run curation | A live SDK closeout path can write and later consume one bounded harvest packet with accepted candidates, evidence anchors, owner hints, next surfaces, and nearest-wrong-target posture without letting the packet become memory canon, routing authority, or final owner acceptance. |
| [AOA-T-0076](../../../../techniques/governance/decision-routing/owner-layer-triage/TECHNIQUE.md) | `aoa-playbooks` owner-followthrough/session-growth plus supporting `aoa-evals` owner-fit | Sibling downstream routes can require owner repo, owner shape, next artifact, and nearest-wrong-target posture before follow-through without turning playbooks, evals, routing, KAG, memo, SDK, or stats into first-authoring authority. |
| [AOA-T-0078](../../../../techniques/governance/decision-routing/decision-fork-cards/TECHNIQUE.md) | `aoa-playbooks` owner-followthrough plus evaluated `aoa-summon` boundary | Sibling route consumers can keep landing, seed staging, proof-first, reanchor, merge, defer, and drop branches explicit before action, while summon refuses to hide unresolved competing routes inside child execution. |
| [AOA-T-0079](../../../../techniques/governance/decision-routing/risk-passport-lift/TECHNIQUE.md) | `aoa-summon` plus `aoa-sdk` A2A summon assessment | Difficulty, risk, control mode, delegate tier, split, reviewed-lane, and human-gate posture can choose, narrow, or block child-route execution without becoming risk scoring, approval policy, or dispatch authority. |
| [AOA-T-0090](../../../../techniques/governance/promotion-boundary/nearest-wrong-target-rejection/TECHNIQUE.md) | `aoa-playbooks` / `aoa-techniques` quest carry plus supporting `aoa-evals` owner-fit | Explicit nearest-wrong rejection can prevent convenience promotion into skill, proof, memo, KAG, routing, runtime, stats, or premature playbook authority while staying smaller than the verdict workflow itself. |
| [AOA-T-0080](../../../../techniques/recovery/diagnosis-repair/session-drift-taxonomy/TECHNIQUE.md) | `aoa-skills` `abyss-self-diagnostic-spine` plus evaluated self-diagnose | A downstream runtime-diagnostic overlay can use bounded drift labels before probable cause, owner hint, exit class, or repair posture without making taxonomy a diagnosis or runtime schema. |
| [AOA-T-0081](../../../../techniques/recovery/diagnosis-repair/diagnosis-from-reviewed-evidence/TECHNIQUE.md) | `aoa-skills` `abyss-self-diagnostic-spine` plus evaluated self-diagnose | A downstream runtime-diagnostic overlay can emit one read-only diagnosis artifact with symptoms, probable causes, confidence, freshness, owner hints, and unknowns before repair. |
| [AOA-T-0082](../../../../techniques/recovery/diagnosis-repair/repair-shape-from-diagnosis/TECHNIQUE.md) | `aoa-sdk` closeout follow-through plus `aoa-skills` repair-cycle artifacts | A downstream closeout route can require diagnosis before surfacing bounded self-repair, and repair-cycle examples can preserve owner target, validation, rollback, approval, iteration, stop, and escalation posture without becoming playbook rollout. |
| [AOA-T-0083](../../../../techniques/recovery/diagnosis-repair/checkpoint-bound-self-repair/TECHNIQUE.md) | `aoa-agents` checkpoint stack, `aoa-playbooks` checkpoint rollout, and `aoa-skills` repair-cycle artifacts | Downstream role and scenario surfaces can keep approval, rollback, health checks, iteration, and improvement logs explicit around repair while techniques remain smaller than role law, proof, runtime, or playbook authority. |
| [AOA-T-0053](../../../../techniques/history/history-artifacts/local-first-session-index/TECHNIQUE.md) | `coding-agent-search (cass)` | A local searchable index over already-saved session artifacts can remain derivative, provenance-aware, and local-first beyond the donor product family. |
| [AOA-T-0084](../../../../techniques/continuity/donor-harvest/progression-evidence-lift/TECHNIQUE.md) | `aoa-skills` `aoa-session-progression-lift` | A downstream skill can use multi-axis progression deltas as descriptive evidence posture without turning them into rank, proof, routing, or owner acceptance. |
| [AOA-T-0085](../../../../techniques/continuity/donor-harvest/multi-axis-quest-overlay/TECHNIQUE.md) | `aoa-skills` `aoa-session-progression-lift` | Quest-shaped reflection can sit over a progression base as reader context while owner truth and proof seams remain elsewhere. |
| [AOA-T-0086](../../../../techniques/governance/automation-readiness/automation-fit-matrix/TECHNIQUE.md) | `aoa-skills` `aoa-automation-opportunity-scan` | Repeat-signal and readiness axes can block or narrow automation before scheduler or mutation authority exists. |
| [AOA-T-0087](../../../../techniques/governance/automation-readiness/human-loop-to-first-landing/TECHNIQUE.md) | `aoa-skills` `aoa-automation-opportunity-scan` | A recurring human loop can land as the smallest honest next artifact instead of becoming hidden automation pressure. |
| [AOA-T-0088](../../../../techniques/governance/automation-readiness/approval-sensitivity-check/TECHNIQUE.md) | `aoa-skills` `aoa-automation-opportunity-scan` | Approval burden, rollback, self-change, and checkpoint posture can force checkpoint-required status before any automation seed claim. |
| [AOA-T-0089](../../../../techniques/governance/promotion-boundary/quest-unit-promotion-review/TECHNIQUE.md) | `aoa-skills` `aoa-quest-harvest` plus `aoa-sdk` technique promotion receipt | One repeated reviewed quest unit can be triaged with one owner target and one reason without becoming skill, playbook, proof, memory, routing, or owner acceptance. |
| [AOA-T-0091](../../../../techniques/proof/owner-truth-closeout/workspace-root-ingress-and-mutation-gate/TECHNIQUE.md) | 8Dionysus shared-root ingress and mutation gate | Ingress and mutation guard evidence can prevent workspace route confusion before edits without importing root projection ownership. |
| [AOA-T-0092](../../../../techniques/proof/owner-truth-closeout/audit-to-closeout-proof-loop/TECHNIQUE.md) | `aoa-playbooks` closeout owner-followthrough and validation-remediation runs | Audit findings can close only through named evidence and owner follow-through rather than audit wording alone. |
| [AOA-T-0093](../../../../techniques/instruction/capability-boundary/recommendation-truth-vs-host-actionability/TECHNIQUE.md) | `aoa-sdk` skill-runtime recommendation gap | A true recommendation can remain visible when host actionability is blocked or routed elsewhere. |
| [AOA-T-0094](../../../../techniques/proof/owner-truth-closeout/canonical-owner-with-validated-mirror/TECHNIQUE.md) | 8Dionysus source projection and workspace install surfaces | Canonical owner and validated mirror can stay separate while parity validation preserves metadata and vocabulary. |
| [AOA-T-0095](../../../../techniques/proof/owner-truth-closeout/github-only-owner-endcap-with-reality-sync/TECHNIQUE.md) | 8Dionysus GitHub required-check contracts plus `aoa-playbooks` owner-first landing | Remote GitHub anchors can rebind staging state and prevent local seed truth from outliving merge reality. |
| [AOA-T-0096](../../../../techniques/proof/owner-truth-closeout/pinned-validation-matrix-before-generated-publish/TECHNIQUE.md) | `aoa-playbooks` split-wave cross-repo rollout | Workflow-pinned refs can expose generated-publish false-green risk before publication. |
| [AOA-T-0097](../../../../techniques/recovery/antifragility-recovery/degrade-reground-recover/TECHNIQUE.md) | `aoa-playbooks` runtime-chaos recovery and stress lanes | Degraded-mode recovery can reground against stronger sources without hidden repair theater. |
| [AOA-T-0098](../../../../techniques/recovery/antifragility-recovery/receipt-first-failure-analysis/TECHNIQUE.md) | `aoa-playbooks` runtime-chaos and stress-harvest surfaces | Failure reading can start from receipts and keep facts separate from hypotheses. |
| [AOA-T-0099](../../../../techniques/recovery/antifragility-recovery/isolated-service-stop-on-shared-substrate/TECHNIQUE.md) | `aoa-playbooks` ToS graph-curation run | An isolated helper service can be stopped while shared substrate continuity and target absence are verified. |
| [AOA-T-0100](../../../../techniques/recovery/antifragility-recovery/stress-receipt-reground-closeout/TECHNIQUE.md) | `aoa-playbooks` stress-lane and stress-harvest surfaces | Stress events can be recorded, regrounded, owner-routed, and closed from reviewed evidence. |
| [AOA-T-0101](../../../../techniques/governance/practice-adoption-lifecycle/local-pattern-adoption-gate/TECHNIQUE.md) | `aoa-skills` Method-growth adoption lifecycle | Local adoption can require owner consent, compatibility, rollback, and retention evidence before durable adoption. |
| [AOA-T-0102](../../../../techniques/governance/promotion-boundary/skill-proposal-handoff-packet/TECHNIQUE.md) | `aoa-skills` Method-growth skill proposal handoff | A technique-side review can emit a bounded skill proposal while `aoa-skills` acceptance remains separate. |
| [AOA-T-0103](../../../../techniques/governance/practice-adoption-lifecycle/adopted-practice-retention-review/TECHNIQUE.md) | `aoa-skills` Method-growth retention and regression checks | Adopted practice can be kept, revised, quarantined, or retired through explicit retention evidence. |
| [AOA-T-0104](../../../../techniques/governance/practice-adoption-lifecycle/superseded-practice-obsolescence-route/TECHNIQUE.md) | `aoa-skills` Method-growth retirement and handoff receipts | Superseded practice can preserve owner receipt, retained lesson, and provenance without automatic deletion. |
| [AOA-T-0105](../../../../techniques/proof/review-evidence/single-missing-evidence-request/TECHNIQUE.md) | Agents-of-Abyss Agon lawful moves, audit evidence ledger, playbook trials, and eval prebindings | A review can ask for exactly one missing evidence object without broad research, verdict overclaim, or proof theater. |
| [AOA-T-0106](../../../../techniques/proof/review-evidence/single-scoped-evidence-reference/TECHNIQUE.md) | Agents-of-Abyss Agon lawful moves, audit evidence ledger, playbook trials, and eval prebindings | A review can offer exactly one scoped reference without proof-by-link or source laundering. |
| [AOA-T-0107](../../../../techniques/proof/review-evidence/single-locus-claim-challenge/TECHNIQUE.md) | Agents-of-Abyss Agon lawful moves, audit evidence ledger, playbook trials, and eval prebindings | A review can challenge exactly one vulnerable claim locus without broad debate, hidden verdict, or tone-as-evidence drift. |

## AOA-T-0084 Through AOA-T-0107 Cross-Context Evidence Notes

2026-05-13 result: exact-fit downstream or second-context evidence found for Packs 35 through 41. This closed the newer promotion-evidence queue at the time; a later focused `AOA-T-0046` pass reduced the residual promoted set to 10 techniques.

This is sibling-repo and downstream-consumer evidence, not external import proof. Do not import skill execution, SDK implementation detail, 8Dionysus projection ownership, playbook scenario law, AoA constitutional law, Agon doctrine, eval verdicts, runtime repair authority, KAG graph ownership, routing, memo writeback, owner acceptance, or proof doctrine into the technique bundles.

Accepted evidence:

- `aoa-skills` `aoa-session-progression-lift` uses `AOA-T-0084` and `AOA-T-0085` through multi-axis progression delta, baseline posture, evidence posture, and quest reflection while keeping rank and owner acceptance outside the skill.
- `aoa-skills` `aoa-automation-opportunity-scan` uses `AOA-T-0086`, `AOA-T-0087`, and `AOA-T-0088` through repeat signal, automation fit, first landing, approval sensitivity, rollback, and checkpoint posture without scheduler or mutating authority.
- `aoa-skills` `aoa-quest-harvest` plus the SDK technique-promotion receipt surface reinforce `AOA-T-0089` as one repeated reviewed quest-unit verdict, not a final owner or playbook verdict.
- 8Dionysus shared-root ingress, workspace-install, source-projection, and GitHub required-check contract surfaces reinforce `AOA-T-0091`, `AOA-T-0094`, and `AOA-T-0095` as owner/mirror/GitHub closeout moves.
- `aoa-playbooks` owner-followthrough, validation-remediation, and split-wave rollout evidence reinforces `AOA-T-0092` and `AOA-T-0096` as proof-loop and pinned-validation moves, not playbook law.
- `aoa-sdk` skill-runtime recommendation-gap evidence reinforces `AOA-T-0093` as a recommendation/actionability boundary.
- `aoa-playbooks` runtime-chaos, stress-lane, stress-harvest, and ToS graph-curation surfaces reinforce `AOA-T-0097` through `AOA-T-0100` as recovery moves with visible stop-lines before runtime repair, KAG, proof, or eval authority.
- `aoa-skills` Method-growth adoption, handoff, retention, and obsolescence surfaces reinforce `AOA-T-0101` through `AOA-T-0104` as practice-lifecycle moves without importing skill promotion or deletion authority.
- Agents-of-Abyss Agon lawful-move grammar, Audit evidence-ledger contracts, `aoa-playbooks` Agon trials, and `aoa-evals` prebindings reinforce `AOA-T-0105` through `AOA-T-0107` as one-object review moves without importing Agon law or eval verdicts.

Rejected or bounded:

- skill workflow execution, activation, and scheduler behavior;
- SDK command wrappers, hooks, storage, and runtime APIs;
- 8Dionysus shared-root source ownership and projection implementation;
- playbook scenario composition, trial success, and owner-followthrough authority;
- AoA center doctrine, Agon law, eval adequacy, and proof verdicts;
- runtime self-healing, KAG graph ownership, routing, memo writeback, stats refresh, and final owner acceptance.

Future search shape: future reinforcement should look for non-AoA or external-builder reuse of the same atomic moves. It should not reopen the 2026-05-13 canonical verdict unless the bundle contract itself drifts or a downstream consumer starts relying on authority the bundle explicitly does not own.

## AOA-T-0046 Focused Route-Map Closure Notes

2026-05-13 result: exact-fit repo-owned route-manifest evidence found for [AOA-T-0046](../../../../techniques/knowledge-lift/kag-source-lift/repo-doc-surface-lift/TECHNIQUE.md).

Accepted evidence:

- `nuxt-content/nuxt-llms` remains the first route-reader support: configured docs sections and links render into a subordinate `llms.txt` reader without replacing authored docs.
- 8Dionysus closes the missing repo-owned route-manifest gap: `docs/PUBLIC_ENTRY_POSTURE.md` owns the onboarding route table, `scripts/public_route_map_common.py` derives and validates `generated/public_route_map.min.json`, and `tests/test_public_route_map.py` keeps the surface `route-map-only`, orientation-focused, and free of low-context implementation refs.

Rejected or bounded:

- 8Dionysus public-entry ownership;
- linked owner-repo authority;
- release or support semantics;
- general docs taxonomy;
- local planning docs, deeper guides, semantic reviews, and status-policy engines.

Future search shape: do not reopen `AOA-T-0046` unless a generated repo-doc reader starts replacing authored docs, a route manifest imports sibling-owner authority, or a future docs layer needs a distinct bounded source class.


## AOA-T-0080 / AOA-T-0081 / AOA-T-0082 / AOA-T-0083 Cross-Context Evidence Notes

2026-05-12 result: exact-fit downstream context found for Pack 34.
This is sibling-repo downstream evidence, not external import proof. Do not
import project-runtime diagnostic overlays, SDK closeout execution, role-law,
playbook scenario design, proof verdicts, memo writeback, stats refresh, or
runtime self-healing into the technique bundles.

Accepted evidence:

- `aoa-skills` at `eed21463dfde1bf0791e8ccbe6fdeaf68f8f0aec` keeps
  `abyss-self-diagnostic-spine` as a project overlay over
  `aoa-session-self-diagnose`: one concrete runtime target, grouped evidence
  axes, drift classes, confidence, freshness, unknowns, and one exit class are
  emitted before repair authority.
- `aoa-skills` evaluated `aoa-session-self-diagnose` and
  `aoa-session-self-repair` as stay-evaluated skill surfaces, preserving
  reviewed diagnosis before repair and prepared/executed/verified repair states
  as distinct outcomes.
- `aoa-sdk` at `931e7460ca4afb85dc20d400e8fad7d7d2c294e6` surfaces
  `aoa-session-self-repair` from reviewed closeout only when a diagnosis
  receipt exists and no repair-cycle receipt has landed.
- `aoa-skills` growth-cycle examples preserve repair packets and repair-cycle
  receipts with owner target, target artifact class, execution posture,
  approval, rollback, health check, iteration limit, stop conditions, and
  escalation route.
- `aoa-agents` at `ff5c397d59916c9a791a04e27328f5f2f3a8bc5f` owns the
  role-facing self-agent checkpoint stack, while `aoa-playbooks` at
  `78069a795690b343c5f228d1614c3e48adeaaead` owns scenario-level checkpoint
  rollout and owner-followthrough continuity.

Rejected or bounded:

- project-runtime diagnostic schemas and commands;
- SDK closeout execution, hooks, storage layout, and owner-handoff queues;
- skill workflow execution and status governance;
- role-law and self-agent profile authority;
- playbook scenario orchestration and real-run gate reviews;
- proof verdicts, memo writeback, stats refresh, runtime self-healing, and
  autonomous self-modification.

Future search shape: future sources can reinforce these canonical defaults
only if taxonomy, diagnosis, repair shape, and checkpoint posture stay as four
separate moves with reviewed evidence before mutation and visible stop lines
before owner, proof, role, playbook, runtime, or memory layers act.

## AOA-T-0076 / AOA-T-0078 / AOA-T-0079 / AOA-T-0090 Cross-Context Evidence Notes

2026-05-12 result: exact-fit downstream second context found for Pack 33.
This is sibling-repo downstream evidence, not external import evidence. Do not
import playbook scenario law, summon authorization, SDK execution behavior,
eval proof, routing/KAG, memo writeback, stats refresh, or owner-object
authorship into the technique bundles.

Accepted evidence:

- `aoa-playbooks` at `78069a795690b343c5f228d1614c3e48adeaaead` keeps owner
  repo, owner shape, nearest-wrong target, route-followthrough decision,
  stop/defer/drop/reanchor posture, and return anchors explicit in
  `owner-followthrough-campaign` and `session-growth-cycle`.
- `AOA-PB-Q-0013` and `AOA-PB-Q-0014` show concrete reanchor outcomes: seed-wave
  and recurrence archive closeout survivors stayed in owner-routed
  follow-through because the route shape was real but immediate promotion into
  skill, proof, memo, stats, runtime, or new playbook authority was not honest.
- `AOA-TECH-Q-0007` shows the same nearest-wrong-target posture in the
  technique layer: the AoA v0.4.0 closeout signal stayed in
  technique-promotion readiness rather than false skill ownership.
- `aoa-skills` at `eed21463dfde1bf0791e8ccbe6fdeaf68f8f0aec` marks
  `aoa-summon` evaluated, keeps branch choice outside summon when several
  routes compete, and requires passport fields before choosing one child lane.
- `aoa-sdk` at `f74c037e0f346713001516f7f3abddabbf64d02a` models
  `QuestPassport` and uses A2A summon assessment to split `d3+`, block
  `control_mode: blocked`, narrow high-risk or human-gated routes to reviewed
  lanes or human gate, and keep stress posture narrowing rather than widening.

Supporting proof lane:

- `aoa-evals` at `de87cbf94ae2178edc1babff02e29db021b23fc0` defines
  `aoa-owner-fit-routing-quality` around owner hypothesis, owner shape,
  rejected nearest-wrong target, and derivative-repo exclusion.
- This lane is supporting only: it can inspect owner-fit routing quality but it
  does not author owner truth, final object quality, or derivative first
  authorship.

Rejected or bounded:

- playbook scenario design;
- summon authorization;
- SDK execution and A2A transport;
- eval verdict authority;
- routing or KAG first authoring;
- memo writeback;
- stats refresh;
- final quest promotion verdicts;
- owner-object authorship.

## AOA-T-0075 / AOA-T-0077 Cross-Context Evidence Notes

2026-05-12 result: exact-fit live second context found.
`aoa-sdk` at `f74c037e0f346713001516f7f3abddabbf64d02a` provides the
clean primary source for Pack 32. This is sibling-repo evidence, not external
import evidence: do not import SDK hook plumbing, `.aoa` storage layout,
command wrappers, closeout execution code, or owner-handoff queue behavior into
`aoa-techniques`.

Accepted evidence:

- `docs/session-growth-checkpoints.md` says checkpoint capture does not emit
  `HARVEST_PACKET` or `CORE_SKILL_APPLICATION_RECEIPT`, and that full harvest
  belongs to the reviewed closeout path.
- The same doc says reviewed closeout builds `closeout-context.json`, rereads
  the reviewed artifact, then executes donor harvest, progression lift, and
  quest harvest in order while keeping the SDK bridge mechanical and requiring
  an agent to apply the skill protocol.
- `src/aoa_sdk/checkpoints/registry.py` blocks reviewed closeout when
  checkpoint agent reviews are still pending.
- `registry.py` aggregates runtime-session checkpoint notes, collects
  shortlisted clusters, harvest/progression/upgrade candidate ids, lineage
  hints, owner follow-through maps, and one ordered donor -> progression ->
  quest skill plan.
- `registry.py` builds accepted donor candidates from shortlisted clusters,
  preserves deferred candidates when no candidate survives, and writes
  `HARVEST_PACKET.json` with session ref, route ref, authority contract,
  reviewed artifact ref, checkpoint-review carry, accepted candidates,
  deferred candidates, extract counts, owner-layer distribution, and reviewed
  evidence density.
- `registry.py` writes `HARVEST_PACKET_RECEIPT.json` plus a core skill
  application receipt for the donor harvest stage.
- `tests/test_checkpoints.py` verifies that closeout chain artifacts carry
  checkpoint semantic review material into the harvest packet, preserve
  multi-commit review material, and emit donor/progression/quest artifacts and
  receipts even without a local checkpoint note.
- `tests/test_closeout.py` verifies that a closeout run can read accepted
  candidates from a harvest packet into owner follow-through briefs with
  source kind `harvest-candidate`, suggested action `draft-owner-artifact`,
  owner repo, next surface, and unit name.

Supporting public lane:

- LangSmith's annotation queue docs describe human review over specific runs,
  queue completion, reviewer notes, rubric feedback, and turning a reviewed
  run's edited input/output into a corrected reference example added to a
  dataset.
- LangSmith's dataset docs describe dataset versioning, filtered or split
  example views, and exporting filtered traces from experiments back to
  datasets.
- LangSmith's production logging automation guide describes `Add to Dataset`
  and `Add to Annotation Queue` actions where selected runs carry inputs,
  outputs, metadata, and feedback into bounded downstream datasets.
- This lane is supporting, not primary proof, because it does not carry
  AoA-style owner hints, nearest-wrong-target posture, or the `HARVEST_PACKET`
  spine.

Rejected or bounded:

- SDK checkpoint capture, post-commit hooks, pre-push/pre-merge gates,
  runtime-session ledgers, and local `.aoa` storage as invariant technique
  requirements.
- SDK closeout command names, report filenames, owner-handoff queue behavior,
  and exact JSON field names beyond the portable packet shape.
- LangSmith product workflows as a direct packet contract; they support
  reviewed-run curation pressure but stay evaluation/dataset-centered.
- Memory writeback, stats refresh, owner placement, progression scoring, quest
  promotion, final owner acceptance, and evaluation dataset governance as
  bundle-owned behavior.

Future search shape: future sources can reinforce these canonical defaults
only if reviewed run, trace, or session artifacts become bounded candidate
records or packet nuclei with evidence anchors before later owner placement,
evaluation, routing, memory, or promotion begins.

## AOA-T-0074 External Evidence Notes

2026-05-12 result: exact-fit second context found.
`3bl3gamer/tg_history_dumper` at
`0058ab229043fc4af6b1859e0c367b9fd9b10d93` provides the clean public source
for Pack 31. The repository is MIT licensed and is used as evidence only: do
not import Go code, Telegram client setup, session-file handling, preview
server behavior, config schema, account/contact/session dumps, or download
implementation into `aoa-techniques`.

Accepted evidence:

- `README.md` states that the tool exports messages as JSON plus media from
  specified dialogs, groups, and channels.
- `README.md` also states that it fetches only messages newer than already
  fetched ones and resumes interrupted file downloads.
- `README.md` documents local message storage as JSON Lines under chat-specific
  paths and related users/chats as JSON Lines peer surfaces.
- `saver.go` exposes a `HistorySaver` boundary with `GetLastMessageID`,
  `SaveRelatedUsers`, `SaveRelatedChats`, `SaveMessages`, `SaveStories`, and a
  file-request callback.
- `saver.go` reads the last saved message id from the append-only local JSONL
  file and uses that as the continuation boundary.
- `saver.go` appends messages with `_TL_LAYER`, resolves media requests before
  writing each message, and derives media paths from chat id, message id,
  filename, index-in-message, and media source.
- `saver.go` keeps related users and chats as append-only JSONL records where
  the latest record for each id wins.
- `tg.go` requests messages newer than the saved id by setting `OffsetID` to
  `lastMsgID + 1`.
- `main.go` loads `lastID`, updates it from fetched messages, saves related
  peers before messages, and only downloads a media file when the target path is
  absent, allowing interrupted downloads to continue.

Rejected or bounded:

- `GeiserX/Telegram-Archive` reinforces incremental local Telegram backup
  pressure, but it is product-heavy around web viewer behavior, auth setup,
  realtime sync, deletion/edit sync, media deduplication, and database
  deployment.
- `jackwener/tg-cli` reinforces local-first SQLite sync, search, and export,
  but it is weaker on media-reference preservation and also includes live
  send/listen operations.
- `groupultra/telegram-search` reinforces core message, reply, and media
  normalization, but widens into search, embeddings, web UI, and storage
  service behavior.
- HTML, CSV, and Markdown converters were rejected as too lossy for media,
  peer, reply, and resume-state preservation.
- marketing, member-scraper, forwarding, bot-control, and cloud-backup projects
  were rejected because their center of gravity is account action, outreach,
  forwarding, or Telegram-as-storage rather than local Telegram-source
  normalization.

Future search shape: future sources can reinforce this canonical default only
if they preserve Telegram-derived message objects, media references, peer or
source provenance, append-only or resumable local storage, and a stop-line
before auth bootstrap, session conversion, account/session dumps, search
products, archive presentation, deletion/edit sync, curation, routing, recall,
or memory writeback.

## AOA-T-0073 External Evidence Notes

2026-05-12 result: exact-fit second context found.
`end1989/ai-image-classification` at
`e3f3500bf274e802d669ed38403b7637b0897366` provides the clean public
source for Pack 30. The repository is MIT licensed and is used as evidence
only: do not import Python code, EasyOCR or PaddleOCR runtime packaging,
database schema, UI workflow, NSFW/moderation features, face detection,
auto-organization, move/delete behavior, or broader media-management
assumptions into `aoa-techniques`.

Accepted evidence:

- `README.md` exposes an offline media sorter with CLIP classification, OCR
  text extraction, review/correction flow, and configurable labels such as
  family, work, receipts, memes, and landscapes.
- `config/config.yaml` keeps the bucket taxonomy explicit, including people,
  events, nature, food, screenshots, receipts, documents, work, art, and
  other-style labels, with separate `auto_move` and `review` thresholds.
- `config/config_loader.py` validates that the auto-move threshold cannot be
  lower than the review threshold.
- `pipeline/classify.py` scores image embeddings against configured labels,
  stores label confidence, applies OCR text only as a bounded confidence boost
  for text-heavy labels such as receipt, chat, and work, filters predictions
  below the review threshold, and separates suggested route plus auto-move
  eligibility from the label itself.
- `pipeline/ocr.py` stores OCR text, average confidence, language, and text
  regions as a side result rather than as final classification truth.
- `backend/database.py` keeps classifications, OCR results, corrections, NSFW
  results, and action logs in separate tables.
- `pipeline/actions.py` keeps move, auto-move, and undo behavior in a separate
  action manager so file actions do not become part of the semantic bucket
  contract.

Rejected or bounded:

- `chintan-projects/photo-triage-agent` is adjacent pressure for local media
  triage, but it does not show the same OCR-side-channel confidence seam.
- `Aditya-Vasipalli/screensort` / Fragmenta is adjacent pressure for
  screenshot categories plus OCR, but widens into intent extraction, calendar
  events, structured data extraction, deletion, and Notion tasks.
- Receipt-only tools were rejected because they become schema extraction or
  bookkeeping workflows rather than mixed-media bucketing.
- Broad AI file organizers and cleanup SaaS products were rejected where the
  center of gravity was cloud storage, duplicate cleanup, auto-delete, or
  storage migration instead of one bounded classification seam.

Future search shape: future sources can reinforce this canonical default only
if they preserve the same narrow seam: bounded media set, explicit taxonomy,
visual semantic scoring, OCR as side-channel, confidence or review thresholds,
and a stop-line before duplicate grouping, OCR pipeline ownership, moderation,
identity inference, deletion, archiving, auto-routing, or full media-management
product behavior.

## AOA-T-0072 External Evidence Notes

2026-05-12 result: exact-fit second context found.
`qarmin/czkawka` at `612c93a6904e819d598f56c59c1f3be75ab42d25`
provides the clean public source for Pack 29. The relevant core and CLI
surfaces are MIT licensed, while the repository also contains mixed-license
GUI/application/assets surfaces. Use it as evidence only: do not import Rust
code, GUI workflow, icons, audio, cache layout, delete strategy names, hardlink
behavior, product cleanup posture, or broader media-management assumptions into
`aoa-techniques`.

Accepted evidence:

- `README.md` exposes Similar Images as finding images that are not exactly the
  same, including cases such as different resolution or watermarks.
- `czkawka_cli/src/commands.rs` exposes `max_difference` as a bounded
  `0-40` threshold with stricter/lower guidance and keeps perceptual hash
  algorithm plus hash size as explicit options.
- `czkawka_core/src/tools/similar_images/mod.rs` and `core.rs` carry
  thresholded perceptual hash comparison, per-entry `difference`, similarity
  presets/bands, and grouping through the similar-images result surface.
- `czkawka_core/src/tools/similar_images/traits.rs` prints grouped similar
  image results with dimensions, size, and similarity labels and can save the
  same grouped results as JSON.
- `czkawka_cli/src/main.rs` routes Similar Images results through the shared
  print/save path, while delete behavior remains a separate advanced-delete
  setting.
- deletion is explicitly default-off through `NONE - do not delete files
  (default)`.
- `czkawka_core/src/tools/similar_images/tests.rs` covers threshold-sensitive
  grouping counts across hash algorithms, filters, hash sizes, and similarity
  values.

Rejected or bounded:

- Do not treat Czkawka's GUI selection flow, cache format, hardlinking,
  duplicate-files cleanup, similar music/video tools, broken-files checks,
  product comparison tables, or application packaging as part of this
  technique.
- Do not import mixed-license GUI/assets surfaces; the canonical proof uses
  only public evidence from the relevant MIT-licensed core and CLI surfaces.
- Do not widen perceptual dedupe into semantic media taxonomy, archive policy,
  representative-selection doctrine, quality ranking, storage cleanup, or bulk
  delete automation.

Future search shape: future sources can reinforce this canonical default only
if they preserve the same narrow grouping seam: bounded media set, perceptual
similarity, explicit threshold or similarity bands, reviewable groups or
candidate pairs, and a stop-line before deletion, archiving, semantic
classification, ranking, or full media-management product behavior.

## AOA-T-0071 External Evidence Notes

2026-05-12 result: exact-fit second context found.
`kotaro-kinoshita/yomitoku` at
`51a51f4ce21d8a0b34998be1a9f03dfb50fa6925` provides the clean public source
for Pack 28. The repository is CC BY-NC-SA 4.0 licensed, so it is used as
evidence only: do not import code, schema text, model weights, sample images,
commercial-use posture, OCR engine setup, LLM server behavior, or product
workflow into `aoa-techniques`.

Accepted evidence:

- `README_EN.md` exposes `YomiToku Extractor` as structured data extraction
  from document images and PDFs through a YAML schema and JSON output.
- `docs/extractor.en.md` defines schema fields, value types, normalization,
  `cell_id`, `bbox`, `description`, `regex`, and merge behavior.
- rule-based extraction has an explicit method order and marks no-match scalar
  extraction with `source: not_found` and low confidence.
- JSON output preserves normalized value, raw text, confidence, source, cell
  ids, and bounding boxes; table output keeps row fields plus source metadata.
- `src/yomitoku/extractor/schema.py` and
  `src/yomitoku/extractor/rule_pipeline.py` implement the schema and rule
  extraction path directly, and `tests/test_extractor.py` covers `cell_id`,
  `bbox`, `regex`, fallback, `not_found`, and source-metadata behavior.

Rejected or bounded:

- Do not treat YomiToku's OCR engine, layout analyzer, Japanese-document focus,
  model setup, LLM extraction mode, vLLM server path, visualization output, or
  commercial edition as invariant requirements.
- `codebywiam/invoice-ocr` was inspected as adjacent MIT-licensed invoice OCR
  app evidence for regex field extraction and manual correction, but it is too
  application-shaped and weak on schema/evidence metadata to be primary proof.
- `nzregs/receipt-api` was inspected as adjacent MIT-licensed receipt API
  evidence for OCR-result line reconstruction and regex extraction of ABN,
  date, and total, but it is older and narrower than the needed schema-backed
  field-object contract.

Future search shape: future sources can reinforce this canonical default only
if they preserve the same narrow field-extraction seam: upstream OCR or layout
handoff, explicit field set, visible template or heuristic selection,
source-evidence or confidence, explicit missing or conflicting result posture,
and a stop-line before locale doctrine, bookkeeping automation, storage,
cleanup, LLM products, or full document-understanding stacks.

## AOA-T-0070 External Evidence Notes

2026-05-12 result: exact-fit second context found.
`JaidedAI/EasyOCR` at `363afb184047ce452e436f4224f3098422df872e`
provides the clean public source for Pack 27. The repository is Apache-2.0
licensed and repeats the staged OCR handoff outside the PaddleOCR/docTR donor
family without requiring `aoa-techniques` to absorb model serving, training,
benchmark, or document-understanding product doctrine.

Accepted evidence:

- `README.md` exposes standard OCR output as bounding box, recognized text,
  and confidence tuples.
- `easyocr/easyocr.py` keeps `detect()` and `recognize()` as separate methods;
  `readtext()` runs detection first, then passes horizontal and free-form
  region lists into recognition.
- dictionary and JSON output modes preserve boxes, text, and confidence as one
  structured result surface rather than forcing plain text as the invariant.
- `custom_model.md`, `trainer/craft/README.md`, and `releasenotes.md` keep
  recognition, CRAFT detection, and separate `detect` / `recognize` method
  concerns visible enough to support the stage boundary.

Rejected or bounded:

- Do not import EasyOCR installation, Docker, model-download, custom training,
  language-pack, demo, business-support, roadmap, or benchmark behavior.
- OCRmyPDF was inspected as adjacent searchable-PDF layering, not a structured
  OCR handoff proof.
- Tesseract.js was inspected as adjacent OCR engine packaging, not a clear
  detect/layout -> recognize -> handoff contract for this bundle.
- Surya was inspected as adjacent document-understanding breadth with layout
  analysis, reading order, table recognition, and GPL licensing, not the narrow
  public proof for this Apache-2.0 technique corpus.
- PaddleOCR and docTR remain donor-family evidence, so they do not count as
  the independent second context.

Future search shape: future sources can reinforce this canonical default only
if they preserve the same narrow handoff seam: visible source regions or layout
handles, recognized text, confidence or uncertainty, and a stop-line before
field extraction, semantic media bucketing, automation, searchable-PDF output,
model serving, benchmarking, or full document-understanding systems.

## AOA-T-0057 External Evidence Notes

2026-05-12 result: exact-fit second context found.
`anthropics/cwc-long-running-agents` at
`ffd563d668a97a38d4aa092bf0d5b1507c046629` provides the clean primary public
source for Pack 14. The source is Apache-2.0 licensed and frames
agent-maintained handoff as a long-running-agent primitive rather than a
transcript, mailbox, or memory product.

Accepted evidence:

- `README.md` names agent-maintained handoff as a core primitive because fresh
  sessions have no memory and context-window summaries lose detail.
- `claude-code-config/.claude/CLAUDE.md` requires each session to read
  `PROGRESS.md` before doing anything else, create it with `Done`,
  `In progress`, `Next`, and `Notes` sections if missing, and keep it current
  after completed items.
- `claude-code-config/README.md` describes the progress-file convention and
  points unattended follow-on sessions at `claude -p "continue from
  PROGRESS.md"`.
- `claude-code-config/.claude/hooks/commit-on-stop.sh` is a backstop that
  commits tracked work at session end so restart state stays durable, while
  leaving the handoff convention itself as the reusable object.
- `AlekseiUL/openclaw-memory-kit` at
  `b154ad075ee96e7c20edcebf2e9aa93a02493262` supports the compaction-specific
  boundary: `config/compaction.json` and `config/memory-flush.json` write
  `memory/handoff.md` before compression, `templates/handoff.md` fixes the
  handoff sections, and `templates/BOOTSTRAP.md` reads the handoff after
  wake-up or compaction before continuing.

Rejected or bounded:

- Do not import `cwc-long-running-agents` evaluator, proof gate, kill switch,
  steering hook, unattended loop, or full harness shape.
- Do not import `openclaw-memory-kit` vector search, daily diary, consolidation
  cron, session-history visibility, health checks, or memory product doctrine.
- Treat `openai/codex#21673`, `NousResearch/hermes-agent#20372`, and
  `NousResearch/hermes-agent#499` only as adjacent pressure because they are
  issue or design-discussion surfaces, not landed workflow proof.
- Keep receipt, git verification, transcript packaging, mailbox delivery,
  memory recall, and phase permission outside this bundle.

Future search shape: reopen only if a new source clarifies packet accuracy,
handoff consumption, or automated pre-compaction triggering without shifting
the bundle into memory systems, session databases, hook governance, transcript
history, mailbox receipt, or full lifecycle orchestration.

## AOA-T-0058 External Evidence Notes

2026-05-12 result: no exact-fit second context found. Pack 15 remains useful
because it separates the handoff-receipt object from several tempting adjacent
handoff and acknowledgment lanes before the long pass continues.

Searched and rejected as adjacent:

- `cmux` multi-agent protocol gist `409030b36c1889f8fc28c0448f05f95f`
  defines a single-line agent-to-agent envelope, a handoff payload with
  `task` and `context`, correlation IDs, and mandatory `ACK`/`RES` flow for
  requests. This is close, but its `ACK` is a transport/request acknowledgment
  meaning "received, working on it"; it does not prove reviewed acceptance of
  a specific handoff packet before continuation.
- `gastownhall/gastown` at
  `2eafac9784301e6a8832a8fa32df9143a17c236a` provides a strong adjacent
  session-cycling lane: `gt handoff`, generated handoff mail, fresh-session
  auto-prime, pending-mail visibility, and explicit escalation acknowledgment.
  This supports the broader handoff family, but the acknowledgment belongs to
  escalation handling and the handoff mail is read-before-continue rather than
  receipt-confirmed packet acceptance.
- GitHub code search was attempted for exact phrase combinations around
  `handoff packet`, `receipt`, `accepted`, `ACK`, and `continue`; no stronger
  exact-fit public candidate surfaced in this pass.

Future search shape: reopen only from a public workflow where a receiver records
`accepted`, `reviewed`, `received`, or equivalent against a stable handoff
packet reference and continuation is visibly blocked until that record exists.
Do not reopen from delivery ACKs, assignment records, request ACKs, escalation
ACKs, session auto-prime hooks, general mailbox platforms, or transfer-control
handoff APIs unless they also carry the receiver-side packet receipt gate.

## AOA-T-0059 External Evidence Notes

2026-05-12 result: no exact-fit second context found. Pack 16 remains useful
because it separates git-backed handoff-claim verification from broader claim
gates, outbound handoff capture, and session-start orientation surfaces.

Searched and rejected as adjacent or partial:

- `confab-framework` 1.8.0 on PyPI is MIT licensed and provides a strong
  public handoff-claim verification lane: `confab gate` scans handoff files,
  extracts claims, checks them against filesystem, environment, scripts,
  pipeline outputs, and count sources, and flags failures before the next agent
  sees them. This is clean supporting evidence for handoff claim hygiene, but
  it is broader than the bundle and not specifically a git-state verification
  seam for concrete handoff repo claims.
- `marcusglee11/LifeOS` at
  `46847c7c1f55b8c11f75137bbabffadf33f5cb29` has a `handoff-pack`
  skill with an inbound `from_codex` mode, `git rev-parse`, `git log`, and
  `git status` fact collection, plus `Claims Verified` and
  `Deltas from Claims` output sections. This is close, but the inspected repo
  has no explicit license metadata and the skill does not spell out a
  claim-by-claim git verdict gate before continuation.
- `antonwing77/session-handoff` at
  `e441e1205cb33c8bbb06a2742fb897385b8f73f8` has a pickup mode that reads the
  handoff, checks out and pulls the branch, runs `git log --oneline -5` and
  `git status`, notes discrepancies from the handoff, and adjusts the plan
  before work starts. This is a strong adjacent pickup discipline, but the
  inspected repo has no explicit license metadata and the output is not a
  distinct verified/mismatch/unverifiable handoff-claim record.
- `HyunKN/Mimir-Skills` at
  `037f40db0a570d3dfaa344e9922a8f56cb02c221` provides evidence-backed
  handoff summaries, branch-state patterns, and a git-context collector, but
  the source of truth is decision records and derived summaries rather than
  handoff claims checked against git state.
- SLOPE public docs and `srbryers/slope` describe compaction handoffs that
  carry git state, active claims, review phase, and sprint context, but the
  inspected public docs do not show a receiver-side claim-versus-git verdict
  gate for a specific handoff packet.
- `anthropics/cwc-long-running-agents` remains Pack 14 evidence: it uses
  `PROGRESS.md` plus git checkpoints as a second record, but it does not by
  itself close Pack 16's claim-verification output requirement.

Future search shape: reopen only from a public workflow where an inbound
handoff's concrete code, file, or commit claims are compared against visible
git evidence and the receiver records verified, mismatched, and unverifiable
claim outcomes before continuation. Do not reopen from generic claim hygiene,
outbound handoff generation, git-state capture, session-start orientation,
branch cleanliness checks, or full code-review/provenance systems unless they
also expose the narrow handoff-claim verdict seam.

## AOA-T-0060 External Evidence Notes

2026-05-12 result: exact-fit second context found.
`anthropics/cwc-long-running-agents` at
`ffd563d668a97a38d4aa092bf0d5b1507c046629` provides the clean public source
for Pack 17. The inspected `claude-code-config/.claude/CLAUDE.md` file carries
file-level Apache-2.0 SPDX metadata and states the opening ritual directly.

Accepted evidence:

- The `Always start here` section says to read `PROGRESS.md` before doing
  anything else, treating it as the handoff note from the previous session.
- If `PROGRESS.md` does not exist, the convention creates it with `Done`,
  `In progress`, `Next`, and `Notes` sections before work proceeds.
- The same startup section then runs `git log --oneline -10` to inspect recent
  committed work and runs a project smoke test, build, or test command once so
  the session starts from a visible baseline instead of a broken handoff.
- The root README explains why: fresh sessions have no memory, context-window
  summaries lose detail, `PROGRESS.md` is re-read first thing on every restart,
  and git commits provide a second record.

Rejected or bounded:

- Do not import the full `cwc-long-running-agents` harness, evaluator, default
  FAIL contract, proof gate, kill switch, steering hook, one-feature policy, or
  unattended-loop guidance.
- Treat smoke/build/test as one project-shaped baseline option, not universal
  startup test doctrine.
- Keep handoff packet creation in AOA-T-0057, concrete git-claim verification
  in AOA-T-0059, and broader task routing or harness lifecycle outside this
  bundle.

Future search shape: future sources can reinforce the canonical default only
if they preserve the same narrow order: read current context before mutation,
check one visible current-state baseline, record mismatch or proceed decision,
and keep task selection, detailed claim verification, and full boot doctrine
outside the opening seam.

## AOA-T-0061 External Evidence Notes

2026-05-12 result: exact-fit second context found.
`calltelemetry/openclaw-linear-plugin` at
`5b66f0e2fa17724f00858321a0c632df515182fc` provides the clean public source
for Pack 18. The repository metadata does not expose an SPDX license, but the
inspected `LICENSE` file is MIT.

Accepted evidence:

- The README documents multi-repo dispatch where a configured `repos` map names
  short repo keys and filesystem paths.
- The issue body marker `<!-- repos: api, frontend -->`, `repo:*` labels, team
  mappings, and config fallback select which repos belong to the current issue.
- Dispatch comments expose named worktree paths per selected repo so the next
  worker can see where each repo lives for that task.
- The pipeline builds a project context block containing the repo map and
  injects it into worker and audit prompts.
- Worker and audit prompts instruct agents to read `CLAUDE.md` and `AGENTS.md`
  in the worktree root before coding or auditing, keeping concrete first-look
  surfaces visible instead of leaving the agent to infer where to start.
- The `multi-repo.ts` and `codex-worktree.ts` implementation keeps repo
  resolution and per-repo worktree creation explicit and resumable.

Rejected or bounded:

- Do not import Linear issue routing, complexity-tier model selection,
  multi-agent orchestration, worker / auditor pipeline, rework loops, PR
  creation, watchdogs, or dispatch state.
- Do not turn this bundle into worktree lifecycle management, multi-repo
  authorization, or workspace-platform doctrine.
- Treat `Zencoder` multi-repo docs as supporting pressure only: they describe
  indexed repo maps and agents loading a repo map, but the inspected public
  page is broader product documentation rather than a small task-bounded
  repo-and-resource startup artifact.
- Treat GitHub Agentic Workflows `MultiRepoOps` and `SideRepoOps` as adjacent
  automation patterns: they show cross-repo target parameters, remote repo
  access, and checkout paths, but not a compact current-task startup map with
  repo roles and first-look resource surfaces.

Future search shape: future sources can reinforce the canonical default only
if they preserve the narrow artifact: selected repos, task-tied repo roles or
paths, first-look surfaces, and an explicit boundary away from architecture
inventories, topology stacks, dispatch policy, and full workspace-platform
governance.

## AOA-T-0062 External Evidence Notes

2026-05-12 result: exact-fit second context found.
`cloudflare/cloudflare-docs` at
`037df074e87cd773eb92836c81994db5e37ee5b9`, file
`src/content/docs/agents/concepts/long-running-agents.mdx` sha
`482c32aed0eb66f65ed1565996606a3dbdfbdd88`, provides the clean public source
for Pack 19. The repository is CC-BY-4.0 licensed.

Accepted evidence:

- The guide frames long-running agents as durable identities whose state,
  schedules, SQL data, and fiber checkpoints survive restarts and hibernation.
- `runFiber()` checkpoints intermediate state through `stash()` and recovers
  from the last checkpoint after eviction or restart.
- The planning strategy persists a `Plan` with ordered `steps`,
  `currentStep`, timestamps, and per-step statuses including `pending`,
  `in_progress`, `complete`, `failed`, and `skipped`.
- `executeNextStep` runs one step, marks it complete with a result, advances
  `currentStep`, and schedules the next step only after that bounded slice
  closes.
- On error, the current step is marked `failed` rather than silently advancing.
- The guide names recovery, visible progress, re-planning after failure or
  changed requirements, human oversight approval checkpoints, and context
  reconstruction as the advantages of the plan boundary.
- The summary keeps the loop narrow: plans break goals into steps, execution
  runs steps one at a time, recovery resumes from the last checkpoint, and the
  long-running agent eventually ends.

Rejected or bounded:

- Do not import Cloudflare Durable Objects, Workers, scheduling APIs, fibers,
  Workflows, sub-agent RPC, storage, hibernation, deployment, or lifecycle
  management into the technique.
- Treat `ax-llm/ax` as adjacent context-compression evidence: its checkpointed
  context policy, actor turns, clarification resume state, and status callbacks
  preserve runtime and prompt continuity, but they do not define a bounded
  work-episode loop with a checkpoint artifact and continue / stop / escalate
  decision before the next episode.
- Treat `Haserjian/assay` as adjacent proof-gate evidence: its episode-native
  runtime SDK seals checkpoints and gates settlement through verified evidence
  with escalate or alert outcomes, but the primary object is evidence
  settlement, not longer-work segmentation over repeated agent episodes.
- Exact-phrase GitHub code-search lanes around `episode`, `checkpoint`,
  `continue`, `stop`, and `escalate` produced no cleaner source before
  code-search rate limiting stopped the broader pass.

Future search shape: future sources can reinforce the canonical default only
if they preserve the same narrow object: one bounded long-running work slice,
one visible checkpoint or failure state, an explicit continue / stop /
escalate or re-plan decision, and a later slice that resumes from durable
state rather than hidden memory. Do not reopen from generic multi-step plans,
workflow engines, runtime checkpointing, context compression, settlement
gates, or autonomous-platform lifecycle docs unless they expose the bounded
episode-loop seam itself.

## AOA-T-0063 External Evidence Notes

2026-05-12 result: exact-fit second context found.
`nacos-group/nacos-group.github.io` at
`405bf9a9ff2b66ba7f6f593344ef3c48ed644d52`, file
`src/content/docs/next/en/manual/user/ai/agent-registry.md` sha
`b72e1ba5c1a1e6675a2adba44fcca180b7313767`, provides the clean public source
for Pack 20. The repository is Apache-2.0 licensed.

Accepted evidence:

- The guide frames Nacos as an A2A Registry for managing agents through agent
  registration, namespace isolation, and version management.
- AgentCards are treated as registry objects that align with the A2A
  AgentCard definition while adding Nacos-local registry management details.
- Agents are uniquely identified by `namespaceId` and `name`; names must be
  unique inside a namespace and may repeat across namespaces.
- AgentCards support multiple unique `version` values, require new versions
  when AgentCard content changes, and select one current default published
  version.
- Consumers get the default published version by default, and can request a
  specific version explicitly.
- SDK publication constructs an `AgentCard` with explicit `name`,
  `description`, `url`, `version`, and `protocolVersion`, then releases it to
  the Nacos registry.
- External-provider publication through console or HTTP API preserves the same
  AgentCard payload shape rather than hiding the entry in runtime state.

Rejected or bounded:

- Do not import Nacos service deployment, console workflow, SDK lifecycle,
  authentication, local endpoints, Spring AI Alibaba integration, or A2A
  invocation into the technique.
- Treat query/list/detail APIs, fuzzy search, skill/tag filtering, endpoint
  subscription, and consumer-side request flow as adjacent to
  `AOA-T-0064 capability-discovery`, not proof that the entry contract owns
  discovery behavior.
- Treat AgentCard field breadth, security schemes, signatures, capabilities,
  transport interfaces, and provider metadata as payload details rather than
  expanding this bundle into capability-spec ownership, trust policy, endpoint
  selection, marketplace curation, or graph semantics.

Future search shape: future sources can reinforce the canonical default only
if they preserve the same narrow object: one registry-facing entry with
explicit name or namespace/name identity, one visible version, one bounded
payload or stable reference, and reviewable metadata or default-version
semantics. Do not reopen from generic registry products, discovery search,
endpoint subscription, trust or signature layers, marketplace catalogs, or
capability schema documents unless they expose the versioned entry publication
contract itself.

## AOA-T-0066 External Evidence Notes

2026-05-12 result: exact-fit second context found.
`dataprofessor/cortex-replay` at
`d61d46a7acbe55b3367f695a04e56eca24871320` provides the clean primary public
source for Pack 23. The inspected repository carries an MIT license and frames
the reusable object as converting already-saved AI coding session transcripts
into one self-contained interactive replay artifact. Snowflake's public Cortex
Code replay guide supports the same workflow as a separate public assistant
surface and guide layer.

Accepted evidence:

- The README presents the object as converting saved JSON session transcripts
  into self-contained interactive HTML replays with no external runtime
  dependency for viewing.
- The CLI can list saved sessions, select a latest or explicit saved session,
  accept a direct transcript file, filter by turns or time windows, and write
  one replay output.
- The renderer preserves replayable flow with turn order, metadata, player
  controls, speed, bookmarks, and visibility toggles while keeping the saved
  transcript as the source artifact.
- The parser and renderer keep filtering and secret redaction as replay-output
  safety controls instead of publishing raw private session material.
- Snowflake's guide independently describes saved-session transcript replay as
  a shareable/local review artifact rather than a hosted replay platform.

Rejected or bounded:

- Do not import Cortex-specific storage locations, account setup, install
  commands, product names as requirements, or live session capture behavior.
- Do not import theme systems, keyboard shortcuts, hosted demo behavior,
  iframe/embed behavior, dashboards, collaboration, analytics, or viewer
  platform doctrine as technique invariants.
- Do not treat a replay artifact as source truth or proof of state changes;
  saved transcripts, capture artifacts, and witness traces keep those sibling
  roles.
- Treat `ai-replay` as same-lineage supporting pressure only unless a later
  pass needs a separate Python-package lane; it was not needed for the primary
  canonical proof.

Future search shape: future sources can reinforce the canonical default only
if they preserve the same narrow object: already-saved session artifacts,
one derivative replay transformation, reviewable flow cues, visible filtering
or redaction limits, and explicit source-artifact authority. Do not reopen from
generic transcript packaging, session search/indexing, witness forensics,
hosted sharing products, dashboards, replay editors, memory systems, or
publishing platforms unless they expose the bounded replay-artifact seam itself.

## AOA-T-0067 External Evidence Notes

2026-05-12 result: exact-fit second context found.
`ai4curation/ai-blame` at
`3892e208e6010ca4e9a936fe7d8143b0418c2fe2` provides the clean primary public
source for Pack 24. The repository is BSD-3-Clause licensed and frames the
object as extracting provenance from AI agent execution traces with
git-blame-style line attribution plus transcript exploration. `empathic/toolpath`
at `5ac423abbfe815699873d23031662c11b6747401` provides supporting
Apache-2.0 provenance-document shape evidence, but not the primary proof.

Accepted evidence:

- `ai-blame` documents line-by-line blame for AI-assisted edits: a target file,
  optional line range, line numbers, line content, model attribution, and block
  grouping.
- Its source model carries blame metadata with timestamp, model, session id,
  agent tool, and optional agent version, so code anchors remain linked back
  to saved trace evidence rather than becoming only display labels.
- The documented review workflow focuses on a line or block, then opens the
  related transcript for context through transcript list and transcript view.
- Transcript docs define transcripts as saved session records with messages,
  metadata, tool and file-operation content blocks, and the source trace file.
- Trace-format docs show Claude and Codex-style traces carrying file path,
  timestamp, model, session id, event/action, content or diff data, and source
  trace records for later inspection.
- `toolpath-claude` supports the same broad provenance family by deriving path
  documents from conversation logs and mapping write/edit tool use to change
  entries keyed by file path.

Rejected or bounded:

- Do not import desktop UI, cache implementation, annotation sidecar policy,
  trace-directory conventions, local path examples, install commands, or agent
  trace format specifics as technique requirements.
- Do not import `ai-blame` stats, timeline, report, or annotate commands as
  invariant behavior; they are adjacent tooling around the narrower lineage
  seam.
- Do not import Toolpath share/resume, graph format governance, provider
  framework, live watching, or pathbase behavior as part of this bundle.
- Treat Grain and Mobb Tracy as adjacent pressure: both describe code-to-
  conversation transparency, but the searched surfaces widen into policy,
  score, product, or hosted integration behavior rather than serving as the
  primary clean proof for this public technique.

Future search shape: future sources can reinforce the canonical default only
if they preserve the same narrow object: code, file, line, diff, or commit
anchors reopening already-saved session or trace evidence through a bounded
review path. Do not reopen from generic AI-percentage scoring, policy gates,
review enforcement, dashboards, hosted search, transcript indexing, memory
systems, or repository analytics unless they expose the direct code-to-evidence
lineage seam itself.

## AOA-T-0068 External Evidence Notes

2026-05-12 result: exact-fit second context found.
`mvar-security/clawzero` at
`17ac1e7ee69eaf32cb616f67ef37d0e9db5d7fe7` provides the clean primary public
source for Pack 25. The repository is Apache-2.0 licensed and frames the
object as a deterministic execution boundary between model output and tool
execution, with sink-policy decisions and witness artifacts. OpenAI Agents
SDK guardrails at `openai/openai-agents-python`
`564584513f74e74f7916bd865ea77003d47b739c` provide supporting boundary
semantics for blocking and tool guardrails, but not the primary proof.

Accepted evidence:

- ClawZero documents a boundary between model output and tool execution, and
  states that enforcement happens before commands, credential access,
  filesystem access, network requests, or other high-privilege tool calls run.
- Its verified-claims surface records command-backed proof that shell
  injection, unsigned package install, temporal taint, budget-limit, and
  witness-chain paths produce reproducible block or verification outcomes.
- Its tests show `protect_*` wrappers raising blocked execution before wrapped
  LangChain, OpenClaw, and MCP calls proceed when the sink verdict is `block`.
- Its witness tests and README keep the review evidence visible through one
  witness artifact with timestamp, runtime, sink type, target, decision,
  reason code, policy id, provenance, adapter, engine, and signature fields.
- OpenAI Agents SDK supports the smaller tool-guardrail shape: blocking input
  guardrails can run before an agent starts, tool input guardrails run before
  custom function-tool execution, guardrail output can carry check details,
  and tripwires or reject behavior halt or skip execution at the covered seam.

Rejected or bounded:

- Do not import ClawZero's attack demonstrations, named policy profiles,
  adapter APIs, install commands, CLI families, temporal-taint engine, package
  trust controls, SARIF export, compliance mapping, budget controls, or MVAR
  governance as requirements for this technique.
- Do not import signed-witness chains or cryptographic verification as the
  default evidence requirement; this bundle only needs one reviewable evidence
  artifact or equivalent surface.
- Do not import OpenAI Agents SDK as a universal guarantee: parallel input
  guardrails may run too late for side-effect prevention, tool guardrails cover
  custom function tools rather than every hosted, built-in, handoff, or
  platform tool path.
- Treat HiddenLayer, TrueFoundry, AgentLock, MandateOS, and similar gateway or
  authorization surfaces as adjacent pressure unless a future pass needs a
  separate product-gateway or signed-authorization sibling; they are too broad
  for this narrow canonical proof.

Future search shape: future sources can reinforce the canonical default only
if they preserve the same narrow object: one explicit verdict boundary before
mutating execution, non-allow outcomes block side effects, and a reviewable
evidence surface records the verdict basis. Do not reopen from broad policy
authoring, human approval, signed-witness infrastructure, compliance export,
attack-pack validation, gateway products, sandboxing, or durable job
orchestration unless they expose the bounded fail-closed evidence gate itself.

## AOA-T-0069 External Evidence Notes

2026-05-12 result: exact-fit second context found.
`pydantic/pydantic-ai` at
`ac684b2638ee1095077ece25b7fed5abe6d14a25` provides the clean primary public
source for Pack 26. The repository is MIT licensed and frames the object as
deferred tool approval or external execution in an agent run, with durable
execution adapters for long-running and human-in-the-loop workflows. LangGraph
at `4a86705bd7f951c6c2cf3dd863f3f12521d9e221` provides supporting
checkpoint/thread/resume boundary evidence, but not the primary proof.

Accepted evidence:

- Pydantic AI `docs/deferred-tools.md` describes tool calls that cannot run in
  the same agent process because they need user approval, an external service,
  or longer background work.
- The stop-the-world flow ends the current run with `DeferredToolRequests`;
  the caller gathers approvals, denials, or external results and starts a new
  run with the original message history plus `DeferredToolResults`.
- Approval requests carry tool name, validated arguments, unique tool call ID,
  and optional metadata; results map back by tool call ID and can approve,
  deny, override arguments, or return external call results.
- External calls can carry a separate task ID in metadata so a background
  worker or later process can match completed work back to the deferred tool
  call before resuming.
- Pydantic AI `docs/durable_execution/overview.md` says durable agents preserve
  progress across transient failures, application errors or restarts, and
  long-running, asynchronous, human-in-the-loop workflows through public
  durable-system integrations.
- LangGraph's official durable execution and interrupt docs support the
  boundary shape: checkpointed state, `thread_id` as persistent cursor,
  indefinite waits for external input, and `Command(resume=...)` continuation.

Rejected or bounded:

- Do not import Pydantic AI model names, decorator APIs, toolset classes,
  capability hooks, test cassette contents, adapter packages, install commands,
  or public-interface wording as technique requirements.
- Do not import Temporal, DBOS, Prefect, Restate, LangGraph, or any other
  durable backend as the invariant implementation. Durable state, saved
  message history, a persisted checkpoint, or equivalent pending-call identity
  is enough.
- Do not treat generic human approval as sufficient proof; this bundle needs
  longer-running continuity across an approval or external-result seam.
- Treat Prefect examples, Temporal samples, HumanLayer approval/session
  surfaces, and broad workflow products as adjacent pressure unless a future
  pass needs a separate scheduler, queue, or agent-session product sibling.

Future search shape: future sources can reinforce the canonical default only
if they preserve the same narrow object: one durable or serialized pending
unit, one explicit approval or external-result seam, and continuation from
durable state, saved history, checkpoint, or equivalent identity. Do not reopen
from one-shot confirmation prompts, fail-closed verdict gates, generic queues,
scheduler platforms, retry doctrine, worker-fleet governance, dashboards, or
total durable-execution product behavior unless they expose the bounded
approval-bound durable-job seam itself.

## AOA-T-0065 External Evidence Notes

2026-05-12 result: exact-fit second context found.
`smart-mcp-proxy/mcpproxy-go` at
`f4ad4e7c36ec8af24325f41453e9c88db8a9afde` provides the clean primary public
source for Pack 22. The repository is MIT licensed. Supporting shape evidence
was also checked in `TBXark/mcp-proxy` at
`4f78891f47eb18578039ec8d45f827e998631f12`, also MIT licensed.

Accepted evidence:

- MCPProxy exposes one default MCP client endpoint and documents routing-mode
  endpoints under the same proxy surface.
- Its upstream-server docs configure multiple `mcpServers` and state that
  MCPProxy connects to multiple MCP servers simultaneously while providing
  unified access through a single endpoint.
- The search/discovery docs show the proxy retrieving tool metadata from
  connected upstream servers, indexing tool names, descriptions, and
  parameters, and returning server-scoped tool results.
- The MCP protocol docs keep tool execution mediated through built-in
  `call_tool_read`, `call_tool_write`, and `call_tool_destructive` variants
  using `server:tool` names and explicit intent fields.
- Sensitive-data detection docs show a proxy-boundary inspection lane over tool
  call arguments and responses, with redacted activity-log evidence rather
  than source code or secret exposure.
- `TBXark/mcp-proxy` supports the simpler shape of multiple configured MCP
  servers behind one HTTP proxy surface, including `stdio`, `sse`, and
  `streamable-http` upstream types and tool filters.

Rejected or bounded:

- Do not import MCPProxy's tray app, web UI, installer behavior, package
  repositories, dashboards, telemetry product, or broader product lifecycle.
- Do not import Docker isolation, process lifecycle, upstream restart logic,
  health diagnostics, OAuth, token management, or user-facing management
  commands as gateway-proxy requirements.
- Do not import BM25 ranking, retrieve-tools selection policy, tool search
  quality, tool recommendation, or context-window optimization as part of this
  technique. They are adjacent selector/discovery concerns.
- Do not import quarantine governance, scanner plugins, RBAC, audit-dashboard
  policy, or enterprise security-platform doctrine. Only the narrow
  proxy-boundary inspection/sanitization idea is relevant here.
- Treat `TBXark/mcp-proxy` as supporting shape evidence, not as full proof of
  the sanitization boundary, because its public docs center aggregation and
  routes more than argument/result inspection.

Future search shape: future sources can reinforce the canonical default only
if they preserve one explicit caller-facing proxy seam over configured upstream
tool surfaces, visible metadata or capability inspection, mediated tool calls,
and any argument/result filtering at the proxy boundary without making
lifecycle, registry, ranking, quarantine, UI, or enterprise platform behavior
part of the invariant.

## AOA-T-0064 External Evidence Notes

2026-05-12 result: exact-fit second context found.
`nacos-group/nacos-group.github.io` at
`405bf9a9ff2b66ba7f6f593344ef3c48ed644d52`, file
`src/content/docs/next/en/manual/user/ai/agent-registry.md` sha
`b72e1ba5c1a1e6675a2adba44fcca180b7313767`, provides the clean public source
for Pack 21. The repository is Apache-2.0 licensed.

Accepted evidence:

- The guide has a distinct `Query Agent` section after publication, so
  discovery is not collapsed into the entry-publication contract.
- The SDK query path retrieves the default published `AgentCard` by
  `agentName`, showing lookup over already-published registry entries.
- The HTTP detail example uses explicit `namespaceId` and `agentName`
  parameters to retrieve one AgentCard.
- The list/search example uses explicit `pageNo`, `pageSize`, `agentName`,
  `namespaceId`, and `search=blur` parameters to search AgentCards by name.
- The console search text preserves the same visible user-facing lookup
  concept: search by Agent name and open detail view.
- The roadmap keeps skill/tag/description filtering as a future search
  dimension, which is useful evidence that those fields should not be imported
  as current canonical requirements.

Rejected or bounded:

- Do not import Nacos service deployment, console workflow, SDK lifecycle,
  authentication, local endpoints, Spring AI Alibaba integration, or A2A
  invocation into the technique.
- Treat `subscribeAgentCard`, endpoint updates, endpoint selection, and
  automatic client invocation as adjacent runtime/subscription behavior rather
  than the bounded lookup contract.
- Treat the `AOA-T-0063` publication evidence as a prerequisite context only:
  this bundle owns lookup over published entries, not entry creation, version
  publication, default-version mutation, or AgentCard payload schema.
- Treat future skill/tag/description filtering, official registry protocol
  work, ranking, trust policy, marketplace curation, and graph semantics as
  future or sibling concerns until a source makes them current, bounded, and
  reviewable as discovery rather than product governance.

Future search shape: future sources can reinforce the canonical default only
if they preserve the same narrow object: lookup over already-published entries,
explicit query fields or parameters, bounded exact/wildcard/fuzzy behavior,
pagination or limit semantics where present, and an explicit result shape
that remains smaller than ranking, trust, endpoint selection, runtime
invocation, marketplace curation, or registry governance.

## AOA-T-0056 External Evidence Notes

2026-05-12 result: exact-fit second context found.
`heurema/mycel` at `4ffa460f3f5efe36f31ef064f26c514ac703ae7b`
provides the clean primary public source for Pack 13. The source is MIT
licensed and explicitly frames itself as an encrypted async mailbox for AI CLI
agents rather than a generic messaging platform.

Accepted evidence:

- `README.md` names the mailbox use case for Claude Code, Codex CLI, and
  Gemini CLI, shows `mycel inbox --json`, and exposes stable `msg_id`,
  `thread_id`, `reply_to`, `read_status`, and `delivery_status` fields.
- `docs/architecture.md` keeps the product boundary as "mailbox, not
  messenger", sync-on-command, local-first, and transport-neutral mailbox
  state.
- `src/cli/thread.rs` creates bounded thread IDs, sends thread messages, and
  logs thread messages ordered by creation time with logical message IDs.
- `src/sync.rs` maintains sync cursors and fetches missing events through
  Negentropy or overlap-window fetch before ingesting them into normalized
  mailbox state.
- `src/store/mod.rs` stores messages, threads, outbox retry state, sync state,
  and explicit ACK rows keyed by logical `msg_id` plus sender.
- `src/cli/inbox.rs` records local ACK rows after message receipt when ACK
  tracking is enabled, while clearly noting that reverse remote ACK sending is
  not complete in the inspected release.
- `tests/integration.rs` and `tests/outbox_test.rs` cover thread IDs, ordered
  thread queries, `msg_id` dedup/retry behavior, ACK rows, and outbox retry
  state.

Rejected or bounded:

- Do not treat local ACK rows as remote delivery confirmation.
- Do not import `mycel` encryption, trust tiers, relay routing, Nostr details,
  A2A/MCP adapter planning, local-gateway plans, or product packaging.
- `Dicklesworthstone/mcp_agent_mail` at
  `0fd616a00161da7802594fa4e1e9aa0a8f5fa1ef` was inspected as a close
  adjacent surface because it has agent identities, inbox/outbox, searchable
  threads, and `acknowledge_message`, but its license rider makes it unsuitable
  as the primary clean canonical evidence source for this public bundle.

Future search shape: reopen only if a new source clarifies remote ACK proof or
cross-agent thread/mailbox semantics without shifting the technique into
handoff authorization, broker governance, or messaging-platform doctrine.

## Active Lead Ledger

These are the current live external-evidence lanes worth searching next.

| technique | last checked lane | adjacent or insufficient fits already ruled out | exact proof still needed | next honest search shape |
|---|---|---|---|---|
| [AOA-T-0032](../../../../techniques/proof/evaluation-chain/context-report-for-ci/TECHNIQUE.md) | repo-local drift and evaluation-report lane plus public agent-markdown CI check/report lane, public prompt-eval CI lane, the 2026-05-12 exemplar sweep over public context-report, token-budget, repo-packing, LLM-ready-docs, and CI reporting surfaces, and the Stage 1 long-pass sweep over public context-compiler, context-drift, fragment-assembly, dependency-graph, and repo-quality report surfaces | local drift reports and composition audits; public instruction-check and workflow-report surfaces such as Continue `/check` and GitHub Agentic Workflows daily repo reports that emit PR checks or activity summaries; Promptfoo CI/CD and `promptfoo-action` surfaces that emit eval JSON or HTML, PR comments, and before/after prompt reports; GitHub Agentic Workflows token/audit reports, Repomix repo-packing and token-count surfaces, Repo Tokens badge-style token counts, `pytest-llm-report`, Calcis prompt cost estimates, `llms-txt-action`, LogicStamp Context, Claude Code Guide context-engineering CI drift detection, ctxloom, Depwire, and FastPace, all of which are adjacent because they own workflow audit, context assembly or compilation, configuration drift, fragment/profile injection, graph context, token/cost monitoring, test or prompt reports, repo-quality/governance reports, or documentation conversion instead of the same CI-facing composition coverage or token-drift artifact | one second public CI-facing report over context composition coverage or token-drift that stays separate from composition mechanics, remediation policy, prompt-quality scoring, generic PR policy checks, context compilers, fragment assemblers, and repo-quality dashboards | search artifact-first public CI or docs-validation repos where an expected source or fragment inventory is compared against an assembled prompt/context artifact and token deltas are emitted as a read-only report, not just as eval matrices, pass or fail gates, token badges, repo-packing outputs, LLM-ready-doc generation, product dashboards, graph compilers, or activity digests |
| [AOA-T-0042](../../../../techniques/instruction/skill-discovery/upstream-skill-health-checking/TECHNIQUE.md) | 2026-05-12 Pack 5 skill-ecosystem lane | `shskills` manifest plus `doctor`, fast-agent skill registry install/update, and Aescut skill/MCP registry checks are useful adjacent surfaces, but they widen into install state, update management, security or permission review, managed registry behavior, or broader trust checks rather than the same minimal pre-surface source availability plus manifest-readiness verdict | one second downstream consumer that checks one upstream skill source for reachability plus minimal `SKILL.md` or manifest parseability before catalog or selector surfacing | search public catalog-publish or source-intake workflows that block or flag broken upstream skill entries before discovery, without install/update management, security scoring, registry governance, or generic monitoring |

## AOA-T-0032 Exemplar Sprint Notes

2026-05-12 result: no exact-fit second consumer found in the exemplar sweep.
The pass is still useful because it narrows a tempting false-positive band
before the long promotion-evidence pass.

Searched and rejected as adjacent:

- GitHub Agentic Workflows token-budget and audit reports: useful workflow
  audit and token telemetry, but not a context-composition coverage report.
- Repomix: useful repo packing, file summaries, and token-count tree support,
  but the object is context assembly or packing rather than a separate
  read-only CI report over an already-composed context.
- Repo Tokens: useful badge-style repository token count and context-window
  percentage, but no source-coverage or composed-context drift report.
- `pytest-llm-report`: useful test coverage plus LLM annotation/token reports,
  but the object is test reporting and annotation telemetry rather than
  context-composition coverage.
- Calcis: useful prompt-file cost and token estimation, but no source coverage
  and no composed-context report artifact.
- `llms-txt-action`: useful documentation conversion for LLM consumption, but
  it generates LLM-ready docs rather than reporting on composition health.
- OpenAI Codex issue `#2765`: useful public context-window pressure signal,
  but an issue discussion is not a CI-facing report artifact over composed
  context coverage or token drift.

GitHub code search was also attempted for exact phrases around context
composition, source coverage, token drift, and CI report artifacts. It found no
exact-match candidates before rate limiting stopped broader code-search
expansion. Do not treat that rate limit as proof that no public candidate
exists; treat it only as searched-lane memory for this pass.

2026-05-12 Stage 1 long-pass result: no exact-fit second consumer found.
The pass sharpened the false-positive boundary before the matrix-wide
promotion-evidence pass moves beyond the old lead queue.

Searched and rejected as adjacent:

- [LogicStamp Context](https://github.com/LogicStamp/logicstamp-context):
  strong public context compiler and CI-friendly stats / compare surface with
  token estimates, generated `context.json` bundles, and context drift
  validation, but the object is context compilation and validation rather than
  a separate read-only report over an already-composed context's expected
  source coverage plus token drift.
- [Claude Code Guide context-engineering CI drift detection](https://cc.bruniaux.com/guide/context-engineering/):
  useful profile and configuration drift discipline, but the object is
  regenerated instruction configuration freshness rather than a
  context-composition coverage artifact.
- [ctxloom](https://ctxloom.dev/): useful fragment/profile assembly, remote
  sync, and token optimization surface, but it owns assembly and injection
  rather than an independent CI report observing a composed artifact.
- [Depwire](https://depwire.dev/): useful graph context, impact analysis,
  generated docs, and CI-ready JSON for code health signals, but not a
  composed-context source-coverage and token-drift report.
- [FastPace](https://fastpace.net/): useful read-only
  repo-quality/context-score and governance reporting, but the object is
  repository quality, audit, and guardrail posture rather than CI-facing
  composition coverage.

Next honest search shape: look for artifact-first public docs-validation or
prompt-build workflows that commit or publish a CI report comparing expected
source or fragment inventories against generated prompt/context artifacts plus
token deltas.

Previous next-shape wording: look for public docs-validation or prompt-build
workflows that emit an artifact comparing expected prompt/context fragments
against the assembled artifact plus token drift, while leaving assembly,
scoring, and remediation to other surfaces.

2026-05-12 Pack 5 precheck result: no exact-fit second consumer found.
Searches around `context report`, `token drift`, `source coverage`, fragment
inventory, and CI report artifacts found no public candidate that changed the
current next-shape boundary. This was a narrow freshness check before moving to
the skill-ecosystem pack, not proof that no candidate exists.

## AOA-T-0005 Stage 2 Long-Pass Notes

2026-05-12 result: no exact-fit second consumer found.
The pass moved `AOA-T-0005` out of "not yet actively searched" posture and
recorded the first durable adjacent-lane boundary for the long-gap donor row.

Searched and rejected as adjacent:

- GitHub code search for `expected_intent_type`, `new intent`, `intent_type`
  plus dry-run / contract / fixture phrases found public intent-classification
  and intent-benchmark surfaces, but no non-origin rollout record with the
  full checklist shape.
- [PRISM Monitor `InstructionRF/data/README.md`](https://github.com/PRISM-System/PRISM-Monitor/blob/f8680e27bb7e4b3494d9c3a17d3f704a41842b17/InstructionRF/data/README.md):
  useful manufacturing intent-classification dataset with expected intent and
  priority labels, but it is an evaluation dataset rather than a one-new-intent
  extension through an existing dry-run chain.
- [ARTE Chatbot `evaluation/intent_eval/run_eval.py`](https://github.com/creep1ng/arte-chatbot/blob/c0f20b994bba4ee8d63acaa86f5c8044d8e220b1/evaluation/intent_eval/run_eval.py):
  useful `intent_type` classification harness with saved results and accuracy
  thresholds, but the object is classifier evaluation against annotated
  queries, not a rollout checklist with fixture, smoke, contract summary,
  published review row, and regression coverage for one new intent path.
- [CS4730 IBN `experiments/run_benchmarks.py`](https://github.com/siddu1324/cs4730-IBN/blob/191704ab4ce680e7b700867ce9e8ac99c6286f75/experiments/run_benchmarks.py):
  useful intent-based networking benchmark that compares translators,
  guardrails, policy rendering, and simulation outcomes against expected
  intent types, but it is a benchmark/evaluation lane rather than a bounded
  rollout record for adding one new intent to a shared chain.
- [Rasa testing docs](https://legacy-docs-oss.rasa.com/docs/rasa/next/testing-your-assistant/):
  useful assistant validation, test-story, NLU evaluation, and CI guidance, but
  it validates conversation and NLU behavior after authoring rather than
  recording a dry-run chain extension checklist.
- [Botpress ADK eval docs](https://botpress.com/docs/adk/testing/evals):
  useful conversation eval, tool assertion, workflow assertion, and regression
  tagging shape, but it is an eval runner surface rather than a new-intent
  rollout artifact.

Next honest search shape: look for a public repository where an existing
intent-to-plan or intent-to-action chain records the addition of exactly one
new intent with a canonical fixture, dedicated smoke run, strict expected
intent routing check, machine-readable summary, visible review artifact, and
regression proof. Do not reopen generic chatbot NLU, intent-classification, or
IBN benchmark lanes without a new rollout-specific signal.

## AOA-T-0022 Stage 2 Long-Pass Notes

2026-05-12 result: no exact-fit second corpus found.
The pass moved `AOA-T-0022` beyond the seeded `aoa-skills` donor and recorded
which tempting public risk lanes are adjacent rather than closure evidence.

Searched and rejected as adjacent:

- GitHub code search for the exact heading family `Failure modes`, `Negative
  effects`, `Misuse patterns`, `Detection signals`, and `Mitigations` found no
  public non-AoA repository candidates.
- Workspace search across sibling owner repositories found only the already
  recorded `aoa-skills/skills/risk/aoa-sanitized-share/SKILL.md` exact donor;
  `aoa-evals` uses `Failure modes` plus `Blind spots`, and `aoa-agents` service
  certification uses a narrower `Failure modes` section, so both remain
  adjacent contrast rather than the same five-part caution split.
- [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/):
  useful open security-risk taxonomy with mitigations around LLM application
  vulnerabilities, but it is a vulnerability/governance framework rather than
  a markdown-first caution section attached to reusable method bundles.
- [Microsoft taxonomy of failure modes in AI agents](https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/):
  useful failure-mode taxonomy with harm categories, effects, mitigations, and
  detection/response opportunities, but it is a broad threat-modeling and
  defensive strategy surface rather than the exact five authored caution
  headings.
- [Microsoft autonomous agentic AI risk guidance](https://learn.microsoft.com/en-us/security/zero-trust/sfi/manage-agentic-risk):
  useful agentic-risk design, security, governance, monitoring, and misuse
  guidance, but it organizes risks by design/security pillars rather than by
  the five markdown caution distinctions.
- [NIST AI RMF 1.0](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10):
  useful cross-sector AI risk-management framework, but it is intentionally
  use-case agnostic and governance-oriented rather than a committed reusable
  corpus with the exact five-part `Risks` contract.

Next honest search shape: look for a committed public or sibling corpus where
authored reusable method, skill, playbook, or evaluation bundles use the exact
five headings together as their risk section. Do not count broad AI safety,
security taxonomy, governance framework, or `Failure modes` plus `Blind spots`
surfaces unless they actually adopt the same five-part markdown contract.

## AOA-T-0035 Stage 2 Long-Pass Notes

2026-05-12 result: no exact-fit second consumer found.
The pass moved `AOA-T-0035` out of pending Pack 3 posture and recorded the
first durable adjacent-lane boundary for profile, preset, module, and
composition lookalikes.

Searched and rejected as adjacent:

- GitHub code search for exact combinations around `preset`, `profile`,
  `module`, `resolved`, `dedupe`, `first appearance`, `--list-profiles`, and
  `--list-presets` found no public non-origin candidate carrying the full
  three-layer composition contract.
- [Docker Compose profiles](https://docs.docker.com/compose/how-tos/profiles/):
  useful service-profile activation and environment selection, but the object
  is service gating inside a Compose application rather than a separate
  module -> profile -> preset contract with preset-first profile expansion and
  read-only inspection as the technique center.
- [SoS report plugin profiles and policy presets](https://sos.readthedocs.io/en/main/plugins.html)
  plus [`sos report` preset/profile options](https://manpages.ubuntu.com/manpages/bionic/man1/sosreport.1.html):
  useful adjacent vocabulary where plugins belong to profiles and presets
  store option sets, but the preset layer is an option/default set rather than
  an ordered profile bundle that expands to deduped modules before launch.
- [VS Code Profiles](https://code.visualstudio.com/docs/configure/profiles):
  useful named editor configuration sets that can be switched, exported, and
  imported, but they are complete profile states rather than an explicit
  module -> profile -> preset layering contract.
- [Dev Container Features](https://containers.dev/features) and
  [Templates](https://containers.dev/templates): useful reusable environment
  building blocks and starter packages, but the public object is feature or
  template selection rather than ordered preset expansion over profiles.
- [Kustomize bases and overlays](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/):
  useful declarative composition, resource assembly, and overlay reuse, but it
  is Kubernetes configuration customization rather than profile/preset runtime
  posture composition with the same dedupe and inspection rule.

Next honest search shape: look for a public runtime or tool repository where
small modules are grouped into ordered profiles, named presets are ordered
profile bundles, preset-expanded profiles resolve before direct profiles,
duplicate profiles and modules are kept once at first appearance, and a
read-only command or artifact shows the resolved profiles/modules before
startup. Do not count profile-only systems, editor profiles, option presets,
templates, overlays, or generic config renderers unless they carry the same
layer contract.

## AOA-T-0037 External Evidence Notes

2026-05-12 result: exact-fit second context found, and `AOA-T-0037` exited the
promoted queue through a bundle-local canonical review.

Searched and accepted:

- [Get Physics Done README](https://github.com/psi-oss/get-physics-done/blob/000d8c829132a4a1419c5e9e89983146d8d1ae75/README.md)
  documents `gpd doctor --runtime <runtime> --local` and
  `gpd doctor --runtime <runtime> --global` as runtime-readiness checks for a
  selected runtime target, and keeps paper/manuscript readiness warnings
  distinct from `paper-build` truth.
- [GPD CLI doctor command](https://github.com/psi-oss/get-physics-done/blob/000d8c829132a4a1419c5e9e89983146d8d1ae75/src/gpd/cli.py)
  routes `doctor --runtime` into runtime-readiness mode with normalized
  runtime, install scope, target directory, and optional live executable
  probes.
- [GPD health implementation](https://github.com/psi-oss/get-physics-done/blob/000d8c829132a4a1419c5e9e89983146d8d1ae75/src/gpd/core/health.py)
  resolves runtime, scope, and target into one doctor context, checks
  runtime-specific launcher/target/provider/toolchain surfaces, returns
  `mode="runtime-readiness"` for selected runtime checks, and separates
  failures from warnings.
- [GPD installer preflight](https://github.com/psi-oss/get-physics-done/blob/000d8c829132a4a1419c5e9e89983146d8d1ae75/bin/install.js)
  consumes the structured doctor report, treats `fail` checks as blockers,
  preserves advisories, and points the operator back to the exact selected
  `gpd doctor --runtime ...` command before continuing.

Rejected as still adjacent:

- Generic `doctor` commands such as package-manager, framework, editor, or
  project-health diagnostics remain adjacent unless the selected runtime,
  profile, preset, target, or equivalent selector changes which checks matter.
- Permission gates, unattended-readiness validators, plan preflight, build
  checks, smoke tests, and monitoring dashboards remain sibling surfaces unless
  they preserve the same selected-target pre-start diagnostic seam.

Future watch shape: keep `AOA-T-0037` centered on selected-target doctor
readiness with item-level severity, and route render truth, lifecycle,
permission alignment, plan validation, build truth, smoke, and monitoring back
to their sibling techniques or owner repos.

## AOA-T-0038 External Evidence Notes

2026-05-12 result: exact-fit second context found, and `AOA-T-0038` exited the
promoted queue through a bundle-local canonical review.

Searched and accepted:

- [Metaflow Devstack README](https://github.com/Netflix/metaflow/blob/6d509db6a094bcba585681a1193e590cb4d8074e/devtools/README.md)
  documents a local Kubernetes development stack with `make up`, `make
  all-up`, `SERVICES_OVERRIDE=... make up`, `make shell`, and `make down`;
  service selection and dependency resolution stay inside the devstack
  lifecycle contract.
- [Metaflow Devstack Makefile](https://github.com/Netflix/metaflow/blob/6d509db6a094bcba585681a1193e590cb4d8074e/devtools/Makefile)
  keeps Docker checks, local tool setup, service selection or override,
  Minikube tunnel startup, Tilt startup, operator next steps, shell handoff,
  and teardown under one bounded local lifecycle surface.
- [Metaflow service picker](https://github.com/Netflix/metaflow/blob/6d509db6a094bcba585681a1193e590cb4d8074e/devtools/pick_services.sh)
  supports interactive service selection and a default all-services path while
  preserving one lifecycle entrypoint.
- [Metaflow non-TUI devstack start path](https://github.com/Netflix/metaflow/blob/6d509db6a094bcba585681a1193e590cb4d8074e/devtools/ci/start-devstack.sh)
  starts the local stack without the Tilt TUI and waits for API, Tiltfile, and
  generated config readiness before handing control onward.

Rejected as still adjacent:

- Generic launchers, install wizards, plain Docker Compose `up`/`down`, and
  Kubernetes or Tilt documentation remain adjacent unless one repo-owned local
  lifecycle contract owns startup, follow-through, and teardown for a bounded
  stack.
- Readiness checks, render previews, smoke tests, and benchmark harnesses
  remain sibling surfaces unless their entrypoint also owns the bounded local
  lifecycle.

Future watch shape: keep `AOA-T-0038` centered on operator-triggered local
stack lifecycle, and route profile composition, rendered truth, readiness
diagnosis, smoke testing, and benchmark comparison back to sibling techniques.

## AOA-T-0039 External Evidence Notes

2026-05-12 result: exact-fit second context found, and `AOA-T-0039` exited the
promoted queue through a bundle-local canonical review.

Searched and accepted:

- [LOCOMO / OpenClaw README](https://github.com/lancedb/locomo-eval/blob/1754b8fe4c7c05d4edbb7f133309c0ab6f4974e0/README.md)
  names `memory-core` as the baseline backend, compares `memory-lancedb` and
  `memory-lancedb-pro` as additive backends, and keeps all three on the same
  LOCOMO benchmark output family.
- [LOCOMO runner](https://github.com/lancedb/locomo-eval/blob/1754b8fe4c7c05d4edbb7f133309c0ab6f4974e0/src/runner.py)
  writes the same run artifacts and summary shape across backend scripts.
- [LOCOMO parallel runner](https://github.com/lancedb/locomo-eval/blob/1754b8fe4c7c05d4edbb7f133309c0ab6f4974e0/scripts/run_parallel.py)
  preserves the same output contract while enabling parallel benchmark
  execution.
- [LOCOMO result summarizer](https://github.com/lancedb/locomo-eval/blob/1754b8fe4c7c05d4edbb7f133309c0ab6f4974e0/scripts/summarize_results.py)
  reads the shared `summary.json` family and renders comparable results across
  baseline and additive runs.

Rejected as still adjacent:

- Benchmark matrices, A/B tests, product leaderboards, rolling baseline gates,
  and regression dashboards remain adjacent unless the baseline-first and
  additive paths share the same measurement surface and artifact shape.
- Baseline fixtures or Criterion-style performance history remain adjacent
  unless additive profiles are explicitly compared against the same baseline
  profile without mutating the default path.

Future watch shape: keep `AOA-T-0039` centered on stable baseline-first
comparison discipline, and route benchmark-suite governance, promotion policy,
rolling regression gates, product scoring, profile composition, and lifecycle
control to their owning techniques or repos.

## AOA-T-0026 External Evidence Notes

2026-05-12 result: exact-fit second context found, and `AOA-T-0026` exited the
promoted queue through a bundle-local canonical review.

Searched and accepted:

- Aider's public options reference documents a default `.aider.chat.history.md`
  chat-history file.
- Aider's public configuration docs make git-root configuration a normal
  project-scoped shape.
- Aider's public FAQ treats `.aider.chat.history.md` as Markdown chat logs that
  can be copied into a gist or otherwise published as raw Markdown.
- GitHub code search found committed `.aider.chat.history.md` artifacts in
  public non-fork repositories, including `launchapp-dev/animus-cli`,
  `terraphim/terraphim-ai`, and
  `CEDARScript/cedarscript-llm-prompt-engineering`.

Rejected as still adjacent:

- Aider's release history also documents `.aider*` gitignore behavior, so
  ignored local tool state is not enough by itself.
- Session browsers, resume databases, local search products, transcript
  packaging tools, and cloud-history wrappers remain sibling or adjacent lanes
  unless the saved session itself is a project-visible artifact.

Future watch shape: keep distinguishing deliberate project-visible session
artifacts from accidental raw-log commits and ignored local tool history.

## AOA-T-0036 External Evidence Notes

2026-05-12 result: exact-fit second context found, and `AOA-T-0036` exited the
promoted queue through a bundle-local canonical review.

Searched and accepted:

- Dockform documents `plan` before `apply`, so the operator sees the planned
  service/config change before Docker Compose startup is invoked.
- Dockform documents `compose render` as a fully resolved Docker Compose config
  render, with secrets masked by default unless explicitly shown.
- Dockform source builds and prints the plan before confirmation, then applies
  the already-built plan; its Docker Compose wrapper renders services, config
  hashes, full config JSON, and raw resolved YAML before `docker compose up -d`.

Rejected as still adjacent:

- Plain `docker compose config`, `docker compose config --services`, and Docker
  Compose `alpha dry-run` expose useful render or simulation primitives, but do
  not by themselves establish the operator review seam.
- Helm `template`, Kustomize build, Skaffold render, deployment previews, and
  generic dry-run surfaces render manifests or deployment plans, but drift into
  deployment-preview authority unless they center local runtime truth review.
- `OpenDAX`-style config-before-startup lanes, Devcontainer
  `read-configuration`, runtime utility pages, and Docker validation checklists
  expose resolved configuration or service lists, but the object is readiness,
  validation, or utility support rather than a distinct pre-start review
  contract.

Future watch shape: keep `AOA-T-0036` centered on the rendered-truth review seam
and route lifecycle control, host readiness, deployment preview, and benchmark
comparison back to their sibling techniques.

## AOA-T-0054 External Evidence Notes

2026-05-12 result: exact-fit second context found, and `AOA-T-0054` exited the
promoted queue through a bundle-local canonical review.

Searched and accepted:

- Claude Code's official skills documentation records a skill content lifecycle
  where invoked skill content enters the conversation and auto-compaction carries
  invoked skills forward within a token budget.
- The same lifecycle says compaction re-attaches recent skill invocations after
  the summary, keeping bounded skill content rather than arbitrary session
  history.
- The same lifecycle gives an explicit post-compaction reload path: when a large
  or older skill was truncated or dropped, re-invoke it after compaction to
  restore the full content.

Rejected as still adjacent:

- Generic skill discovery, marketplace installation, plugin setup, and skill
  registry surfaces remain adjacent unless the object is post-compaction skill
  availability or reload.
- Long-term memory, transcript replay, context-summary policy, and full prompt
  reconstruction remain sibling lanes rather than evidence for this technique.
- Product-wide skill lifecycle governance remains too broad unless it preserves
  the narrow compaction recovery seam.

Future watch shape: keep `AOA-T-0054` centered on post-compaction skill
availability, bounded reattachment, and explicit reload from canonical sources;
route compaction summary policy, memory recall, installer behavior, marketplace
curation, and full context reconstruction to sibling techniques.

## AOA-T-0055 External Evidence Notes

2026-05-12 result: exact-fit second context found, and `AOA-T-0055` exited the
promoted queue through bundle-local canonical review.

Exact-fit source:

- [SpecForge-Agent](https://github.com/wirelessr/SpecForge-Agent) at
  `bfbc98f7be766b36e7979fb5fd9472d69a3d0c48` documents a complete
  `Requirements -> Design -> Tasks -> Execution` workflow with phased approval.
- Its `PlanAgent` creates `requirements.md`, `DesignAgent` builds `design.md`
  from approved requirements, and `TasksAgent` reads both `design.md` and
  `requirements.md` before writing `tasks.md`.
- Its end-to-end workflow tests check that `requirements.md`, `design.md`, and
  `tasks.md` exist and are generated before implementation proceeds.

Supporting boundary check:

- [GitHub Spec Kit](https://github.com/github/spec-kit) at
  `765e60f1c46a242b44238ce1fc7bdd2a5e9cd1ab` exposes a visible
  `spec.md` -> `plan.md` -> `tasks.md` spine. It supports the layer boundary,
  but the technique intentionally does not import Spec Kit's full SDD command
  suite, constitution checks, hooks, research artifacts, branch workflow, or
  implementation flow.

Rejected widening:

- full spec-driven development doctrine;
- Kiro or Spec Kit command suites;
- approval orchestration;
- agent platform architecture;
- memory/session management;
- implementation execution;
- task dependency graph, ready-frontier, ranking, or staffing behavior.

Future watch shape: keep `AOA-T-0055` centered on the pre-execution planning
ladder. Split future work only if methodology adoption, approval flow, command
automation, implementation execution, research/constitution gates, memory
state, or dependency graph coordination becomes the actual object.

## Deferred Pack Watch

These bundles still need external evidence, but no new bounded lane note is worth recording here yet beyond the current queue docs.

| technique | current blocker | next honest trigger |
|---|---|---|
| [AOA-T-0020](../../../../techniques/knowledge-lift/kag-source-lift/evidence-note-provenance-lift/TECHNIQUE.md) | Stage 2 Pack 6 checked Agent Loom; it remains adjacent because typed markdown evidence records and paths exist, but no derived note-kind/path provenance manifest or reader was accepted | one committed non-eval corpus that reuses typed note-kind and note-path provenance in a derived reader or manifest |
| [AOA-T-0005](../../../../techniques/execution/intent-chain/new-intent-rollout-checklist/TECHNIQUE.md) | Stage 2 checked intent-classification, chatbot eval, and IBN benchmark lanes; they remain adjacent because they evaluate intents rather than recording one-new-intent dry-run-chain rollout | one non-origin rollout record proving the same checklist on a real new-intent extension path |
| [AOA-T-0022](../../../../techniques/knowledge-lift/kag-source-lift/risk-and-negative-effect-lift/TECHNIQUE.md) | Stage 2 checked exact-heading public code search, sibling corpus search, and broad AI risk/framework lanes; they remain adjacent unless the exact five-part markdown contract is present | one second committed corpus using the exact five-part `Risks` split |

## AOA-T-0020 And AOA-T-0046 Through AOA-T-0048 Stage 2 Pack 6 Notes

2026-05-12 result: Pack 6 moved two fresh source-lift rows from origin-only
to first second-context support, and preserved two adjacent or unresolved lanes
without forcing status changes.

Exact-fit second-context support:

- [AOA-T-0046](../../../../techniques/knowledge-lift/kag-source-lift/repo-doc-surface-lift/TECHNIQUE.md):
  `nuxt-content/nuxt-llms` at `6faa1c45e082274267eae9295b501ab0053d0365`
  exposes a `llms.txt` route built from configured documentation sections,
  titles, descriptions, links, and notes. This fits the bounded repo-doc
  surface-lift contract because the generated reader points back to authored
  docs instead of becoming docs truth, policy, scoring, or a filesystem-wide
  taxonomy.
- [AOA-T-0047](../../../../techniques/knowledge-lift/kag-source-lift/github-review-template-lift/TECHNIQUE.md):
  GitHub's public issue and pull request template behavior turns authored
  repository templates into issue chooser entries, rendered issue forms, and
  pull request body intake surfaces. This fits the template-intake lift
  contract as first second-context evidence, but not yet as a review-specific
  manifest or state machine.

Adjacent or unresolved lanes:

- [AOA-T-0020](../../../../techniques/knowledge-lift/kag-source-lift/evidence-note-provenance-lift/TECHNIQUE.md):
  Agent Loom at `0b8273c25c367bd64b7a9a31c95cfca26a620e7e` is a strong
  public markdown-first record corpus with typed evidence records, audit
  records, and record paths. It remains adjacent because the accepted source
  surfaces preserve record grammar and repo-local graph reading, not the same
  derived note-kind plus note-path provenance manifest or reader.
- [AOA-T-0048](../../../../techniques/knowledge-lift/kag-source-lift/semantic-review-surface-lift/TECHNIQUE.md):
  public AI/code review and quality-report products were checked as likely
  overlap, but they widen into scoring, summarization, policy checks, or
  product review rather than preserving authored semantic-review markdown as
  the source for a bounded derived cluster reader.

Next honest search shape:

- `AOA-T-0020`: a committed non-eval markdown corpus with typed support notes
  lifted by kind and path into a derived reader or manifest.
- `AOA-T-0046`: closed by the 2026-05-13 focused route-map pass; reopen only
  if the route-reader boundary drifts or a separate docs layer needs its own
  source class.
- `AOA-T-0047`: a review-specific template manifest or intake reader that
  inventories authored templates without owning approval, triage, or review
  state.
- `AOA-T-0048`: an authored semantic-review or boundary-review markdown corpus
  with a derived cluster/finding/next-step reader, not an AI review score or
  generic review summary.

## Notes

- Use [Promotion Readiness Matrix](../promotion-readiness-matrix/README.md) for the full queue and lane counts.
- Use [External Evidence Sprint Runbook](../external-evidence-sprint-runbook/README.md) for execution order and operator rules.
- When a bundle exits the queue, keep the closure precedent here short and move the real verdict back into the bundle-local notes plus shared queue docs.
