# Audit

This package owns the `aoa-techniques` side of the cross-project Audit mechanic:
making promotion pressure, evidence gaps, searched lanes, and canonical
readiness legible enough to route the next honest move.

Start with:

- [Direction](DIRECTION.md): current intent, boundaries, and route posture.
- [Parts](PARTS.md): active part map.
- [Provenance](PROVENANCE.md): active-first bridge back to pre-split surfaces.
- [Landing Log](LANDING_LOG.md): dated accounting for structural landings.
- [Roadmap](ROADMAP.md): next honest passes.

Current active parts:

- [Promotion Readiness Matrix](parts/promotion-readiness-matrix/README.md):
  active readiness queues and owner-local promotion posture.
- [Promotion Wave A Runbook](parts/promotion-wave-a-runbook/README.md):
  bounded promotion wave mechanics.
- [External Evidence Sprint Runbook](parts/external-evidence-sprint-runbook/README.md):
  sprint path for evidence-gated external technique candidates.
- [External Evidence Ledger](parts/external-evidence-ledger/README.md):
  searched-lane and evidence status ledger.

Audit can name blockers, searched evidence, and readiness posture. It does not
issue proof verdicts or silently flip technique status.

## Audit Gate

Before audit material changes a bundle status, it must be able to name:

- the bundle-local evidence note that owns the verdict
- the exact blocker or closure signal
- the external, downstream, or bundle-local proof surface being used
- the owner-local route for any shared queue update
- the stop line that prevents audit notes from replacing canonical review

If those cannot be named, keep the material here as queue posture, searched-lane
memory, or a runbook note rather than promoting technique status.
