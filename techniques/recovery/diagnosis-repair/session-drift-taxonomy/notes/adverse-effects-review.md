# Adverse Effects Review

## Technique
- id: AOA-T-0080
- name: session-drift-taxonomy
- current role: bounded canonical default

## Review focus

Review the effects of making a read-only drift taxonomy the default first
classification move when reviewed friction needs diagnosis later.

## Failure modes

- taxonomy labels are mistaken for probable causes
- one anecdote is inflated into structural drift
- owner hints, repair shapes, or blame language leak into the taxonomy pass
- local label sets become hidden portability requirements

## Negative effects

- over-classification can make weak evidence look stronger than it is
- repeated labels can become jargon that hides the actual symptoms
- downstream diagnosis may inherit a stale or overconfident drift class

## Misuse patterns

- using taxonomy as a substitute for diagnosis
- naming a repair plan before the drift class is stable
- classifying live, unreviewed friction as if it were reviewed evidence
- forcing one favorite label when mixed or uncertain posture is more honest

## Detection signals

- reviewers cannot separate symptom, drift type, probable cause, and repair
- the taxonomy output contains owner verdicts or mutation instructions
- confidence is higher than the evidence supports
- the label set reads like project folklore rather than a bounded vocabulary

## Mitigations

- require reviewed evidence before classification
- keep mixed and uncertain outputs available
- preserve diagnosis and repair as separate downstream moves
- reduce project-local labels to adaptation examples

## Recommendation

Keep the canonical bundle and use this note as one bounded watch surface. Future
changes should sharpen the drift-label seam without widening it into diagnosis,
owner routing, proof, repair planning, or runtime diagnostic doctrine.
