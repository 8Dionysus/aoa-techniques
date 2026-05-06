# Audit Active Parts Split

Status: accepted
Date: 2026-05-01

## Context

`mechanics/audit/` had grown into several flat surfaces: promotion readiness,
promotion-wave execution, external-evidence sprinting, and searched-lane memory.
That kept the files discoverable, but it did not match the AoA mechanics shape
now used by Agon and Distillation.

Audit is also a high-risk route surface because it names promotion pressure. If
the route is hard to read, future agents can mistake queue pressure or searched
lanes for canonical proof.

## Options

- Keep all Audit files flat and rely on existing links.
- Move only the largest matrix into a part and leave the rest flat.
- Split Audit into route cards, active parts, provenance, landing log, and
  legacy accounting without changing promotion status or evidence verdicts.

## Decision

Move the four active Audit surfaces into `mechanics/audit/parts/`:

- `promotion-readiness-matrix`
- `promotion-evidence-runbook`
- `external-evidence-sprint-runbook`
- `external-evidence-ledger`

Add route-local `AGENTS.md`, `DIRECTION.md`, `PARTS.md`, `PROVENANCE.md`,
`LANDING_LOG.md`, `ROADMAP.md`, `parts/`, and `legacy/` surfaces.

No promotion posture, readiness counts, evidence lanes, or technique statuses
change in this split.

## Consequences

Future Audit work has a clearer active route and can preserve raw receipts
before any ledger or runbook compaction. The tradeoff is link churn: entrypoint
docs, recurrence manifests, tests, and quest owner surfaces must point to the
new part-local paths.

The split reinforces the project rule that Audit can name blockers, searched
lanes, and readiness posture, but bundle-local evidence and canonical review
still own promotion authority.
