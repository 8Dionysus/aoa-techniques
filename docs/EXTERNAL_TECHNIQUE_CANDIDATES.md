# External Technique Candidates

This doc records the remaining external donor-derived technique candidates tracked from `seeds/seed_4.txt` and `seeds/seed_6.txt`.

Use it when the question is not "which landed technique should I open?", but "which remaining external seed idea should we distill into a real `aoa-techniques` bundle next?"

It is an intake and decision surface.
It does not change technique status, create a new bundle, or authorize import by itself.

## Scope

- this doc tracks the remaining `20` external donor-derived candidates
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

## How To Read The Verdicts

- `ready to distill here`
  - the pattern already looks like a bounded, public-safe technique that can be drafted into `aoa-techniques` without waiting for a new home-repo incubation cycle
- `future import here`
  - the pattern looks like a good next-wave candidate for `aoa-techniques`, but still needs one more narrowing pass before drafting
- `hold because overlap`
  - the pattern is real, but current separability from an existing landed technique is not sharp enough yet
- `incubate elsewhere, then distill here`
  - the pattern still needs one more stable contract pass in a home repo before it can be extracted into `aoa-techniques`
- `substrate or architecture pattern, not yet a technique`
  - the current seed idea is still too infra-shaped, role-shaped, or optimization-shaped to behave like one bounded technique bundle

## Current Summary

- `0` ready to distill here
- `8` future import here
- `4` hold because overlap
- `5` incubate elsewhere, then distill here
- `3` substrate or architecture pattern, not yet a technique

Most recent landings from this backlog:

- [AOA-T-0027](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md)
- [AOA-T-0028](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md)

## Ready To Distill Here

None right now. The current strict-safe lane has already been landed into [AOA-T-0027](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) and [AOA-T-0028](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md).

## Future Import Here

| seed candidate | donor | suggested technique name | tentative domain | working contract | next move |
|---|---|---|---|---|---|
| `skill_marketplace_curation` | `n-skills` | `skill-marketplace-curation` | `docs` | curate a local discoverability layer over upstream-owned skill sources without pretending to own them | keep it editorial and discovery-focused rather than registry or governance heavy |
| `fragmented_agent_context` | `agents-md` | `fragmented-agent-context` | `docs` | keep agent context in bounded fragments before deterministic assembly | center source partitioning and modular authoring rather than the final generated artifact already covered by [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) |
| `context_report_for_ci` | `agents-md` | `context-report-for-ci` | `evaluation` | emit CI-facing reports for context composition, source coverage, or token-estimate drift | import it as a validation or report surface, not as a second docs-composition technique |
| `nested_rule_loading` | `ruler` | `nested-rule-loading` | `docs` | load hierarchical rule layers while preserving one-way source ownership and explicit precedence | isolate the nested loading contract from the wider `ruler` product surface |
| `one-command_service_lifecycle` | `OpenMemory-Code` | `one-command-service-lifecycle` | `agent-workflows` | start and stop a bounded local service stack for agent work through one explicit lifecycle command | keep it to local lifecycle discipline and avoid broad project-launcher semantics |
| `versionable_agent_transcripts` | `SpecStory` | `versionable-session-transcripts` | `history` | keep AI session transcripts as versioned repo artifacts for later audit and distillation | keep it artifact-first and avoid memory recall, retrieval, or instruction-policy widening |
| `shell_composability` | `qqqa` | `shell-composable-agent-invocation` | `agent-workflows` | make agent runs composable as shell tools through explicit files, pipes, and one-shot calls | keep the shell boundary explicit and avoid drifting into generic shell best practices |
| `phase_sync_for_agents` | `agentwise` | `phase-synchronized-agent-handoff` | `agent-workflows` | synchronize multi-agent work through explicit phase checkpoints and bounded handoff seams | distill only the checkpoint and handoff contract, not the whole orchestration stack |

## Hold Because Overlap

| seed candidate | donor | suggested technique name | tentative domain | overlap note | next move |
|---|---|---|---|---|---|
| `external_sync_manifest` | `n-skills` | `external-sync-manifest` | `docs` | too close to [AOA-T-0024](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md), which already covers explicit upstream mirroring plus provenance | reopen only if a clean contract emerges that is about sync control rather than provenance-backed mirroring |
| `project_memory_bootstrap` | `OpenMemory-Code` | `project-history-bootstrap` | `history` | too close to [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) unless it is narrowed to history bootstrap without memory-substrate semantics | reopen only if the seed can be reduced to local-first history bootstrapping and nothing more |
| `context_injection_for_coding_agents` | `agents-md` | `bounded-context-injection-for-coding-agents` | `docs` | currently overlaps both [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) and [AOA-T-0023](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) | reopen only if injection itself becomes the distinct contract rather than composition or one-shot execution |
| `single_step_agent` | `qqqa` | `single-step-confirmed-agent-action` | `agent-workflows` | currently too close to [AOA-T-0023](../techniques/agent-workflows/stateless-single-shot-agent/TECHNIQUE.md) | reopen only if the true center becomes the one-step mutating boundary, not generic stateless invocation |

## Incubate Elsewhere, Then Distill Here

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

1. `nested_rule_loading`
2. `fragmented_agent_context`
3. `shell_composability`
4. `context_report_for_ci`
5. `versionable_agent_transcripts`
6. `phase_sync_for_agents`
7. `skill_marketplace_curation`

Then revisit the overlap and incubation lanes only after one of their missing boundaries becomes explicit.

## Notes

- these are candidate techniques, not commitments to import
- a candidate can still be a valid AoA technique even if it currently needs incubation outside this repo before extraction
- this doc deliberately separates `wrong home right now` from `not a technique at all`
