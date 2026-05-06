# Origin Evidence

## Technique
- id: AOA-T-0089
- name: quest-unit-promotion-review

## Source project
- name: aoa-skills
- source files:
  - `skills/aoa-quest-harvest/SKILL.md`
  - `skills/aoa-quest-harvest/references/promotion-outcomes.md`
  - `skills/aoa-quest-harvest/references/quest-promotion-receipt-schema.yaml`
  - `skills/aoa-quest-harvest/checks/review.md`
  - `skills/aoa-quest-harvest/examples/runtime.md`

## Evidence
- the quest-harvest skill is already bounded to one repeated reviewed quest unit rather than the wider session-harvest family
- the allowed outcomes explicitly distinguish `skill`, `playbook`, `agent`, `eval`, `memo`, and keep-or-open quest posture
- the review checklist requires the repeated unit, correct owner target, and rejected nearest-wrong target to remain visible
- the runtime example proves the skill is a final promotion decision rather than an authoring or execution workflow

## Interpretation
- the reusable object is one final promotion review over one repeated reviewed quest unit
- the public technique can stay focused on the verdict seam without importing repo-local authoring doctrine
