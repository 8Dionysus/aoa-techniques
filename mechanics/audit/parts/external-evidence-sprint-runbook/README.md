# External Evidence Sprint Runbook

This runbook records the live maintainer path for external-evidence work over the remaining `promoted` queue in `aoa-techniques`.

Use it when the question is not "which promoted bundle is generally closest to `canonical`?", but "how should the next external proof sprint run without repeating stale searches, widening bundle meaning, or faking closure?"

See also:
- [Promotion Readiness Matrix](../promotion-readiness-matrix/README.md)
- [Promotion Evidence Runbook](../promotion-evidence-runbook/README.md)
- [External Evidence Ledger](../external-evidence-ledger/README.md)
- [Long-Gap Canon Design](../../../distillation/parts/long-gap-reentry/README.md)
- [Roadmap](../../../../ROADMAP.md)
- [External Import Runbook](../../../distillation/parts/external-import-runbook/README.md)

## When To Open This

Open this runbook only when all of the following are already true:

- the bundle is already `promoted`
- the bundle already has the normal local note package for its current maturity claim
- the remaining blocker is external evidence, not missing bundle structure
- the next move should reduce uncertainty even if no status changes happen

If the problem is really donor intake or a new extraction, use [External Import Runbook](../../../distillation/parts/external-import-runbook/README.md) instead.

## Non-Goals

- no status flips unless bundle-local notes can honestly support them
- no donor-import workflow inside this runbook
- no bundle widening just to fit a tempting external surface
- no repeated searching of a lane that is already logged as exhausted without a new signal
- no opportunistic multi-technique promotion PRs; a coherent evidence pack is allowed only when every status change has bundle-local readiness notes and adverse-effect review support before shared queue docs move

## Current Sprint Order

Run the external evidence queue in this order:

1. lead queue:
   - [AOA-T-0032](../../../../techniques/proof/evaluation-chain/context-report-for-ci/TECHNIQUE.md) remains `promoted`; the 2026-05-12 Stage 1 long-pass sweep added searched-lane memory for context-compiler, context-drift, fragment-assembly, dependency-graph, and repo-quality report surfaces, but found no exact-fit second consumer
2. residual skill-ecosystem source-readiness lane:
   - [AOA-T-0042](../../../../techniques/instruction/skill-discovery/upstream-skill-health-checking/TECHNIQUE.md)
     remains `promoted`; the 2026-05-12 Pack 5 search ruled out manifest/doctor,
     registry-update, and security-risk lanes as adjacent, so reopen only from
     a pre-surface source availability plus manifest-readiness signal
3. markdown-first and fresh-extraction follow-through:
   - [AOA-T-0020](../../../../techniques/knowledge-lift/kag-source-lift/evidence-note-provenance-lift/TECHNIQUE.md)
     remains `promoted`; the 2026-05-12 Pack 6 pass ruled out Agent Loom as
     adjacent because it has typed markdown evidence records and paths but no
     accepted derived note-kind/path provenance manifest or reader
   - [AOA-T-0046](../../../../techniques/knowledge-lift/kag-source-lift/repo-doc-surface-lift/TECHNIQUE.md)
     remains `promoted`; the 2026-05-12 Pack 6 pass recorded first
     second-context support from `nuxt-content/nuxt-llms`, but the next
     promotion trigger is a second repo-owned docs route manifest outside
     framework-specific `llms.txt` generation
   - [AOA-T-0047](../../../../techniques/knowledge-lift/kag-source-lift/github-review-template-lift/TECHNIQUE.md)
     remains `promoted`; the 2026-05-12 Pack 6 pass recorded first
     second-context support from GitHub's issue and pull request template
     surfaces, but the next promotion trigger is a review-specific template
     manifest or intake reader beyond platform-native rendering
   - [AOA-T-0048](../../../../techniques/knowledge-lift/kag-source-lift/semantic-review-surface-lift/TECHNIQUE.md)
     remains `promoted`; the 2026-05-12 Pack 6 pass ruled out AI review, code
     review summary, quality-report, and scoring lanes as adjacent
4. long-gap holds:
   - [AOA-T-0005](../../../../techniques/execution/intent-chain/new-intent-rollout-checklist/TECHNIQUE.md)
     remains `promoted`; the 2026-05-12 Stage 2 long-pass search ruled out
     generic intent-classification, assistant-eval, and IBN benchmark lanes as
     adjacent, so reopen only from a rollout-specific signal
   - [AOA-T-0022](../../../../techniques/knowledge-lift/kag-source-lift/risk-and-negative-effect-lift/TECHNIQUE.md)
     remains `promoted`; the 2026-05-12 Stage 2 long-pass search ruled out
     exact-heading public code search, sibling contrast surfaces, and broad AI
     risk-framework lanes as adjacent, so reopen only from a corpus that
     actually adopts the same five-part markdown contract

Closed precedents:

- [AOA-T-0028](../../../../techniques/execution/agent-workflows-core/confirmation-gated-mutating-action/TECHNIQUE.md) and [AOA-T-0031](../../../../techniques/execution/agent-workflows-core/shell-composable-agent-invocation/TECHNIQUE.md) have exited this sprint lane through separate canonical reviews.
- [AOA-T-0026](../../../../techniques/history/history-artifacts/session-capture-as-repo-artifact/TECHNIQUE.md) has exited this sprint lane through a separate canonical review after Aider's public `.aider.chat.history.md` artifact family closed the capture-as-artifact gap.
- [AOA-T-0036](../../../../techniques/execution/runtime-truth-lifecycle/render-truth-before-startup/TECHNIQUE.md) has exited this sprint lane through a separate canonical review after Dockform's plan/render-before-apply surface closed the render-truth review seam.
- [AOA-T-0037](../../../../techniques/execution/runtime-truth-lifecycle/contextual-host-doctor/TECHNIQUE.md) has exited this sprint lane through a separate canonical review after Get Physics Done's selected-runtime `gpd doctor` surface closed the contextual preflight readiness gap.
- [AOA-T-0038](../../../../techniques/execution/runtime-truth-lifecycle/one-command-service-lifecycle/TECHNIQUE.md) has exited this sprint lane through a canonical review after Metaflow Devstack closed the one-entrypoint local lifecycle gap.
- [AOA-T-0039](../../../../techniques/execution/runtime-truth-lifecycle/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) has exited this sprint lane through a canonical review after LOCOMO / OpenClaw closed the baseline-first additive benchmark gap.
- [AOA-T-0027](../../../../techniques/instruction/instruction-surface/cross-agent-skill-propagation/TECHNIQUE.md), [AOA-T-0029](../../../../techniques/instruction/instruction-surface/nested-rule-loading/TECHNIQUE.md), and [AOA-T-0030](../../../../techniques/instruction/instruction-surface/fragmented-agent-context/TECHNIQUE.md) have exited this sprint lane through a canonical review after ai-rulez, Claude Code memory/rules, and Cline Rules closed the managed fan-out, layered precedence, and fragment-first context gaps.
- [AOA-T-0024](../../../../techniques/instruction/instruction-surface/upstream-mirroring-with-provenance/TECHNIQUE.md), [AOA-T-0025](../../../../techniques/instruction/capability-registry/capability-spec-versioning/TECHNIQUE.md), [AOA-T-0040](../../../../techniques/instruction/capability-boundary/skill-vs-command-boundary/TECHNIQUE.md), [AOA-T-0041](../../../../techniques/instruction/skill-discovery/skill-marketplace-curation/TECHNIQUE.md), and [AOA-T-0043](../../../../techniques/instruction/capability-boundary/multi-source-primary-input-provenance/TECHNIQUE.md) have exited this sprint lane through a canonical review after managedcode/dotnet-skills, A2A Agent Card, Claude Code skills, VoltAgent awesome-agent-skills, and StableNexus closed the mirror-provenance, versioned-capability, skill-command, editorial-curation, and primary/supporting source-ordering gaps.
- [AOA-T-0045](../../../../techniques/history/history-artifacts/witness-trace-as-reviewable-artifact/TECHNIQUE.md) has exited this sprint lane through a canonical review after Maida / AgentDbg closed the structured run trace artifact gap.
- [AOA-T-0033](../../../../techniques/instruction/docs-boundary/decision-rationale-recording/TECHNIQUE.md) has exited this sprint lane through a canonical review after MADR closed the one-decision rationale record gap.
- [AOA-T-0049](../../../../techniques/execution/ready-work-graphs/dependency-aware-task-graph/TECHNIQUE.md) and [AOA-T-0050](../../../../techniques/execution/ready-work-graphs/ready-work-from-blocker-graph/TECHNIQUE.md) have exited this sprint lane through a canonical review after Taskwarrior closed the dependency-graph and blocker-free frontier gaps.
- [AOA-T-0051](../../../../techniques/continuity/review-compaction/commit-triggered-background-review/TECHNIQUE.md) and [AOA-T-0052](../../../../techniques/continuity/review-compaction/review-findings-compaction/TECHNIQUE.md) have exited this sprint lane through a canonical review after Qodo / PR-Agent closed the push-triggered review artifact and persistent findings-compaction gaps.
- [AOA-T-0054](../../../../techniques/continuity/review-compaction/compaction-resilient-skill-loading/TECHNIQUE.md) has exited this sprint lane through a canonical review after Claude Code's official skills lifecycle closed the post-compaction skill reattachment and re-invocation gap.
- [AOA-T-0055](../../../../techniques/execution/ready-work-graphs/requirements-design-tasks-ladder/TECHNIQUE.md) has exited this sprint lane through a canonical review after SpecForge-Agent closed the requirement, design, and task artifact ladder gap, with GitHub Spec Kit used only as supporting boundary evidence.
- [AOA-T-0056](../../../../techniques/continuity/handoff-continuation/channelized-agent-mailbox/TECHNIQUE.md) has exited this sprint lane through a canonical review after `mycel` closed the channelized mailbox gap with an AI-agent mailbox, bounded thread identity, replayable thread logs, sync cursor, outbox retry, read/delivery state, and explicit local ACK rows.
- [AOA-T-0057](../../../../techniques/continuity/handoff-continuation/structured-handoff-before-compaction/TECHNIQUE.md) has exited this sprint lane through a canonical review after `cwc-long-running-agents` and `openclaw-memory-kit` closed the structured handoff-before-context-loss gap with read-before-restart progress notes and compaction memoryFlush handoff packets.
- [AOA-T-0060](../../../../techniques/continuity/handoff-continuation/session-opening-ritual-before-work/TECHNIQUE.md) has exited this sprint lane through a canonical review after `cwc-long-running-agents` closed the session-opening gap with a read-first `PROGRESS.md`, recent git-history check, and project baseline check before work.
- [AOA-T-0061](../../../../techniques/continuity/handoff-continuation/cross-repo-resource-map-bootstrap/TECHNIQUE.md) has exited this sprint lane through a canonical review after `openclaw-linear-plugin` closed the cross-repo startup-map gap with configured repo maps, selected repo sets, named worktree paths, injected project context, and first-read root instruction files.
- [AOA-T-0062](../../../../techniques/continuity/handoff-continuation/episode-bounded-agent-loop/TECHNIQUE.md) has exited this sprint lane through a canonical review after Cloudflare's long-running Agents guide closed the bounded episode-loop gap with durable plan steps, checkpoints, one-step-at-a-time execution, next-step scheduling, failed-step state, re-planning, and human oversight boundaries.
- [AOA-T-0063](../../../../techniques/instruction/capability-registry/versioned-agent-registry-contract/TECHNIQUE.md) has exited this sprint lane through a canonical review after Nacos's A2A Registry guide closed the named versioned registry-entry gap with namespace/name identity, unique versions, a current default published version, SDK and HTTP publication paths, and explicit AgentCard fields.
- [AOA-T-0064](../../../../techniques/instruction/capability-registry/capability-discovery/TECHNIQUE.md) has exited this sprint lane through a canonical review after Nacos's A2A Registry guide closed the bounded discovery-query gap with SDK name lookup, HTTP detail lookup, explicit list/search parameters, and future search dimensions kept outside the current contract.
- [AOA-T-0065](../../../../techniques/tool-use/tool-gateway/mcp-gateway-proxy/TECHNIQUE.md) has exited this sprint lane through a canonical review after `smart-mcp-proxy/mcpproxy-go` closed the gateway-proxy gap with one MCP client endpoint over multiple configured upstream servers, tool metadata discovery, mediated `call_tool_*` variants, server-scoped tool names, and proxy-boundary sensitive-data inspection.
- [AOA-T-0066](../../../../techniques/history/history-artifacts/transcript-replay-artifact/TECHNIQUE.md) has exited this sprint lane through a canonical review after `dataprofessor/cortex-replay` plus Snowflake's public Cortex Code replay guide closed the transcript-replay gap with already-saved session transcripts transformed into one self-contained interactive replay artifact, bounded filtering/redaction controls, and source-artifact authority kept visible.
- [AOA-T-0067](../../../../techniques/history/history-artifacts/transcript-linked-code-lineage/TECHNIQUE.md) has exited this sprint lane through a canonical review after `ai4curation/ai-blame` closed the code-lineage gap with AI trace-derived line attribution, session id metadata, transcript listing/viewing, and review workflows that reopen saved session evidence from code lines or blocks.
- [AOA-T-0068](../../../../techniques/governance/approval-evidence/fail-closed-evidence-gate/TECHNIQUE.md) has exited this sprint lane through a canonical review after `mvar-security/clawzero` closed the fail-closed gate gap with deterministic execution-boundary enforcement before tool/process sinks, explicit allow/block decisions, adapter-level blocked execution, and witness artifacts that preserve reviewable verdict evidence.
- [AOA-T-0069](../../../../techniques/governance/approval-evidence/approval-bound-durable-jobs/TECHNIQUE.md) has exited this sprint lane through a canonical review after `pydantic/pydantic-ai` closed the approval-bound durable-job gap with deferred approval and external-call requests, stable pending-call identity, original message history, explicit deferred results, and durable-execution support for long-running human-in-the-loop workflows.
- [AOA-T-0070](../../../../techniques/ingest/media-ingest/two-stage-document-ocr-pipeline/TECHNIQUE.md) has exited this sprint lane through a canonical review after `JaidedAI/EasyOCR` closed the staged OCR handoff gap with separate detection and recognition methods, public bounding-box/text/confidence results, structured dict/JSON output, and visible CRAFT detection plus CRNN/custom recognition stage boundaries.
- [AOA-T-0071](../../../../techniques/ingest/media-ingest/template-backed-field-extraction-after-ocr/TECHNIQUE.md) has exited this sprint lane through a canonical review after `kotaro-kinoshita/yomitoku` closed the post-OCR field extraction gap with YAML schema field targets, visible rule methods, source metadata, confidence, and explicit `not_found` posture for missed extraction.
- [AOA-T-0072](../../../../techniques/ingest/media-ingest/perceptual-media-dedupe-with-threshold-review/TECHNIQUE.md) has exited this sprint lane through a canonical review after `qarmin/czkawka` closed the perceptual media dedupe gap with explicit threshold tuning, perceptual hash options, reviewable grouped output, JSON/text result surfaces, and default-off deletion.
- Use their entries in [External Evidence Ledger](../external-evidence-ledger/README.md) as closure examples, not as active search targets.

Why this order:

- `AOA-T-0032` is still the clearest report-only blocker, but its currently known public lanes are searched; reopen it only from a new artifact-first signal instead of repeating context-compiler, fragment-assembly, graph, or repo-quality searches
- `AOA-T-0042` is the only Pack 5 residual; reopen it from source-readiness-before-surfacing evidence rather than install/update, security scanning, registry governance, or generic monitoring overlap
- `AOA-T-0020` should not reopen until a real non-origin note-kind/path manifest or reader exists
- `AOA-T-0046` and `AOA-T-0047` now have first second-context support; reopen them only from a stronger repo-owned route or review-template reader, not from generic docs generation or platform-native forms
- `AOA-T-0048` should not reopen until a real non-origin semantic-review reader exists
- `AOA-T-0033` is closed; future decision-record work should split into a sibling only if multi-decision records, ADR tooling, or decision-log governance become the actual object
- `AOA-T-0049` and `AOA-T-0050` are closed; future graph work should split only if ranking, dispatch, graph health, or tracker policy becomes the actual object
- `AOA-T-0051` and `AOA-T-0052` are closed; future review-loop work should split only if auto-fix, approval, merge policy, review chat, or full PR governance becomes the actual object
- `AOA-T-0054` is closed; future post-compaction work should split only if compaction-summary policy, memory recall, full context reconstruction, installer behavior, marketplace curation, or product-wide skill lifecycle governance becomes the actual object
- `AOA-T-0055` is closed; future planning-ladder work should split only if methodology adoption, approval flow, command automation, research or constitution gates, memory state, implementation execution, task dependency graphs, or ready-frontier coordination becomes the actual object
- `AOA-T-0056` is closed; future mailbox work should split only if remote delivery proof, broker governance, trust or encryption policy, adapters, transcript history, or handoff authorization becomes the actual object
- `AOA-T-0057` is closed; future handoff-packet work should split only if transcript packaging, mailbox receipt, git verification, memory search, session databases, hook policy, cron memory, or full harness lifecycle governance becomes the actual object
- `AOA-T-0060` is closed; future session-opening work should split only if task selection, startup test doctrine, git-claim verification, handoff authoring, or full boot protocol becomes the actual object
- `AOA-T-0061` is closed; future cross-repo startup work should split only if semantic context mapping, architecture inventories, repo authorization, worktree lifecycle, dispatch routing, model selection, or full workspace-platform governance becomes the actual object
- `AOA-T-0062` is closed; future episode-loop work should split only if session-opening ritual, handoff packet shape, git-claim verification, runtime checkpointing, proof settlement, durable-job orchestration, supervision, budgeting, or full autonomous-agent lifecycle governance becomes the actual object
- `AOA-T-0063` is closed; future registry-entry work should split only if capability-spec schema, discovery query behavior, fuzzy search, endpoint subscription, registry product workflow, trust or signature policy, marketplace curation, graph semantics, or registry governance becomes the actual object
- `AOA-T-0064` is closed; future discovery work should split only if ranking, recommendation, endpoint subscription, runtime invocation, trust or signature policy, marketplace curation, graph semantics, registry product workflow, or broader registry protocol governance becomes the actual object
- `AOA-T-0065` is closed; future gateway work should split only if routing mode selection, tool ranking, quarantine governance, scanner policy, local service lifecycle, OAuth or token management, UI/dashboard behavior, endpoint subscription, or broader MCP platform governance becomes the actual object
- `AOA-T-0066` is closed; future replay work should split only if first-save capture, transcript packaging, local indexing, witness forensics, hosted sharing, dashboards, replay editors, memory systems, or publishing platforms become the actual object
- `AOA-T-0067` is closed; future lineage work should split only if AI-percentage scoring, policy gates, review enforcement, transcript indexing, hosted search, dashboards, telemetry, repository analytics, or memory recall becomes the actual object
- `AOA-T-0068` is closed; future fail-closed gate work should split only if human approval, signed witness chains, attack-pack validation, policy authoring, gateway products, sandboxing, compliance export, budget controls, or durable job orchestration becomes the actual object
- `AOA-T-0069` is closed; future durable-job work should split only if scheduler products, queue semantics, workflow histories, retry doctrine, cloud workers, worker-fleet governance, dashboards, one-shot confirmation prompts, fail-closed verdict gates, or total durable-execution platform behavior becomes the actual object
- `AOA-T-0070` is closed; future OCR work should split only if searchable-PDF generation, OCR serving, model training, benchmark doctrine, receipt or invoice schema law, template-backed extraction, semantic media bucketing, cleanup actions, or total document-understanding product behavior becomes the actual object
- `AOA-T-0072` is closed; future perceptual dedupe work should split only if duplicate manifests, representative selection, quality ranking, archive policy, hardlink strategy, storage cleanup, semantic media bucketing, or full media-management product behavior becomes the actual object
- `AOA-T-0005` and `AOA-T-0022` stay long-gap by design; `AOA-T-0005`
  now has searched-lane memory, so repeat searches should start from a real
  new-intent rollout artifact rather than NLU/eval/benchmark overlap
- `AOA-T-0022` now has searched-lane memory too, so repeat searches should
  start from committed authored bundles with all five caution headings rather
  than broad risk taxonomy, security framework, or `Failure modes` plus
  `Blind spots` overlap

## Swarm Layout

- main agent owns:
  - sprint order
  - exact-fit versus overlap verdicts
  - updates to [Promotion Readiness Matrix](../promotion-readiness-matrix/README.md)
  - updates to [External Evidence Ledger](../external-evidence-ledger/README.md)
  - any later sync to [Roadmap](../../../../ROADMAP.md)
  - `python -m pip install -r requirements-dev.txt`
  - final `python scripts/release_check.py`
- each worker owns:
  - one technique bundle at a time
  - one bounded search lane
  - bundle-local note edits only when exact-fit evidence is real
- workers must not edit:
  - `TECHNIQUE_INDEX.md`
  - `generated/**`
  - repo-wide semantic-review docs
  - repo-wide roadmap or queue docs unless the main agent requests the sync

## Search Order

1. Read the bundle first.
   - open `TECHNIQUE.md`
   - open `notes/canonical-readiness.md`
   - open `notes/second-context-adaptation.md` when it exists
2. Check shared search memory.
   - open [Promotion Readiness Matrix](../promotion-readiness-matrix/README.md)
   - open [External Evidence Ledger](../external-evidence-ledger/README.md)
   - do not rerun a false-positive lane unless a new public signal exists
3. Search the exact object layer first.
   - look for the same reusable object in a second real public consumer
   - prefer live artifacts, workflows, or repo-owned surfaces over marketing or architectural prose
4. Reject adjacent fits explicitly.
   - if the surface is really a sibling technique, name it and stop
   - if the surface widens into product, platform, or orchestration doctrine, stop
5. Update locally only after the evidence is real.
   - update bundle-local notes first
   - delay any status discussion until the bundle can honestly carry it

## Evidence Verdict Contract

Each search lane should end with one bounded result:

- `exact-fit evidence found`
  - name the second consumer
  - explain why it matches the current bundle contract
  - list the bundle-local files that should change
- `adjacent but insufficient`
  - name the surface
  - explain why it is overlap, sibling, or too broad
  - add the result to [External Evidence Ledger](../external-evidence-ledger/README.md)
- `no fit found in searched lane`
  - name the lane
  - restate the blocker in one sentence
  - name the next honest search shape

## Bundle-Local Update Path

If exact-fit evidence lands, the preferred local update order is:

1. update `notes/second-context-adaptation.md`
2. update `notes/canonical-readiness.md`
3. update `TECHNIQUE.md` only if wording, examples, checks, or frontmatter need honest reinforcement
4. add `notes/adverse-effects-review.md` only if the bundle is actually ready to become `canonical`

## Stop Rules

- if the candidate evidence would require new bundle meaning, stop and log it as overlap
- if the candidate evidence is really a donor for a future new technique, route it to [External Import Runbook](../../../distillation/parts/external-import-runbook/README.md)
- if the search result only improves examples but not live reuse, keep the status blocker explicit
- if the same public source appears across multiple bundles, split ownership by target bundle and keep note edits disjoint
- if the sprint finds no exact-fit evidence, that is still a valid result; close the lane cleanly and move on

## Completion Criteria

An external evidence sprint is successful when each active bundle exits with one of these outcomes:

- one exact-fit second consumer is found and bundle-local notes are updated honestly
- one adjacent lane is ruled out and recorded so it is not searched again casually
- one searched lane is exhausted and the next search shape is named concretely

The sprint does not need to increase the canonical count to count as progress.

## Validation And Merge Discipline

- keep bundle edits local until evidence is real
- merge one technique per PR
- run `python scripts/release_check.py` after a merge-ready bundle exists
- update [Promotion Readiness Matrix](../promotion-readiness-matrix/README.md), [External Evidence Ledger](../external-evidence-ledger/README.md), and [Roadmap](../../../../ROADMAP.md) only when the blocker or queue meaning actually changed

## Notes

- This runbook is intentionally narrower than [Roadmap](../../../../ROADMAP.md); it owns live search execution, not the whole historical audit record.
- Expand [External Evidence Ledger](../external-evidence-ledger/README.md) when a real lane search happens or a bundle exits the queue.
