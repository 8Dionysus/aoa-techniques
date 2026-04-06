# Origin Evidence

## Technique
- id: AOA-T-0081
- name: diagnosis-from-reviewed-evidence

## Source project
- name: aoa-skills
- source files:
  - `skills/aoa-session-self-diagnose/SKILL.md`
  - `skills/aoa-session-self-diagnose/checks/review.md`
  - `tests/fixtures/skill_evaluation_cases.yaml`
  - `tests/fixtures/skill_evaluation_snapshots/aoa-session-self-diagnose/session_self_diagnose_reviewed_drift_pattern.md`

## Evidence
- the diagnosis skill explicitly gathers symptoms and evidence refs before naming probable causes
- the skill requires owner hints and repair-shape suggestions while still forbidding hidden mutation
- the review checklist keeps symptoms and causes separate, preserves unknowns, and rejects lazy blame of one convenient owner
- the reviewed drift-pattern evaluation snapshot expects a diagnosis packet rather than immediate repair or promotion

## Interpretation
- the reusable object is one bounded read-only diagnosis pass over reviewed evidence
- the public technique can stay smaller than repair planning while still producing a useful diagnosis packet
