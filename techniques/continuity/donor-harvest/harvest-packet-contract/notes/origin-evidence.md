# Origin Evidence

## Technique
- id: AOA-T-0077
- name: harvest-packet-contract

## Source project
- name: aoa-skills
- source files:
  - `skills/aoa-session-donor-harvest/SKILL.md`
  - `skills/aoa-session-donor-harvest/references/harvest-packet-contract.md`
  - `skills/aoa-session-donor-harvest/checks/review.md`
  - `tests/fixtures/skill_evaluation_cases.yaml`
  - `tests/fixtures/skill_evaluation_snapshots/aoa-session-donor-harvest/session_donor_harvest_reviewed_multi_unit_session.md`

## Evidence
- the donor-harvest skill now explicitly names `HARVEST_PACKET` as the nucleus output rather than a loose donor summary
- the packet reference narrows the required fields to `session_ref`, `reviewed_artifacts`, and `extracts` instead of allowing an unbounded recap schema
- the same reference keeps optional family fields such as forks, diagnosis, repair, progression, and quest hooks clearly subordinate
- the reviewed multi-unit evaluation snapshot expects one packet that still separates several reusable units cleanly before any later follow-on seam closes

## Interpretation
- the reusable object is one bounded post-session packet contract over reviewed extracts
- the public technique can stay narrower than donor extraction and narrower than any later family verdict while still preserving a useful nucleus packet
