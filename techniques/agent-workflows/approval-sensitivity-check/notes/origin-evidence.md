# Origin Evidence

## Technique
- id: AOA-T-0088
- name: approval-sensitivity-check

## Source project
- name: aoa-skills
- source files:
  - `skills/aoa-automation-opportunity-scan/SKILL.md`
  - `skills/aoa-automation-opportunity-scan/references/checkpoint-boundary.md`
  - `skills/aoa-automation-opportunity-scan/references/session-harvest-integration.md`
  - `skills/aoa-session-self-diagnose/SKILL.md`
  - `skills/aoa-session-self-repair/SKILL.md`
  - `tests/fixtures/skill_evaluation_cases.yaml`

## Evidence
- the automation-opportunity skill already marks `checkpoint_required` when routes cross self-change, hidden authority, or important mutation boundaries
- the checkpoint-boundary reference enumerates strong triggers such as important-surface mutation, shifting authority, missing rollback, missing health checks, and self-repair posture
- the session-harvest integration note keeps blocked automation diagnosis and prerequisite repair explicit instead of letting automation desire hide the real blocker
- the evaluation fixtures include both an approval-heavy autopatch desire that should stay `not_now` and diagnosis or repair routes that surface missing approval and rollback posture before honest automation lift

## Interpretation
- the reusable object is one bounded approval-sensitivity check over an automation candidate rather than one full repair framework or change-management system
- the public technique can stay bounded to checkpoint-required classification without widening into approval implementation, scheduler policy, or generic governance doctrine
