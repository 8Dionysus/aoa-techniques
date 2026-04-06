---
id: AOA-T-0084
name: progression-evidence-lift
domain: agent-workflows
status: promoted
origin:
  project: aoa-skills
  path: skills/aoa-session-progression-lift/SKILL.md + skills/aoa-session-progression-lift/references/progression-axes.md
  note: Extracted from the aoa-session-progression-lift skill where reviewed session evidence becomes a bounded multi-axis progression delta instead of one sovereign score.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - progression
  - evidence
  - post-session
  - mastery
summary: Lift reviewed session evidence into a bounded multi-axis progression delta with explicit verdicts and small unlock hints so growth stays descriptive and evidence-backed instead of collapsing into one score.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-04-05
export_ready: true
relations:
  - type: complements
    target: AOA-T-0085
  - type: complements
    target: AOA-T-0075
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# progression-evidence-lift

## Intent

Lift reviewed session evidence into a bounded multi-axis progression delta so
growth stays legible and evidence-backed without inventing one universal score
or hidden routing authority.

## When to use

- a reviewed session produced meaningful mastery evidence
- the route needs progression legibility without mutating role or owner truth
- the output should stay small, qualitative, and multi-axis
- reviewers need explicit verdicts such as advance, hold, reanchor, or downgrade

## When not to use

- there is no reviewed evidence
- the request wants one universal power number
- progression language is being used as policy or routing authority
- the route is trying to grant rights or status without evidence

## Inputs

- one reviewed session artifact or harvest packet
- named evidence refs
- any current progression baseline if it exists
- relevant role or cohort context if needed

## Outputs

- one bounded `PROGRESSION_DELTA`
- one qualitative movement note per meaningful axis
- one verdict such as advance, hold, reanchor, or downgrade
- one small unlock hint set only when evidence supports it
- one explicit place for negative or zero movement

## Core procedure

1. Start from reviewed evidence refs rather than from mood.
2. Assess movement qualitatively across a bounded axis set.
3. Preserve zero or negative movement when it is more honest than forced progress.
4. Emit one verdict that matches the evidence rather than one inflated celebration.
5. Keep unlock hints small and explicit.
6. Reject universal scores and sovereign rank authority.

## Contracts

- progression remains evidence-backed
- movement stays multi-axis rather than one-score
- verdicts remain descriptive, not sovereign
- unlock hints stay small and reviewable
- progression does not replace owner-layer truth or routing authority

Relationship to adjacent techniques: unlike [AOA-T-0075](../session-donor-harvest/TECHNIQUE.md), this technique does not extract reusable units from a reviewed session artifact; it only reflects mastery movement from already reviewed evidence. Unlike [AOA-T-0085](../multi-axis-quest-overlay/TECHNIQUE.md), it owns the progression delta itself rather than the optional quest- or RPG-shaped reflection layered over that delta.

## Risks

### Failure modes

- movement is invented from vibe instead of evidence
- several axes are flattened into one total score
- unlock hints become hidden authority grants

### Negative effects

- forced positive motion can make review less honest
- progression overlays can distract from owner truth if they overgrow
- teams may confuse a descriptive verdict with rank or permission

### Misuse patterns

- using progression to decide what repo or skill should run next
- granting status or authority through flavor instead of evidence
- treating every reviewed session as if it must show progress
- collapsing multi-axis movement into one celebratory metric

### Detection signals

- no evidence refs support meaningful movement claims
- the output contains one total score or rank number
- hold, reanchor, or downgrade are absent even when evidence is mixed
- unlock hints read like permissions rather than reflections

### Mitigations

- require reviewed evidence for meaningful claims
- preserve zero and negative movement
- keep unlock hints explicitly small
- reject universal scoring and authority language

## Validation

Verify the technique by confirming that:
- meaningful axis claims cite reviewed evidence
- the output stays multi-axis
- the verdict matches the evidence
- zero or negative movement remains possible
- no universal score or hidden policy authority appears

See `checks/progression-evidence-lift-checklist.md`.

## Adaptation notes

What can vary across projects:
- the axis names
- the verdict vocabulary
- whether cohort or role context is included
- the rendering format for unlock hints

What should stay invariant:
- progression starts from reviewed evidence
- movement stays multi-axis
- verdicts remain descriptive
- universal scores remain out of scope

Project-shaped details that should not be treated as invariant:
- one game-like progression ladder
- one role hierarchy
- one unlock taxonomy
- one status board

AoA adaptation example:
- common axes include `boundary_integrity`, `execution_reliability`, `change_legibility`, `review_sharpness`, `proof_discipline`, `provenance_hygiene`, and `deep_readiness`
- unlock hints may later help session-harvest planning, but they do not replace owner truth

## Public sanitization notes

This public bundle keeps only the reusable progression-evidence seam: reviewed evidence, bounded multi-axis movement, explicit verdicts, and small unlock hints. AoA role language, local status ladders, and skill wrappers were reduced to adaptation examples or kept out of the invariant core.

## Example

See `examples/minimal-progression-evidence-lift.md`.

## Checks

See `checks/progression-evidence-lift-checklist.md`.

## Promotion history

- born in `aoa-skills` as the evidence-lift half of `aoa-session-progression-lift`
- extracted into `aoa-techniques` on 2026-04-05 as a bounded multi-axis progression workflow

## Future evolution

- keep quest- or RPG-shaped reflection separate through `AOA-T-0085`
- keep owner truth and routing authority outside this bundle
- add a second live context that uses the same multi-axis progression seam outside the current AoA session-harvest lineage
