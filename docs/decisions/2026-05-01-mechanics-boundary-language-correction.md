# Mechanics Boundary Language Correction

Status: accepted
Date: 2026-05-01

## Context

The previous mechanics pass correctly noticed a real boundary problem:
`aoa-techniques` needs to remain portable as a public technique library while
also participating in OS Abyss and AoA mechanics. The implementation overdid
that insight by turning the boundary concern into repeated
`Law/Local/Bridge` prose blocks.

That shape was too heavy for this repository. `Agents-of-Abyss` keeps many of
these boundaries legible through concise owner split, route cards, part maps,
provenance surfaces, and stop-lines; it does not force every active section to
restate the same three-part formula.

## Decision

Remove the universal `Law/Local/Bridge` prose pattern from active mechanics
route surfaces. Keep the actual boundary intent in lighter language:

- name the stronger owner when a mechanics surface depends on external
  authority
- keep AoA-only context out of the portable technique core
- preserve provenance and stop-lines where candidate movement needs them
- do not let registry metadata become a required README section shape

Distillation registries may keep compact boundary fields for now because they
validate candidate movement and do not by themselves publish technique canon.
Those fields are route metadata, not an instruction to copy the same block into
every mechanic.

## Consequences

The active mechanics pages become shorter and more natural. Future mechanics
work should preserve the idea through owner routing, provenance, and candidate
gates instead of by inserting a named block wherever a boundary exists.

This does not weaken portability or owner separation. It makes the separation
less theatrical and easier to read.
