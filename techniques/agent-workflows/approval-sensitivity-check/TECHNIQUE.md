---
id: AOA-T-0088
name: approval-sensitivity-check
domain: agent-workflows
status: promoted
origin:
  project: aoa-skills
  path: skills/aoa-automation-opportunity-scan/SKILL.md + skills/aoa-automation-opportunity-scan/references/checkpoint-boundary.md
  note: Extracted from the aoa-automation-opportunity-scan skill where automation candidates that touch important surfaces or hidden authority must surface explicit checkpoint posture before any seed-ready claim can stay honest.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - automation
  - approval
  - checkpoint
  - risk
summary: Classify whether an automation candidate crosses approval, rollback, or self-change boundaries so checkpoint-required posture appears before any seed-ready claim becomes credible.
maturity_score: 3
rigor_level: bounded
reversibility: moderate
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-04-05
export_ready: true
relations:
  - type: complements
    target: AOA-T-0028
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

# approval-sensitivity-check

## Intent

Classify whether one automation candidate crosses approval, rollback, hidden
authority, or self-change boundaries so later seed or repair work must carry
explicit checkpoint posture instead of feeling like silent automation.

## When to use

- an automation candidate may mutate important system surfaces
- authority, approval, rollback, or health-check posture is unclear
- the route looks automation-worthy but could become unsafe without one explicit checkpoint verdict
- reviewers need to know whether the next honest move is still a seed candidate or a checkpoint-aware repair or proposal

## When not to use

- the route is clearly low-risk and read-only
- the real task is generic confirmation before mutation rather than automation-candidate review
- no recurring reviewed route exists yet
- the route still needs basic fit classification or donor extraction first

## Inputs

- one recurring automation candidate
- mutation surface and authority posture
- rollback and health-check posture
- secret and environment coupling
- any existing approval gate or its current absence

## Outputs

- one approval-sensitivity verdict
- one explicit `checkpoint_required` or `not_required` result
- one short explanation of the strongest checkpoint trigger
- one downgraded landing recommendation when the candidate is not honestly seed-ready yet

## Core procedure

1. Start from one bounded automation candidate rather than from generic risk language.
2. Ask whether the route mutates important surfaces, relies on hidden authority, behaves like self-change, or lacks visible rollback and health checks.
3. Mark `checkpoint_required` whenever approval posture or rollback discipline would be essential to keep the route reviewable.
4. Downgrade any `seed_ready` impulse when checkpoint posture is still missing or underdefined.
5. Distinguish low-risk read-only or preview-oriented candidates from approval-heavy or mutation-heavy candidates.
6. Name the next honest artifact as a checkpoint-aware repair route, reviewed seed proposal, or defer verdict when risk posture is still too open.
7. Preserve the difference between a checkpoint requirement and permission to execute.

## Contracts

- the check classifies one candidate's approval burden; it does not approve execution
- `checkpoint_required` is a boundary flag, not a scheduler or mutation grant
- hidden authority, missing rollback, and missing health checks all count against seed-ready posture
- later repair or approval systems still own the actual checkpoint stack

Relationship to adjacent techniques: unlike [AOA-T-0028](../confirmation-gated-mutating-action/TECHNIQUE.md), this technique does not govern a general confirmation seam before mutation; it only classifies whether an automation candidate has crossed into checkpoint-required territory. Unlike [AOA-T-0083](../checkpoint-bound-self-repair/TECHNIQUE.md), it does not build the full repair checkpoint packet; it only decides when automation-oriented lift must hand off to one.

## Risks

### Failure modes

- approval-heavy candidates are mislabeled as safe or seed-ready
- checkpoint posture is triggered too late because hidden authority was ignored
- checkpoint-required results are mistaken for permission to proceed

### Negative effects

- teams may automate mutation-heavy routes before rollback and health checks exist
- over-triggering checkpoint posture can make low-risk read-only candidates look scarier than they are
- reviewers may conflate approval sensitivity with general worthiness or priority

### Misuse patterns

- treating the check as a green light instead of a boundary classification
- using approval jargon to hide self-change or secret-heavy behavior
- widening the check into one full repair or governance framework
- skipping fit classification and donor evidence because the route feels urgent

### Detection signals

- mutation surface or authority posture is missing from the write-up
- rollback or health-check seams are absent on a meaningful candidate
- the next artifact still sounds like immediate implementation after `checkpoint_required`
- reviewers cannot tell whether the route is read-only, preview-only, or mutating

### Mitigations

- require explicit mutation and authority posture
- keep `checkpoint_required` separate from permission to execute
- preserve a downgrade path to repair, reviewed proposal, or defer
- keep full checkpoint packet construction in later explicit techniques

## Validation

Verify the technique by confirming that:
- one automation candidate is named explicitly
- mutation, authority, rollback, and health-check posture are visible
- `checkpoint_required` is explicit when the route is approval-heavy or self-changing
- low-risk read-only candidates can still remain outside checkpoint posture
- the result does not imply permission to execute

See `checks/approval-sensitivity-check-checklist.md`.

## Adaptation notes

What can vary across projects:
- the names of approval classes
- the rollback-anchor format
- the health-check surface
- whether the result is rendered in prose, YAML, or a small packet field

What should stay invariant:
- one candidate still gets one approval-sensitivity verdict
- hidden authority and missing rollback stay visible
- `checkpoint_required` remains boundary posture rather than permission
- low-risk read-only candidates remain distinguishable from self-changing ones

Project-shaped details that should not be treated as invariant:
- one approval bot or command
- one repo layout
- one scheduler stack
- one change-management doctrine

AoA adaptation example:
- common checkpoint triggers include important surface mutation, hidden or shifting authority, missing rollback marker, missing health check, and self-repair posture
- common resulting artifacts include a checkpoint-aware repair route, a reviewed seed proposal, or a defer verdict

## Public sanitization notes

This public bundle keeps only the reusable approval-boundary seam: one automation candidate, one explicit checkpoint-required verdict, and one reasoned downgrade path when mutation or hidden authority raises the burden. AoA approval commands, local ops doctrine, and runtime wrappers were reduced to adaptation examples or kept out of the invariant core.

## Example

See `examples/minimal-approval-sensitivity-check.md`.

## Checks

See `checks/approval-sensitivity-check-checklist.md`.

## Promotion history

- born in `aoa-skills` as the checkpoint-boundary seam inside `aoa-automation-opportunity-scan`
- extracted into `aoa-techniques` on 2026-04-05 as a bounded approval-sensitivity check over one automation candidate

## Future evolution

- keep generic confirmation seams separate through `AOA-T-0028`
- keep full self-repair checkpoint packets separate through `AOA-T-0083`
- add a second live context that uses the same automation-bound approval check outside the current AoA session-harvest automation lineage
