# Audit

This package owns the `aoa-techniques` side of the cross-project Audit mechanic:
making promotion pressure, evidence gaps, searched lanes, and canonical
readiness legible enough to route the next honest move.

## Mechanic card

Status: active promotion and evidence route.

### Trigger

Use this package when technique promotion pressure, evidence gaps, searched
lanes, canonical-readiness posture, or external proof routes need to be made
legible before a bundle status or queue changes.

### Local owns

This package owns readiness queues, evidence-sprint runbooks, searched-lane
memory, active audit parts, and provenance bridges for technique-canon audit
pressure.

### Stronger owner split

`techniques/**/TECHNIQUE.md` and bundle-local notes own technique status
evidence. `aoa-evals` owns proof verdicts. `Agents-of-Abyss` owns center Audit
doctrine and owner-request grammar. Sibling repos own their own downstream
evidence before it can be treated as accepted use.

### Inputs

- bundle-local evidence notes and review state
- external or downstream proof surfaces
- searched-lane records
- promotion-readiness blockers or closure signals
- audit provenance from pre-split surfaces

### Outputs

- readiness posture
- evidence sprint route
- searched-lane ledger entry
- owner-local follow-up route
- no status change unless bundle-local evidence also moves

### Must not claim

- proof verdicts
- canonical promotion by queue pressure alone
- sibling owner acceptance
- generated or ledger authority over authored bundle meaning
- donor import ownership, which routes to Distillation

### Validation

Use [AGENTS](AGENTS.md#verify) for the package validation lane.

### Next route

Start from [DIRECTION](DIRECTION.md), [PARTS](PARTS.md), and the relevant part
README. Use [PROVENANCE](PROVENANCE.md) only when auditing source lineage. If a
bundle status would move, update the bundle-local evidence route first.

## Active route

- [Direction](DIRECTION.md): current intent, boundaries, and route posture.
- [Parts](PARTS.md): active part map.
- [Provenance](PROVENANCE.md): active-first bridge back to pre-split surfaces.
- [Landing Log](LANDING_LOG.md): dated accounting for structural landings.
- [Roadmap](ROADMAP.md): next honest passes.

## Functioning parts

- [Promotion Readiness Matrix](parts/promotion-readiness-matrix/README.md):
  active readiness queues and owner-local promotion posture.
- [Promotion Evidence Runbook](parts/promotion-evidence-runbook/README.md):
  bounded promotion wave mechanics.
- [External Evidence Sprint Runbook](parts/external-evidence-sprint-runbook/README.md):
  sprint path for evidence-gated external technique candidates.
- [External Evidence Ledger](parts/external-evidence-ledger/README.md):
  searched-lane and evidence status ledger.
- [Canonical Retro Audit](parts/canonical-retro-audit/README.md):
  retro-checks over already-canonical rows so stale metadata or contradictory
  verdicts do not hide inside the canon.

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
