# Recurrence Active Parts Split

Status: accepted

Date: 2026-05-02

## Context

`mechanics/recurrence/` kept two active technique-layer surfaces as flat
package-root files: live observation producers and recurrence review decision
closure.

`Agents-of-Abyss` owns the center Recurrence mechanic with return law,
continuity vocabulary, owner split, and owner request packets. The current AoA
queue has no direct `ORQ-RECURRENCE-TECHNIQUES-*` request, so
`aoa-techniques` should not present this split as owner-request acceptance.

The local job is narrower: keep technique canon and candidate-intake beacons
observable without letting recurrence signals become candidate creation,
promotion authority, hold release, proof verdict, memory continuity, routing
decision, or runtime return.

## Decision

Move the two flat Recurrence surfaces into `parts/*/README.md` and add the
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

Add Recurrence to `mechanics/REQUEST_RECEIPTS.md` only under Non-ORQ Center
Pressure, with `candidate-only` posture.

## Consequences

- Recurrence now matches the active route shape used by the grown mechanics
  packages.
- Live observation remains advisory and cannot authorize status, candidate,
  hold, or promotion changes.
- Review decision closure remains a review packet posture and cannot mutate
  technique status by itself.
- AoA recurrence law, SDK carry, memo recall, routing dispatch, proof gates,
  runtime return, stats visibility, KAG regrounding, and playbook choreography
  stay with their owning repositories.
- Legacy preservation now has a package-local scaffold and must keep
  `legacy/INDEX.md`, `legacy/DISTILLATION_LOG.md`, and `PROVENANCE.md`
  aligned.

## Verification

Verify with:

```bash
python -m unittest tests.test_recurrence_mechanics_topology tests.test_recurrence_manifest_topology tests.test_mechanics_request_receipts tests.test_validate_repo
python scripts/validate_repo.py
python -m unittest discover -s tests
```
