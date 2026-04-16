# Technique Kinds

This file is generated from `../generated/technique_catalog.json` plus the repo-owned `kind` registry.
Do not edit it by hand; run `python scripts/build_kind_manifest.py`.

Use this surface when `domain` already narrowed the owner layer and you need the bounded second cut that answers what primary reusable practice a technique is.

This surface is kind-first, not promotion-first. It keeps `kind` singular, repo-owned, and subordinate to authored bundle meaning.

See also:
- [Technique Kind Guide](TECHNIQUE_KIND_GUIDE.md)
- [Technique Selection](TECHNIQUE_SELECTION.md)
- [Technique Kinds Seed](TECHNIQUE_KINDS_SEED.md)
- [Technique Kind Handoff Pack](TECHNIQUE_KIND_HANDOFF_PACK.md)
- [Full kind manifest](../generated/technique_kind_manifest.json)
- [Min kind manifest](../generated/technique_kind_manifest.min.json)
- [Documentation Map](README.md)

## Kind Scope

| kind | summary | total | canonical | promoted |
|---|---|---|---|---|
| `workflow` | Ordered procedure for doing bounded work or coordinating state change. | `11` | `4` | `7` |
| `guardrail` | Boundary, gate, or containment contract that prevents unsafe mutation, wrong routing, or hidden strictness. | `11` | `4` | `7` |
| `validation` | Check, test, smoke, integrity, readiness, or proof pattern that emits or consumes explicit evidence. | `10` | `4` | `6` |
| `composition` | Deterministic assembly of fragments, profiles, rules, or tool surfaces into one effective result. | `7` | `2` | `5` |
| `distribution` | Fan-out, mirroring, parity, or version alignment of canonical truth across multiple surfaces. | `4` | `1` | `3` |
| `artifact` | Durable artifact shape, storage, capture, snapshot, transcript, note, spec, or index contract. | `14` | `6` | `8` |
| `lift` | Bounded derivation of a secondary surface from an authoritative source while keeping the source authoritative. | `11` | `4` | `7` |
| `discovery` | Editorial or query-oriented surfacing of capabilities or resources without taking ownership of their meaning. | `2` | `0` | `2` |
| `handoff` | Checkpoint, packet, mailbox, receipt, continuation, or resume seam across runs, agents, approvals, or episodes. | `11` | `0` | `11` |
| `ingest` | Normalization of raw external inputs into reviewable structured intermediates. | `5` | `0` | `5` |
| `assessment` | Classification, diagnosis, route comparison, or decision-support pattern that stays descriptive rather than mutating. | `9` | `0` | `9` |
| `recovery` | Degraded continuation, regrounding, repair, rollback, or explicit recovery posture. | `5` | `0` | `5` |

## `workflow`

Ordered procedure for doing bounded work or coordinating state change.

Choose this when:
- the main promise is how to do the work step by step
- state change or execution choreography is the center of gravity

Do not use this when:
- the primary value is blocking unsafe actions
- the technique is mainly about durable artifact shape, not the work loop

Counts: `total` 11, `canonical` 4, `promoted` 7.

| domain | entries |
|---|---|
| `agent-workflows` | `11` |
| `docs` | `0` |
| `evaluation` | `0` |
| `system-recovery` | `0` |
| `validation-patterns` | `0` |
| `history` | `0` |

| technique | domain | status | summary | source |
|---|---|---|---|---|
| [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) | `agent-workflows` | `canonical` | Safe workflow for agent-driven changes using explicit planning, scoped diffs, explicit validation, and concise reporting. | [TECHNIQUE.md](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) |
| [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) | `agent-workflows` | `canonical` | Safe workflow that normalizes intent into a traceable plan, validates it with dry-run, and enforces contract checks before any real execution path exists. | [TECHNIQUE.md](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) |
| [AOA-T-0014](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) | `agent-workflows` | `canonical` | Implement a bounded behavior slice through test-first discipline, minimal implementation, and explicit refactor limits. | [TECHNIQUE.md](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) |
| [AOA-T-0023](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) | `agent-workflows` | `canonical` | Keep shell-side agent work mostly stateless and bounded to one confirmed step per invocation so runs stay composable, reviewable, and low-memory by default. | [TECHNIQUE.md](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) |
| [AOA-T-0038](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) | `agent-workflows` | `promoted` | Start and stop a bounded local service stack through one explicit lifecycle entrypoint so prerequisite checks, visible runtime status, and clean shutdown stay reviewable without widening into generic launcher or platform doctrine. | [TECHNIQUE.md](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) |
| [AOA-T-0049](../techniques/agent-workflows/dependency-aware-task-graph/TECHNIQUE.md) | `agent-workflows` | `promoted` | Model multi-step coding work as explicit dependency nodes and edges so blocked state and ready work stay reviewable instead of hiding in chat memory. | [TECHNIQUE.md](../techniques/agent-workflows/dependency-aware-task-graph/TECHNIQUE.md) |
| [AOA-T-0050](../techniques/agent-workflows/ready-work-from-blocker-graph/TECHNIQUE.md) | `agent-workflows` | `promoted` | Derive the next bounded work queue from blocker-free graph state so operators choose from what is truly ready instead of narrating readiness from memory. | [TECHNIQUE.md](../techniques/agent-workflows/ready-work-from-blocker-graph/TECHNIQUE.md) |
| [AOA-T-0051](../techniques/agent-workflows/commit-triggered-background-review/TECHNIQUE.md) | `agent-workflows` | `promoted` | Trigger a bounded background review after a commit so findings survive as inspectable artifacts without widening into autonomous merge, rewrite, or CI governance. | [TECHNIQUE.md](../techniques/agent-workflows/commit-triggered-background-review/TECHNIQUE.md) |
| [AOA-T-0055](../techniques/agent-workflows/requirements-design-tasks-ladder/TECHNIQUE.md) | `agent-workflows` | `promoted` | Separate requirements, design, and task slices so implementation planning stays reviewable without importing a full spec-driven methodology stack. | [TECHNIQUE.md](../techniques/agent-workflows/requirements-design-tasks-ladder/TECHNIQUE.md) |
| [AOA-T-0092](../techniques/agent-workflows/audit-to-closeout-proof-loop/TECHNIQUE.md) | `agent-workflows` | `promoted` | Turn a reviewed audit finding set into a live-confirmed, proof-backed closeout loop so remediation claims rest on named evidence instead of audit wording alone. | [TECHNIQUE.md](../techniques/agent-workflows/audit-to-closeout-proof-loop/TECHNIQUE.md) |
| [AOA-T-0095](../techniques/agent-workflows/github-only-owner-endcap-with-reality-sync/TECHNIQUE.md) | `agent-workflows` | `promoted` | Close a remote-only owner surface through GitHub-native issue and PR flow, then rebind staging and reality checks to the merged owner anchors so seed-garden truth does not outlive the landing. | [TECHNIQUE.md](../techniques/agent-workflows/github-only-owner-endcap-with-reality-sync/TECHNIQUE.md) |

## `guardrail`

Boundary, gate, or containment contract that prevents unsafe mutation, wrong routing, or hidden strictness.

Choose this when:
- the main promise is when to stop, gate, reject, or require approval
- the technique narrows action through explicit policy seams or fail-closed posture

Do not use this when:
- the technique mostly verifies correctness after the fact
- the primary value is assembling or publishing artifacts

Counts: `total` 11, `canonical` 4, `promoted` 7.

| domain | entries |
|---|---|
| `agent-workflows` | `6` |
| `docs` | `3` |
| `evaluation` | `2` |
| `system-recovery` | `0` |
| `validation-patterns` | `0` |
| `history` | `0` |

| technique | domain | status | summary | source |
|---|---|---|---|---|
| [AOA-T-0028](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) | `agent-workflows` | `canonical` | Require one explicit confirmation seam before a read or plan flow crosses into a mutating action so the action stays reviewable without widening into a multi-step autonomous loop. | [TECHNIQUE.md](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) |
| [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) | `agent-workflows` | `promoted` | Checklist for safely adding a new intent type to an intent-plan-dry-run chain without contract drift. | [TECHNIQUE.md](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) |
| [AOA-T-0068](../techniques/agent-workflows/fail-closed-evidence-gate/TECHNIQUE.md) | `agent-workflows` | `promoted` | Stop mutating execution at the boundary unless an explicit allow verdict exists, and emit reviewable evidence for blocked or allowed paths instead of relying on best-effort warnings. | [TECHNIQUE.md](../techniques/agent-workflows/fail-closed-evidence-gate/TECHNIQUE.md) |
| [AOA-T-0090](../techniques/agent-workflows/nearest-wrong-target-rejection/TECHNIQUE.md) | `agent-workflows` | `promoted` | Reject the nearest wrong promotion target explicitly so repeated reviewed work does not collapse into the most convenient adjacent owner layer. | [TECHNIQUE.md](../techniques/agent-workflows/nearest-wrong-target-rejection/TECHNIQUE.md) |
| [AOA-T-0091](../techniques/agent-workflows/workspace-root-ingress-and-mutation-gate/TECHNIQUE.md) | `agent-workflows` | `promoted` | Enter federated workspaces through one explicit ingress pass and gate risky mutation through one explicit guard pass so session posture stays reviewable instead of hiding in operator memory. | [TECHNIQUE.md](../techniques/agent-workflows/workspace-root-ingress-and-mutation-gate/TECHNIQUE.md) |
| [AOA-T-0093](../techniques/agent-workflows/recommendation-truth-vs-host-actionability/TECHNIQUE.md) | `agent-workflows` | `promoted` | Keep router recommendation truth separate from host actionability so non-executable recommendations stay visible, canonical install roots stay authoritative, and runnable actions do not masquerade as merely relevant advice. | [TECHNIQUE.md](../techniques/agent-workflows/recommendation-truth-vs-host-actionability/TECHNIQUE.md) |
| [AOA-T-0034](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md) | `docs` | `canonical` | Turn sensitive technical material into a shareable artifact by removing, redacting, or generalizing details while preserving the lesson and staying distinct from approval gating or execution planning. | [TECHNIQUE.md](../techniques/docs/public-safe-artifact-sanitization/TECHNIQUE.md) |
| [AOA-T-0040](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md) | `docs` | `promoted` | Separate reusable skill meaning from user-facing command invocation so shared capability stays portable without collapsing into slash-command syntax or command-specific workflow policy. | [TECHNIQUE.md](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md) |
| [AOA-T-0043](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md) | `docs` | `promoted` | Mark primary versus supporting source inputs explicitly when bridging multiple source surfaces so downstream readers and synthesis keep provenance priority visible without turning the bridge into graph semantics or ranking doctrine. | [TECHNIQUE.md](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md) |
| [AOA-T-0007](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) | `evaluation` | `canonical` | Staged pattern for promoting an observed validation signal into strict enforcement without losing diagnostics or widening the fail surface too early. | [TECHNIQUE.md](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) |
| [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) | `evaluation` | `canonical` | Distinguish strict required sources from tolerant optional sources so operator-facing summary surfaces remain useful without hiding true hard failures. | [TECHNIQUE.md](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) |

## `validation`

Check, test, smoke, integrity, readiness, or proof pattern that emits or consumes explicit evidence.

Choose this when:
- the technique produces or evaluates proof, health, integrity, or contract-verification signals
- a verdict or evidence surface is the main reusable output

Do not use this when:
- the technique mainly classifies options or diagnoses routes without claiming proof
- the primary value is a durable artifact layout or history container

Counts: `total` 10, `canonical` 4, `promoted` 6.

| domain | entries |
|---|---|
| `agent-workflows` | `1` |
| `docs` | `0` |
| `evaluation` | `8` |
| `system-recovery` | `0` |
| `validation-patterns` | `1` |
| `history` | `0` |

| technique | domain | status | summary | source |
|---|---|---|---|---|
| [AOA-T-0096](../techniques/agent-workflows/pinned-validation-matrix-before-generated-publish/TECHNIQUE.md) | `agent-workflows` | `promoted` | Rebuild generated outputs against the same workflow-pinned sibling refs that CI will validate before publish so local green does not overstate merge-readiness. | [TECHNIQUE.md](../techniques/agent-workflows/pinned-validation-matrix-before-generated-publish/TECHNIQUE.md) |
| [AOA-T-0003](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) | `evaluation` | `canonical` | Runnable smoke pattern where each smoke path emits a machine-readable summary that becomes the primary validation contract. | [TECHNIQUE.md](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) |
| [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) | `evaluation` | `canonical` | Read-only integrity verdict that checks telemetry and summary-layout invariants across latest published summaries without widening the hard fail surface. | [TECHNIQUE.md](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) |
| [AOA-T-0015](../techniques/evaluation/contract-test-design/TECHNIQUE.md) | `evaluation` | `canonical` | Make a boundary explicit by defining expected inputs, outputs, and verification around the contract rather than around hidden internals. | [TECHNIQUE.md](../techniques/evaluation/contract-test-design/TECHNIQUE.md) |
| [AOA-T-0017](../techniques/evaluation/property-invariants/TECHNIQUE.md) | `evaluation` | `canonical` | Express stable system or domain truths as invariant-oriented tests or checks so broad behavior is constrained beyond a small handpicked example set. | [TECHNIQUE.md](../techniques/evaluation/property-invariants/TECHNIQUE.md) |
| [AOA-T-0032](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md) | `evaluation` | `promoted` | Emit CI-facing reports for context composition, source coverage, token-estimate drift, and related composition checks without turning the report surface into the composition technique itself. | [TECHNIQUE.md](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md) |
| [AOA-T-0037](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md) | `evaluation` | `promoted` | Run selector-aware host-readiness checks before startup so environment drift becomes visible for the chosen runtime without widening into generic monitoring or lifecycle control. | [TECHNIQUE.md](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md) |
| [AOA-T-0039](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) | `evaluation` | `promoted` | Benchmark one stable baseline profile first, then compare additive profiles against the same measurement surface and artifact shape so richer profiles stay additive and off the default path. | [TECHNIQUE.md](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) |
| [AOA-T-0042](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md) | `evaluation` | `promoted` | Check upstream-owned skill sources for availability and manifest-readiness before surfacing them as selectable inputs so broken entries stay visible and reviewable without widening into generic monitoring, registry governance, or security doctrine. | [TECHNIQUE.md](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md) |
| [AOA-T-0098](../techniques/validation-patterns/receipt-first-failure-analysis/TECHNIQUE.md) | `validation-patterns` | `promoted` | Start failure review from source-owned receipts, separate facts from hypotheses, and tie any recovery change to explicit evidence rather than folklore or dashboard mythology. | [TECHNIQUE.md](../techniques/validation-patterns/receipt-first-failure-analysis/TECHNIQUE.md) |

## `composition`

Deterministic assembly of fragments, profiles, rules, or tool surfaces into one effective result.

Choose this when:
- the technique builds one effective view from smaller pieces
- ordering, precedence, or assembly logic is the main contract

Do not use this when:
- one source is being fanned out to multiple targets
- the technique is mostly a work loop or approval boundary

Counts: `total` 7, `canonical` 2, `promoted` 5.

| domain | entries |
|---|---|
| `agent-workflows` | `3` |
| `docs` | `4` |
| `evaluation` | `0` |
| `system-recovery` | `0` |
| `validation-patterns` | `0` |
| `history` | `0` |

| technique | domain | status | summary | source |
|---|---|---|---|---|
| [AOA-T-0031](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) | `agent-workflows` | `canonical` | Make agent runs composable as shell-side one-shot tools through explicit stdin, stdout, files, and pipes without widening into generic shell advice or autonomous loops. | [TECHNIQUE.md](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md) |
| [AOA-T-0036](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md) | `agent-workflows` | `promoted` | Render the actual composed runtime truth before startup so operators review the effective service and config view instead of relying only on declared profiles. | [TECHNIQUE.md](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md) |
| [AOA-T-0065](../techniques/agent-workflows/mcp-gateway-proxy/TECHNIQUE.md) | `agent-workflows` | `promoted` | Front multiple configured MCP servers through one bounded gateway proxy so callers use one reviewable tool surface with explicit metadata and sanitization instead of binding directly to each upstream server. | [TECHNIQUE.md](../techniques/agent-workflows/mcp-gateway-proxy/TECHNIQUE.md) |
| [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) | `docs` | `canonical` | Compose agent context from smaller fragments into a stable generated artifact with deterministic ordering and source traceability. | [TECHNIQUE.md](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) |
| [AOA-T-0029](../techniques/docs/nested-rule-loading/TECHNIQUE.md) | `docs` | `promoted` | Load hierarchical rule layers with explicit precedence so nested additions stay subordinate to one canonical source of ownership. | [TECHNIQUE.md](../techniques/docs/nested-rule-loading/TECHNIQUE.md) |
| [AOA-T-0030](../techniques/docs/fragmented-agent-context/TECHNIQUE.md) | `docs` | `promoted` | Keep agent context in bounded fragments before deterministic assembly so modular authoring stays reviewable without collapsing into the final generated artifact. | [TECHNIQUE.md](../techniques/docs/fragmented-agent-context/TECHNIQUE.md) |
| [AOA-T-0035](../techniques/docs/profile-preset-composition/TECHNIQUE.md) | `docs` | `promoted` | Compose small reusable profiles into named presets so runtime posture stays reviewable without flattening composition into one opaque config or launcher doctrine. | [TECHNIQUE.md](../techniques/docs/profile-preset-composition/TECHNIQUE.md) |

## `distribution`

Fan-out, mirroring, parity, or version alignment of canonical truth across multiple surfaces.

Choose this when:
- one authoritative source must reach multiple targets without drift
- mirroring, propagation, or parity validation is the main reusable contract

Do not use this when:
- the technique is mainly composing inputs into one result
- the technique mostly defines the durable artifact itself

Counts: `total` 4, `canonical` 1, `promoted` 3.

| domain | entries |
|---|---|
| `agent-workflows` | `0` |
| `docs` | `4` |
| `evaluation` | `0` |
| `system-recovery` | `0` |
| `validation-patterns` | `0` |
| `history` | `0` |

| technique | domain | status | summary | source |
|---|---|---|---|---|
| [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) | `docs` | `canonical` | Keep one canonical rule source and distribute it to multiple agent-facing instruction surfaces without turning each target into a hand-maintained source of truth. | [TECHNIQUE.md](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) |
| [AOA-T-0024](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) | `docs` | `promoted` | Mirror upstream-owned content into a curated local collection through an explicit source manifest and preserved provenance so the local copy stays reviewable without pretending to be the canonical source. | [TECHNIQUE.md](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) |
| [AOA-T-0027](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) | `docs` | `promoted` | Keep one canonical skill or rule source and propagate it to multiple agent-facing targets without turning each target into a hand-maintained source of truth. | [TECHNIQUE.md](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) |
| [AOA-T-0094](../techniques/docs/canonical-owner-with-validated-mirror/TECHNIQUE.md) | `docs` | `promoted` | Keep one canonical cross-repo contract owner and allow local mirrors only when explicit parity validation keeps owner metadata and vocabulary exactly aligned. | [TECHNIQUE.md](../techniques/docs/canonical-owner-with-validated-mirror/TECHNIQUE.md) |

## `artifact`

Durable artifact shape, storage, capture, snapshot, transcript, note, spec, or index contract.

Choose this when:
- the technique primarily defines what durable artifact should exist and how it stays legible
- layout, storage, snapshot, indexing, replay, or rationale shape is central

Do not use this when:
- the technique mainly derives a secondary lookup surface from another authoritative source
- the main promise is stepwise execution or approval gating

Counts: `total` 14, `canonical` 6, `promoted` 8.

| domain | entries |
|---|---|
| `agent-workflows` | `1` |
| `docs` | `6` |
| `evaluation` | `1` |
| `system-recovery` | `0` |
| `validation-patterns` | `0` |
| `history` | `6` |

| technique | domain | status | summary | source |
|---|---|---|---|---|
| [AOA-T-0085](../techniques/agent-workflows/multi-axis-quest-overlay/TECHNIQUE.md) | `agent-workflows` | `promoted` | Add quest-, RPG-, or chronicle-shaped reflection to a bounded multi-axis progression result so route legibility improves without letting flavor overwrite owner truth, proof, or routing authority. | [TECHNIQUE.md](../techniques/agent-workflows/multi-axis-quest-overlay/TECHNIQUE.md) |
| [AOA-T-0002](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) | `docs` | `canonical` | Repository document role separation pattern that keeps status, plans, history, decisions, and run instructions in distinct canonical homes. | [TECHNIQUE.md](../techniques/docs/source-of-truth-layout/TECHNIQUE.md) |
| [AOA-T-0009](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) | `docs` | `canonical` | Keep top-level status documents short and link-driven, while routing detailed execution state and history to their canonical homes. | [TECHNIQUE.md](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md) |
| [AOA-T-0016](../techniques/docs/bounded-context-map/TECHNIQUE.md) | `docs` | `canonical` | Reduce semantic drift by naming bounded contexts, separating responsibilities, and making handoff interfaces visible for docs and scoping work. | [TECHNIQUE.md](../techniques/docs/bounded-context-map/TECHNIQUE.md) |
| [AOA-T-0025](../techniques/docs/capability-spec-versioning/TECHNIQUE.md) | `docs` | `promoted` | Keep agent-facing capability contracts in a versioned, reviewable spec so capability changes stay explicit and reusable without turning the spec into routing or registry policy. | [TECHNIQUE.md](../techniques/docs/capability-spec-versioning/TECHNIQUE.md) |
| [AOA-T-0033](../techniques/docs/decision-rationale-recording/TECHNIQUE.md) | `docs` | `promoted` | Keep one meaningful decision in a reviewable note with context, options, rationale, and consequences while staying out of source-of-truth governance and architecture taxonomy. | [TECHNIQUE.md](../techniques/docs/decision-rationale-recording/TECHNIQUE.md) |
| [AOA-T-0063](../techniques/docs/versioned-agent-registry-contract/TECHNIQUE.md) | `docs` | `promoted` | Keep registry-facing capability entries reviewable as named versioned records with explicit references and metadata so publication stays bounded without widening into discovery policy or registry product doctrine. | [TECHNIQUE.md](../techniques/docs/versioned-agent-registry-contract/TECHNIQUE.md) |
| [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) | `evaluation` | `canonical` | Dual-write summary pattern that keeps a stable latest alias, preserves nested history, and prevents double-count accumulation. | [TECHNIQUE.md](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) |
| [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) | `history` | `canonical` | Package already-saved AI session transcripts as readable, versionable Markdown artifacts so review, handoff, and selective sharing stay possible without reopening capture semantics or turning transcript history into memory or instruction authority. | [TECHNIQUE.md](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) |
| [AOA-T-0053](../techniques/history/local-first-session-index/TECHNIQUE.md) | `history` | `canonical` | Build a local searchable index over already-saved session artifacts so teams can browse or query saved history without reopening capture semantics or turning the index into memory or dashboard doctrine. | [TECHNIQUE.md](../techniques/history/local-first-session-index/TECHNIQUE.md) |
| [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) | `history` | `promoted` | Capture AI coding sessions as versioned repo artifacts so project history stays searchable, reviewable, and reusable without turning session logs into memory or instruction policy. | [TECHNIQUE.md](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) |
| [AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) | `history` | `promoted` | Preserve a bounded witness trace as a reviewable artifact with step visibility, state-delta notes, and human-readable summary so a nontrivial run can be inspected before any writeback or promotion without creating a new memory-object kind. | [TECHNIQUE.md](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) |
| [AOA-T-0066](../techniques/history/transcript-replay-artifact/TECHNIQUE.md) | `history` | `promoted` | Turn already-saved session history into a replayable artifact so reviewers can inspect message flow and timeline without reopening capture semantics or widening into hosted replay-platform doctrine. | [TECHNIQUE.md](../techniques/history/transcript-replay-artifact/TECHNIQUE.md) |
| [AOA-T-0067](../techniques/history/transcript-linked-code-lineage/TECHNIQUE.md) | `history` | `promoted` | Link code history back to saved session evidence so reviewers can reopen the originating transcript or rationale without widening the bundle into generic repo analytics or memory doctrine. | [TECHNIQUE.md](../techniques/history/transcript-linked-code-lineage/TECHNIQUE.md) |

## `lift`

Bounded derivation of a secondary surface from an authoritative source while keeping the source authoritative.

Choose this when:
- the technique turns source-owned artifacts into derived manifests, packets, overlays, or review surfaces
- the derived output must stay weaker than the source

Do not use this when:
- the artifact being defined is itself the primary source of truth
- the technique is mainly about raw input ingestion from external sources

Counts: `total` 11, `canonical` 4, `promoted` 7.

| domain | entries |
|---|---|
| `agent-workflows` | `2` |
| `docs` | `8` |
| `evaluation` | `1` |
| `system-recovery` | `0` |
| `validation-patterns` | `0` |
| `history` | `0` |

| technique | domain | status | summary | source |
|---|---|---|---|---|
| [AOA-T-0075](../techniques/agent-workflows/session-donor-harvest/TECHNIQUE.md) | `agent-workflows` | `promoted` | Distill a reviewed session artifact into a bounded donor pack of reusable units so candidate practice, workflow, and scenario objects can be evaluated without turning session history into memory or forcing promotion. | [TECHNIQUE.md](../techniques/agent-workflows/session-donor-harvest/TECHNIQUE.md) |
| [AOA-T-0084](../techniques/agent-workflows/progression-evidence-lift/TECHNIQUE.md) | `agent-workflows` | `promoted` | Lift reviewed session evidence into a bounded multi-axis progression delta with explicit verdicts and small unlock hints so growth stays descriptive and evidence-backed instead of collapsing into one score. | [TECHNIQUE.md](../techniques/agent-workflows/progression-evidence-lift/TECHNIQUE.md) |
| [AOA-T-0018](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) | `docs` | `canonical` | Lift stable technique markdown sections into derived section-level units while keeping the bundle markdown authoritative. | [TECHNIQUE.md](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) |
| [AOA-T-0019](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) | `docs` | `canonical` | Treat bounded frontmatter and derived catalog outputs as a metadata spine for bundle routing without replacing markdown meaning or growing schema past current needs. | [TECHNIQUE.md](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) |
| [AOA-T-0021](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) | `docs` | `canonical` | Lift small typed direct relations into bounded edge hints for derived consumers without turning them into graph semantics. | [TECHNIQUE.md](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) |
| [AOA-T-0020](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) | `docs` | `promoted` | Use typed evidence note kinds and note paths as bounded provenance handles in derived manifests without flattening them into a note graph. | [TECHNIQUE.md](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) |
| [AOA-T-0022](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) | `docs` | `promoted` | Lift richer `Risks` language into bounded caution-oriented lookup and reuse without turning caution into metadata, scoring, or generated policy. | [TECHNIQUE.md](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) |
| [AOA-T-0046](../techniques/docs/repo-doc-surface-lift/TECHNIQUE.md) | `docs` | `promoted` | Lift one bounded set of authoritative repo docs and status files into derived routing knowledge without replacing the authored docs or widening into a docs taxonomy. | [TECHNIQUE.md](../techniques/docs/repo-doc-surface-lift/TECHNIQUE.md) |
| [AOA-T-0047](../techniques/docs/github-review-template-lift/TECHNIQUE.md) | `docs` | `promoted` | Lift authored GitHub issue and pull-request review templates into derived intake knowledge without turning templates into workflow automation or policy scoring. | [TECHNIQUE.md](../techniques/docs/github-review-template-lift/TECHNIQUE.md) |
| [AOA-T-0048](../techniques/docs/semantic-review-surface-lift/TECHNIQUE.md) | `docs` | `promoted` | Lift authored semantic-review docs into derived boundary-review knowledge without creating automatic semantic verdicts. | [TECHNIQUE.md](../techniques/docs/semantic-review-surface-lift/TECHNIQUE.md) |
| [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) | `evaluation` | `canonical` | Read-only aggregation pattern that turns latest published summaries into a bounded remediation snapshot without replaying history or changing runtime behavior. | [TECHNIQUE.md](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) |

## `discovery`

Editorial or query-oriented surfacing of capabilities or resources without taking ownership of their meaning.

Choose this when:
- selection, lookup, or curation is the main behavior
- the technique helps a caller discover what exists without becoming registry product doctrine

Do not use this when:
- the technique mainly versions or stores the authoritative contract
- the main value is safety gating or route diagnosis

Counts: `total` 2, `canonical` 0, `promoted` 2.

| domain | entries |
|---|---|
| `agent-workflows` | `0` |
| `docs` | `2` |
| `evaluation` | `0` |
| `system-recovery` | `0` |
| `validation-patterns` | `0` |
| `history` | `0` |

| technique | domain | status | summary | source |
|---|---|---|---|---|
| [AOA-T-0041](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) | `docs` | `promoted` | Curate a local discoverability layer over upstream-owned skill sources so selection stays editorial and reviewable without pretending the catalog owns sync, capability meaning, or registry policy. | [TECHNIQUE.md](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) |
| [AOA-T-0064](../techniques/docs/capability-discovery/TECHNIQUE.md) | `docs` | `promoted` | Keep capability lookup reviewable as explicit bounded queries over published registry entries so discovery stays separate from ranking, marketplace curation, trust policy, and registry product doctrine. | [TECHNIQUE.md](../techniques/docs/capability-discovery/TECHNIQUE.md) |

## `handoff`

Checkpoint, packet, mailbox, receipt, continuation, or resume seam across runs, agents, approvals, or episodes.

Choose this when:
- transfer and continuation are the main reusable seam
- the technique keeps work durable or resumable across bounded context loss

Do not use this when:
- the technique is mainly the work loop itself
- the technique only stores history without a transfer or continuation seam

Counts: `total` 11, `canonical` 0, `promoted` 11.

| domain | entries |
|---|---|
| `agent-workflows` | `11` |
| `docs` | `0` |
| `evaluation` | `0` |
| `system-recovery` | `0` |
| `validation-patterns` | `0` |
| `history` | `0` |

| technique | domain | status | summary | source |
|---|---|---|---|---|
| [AOA-T-0052](../techniques/agent-workflows/review-findings-compaction/TECHNIQUE.md) | `agent-workflows` | `promoted` | Compact and revalidate review findings against current code so repeated or stale findings do not overwhelm the current review surface. | [TECHNIQUE.md](../techniques/agent-workflows/review-findings-compaction/TECHNIQUE.md) |
| [AOA-T-0054](../techniques/agent-workflows/compaction-resilient-skill-loading/TECHNIQUE.md) | `agent-workflows` | `promoted` | Re-seed skill availability after context compaction so agents can reload needed skills from canonical sources without widening into full context reconstruction or prompt stuffing. | [TECHNIQUE.md](../techniques/agent-workflows/compaction-resilient-skill-loading/TECHNIQUE.md) |
| [AOA-T-0056](../techniques/agent-workflows/channelized-agent-mailbox/TECHNIQUE.md) | `agent-workflows` | `promoted` | Keep agent communication inside durable named channels with ordered replay and explicit acknowledgment so coordination survives session gaps without widening into a full messaging platform or handoff-governance stack. | [TECHNIQUE.md](../techniques/agent-workflows/channelized-agent-mailbox/TECHNIQUE.md) |
| [AOA-T-0057](../techniques/agent-workflows/structured-handoff-before-compaction/TECHNIQUE.md) | `agent-workflows` | `promoted` | Write one structured handoff artifact before compaction or session rollover so the next session can resume from explicit state instead of hidden memory or transcript replay. | [TECHNIQUE.md](../techniques/agent-workflows/structured-handoff-before-compaction/TECHNIQUE.md) |
| [AOA-T-0058](../techniques/agent-workflows/receipt-confirmed-handoff-packet/TECHNIQUE.md) | `agent-workflows` | `promoted` | Require an explicit receipt state for a handoff packet before the receiving side continues so ownership transfer stays reviewable instead of being inferred from delivery or silence. | [TECHNIQUE.md](../techniques/agent-workflows/receipt-confirmed-handoff-packet/TECHNIQUE.md) |
| [AOA-T-0059](../techniques/agent-workflows/git-verified-handoff-claims/TECHNIQUE.md) | `agent-workflows` | `promoted` | Verify concrete handoff claims against visible git state before continuation so the next session trusts repo evidence rather than memory or summary prose alone. | [TECHNIQUE.md](../techniques/agent-workflows/git-verified-handoff-claims/TECHNIQUE.md) |
| [AOA-T-0060](../techniques/agent-workflows/session-opening-ritual-before-work/TECHNIQUE.md) | `agent-workflows` | `promoted` | Start a resumed or handed-off session with one visible read-and-verify ritual before the first mutation so work begins from current state rather than stale assumptions. | [TECHNIQUE.md](../techniques/agent-workflows/session-opening-ritual-before-work/TECHNIQUE.md) |
| [AOA-T-0061](../techniques/agent-workflows/cross-repo-resource-map-bootstrap/TECHNIQUE.md) | `agent-workflows` | `promoted` | Bootstrap cross-repo work from one explicit resource map so the next session can see which repos and surfaces matter before deeper continuation begins. | [TECHNIQUE.md](../techniques/agent-workflows/cross-repo-resource-map-bootstrap/TECHNIQUE.md) |
| [AOA-T-0062](../techniques/agent-workflows/episode-bounded-agent-loop/TECHNIQUE.md) | `agent-workflows` | `promoted` | Break longer work into explicit episodes with checkpoints and continue, stop, or escalate decisions so continuation stays reviewable instead of slipping into open-ended autonomy. | [TECHNIQUE.md](../techniques/agent-workflows/episode-bounded-agent-loop/TECHNIQUE.md) |
| [AOA-T-0069](../techniques/agent-workflows/approval-bound-durable-jobs/TECHNIQUE.md) | `agent-workflows` | `promoted` | Keep longer-running work durable across one explicit approval seam so checkpoint, pause, and resume remain reviewable without widening into a scheduler or orchestration platform. | [TECHNIQUE.md](../techniques/agent-workflows/approval-bound-durable-jobs/TECHNIQUE.md) |
| [AOA-T-0077](../techniques/agent-workflows/harvest-packet-contract/TECHNIQUE.md) | `agent-workflows` | `promoted` | Keep one bounded HARVEST_PACKET contract over a reviewed session so downstream routing, diagnosis, repair, progression, and quest seams can consume explicit packet fields without silently replacing one another. | [TECHNIQUE.md](../techniques/agent-workflows/harvest-packet-contract/TECHNIQUE.md) |

## `ingest`

Normalization of raw external inputs into reviewable structured intermediates.

Choose this when:
- the source begins as raw documents, media, exports, or OCR output
- normalization, extraction, dedupe, or bucketing is the main contract

Do not use this when:
- the technique derives secondary surfaces from already authoritative repo-owned artifacts
- the main promise is downstream diagnosis or approval policy

Counts: `total` 5, `canonical` 0, `promoted` 5.

| domain | entries |
|---|---|
| `agent-workflows` | `5` |
| `docs` | `0` |
| `evaluation` | `0` |
| `system-recovery` | `0` |
| `validation-patterns` | `0` |
| `history` | `0` |

| technique | domain | status | summary | source |
|---|---|---|---|---|
| [AOA-T-0070](../techniques/agent-workflows/two-stage-document-ocr-pipeline/TECHNIQUE.md) | `agent-workflows` | `promoted` | Stage OCR as detect or layout -> recognize -> structured handoff so downstream extraction stays reviewable, interchangeable, and confidence-aware instead of collapsing OCR and field logic into one opaque step. | [TECHNIQUE.md](../techniques/agent-workflows/two-stage-document-ocr-pipeline/TECHNIQUE.md) |
| [AOA-T-0071](../techniques/agent-workflows/template-backed-field-extraction-after-ocr/TECHNIQUE.md) | `agent-workflows` | `promoted` | Extract bounded fields after OCR through explicit templates, heuristics, and missing-or-conflict signaling so structured receipt-like data stays reviewable instead of being guessed by one opaque parser. | [TECHNIQUE.md](../techniques/agent-workflows/template-backed-field-extraction-after-ocr/TECHNIQUE.md) |
| [AOA-T-0072](../techniques/agent-workflows/perceptual-media-dedupe-with-threshold-review/TECHNIQUE.md) | `agent-workflows` | `promoted` | Group near-duplicate media through perceptual similarity and thresholded review buckets so cleanup stays reviewable instead of collapsing into silent deletion or one-threshold dogma. | [TECHNIQUE.md](../techniques/agent-workflows/perceptual-media-dedupe-with-threshold-review/TECHNIQUE.md) |
| [AOA-T-0073](../techniques/agent-workflows/semantic-media-bucketing-with-vision-plus-ocr/TECHNIQUE.md) | `agent-workflows` | `promoted` | Bucket mixed media through bounded visual semantics plus OCR side text so screenshots, memes, receipts, and other media classes remain reviewable under explicit confidence gates instead of widening into open-ended multimodal automation. | [TECHNIQUE.md](../techniques/agent-workflows/semantic-media-bucketing-with-vision-plus-ocr/TECHNIQUE.md) |
| [AOA-T-0074](../techniques/agent-workflows/telegram-export-normalization-to-local-store/TECHNIQUE.md) | `agent-workflows` | `promoted` | Normalize Telegram messages and media into a resumable local store with visible provenance so later workflows can inspect, route, or distill the data without collapsing auth, session, or memory doctrine into the storage contract. | [TECHNIQUE.md](../techniques/agent-workflows/telegram-export-normalization-to-local-store/TECHNIQUE.md) |

## `assessment`

Classification, diagnosis, route comparison, or decision-support pattern that stays descriptive rather than mutating.

Choose this when:
- the technique compares options, labels drift, or names likely causes or owner targets
- the output is a bounded verdict packet, matrix, route card, or routing aid rather than proof of correctness

Do not use this when:
- the technique is a hard proof or integrity check
- the technique directly performs repair, mutation, or guarded execution

Counts: `total` 9, `canonical` 0, `promoted` 9.

| domain | entries |
|---|---|
| `agent-workflows` | `9` |
| `docs` | `0` |
| `evaluation` | `0` |
| `system-recovery` | `0` |
| `validation-patterns` | `0` |
| `history` | `0` |

| technique | domain | status | summary | source |
|---|---|---|---|---|
| [AOA-T-0076](../techniques/agent-workflows/owner-layer-triage/TECHNIQUE.md) | `agent-workflows` | `promoted` | Route one bounded reusable unit to one primary owner layer and one rejected nearest-wrong target so practice, workflow, scenario, proof, recall, and role surfaces stay distinct instead of collapsing into generic reuse. | [TECHNIQUE.md](../techniques/agent-workflows/owner-layer-triage/TECHNIQUE.md) |
| [AOA-T-0078](../techniques/agent-workflows/decision-fork-cards/TECHNIQUE.md) | `agent-workflows` | `promoted` | Turn one reviewed session or harvest packet into explicit decision fork cards so materially different next routes stay visible with gains, costs, owner targets, and stop conditions instead of collapsing into one hidden recommendation. | [TECHNIQUE.md](../techniques/agent-workflows/decision-fork-cards/TECHNIQUE.md) |
| [AOA-T-0079](../techniques/agent-workflows/risk-passport-lift/TECHNIQUE.md) | `agent-workflows` | `promoted` | Attach one small risk passport to each explicit next route so difficulty, risk, control mode, delegate tier, and stop-condition posture stay visible without turning branch analysis into hidden routing policy. | [TECHNIQUE.md](../techniques/agent-workflows/risk-passport-lift/TECHNIQUE.md) |
| [AOA-T-0080](../techniques/agent-workflows/session-drift-taxonomy/TECHNIQUE.md) | `agent-workflows` | `promoted` | Classify repeated post-session friction into bounded drift types so diagnosis can say what kind of problem is present before it claims one probable cause, owner hint, or repair shape. | [TECHNIQUE.md](../techniques/agent-workflows/session-drift-taxonomy/TECHNIQUE.md) |
| [AOA-T-0081](../techniques/agent-workflows/diagnosis-from-reviewed-evidence/TECHNIQUE.md) | `agent-workflows` | `promoted` | Turn reviewed friction evidence into a bounded diagnosis packet that separates symptoms from probable causes, preserves unknowns, and names likely owner hints without mutating anything yet. | [TECHNIQUE.md](../techniques/agent-workflows/diagnosis-from-reviewed-evidence/TECHNIQUE.md) |
| [AOA-T-0086](../techniques/agent-workflows/automation-fit-matrix/TECHNIQUE.md) | `agent-workflows` | `promoted` | Classify one recurring manual route across repeat signal, determinism, proof posture, reversibility, and approval sensitivity so automation desire becomes a bounded verdict rather than vague enthusiasm. | [TECHNIQUE.md](../techniques/agent-workflows/automation-fit-matrix/TECHNIQUE.md) |
| [AOA-T-0087](../techniques/agent-workflows/human-loop-to-seed-lift/TECHNIQUE.md) | `agent-workflows` | `promoted` | Route one recurring human loop to the first honest automation-facing landing so seed-ready candidates become bounded skills or playbook seeds while unstable routes stay manual, repair-bound, or deferred. | [TECHNIQUE.md](../techniques/agent-workflows/human-loop-to-seed-lift/TECHNIQUE.md) |
| [AOA-T-0088](../techniques/agent-workflows/approval-sensitivity-check/TECHNIQUE.md) | `agent-workflows` | `promoted` | Classify whether an automation candidate crosses approval, rollback, or self-change boundaries so checkpoint-required posture appears before any seed-ready claim becomes credible. | [TECHNIQUE.md](../techniques/agent-workflows/approval-sensitivity-check/TECHNIQUE.md) |
| [AOA-T-0089](../techniques/agent-workflows/quest-unit-promotion-review/TECHNIQUE.md) | `agent-workflows` | `promoted` | Review one repeated reviewed quest unit and emit one bounded promotion verdict so leaf workflow, route, role, proof, and recall surfaces do not collapse into generic reuse pressure. | [TECHNIQUE.md](../techniques/agent-workflows/quest-unit-promotion-review/TECHNIQUE.md) |

## `recovery`

Degraded continuation, regrounding, repair, rollback, or explicit recovery posture.

Choose this when:
- the technique exists to keep work safe when the normal path is weakened or broken
- repair or recovery posture is the main reusable contract

Do not use this when:
- the technique only diagnoses a problem without shaping recovery or repair
- the technique is a steady-state workflow with no degraded or repair posture

Counts: `total` 5, `canonical` 0, `promoted` 5.

| domain | entries |
|---|---|
| `agent-workflows` | `2` |
| `docs` | `0` |
| `evaluation` | `0` |
| `system-recovery` | `3` |
| `validation-patterns` | `0` |
| `history` | `0` |

| technique | domain | status | summary | source |
|---|---|---|---|---|
| [AOA-T-0082](../techniques/agent-workflows/repair-shape-from-diagnosis/TECHNIQUE.md) | `agent-workflows` | `promoted` | Turn a reviewed diagnosis packet into the smallest honest repair shape so the next artifact stays bounded, owner-aware, and smaller than a scenario rollout. | [TECHNIQUE.md](../techniques/agent-workflows/repair-shape-from-diagnosis/TECHNIQUE.md) |
| [AOA-T-0083](../techniques/agent-workflows/checkpoint-bound-self-repair/TECHNIQUE.md) | `agent-workflows` | `promoted` | Keep self-repair behind explicit checkpoint posture with approval, rollback, health checks, iteration limits, and improvement-log visibility so repair stays reviewable instead of feeling like silent self-modification. | [TECHNIQUE.md](../techniques/agent-workflows/checkpoint-bound-self-repair/TECHNIQUE.md) |
| [AOA-T-0097](../techniques/system-recovery/degrade-reground-recover/TECHNIQUE.md) | `system-recovery` | `promoted` | Continue safely in a bounded degraded mode, reground against stronger sources, and recover later through explicit source-owned evidence instead of hidden repair theater. | [TECHNIQUE.md](../techniques/system-recovery/degrade-reground-recover/TECHNIQUE.md) |
| [AOA-T-0099](../techniques/system-recovery/isolated-service-stop-on-shared-substrate/TECHNIQUE.md) | `system-recovery` | `promoted` | Stop one bounded service while keeping shared substrate services alive, then verify both target absence and substrate continuity so closeout does not widen into unnecessary teardown. | [TECHNIQUE.md](../techniques/system-recovery/isolated-service-stop-on-shared-substrate/TECHNIQUE.md) |
| [AOA-T-0100](../techniques/system-recovery/stress-receipt-reground-closeout/TECHNIQUE.md) | `system-recovery` | `promoted` | Record one bounded stress event, preserve the smallest honest continuation, route through owner layers, and close out with reviewed evidence before any later proof reading. | [TECHNIQUE.md](../techniques/system-recovery/stress-receipt-reground-closeout/TECHNIQUE.md) |

## Boundaries

- `domain` stays the first owner and routing axis.
- `kind` stays one bounded primary reusable-practice axis only.
- `tags` remain the freeform nuance layer.
- `family` stays scout-only and does not become frontmatter or schema truth in this wave.
