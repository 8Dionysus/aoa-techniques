---
id: AOA-T-0104
name: superseded-practice-obsolescence-route
domain: agent-workflows
kind: handoff
status: promoted
origin:
  project: aoa-techniques
  path: mechanics/method-growth/parts/obsolescence/README.md + mechanics/method-growth/PROVENANCE.md
  note: Extracted from the Method-growth obsolescence surface, with the AoA center pruning contract used as boundary reinforcement for explicit supersession, drop, merge, defer, or reanchor routes.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - method-growth
  - obsolescence
  - supersession
  - owner-boundary
summary: Route one adopted practice toward supersession, merge, reanchor, defer, drop, or deprecation review with owner receipt, retained lesson, and provenance intact.
maturity_score: 3
rigor_level: bounded
reversibility: moderate
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-05-03
export_ready: true
relations:
  - type: used_together_for
    target: AOA-T-0103
  - type: complements
    target: AOA-T-0090
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

# superseded-practice-obsolescence-route

## Intent

Route one adopted or shadowed practice that should not remain active as-is
toward supersession, merge, reanchor, defer, drop, or deprecation review while
preserving owner receipt, source evidence, rollback or quarantine posture, and
the smallest retained lesson.

## When to use

- a retention review says an adopted or shadowed practice should route toward
  obsolescence instead of staying active
- a replacement, merge target, reanchor target, defer reason, or drop reason is
  visible but has not been accepted by the object owner
- reviewers need to prevent silent deletion while also preventing stale active
  practice from lingering
- the owner needs a compact route packet before any local retirement,
  supersession, or deprecation action
- the useful lesson from a failed, merged, or superseded route should survive
  without turning into a memory object, proof verdict, skill, or route policy

## When not to use

- the practice has not passed a local adoption gate or shadow-use review yet
- the only question is whether the practice should remain active
- the owning surface has already performed and recorded local retirement
- the real issue is proof failure that belongs first in an evaluation surface
- the route should become a new technique, skill, playbook, memory object, role,
  runtime behavior, or routing rule rather than an obsolescence packet

## Inputs

- one adopted or shadowed practice under obsolescence pressure
- the current stage or status of that practice
- the owner surface that can accept or reject the route
- the reason the practice should not advance or remain active as-is
- a replacement, merge target, reanchor target, defer condition, or explicit
  note that no target is known
- source evidence and provenance for the practice and the obsolescence pressure
- rollback, quarantine, or restoration path if the route is later rejected
- the smallest retained lesson worth preserving after the route closes

## Outputs

- one obsolescence route packet
- one route label such as `supersede`, `merge`, `reanchor`, `defer`, `drop`, or
  `deprecation_review`
- the owner receipt target for any actual status change
- the source evidence that must not be erased
- the replacement, merge, reanchor, defer, or drop detail
- one retained lesson and any downstream hint for memory, stats, proof, skill,
  routing, or runtime owners
- an explicit stop-line that the packet does not delete, deprecate, erase
  evidence, write memory truth, prove failure, activate a skill, change routing,
  or mutate runtime behavior

## Core procedure

1. Start from one adopted or shadowed practice. Stop if several practices are
   fused together or if no adoption or shadow-use record exists.
2. Name the current stage, owner surface, and active behavior or artifact that
   would be affected if the practice stopped advancing as-is.
3. State the reason for obsolescence pressure: superseded, merged elsewhere,
   redundant, stale, harmful, unsupported, no longer owner-fit, or not worth
   retaining as active practice.
4. Choose one route label: `supersede`, `merge`, `reanchor`, `defer`, `drop`,
   or `deprecation_review`. If the evidence cannot support one label, return
   `defer`.
5. Name the replacement, merge target, reanchor target, defer condition, drop
   reason, or explicit absence of a target.
6. Preserve source evidence, the rollback or quarantine path, and the smallest
   retained lesson before any owner-local status change is considered.
7. Emit the route packet to the owner receipt target and stop before deletion,
   deprecation, proof, memory writeback, skill activation, route mutation, or
   runtime change.

## Contracts

- one route packet covers one adopted or shadowed practice and one owner receipt
  target
- obsolescence is not erasure
- a dropped route is not owner-local deletion
- a deprecation review packet is not the same as marking an object deprecated
- a retained lesson is not memory authority, proof authority, or final landing
- source evidence and rollback or quarantine posture must remain visible
- `defer` is required when current stage, owner target, reason, or retained
  lesson cannot be named

Relationship to adjacent techniques: this technique normally follows
[AOA-T-0103](../adopted-practice-retention-review/TECHNIQUE.md) when a
retention verdict routes toward obsolescence. Unlike
[AOA-T-0090](../nearest-wrong-target-rejection/TECHNIQUE.md), it does not only
reject an adjacent target; it emits the obsolescence route packet. Unlike
[AOA-T-0076](../owner-layer-triage/TECHNIQUE.md), it does not choose the first
owner layer for a reusable unit; it sends one already-owned practice toward a
reviewable owner receipt.

## Risks

### Failure modes

- the route packet is misread as permission to delete or mark deprecated
- source evidence disappears because the route is treated as cleanup
- reviewers choose `drop` when the honest route is merge, reanchor, or defer

### Negative effects

- too much obsolescence routing can burden low-risk practice cleanup
- stale active references may linger if the owner receipt is never reviewed
- a retained lesson can look stronger than the evidence that produced it

### Misuse patterns

- using obsolescence routing to avoid a retention review
- calling a route `supersede` without naming a real replacement
- treating a memory or stats hint as the final owner receipt
- using deprecation language as a proof verdict
- deleting support files before provenance and rollback are preserved

### Detection signals

- the route packet cannot name the current stage
- no owner receipt target is visible
- replacement, merge, reanchor, defer, or drop detail is vague
- retained lesson text is missing or reads like final authority
- the write-up contains actual deletion, deprecation, proof, skill, routing, or
  runtime actions

### Mitigations

- require one route label and one owner receipt target
- require preserved source evidence before any cleanup work
- name the rollback or quarantine path even when the route seems obvious
- route memory, stats, proof, skill, routing, and runtime consequences to their
  owners as downstream hints only
- use `defer` when the route cannot be made reviewable yet

## Validation

Verify the technique by confirming that:
- one adopted or shadowed practice is named
- current stage and owner receipt target are visible
- the reason it should not remain active as-is is explicit
- exactly one route label is chosen or the result is `defer`
- replacement, merge target, reanchor target, defer condition, drop reason, or
  explicit absence of target is stated
- source evidence, rollback or quarantine posture, and retained lesson remain
  visible
- no deletion, deprecation, proof, memory writeback, skill activation, route
  mutation, or runtime change is performed inside the packet

See `checks/superseded-practice-obsolescence-route-checklist.md`.

## Adaptation notes

What can vary across projects:
- route labels
- owner receipt format
- retention-review format that triggers the route
- how rollback, quarantine, or restoration paths are recorded
- whether the packet lives in Markdown, YAML, issue comments, or a review note

What should stay invariant:
- obsolescence routing stays separate from deletion and deprecation execution
- one packet covers one practice and one owner receipt target
- source evidence and retained lesson survive the route
- owner-local retirement truth belongs to the object owner
- downstream memory, stats, proof, skill, routing, and runtime effects remain
  hints until accepted by their owners

Project-shaped details that should not be treated as invariant:
- one repository map
- one Method-growth vocabulary
- one deprecation policy
- one memory or stats substrate
- one release process

AoA adaptation example:
- `aoa-techniques` can emit an obsolescence route packet when Method-growth
  retention says a technique-layer practice should stop being active as-is
- `Agents-of-Abyss` center pruning language helps keep the route explicit:
  name current stage, stop reason, owner receipt, and retained lesson
- actual owner-local retirement, proof, memory, skill, routing, and runtime
  changes remain outside this technique

## Public sanitization notes

This public bundle keeps only the portable route move: one practice, current
stage, owner receipt target, route label, source evidence, rollback or
quarantine posture, and retained lesson. Project-specific command wrappers,
local operator detail, and owner acceptance mechanics were reduced to
provenance and adaptation context.

## Example

See `examples/minimal-superseded-practice-obsolescence-route.md`.

## Checks

See `checks/superseded-practice-obsolescence-route-checklist.md`.

## Promotion history

- born in `aoa-techniques` Method-growth mechanics as part of the v0.7
  downstream adoption wave
- shaped against AoA center pruning language so obsolescence remains explicit
  without becoming erasure
- extracted into `aoa-techniques` on 2026-05-03 as one bounded owner-aware route
  packet rather than deletion, deprecation execution, proof, memory, skill,
  routing, or runtime authority

## Future evolution

- add one second live context where a non-Method-growth practice is merged,
  reanchored, deferred, or dropped by the same route packet
- consider typed obsolescence route fields only after several projects reuse
  the same output shape
- keep actual status flips and retirement procedures in owner-local surfaces
