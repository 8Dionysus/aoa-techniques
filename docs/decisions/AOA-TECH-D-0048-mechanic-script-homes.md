# Mechanic Script Homes

Date: 2026-05-14

## Index Metadata

- Decision ID: AOA-TECH-D-0048
- Original date: 2026-05-14
- Surface classes: mechanic package, mechanic part
- Technique axes: mechanic bridge
- Mechanic parents: none
- Guard families: mechanic topology, part-local artifact
- Posture: accepted

## Context

Root `scripts/` had become a mix of repo-wide validators/builders and helper
commands that only served one mechanic part.

The clearest one-owner cases were:

- `scripts/build_topology_scout.py`
- `scripts/build_tree_projection.py`
- `scripts/publish_live_receipts.py`

The first two rebuild Distillation `technique-reform-ingress` reports. The
third appends owner-local live receipts consumed as Recurrence observation
evidence.

## Decision

Move one-owner mechanic helper scripts to the owning part:

- `mechanics/distillation/parts/technique-reform-ingress/scripts/`
- `mechanics/recurrence/parts/live-observation-producers/scripts/`

Keep root `scripts/` for repo-wide validators, release orchestration, and
builders whose outputs are repo-wide generated or docs surfaces.

## Root Pass

The same pass inspected the tracked root directories rather than stopping at
the first suspicious path:

- `.agents/` and `.github/` remain platform and agent-lane support surfaces.
- `config/` and `examples/` now hold only route cards plus repo-wide reserved
  surfaces; `data/` was later retired because no active repo-wide payload
  remained.
- `docs/`, `generated/`, `legacy/`, `techniques/`, and `tests/` remain
  repo-wide doctrine, generated readers, archive, canon, and verification
  surfaces.
- `quests/` and root quest schemas remain in the root by explicit Questbook
  stop-line; the Questbook mechanic does not absorb those public projections.
- `schemas/` and `templates/` remain repo-wide contracts and authoring
  scaffolds unless a schema or example has exactly one mechanic owner.
- `incoming/` remains its own intake surface and was not the only suspected
  root tail in this continuation.

## Consequences

- Root `scripts/` is smaller and no longer looks like the owner of
  technique-reform scout reports or recurrence live-receipt publishing.
- Part-local route cards now describe how those helper commands may be used.
- `release_check.py` still orchestrates repo-wide validation, but calls the
  part-local report builders through their owning paths.
- Shared parsing and validation logic remains in root `scripts/validate_repo.py`
  because it still validates repo-wide contracts and generated parity.

## Verification

Verification was routed through the targeted owner checks and repository validation lanes.
