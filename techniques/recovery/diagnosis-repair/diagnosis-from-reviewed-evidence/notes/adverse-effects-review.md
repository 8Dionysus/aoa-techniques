# Adverse Effects Review

## Technique
- id: AOA-T-0081
- name: diagnosis-from-reviewed-evidence
- current role: bounded canonical default

## Review focus

Review the effects of making a read-only diagnosis packet the default move when
reviewed friction has enough evidence to name symptoms, probable causes, owner
hints, and unknowns before repair.

## Failure modes

- symptoms and probable causes collapse into one narrative
- likely owner hints are treated as final owner verdicts
- unknowns disappear even though evidence remains mixed
- suggested repair shapes become hidden mutation instructions

## Negative effects

- overconfident diagnosis can settle weak evidence too early
- repeated diagnosis passes can delay an already justified bounded repair
- downstream repair may inherit an owner hint as if it were owner law

## Misuse patterns

- writing diagnosis from live debugging instead of reviewed evidence
- using diagnosis as a replacement for repair planning
- naming one convenient owner before the evidence supports it
- silently fixing the issue while producing a diagnosis packet

## Detection signals

- the packet has no evidence refs for meaningful symptoms
- probable causes are written as certainty where confidence is thin
- repair commands, edits, or playbook steps appear in the diagnosis output
- reviewers cannot explain which evidence supports each cause

## Mitigations

- require reviewed evidence refs before causes
- keep owner hints explicitly non-sovereign
- preserve unknowns and confidence posture
- hand off to repair-shaping only after the diagnosis packet is readable

## Recommendation

Keep the canonical bundle and use this note as one bounded watch surface. Future
changes should keep diagnosis read-only and evidence-shaped without widening it
into repair, owner-law, proof, runtime health, or incident-response doctrine.
