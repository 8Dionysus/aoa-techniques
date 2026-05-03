# Growth Cycle Active Parts Split

Status: accepted

Date: 2026-05-01

## Context

`mechanics/growth-cycle/` kept four active technique-layer surfaces as flat
package-root files: mastery harvest posture, technique feat model, questbook
integration, and reviewed closeout promotion-readiness incubation.

`Agents-of-Abyss` owns the center Growth Cycle mechanic with stage law, owner
split, and owner request packets. The current AoA queue has no direct
`ORQ-GROWTHCYCLE-TECHNIQUES-*` request, so `aoa-techniques` should not pretend
this split is an owner-request landing.

## Decision

Move the four flat Growth-cycle surfaces into `parts/*/README.md` and add the
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

Add Growth-cycle to `mechanics/REQUEST_RECEIPTS.md` only under Non-ORQ Center
Pressure, with `candidate-only` posture.

Add a `.gitignore` exception for `mechanics/*/ROADMAP.md` so mechanics package
roadmaps remain visible to git instead of requiring force-adds for every split.

## Consequences

- Growth-cycle now matches the active route shape used by the grown mechanics
  packages.
- Feat cards and mastery harvest stay derived or reflective; they do not become
  technique canon or achievement authority.
- Questbook integration remains a deferred-obligation route rather than a donor
  backlog.
- Promotion-readiness incubation remains an explicit holding lane until
  repeated reviewed evidence justifies a real technique bundle.
- Mechanics splits can add package roadmaps without silently producing ignored
  files.
- Legacy preservation now has a package-local scaffold and must keep
  `legacy/INDEX.md`, `legacy/DISTILLATION_LOG.md`, and `PROVENANCE.md`
  aligned.

## Verification

Verify with:

```bash
python -m unittest tests.test_growth_cycle_mechanics_topology tests.test_mechanics_request_receipts tests.test_validate_repo
python scripts/validate_repo.py
python -m unittest discover -s tests
```
