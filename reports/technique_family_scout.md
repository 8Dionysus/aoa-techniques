# Technique Family Scout

This file is generated from the current kind registry, family seed, wave1 overlay, and generated catalog.
Do not edit it by hand; run `python scripts/build_kind_manifest.py`.

This report is scout-only, non-authoritative, and weaker than bundle frontmatter. It must not be treated as schema truth, frontmatter truth, or automatic remap authority.

Use this report when you want to inspect likely family clusters without promoting `family` into frontmatter, schema, or validator-required bundle truth.

## Scout Scope

| family | summary | total | canonical | promoted |
|---|---|---|---|---|
| `agent-workflows-core` | Safe bounded agent execution backbone, one-shot posture, and mutation seam discipline. | `5` | `5` | `0` |
| `intent-chain` | Intent normalization, dry-run validation, and safe rollout of new intent types. | `2` | `1` | `1` |
| `docs-boundary` | Document-role separation, status snapshots, rationale notes, and public-safe sharing hygiene. | `4` | `3` | `1` |
| `instruction-surface` | Composed, mirrored, layered, and propagated instruction or context surfaces with explicit source ownership. | `7` | `2` | `5` |
| `evaluation-chain` | Machine-readable validation contract production and staged promotion from signal to enforcement. | `3` | `2` | `1` |
| `published-summary` | Published summary storage, remediation, integrity, and rendering policy. | `4` | `4` | `0` |
| `skill-support` | Boundary-contract testing, invariant coverage, and bounded-context vocabulary around capability seams. | `3` | `3` | `0` |
| `kag-source-lift` | Section, metadata, provenance, relation, repo-doc, and review-surface lift from authoritative markdown. | `8` | `3` | `5` |
| `history-artifacts` | Capture, version, replay, index, and lineage-link session evidence as durable reviewable artifacts. | `6` | `2` | `4` |
| `runtime-truth-lifecycle` | Render effective runtime truth, check host readiness, operate service lifecycle, and benchmark additive profiles. | `4` | `0` | `4` |
| `capability-registry` | Versioned capability or registry contracts and bounded lookup over published entries. | `3` | `0` | `3` |
| `capability-boundary` | Explicit separation between capability meaning, input provenance, recommendation truth, and host actionability. | `3` | `0` | `3` |
| `skill-discovery` | Editorial discovery and health visibility over upstream-owned skill sources. | `2` | `0` | `2` |
| `ready-work-graphs` | Dependency-aware planning, frontier selection, and laddering from requirements to tasks. | `3` | `0` | `3` |
| `review-compaction` | Background review triggering, findings compaction, and recovery of capability loading after compaction. | `3` | `0` | `3` |
| `handoff-continuation` | Mailbox, packet, receipt, checkpoint, episode, and cross-repo continuation seams. | `7` | `0` | `7` |
| `tool-gateway` | One bounded caller surface over multiple upstream tool or MCP endpoints. | `1` | `0` | `1` |
| `approval-evidence` | Approval-gated mutation and durable work with explicit allow or block evidence. | `2` | `0` | `2` |
| `media-ingest` | OCR, field extraction, normalization, dedupe, and semantic bucketing of external media inputs. | `5` | `0` | `5` |
| `donor-harvest` | Harvest reviewed sessions into donor packs, bounded packets, progression deltas, or overlay artifacts without forced promotion. | `4` | `0` | `4` |
| `decision-routing` | Owner-layer routing, explicit fork cards, and route risk posture for next-step choice. | `3` | `0` | `3` |
| `diagnosis-repair` | Drift taxonomy, diagnosis packets, repair shaping, and checkpoint-bound self-repair. | `4` | `0` | `4` |
| `automation-governance` | Automation-worthiness, approval sensitivity, seed routing, and promotion-boundary review. | `5` | `0` | `5` |
| `owner-truth-closeout` | Ingress or mutation gates, proof-backed closeout, validated mirrors, and publish-readiness against owner truth. | `5` | `0` | `5` |
| `antifragility-recovery` | Degraded continuation, regrounding, and receipt-first failure analysis. | `3` | `0` | `3` |

Unassigned wave1 family suggestions: `0`.

## `agent-workflows-core`

Safe bounded agent execution backbone, one-shot posture, and mutation seam discipline.

Typical domains: `agent-workflows`.
Typical kinds: `workflow`, `guardrail`, `composition`.

Counts: `total` 5, `canonical` 5, `promoted` 0.

| technique | domain | kind | status | summary |
|---|---|---|---|---|
| [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) | `agent-workflows` | `workflow` | `canonical` | Safe workflow for agent-driven changes using explicit planning, scoped diffs, explicit validation, and concise reporting. |
| [AOA-T-0014](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) | `agent-workflows` | `workflow` | `canonical` | Implement a bounded behavior slice through test-first discipline, minimal implementation, and explicit refactor limits. |
| [AOA-T-0023](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) | `agent-workflows` | `workflow` | `canonical` | Keep shell-side agent work mostly stateless and bounded to one confirmed step per invocation so runs stay composable, reviewable, and low-memory by default. |
| [AOA-T-0028](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) | `agent-workflows` | `guardrail` | `canonical` | Require one explicit confirmation seam before a read or plan flow crosses into a mutating action so the action stays reviewable without widening into a multi-step autonomous loop. |
| [AOA-T-0031](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) | `agent-workflows` | `composition` | `canonical` | Make agent runs composable as shell-side one-shot tools through explicit stdin, stdout, files, and pipes without widening into generic shell advice or autonomous loops. |

## `intent-chain`

Intent normalization, dry-run validation, and safe rollout of new intent types.

Typical domains: `agent-workflows`.
Typical kinds: `workflow`, `guardrail`.

Counts: `total` 2, `canonical` 1, `promoted` 1.

| technique | domain | kind | status | summary |
|---|---|---|---|---|
| [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) | `agent-workflows` | `workflow` | `canonical` | Safe workflow that normalizes intent into a traceable plan, validates it with dry-run, and enforces contract checks before any real execution path exists. |
| [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) | `agent-workflows` | `guardrail` | `promoted` | Checklist for safely adding a new intent type to an intent-plan-dry-run chain without contract drift. |

## `docs-boundary`

Document-role separation, status snapshots, rationale notes, and public-safe sharing hygiene.

Typical domains: `docs`.
Typical kinds: `artifact`, `guardrail`.

Counts: `total` 4, `canonical` 3, `promoted` 1.

| technique | domain | kind | status | summary |
|---|---|---|---|---|
| [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) | `docs` | `artifact` | `canonical` | Repository document role separation pattern that keeps status, plans, history, decisions, and run instructions in distinct canonical homes. |
| [AOA-T-0009](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) | `docs` | `artifact` | `canonical` | Keep top-level status documents short and link-driven, while routing detailed execution state and history to their canonical homes. |
| [AOA-T-0034](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md) | `docs` | `guardrail` | `canonical` | Turn sensitive technical material into a shareable artifact by removing, redacting, or generalizing details while preserving the lesson and staying distinct from approval gating or execution planning. |
| [AOA-T-0033](../techniques/docs/decision-rationale-recording/TECHNIQUE.md) | `docs` | `artifact` | `promoted` | Keep one meaningful decision in a reviewable note with context, options, rationale, and consequences while staying out of source-of-truth governance and architecture taxonomy. |

## `instruction-surface`

Composed, mirrored, layered, and propagated instruction or context surfaces with explicit source ownership.

Typical domains: `docs`.
Typical kinds: `composition`, `distribution`.

Counts: `total` 7, `canonical` 2, `promoted` 5.

| technique | domain | kind | status | summary |
|---|---|---|---|---|
| [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) | `docs` | `composition` | `canonical` | Compose agent context from smaller fragments into a stable generated artifact with deterministic ordering and source traceability. |
| [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) | `docs` | `distribution` | `canonical` | Keep one canonical rule source and distribute it to multiple agent-facing instruction surfaces without turning each target into a hand-maintained source of truth. |
| [AOA-T-0024](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) | `docs` | `distribution` | `promoted` | Mirror upstream-owned content into a curated local collection through an explicit source manifest and preserved provenance so the local copy stays reviewable without pretending to be the canonical source. |
| [AOA-T-0027](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) | `docs` | `distribution` | `promoted` | Keep one canonical skill or rule source and propagate it to multiple agent-facing targets without turning each target into a hand-maintained source of truth. |
| [AOA-T-0029](../techniques/docs/nested-rule-loading/TECHNIQUE.md) | `docs` | `composition` | `promoted` | Load hierarchical rule layers with explicit precedence so nested additions stay subordinate to one canonical source of ownership. |
| [AOA-T-0030](../techniques/docs/fragmented-agent-context/TECHNIQUE.md) | `docs` | `composition` | `promoted` | Keep agent context in bounded fragments before deterministic assembly so modular authoring stays reviewable without collapsing into the final generated artifact. |
| [AOA-T-0035](../techniques/docs/profile-preset-composition/TECHNIQUE.md) | `docs` | `composition` | `promoted` | Compose small reusable profiles into named presets so runtime posture stays reviewable without flattening composition into one opaque config or launcher doctrine. |

## `evaluation-chain`

Machine-readable validation contract production and staged promotion from signal to enforcement.

Typical domains: `evaluation`.
Typical kinds: `validation`, `guardrail`.

Counts: `total` 3, `canonical` 2, `promoted` 1.

| technique | domain | kind | status | summary |
|---|---|---|---|---|
| [AOA-T-0003](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) | `evaluation` | `validation` | `canonical` | Runnable smoke pattern where each smoke path emits a machine-readable summary that becomes the primary validation contract. |
| [AOA-T-0007](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) | `evaluation` | `guardrail` | `canonical` | Staged pattern for promoting an observed validation signal into strict enforcement without losing diagnostics or widening the fail surface too early. |
| [AOA-T-0032](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md) | `evaluation` | `validation` | `promoted` | Emit CI-facing reports for context composition, source coverage, token-estimate drift, and related composition checks without turning the report surface into the composition technique itself. |

## `published-summary`

Published summary storage, remediation, integrity, and rendering policy.

Typical domains: `evaluation`.
Typical kinds: `artifact`, `lift`, `validation`, `guardrail`.

Counts: `total` 4, `canonical` 4, `promoted` 0.

| technique | domain | kind | status | summary |
|---|---|---|---|---|
| [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) | `evaluation` | `artifact` | `canonical` | Dual-write summary pattern that keeps a stable latest alias, preserves nested history, and prevents double-count accumulation. |
| [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) | `evaluation` | `lift` | `canonical` | Read-only aggregation pattern that turns latest published summaries into a bounded remediation snapshot without replaying history or changing runtime behavior. |
| [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) | `evaluation` | `validation` | `canonical` | Read-only integrity verdict that checks telemetry and summary-layout invariants across latest published summaries without widening the hard fail surface. |
| [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) | `evaluation` | `guardrail` | `canonical` | Distinguish strict required sources from tolerant optional sources so operator-facing summary surfaces remain useful without hiding true hard failures. |

## `skill-support`

Boundary-contract testing, invariant coverage, and bounded-context vocabulary around capability seams.

Typical domains: `evaluation`, `docs`.
Typical kinds: `validation`, `artifact`.

Counts: `total` 3, `canonical` 3, `promoted` 0.

| technique | domain | kind | status | summary |
|---|---|---|---|---|
| [AOA-T-0016](../techniques/docs/bounded-context-map/TECHNIQUE.md) | `docs` | `artifact` | `canonical` | Reduce semantic drift by naming bounded contexts, separating responsibilities, and making handoff interfaces visible for docs and scoping work. |
| [AOA-T-0015](../techniques/evaluation/contract-test-design/TECHNIQUE.md) | `evaluation` | `validation` | `canonical` | Make a boundary explicit by defining expected inputs, outputs, and verification around the contract rather than around hidden internals. |
| [AOA-T-0017](../techniques/evaluation/property-invariants/TECHNIQUE.md) | `evaluation` | `validation` | `canonical` | Express stable system or domain truths as invariant-oriented tests or checks so broad behavior is constrained beyond a small handpicked example set. |

## `kag-source-lift`

Section, metadata, provenance, relation, repo-doc, and review-surface lift from authoritative markdown.

Typical domains: `docs`.
Typical kinds: `lift`.

Counts: `total` 8, `canonical` 3, `promoted` 5.

| technique | domain | kind | status | summary |
|---|---|---|---|---|
| [AOA-T-0018](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) | `docs` | `lift` | `canonical` | Lift stable technique markdown sections into derived section-level units while keeping the bundle markdown authoritative. |
| [AOA-T-0019](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) | `docs` | `lift` | `canonical` | Treat bounded frontmatter and derived catalog outputs as a metadata spine for bundle routing without replacing markdown meaning or growing schema past current needs. |
| [AOA-T-0021](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) | `docs` | `lift` | `canonical` | Lift small typed direct relations into bounded edge hints for derived consumers without turning them into graph semantics. |
| [AOA-T-0020](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) | `docs` | `lift` | `promoted` | Use typed evidence note kinds and note paths as bounded provenance handles in derived manifests without flattening them into a note graph. |
| [AOA-T-0022](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) | `docs` | `lift` | `promoted` | Lift richer `Risks` language into bounded caution-oriented lookup and reuse without turning caution into metadata, scoring, or generated policy. |
| [AOA-T-0046](../techniques/docs/repo-doc-surface-lift/TECHNIQUE.md) | `docs` | `lift` | `promoted` | Lift one bounded set of authoritative repo docs and status files into derived routing knowledge without replacing the authored docs or widening into a docs taxonomy. |
| [AOA-T-0047](../techniques/docs/github-review-template-lift/TECHNIQUE.md) | `docs` | `lift` | `promoted` | Lift authored GitHub issue and pull-request review templates into derived intake knowledge without turning templates into workflow automation or policy scoring. |
| [AOA-T-0048](../techniques/docs/semantic-review-surface-lift/TECHNIQUE.md) | `docs` | `lift` | `promoted` | Lift authored semantic-review docs into derived boundary-review knowledge without creating automatic semantic verdicts. |

## `history-artifacts`

Capture, version, replay, index, and lineage-link session evidence as durable reviewable artifacts.

Typical domains: `history`.
Typical kinds: `artifact`.

Counts: `total` 6, `canonical` 2, `promoted` 4.

| technique | domain | kind | status | summary |
|---|---|---|---|---|
| [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) | `history` | `artifact` | `canonical` | Package already-saved AI session transcripts as readable, versionable Markdown artifacts so review, handoff, and selective sharing stay possible without reopening capture semantics or turning transcript history into memory or instruction authority. |
| [AOA-T-0053](../techniques/history/local-first-session-index/TECHNIQUE.md) | `history` | `artifact` | `canonical` | Build a local searchable index over already-saved session artifacts so teams can browse or query saved history without reopening capture semantics or turning the index into memory or dashboard doctrine. |
| [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) | `history` | `artifact` | `promoted` | Capture AI coding sessions as versioned repo artifacts so project history stays searchable, reviewable, and reusable without turning session logs into memory or instruction policy. |
| [AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) | `history` | `artifact` | `promoted` | Preserve a bounded witness trace as a reviewable artifact with step visibility, state-delta notes, and human-readable summary so a nontrivial run can be inspected before any writeback or promotion without creating a new memory-object kind. |
| [AOA-T-0066](../techniques/history/transcript-replay-artifact/TECHNIQUE.md) | `history` | `artifact` | `promoted` | Turn already-saved session history into a replayable artifact so reviewers can inspect message flow and timeline without reopening capture semantics or widening into hosted replay-platform doctrine. |
| [AOA-T-0067](../techniques/history/transcript-linked-code-lineage/TECHNIQUE.md) | `history` | `artifact` | `promoted` | Link code history back to saved session evidence so reviewers can reopen the originating transcript or rationale without widening the bundle into generic repo analytics or memory doctrine. |

## `runtime-truth-lifecycle`

Render effective runtime truth, check host readiness, operate service lifecycle, and benchmark additive profiles.

Typical domains: `agent-workflows`, `evaluation`.
Typical kinds: `composition`, `validation`, `workflow`.

Counts: `total` 4, `canonical` 0, `promoted` 4.

| technique | domain | kind | status | summary |
|---|---|---|---|---|
| [AOA-T-0036](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md) | `agent-workflows` | `composition` | `promoted` | Render the actual composed runtime truth before startup so operators review the effective service and config view instead of relying only on declared profiles. |
| [AOA-T-0038](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) | `agent-workflows` | `workflow` | `promoted` | Start and stop a bounded local service stack through one explicit lifecycle entrypoint so prerequisite checks, visible runtime status, and clean shutdown stay reviewable without widening into generic launcher or platform doctrine. |
| [AOA-T-0037](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md) | `evaluation` | `validation` | `promoted` | Run selector-aware host-readiness checks before startup so environment drift becomes visible for the chosen runtime without widening into generic monitoring or lifecycle control. |
| [AOA-T-0039](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) | `evaluation` | `validation` | `promoted` | Benchmark one stable baseline profile first, then compare additive profiles against the same measurement surface and artifact shape so richer profiles stay additive and off the default path. |

## `capability-registry`

Versioned capability or registry contracts and bounded lookup over published entries.

Typical domains: `docs`.
Typical kinds: `artifact`, `discovery`.

Counts: `total` 3, `canonical` 0, `promoted` 3.

| technique | domain | kind | status | summary |
|---|---|---|---|---|
| [AOA-T-0025](../techniques/docs/capability-spec-versioning/TECHNIQUE.md) | `docs` | `artifact` | `promoted` | Keep agent-facing capability contracts in a versioned, reviewable spec so capability changes stay explicit and reusable without turning the spec into routing or registry policy. |
| [AOA-T-0063](../techniques/docs/versioned-agent-registry-contract/TECHNIQUE.md) | `docs` | `artifact` | `promoted` | Keep registry-facing capability entries reviewable as named versioned records with explicit references and metadata so publication stays bounded without widening into discovery policy or registry product doctrine. |
| [AOA-T-0064](../techniques/docs/capability-discovery/TECHNIQUE.md) | `docs` | `discovery` | `promoted` | Keep capability lookup reviewable as explicit bounded queries over published registry entries so discovery stays separate from ranking, marketplace curation, trust policy, and registry product doctrine. |

## `capability-boundary`

Explicit separation between capability meaning, input provenance, recommendation truth, and host actionability.

Typical domains: `docs`, `agent-workflows`.
Typical kinds: `guardrail`.

Counts: `total` 3, `canonical` 0, `promoted` 3.

| technique | domain | kind | status | summary |
|---|---|---|---|---|
| [AOA-T-0093](../techniques/agent-workflows/recommendation-truth-vs-host-actionability/TECHNIQUE.md) | `agent-workflows` | `guardrail` | `promoted` | Keep router recommendation truth separate from host actionability so non-executable recommendations stay visible, canonical install roots stay authoritative, and runnable actions do not masquerade as merely relevant advice. |
| [AOA-T-0040](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md) | `docs` | `guardrail` | `promoted` | Separate reusable skill meaning from user-facing command invocation so shared capability stays portable without collapsing into slash-command syntax or command-specific workflow policy. |
| [AOA-T-0043](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md) | `docs` | `guardrail` | `promoted` | Mark primary versus supporting source inputs explicitly when bridging multiple source surfaces so downstream readers and synthesis keep provenance priority visible without turning the bridge into graph semantics or ranking doctrine. |

## `skill-discovery`

Editorial discovery and health visibility over upstream-owned skill sources.

Typical domains: `docs`, `evaluation`.
Typical kinds: `discovery`, `validation`.

Counts: `total` 2, `canonical` 0, `promoted` 2.

| technique | domain | kind | status | summary |
|---|---|---|---|---|
| [AOA-T-0041](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) | `docs` | `discovery` | `promoted` | Curate a local discoverability layer over upstream-owned skill sources so selection stays editorial and reviewable without pretending the catalog owns sync, capability meaning, or registry policy. |
| [AOA-T-0042](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md) | `evaluation` | `validation` | `promoted` | Check upstream-owned skill sources for availability and manifest-readiness before surfacing them as selectable inputs so broken entries stay visible and reviewable without widening into generic monitoring, registry governance, or security doctrine. |

## `ready-work-graphs`

Dependency-aware planning, frontier selection, and laddering from requirements to tasks.

Typical domains: `agent-workflows`.
Typical kinds: `workflow`.

Counts: `total` 3, `canonical` 0, `promoted` 3.

| technique | domain | kind | status | summary |
|---|---|---|---|---|
| [AOA-T-0049](../techniques/agent-workflows/dependency-aware-task-graph/TECHNIQUE.md) | `agent-workflows` | `workflow` | `promoted` | Model multi-step coding work as explicit dependency nodes and edges so blocked state and ready work stay reviewable instead of hiding in chat memory. |
| [AOA-T-0050](../techniques/agent-workflows/ready-work-from-blocker-graph/TECHNIQUE.md) | `agent-workflows` | `workflow` | `promoted` | Derive the next bounded work queue from blocker-free graph state so operators choose from what is truly ready instead of narrating readiness from memory. |
| [AOA-T-0055](../techniques/agent-workflows/requirements-design-tasks-ladder/TECHNIQUE.md) | `agent-workflows` | `workflow` | `promoted` | Separate requirements, design, and task slices so implementation planning stays reviewable without importing a full spec-driven methodology stack. |

## `review-compaction`

Background review triggering, findings compaction, and recovery of capability loading after compaction.

Typical domains: `agent-workflows`.
Typical kinds: `workflow`, `handoff`.

Counts: `total` 3, `canonical` 0, `promoted` 3.

| technique | domain | kind | status | summary |
|---|---|---|---|---|
| [AOA-T-0051](../techniques/agent-workflows/commit-triggered-background-review/TECHNIQUE.md) | `agent-workflows` | `workflow` | `promoted` | Trigger a bounded background review after a commit so findings survive as inspectable artifacts without widening into autonomous merge, rewrite, or CI governance. |
| [AOA-T-0052](../techniques/agent-workflows/review-findings-compaction/TECHNIQUE.md) | `agent-workflows` | `handoff` | `promoted` | Compact and revalidate review findings against current code so repeated or stale findings do not overwhelm the current review surface. |
| [AOA-T-0054](../techniques/agent-workflows/compaction-resilient-skill-loading/TECHNIQUE.md) | `agent-workflows` | `handoff` | `promoted` | Re-seed skill availability after context compaction so agents can reload needed skills from canonical sources without widening into full context reconstruction or prompt stuffing. |

## `handoff-continuation`

Mailbox, packet, receipt, checkpoint, episode, and cross-repo continuation seams.

Typical domains: `agent-workflows`.
Typical kinds: `handoff`.

Counts: `total` 7, `canonical` 0, `promoted` 7.

| technique | domain | kind | status | summary |
|---|---|---|---|---|
| [AOA-T-0056](../techniques/agent-workflows/channelized-agent-mailbox/TECHNIQUE.md) | `agent-workflows` | `handoff` | `promoted` | Keep agent communication inside durable named channels with ordered replay and explicit acknowledgment so coordination survives session gaps without widening into a full messaging platform or handoff-governance stack. |
| [AOA-T-0057](../techniques/agent-workflows/structured-handoff-before-compaction/TECHNIQUE.md) | `agent-workflows` | `handoff` | `promoted` | Write one structured handoff artifact before compaction or session rollover so the next session can resume from explicit state instead of hidden memory or transcript replay. |
| [AOA-T-0058](../techniques/agent-workflows/receipt-confirmed-handoff-packet/TECHNIQUE.md) | `agent-workflows` | `handoff` | `promoted` | Require an explicit receipt state for a handoff packet before the receiving side continues so ownership transfer stays reviewable instead of being inferred from delivery or silence. |
| [AOA-T-0059](../techniques/agent-workflows/git-verified-handoff-claims/TECHNIQUE.md) | `agent-workflows` | `handoff` | `promoted` | Verify concrete handoff claims against visible git state before continuation so the next session trusts repo evidence rather than memory or summary prose alone. |
| [AOA-T-0060](../techniques/agent-workflows/session-opening-ritual-before-work/TECHNIQUE.md) | `agent-workflows` | `handoff` | `promoted` | Start a resumed or handed-off session with one visible read-and-verify ritual before the first mutation so work begins from current state rather than stale assumptions. |
| [AOA-T-0061](../techniques/agent-workflows/cross-repo-resource-map-bootstrap/TECHNIQUE.md) | `agent-workflows` | `handoff` | `promoted` | Bootstrap cross-repo work from one explicit resource map so the next session can see which repos and surfaces matter before deeper continuation begins. |
| [AOA-T-0062](../techniques/agent-workflows/episode-bounded-agent-loop/TECHNIQUE.md) | `agent-workflows` | `handoff` | `promoted` | Break longer work into explicit episodes with checkpoints and continue, stop, or escalate decisions so continuation stays reviewable instead of slipping into open-ended autonomy. |

## `tool-gateway`

One bounded caller surface over multiple upstream tool or MCP endpoints.

Typical domains: `agent-workflows`.
Typical kinds: `composition`.

Counts: `total` 1, `canonical` 0, `promoted` 1.

| technique | domain | kind | status | summary |
|---|---|---|---|---|
| [AOA-T-0065](../techniques/agent-workflows/mcp-gateway-proxy/TECHNIQUE.md) | `agent-workflows` | `composition` | `promoted` | Front multiple configured MCP servers through one bounded gateway proxy so callers use one reviewable tool surface with explicit metadata and sanitization instead of binding directly to each upstream server. |

## `approval-evidence`

Approval-gated mutation and durable work with explicit allow or block evidence.

Typical domains: `agent-workflows`.
Typical kinds: `guardrail`, `handoff`.

Counts: `total` 2, `canonical` 0, `promoted` 2.

| technique | domain | kind | status | summary |
|---|---|---|---|---|
| [AOA-T-0068](../techniques/agent-workflows/fail-closed-evidence-gate/TECHNIQUE.md) | `agent-workflows` | `guardrail` | `promoted` | Stop mutating execution at the boundary unless an explicit allow verdict exists, and emit reviewable evidence for blocked or allowed paths instead of relying on best-effort warnings. |
| [AOA-T-0069](../techniques/agent-workflows/approval-bound-durable-jobs/TECHNIQUE.md) | `agent-workflows` | `handoff` | `promoted` | Keep longer-running work durable across one explicit approval seam so checkpoint, pause, and resume remain reviewable without widening into a scheduler or orchestration platform. |

## `media-ingest`

OCR, field extraction, normalization, dedupe, and semantic bucketing of external media inputs.

Typical domains: `agent-workflows`.
Typical kinds: `ingest`.

Counts: `total` 5, `canonical` 0, `promoted` 5.

| technique | domain | kind | status | summary |
|---|---|---|---|---|
| [AOA-T-0070](../techniques/agent-workflows/two-stage-document-ocr-pipeline/TECHNIQUE.md) | `agent-workflows` | `ingest` | `promoted` | Stage OCR as detect or layout -> recognize -> structured handoff so downstream extraction stays reviewable, interchangeable, and confidence-aware instead of collapsing OCR and field logic into one opaque step. |
| [AOA-T-0071](../techniques/agent-workflows/template-backed-field-extraction-after-ocr/TECHNIQUE.md) | `agent-workflows` | `ingest` | `promoted` | Extract bounded fields after OCR through explicit templates, heuristics, and missing-or-conflict signaling so structured receipt-like data stays reviewable instead of being guessed by one opaque parser. |
| [AOA-T-0072](../techniques/agent-workflows/perceptual-media-dedupe-with-threshold-review/TECHNIQUE.md) | `agent-workflows` | `ingest` | `promoted` | Group near-duplicate media through perceptual similarity and thresholded review buckets so cleanup stays reviewable instead of collapsing into silent deletion or one-threshold dogma. |
| [AOA-T-0073](../techniques/agent-workflows/semantic-media-bucketing-with-vision-plus-ocr/TECHNIQUE.md) | `agent-workflows` | `ingest` | `promoted` | Bucket mixed media through bounded visual semantics plus OCR side text so screenshots, memes, receipts, and other media classes remain reviewable under explicit confidence gates instead of widening into open-ended multimodal automation. |
| [AOA-T-0074](../techniques/agent-workflows/telegram-export-normalization-to-local-store/TECHNIQUE.md) | `agent-workflows` | `ingest` | `promoted` | Normalize Telegram messages and media into a resumable local store with visible provenance so later workflows can inspect, route, or distill the data without collapsing auth, session, or memory doctrine into the storage contract. |

## `donor-harvest`

Harvest reviewed sessions into donor packs, bounded packets, progression deltas, or overlay artifacts without forced promotion.

Typical domains: `agent-workflows`.
Typical kinds: `lift`, `artifact`, `handoff`.

Counts: `total` 4, `canonical` 0, `promoted` 4.

| technique | domain | kind | status | summary |
|---|---|---|---|---|
| [AOA-T-0075](../techniques/agent-workflows/session-donor-harvest/TECHNIQUE.md) | `agent-workflows` | `lift` | `promoted` | Distill a reviewed session artifact into a bounded donor pack of reusable units so candidate practice, workflow, and scenario objects can be evaluated without turning session history into memory or forcing promotion. |
| [AOA-T-0077](../techniques/agent-workflows/harvest-packet-contract/TECHNIQUE.md) | `agent-workflows` | `handoff` | `promoted` | Keep one bounded HARVEST_PACKET contract over a reviewed session so downstream routing, diagnosis, repair, progression, and quest seams can consume explicit packet fields without silently replacing one another. |
| [AOA-T-0084](../techniques/agent-workflows/progression-evidence-lift/TECHNIQUE.md) | `agent-workflows` | `lift` | `promoted` | Lift reviewed session evidence into a bounded multi-axis progression delta with explicit verdicts and small unlock hints so growth stays descriptive and evidence-backed instead of collapsing into one score. |
| [AOA-T-0085](../techniques/agent-workflows/multi-axis-quest-overlay/TECHNIQUE.md) | `agent-workflows` | `artifact` | `promoted` | Add quest-, RPG-, or chronicle-shaped reflection to a bounded multi-axis progression result so route legibility improves without letting flavor overwrite owner truth, proof, or routing authority. |

## `decision-routing`

Owner-layer routing, explicit fork cards, and route risk posture for next-step choice.

Typical domains: `agent-workflows`.
Typical kinds: `assessment`.

Counts: `total` 3, `canonical` 0, `promoted` 3.

| technique | domain | kind | status | summary |
|---|---|---|---|---|
| [AOA-T-0076](../techniques/agent-workflows/owner-layer-triage/TECHNIQUE.md) | `agent-workflows` | `assessment` | `promoted` | Route one bounded reusable unit to one primary owner layer and one rejected nearest-wrong target so practice, workflow, scenario, proof, recall, and role surfaces stay distinct instead of collapsing into generic reuse. |
| [AOA-T-0078](../techniques/agent-workflows/decision-fork-cards/TECHNIQUE.md) | `agent-workflows` | `assessment` | `promoted` | Turn one reviewed session or harvest packet into explicit decision fork cards so materially different next routes stay visible with gains, costs, owner targets, and stop conditions instead of collapsing into one hidden recommendation. |
| [AOA-T-0079](../techniques/agent-workflows/risk-passport-lift/TECHNIQUE.md) | `agent-workflows` | `assessment` | `promoted` | Attach one small risk passport to each explicit next route so difficulty, risk, control mode, delegate tier, and stop-condition posture stay visible without turning branch analysis into hidden routing policy. |

## `diagnosis-repair`

Drift taxonomy, diagnosis packets, repair shaping, and checkpoint-bound self-repair.

Typical domains: `agent-workflows`.
Typical kinds: `assessment`, `recovery`.

Counts: `total` 4, `canonical` 0, `promoted` 4.

| technique | domain | kind | status | summary |
|---|---|---|---|---|
| [AOA-T-0080](../techniques/agent-workflows/session-drift-taxonomy/TECHNIQUE.md) | `agent-workflows` | `assessment` | `promoted` | Classify repeated post-session friction into bounded drift types so diagnosis can say what kind of problem is present before it claims one probable cause, owner hint, or repair shape. |
| [AOA-T-0081](../techniques/agent-workflows/diagnosis-from-reviewed-evidence/TECHNIQUE.md) | `agent-workflows` | `assessment` | `promoted` | Turn reviewed friction evidence into a bounded diagnosis packet that separates symptoms from probable causes, preserves unknowns, and names likely owner hints without mutating anything yet. |
| [AOA-T-0082](../techniques/agent-workflows/repair-shape-from-diagnosis/TECHNIQUE.md) | `agent-workflows` | `recovery` | `promoted` | Turn a reviewed diagnosis packet into the smallest honest repair shape so the next artifact stays bounded, owner-aware, and smaller than a scenario rollout. |
| [AOA-T-0083](../techniques/agent-workflows/checkpoint-bound-self-repair/TECHNIQUE.md) | `agent-workflows` | `recovery` | `promoted` | Keep self-repair behind explicit checkpoint posture with approval, rollback, health checks, iteration limits, and improvement-log visibility so repair stays reviewable instead of feeling like silent self-modification. |

## `automation-governance`

Automation-worthiness, approval sensitivity, seed routing, and promotion-boundary review.

Typical domains: `agent-workflows`.
Typical kinds: `assessment`, `guardrail`.

Counts: `total` 5, `canonical` 0, `promoted` 5.

| technique | domain | kind | status | summary |
|---|---|---|---|---|
| [AOA-T-0086](../techniques/agent-workflows/automation-fit-matrix/TECHNIQUE.md) | `agent-workflows` | `assessment` | `promoted` | Classify one recurring manual route across repeat signal, determinism, proof posture, reversibility, and approval sensitivity so automation desire becomes a bounded verdict rather than vague enthusiasm. |
| [AOA-T-0087](../techniques/agent-workflows/human-loop-to-seed-lift/TECHNIQUE.md) | `agent-workflows` | `assessment` | `promoted` | Route one recurring human loop to the first honest automation-facing landing so seed-ready candidates become bounded skills or playbook seeds while unstable routes stay manual, repair-bound, or deferred. |
| [AOA-T-0088](../techniques/agent-workflows/approval-sensitivity-check/TECHNIQUE.md) | `agent-workflows` | `assessment` | `promoted` | Classify whether an automation candidate crosses approval, rollback, or self-change boundaries so checkpoint-required posture appears before any seed-ready claim becomes credible. |
| [AOA-T-0089](../techniques/agent-workflows/quest-unit-promotion-review/TECHNIQUE.md) | `agent-workflows` | `assessment` | `promoted` | Review one repeated reviewed quest unit and emit one bounded promotion verdict so leaf workflow, route, role, proof, and recall surfaces do not collapse into generic reuse pressure. |
| [AOA-T-0090](../techniques/agent-workflows/nearest-wrong-target-rejection/TECHNIQUE.md) | `agent-workflows` | `guardrail` | `promoted` | Reject the nearest wrong promotion target explicitly so repeated reviewed work does not collapse into the most convenient adjacent owner layer. |

## `owner-truth-closeout`

Ingress or mutation gates, proof-backed closeout, validated mirrors, and publish-readiness against owner truth.

Typical domains: `agent-workflows`, `docs`.
Typical kinds: `guardrail`, `workflow`, `validation`, `distribution`.

Counts: `total` 5, `canonical` 0, `promoted` 5.

| technique | domain | kind | status | summary |
|---|---|---|---|---|
| [AOA-T-0091](../techniques/agent-workflows/workspace-root-ingress-and-mutation-gate/TECHNIQUE.md) | `agent-workflows` | `guardrail` | `promoted` | Enter federated workspaces through one explicit ingress pass and gate risky mutation through one explicit guard pass so session posture stays reviewable instead of hiding in operator memory. |
| [AOA-T-0092](../techniques/agent-workflows/audit-to-closeout-proof-loop/TECHNIQUE.md) | `agent-workflows` | `workflow` | `promoted` | Turn a reviewed audit finding set into a live-confirmed, proof-backed closeout loop so remediation claims rest on named evidence instead of audit wording alone. |
| [AOA-T-0095](../techniques/agent-workflows/github-only-owner-endcap-with-reality-sync/TECHNIQUE.md) | `agent-workflows` | `workflow` | `promoted` | Close a remote-only owner surface through GitHub-native issue and PR flow, then rebind staging and reality checks to the merged owner anchors so seed-garden truth does not outlive the landing. |
| [AOA-T-0096](../techniques/agent-workflows/pinned-validation-matrix-before-generated-publish/TECHNIQUE.md) | `agent-workflows` | `validation` | `promoted` | Rebuild generated outputs against the same workflow-pinned sibling refs that CI will validate before publish so local green does not overstate merge-readiness. |
| [AOA-T-0094](../techniques/docs/canonical-owner-with-validated-mirror/TECHNIQUE.md) | `docs` | `distribution` | `promoted` | Keep one canonical cross-repo contract owner and allow local mirrors only when explicit parity validation keeps owner metadata and vocabulary exactly aligned. |

## `antifragility-recovery`

Degraded continuation, regrounding, and receipt-first failure analysis.

Typical domains: `system-recovery`, `validation-patterns`.
Typical kinds: `recovery`, `validation`.

Counts: `total` 3, `canonical` 0, `promoted` 3.

| technique | domain | kind | status | summary |
|---|---|---|---|---|
| [AOA-T-0097](../techniques/system-recovery/degrade-reground-recover/TECHNIQUE.md) | `system-recovery` | `recovery` | `promoted` | Continue safely in a bounded degraded mode, reground against stronger sources, and recover later through explicit source-owned evidence instead of hidden repair theater. |
| [AOA-T-0099](../techniques/system-recovery/isolated-service-stop-on-shared-substrate/TECHNIQUE.md) | `system-recovery` | `recovery` | `promoted` | Stop one bounded service while keeping shared substrate services alive, then verify both target absence and substrate continuity so closeout does not widen into unnecessary teardown. |
| [AOA-T-0098](../techniques/validation-patterns/receipt-first-failure-analysis/TECHNIQUE.md) | `validation-patterns` | `validation` | `promoted` | Start failure review from source-owned receipts, separate facts from hypotheses, and tie any recovery change to explicit evidence rather than folklore or dashboard mythology. |

## Boundaries

- This report is scout-only, non-authoritative, and weaker than bundle frontmatter. It must not be treated as schema truth, frontmatter truth, or automatic remap authority.
- Family suggestions may inform later clustering work, but bundle frontmatter remains the stronger source of meaning.
- Do not use this report to add automatic remaps or new required metadata in this wave.
