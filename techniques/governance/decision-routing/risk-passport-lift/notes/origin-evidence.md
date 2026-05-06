# Origin Evidence

## Technique
- id: AOA-T-0079
- name: risk-passport-lift

## Source project
- name: aoa-skills
- source files:
  - `skills/aoa-session-route-forks/SKILL.md`
  - `skills/aoa-session-route-forks/checks/review.md`
  - `tests/fixtures/skill_evaluation_cases.yaml`
  - `tests/fixtures/skill_evaluation_snapshots/aoa-session-route-forks/session_route_forks_reviewed_branch_choice.md`

## Evidence
- the route-forks skill explicitly attaches a route passport with difficulty, risk, control mode, and delegate tier instead of hiding posture in free-form prose
- the skill and review checklist both require visible costs, risks, and stop conditions for risky branches
- the reviewed branch-choice evaluation snapshot expects at least one cost or risk per route plus explicit stop-condition posture
- the skill keeps route passports smaller than branch analysis by preserving branch cards as the primary object

## Interpretation
- the reusable object is one small per-route posture summary that complements branch cards
- the public technique can stay bounded to route-passport metadata without widening into a planner, risk engine, or approval system
