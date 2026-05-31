# Mechanics Owner Request Receipts

Status: accepted

Date: 2026-05-01

## Index Metadata

- Decision ID: AOA-TECH-D-0012
- Original date: 2026-05-01
- Surface classes: mechanic package
- Technique axes: mechanic bridge
- Mechanic parents: none
- Guard families: mechanic topology, docs route
- Posture: accepted

## Context

`Agents-of-Abyss` already carries a center-side owner-request protocol and queue
for moving mechanics into stronger owner repositories. Several requests target
`aoa-techniques`, but this repository did not yet have a local surface that
showed which requests had been mapped, which local mechanics surfaces answered
them, and which stop-lines still protected owner-local truth.

The earlier attempt to express cross-repo boundaries as repeated "law/local"
blocks was too heavy. The right shape is a compact route surface that lets
agents find downstream requests without importing AoA center authority into
every package README.

## Decision

Add `mechanics/REQUEST_RECEIPTS.md` as the owner-local receipt map for AoA
center-side owner requests targeting `aoa-techniques`.

The file records only local mapping and evidence posture. It does not redefine
AoA request vocabulary, copy the AoA queue, mark center requests accepted, or
claim local landings without owner-local proof.

`mechanics/AGENTS.md` and `mechanics/README.md` route agents to the receipt map
only when work cites an `ORQ-*` request or answers a downstream owner request.

## Consequences

- Direct AoA requests to `aoa-techniques` become discoverable from the local
  mechanics entry surface.
- Distillation, method-growth, and Experience can be mapped without forcing the
  same block into every package README.
- Agon remains separate as a wave/provenance-derived candidate lane because no
  direct `ORQ-AGON-TECHNIQUES-*` request exists in the current AoA queue.
- Future acceptance or landing claims still require local owner evidence and
  the relevant validation or proof route.

## Verification

Verify with the normal repository validation path after the change:

```bash
python scripts/validate_repo.py
python -m unittest discover -s tests
```
