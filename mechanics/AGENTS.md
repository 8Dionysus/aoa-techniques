# AGENTS.md

## Applies to

This card applies to `mechanics/` and all descendants unless a nearer
`AGENTS.md` narrows the path.

## Role

`mechanics/` owns reusable practice-motion surfaces for `aoa-techniques`.
These files describe how practice moves through the repo by participating in
cross-project AoA mechanics: method-growth, distillation, audit, growth-cycle,
Agon, recurrence, experience, release-support, antifragility, checkpoint, and
boundary-bridge, questbook, and RPG.

Mechanics are not canonical technique bundles. They shape the route into or
around canon, while `techniques/` owns published technique content and
`generated/` owns derived reader evidence.

## Owner lane

This surface owns:

- owner-local movement grammar for candidate-to-technique flow inside the AoA
  mechanics vocabulary
- bounded intake, promotion, adoption, mastery, recurrence, release-support,
  experience, antifragility, checkpoint, boundary-bridge, questbook, and RPG
  routes
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

## Read before editing

1. Read the repository root `AGENTS.md`, `README.md`, `ROADMAP.md`, and
   `docs/START_HERE.md`.
2. Read `docs/TECHNIQUE_ATOM_CONTRACT.md`,
   `docs/TECHNIQUE_TOPOLOGY_CONTRACT.md`, and `mechanics/README.md`.
3. If the work cites an AoA center-side `ORQ-*` request or downstream owner
   request, read `mechanics/REQUEST_RECEIPTS.md`.
4. Read the nearest package README for the touched path, starting with its
   local `Mechanic card`.
5. If the package has `DIRECTION.md`, `PARTS.md`, `PROVENANCE.md`, `legacy/`,
   or `parts/`, use those active route surfaces before opening raw legacy.
6. For status, release, or promotion changes, also read
   `docs/review/CANONICAL_RUBRIC.md`, `docs/review/CANONICAL_REVIEW_GUIDE.md`, and
   `docs/RELEASING.md`.

## Boundaries

- Mechanics may route, constrain, stage, and prepare movement, but they do not
  silently promote candidates into canon.
- Every cross-repo handoff must name the owner and stop-line rather than
  importing that owner's authority into this repo.
- When a mechanics surface points to another AoA owner, name the owner route
  and stop-line only as much as the current surface needs. Do not import sibling
  authority or turn boundary notes into a local doctrine block.
- Package README cards use `Local owns`, not `Center owns`: `aoa-techniques`
  names its technique-layer authority, then routes stronger law or acceptance
  to `Agents-of-Abyss`, `REQUEST_RECEIPTS.md`, `PROVENANCE.md`, or the sibling
  owner only when relevant.
- Package README cards do not carry validation command lanes. Keep validation
  in the nearest `AGENTS.md` so package cards stay source-oriented and local
  checks stay operational.
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
- Grown mechanics packages should keep a `legacy/` scaffold even when raw
  inventory is empty. Use it as the provenance district and source-to-active
  bridge, not as a placeholder receipt store.
- When a package grows beyond a simple README, prefer the AoA split:
  `DIRECTION.md`, `PARTS.md`, `PROVENANCE.md`, `LANDING_LOG.md`, `parts/`, and
  `legacy/`, one mechanic at a time.
- Package `ROADMAP.md` files should name current contour, next work,
  condition-based later triggers, and stop-lines without becoming landing logs
  or raw ledgers.
- Root `ROADMAP.md` owns repo-level mechanics-to-canon direction. Package
  `ROADMAP.md` files own package-local future pressure.
- New top-level mechanics should match the AoA cross-project mechanics unless a
  repo-local mechanic is explicitly justified in a decision note.
- If a mechanics surface becomes a reusable practice unit with stable inputs,
  outputs, risks, and validation, promote it into `techniques/` through the
  normal review path instead of letting it sprawl here.

## Validation

Use the root validation path after changes:

```bash
python scripts/validate_repo.py
python scripts/run_tests.py
```

If Agon binding candidates, questbook references, RPG references, manifests, or
generated reader surfaces change, run their named builders or validators before
closeout.

## Closeout

Report the mechanic package, part, request receipt, provenance, generated
surface, or test lane changed; source surfaces consulted; checks run; checks
skipped; and whether any candidate should move toward a technique bundle,
remain mechanics-owned, or route to a sibling AoA owner.
