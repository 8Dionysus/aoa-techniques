# Origin Evidence

## Technique
- id: AOA-T-0096
- name: pinned-validation-matrix-before-generated-publish

## Source project
- name: aoa-routing + aoa-skills + Dionysus
- source files:
  - `scripts/build_router.py`
  - `tests/test_live_workspace_contracts.py`
  - `scripts/publish_core_skill_receipts.py`
  - `reports/ecosystem-audits/2026-04-07.cross-repo.surface-detection-wave-rollout-session-harvest.md`

## Evidence
- the surface-detection second-wave landing exposed a repeatable gap between
  local workspace rebuilds and the sibling refs that GitHub workflows actually
  validated
- `aoa-routing` needed a repair pass that synced generated snapshots with the
  live `aoa-playbooks` review track instead of trusting stale local
  expectations
- `aoa-skills` needed portable receipt-schema mirrors so the publish path would
  match the workflow-consumed contracts rather than a narrower local state
- the via-negativa owner wave replayed the same family on 2026-04-08:
  `aoa-routing` needed a parity-only follow-up so
  `generated/two_stage_router_eval_cases.jsonl` matched the
  workflow-pinned `aoa-skills` snapshot that GitHub actually validated rather
  than a convenient local sibling state
- the same wave also required `aoa-skills` to rebase onto fresh `origin/main`
  so the required `validate` check reran on the final head before merge,
  reinforcing that merge-readiness has to track the workflow's real inputs and
  head state instead of a local pre-merge impression
- the durable session harvest in `Dionysus` recorded the surviving reusable
  object as a technique-shaped publish-hygiene law rather than as repo-local CI
  trivia

## Interpretation
- the surviving reusable object is one bounded rule for generated publish:
  reproduce the workflow-pinned matrix first, then rebuild and validate
- the public technique can stay smaller than full release choreography while
  still preventing false local confidence
- the via-negativa replay strengthens the evidence for the same law without yet
  proving a second non-identical publish family
