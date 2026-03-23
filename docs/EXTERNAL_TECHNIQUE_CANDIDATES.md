# External Technique Candidates

This doc records the remaining external donor-derived technique candidates tracked from `seeds/seed_4.txt` and `seeds/seed_6.txt`.

Use it when the question is not "which landed technique should I open?", but "which remaining external seed idea should we distill into a real `aoa-techniques` bundle next?"

It is an intake and decision surface.
It does not change technique status, create a new bundle, or authorize import by itself.

## Scope

- this doc tracks the remaining `16` external donor-derived candidates
- it excludes the already-landed external imports:
  - [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md)
  - [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md)
  - [AOA-T-0023](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md)
  - [AOA-T-0028](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md)
  - [AOA-T-0024](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md)
  - [AOA-T-0025](../techniques/docs/capability-spec-versioning/TECHNIQUE.md)
  - [AOA-T-0027](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md)
  - [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md)
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
- `4` future import here
- `4` hold because overlap
- `5` needs layer incubation before distillation here
- `3` substrate or architecture pattern, not yet a technique

Most recent landings from this backlog:

- [AOA-T-0029](../techniques/docs/nested-rule-loading/TECHNIQUE.md)
- [AOA-T-0030](../techniques/docs/fragmented-agent-context/TECHNIQUE.md)
- [AOA-T-0031](../techniques/agent-workflows/shell-composable-agent-invocation/TECHNIQUE.md)
- [AOA-T-0032](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md)
- [AOA-T-0027](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md)
- [AOA-T-0028](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md)

Current history watch:

- keep `versionable_agent_transcripts` and `project_memory_bootstrap` out of the immediate next wave until the seam around [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) is sharper

## Ready To Distill Here

None right now. The current strict-safe lane has already been landed into [AOA-T-0027](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) and [AOA-T-0028](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md).

## Future Import Here

| seed candidate | donor | suggested technique name | tentative domain | working contract | next move |
|---|---|---|---|---|---|
| `skill_marketplace_curation` | `n-skills` | `skill-marketplace-curation` | `docs` | curate a local discoverability layer over upstream-owned skill sources without pretending to own them | keep it editorial and discovery-focused rather than registry or governance heavy |
| `one-command_service_lifecycle` | `OpenMemory-Code` | `one-command-service-lifecycle` | `agent-workflows` | start and stop a bounded local service stack for agent work through one explicit lifecycle command | keep it to local lifecycle discipline and avoid broad project-launcher semantics |
| `versionable_agent_transcripts` | `SpecStory` | `versionable-session-transcripts` | `history` | keep AI session transcripts as versioned repo artifacts for later audit and distillation | keep it artifact-first and avoid memory recall, retrieval, or instruction-policy widening |
| `phase_sync_for_agents` | `agentwise` | `phase-synchronized-agent-handoff` | `agent-workflows` | synchronize multi-agent work through explicit phase checkpoints and bounded handoff seams | narrow it through the current `phase_sync_for_agents` slice below and keep only the checkpoint and handoff contract, not the whole orchestration stack |

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

1. `phase_sync_for_agents`
2. `skill_marketplace_curation`
3. `one-command_service_lifecycle`
4. `versionable_agent_transcripts` after one cleaner history seam around [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md)

Then revisit the overlap and incubation lanes only after one of their missing boundaries becomes explicit.

## Current Narrowing Slice: `phase_sync_for_agents`

Treat `phase_sync_for_agents` as the active seed-refinement lane because it is already the top recommended next expansion object and the reusable center looks smaller than the broader `agentwise` orchestration package.

### Working extraction target

- public technique name: `phase-synchronized-agent-handoff`
- tentative domain: `agent-workflows`
- narrow contract: coordinate multi-agent work through explicit named phases where each handoff happens only at one declared checkpoint with a visible status summary, one explicit handoff artifact or status packet, and one clear next owner

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

## Notes

- these are candidate techniques, not commitments to import
- a candidate can still be a valid AoA technique even if it currently needs one more extraction pass before it can land here cleanly
- this doc deliberately separates `not yet extracted into a technique` from `not a technique at all`
