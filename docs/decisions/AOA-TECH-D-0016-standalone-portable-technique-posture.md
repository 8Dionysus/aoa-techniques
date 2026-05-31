# Standalone Portable Technique Posture

Status: accepted
Date: 2026-05-01

## Index Metadata

- Decision ID: AOA-TECH-D-0016
- Original date: 2026-05-01
- Surface classes: root/topology, public status
- Technique axes: standalone portability
- Mechanic parents: none
- Guard families: root surface, public-safety
- Posture: accepted

## Context

`aoa-techniques` is both part of OS Abyss and a public practice canon. The
project should support builders who want to reuse only the techniques in their
own agent systems without deploying the whole AoA ecosystem.

The repository already treats techniques as bounded and portable, but the
standalone consumption contract needed to be explicit so future mechanics,
generated surfaces, and sibling-repo bridges do not accidentally make OS Abyss a
hidden dependency.

## Decision

Record a dual posture for `aoa-techniques`:

- as a standalone public library, each technique, capsule, or bundle should be
  understandable and reusable outside OS Abyss
- as an AoA organ, the same authored sources keep stable IDs, topology,
  provenance, review posture, mechanics, and generated surfaces for sibling
  repos

AoA references may explain source ownership, provenance, owner boundaries, and
integration routes. They should not be required for the core technique to be
executed by an external agent system after that system supplies its own local
context and orchestration.

## Consequences

Future technique authoring and mechanics work should keep portable practice
distinct from AoA-only integration detail. Mechanics references should make
clear whether sibling material is provenance, optional integration context, or a
required owner handoff.

This does not weaken AoA ownership. It keeps the authored practice useful both
inside OS Abyss and outside it.
