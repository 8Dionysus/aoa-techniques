# Audit Legacy Log

## 2026-05-01 - Flat files moved into active parts

The four pre-split audit files were moved into active part homes:

- `PROMOTION_READINESS_MATRIX.md` -> `parts/promotion-readiness-matrix/README.md`
- `PROMOTION_WAVE_A_RUNBOOK.md` -> `parts/promotion-wave-a-runbook/README.md`
- `EXTERNAL_EVIDENCE_SPRINT_RUNBOOK.md` -> `parts/external-evidence-sprint-runbook/README.md`
- `EXTERNAL_EVIDENCE_LEDGER.md` -> `parts/external-evidence-ledger/README.md`

No ledger or runbook was shortened in this slice, so no raw pre-prune receipt
was added.

Promotion posture, readiness counts, evidence lanes, and technique statuses were
not changed.

## 2026-05-03 - Root closure-audit roadmap preserved as legacy raw

The former root `ROADMAP.md` carried a long repo-first closure audit, live
snapshot, and historical phase findings. Root `ROADMAP.md` was slimmed back to
live repository direction and horizon posture.

The pre-slim audit text is preserved at
`legacy/raw/ROOT_CLOSURE_AUDIT_ROADMAP_2026-05-03.md`.

Technique statuses, evidence verdicts, promotion queues, and active Audit parts
were not changed by this move.
