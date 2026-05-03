# Audit Legacy Index

This index maps pre-split Audit surfaces and future raw receipts to active
parts.

| Legacy or pre-split source | Active route | Distilled signal | Status |
|---|---|---|---|
| Flat `PROMOTION_READINESS_MATRIX.md` | [parts/promotion-readiness-matrix](../parts/promotion-readiness-matrix/README.md) | Promoted-corpus readiness stays visible as queue posture, lane counts, blockers, and suggested wave order. | active-moved |
| Flat `PROMOTION_WAVE_A_RUNBOOK.md` | [parts/promotion-wave-a-runbook](../parts/promotion-wave-a-runbook/README.md) | Evidence-prep wave mechanics stay bounded to leading promoted candidates without status flips. | active-moved |
| Flat `EXTERNAL_EVIDENCE_SPRINT_RUNBOOK.md` | [parts/external-evidence-sprint-runbook](../parts/external-evidence-sprint-runbook/README.md) | External proof searches keep execution order, rejection rules, and stale-lane discipline. | active-moved |
| Flat `EXTERNAL_EVIDENCE_LEDGER.md` | [parts/external-evidence-ledger](../parts/external-evidence-ledger/README.md) | Searched-lane memory and closure precedents stay visible without replacing bundle-local notes. | active-moved |
| Former root closure-audit `ROADMAP.md` | [raw/ROOT_CLOSURE_AUDIT_ROADMAP_2026-05-03.md](raw/ROOT_CLOSURE_AUDIT_ROADMAP_2026-05-03.md) plus active Audit parts | Historical repo-first closure audit remains preserved after root `ROADMAP.md` was slimmed to live repo direction. | preserved-raw |

## Rule

If a legacy source starts carrying current behavior, move that behavior into the
owning active part and record the distillation here.
