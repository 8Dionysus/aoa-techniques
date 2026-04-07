# Origin Evidence

## Technique
- id: AOA-T-0094
- name: canonical-owner-with-validated-mirror

## Source project
- name: Dionysus + AoA ecosystem repos
- source files:
  - `/srv/Dionysus/reports/ecosystem-audits/2026-04-07.cross-repo.aoa-stats-fixpack-rollout-session-harvest.md`
  - `/srv/Dionysus/reports/ecosystem-audits/2026-04-07.cross-repo.aoa-stats-fixpack-rollout-session-harvest.packet.json`
  - `/srv/aoa-stats/schemas/stats-event-envelope.schema.json`
  - `/srv/aoa-stats/scripts/build_views.py`
  - `/srv/aoa-evals/schemas/stats-event-envelope.schema.json`
  - `/srv/aoa-evals/scripts/validate_repo.py`
  - `/srv/aoa-skills/config/project_core_skill_kernel.json`

## Evidence
- the April 7, 2026 cross-repo rollout moved the shared stats event envelope to `aoa-stats` as the canonical owner and left `aoa-evals` with an explicit mirror rather than a competing source
- `aoa-stats` now fails early when `event_kind` leaves the allowed vocabulary instead of accepting any non-empty string
- `aoa-evals` validates mirror parity against the canonical schema so ownership metadata and enum values cannot silently drift
- the same rollout absorbed `diagnosis_packet_receipt` into the shared vocabulary without reopening split-brain drift across repositories

## Interpretation
- the surviving reusable object is a cross-repo contract law: one canonical owner, legal mirrors only with explicit parity validation, and fail-fast consumer vocabulary checks
- the public technique can stay bounded around ownership, mirror legality, and vocabulary drift prevention without widening into rollout sequencing or live publisher operations
