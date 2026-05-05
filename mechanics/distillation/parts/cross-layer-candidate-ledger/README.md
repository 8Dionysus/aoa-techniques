# Cross-Layer Technique Candidates

This doc records the cross-layer technique candidates pulled from the Dionysus donor note `seed_donors_inside.md`.

Use it when the question is not "which landed technique should I open?", but "which technique-shaped candidates from that donor note should count as staged carry-over, future imports, overlap holds, layer-incubation lanes, or not-yet-technique-shaped architecture?"

This is an intake and decision surface.
It does not change technique status, create a new bundle, or authorize import by itself.

The detailed pre-prune receipt is preserved at
[legacy/raw/CROSS_LAYER_CANDIDATE_LEDGER_2026-05-01_PRE_PRUNE.md](../../legacy/raw/CROSS_LAYER_CANDIDATE_LEDGER_2026-05-01_PRE_PRUNE.md).

## Scope

- this doc accounts for the full `24` technique-shaped candidate names explicitly proposed in the donor note
- it treats `seed_donors_inside.md` as origin commentary and donor soil, not as a canonical Dionysus wave seed
- it includes `6` candidates that are already staged in the [External Candidate Ledger](../external-candidate-ledger/README.md) so the full donor-note universe stays visible in one place
- it classifies the remaining `18` candidates here as landed wave imports, new future imports, overlap holds, layer-incubation lanes, or not-yet-technique-shaped architecture

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

## Structured Registry

The part-local registry keeps the full donor-note universe machine-checkable
without turning the ledger into promotion authority:

- [config/cross_layer_candidate_registry.seed.json](config/cross_layer_candidate_registry.seed.json)
  carries the structured accounting for all `24` candidates.
- [generated/cross_layer_candidate_registry.min.json](generated/cross_layer_candidate_registry.min.json)
  is derived evidence for counts, waves, source layers, and current gates.
- [schemas/](schemas/) and [examples/](examples/) document the expected entry
  shape.
- [scripts/build_cross_layer_candidate_registry.py](scripts/build_cross_layer_candidate_registry.py)
  builds the derived index, and
  [scripts/validate_cross_layer_candidate_registry.py](scripts/validate_cross_layer_candidate_registry.py)
  verifies that the index still matches the seed.

The registry must preserve this README's verdicts and stop lines. It does not
create technique bundles, change candidate status, authorize import, or give
recurrence promotion authority.

Validation:

```bash
python mechanics/distillation/parts/cross-layer-candidate-ledger/scripts/build_cross_layer_candidate_registry.py --check
python mechanics/distillation/parts/cross-layer-candidate-ledger/scripts/validate_cross_layer_candidate_registry.py
python -m pytest -q mechanics/distillation/parts/cross-layer-candidate-ledger/tests/test_cross_layer_candidate_registry.py
```

## Already Staged Elsewhere

| candidate | donor or source layer | tentative domain | inherited verdict | boundary note | next move |
|---|---|---|---|---|---|
| `skill-marketplace-curation` | `n-skills` | `docs` | landed as [AOA-T-0041](../../../../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) | keep it editorial and discovery-focused rather than registry or governance heavy | keep the external intake surface as the canonical donor trail and use [AOA-T-0041](../../../../techniques/docs/skill-marketplace-curation/TECHNIQUE.md) for the landed contract |
| `review-gated-history-derived-instructions` | `SpecStory` | not in the current domain map | `needs layer incubation before distillation here` | the raw idea still risks turning history into hidden instruction authority | incubate only if a strict review gate becomes part of the invariant rather than a later editorial caution |
| `phase-synchronized-agent-handoff` | `agentwise` | `agent-workflows` | `future import here` | distill only the checkpoint and handoff contract, not the whole orchestration stack | keep it staged in the external donor surface and reopen it there if a cleaner phase-checkpoint contract emerges |
| `versioned-agent-registry-contract` | `agentic` | `docs` only after spec extraction | `needs layer incubation before distillation here` | the seed is still a stateful runtime registry rather than a reviewable public contract | incubate until registry semantics can be separated cleanly from registry implementation |
| `bounded-specialist-generation` | `agentwise` | `agent-workflows` only after heavy narrowing | `needs layer incubation before distillation here` | the seed is still mostly role and orchestration behavior rather than one reusable technique contract | wait for one stable specialist-scope and handoff contract before extraction |
| `review-gated-execution-history-distillation` | `agentic` | not in the current domain map | `needs layer incubation before distillation here` | the seed still behaves like a learning loop rather than a bounded, reviewable technique | wait for one explicit distillation contract that keeps adaptive behavior subordinate to human review |

## Landed From This Wave Map

| candidate | landed technique | domain | landing note |
|---|---|---|---|
| `profile-preset-composition` | [AOA-T-0035](../../../../techniques/instruction/instruction-surface/profile-preset-composition/TECHNIQUE.md) | `docs` | Wave A lead now lands as a bounded docs technique for module-profile-preset composition without widening into render, doctor, or lifecycle semantics. |
| `render-truth-before-startup` | [AOA-T-0036](../../../../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md) | `agent-workflows` | Wave A second step now lands as a bounded pre-start rendered-truth workflow without widening into readiness checks, lifecycle control, or config publication. |
| `contextual-host-doctor` | [AOA-T-0037](../../../../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md) | `evaluation` | Wave A third step now lands as a bounded selector-aware preflight diagnostic without widening into monitoring, smoke, or lifecycle control. |
| `one-command-service-lifecycle` | [AOA-T-0038](../../../../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md) | `agent-workflows` | Wave A external anchor now lands as a bounded local lifecycle technique for one-entrypoint startup and shutdown without widening into launcher doctrine, install flows, or memory semantics. |
| `baseline-first-additive-profile-benchmarks` | [AOA-T-0039](../../../../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md) | `evaluation` | Wave A closing step now lands as a bounded baseline-then-additive comparison technique that keeps benchmark claims comparable without widening into suite ownership, product scoring, or promotion policy. |
| `skill-vs-command-boundary` | [AOA-T-0040](../../../../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md) | `docs` | Wave B opening step now lands as a bounded docs technique for keeping reusable skill meaning distinct from user-facing command wrappers without widening into propagation, marketplace policy, routing, or slash-command product semantics. |
| `upstream-skill-health-checking` | [AOA-T-0042](../../../../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md) | `evaluation` | Wave B third step now lands as a bounded source-readiness technique for checking upstream availability and manifest shape before selector surfacing without widening into monitoring, registry governance, or security scanning doctrine. |
| `multi-source-primary-input-provenance` | [AOA-T-0043](../../../../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md) | `docs` | Wave B closing step now lands as a bounded provenance-ordering technique for keeping one combined surface explicit about primary versus supporting inputs without widening into note-provenance lift, relation semantics, ranking, or bridge architecture. |
| `versionable-session-transcripts` | [AOA-T-0044](../../../../techniques/history/versionable-session-transcripts/TECHNIQUE.md) | `history` | Wave C first step now lands as a bounded post-capture transcript-packaging technique for readable Markdown export, review, and commit without reopening capture semantics or widening into memory or instruction authority. |
| `witness-trace-as-reviewable-artifact` | [AOA-T-0045](../../../../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md) | `history` | Wave C closing step now lands as a bounded witness-export and review technique for structured trace inspection, citation, and summary without widening into runtime witness behavior, memory writeback, or a new memory-object kind. |

## Future Import Here

None right now. The remaining live sequencing track now sits in the external narrowing lane for `phase-synchronized-agent-handoff`.

## Landed Wave Anchors

The old wave program is no longer an active execution queue. Waves A, B, and C
are fully landed; their detailed order, worker-role notes, and seam rationale
are preserved in the pre-prune receipt.

Keep these compact anchors active:

- Wave A landed [AOA-T-0035](../../../../techniques/instruction/instruction-surface/profile-preset-composition/TECHNIQUE.md),
  [AOA-T-0036](../../../../techniques/agent-workflows/render-truth-before-startup/TECHNIQUE.md),
  [AOA-T-0037](../../../../techniques/evaluation/contextual-host-doctor/TECHNIQUE.md),
  [AOA-T-0038](../../../../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md),
  and [AOA-T-0039](../../../../techniques/evaluation/baseline-first-additive-profile-benchmarks/TECHNIQUE.md);
  keep local lifecycle distinct from profile, rendered-truth, preflight, and
  additive-benchmark contracts.
- Wave B landed [AOA-T-0040](../../../../techniques/docs/skill-vs-command-boundary/TECHNIQUE.md),
  [AOA-T-0042](../../../../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md),
  and [AOA-T-0043](../../../../techniques/docs/multi-source-primary-input-provenance/TECHNIQUE.md),
  with [AOA-T-0041](../../../../techniques/docs/skill-marketplace-curation/TECHNIQUE.md)
  as the external companion; keep curation, boundary, upstream-readiness, and
  primary-input provenance separate from registry governance, routing policy,
  retrieval ranking, and graph semantics.
- Wave C landed [AOA-T-0044](../../../../techniques/history/versionable-session-transcripts/TECHNIQUE.md)
  and [AOA-T-0045](../../../../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md);
  [AOA-T-0026](../../../../techniques/history/session-capture-as-repo-artifact/TECHNIQUE.md)
  still owns session capture, persistence, and artifact-layer availability.

If future work needs exact wave execution order, use the preserved raw receipt.

## Implementation Rules

- external donors continue to use the normal external-import package in the external intake surface: `TECHNIQUE.md`, `notes/external-origin.md`, `notes/external-import-review.md`, `notes/second-context-adaptation.md`, one checklist, one minimal public-safe example, and the expected generated-surface sync
- cross-layer or internal-origin candidates here should use donor-appropriate origin and adaptation notes without forcing `external-*` note names where the donor is not actually an external-import case
- do not reopen `hold because overlap`, `needs layer incubation before distillation here`, or `substrate or architecture pattern, not yet a technique` lanes just to fill a wave
- do not treat a sibling repo's local behavior as technique authority;
  name the source owner, extraction route, and stop line only where it changes
  the candidate route
- do not draft a bundle until the candidate can name its atomic move, likely
  `domain`, primary `kind`, family posture, capability class, substrate,
  execution profile, risk posture, and standalone portability note
- shared generated surfaces should be synchronized only after a bundle draft is merge-ready, and only by the main agent

## Reopen Gate

Reopen a row from this cross-layer ledger only through one of these routes:

- inherited external rows reopen in the [External Candidate Ledger](../external-candidate-ledger/README.md)
  unless new independent cross-layer evidence changes the source boundary
- landed rows do not reopen as candidates; use bundle-local review if the
  landed technique contract drifts
- overlap, layer-incubation, and architecture rows can move only when their
  active ledger row and structured registry seed carry the full gate packet

Atom/topology gate:

- `atomic_move_note`: the one executable move being extracted
- `atomic_move_status`: named, landed, inherited, or still not named cleanly
- likely `domain` and primary `kind`
- likely family or reason no family is stable yet
- capability class, substrate, execution profile, and risk posture
- nearest landed technique, overlap watch, or layer-owner surface

Boundary/portability gate:

- `higher_law`: the source owner or AoA layer whose authority and stop lines
  matter for extraction
- `local_route`: why this row stays held, moves to incubation, enters import
  review, or remains closed as landed
- `bridge_stop_line`: what must not cross from source layer into technique canon
- what remains portable outside OS Abyss
- `aoa_only_context` or equivalent note for local integration context
- source owner and generated or indexed surfaces expected to change

If a row cannot name those fields, keep the row in its current verdict lane.
Do not update the generated registry directly; update the seed and validate the
derived index as evidence only.

## Hold Because Overlap

| candidate | donor or source layer | tentative domain | overlap note | next move |
|---|---|---|---|---|
| `progressive-skill-discovery` | `n-skills`, MCP Gateway Registry, repo-owned selector surfaces | `docs` | too close to `skill-marketplace-curation` plus the repo's current `pick -> inspect -> expand -> object use` discovery posture to count as a separate technique contract yet | reopen only if progressive disclosure itself becomes the distinct invariant rather than a restatement of curated discovery and selector behavior |
| `bounded-counterpart-edge-projection` | `aoa-kag`, `Tree-of-Sophia` bridge contracts | `docs` | too close to [AOA-T-0021](../../../../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) unless counterpart-specific non-identity semantics become a distinct reusable contract | reopen only if the counterpart edge can stay clearly narrower than generic bounded relation lift and carry a stable non-collapse contract of its own |

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
- the landed Wave A, Wave B, and Wave C families point at their technique
  bundles while inherited external placements stay in the external intake
  surface
- cross-layer links are provenance and boundary context unless a tracked
  bundle explicitly promotes one portable technique contract
