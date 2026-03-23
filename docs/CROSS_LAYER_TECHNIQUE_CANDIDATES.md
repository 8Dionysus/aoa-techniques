# Cross-Layer Technique Candidates

This doc records the cross-layer technique candidates pulled from the Dionysus donor note `seed_donors_inside.md`.

Use it when the question is not "which landed technique should I open?", but "which technique-shaped candidates from that donor note should count as staged carry-over, future imports, overlap holds, layer-incubation lanes, or not-yet-technique-shaped architecture?"

This is an intake and decision surface.
It does not change technique status, create a new bundle, or authorize import by itself.

## Scope

- this doc accounts for the full `24` technique-shaped candidate names explicitly proposed in the donor note
- it treats `seed_donors_inside.md` as origin commentary and donor soil, not as a canonical Dionysus wave seed
- it includes `8` candidates that are already staged in [EXTERNAL_TECHNIQUE_CANDIDATES.md](EXTERNAL_TECHNIQUE_CANDIDATES.md) so the full donor-note universe stays visible in one place
- it classifies the remaining `16` candidates here as new future imports, overlap holds, layer-incubation lanes, or not-yet-technique-shaped architecture

## Doctrine Seam

- if something is already a reusable, bounded, public-safe technique, its canonical home is `aoa-techniques`
- neighboring `aoa-*` repos may incubate the pattern, prove it in live use, or consume the resulting technique, but they do not become the long-term owner of the technique canon
- these verdicts therefore do **not** mean "another repo should own the technique instead"
- they mean one of five narrower things:
  - the candidate is already staged elsewhere in this repo's current intake surfaces
  - the pattern still needs one more narrowing pass before extraction here
  - the candidate still overlaps an already-landed technique or repo-owned surface here
  - the source pattern still needs one more stable contract pass in a layer repo before extraction here
  - the current seed idea is still too infra-shaped, role-shaped, or architecture-shaped to behave like one bounded technique bundle

## How To Read The Verdicts

- `already staged elsewhere`
  - the candidate already appears in a current repo intake surface and keeps the inherited verdict from that surface
- `future import here`
  - the pattern looks like a good next-wave candidate for `aoa-techniques`, but still needs one more narrowing pass before drafting
- `hold because overlap`
  - the pattern is real, but current separability from an existing landed technique or reader surface is not sharp enough yet
- `needs layer incubation before distillation here`
  - the pattern still needs one more stable contract pass in a layer repo before it can be extracted into `aoa-techniques`
- `substrate or architecture pattern, not yet a technique`
  - the current seed idea is still too infra-shaped, role-shaped, or optimization-shaped to behave like one bounded technique bundle

## Current Summary

- `0` ready to distill here
- `8` already staged elsewhere
- `8` future import here
- `2` hold because overlap
- `3` needs layer incubation before distillation here
- `3` substrate or architecture pattern, not yet a technique

## Already Staged Elsewhere

| candidate | donor or source layer | tentative domain | inherited verdict | boundary note | next move |
|---|---|---|---|---|---|
| `skill-marketplace-curation` | `n-skills` | `docs` | `future import here` | keep it editorial and discovery-focused rather than registry or governance heavy | keep the active staging in [EXTERNAL_TECHNIQUE_CANDIDATES.md](EXTERNAL_TECHNIQUE_CANDIDATES.md) as the canonical intake surface for this external donor |
| `versionable-session-transcripts` | `SpecStory` | `history` | `future import here` | keep it artifact-first and avoid memory recall, retrieval, or instruction-policy widening | keep it staged against the history seam around [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) rather than reclassifying it here |
| `review-gated-history-derived-instructions` | `SpecStory` | not in the current domain map | `needs layer incubation before distillation here` | the raw idea still risks turning history into hidden instruction authority | incubate only if a strict review gate becomes part of the invariant rather than a later editorial caution |
| `phase-synchronized-agent-handoff` | `agentwise` | `agent-workflows` | `future import here` | distill only the checkpoint and handoff contract, not the whole orchestration stack | keep it staged in the external donor surface and reopen it there if a cleaner phase-checkpoint contract emerges |
| `versioned-agent-registry-contract` | `agentic` | `docs` only after spec extraction | `needs layer incubation before distillation here` | the seed is still a stateful runtime registry rather than a reviewable public contract | incubate until registry semantics can be separated cleanly from registry implementation |
| `bounded-specialist-generation` | `agentwise` | `agent-workflows` only after heavy narrowing | `needs layer incubation before distillation here` | the seed is still mostly role and orchestration behavior rather than one reusable technique contract | wait for one stable specialist-scope and handoff contract before extraction |
| `review-gated-execution-history-distillation` | `agentic` | not in the current domain map | `needs layer incubation before distillation here` | the seed still behaves like a learning loop rather than a bounded, reviewable technique | wait for one explicit distillation contract that keeps adaptive behavior subordinate to human review |
| `one-command-service-lifecycle` | `OpenMemory-Code` | `agent-workflows` | `future import here` | keep it to local lifecycle discipline and avoid broad project-launcher semantics | keep the active staging in [EXTERNAL_TECHNIQUE_CANDIDATES.md](EXTERNAL_TECHNIQUE_CANDIDATES.md) and avoid widening it into generic infra orchestration |

## Future Import Here

| candidate | donor or source layer | tentative domain | working contract | boundary note | next move |
|---|---|---|---|---|---|
| `upstream-skill-health-checking` | `n-skills`, MCP Gateway Registry | `evaluation` | check upstream-owned skill sources through a bounded health pass before surfacing them as selectable inputs | keep it about upstream-source health and shape signals, not generic monitoring or marketplace policy | narrow it to source availability and manifest-readiness checks rather than a broader registry health program |
| `skill-vs-command-boundary` | `agentic-dev-team` | `docs` | separate reusable skill surfaces from direct user-invoked command surfaces so shared capability does not collapse into invocation syntax | keep it about artifact boundaries, not role taxonomy, routing policy, or slash-command product design | distill only the contract boundary between reusable skill meaning and user-facing command invocation |
| `witness-trace-as-reviewable-artifact` | `aoa-memo`, `aoa-playbooks` | `history` | preserve witness trace output as a reviewable artifact that can be inspected and cited without turning it into a new memory kind | keep it artifact-first and avoid widening it into memory-substrate semantics or full witness runtime behavior | narrow it to the export and review contract before considering wider witness workflow siblings |
| `profile-preset-composition` | `abyss-stack` | `docs` | compose small reusable profiles into named presets so runtime posture stays reviewable without flattening composition into one opaque config | keep it at composition and naming rules, not deployment orchestration or launcher behavior | distill only the profile-plus-preset composition contract and explicit ownership of each layer |
| `render-truth-before-startup` | `abyss-stack` | `agent-workflows` | render the actual composed runtime truth before startup so operators review the real active configuration rather than inferred intent | keep it on pre-start rendered truth and review seams, not secret transport or runtime manager semantics | distill the render-and-review step as the reusable center and keep provider specifics out |
| `contextual-host-doctor` | `abyss-stack` | `evaluation` | run contextual host-readiness checks against the selected profile before startup so environment drift becomes visible early | keep it profile-scoped and diagnostic, not generic fleet monitoring or continuous incident tooling | narrow it to preflight readiness checks whose outputs stay human-reviewable |
| `baseline-first-additive-profile-benchmarks` | `ATM10-Agent`, `abyss-stack` | `evaluation` | benchmark one stable baseline profile first, then compare additive profiles against the same surface so claims stay comparable | keep it about additive comparison discipline, not benchmark theater or product-wide scoring | distill the baseline-then-additive comparison contract and leave benchmark suites or product claims outside the technique |
| `multi-source-primary-input-provenance` | `aoa-kag`, `Tree-of-Sophia` bridge contracts | `docs` | mark primary versus supporting source inputs explicitly when bridging multiple source surfaces so downstream retrieval and synthesis keep provenance priority visible | keep it on input provenance ordering, not graph semantics, synthesis policy, or retrieval ranking | reopen it as a bounded provenance-ordering technique rather than a larger bridge-architecture program |

## Hold Because Overlap

| candidate | donor or source layer | tentative domain | overlap note | next move |
|---|---|---|---|---|
| `progressive-skill-discovery` | `n-skills`, MCP Gateway Registry, repo-owned selector surfaces | `docs` | too close to `skill-marketplace-curation` plus the repo's current `pick -> inspect -> expand -> object use` discovery posture to count as a separate technique contract yet | reopen only if progressive disclosure itself becomes the distinct invariant rather than a restatement of curated discovery and selector behavior |
| `bounded-counterpart-edge-projection` | `aoa-kag`, `Tree-of-Sophia` bridge contracts | `docs` | too close to [AOA-T-0021](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) unless counterpart-specific non-identity semantics become a distinct reusable contract | reopen only if the counterpart edge can stay clearly narrower than generic bounded relation lift and carry a stable non-collapse contract of its own |

## Needs Layer Incubation Before Distillation Here

| candidate | donor or source layer | tentative domain if later imported | why it still needs incubation | next move |
|---|---|---|---|---|
| `temperature-gated-writeback` | `aoa-memo` | not in the current domain map | the pattern is still tightly coupled to memory writeback policy and temperature semantics owned by the memory layer | wait for one stable, public-safe writeback contract in `aoa-memo` before extracting a bounded technique |
| `checkpoint-cohort-rollout` | `aoa-agents`, `aoa-playbooks` | `agent-workflows` only after heavy narrowing | the current seed is still mostly playbook composition and role choreography rather than one reusable technique contract | wait for one stable checkpoint or handoff slice that can stand without the whole cohort rollout program |
| `witness-to-compost-promotion` | `aoa-playbooks`, `Tree-of-Sophia` support surfaces | `docs` only after heavy narrowing | the seed is still a route from witness output into compost artifacts rather than one bounded reusable technique | incubate until promotion gates and destination-artifact contracts can be stated without the full pilot playbook |

## Substrate Or Architecture Pattern, Not Yet A Technique

| candidate | donor or source layer | why it is not technique-shaped yet | what would have to change |
|---|---|---|---|
| `model-tier-state-machine` | `aoa-agents`, `abyss-stack` | the current seed is a model-routing and orchestration state machine, not one bounded reusable technique contract | extract a smaller public-safe seam, such as deep-call escalation or distillation handoff, before proposing a technique bundle |
| `cross-service-sla-normalization` | `ATM10-Agent`, `abyss-stack` | the current seed is still a multi-service architecture and measurement-policy cluster rather than one reviewable contract | extract one bounded comparison, readiness, or reporting contract above the SLA program before proposing a technique |
| `bridge-ready-retrieval-axis` | `aoa-kag` bridge contracts | the current seed is still a retrieval-substrate and bridge-architecture notion rather than one bounded reusable technique | extract one smaller input-boundary or retrieval contract first instead of treating the full axis as a technique |

## Notes

- these are candidate techniques, not commitments to import
- a candidate can still be a valid AoA technique even if it currently needs one more extraction pass before it can land here cleanly
- the `already staged elsewhere` section exists so the full `24`-name donor-note universe stays accounted for without reclassifying the current external-donor intake surface
