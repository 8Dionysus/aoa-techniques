# AGENTS.md

Route card for the `aoa-techniques/mechanics/` surface.

## Purpose

`mechanics/` owns reusable practice-motion surfaces for `aoa-techniques`.
These files describe how practice moves through the repo by participating in
cross-project AoA mechanics: method-growth, distillation, audit, growth-cycle,
Agon, recurrence, experience, release-support, antifragility, checkpoint, and
boundary-bridge, and questbook.

Mechanics are not canonical technique bundles. They shape the route into or
around canon, while `techniques/` owns published technique content and
`generated/` owns derived reader evidence.

## Owner lane

This surface owns:

- owner-local movement grammar for candidate-to-technique flow inside the AoA
  mechanics vocabulary
- bounded intake, promotion, adoption, mastery, recurrence, release-support,
  experience, antifragility, checkpoint, boundary-bridge, and questbook routes
- public-safe stop-lines for deciding when a surface must hand off to another
  AoA repo
- reusable precedent notes that are too procedural for general `docs/` but not
  yet technique bundles

It does not own:

- canonical technique bundle meaning, which belongs under `techniques/`
- generated catalogs, manifests, cards, or export truth, which belongs under
  `generated/` and the scripts that build it
- skill execution workflows, which belong in `aoa-skills`
- portable proof/eval authority, which belongs in `aoa-evals`
- scenario composition, quests, or campaign ownership outside repo-local
  questbook references
- AoA constitutional doctrine, which belongs in `Agents-of-Abyss`

## Start here

1. Read the repository root `AGENTS.md`, `README.md`, `ROADMAP.md`, and
   `docs/START_HERE.md`.
2. Read `docs/TECHNIQUE_ATOM_CONTRACT.md`,
   `docs/TECHNIQUE_TOPOLOGY_CONTRACT.md`, and `mechanics/README.md`.
3. If the work cites an AoA center-side `ORQ-*` request or downstream owner
   request, read `mechanics/REQUEST_RECEIPTS.md`.
4. Read the nearest package README for the touched path.
5. If the package has `DIRECTION.md`, `PARTS.md`, `PROVENANCE.md`, `legacy/`,
   or `parts/`, use those active route surfaces before opening raw legacy.
6. For status, release, or promotion changes, also read
   `docs/CANONICAL_RUBRIC.md`, `docs/CANONICAL_REVIEW_GUIDE.md`, and
   `docs/RELEASING.md`.

## Local law

- Mechanics may route, constrain, stage, and prepare movement, but they do not
  silently promote candidates into canon.
- Every cross-repo handoff must name the owner and stop-line rather than
  importing that owner's authority into this repo.
- When a mechanics surface points to another AoA owner, name the owner route
  and stop-line only as much as the current surface needs. Do not import sibling
  authority or turn boundary notes into a local doctrine block.
- When a mechanics surface answers an AoA center-side owner request, keep the
  local receipt in `mechanics/REQUEST_RECEIPTS.md` and do not treat the request
  packet as local acceptance or landing.
- Before a mechanics candidate becomes a technique bundle, the active surface
  should be able to name the atomic move, likely `domain`, likely `kind`,
  likely family or reason no family is stable yet, capability class, substrate,
  execution profile, risk posture, and nearest relation or conflict points.
- Evidence and donor material must stay public-safe, source-linked, and
  reversible.
- Generated artifacts remain evidence, not authority.
- Legacy surfaces preserve source lineage. They are not trash archives, and they
  must not be the only place current active behavior lives.
- When a package grows beyond a simple README, prefer the AoA split:
  `DIRECTION.md`, `PARTS.md`, `PROVENANCE.md`, `LANDING_LOG.md`, `parts/`, and
  `legacy/`, one mechanic at a time.
- New top-level mechanics should match the AoA cross-project mechanics unless a
  repo-local mechanic is explicitly justified in a decision note.
- If a mechanics surface becomes a reusable practice unit with stable inputs,
  outputs, risks, and validation, promote it into `techniques/` through the
  normal review path instead of letting it sprawl here.

## Verify

Use the root validation path after changes:

```bash
python scripts/validate_repo.py
python -m unittest discover -s tests
```

If Agon binding candidates, questbook references, manifests, or generated
reader surfaces change, run their named builders or validators before closeout.
