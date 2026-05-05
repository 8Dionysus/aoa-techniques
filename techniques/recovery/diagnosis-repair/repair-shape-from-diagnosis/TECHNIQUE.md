---
id: AOA-T-0082
name: repair-shape-from-diagnosis
domain: agent-workflows
kind: recovery
status: promoted
origin:
  project: aoa-skills
  path: skills/aoa-session-self-repair/SKILL.md + skills/aoa-session-self-repair/techniques.yaml
  note: Extracted from the aoa-session-self-repair skill where a reviewed diagnosis packet is converted into the smallest honest repair packet instead of one vague self-improvement request.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - repair
  - diagnosis
  - bounded-change
  - post-session
summary: Turn a reviewed diagnosis packet into the smallest honest repair shape so the next artifact stays bounded, owner-aware, and smaller than a scenario rollout.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-04-05
export_ready: true
relations:
  - type: complements
    target: AOA-T-0081
  - type: complements
    target: AOA-T-0083
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# repair-shape-from-diagnosis

## Intent

Turn a reviewed diagnosis packet into the smallest honest repair shape so the
next step stays bounded and explicit instead of becoming vague self-improvement
rhetoric or a hidden scenario rollout.

## When to use

- a reviewed diagnosis already exists
- the next honest move is a bounded repair packet rather than another diagnosis pass
- the repair still fits inside one bounded owner-facing unit
- reviewers need one explicit target artifact or repair quest instead of general aspiration

## When not to use

- diagnosis does not exist yet
- the repair is large enough to be a playbook or broader rollout
- the request mainly wants the system to "improve itself" without a bounded target
- the real issue is checkpoint posture rather than the repair shape itself

## Inputs

- one reviewed diagnosis packet
- likely owner targets or owner-layer hints
- known validation surfaces
- current risk and approval posture if already visible

## Outputs

- one smallest honest repair shape
- one primary owner target
- one target artifact class or repair quest shape
- one validation plan
- one stop or escalation cue if the repair would widen

## Core procedure

1. Start from a reviewed diagnosis packet rather than from aspiration.
2. Restate the actual bounded problem the repair should address.
3. Choose the smallest owner-facing artifact that can honestly address the diagnosis.
4. Reject shapes that smuggle a playbook-scale rollout into one "repair packet".
5. Name the validation plan that proves the repair worked.
6. Preserve escalation when the repair widens past one bounded unit.
7. Hand checkpoint posture to a later seam rather than hiding it implicitly.

## Contracts

- diagnosis is a prerequisite
- the chosen repair shape stays smaller than a scenario rollout
- one primary owner target remains explicit
- validation remains part of the repair shape, not a later surprise
- escalation remains valid when the repair cannot stay bounded

Relationship to adjacent techniques: unlike [AOA-T-0081](../diagnosis-from-reviewed-evidence/TECHNIQUE.md), this technique does not explain symptoms and probable causes; it starts after diagnosis exists. Unlike [AOA-T-0083](../checkpoint-bound-self-repair/TECHNIQUE.md), it does not own the checkpoint stack itself; it chooses the repair shape that later checkpoint posture should govern.

## Risks

### Failure modes

- the chosen repair shape is larger than the diagnosis justifies
- a vague "improve the system" request is treated as if it were bounded
- owner target and validation plan remain implicit

### Negative effects

- too much repair ceremony can slow obvious small fixes
- too-small repair shapes can hide a wider scenario problem
- teams may skip escalation because the label "repair packet" sounds tidy

### Misuse patterns

- choosing a playbook-scale rollout as if it were one repair packet
- using repair shaping before diagnosis exists
- confusing repair shape with checkpoint posture
- turning repair shaping into general roadmap planning

### Detection signals

- the proposed artifact is much larger than the diagnosis packet
- validation is missing or generic
- the same repair packet keeps reopening because the real issue was wider
- reviewers cannot explain why this is the smallest honest shape

### Mitigations

- require diagnosis first
- name one primary owner target explicitly
- preserve escalation when the repair widens
- keep checkpoint posture explicit as a separate seam

## Validation

Verify the technique by confirming that:
- a reviewed diagnosis exists
- the chosen repair shape is the smallest honest shape
- one primary owner target is explicit
- validation and escalation cues are named
- the output stays smaller than a scenario rollout

See `checks/repair-shape-from-diagnosis-checklist.md`.

## Adaptation notes

What can vary across projects:
- the names of owner targets
- the artifact classes used for the repair
- how validation plans are recorded
- whether escalation becomes a ticket, quest, or review note

What should stay invariant:
- diagnosis comes first
- the repair shape stays bounded
- owner target and validation plan stay explicit
- escalation remains valid when widening is honest

Project-shaped details that should not be treated as invariant:
- one issue template
- one repo naming convention
- one rollout board
- one approval ladder

AoA adaptation example:
- common repair shapes include a bounded skill delta, technique delta, playbook correction note, or repair quest
- owner targets often map toward `aoa-skills`, `aoa-techniques`, `aoa-evals`, or `aoa-agents`

## Public sanitization notes

This public bundle keeps only the reusable repair-shaping seam: start from reviewed diagnosis, choose the smallest honest owner-facing repair artifact, name validation, and preserve escalation when needed. AoA repo names, local issue systems, and skill wrappers were reduced to adaptation examples or kept out of the invariant core.

## Example

See `examples/minimal-repair-shape-from-diagnosis.md`.

## Checks

See `checks/repair-shape-from-diagnosis-checklist.md`.

## Promotion history

- born in `aoa-skills` as the repair-shaping half of `aoa-session-self-repair`
- extracted into `aoa-techniques` on 2026-04-05 as a bounded repair-shaping workflow

## Future evolution

- keep diagnosis separate through `AOA-T-0081`
- keep checkpoint posture separate through `AOA-T-0083`
- add a second live context that uses the same bounded repair-shaping seam outside the current AoA session-harvest lineage
