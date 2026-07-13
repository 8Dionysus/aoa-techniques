# Mechanics Legacy Scaffold Bridge

Status: accepted

Date: 2026-05-03

## Index Metadata

- Decision ID: AOA-TECH-D-0025
- Original date: 2026-05-03
- Surface classes: mechanic package, legacy/provenance
- Technique axes: mechanic bridge
- Mechanic parents: none
- Guard families: mechanic topology, legacy/provenance
- Posture: accepted

## Context

Several `mechanics/*/` packages had active route files, parts, and provenance
bridges but no `legacy/` district because no raw source receipt had been
preserved during the split. That made the absence of raw material look too much
like an absence of provenance posture.

The mature mechanics packages already use `legacy/` as a provenance district:
raw receipts are preserved there, while active behavior stays in `README.md`,
`DIRECTION.md`, `PARTS.md`, and `parts/`.

## Decision

Add a legacy scaffold to mechanics packages that have no preserved raw receipts:

- `boundary-bridge`
- `checkpoint`
- `experience`
- `growth-cycle`
- `method-growth`
- `questbook`
- `recurrence`
- `release-support`
- `rpg`

Each scaffold contains:

- `legacy/AGENTS.md`
- `legacy/README.md`
- `legacy/INDEX.md`
- `legacy/DISTILLATION_LOG.md`
- `legacy/raw/README.md`

Keep raw inventory empty for these packages until an actual source receipt is
preserved. The scaffold is still active provenance infrastructure, not a
placeholder receipt.

## Consequences

- Every grown mechanics package now has a visible place for source-to-active
  accounting.
- `PROVENANCE.md` can point to a real legacy district instead of describing
  legacy as absent.
- Empty raw inventory is explicit and testable.
- Future-looking receipt work belongs in package `ROADMAP.md`; current
  provenance docs describe the present bridge and inventory state.
- Raw legacy files must not become the only place current active behavior
  lives.

## Verification

Verify with:

Verification was routed through the targeted owner checks and repository validation lanes.
