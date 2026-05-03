# AGENTS.md

Route card for `mechanics/recurrence/`.

## Purpose

This package owns the `aoa-techniques` side of recurrence: technique canon and
candidate-intake observation, plus review-decision closure posture.

It does not own AoA recurrence law, runtime return, memory recall, routing
dispatch, proof verdicts, playbook choreography, SDK control-plane carry,
derived stats, KAG regrounding, or technique status changes.

## Start here

1. Root `AGENTS.md`.
2. `mechanics/AGENTS.md`.
3. `mechanics/recurrence/README.md`.
4. `DIRECTION.md`, `PARTS.md`, `PROVENANCE.md`, and the touched part README.
5. `mechanics/REQUEST_RECEIPTS.md` only when naming AoA center-side pressure.

## Local law

- Keep recurrence here technique-layered: observation producers and review
  closure, not operational continuity.
- Do not import `Agents-of-Abyss` recurrence law as local implementation
  authority.
- Do not treat generated registries, readiness JSON, manifests, live receipts,
  or recurrence beacons as technique promotion authority.
- Do not create hidden memory continuity, runtime resume, proof verdict,
  router decision, owner acceptance, or automatic technique creation.
- If a stable reusable practice emerges, route it into `techniques/` through
  the normal technique review path.

## Verify

Use the root validation path after changes:

```bash
python scripts/validate_repo.py
python -m unittest discover -s tests
```
