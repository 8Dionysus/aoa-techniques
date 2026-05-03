# Boundary Bridge Candidate Mechanic

Status: accepted

Date: 2026-05-03

## Context

`Agents-of-Abyss` has a landed Boundary Bridge mechanic that owns
boundary-crossing doctrine, bridge modes, owner maps, non-transfer stop-lines,
and owner-request packets. The center owner map routes ToS meaning to
`Tree-of-Sophia`, derived projection to `aoa-kag`, route behavior to
`aoa-routing`, memory and witness objects to `aoa-memo`, proof to `aoa-evals`,
scenario choreography to `aoa-playbooks`, compatibility to `aoa-sdk`, runtime
to `abyss-stack`, and public projection to the public route owner after
evidence lands.

`aoa-techniques` already carries boundary-adjacent practice: owner-layer
triage, nearest-wrong-target rejection, bounded context mapping,
canonical-owner mirrors, source-lift and KAG exports, direct relation lifts,
multi-source provenance, repo-doc surface lifts, contract boundary testing,
fail-closed evidence gates, and audit-to-closeout proof loops.

The current AoA queue has no direct `ORQ-BRIDGE-TECHNIQUES-*` request, so this
repo should not present boundary-bridge work as center request acceptance.

## Decision

Add a local `mechanics/boundary-bridge/` package as candidate-only practice
pressure.

Create active package route files:

- `AGENTS.md`
- `README.md`
- `DIRECTION.md`
- `PARTS.md`
- `PROVENANCE.md`
- `LANDING_LOG.md`
- `ROADMAP.md`
- `parts/AGENTS.md`
- `parts/README.md`

Create three active parts:

- `parts/owner-boundary-anchors/README.md`
- `parts/derived-projection-anchors/README.md`
- `parts/proof-claim-anchors/README.md`

Do not create `legacy/raw/` in this pass because no local pre-split
boundary-bridge wave receipt or raw source packet is being moved.

Add Boundary-bridge to `mechanics/REQUEST_RECEIPTS.md` only under Non-ORQ
Center Pressure, with `candidate-only` posture.

## Consequences

- Boundary-bridge pressure becomes discoverable in the mechanics map without
  importing AoA center law as local implementation authority.
- Existing boundary-adjacent technique bundles remain canonical only through
  their `techniques/**/TECHNIQUE.md` homes.
- Generated readers, KAG exports, repo-doc routing, relation hints, and
  compatibility mirrors remain derived or mirrored surfaces rather than source
  truth.
- Owner acceptance, identity claims, ToS canon, source interpretation, routing
  authority, SDK authority, memory authority, runtime authority, public
  projection authority, generated companion authority, proof before
  `aoa-evals` or source-owner evidence, and technique promotion stay outside
  this package.

## Verification

Verify with:

```bash
python -m unittest tests.test_boundary_bridge_mechanics_topology tests.test_mechanics_request_receipts tests.test_validate_repo
python scripts/validate_repo.py
python -m unittest discover -s tests
```
