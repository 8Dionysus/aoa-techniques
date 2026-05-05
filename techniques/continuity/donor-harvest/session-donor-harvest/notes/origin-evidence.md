# Origin Evidence

## Technique
- id: AOA-T-0075
- name: session-donor-harvest

## Source project
- name: aoa-skills
- source files:
  - `skills/aoa-session-donor-harvest/SKILL.md`
  - `skills/aoa-session-donor-harvest/techniques.yaml`
  - `skills/aoa-session-donor-harvest/checks/review.md`
  - `tests/fixtures/skill_evaluation_cases.yaml`
  - `tests/fixtures/skill_evaluation_snapshots/aoa-session-donor-harvest/session_donor_harvest_reviewed_multi_unit_session.md`

## Evidence
- the donor skill explicitly requires a reviewed post-session artifact and rejects live capture, transcript export, and local indexing as out-of-scope prerequisites
- the workflow extracts reusable units instead of themes, splits merged candidates, and preserves a donor-pack posture before any final promotion verdict
- the skill review checklist requires one concrete next artifact per accepted candidate while still allowing `hold` instead of forced promotion
- the evaluation fixture for the reviewed multi-unit session requires several candidate units to survive in parallel instead of collapsing practice, workflow, and broader route into one bucket

## Interpretation
- the reusable object is one post-session donor-extraction pass over a reviewed session artifact
- the public technique can stay bounded to donor-pack creation with evidence anchors without importing skill invocation wrappers, repo-local routing policy, or final promotion doctrine
