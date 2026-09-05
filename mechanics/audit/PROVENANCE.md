# Audit Provenance Bridge

This is the active-first bridge from current Audit parts back to pre-split
evidence. Use it when auditing how route surfaces moved, not when you need the
current operating contract.

## Current route first

Start with the active surfaces:

- [README](README.md)
- [DIRECTION](DIRECTION.md)
- [PARTS](PARTS.md)
- [parts](parts/)
- [LANDING_LOG](LANDING_LOG.md)

If those surfaces answer the task, stop there. Do not pull legacy route names
into current behavior just because they once existed.

## Source map

| Evidence source | Active route | Distilled signal |
|---|---|---|
| Pre-split flat `PROMOTION_READINESS_MATRIX.md` | [parts/promotion-readiness-matrix](parts/promotion-readiness-matrix/README.md) | Promoted-corpus readiness stays visible as queue posture, lane counts, blockers, and suggested wave order. |
| Pre-split flat `PROMOTION_WAVE_A_RUNBOOK.md` | [parts/promotion-evidence-runbook](parts/promotion-evidence-runbook/README.md) | The current promotion evidence-prep wave stays bounded to leading promoted candidates without status flips. |
| Pre-split flat `EXTERNAL_EVIDENCE_SPRINT_RUNBOOK.md` | [parts/external-evidence-sprint-runbook](parts/external-evidence-sprint-runbook/README.md) | External proof searches have an execution path that rejects adjacent fits and avoids stale lane reruns. |
| Pre-split flat `EXTERNAL_EVIDENCE_LEDGER.md` | [parts/external-evidence-ledger](parts/external-evidence-ledger/README.md) | Searched-lane memory and closure precedents stay visible without replacing bundle-local notes. |
| 2026-05-14 canonical corpus retro-check | [parts/canonical-retro-audit](parts/canonical-retro-audit/README.md) | Already-canonical rows have a bounded metadata/evidence/verdict coherence check that does not become proof authority or automatic demotion. |
| Former root closure-audit `ROADMAP.md` | active Audit parts | The root roadmap now owns live repo direction; the former closure-audit baseline is recoverable from the [immutable historical source](https://github.com/8Dionysus/aoa-techniques/blob/feffba63dc22fd921512ba5a3ff1b5d78606f93b/mechanics/audit/legacy/raw/ROOT_CLOSURE_AUDIT_ROADMAP_2026-05-03.md). |

## Legacy posture

The 2026-05-01 split moved the current flat files into active part homes without
rewriting promotion posture, evidence lanes, queue counts, or technique status.
No raw pre-prune receipt was needed because no audit ledger was shortened in
this slice.

When a future pass compacts an audit ledger, runbook, or root-facing audit
surface, record the exact pre-change Git commit and original path in this
provenance bridge or the retirement decision, and record the distillation in
`LANDING_LOG.md`. Do not create an archive-only raw copy.

## Audit rule

When evidence changes current behavior, update the relevant bundle-local
evidence notes first, then update the active Audit part, then update this bridge
and the landing log if source topology changed.
