---
id: AOA-T-0087
name: human-loop-to-seed-lift
domain: agent-workflows
status: promoted
origin:
  project: aoa-skills
  path: skills/aoa-automation-opportunity-scan/SKILL.md + skills/aoa-automation-opportunity-scan/references/playbook-seed-bridge.md
  note: Extracted from the aoa-automation-opportunity-scan skill where one recurring human loop is routed to the first honest landing as a skill, playbook seed, technique candidate, repair quest, or defer verdict instead of being forced directly into automation.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - automation
  - seed
  - routing
  - post-session
summary: Route one recurring human loop to the first honest automation-facing landing so seed-ready candidates become bounded skills or playbook seeds while unstable routes stay manual, repair-bound, or deferred.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-04-05
export_ready: true
relations:
  - type: complements
    target: AOA-T-0086
  - type: complements
    target: AOA-T-0076
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# human-loop-to-seed-lift

## Intent

Lift one recurring human loop into the first honest automation-facing landing
without skipping the difference between a bounded skill, a playbook seed, a
technique candidate, a repair quest, or a defer verdict.

## When to use

- a recurring reviewed route already has enough shape for a next-artifact decision
- the real question is where the route should land first rather than whether the fit matrix is strong
- a team needs one bounded owner-aware handoff instead of vague "automate this later" language
- schedule hints, if present, must remain advisory rather than becoming authority

## When not to use

- no reviewed recurring route exists yet
- the route still needs fit classification or approval-checkpoint analysis first
- the task is asking for live automation, hidden scheduling, or direct mutation authority
- the route is already a mature implementation artifact rather than a first landing decision

## Inputs

- one recurring reviewed route
- one readiness classification or equivalent evidence
- likely owner-layer options
- known schedule hints, if any
- known blockers that may force repair, defer, or checkpoint posture

## Outputs

- one first-honest-landing verdict
- one owner-layer recommendation
- one next-artifact type such as `skill`, `playbook_seed`, `technique_candidate`, `repair_quest`, or `defer`
- one rejected nearest-wrong target
- optional schedule hints kept as advisory only

## Core procedure

1. Start from one recurring reviewed human loop rather than from abstract automation aspiration.
2. Ask which first landing keeps the route smallest and most truthful.
3. Choose `skill` when the route is one bounded executable workflow.
4. Choose `playbook_seed` when the route is a recurring scenario composed of multiple skills, checkpoints, or scheduled rhythms.
5. Choose `technique_candidate` when the reusable core is a stable practice behind several possible automations.
6. Choose `repair_quest` or `defer` when missing proof, missing boundaries, or hidden authority still block honest lift.
7. Record the nearest wrong target so promotion pressure stays explicit and reviewers can see what was intentionally rejected.

## Contracts

- the lift chooses the first honest landing; it does not grant live automation authority
- schedule hints remain hints rather than runtime truth
- one bounded skill must not hide a recurring scenario seed
- repair or defer verdicts remain honorable outcomes rather than failures of ambition

Relationship to adjacent techniques: unlike [AOA-T-0086](../automation-fit-matrix/TECHNIQUE.md), this technique does not classify the route across readiness rows; it starts after enough evidence exists to choose a first landing. Unlike [AOA-T-0076](../owner-layer-triage/TECHNIQUE.md), it is narrower and more automation-facing: it chooses the first honest lift from a human loop into an automation-oriented artifact rather than placing any reusable unit into any owner layer.

## Risks

### Failure modes

- the route is forced into a skill when it really wants a scenario seed or defer verdict
- schedule hints quietly become authority
- the rejected nearest-wrong target is omitted, hiding classification pressure

### Negative effects

- teams may create brittle skills where a broader playbook seed was needed
- too much optimism can move unstable work into seed lanes before repair or checkpoint posture exists
- defers can look like indecision if the bundle does not explain why smaller is more honest

### Misuse patterns

- treating `playbook_seed` as a synonym for "automation exists now"
- using one landing verdict as proof that implementation should begin immediately
- hiding unresolved blockers behind a positive owner-layer label
- widening the lift into a generic roadmap or prioritization system

### Detection signals

- the route cannot name one current manual loop
- schedule hints are phrased like commands or fixed policy
- reviewers cannot tell why one landing was chosen over another
- the nearest wrong target is missing even though obvious alternatives existed

### Mitigations

- require one explicit current manual loop first
- keep schedule hints advisory only
- require one rejected nearest-wrong target
- preserve repair and defer as honest outcomes

## Validation

Verify the technique by confirming that:
- one recurring reviewed loop is named
- the first landing stays smaller than a full implementation
- owner-layer and next-artifact posture are explicit
- schedule hints remain advisory only
- the nearest wrong target is visible when classification pressure exists

See `checks/human-loop-to-seed-lift-checklist.md`.

## Adaptation notes

What can vary across projects:
- the names of owner layers
- the names of next-artifact types
- whether schedule hints are expressed in prose, fields, or follow-up notes
- which automation surfaces count as local skills versus scenario seeds

What should stay invariant:
- one human loop still gets one first-honest-landing verdict
- schedule hints remain advisory
- smaller landings beat premature implementation
- repair and defer remain acceptable outputs

Project-shaped details that should not be treated as invariant:
- one repo map
- one scheduler stack
- one skill registry
- one prioritization board

AoA adaptation example:
- first landings commonly include `aoa-skills`, `aoa-playbooks`, `aoa-techniques`, or a repair/defer lane
- a recurring session closeout route often lands as a playbook seed before any scheduler or runtime implementation exists

## Public sanitization notes

This public bundle keeps only the reusable first-landing seam: one recurring human loop, one owner-aware next-artifact verdict, and one rejected nearest wrong target. AoA repo names, specific scheduler ideas, and project-local queue shapes were reduced to adaptation examples or kept out of the invariant core.

## Example

See `examples/minimal-human-loop-to-seed-lift.md`.

## Checks

See `checks/human-loop-to-seed-lift-checklist.md`.

## Promotion history

- born in `aoa-skills` as the first-landing bridge inside `aoa-automation-opportunity-scan`
- extracted into `aoa-techniques` on 2026-04-05 as a bounded lift from recurring human work into a seed-oriented next artifact

## Future evolution

- keep fit classification separate through `AOA-T-0086`
- keep generic owner placement separate through `AOA-T-0076`
- add a second live context that uses the same first-honest-landing seam outside the current AoA session-harvest automation lineage
