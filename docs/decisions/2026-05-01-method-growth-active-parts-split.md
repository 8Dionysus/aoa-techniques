# Method-Growth Active Parts Split

Status: accepted

Date: 2026-05-01

## Context

`mechanics/method-growth/` still kept five active v0.7 downstream adoption
surfaces as flat package-root files. That made the package shallower than the
AoA mechanics shape already used for Agon, Audit, and Distillation in this repo.

The files were not raw legacy receipts. They were compact active mechanics
surfaces for pattern adoption, adoption boundaries, technique-to-skill handoff,
retention, and obsolescence.

## Decision

Move the five flat Method-growth surfaces into `parts/*/README.md` and add the
active package route files:

- `AGENTS.md`
- `DIRECTION.md`
- `PARTS.md`
- `PROVENANCE.md`
- `LANDING_LOG.md`
- `ROADMAP.md`
- `parts/AGENTS.md`
- `parts/README.md`

Treat the previous flat files as active part-local homes, not raw receipts.
The `2026-05-03` legacy scaffold decision adds a provenance district with empty
raw inventory for this package.

## Consequences

- Method-growth now matches the active/parts/provenance pattern used by the more
  mature mechanics packages.
- `ORQ-METHOD-TECHNIQUES-001` can point at concrete local response surfaces
  without treating those surfaces as technique canon.
- Work can deepen one Method-growth part at a time instead of editing a flat
  package root.
- Legacy preservation now has a package-local scaffold and must keep
  `legacy/INDEX.md`, `legacy/DISTILLATION_LOG.md`, and `PROVENANCE.md`
  aligned.

## Verification

Verify with:

```bash
python -m unittest tests.test_method_growth_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
```
