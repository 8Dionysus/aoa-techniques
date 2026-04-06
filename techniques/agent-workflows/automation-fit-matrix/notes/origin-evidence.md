# Origin Evidence

## Technique
- id: AOA-T-0086
- name: automation-fit-matrix

## Source project
- name: aoa-skills
- source files:
  - `skills/aoa-automation-opportunity-scan/SKILL.md`
  - `skills/aoa-automation-opportunity-scan/references/automation-fit-matrix.md`
  - `skills/aoa-automation-opportunity-scan/references/automation-opportunity-packet-schema.yaml`
  - `tests/fixtures/skill_evaluation_cases.yaml`
  - `tests/fixtures/skill_evaluation_snapshots/aoa-automation-opportunity-scan/automation_opportunity_scan_recurring_review_closeout_route.md`
  - `tests/fixtures/skill_evaluation_snapshots/aoa-automation-opportunity-scan/automation_opportunity_scan_one_off_creative_strategy_thread.md`

## Evidence
- the automation-opportunity skill explicitly classifies repeat signal, friction, determinism, input clarity, output clarity, proof surface, reversibility, secret coupling, and approval sensitivity before it emits `seed_ready` or `not_now`
- the authored fit matrix reference already defines strong and weak posture for each row plus the likely consequence of weak posture
- the packet schema keeps the result bounded around explicit route fields and a verdict instead of a hidden score engine
- the paired positive and negative evaluation snapshots prove the same matrix distinguishes a recurring reviewed closeout route from a one-off creative thread

## Interpretation
- the reusable object is one small route-classification matrix rather than a playbook, skill, or scheduler
- the public technique can stay bounded to evidence-backed readiness classification without widening into routing, approval, or automation-authority doctrine
