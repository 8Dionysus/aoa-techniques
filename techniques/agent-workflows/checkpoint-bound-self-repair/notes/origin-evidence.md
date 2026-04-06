# Origin Evidence

## Technique
- id: AOA-T-0083
- name: checkpoint-bound-self-repair

## Source project
- name: aoa-skills
- source files:
  - `skills/aoa-session-self-repair/SKILL.md`
  - `skills/aoa-session-self-repair/references/checkpoint-bridge.md`
  - `skills/aoa-session-self-repair/checks/review.md`
  - `tests/fixtures/skill_evaluation_cases.yaml`
  - `tests/fixtures/skill_evaluation_snapshots/aoa-session-self-repair/session_self_repair_reviewed_diagnosis_packet.md`

## Evidence
- the self-repair skill explicitly records checkpoint posture with policy fit, approval, rollback marker, health check, iteration limit, and improvement log
- the checkpoint bridge reference makes the non-silent self-repair rule explicit and forbids hidden doctrine edits or retry loops disguised as progress
- the review checklist requires checkpoint posture and rejects approval bypass
- the reviewed diagnosis-packet evaluation snapshot expects rollback and health-check posture as part of the repair output

## Interpretation
- the reusable object is one checkpoint stack around bounded self-repair
- the public technique can stay narrower than general approval doctrine while still making self-repair reviewable
