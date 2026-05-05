# Origin Evidence

## Technique
- id: AOA-T-0082
- name: repair-shape-from-diagnosis

## Source project
- name: aoa-skills
- source files:
  - `skills/aoa-session-self-repair/SKILL.md`
  - `skills/aoa-session-self-repair/checks/review.md`
  - `tests/fixtures/skill_evaluation_cases.yaml`
  - `tests/fixtures/skill_evaluation_snapshots/aoa-session-self-repair/session_self_repair_reviewed_diagnosis_packet.md`

## Evidence
- the self-repair skill explicitly requires a reviewed diagnosis before any repair packet is a fit
- the skill chooses the smallest honest repair shape, names the primary owner repo, and records validation plus stop conditions
- the review checklist rejects playbook-scale rollout collapse and keeps escalation explicit if the repair widens
- the reviewed diagnosis-packet evaluation snapshot expects a bounded repair packet rather than another diagnosis pass or a vague self-improvement ask

## Interpretation
- the reusable object is one bounded repair-shaping pass that starts after diagnosis
- the public technique can stay smaller than checkpoint doctrine and smaller than rollout design while still producing a useful repair shape
