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
- `atm10-agent/docs/DECISIONS.md` records the formal onboarding policy for each new `intent_type`: one canonical fixture, one smoke run, one strict contract-check with `--require-trace-id` and `--require-intent-id`, summary and artifact wiring, and at least one end-to-end regression test.
- `atm10-agent/docs/RUNBOOK.md` turns that policy into a concrete rollout checklist with explicit commands for the fixture path, smoke run, strict `expected-intent-type` contract-check, summary row, artifact path, and minimum regression coverage.
- `atm10-agent/docs/SESSION_2026-02-24.md` records the precursor contract hardening that makes the checklist meaningful: canonical fixtures carry `intent_id/trace_id`, CI exposes those fields in `Automation Smoke Contracts`, and strict traceability checks are enabled for intent-chain validation.
- `atm10-agent/docs/SESSION_2026-03-03.md` shows the checklist used end-to-end for `open_world_map`: a new canonical fixture, dedicated smoke run, strict `expected-intent-type open_world_map` validation, new summary row, new artifact path, targeted tests, and full regression.

## Interpretation
- The origin proves this technique as a bounded extension checklist for an existing dry-run automation chain: new intent rollouts stay reviewable, traceable, and contract-enforced instead of becoming one-off workflow edits.
