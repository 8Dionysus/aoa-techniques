# External Technique Candidates

This doc records the remaining external donor-derived technique candidates tracked from `seeds/seed_4.txt` and `seeds/seed_6.txt`.

Use it when the question is not "which landed technique should I open?", but "which remaining external seed idea should we distill into a real `aoa-techniques` bundle next?"

It is an intake and decision surface.
It does not change technique status, create a new bundle, or authorize import by itself.

## Scope

- this doc tracks the remaining `13` external donor-derived candidates
- it excludes the already-landed external imports:
  - [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md)
  - [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md)
  - [AOA-T-0023](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md)
  - [AOA-T-0028](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md)
  - [AOA-T-0024](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md)
  - [AOA-T-0025](../techniques/docs/capability-spec-versioning/TECHNIQUE.md)
  - [AOA-T-0027](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md)
  - [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md)
  - [AOA-T-0038](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md)
  - [AOA-T-0041](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md)
  - [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md)
- current donor pool represented here:
  - `n-skills`
  - `agents-md`
  - `ruler`
  - `OpenMemory-Code`
  - `qqqa`
  - `agentwise`
  - `agentic`
  - `SpecStory`

## Doctrine Seam

- if something is already a reusable, bounded, public-safe technique, its canonical home is `aoa-techniques`
- neighboring `aoa-*` repos may incubate the pattern, prove it in live use, or consume the resulting technique, but they do not become the long-term owner of the technique canon
- these verdicts therefore do **not** mean "another repo should own the technique instead"
- they mean one of four narrower things:
  - the technique is ready to extract here now
  - the technique still needs one more narrowing pass before extraction here
  - the candidate still overlaps an already-landed technique here
  - the source pattern is still layer-owned behavior or substrate and is not yet technique-shaped

## How To Read The Verdicts

- `ready to distill here`
  - the pattern already looks like a bounded, public-safe technique that can be drafted into `aoa-techniques` without waiting for a new home-repo incubation cycle
- `future import here`
  - the pattern looks like a good next-wave candidate for `aoa-techniques`, but still needs one more narrowing pass before drafting
- `hold because overlap`
  - the pattern is real, but current separability from an existing landed technique is not sharp enough yet
- `needs layer incubation before distillation here`
  - the pattern still needs one more stable contract pass in a layer repo before it can be extracted into `aoa-techniques`
- `substrate or architecture pattern, not yet a technique`
  - the current seed idea is still too infra-shaped, role-shaped, or optimization-shaped to behave like one bounded technique bundle

## Current Summary

- `0` ready to distill here
- `1` future import here
- `4` hold because overlap
- `5` needs layer incubation before distillation here
- `3` substrate or architecture pattern, not yet a technique

Most recent landings from this backlog:

- [AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md)
- [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md)
- [AOA-T-0041](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md)
- [AOA-T-0038](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md)
- [AOA-T-0029](../techniques/docs/nested-rule-loading/TECHNIQUE.md)
- [AOA-T-0030](../techniques/docs/fragmented-agent-context/TECHNIQUE.md)
- [AOA-T-0031](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md)
- [AOA-T-0032](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md)
- [AOA-T-0027](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md)
- [AOA-T-0028](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md)

Current history watch:

- keep `project_memory_bootstrap` out of the immediate next wave against [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md); the Wave C history pair now lands through [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) and [AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md)

## Current Wave Placement

The current `future import here` lane is now staged as a wave program rather than a flat next-candidate queue.

The goal is to keep the import path coherent by family while still landing one technique per PR.

## Swarm Execution Layer

- the main agent owns wave boundaries, final wording, the cross-doc sequence, shared generated-surface sync, and `python scripts/release_check.py` so the shared contract does not fragment across workers
- each worker handles one technique at a time, with one bundle draft, one evidence package, and one PR-sized scope
- external anchors are execution seeds, not merge units: they mark which candidate opens the wave, while the rest of the family follows under the same boundary
- execution role: keep [AOA-T-0038](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) as the landed Wave A lifecycle anchor inside the now-complete runtime family after `profile-preset-composition`, `render-truth-before-startup`, `contextual-host-doctor`, and `baseline-first-additive-profile-benchmarks` fixed the sibling boundaries
- execution note: Wave A remains fully landed across the external and cross-layer intake surfaces; keep `AOA-T-0038` as the lifecycle sibling only and do not reopen launcher doctrine while later sequencing moves elsewhere
- execution role: keep [AOA-T-0041](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) as the landed Wave B external curation anchor after [AOA-T-0040](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md) clarified the reusable-skill versus user-invocation seam
- execution note: Wave B is now fully landed across both intake surfaces through [AOA-T-0040](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md), [AOA-T-0041](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md), [AOA-T-0042](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md), and [AOA-T-0043](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md); keep the next sequencing on the narrowing lane and the closed Wave C seam rather than reopening marketplace, registry, or bridge doctrine
- Wave C is now fully landed across the external and cross-layer intake surfaces through [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) and [AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md); keep later sequencing on the narrowing lane and the closed seam around [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md)
- `phase_sync_for_agents` stays outside the waves as a narrowing lane and does not block Wave A or Wave B
- latest public donor read for `phase_sync_for_agents` still presents phase sync inside broad orchestration, routing, shared context, monitoring, and token-optimization posture rather than as a standalone handoff contract

### Wave A - Runtime Truth And Local Lifecycle

- external wave anchor here is now landed as [AOA-T-0038](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) `one-command-service-lifecycle`
- Wave A is now fully landed across both intake surfaces with [AOA-T-0035](../techniques/docs/profile-preset-composition/TECHNIQUE.md), [AOA-T-0036](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md), [AOA-T-0037](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md), and [AOA-T-0039](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) tracked in [CROSS_LAYER_TECHNIQUE_CANDIDATES.md](CROSS_LAYER_TECHNIQUE_CANDIDATES.md)
- shared in-scope boundary for the full wave: profile composition, rendered runtime truth, profile-scoped preflight, additive comparison discipline, and bounded local lifecycle
- shared out-of-scope boundary for the full wave: deployment orchestration, secret transport, fleet monitoring, memory semantics, and generic launcher or platform doctrine

### Wave B - Curated Input Surfaces And Capability Boundaries

- external wave anchor here is now landed as [AOA-T-0041](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) `skill-marketplace-curation`
- cross-layer opener now landed as [AOA-T-0040](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md) `skill-vs-command-boundary`
- the remaining native family stays staged in [CROSS_LAYER_TECHNIQUE_CANDIDATES.md](CROSS_LAYER_TECHNIQUE_CANDIDATES.md) as the source/discovery/boundary cluster
- source-readiness sibling now landed as [AOA-T-0042](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md) `upstream-skill-health-checking`
- provenance-ordering sibling now landed as [AOA-T-0043](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md) `multi-source-primary-input-provenance`
- Wave B is now fully landed across both intake surfaces
- shared in-scope boundary for the full wave: curated discoverability, artifact-boundary clarity, upstream shape and availability checks, and primary-vs-supporting provenance ordering
- shared out-of-scope boundary for the full wave: registry governance, routing policy, slash-command product semantics, retrieval ranking, and graph semantics

### Wave C - History As Reviewable Artifact

- external wave anchor here is now landed as [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) `versionable-session-transcripts`
- the cross-layer companion now lands in [CROSS_LAYER_TECHNIQUE_CANDIDATES.md](CROSS_LAYER_TECHNIQUE_CANDIDATES.md) as [AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) `witness-trace-as-reviewable-artifact`
- prerequisite for the full wave: keep the techniques artifact-first and do not let them widen into memory substrate, recall surfaces, or hidden instruction authority
- keep the landed pair behind the same seam around [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) now that both post-capture history siblings are extracted
- execution role: keep [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) as the post-capture transcript-shaping anchor and do not let it collapse back into first-save capture or widen into hosted sharing and rule-derivation behavior
- `AOA-T-0026` keeps ownership of whether a session gets captured at all, where the project-scoped artifact home lives, and whether local-first artifact availability exists without cloud dependence
- [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) now owns the post-capture transcript packaging sibling: selected conversations can be combined, reviewed, edited, and preserved as readable Markdown artifacts for commit or sharing without reopening capture semantics
- [AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) now owns post-capture witness export, citation, and review-packet discipline over an existing artifact without becoming runtime witness generation, memory writeback, or future-instruction derivation

### Active Narrowing Lane, Not A Wave Yet

- keep `phase_sync_for_agents` as the active narrowing lane rather than promoting it into a large import wave yet
- reopen it only when the draft can name the phase boundary, the handoff packet, what permits the receiving agent to continue, and the stop, return, or escalation rule without leaning on broader orchestration doctrine
- latest public donor evidence is still a no-go for drafting: it does not yet expose those four readiness fields as a standalone public contract apart from the larger orchestration package
- do not let this narrowing lane block Wave A or Wave B
- the narrowing lane remains a separate sequencing track, not part of the wave queue

## Ready To Distill Here

None right now. The current strict-safe lane has already been landed into [AOA-T-0027](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) and [AOA-T-0028](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md).

## Future Import Here

| seed candidate | donor | suggested technique name | tentative domain | working contract | next move |
|---|---|---|---|---|---|
| `phase_sync_for_agents` | `agentwise` | `phase-synchronized-agent-handoff` | `agent-workflows` | synchronize multi-agent work through explicit phase checkpoints and bounded handoff seams | keep it in the current narrowing slice because the latest public donor read still does not expose a standalone phase boundary, handoff packet, continuation permission, and stop/return/escalation rule apart from the orchestration stack |

## Hold Because Overlap

| seed candidate | donor | suggested technique name | tentative domain | overlap note | next move |
|---|---|---|---|---|---|
| `external_sync_manifest` | `n-skills` | `external-sync-manifest` | `docs` | too close to [AOA-T-0024](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md), which already covers explicit upstream mirroring plus provenance | reopen only if a clean contract emerges that is about sync control rather than provenance-backed mirroring |
| `project_memory_bootstrap` | `OpenMemory-Code` | `project-history-bootstrap` | `history` | too close to [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) unless it is narrowed to history bootstrap without memory-substrate semantics | reopen only if the seed can be reduced to local-first history bootstrapping and nothing more |
| `context_injection_for_coding_agents` | `agents-md` | `bounded-context-injection-for-coding-agents` | `docs` | currently overlaps both [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) and [AOA-T-0023](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) | reopen only if injection itself becomes the distinct contract rather than composition or one-shot execution |
| `single_step_agent` | `qqqa` | `single-step-confirmed-agent-action` | `agent-workflows` | currently too close to [AOA-T-0023](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) | reopen only if the true center becomes the one-step mutating boundary, not generic stateless invocation |

## Needs Layer Incubation Before Distillation Here

| seed candidate | donor | suggested technique name | tentative domain if later imported | why it still needs incubation | next move |
|---|---|---|---|---|---|
| `memory_enforcement_layers` | `OpenMemory-Code` | `layered-memory-enforcement` | not in the current domain map | the pattern is still tightly coupled to memory substrate ownership and enforcement behavior | wait for one stable, public-safe layered contract in a memory home before extracting a bounded technique |
| `history_to_instructions` | `SpecStory` | `review-gated-history-derived-instructions` | not in the current domain map | the idea is useful, but in raw form it makes history into hidden instruction authority | incubate only if a strict review gate is made part of the invariant rather than a later editorial caution |
| `dynamic_specialist_generation` | `agentwise` | `bounded-specialist-generation` | `agent-workflows` only after heavy narrowing | the current seed is still mostly role and orchestration behavior rather than one reusable technique contract | wait for one stable specialist-scope and handoff contract before extraction |
| `persistent_agent_registry` | `agentic` | `versioned-agent-registry-contract` | `docs` only after spec extraction | the seed is still a stateful runtime registry rather than a reviewable public contract | incubate until registry semantics can be separated cleanly from registry implementation |
| `execution_history_learning` | `agentic` | `review-gated-execution-history-distillation` | not in the current domain map | the seed still behaves like a learning loop rather than a bounded, reviewable technique | wait for one explicit distillation contract that keeps adaptive behavior subordinate to human review |

## Substrate Or Architecture Pattern, Not Yet A Technique

| seed candidate | donor | why it is not technique-shaped yet | what would have to change |
|---|---|---|---|
| `shared_context_server` | `agentwise` | the current seed is a shared runtime substrate with state and coordination semantics, not one bounded reusable technique contract | extract a smaller public-safe pattern above the server layer, such as a narrow context-sharing handoff contract |
| `token_optimization_by_context_sharing` | `agentwise` | the current seed is still a performance strategy tied to caching and product tradeoffs rather than one reviewable contract | extract one bounded technique that is about explicit context reuse discipline, not generalized token optimization |
| `agent_self_assembly` | `agentic` | the current seed is an architecture cluster around runtime composition of agents from capabilities and constraints | extract a single smaller contract, such as bounded capability selection or bounded assembly review, before proposing a technique bundle |

## Recommended Next Expansion Order

If the goal is to grow the corpus without widening repo boundaries, the strongest current order is:

1. keep `phase_sync_for_agents` active as a narrowing lane in parallel, but do not promote it into a bundle wave yet
2. revisit the overlap and incubation lanes only after one of their missing boundaries becomes explicit

Then revisit the overlap and incubation lanes only after one of their missing boundaries becomes explicit.

## Current Narrowing Slice: `phase_sync_for_agents`

Treat `phase_sync_for_agents` as the active seed-refinement lane because it is already the top recommended next expansion object and the reusable center looks smaller than the broader `agentwise` orchestration package.

### Working extraction target

- public technique name: `phase-synchronized-agent-handoff`
- tentative domain: `agent-workflows`
- narrow contract: coordinate multi-agent work through explicit named phases where each handoff happens only at one declared checkpoint with a visible status summary, one explicit handoff artifact or status packet, and one clear next owner

### Current donor read stays no-go

- public evidence refresh checked on `2026-03-23` across the GitHub README and `agentwise-docs.vercel.app` home still shows phase sync as part of a larger orchestration package rather than as one standalone handoff contract
- public donor signals currently visible are `phase-based synchronization across all agents` and `Phase Controller`, but they still sit inside a package that foregrounds `Smart Model Router`, `Dynamic Task Distributor`, `SharedContextServer`, `Context Coordination`, and dashboard monitoring
- named phase boundary: partial only; the donor names phase sync broadly, but still does not isolate one reusable handoff boundary in plain language
- handoff packet: missing; public donor material still does not show one explicit packet shape or bounded handoff artifact
- continuation permission: missing; public donor material still does not say what authorizes the receiving agent to continue
- stop, return, or escalation rule: missing; public donor material still does not expose one bounded failure rule as a public contract
- keep the lane active, but do not draft the bundle while those gaps remain implicit

### Current public evidence map

- GitHub `README.md` checked on `2026-03-23`: the public donor still centers `Smart Orchestration`, `Phase-based Synchronization across all agents`, `SharedContextServer`, `Real-Time Monitor Dashboard`, `Smart Model Routing`, and `Project Registry Sync`
- `agentwise-docs.vercel.app` home checked on `2026-03-23`: the public docs still market `parallel AI agent execution`, `intelligent task distribution`, `Smart Model Routing`, `Dynamic Agents`, and `Real-time Monitor`
- `checkpoint`, `handoff`, and `packet` still do not appear in the public GitHub README or docs home, so the donor still does not expose one bounded transfer object, continuation rule, or failure packet in public

### Public evidence required before reopen

- one public README, doc, example, or issue that names a single reusable checkpoint boundary rather than only broad multi-phase orchestration
- one public handoff artifact or packet shape that can be quoted as the bounded transfer object
- one public rule that states what permits the receiving agent to continue
- one public rule that forces stop, return, or escalation when the packet or boundary is invalid

### What stays in scope

- one explicit phase or checkpoint name for the current handoff
- one visible entry or exit condition for crossing that phase boundary
- one reviewable handoff packet that tells the receiving agent what is done, what remains blocked, and what should happen next
- one explicit stop, return, or escalation rule when the packet is incomplete or the phase boundary is no longer valid

### What stays out of the donor

- model routing
- shared context server or token optimization
- dynamic specialist generation
- persistent agent registry or execution-history learning
- dashboard, analytics, or live monitoring
- generic parallel-execution doctrine without an explicit checkpoint and handoff contract

### Nearest overlap watch

- [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) remains the broader multi-step change workflow; this seed should own cross-agent checkpoint and handoff seams, not the whole plan/verify/report loop
- [AOA-T-0023](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) remains the single-shot fast path; it may be a source or sink of a handoff, but it is not the handoff contract itself
- `bounded-specialist-generation` remains an adjacent incubation lane and must stay out of scope until specialist creation can be separated cleanly from handoff discipline

### Honest reopen trigger

Reopen this seed as a real bundle only when the draft can say, in plain language:

- what phase boundary is being crossed
- what artifact or status packet is handed off
- what makes the receiving agent allowed to continue
- what forces a stop, return, or escalation instead of silent continuation

### Expected first import package

- one `TECHNIQUE.md`
- one `notes/external-origin.md`
- one `notes/external-import-review.md`
- one `notes/second-context-adaptation.md`
- one checklist
- one minimal example

This remains a per-technique package, not a multi-technique wave bundle.
Shared generated surfaces should be synchronized only after the bundle draft is merge-ready, and only by the main agent.

## Notes

- these are candidate techniques, not commitments to import
- a candidate can still be a valid AoA technique even if it currently needs one more extraction pass before it can land here cleanly
- this doc deliberately separates `not yet extracted into a technique` from `not a technique at all`
