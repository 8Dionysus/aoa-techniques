# Cross-Layer Technique Candidates

This doc records the cross-layer technique candidates pulled from the Dionysus donor note `seed_donors_inside.md`.

Use it when the question is not "which landed technique should I open?", but "which technique-shaped candidates from that donor note should count as staged carry-over, future imports, overlap holds, layer-incubation lanes, or not-yet-technique-shaped architecture?"

This is an intake and decision surface.
It does not change technique status, create a new bundle, or authorize import by itself.

## Scope

- this doc accounts for the full `24` technique-shaped candidate names explicitly proposed in the donor note
- it treats `seed_donors_inside.md` as origin commentary and donor soil, not as a canonical Dionysus wave seed
- it includes `6` candidates that are already staged in [EXTERNAL_TECHNIQUE_CANDIDATES.md](EXTERNAL_TECHNIQUE_CANDIDATES.md) so the full donor-note universe stays visible in one place
- it classifies the remaining `17` candidates here as landed wave imports, new future imports, overlap holds, layer-incubation lanes, or not-yet-technique-shaped architecture

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
- `6` already staged elsewhere
- `10` landed from this wave map
- `0` future import here
- `2` hold because overlap
- `3` needs layer incubation before distillation here
- `3` substrate or architecture pattern, not yet a technique

## Already Staged Elsewhere

| candidate | donor or source layer | tentative domain | inherited verdict | boundary note | next move |
|---|---|---|---|---|---|
| `skill-marketplace-curation` | `n-skills` | `docs` | landed as [AOA-T-0041](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) | keep it editorial and discovery-focused rather than registry or governance heavy | keep the external intake surface as the canonical donor trail and use [AOA-T-0041](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) for the landed contract |
| `review-gated-history-derived-instructions` | `SpecStory` | not in the current domain map | `needs layer incubation before distillation here` | the raw idea still risks turning history into hidden instruction authority | incubate only if a strict review gate becomes part of the invariant rather than a later editorial caution |
| `phase-synchronized-agent-handoff` | `agentwise` | `agent-workflows` | `future import here` | distill only the checkpoint and handoff contract, not the whole orchestration stack | keep it staged in the external donor surface and reopen it there if a cleaner phase-checkpoint contract emerges |
| `versioned-agent-registry-contract` | `agentic` | `docs` only after spec extraction | `needs layer incubation before distillation here` | the seed is still a stateful runtime registry rather than a reviewable public contract | incubate until registry semantics can be separated cleanly from registry implementation |
| `bounded-specialist-generation` | `agentwise` | `agent-workflows` only after heavy narrowing | `needs layer incubation before distillation here` | the seed is still mostly role and orchestration behavior rather than one reusable technique contract | wait for one stable specialist-scope and handoff contract before extraction |
| `review-gated-execution-history-distillation` | `agentic` | not in the current domain map | `needs layer incubation before distillation here` | the seed still behaves like a learning loop rather than a bounded, reviewable technique | wait for one explicit distillation contract that keeps adaptive behavior subordinate to human review |

## Landed From This Wave Map

| candidate | landed technique | domain | landing note |
|---|---|---|---|
| `profile-preset-composition` | [AOA-T-0035](../techniques/docs/profile-preset-composition/TECHNIQUE.md) | `docs` | Wave A lead now lands as a bounded docs technique for module-profile-preset composition without widening into render, doctor, or lifecycle semantics. |
| `render-truth-before-startup` | [AOA-T-0036](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md) | `agent-workflows` | Wave A second step now lands as a bounded pre-start rendered-truth workflow without widening into readiness checks, lifecycle control, or config publication. |
| `contextual-host-doctor` | [AOA-T-0037](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md) | `evaluation` | Wave A third step now lands as a bounded selector-aware preflight diagnostic without widening into monitoring, smoke, or lifecycle control. |
| `one-command-service-lifecycle` | [AOA-T-0038](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) | `agent-workflows` | Wave A external anchor now lands as a bounded local lifecycle technique for one-entrypoint startup and shutdown without widening into launcher doctrine, install flows, or memory semantics. |
| `baseline-first-additive-profile-benchmarks` | [AOA-T-0039](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) | `evaluation` | Wave A closing step now lands as a bounded baseline-then-additive comparison technique that keeps benchmark claims comparable without widening into suite ownership, product scoring, or promotion policy. |
| `skill-vs-command-boundary` | [AOA-T-0040](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md) | `docs` | Wave B opening step now lands as a bounded docs technique for keeping reusable skill meaning distinct from user-facing command wrappers without widening into propagation, marketplace policy, routing, or slash-command product semantics. |
| `upstream-skill-health-checking` | [AOA-T-0042](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md) | `evaluation` | Wave B third step now lands as a bounded source-readiness technique for checking upstream availability and manifest shape before selector surfacing without widening into monitoring, registry governance, or security scanning doctrine. |
| `multi-source-primary-input-provenance` | [AOA-T-0043](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md) | `docs` | Wave B closing step now lands as a bounded provenance-ordering technique for keeping one combined surface explicit about primary versus supporting inputs without widening into note-provenance lift, relation semantics, ranking, or bridge architecture. |
| `versionable-session-transcripts` | [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) | `history` | Wave C first step now lands as a bounded post-capture transcript-packaging technique for readable Markdown export, review, and commit without reopening capture semantics or widening into memory or instruction authority. |
| `witness-trace-as-reviewable-artifact` | [AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) | `history` | Wave C closing step now lands as a bounded witness-export and review technique for structured trace inspection, citation, and summary without widening into runtime witness behavior, memory writeback, or a new memory-object kind. |

## Future Import Here

None right now. The remaining live sequencing track now sits in the external narrowing lane for `phase-synchronized-agent-handoff`.

## Current Wave Program

The current `future import here` lane is now staged as a wave program rather than a flat next-candidate queue.

The `already staged elsewhere` candidates keep their inherited placement in [EXTERNAL_TECHNIQUE_CANDIDATES.md](EXTERNAL_TECHNIQUE_CANDIDATES.md) and are not remapped here.

Each technique in a wave still lands through its own PR. The wave is a family-level import program, not a multi-technique merge unit.

- the main agent owns wave boundaries, final wording, shared generated surfaces, intake or roadmap sync, and `python scripts/release_check.py`
- before that final release-check path, install local validator deps with `python -m pip install -r requirements-dev.txt`
- each worker should own only one future bundle directory plus its `notes/`, `checks/`, and `examples/`
- shared files such as catalog, index, and generated surfaces stay out of worker ownership until a bundle draft is merge-ready

### Wave A - Runtime Truth And Local Lifecycle

- landed techniques:
  - [AOA-T-0035](../techniques/docs/profile-preset-composition/TECHNIQUE.md) `profile-preset-composition`
  - [AOA-T-0036](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md) `render-truth-before-startup`
  - [AOA-T-0037](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md) `contextual-host-doctor`
  - [AOA-T-0038](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) `one-command-service-lifecycle`
  - [AOA-T-0039](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) `baseline-first-additive-profile-benchmarks`
- execution order:
  1. `profile-preset-composition` (landed as [AOA-T-0035](../techniques/docs/profile-preset-composition/TECHNIQUE.md))
  2. `render-truth-before-startup` (landed as [AOA-T-0036](../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md))
  3. `contextual-host-doctor` (landed as [AOA-T-0037](../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md))
  4. `one-command-service-lifecycle` (landed as [AOA-T-0038](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md))
  5. `baseline-first-additive-profile-benchmarks` (landed as [AOA-T-0039](../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md))
- remaining candidates staged here: `none`
- external companion now landed as [AOA-T-0038](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) through [EXTERNAL_TECHNIQUE_CANDIDATES.md](EXTERNAL_TECHNIQUE_CANDIDATES.md)
- in scope: profile composition, rendered runtime truth, profile-scoped preflight, additive comparison discipline, and bounded local lifecycle
- out of scope: deployment orchestration, secret transport, fleet monitoring, memory semantics, and generic launcher or platform doctrine
- overlap watch: keep [AOA-T-0038](../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) as the lifecycle sibling only; do not let it absorb the profile/preset, rendered-truth, or preflight contracts of the other Wave A techniques
- completion note: Wave A remains fully landed across the cross-layer and external intake surfaces and should stay closed while later sequencing moves elsewhere

### Wave B - Curated Input Surfaces And Capability Boundaries

- landed techniques:
  - [AOA-T-0040](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md) `skill-vs-command-boundary`
  - [AOA-T-0041](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) `skill-marketplace-curation` as the landed external companion
  - [AOA-T-0042](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md) `upstream-skill-health-checking`
  - [AOA-T-0043](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md) `multi-source-primary-input-provenance`
- execution order:
  1. `skill-vs-command-boundary` (landed as [AOA-T-0040](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md))
  2. `skill-marketplace-curation` (landed as [AOA-T-0041](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) via [EXTERNAL_TECHNIQUE_CANDIDATES.md](EXTERNAL_TECHNIQUE_CANDIDATES.md))
  3. `upstream-skill-health-checking` (landed as [AOA-T-0042](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md))
  4. `multi-source-primary-input-provenance` (landed as [AOA-T-0043](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md))
- candidates staged here: `none`
- external companion now landed in [EXTERNAL_TECHNIQUE_CANDIDATES.md](EXTERNAL_TECHNIQUE_CANDIDATES.md) as [AOA-T-0041](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md)
- in scope: artifact-boundary clarity, curated discoverability, upstream shape and availability checks, and primary-vs-supporting provenance ordering
- out of scope: registry governance, routing policy, slash-command product semantics, retrieval ranking, and graph semantics
- overlap watch: keep `skill-marketplace-curation` editorial and discovery-focused; if `multi-source-primary-input-provenance` starts sounding like bridge architecture or retrieval ranking, defer it instead of widening Wave B
- overlap watch: keep `skill-vs-command-boundary` distinct from [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) and [AOA-T-0027](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md); keep `upstream-skill-health-checking` distinct from [AOA-T-0024](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) and [AOA-T-0032](../techniques/evaluation/context-report-for-ci/TECHNIQUE.md); keep `multi-source-primary-input-provenance` distinct from [AOA-T-0020](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) and [AOA-T-0021](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md)
- completion note: Wave B is now fully landed across the cross-layer and external intake surfaces through [AOA-T-0040](../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md), [AOA-T-0041](../techniques/docs/skill-marketplace-curation/TECHNIQUE.md), [AOA-T-0042](../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md), and [AOA-T-0043](../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md); the remaining live sequencing track is the active narrowing lane now that Wave C is fully landed through [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) and [AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md)

### Wave C - History As Reviewable Artifact

- landed techniques:
  - [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) `versionable-session-transcripts`
  - [AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) `witness-trace-as-reviewable-artifact`
- external companion now landed through [EXTERNAL_TECHNIQUE_CANDIDATES.md](EXTERNAL_TECHNIQUE_CANDIDATES.md) as [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) `versionable-session-transcripts`
- prerequisite: keep both techniques artifact-first and do not let them widen into memory substrate, recall surfaces, or hidden instruction authority
- seam rule: [AOA-T-0026](../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md) owns capture, persistence, and artifact-layer availability; Wave C may begin only at post-capture artifact shaping, export, or review
- `AOA-T-0026` keeps ownership of whether sessions are captured, where the local project-scoped artifact layer lives, and whether a reviewer can inspect the saved artifact without hidden runtime state
- [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) now owns transcript versionability, readable packaging, redactable export, and comparison-ready transcript shaping over an already-saved artifact
- [AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) now owns witness export, citation, and review-packet discipline over an already-saved artifact instead of witness runtime behavior or memory writeback
- execution order after seam clarification:
  1. `versionable-session-transcripts` (landed as [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md))
  2. `witness-trace-as-reviewable-artifact` (landed as [AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md))
- keep the landed pair narrow enough to separate [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) from raw session capture and [AOA-T-0045](../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) from a new memory kind
- no-go rule for future siblings: if a draft still needs `save sessions locally` or `derive future instructions` to explain its value, keep Wave C closed
- completion note: Wave C is now fully landed across the external and cross-layer intake surfaces and should stay closed while later sequencing focuses on the active narrowing lane

## Implementation Rules For The Current Wave Program

- external donors continue to use the normal external-import package in the external intake surface: `TECHNIQUE.md`, `notes/external-origin.md`, `notes/external-import-review.md`, `notes/second-context-adaptation.md`, one checklist, one minimal public-safe example, and the expected generated-surface sync
- cross-layer or internal-origin candidates here should use donor-appropriate origin and adaptation notes without forcing `external-*` note names where the donor is not actually an external-import case
- do not reopen `hold because overlap`, `needs layer incubation before distillation here`, or `substrate or architecture pattern, not yet a technique` lanes just to fill a wave
- shared generated surfaces should be synchronized only after a bundle draft is merge-ready, and only by the main agent

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
- the original `24`-name donor-note universe is still accounted for here because the intake map keeps `6` inherited external placements, `10` landed imports from the current wave map, and the remaining native candidate lanes visible in one surface
- the wave program here now points the landed Wave A, Wave B, and Wave C families at their technique bundles while inherited external placements stay in the external intake surface
