# 2026-05-03 - Root source-of-truth topology

## Index Metadata

- Decision ID: AOA-TECH-D-0033
- Original date: 2026-05-03
- Surface classes: root/topology
- Technique axes: topology
- Mechanic parents: none
- Guard families: root surface
- Posture: accepted

## Context

`aoa-techniques` had grown a strong body of technique contracts, generated
surfaces, mechanics packages, and public route docs. The root markdown layer was
still carrying too much mixed responsibility: public entry, repository
authority, direction, audit history, corpus maps, generated routing, and
mechanic pointers were all visible, but the authority split was not as clean as
the current AoA root architecture.

The repository also needs a dual posture: it is an AoA organ, but it must stay
usable as a standalone public library of compact techniques.

## Options

- Keep the current root shape and patch wording in place.
- Copy the Agents-of-Abyss root architecture directly.
- Adapt the AoA pattern by adding a local charter and root-surface law, then
  slim root direction while preserving audit history under Audit legacy.

## Decision

Use the adapted AoA pattern.

Add `CHARTER.md` as the repository authority boundary and
`docs/ROOT_SURFACE_LAW.md` as the placement law for root and docs-root
surfaces.

Keep root `ROADMAP.md` as live repo-level direction and move the previous
closure-audit roadmap to
`mechanics/audit/legacy/raw/ROOT_CLOSURE_AUDIT_ROADMAP_2026-05-03.md`.

Update repo-doc source-lift surfaces so the public route/canon/status layer
names the new authority files rather than leaving them implicit.

## Rationale

`aoa-techniques` should not become a miniature `Agents-of-Abyss` center. It owns
reusable practice, not constitutional federation law. But it does need the same
discipline: public entry, authority boundary, root placement, direction,
obligations, release history, generated companions, and mechanic evidence must
not silently replace one another.

Keeping the old closure audit under Audit legacy preserves provenance without
making historical audit accounting the live root roadmap.

## Consequences

- Future root markdown changes should start from `CHARTER.md` and
  `docs/ROOT_SURFACE_LAW.md`.
- Root `ROADMAP.md` should stay compact and directional.
- Audit details should live in Audit parts, landing logs, provenance, or legacy
  raw receipts.
- Generated repo-doc manifests must include the authority surfaces and remain
  routing aids only.
- The standalone public-library posture stays explicit alongside AoA organ
  posture.
