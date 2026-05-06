# Origin Evidence

## Technique
- id: AOA-T-0078
- name: decision-fork-cards

## Source project
- name: aoa-skills
- source files:
  - `skills/aoa-session-route-forks/SKILL.md`
  - `skills/aoa-session-route-forks/checks/review.md`
  - `tests/fixtures/skill_evaluation_cases.yaml`
  - `tests/fixtures/skill_evaluation_snapshots/aoa-session-route-forks/session_route_forks_reviewed_branch_choice.md`

## Evidence
- the route-forks skill explicitly starts only after review and requires several plausible next moves instead of one obvious bounded route
- the skill procedure separates materially different branches, names likely owner targets, and requires gains, costs, risks, and stop conditions
- the review checklist rejects hidden recommendation collapse and keeps `aoa-routing` and `aoa-kag` out of first authoring
- the reviewed branch-choice evaluation snapshot expects explicit branch cards with owner targets and visible stop conditions

## Interpretation
- the reusable object is one bounded branch-card workflow over several plausible post-session routes
- the public technique can stay smaller than playbook design and smaller than routing policy while still keeping next-route choice legible
