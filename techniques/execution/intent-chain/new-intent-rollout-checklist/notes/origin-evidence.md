# Origin Evidence

## Technique
- id: AOA-T-0005
- name: new-intent-rollout-checklist

## Source project
- name: atm10-agent
- source files:
  - `atm10-agent/docs/DECISIONS.md`
  - `atm10-agent/docs/RUNBOOK.md`
  - `atm10-agent/docs/SESSION_2026-02-24.md`
  - `atm10-agent/docs/SESSION_2026-03-03.md`

## Evidence
- `atm10-agent/docs/SESSION_2026-02-24.md` records the contract hardening that makes the rollout checklist real rather than ceremonial: canonical fixtures carry `intent_id/trace_id`, CI summaries expose those fields, and strict `--require-trace-id` plus `--require-intent-id` checks are enabled for intent-chain validation.
- `atm10-agent/docs/DECISIONS.md` formalizes the onboarding policy for each new `intent_type`: one canonical fixture, one smoke run, one strict contract-check with explicit routing assertions, summary and artifact wiring, and at least one end-to-end regression test.
- `atm10-agent/docs/RUNBOOK.md` turns that policy into a concrete reusable checklist in `M6.19`, while `M6.8` adds the complementary troubleshooting procedure for failures across fixture, smoke, contract-check, and artifact-wiring layers.
- `atm10-agent/docs/SESSION_2026-03-03.md` shows the checklist executed end to end for `open_world_map`: a new canonical fixture, dedicated smoke run, strict `expected-intent-type open_world_map` validation, new summary row, new artifact path, targeted tests, and a full regression pass.
- The same 2026-03-03 session explicitly notes that the public `automation_plan_v1` contract did not change, which shows the rollout checklist can extend the supported intent set without redefining the shared chain itself.

## Interpretation
- The origin proves this technique as a bounded extension checklist for an existing dry-run automation chain: new intent rollouts stay reviewable, traceable, artifact-visible, and contract-enforced instead of becoming one-off workflow edits.
