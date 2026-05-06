# Origin Evidence

## Technique
- id: AOA-T-0087
- name: human-loop-to-seed-lift

## Source project
- name: aoa-skills
- source files:
  - `skills/aoa-automation-opportunity-scan/SKILL.md`
  - `skills/aoa-automation-opportunity-scan/references/playbook-seed-bridge.md`
  - `skills/aoa-automation-opportunity-scan/references/session-harvest-integration.md`
  - `skills/aoa-automation-opportunity-scan/references/automation-opportunity-packet-schema.yaml`
  - `tests/fixtures/skill_evaluation_cases.yaml`
  - `tests/fixtures/skill_evaluation_snapshots/aoa-automation-opportunity-scan/automation_opportunity_scan_recurring_review_closeout_route.md`

## Evidence
- the automation-opportunity skill explicitly routes each recurring route toward `skill`, `playbook_seed`, `technique_candidate`, `repair_quest`, or `defer` instead of treating "automation" as one undifferentiated landing
- the playbook-seed bridge already distinguishes one bounded executable workflow from one recurring multi-skill or scheduled scenario
- the session-harvest integration note keeps automation scanning subordinate to donor harvest, fork routing, diagnosis, repair, and progression instead of letting it swallow the family
- the recurring closeout evaluation snapshot expects an owner layer, a next artifact, and a rejected nearest wrong target while keeping `schedule_hint` advisory only

## Interpretation
- the reusable object is one bounded first-honest-landing lift from a recurring human loop into a seed-facing artifact
- the public technique can stay bounded to landing choice without widening into implementation, scheduler authority, or generic roadmap doctrine
