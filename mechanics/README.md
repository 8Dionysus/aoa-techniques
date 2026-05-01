# Mechanics

`mechanics/` is the owner-local home where `aoa-techniques` participates in the
cross-project AoA mechanics. It keeps procedural movement around technique canon
out of the general docs pile without pretending those surfaces are already
published technique bundles.

The top-level package names follow the AoA mechanics vocabulary. Repo-local
concerns such as donor refinery, promotion readiness, adoption, mastery, and
stress live inside those cross-cutting mechanics instead of becoming unrelated
parallel axes.

## Cross-Mechanics Map

- [method-growth](method-growth/README.md): technique adoption, technique-skill
  handoff, retention, obsolescence, and owner landing of reusable practice.
- [distillation](distillation/README.md): donor intake, external import,
  cross-layer candidate capture, long-gap re-entry, and candidate extraction.
- [audit](audit/README.md): promotion readiness, evidence sprinting, evidence
  ledgers, and canonical-pressure visibility.
- [growth-cycle](growth-cycle/README.md): mastery harvest, feat reflection,
  questbook integration, and reviewed closeout incubation.
- [agon](agon/README.md): Agon practice-candidate bridges, active parts,
  provenance, and preserved wave receipts.
- [recurrence](recurrence/README.md): recurrence observation and closure
  mechanics that feed technique review without becoming authority.
- [experience](experience/README.md): experience-mechanic governance,
  authority, service, scope, handoff, and decision surfaces.
- [release-support](release-support/README.md): installation and sovereign
  release support surfaces that remain bounded by owner consent.
- [antifragility](antifragility/README.md): stress, chaos, degraded-mode, and
  recovery-oriented practice routes.

## Boundary

Use `mechanics/` when a file describes how a practice candidate moves, matures,
gets reviewed, hands off, recurs, survives stress, or supports a release. Use
`docs/` when the file explains repository orientation, review doctrine,
generated-reader interpretation, or public selection guidance. Use
`techniques/` when the reusable practice unit is ready to stand as a bundle.

Mechanics can prepare canon. They do not replace canon.

## Active And Legacy Split

When a mechanic has grown through waves, seeds, receipts, or candidate packets,
do not flatten every file into the package root. Build the package one mechanic
at a time:

- active behavior in `README.md`, `DIRECTION.md`, `PARTS.md`, and `parts/`
- provenance bridge in `PROVENANCE.md`
- checked landing history in `LANDING_LOG.md`
- preserved source receipts in `legacy/raw/`
- source-to-active accounting in `legacy/INDEX.md` and
  `legacy/DISTILLATION_LOG.md`

Use [agon](agon/README.md) as the first owner-local example of this split.
