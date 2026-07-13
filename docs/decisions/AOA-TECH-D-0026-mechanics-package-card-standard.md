# Mechanics Package Card Standard

Status: accepted

Date: 2026-05-03

## Index Metadata

- Decision ID: AOA-TECH-D-0026
- Original date: 2026-05-03
- Surface classes: mechanic package
- Technique axes: mechanic bridge
- Mechanic parents: none
- Guard families: mechanic topology
- Posture: accepted

## Context

After the mechanics split, active/legacy scaffolding, and owner-request receipt
work, the mechanics packages had the right files but uneven entry shapes. Some
package READMEs already behaved like agent-operable cards; others still opened
with a thin route list or a package-specific gate.

`Agents-of-Abyss` now provides the architectural example for mechanics cards:
trigger, owned authority, stronger owner split, inputs, outputs, stop-lines,
validation, and next route. Copying that shape directly into `aoa-techniques`
would be wrong, because this repository is not the constitutional center. It is
the technique-canon organ and must stay usable as a standalone public technique
library.

The earlier repeated law/local/bridge wording also showed the risk: boundary
separation helps, but heavy blocks in every README make the route feel imposed
rather than useful.

## Options

- Leave package READMEs uneven and rely on `DIRECTION.md`, `PARTS.md`, and
  `PROVENANCE.md` for deeper orientation.
- Copy the AoA center mechanic-card headings directly, including `Center owns`.
- Adopt the center card shape but translate its authority into an owner-local
  `aoa-techniques` card.

## Decision

Adopt a local package-card standard for every `mechanics/<slug>/README.md`.

The local headings are:

- `## Mechanic card`
- `### Trigger`
- `### Local owns`
- `### Stronger owner split`
- `### Inputs`
- `### Outputs`
- `### Must not claim`
- `### Validation`
- `### Next route`

`mechanics/README.md` owns the package-card standard. `mechanics/AGENTS.md`
routes agents through the nearest package card before active parts or legacy.
Package READMEs use `Local owns`, not `Center owns`, because
`aoa-techniques` names its technique-layer authority and routes stronger law or
acceptance to `Agents-of-Abyss`, `mechanics/REQUEST_RECEIPTS.md`,
`PROVENANCE.md`, or the sibling owner only when relevant.
When a package is named in `mechanics/REQUEST_RECEIPTS.md`, its card status
should mirror the local receipt posture such as `mapped-with-local-evidence` or
`candidate-only` without changing the center queue.

This decision does not add package-local `OWNER_MAP.md`, `OWNER_REQUESTS.md`,
or a mechanics registry to `aoa-techniques`. Those center-side mechanisms stay
in `Agents-of-Abyss` unless a future owner-local need is proven.

## Consequences

- Future agents can enter any mechanics package with the same compact question
  set before opening parts or provenance.
- The packages become longer, but the added text is bounded to routing,
  ownership, inputs, outputs, stop-lines, validation, and next route.
- AoA center law remains upstream; local package cards do not import it as
  implementation authority.
- Direct center requests still route through `mechanics/REQUEST_RECEIPTS.md`.
  Candidate-only pressure stays candidate-only until a local owner surface and
  proof route actually land.
- New mechanics packages should include the card headings before they grow
  active parts or legacy scaffolds.

## Verification

The package-card standard is covered by
`mechanics/tests/test_mechanics_package_cards.py`.

Verify with:

Verification was routed through the targeted owner checks and repository validation lanes.
