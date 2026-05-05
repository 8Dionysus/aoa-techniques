# Origin Evidence

## Technique
- id: AOA-T-0080
- name: session-drift-taxonomy

## Source project
- name: aoa-skills
- source files:
  - `skills/aoa-session-self-diagnose/SKILL.md`
  - `skills/aoa-session-self-diagnose/checks/review.md`
  - `tests/fixtures/skill_evaluation_cases.yaml`
  - `tests/fixtures/skill_evaluation_snapshots/aoa-session-self-diagnose/session_self_diagnose_reviewed_drift_pattern.md`

## Evidence
- the diagnosis skill explicitly classifies drift types such as boundary drift, proof debt, role leakage, memory contamination, route collapse, compaction damage, and repeated blocker patterns
- the skill separates taxonomy from probable cause by asking the diagnosis pass to preserve unknowns and not overclaim thin evidence
- the review checklist requires symptoms and causes to remain separate and forbids lazy blame of one convenient owner layer
- the reviewed drift-pattern evaluation snapshot expects a diagnosis path only after repeated friction signals survive the reviewed session

## Interpretation
- the reusable object is one bounded taxonomy layer over reviewed post-session friction
- the public technique can stay smaller than full diagnosis while still naming a portable drift vocabulary
