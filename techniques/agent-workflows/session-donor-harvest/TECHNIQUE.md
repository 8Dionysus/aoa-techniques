---
id: AOA-T-0075
name: session-donor-harvest
domain: agent-workflows
status: promoted
origin:
  project: aoa-skills
  path: skills/aoa-session-donor-harvest/SKILL.md + skills/aoa-session-donor-harvest/techniques.yaml
  note: Extracted from the aoa-session-donor-harvest skill where reviewed session artifacts are distilled into bounded donor candidates before owner-layer routing and later promotion.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - reviewed-session
  - donor
  - harvest
  - post-session
summary: Distill a reviewed session artifact into a bounded donor pack of reusable units so candidate practice, workflow, and scenario objects can be evaluated without turning session history into memory or forcing promotion.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-04-05
export_ready: true
relations:
  - type: complements
    target: AOA-T-0076
  - type: complements
    target: AOA-T-0044
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# session-donor-harvest

## Intent

Turn one reviewed session artifact into a bounded donor pack of reusable candidates so later placement, drafting, and promotion work starts from named units with visible evidence anchors instead of from vague memory of the session.

## When to use

- a session transcript, compaction note, review packet, or bounded recap already exists and has been reviewed
- the main question is which reusable units emerged from the session rather than merely what happened
- several candidate units may coexist and should be split before any owner-layer verdict or promotion choice
- later work needs one donor pack with evidence anchors, candidate kinds, and defer or hold posture
- the workflow must stay post-session and reviewable rather than reopen live execution

## When not to use

- the session is still live, unreviewed, or only partially captured
- the real need is raw session capture, transcript export, replay packaging, or local indexing
- the work already has one isolated repeated quest unit and only needs final promotion triage
- the artifact is only a progress log, emotional recap, or theme cloud with no bounded reusable unit
- the intended first output is a derivative routing or graph surface rather than a source-owned reusable object

## Inputs

- one reviewed session artifact
- session goal and closure state
- repeat or reuse signals visible in the artifact
- explicit uncertainty notes and boundary risks
- desired donor-pack posture such as classify-only, draft-stub, or patch-ready follow-through

## Outputs

- one bounded donor harvest pack
- one candidate record for each kept reusable unit
- visible evidence anchors for every kept candidate
- one reuse-kind hint for each kept candidate such as pattern, mechanic, utility, law, proof, recall, or route
- one defer, drop, or hold list for material that should not be promoted yet

## Core procedure

1. Start from a reviewed session artifact rather than from transient chat memory.
2. Scan for reusable units, not topics. Prefer explicit moves, laws, checklists, structures, routes, or proof patterns.
3. Split merged candidate clusters until each kept record names one reusable unit.
4. Reject theme-only repetition, broad "good idea" residue, and aesthetic resonance when no bounded reusable unit survives.
5. Capture evidence anchors for each kept candidate so later owner placement can cite where the unit actually appears in the reviewed artifact.
6. Mark the candidate with a reuse-kind hint such as pattern, mechanic, utility, law, proof, recall, or route.
7. Keep the donor pack smaller than a promotion verdict. The pack should preserve candidate units and evidence without pretending the owner decision is already closed.
8. Record defer or hold outcomes for weak, mixed, or under-evidenced candidates instead of forcing every unit into canon.
9. Hand each kept candidate to an owner-layer placement pass such as `AOA-T-0076 owner-layer-triage`.
10. Draft the smallest next artifact only after one primary owner shape is explicit.

## Contracts

- invocation is explicit and post-session
- the technique starts from a reviewed artifact rather than raw live session state
- one candidate record names one reusable unit
- every kept candidate keeps visible evidence anchors
- the donor pack stays smaller than owner placement, promotion verdict, or writeback
- session history remains source evidence, not memory canon or instruction authority
- derivative routing or graph surfaces do not become first-authoring targets for source-owned meaning

Relationship to adjacent techniques: unlike [AOA-T-0044](../../history/versionable-session-transcripts/TECHNIQUE.md), this technique assumes the transcript or equivalent reviewed artifact already exists and only owns donor extraction after review. Unlike [AOA-T-0076](../owner-layer-triage/TECHNIQUE.md), it does not decide the final primary owner layer for each candidate. It should also stay narrower than final quest promotion triage because it can emit several candidate units from one session instead of one promotion verdict.

## Risks

### Failure modes

- mixed clusters survive and later owner placement has to guess what the unit really is
- the donor pack becomes a noisy session summary instead of a reusable-unit pack
- candidates lose their evidence anchors and later drafting turns into memory or interpretation drift

### Negative effects

- over-harvesting can create too many thin candidates from one session
- donor extraction adds review overhead when the honest outcome should have been `hold`
- teams may confuse a rich donor pack with proof that promotion should already happen

### Misuse patterns

- using the technique for live sessions that still need execution or review
- relabeling transcript packaging or local indexing as donor harvest
- treating every repeated topic as a reusable unit
- letting derivative routing, graph, or memory surfaces become the first destination

### Detection signals

- candidate names describe topics instead of reusable units
- evidence anchors are missing or too vague to reopen the source artifact
- the donor pack reads like one long recap instead of several bounded candidate records
- reviewers cannot explain why a weak item was not deferred or held

### Mitigations

- split candidates aggressively until each one names one reusable unit
- require an evidence anchor for every kept candidate
- preserve `defer` and `hold` as valid outcomes
- keep owner placement and promotion as explicit later seams instead of hiding them inside the donor pack

## Validation

Verify the technique by confirming that:
- the source artifact is reviewed and bounded
- each kept candidate names one reusable unit rather than one topic cluster
- each kept candidate preserves at least one evidence anchor
- the donor pack remains smaller than owner placement or promotion verdict
- defer or hold outcomes remain available for weak candidates
- the bundle is not being used for capture, transcript export, replay packaging, or indexing

See `checks/session-donor-harvest-checklist.md`.

## Adaptation notes

What can vary across projects:
- the reviewed session artifact format
- how evidence anchors are recorded
- the donor-pack schema
- the names of reuse kinds or later owner layers
- whether the next step is classify-only, draft-stub, or patch-ready

What should stay invariant:
- donor harvest starts after review
- candidate units stay bounded and split
- evidence anchors stay visible
- the donor pack remains smaller than owner placement and promotion

Project-shaped details that should not be treated as invariant:
- one compaction-note template
- one transcript export tool
- one repo naming scheme for next artifacts
- one ecosystem's owner-layer map

AoA adaptation example:
- practice canon usually maps to `aoa-techniques`
- bounded executable workflow usually maps to `aoa-skills`
- multi-step recurring scenario usually maps to `aoa-playbooks`
- proof or verdict posture usually maps to `aoa-evals`
- recall or writeback posture usually maps to `aoa-memo`
- role or actor-boundary posture usually maps to `aoa-agents`

## Public sanitization notes

This public bundle keeps only the reusable post-session donor-extraction contract: start from a reviewed session artifact, split reusable units, preserve evidence anchors, and emit a bounded donor pack. AoA repo names, local pack formats, runtime invocation wrappers, and later promotion mechanics were reduced to adaptation examples or kept out of the invariant core.

## Example

See `examples/minimal-session-donor-harvest.md`.

## Checks

See `checks/session-donor-harvest-checklist.md`.

## Promotion history

- born in `aoa-skills` as part of `aoa-session-donor-harvest`
- extracted into `aoa-techniques` on 2026-04-05 as a bounded post-session donor-extraction workflow

## Future evolution

- keep owner placement separate through `AOA-T-0076` instead of widening this bundle into full routing doctrine
- add a second live context that uses the same donor-pack boundary outside the current AoA session-harvest lineage
- keep transcript packaging, replay, indexing, and final promotion verdicts in sibling techniques rather than reopening them here
