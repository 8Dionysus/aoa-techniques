---
id: AOA-T-0080
name: session-drift-taxonomy
domain: agent-workflows
status: promoted
origin:
  project: aoa-skills
  path: skills/aoa-session-self-diagnose/SKILL.md + skills/aoa-session-self-diagnose/techniques.yaml
  note: Extracted from the aoa-session-self-diagnose skill where repeated post-session friction is first classified into bounded drift types before a diagnosis packet names probable causes or repair shapes.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - diagnosis
  - taxonomy
  - drift
  - post-session
summary: Classify repeated post-session friction into bounded drift types so diagnosis can say what kind of problem is present before it claims one probable cause, owner hint, or repair shape.
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
    target: AOA-T-0076
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# session-drift-taxonomy

## Intent

Classify repeated post-session friction into bounded drift types so a later
diagnosis pass can describe what kind of problem is present before claiming one
probable cause or repair direction.

## When to use

- the session is reviewed and several friction signals survived it
- the next honest move is diagnosis rather than immediate repair
- the same class of confusion, contradiction, or proof blur may be recurring
- reviewers need a bounded vocabulary before they trust a diagnosis packet

## When not to use

- the session is still live or unreviewed
- the issue is already fully diagnosed
- the route only needs one repair packet or one final promotion verdict
- the friction is too weak or singular to justify structural classification

## Inputs

- one reviewed session artifact or harvest packet
- observed frictions, failures, contradictions, or proof gaps
- any repeated blockers or earlier related evidence

## Outputs

- one bounded drift-type list
- one description of what each drift type means in the current case
- one explicit separation between drift type and probable cause
- one reminder that owner hints and repair shapes come later

## Core procedure

1. Start from reviewed friction evidence rather than live debugging.
2. Separate raw symptoms from the drift category they suggest.
3. Classify only bounded drift types such as boundary drift, proof debt, role leakage, memory contamination, route collapse, compaction damage, or repeated blocker patterns.
4. Reject vague mood labels that do not help later diagnosis.
5. Preserve mixed or uncertain classifications when the evidence does not justify one clean label.
6. Hand the bounded taxonomy forward to a diagnosis pass instead of pretending taxonomy alone solved the problem.

## Contracts

- taxonomy is read-only
- drift type is not the same thing as probable cause
- one odd anecdote is not enough for structural classification
- bounded labels should help later diagnosis rather than replace it
- the taxonomy stays smaller than a full diagnosis packet

Relationship to adjacent techniques: unlike [AOA-T-0081](../diagnosis-from-reviewed-evidence/TECHNIQUE.md), this technique does not claim probable causes, owner hints, or repair shapes over the whole packet; it only classifies the type of drift. Unlike [AOA-T-0076](../owner-layer-triage/TECHNIQUE.md), it does not place one reusable unit into one owner layer.

## Risks

### Failure modes

- vague labels replace real classification
- drift type is confused with probable cause
- one anecdote gets inflated into a systemic taxonomy verdict

### Negative effects

- over-classification can make weak evidence look stronger than it is
- taxonomy jargon can obscure the real session evidence
- teams may reuse one favorite label for every friction pattern

### Misuse patterns

- using taxonomy as a substitute for diagnosis
- inventing new labels when a bounded existing type already fits
- treating one temporary inconvenience as structural drift
- using taxonomy to blame one owner layer prematurely

### Detection signals

- classifications sound like vibes instead of bounded drift types
- reviewers cannot tell the difference between symptom, drift type, and cause
- the taxonomy verdict is more confident than the evidence supports
- owner hints appear before the taxonomy pass is done

### Mitigations

- keep drift labels bounded and reusable
- separate taxonomy from probable-cause language
- preserve mixed or uncertain labels when needed
- hand off to diagnosis instead of pretending taxonomy is enough

## Validation

Verify the technique by confirming that:
- the source evidence is reviewed
- drift labels stay bounded and reusable
- symptom, drift type, and probable cause remain distinct
- mixed or uncertain classifications remain possible
- the output stays smaller than a full diagnosis packet

See `checks/session-drift-taxonomy-checklist.md`.

## Adaptation notes

What can vary across projects:
- the exact drift labels
- how strong repeated evidence must be before classification
- whether severity tags accompany the taxonomy
- how mixed classifications are represented

What should stay invariant:
- taxonomy starts after review
- drift type stays distinct from cause
- uncertainty remains available
- the taxonomy remains smaller than the full diagnosis pass

Project-shaped details that should not be treated as invariant:
- one team's favorite label set
- one escalation ladder
- one owner map
- one reporting schema

AoA adaptation example:
- frequent labels include `boundary_drift`, `proof_debt`, `role_leakage`, `route_collapse`, and `compaction_damage`
- owner hints and repair shapes remain later seams rather than part of the taxonomy itself

## Public sanitization notes

This public bundle keeps only the reusable taxonomy seam: reviewed friction, bounded drift labels, explicit uncertainty, and a clear separation from probable cause. AoA repo naming, local severity conventions, and skill invocation wrappers were reduced to adaptation examples or kept out of the invariant core.

## Example

See `examples/minimal-session-drift-taxonomy.md`.

## Checks

See `checks/session-drift-taxonomy-checklist.md`.

## Promotion history

- born in `aoa-skills` as the taxonomy half of `aoa-session-self-diagnose`
- extracted into `aoa-techniques` on 2026-04-05 as a bounded reviewed-session drift-classification technique

## Future evolution

- keep full diagnosis separate through `AOA-T-0081`
- keep owner verdicts and repair planning outside this bundle
- add a second live context that uses the same bounded drift taxonomy outside the current AoA session-harvest lineage
