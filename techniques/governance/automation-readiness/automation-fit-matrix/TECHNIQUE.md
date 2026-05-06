---
id: AOA-T-0086
name: automation-fit-matrix
domain: agent-workflows
kind: assessment
status: promoted
origin:
  project: aoa-skills
  path: skills/aoa-automation-opportunity-scan/SKILL.md + skills/aoa-automation-opportunity-scan/references/automation-fit-matrix.md
  note: Extracted from the aoa-automation-opportunity-scan skill where recurring manual routes are classified across repeat signal, determinism, proof posture, reversibility, and approval sensitivity before any seed-ready claim is made.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - automation
  - classification
  - fit-matrix
  - reviewed-work
summary: Classify one recurring manual route across repeat signal, determinism, proof posture, reversibility, and approval sensitivity so automation desire becomes a bounded verdict rather than vague enthusiasm.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-04-05
export_ready: true
relations:
  - type: complements
    target: AOA-T-0087
  - type: complements
    target: AOA-T-0088
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# automation-fit-matrix

## Intent

Classify one recurring manual route with a small automation-fit matrix so the
result says whether the route is honestly ready for automation-oriented lift,
still blocked, or not worth forcing yet.

## When to use

- a reviewed session or recurring project slice exposes a repeated manual route
- the team needs an explicit read on repeat signal, friction, determinism, and proof posture before calling the route automation-ready
- the route may be a good automation candidate, but enthusiasm still needs one bounded classification object
- reviewers want a small matrix instead of one opaque confidence score or a vague "this should be automated" statement

## When not to use

- the route only happened once and still looks exploratory
- the real task is choosing the final owner layer or next artifact rather than classifying fit
- the route is mostly creative synthesis with no stable trigger or output contract
- the matrix would be used as sovereign routing or approval authority

## Inputs

- one reviewed route description
- repeat evidence across sessions, windows, or artifacts
- current friction signals
- current trigger, input, and output posture
- current proof, dry-run, reversibility, secret-coupling, and approval posture when known

## Outputs

- one bounded automation-fit matrix
- one explicit verdict such as `seed_ready`, `checkpoint_required`, or `not_now`
- one short explanation for the strongest blocking or enabling factors
- one reminder that the matrix is descriptive rather than sovereign

## Core procedure

1. Start from one reviewed recurring route rather than from abstract automation desire.
2. Score the route with small explicit rows: frequency, friction, determinism, input clarity, output clarity, proof surface, dry-run posture, reversibility, secret coupling, and approval sensitivity.
3. Keep each row descriptive and evidence-backed instead of numeric and fake-precise.
4. Name the strongest enabling signals and the strongest blockers.
5. Emit `seed_ready` only when repeat signal, rule stability, proof posture, and bounded reversibility are all honestly present.
6. Emit `checkpoint_required` when the route could be automation-worthy but authority, mutation, or rollback posture raises the burden.
7. Emit `not_now` when the route is still too unstable, secret-heavy, or vague to justify automation lift.

## Contracts

- the matrix classifies one route; it does not create automation authority
- row descriptions stay evidence-backed and small
- verdicts remain bounded to readiness posture, not final implementation or routing doctrine
- a strong fit does not remove the need for later owner-layer or checkpoint decisions

Relationship to adjacent techniques: unlike [AOA-T-0087](../human-loop-to-seed-lift/TECHNIQUE.md), this technique does not choose the first honest landing or next artifact; it only classifies whether the route has enough shape to lift. Unlike [AOA-T-0088](../approval-sensitivity-check/TECHNIQUE.md), it does not own the checkpoint or approval analysis itself; it only includes approval sensitivity as one row in the matrix.

## Risks

### Failure modes

- the matrix hides missing evidence behind confident labels
- row meanings drift into one opaque score
- verdicts are emitted even when key rows are unknown

### Negative effects

- teams may over-trust a clean-looking matrix and skip later boundary checks
- fake precision can make unstable routes look more mature than they are
- low-value repetitive work can receive too much automation pressure

### Misuse patterns

- using the matrix as final routing authority
- calling one exciting session a repeat signal
- hiding secret-heavy or approval-heavy work behind generalized row labels
- collapsing multiple different routes into one matrix

### Detection signals

- evidence refs for repeat signal or proof posture are missing
- the matrix cannot name one current manual route
- verdict language sounds like implementation approval instead of readiness posture
- reviewers disagree on what one row actually means

### Mitigations

- keep one matrix per route
- keep row vocabulary descriptive and small
- require explicit blockers when key rows are weak or unknown
- hand off owner and checkpoint questions to later explicit seams

## Validation

Verify the technique by confirming that:
- one reviewed recurring route is named explicitly
- each row is evidence-backed or honestly marked unknown
- the verdict matches the strongest blockers and enabling factors
- approval sensitivity and reversibility remain visible
- the matrix does not pretend to be routing or execution authority

See `checks/automation-fit-matrix-checklist.md`.

## Adaptation notes

What can vary across projects:
- the exact row wording
- the names of verdict labels
- how repeat evidence is referenced
- whether the matrix is written as markdown, YAML, or a small table

What should stay invariant:
- one route stays one matrix
- repeat signal, determinism, proof posture, reversibility, and approval sensitivity remain visible
- verdicts stay descriptive rather than sovereign
- the matrix remains smaller than any later seed, skill, or playbook artifact

Project-shaped details that should not be treated as invariant:
- one repo-specific automation queue
- one score system
- one scheduler vocabulary
- one local environment or secret model

AoA adaptation example:
- common rows include repeat signal, friction, determinism, input and output clarity, proof surface, dry run, reversibility, secret coupling, and approval sensitivity
- common verdicts are `seed_ready`, `checkpoint_required`, and `not_now`

## Public sanitization notes

This public bundle keeps only the reusable route-classification seam: one small matrix over repeat signal, friction, determinism, proof posture, reversibility, and approval sensitivity. AoA repo names, local scheduler language, and project-specific automation queues were reduced to adaptation examples or kept out of the invariant core.

## Example

See `examples/minimal-automation-fit-matrix.md`.

## Checks

See `checks/automation-fit-matrix-checklist.md`.

## Promotion history

- born in `aoa-skills` as the classification spine inside `aoa-automation-opportunity-scan`
- extracted into `aoa-techniques` on 2026-04-05 as a bounded recurring-route fit matrix

## Future evolution

- keep first-landing choice separate through `AOA-T-0087`
- keep approval and checkpoint posture separate through `AOA-T-0088`
- add a second live context that uses the same small fit matrix outside the current AoA session-harvest automation lineage
