# AGENTS.md

Route card for the `aoa-techniques/mechanics/rpg/` package.

## Purpose

`mechanics/rpg/` owns the `aoa-techniques` side of RPG-shaped practice
pressure: feat reflection, progression language, quest overlays, and owner
handoffs that may help agents read technique work without mutating technique
canon.

This package is candidate-only. It is not the AoA center RPG mechanic, not a
runtime ledger, not a role system, and not a proof or quest authority.

## Owner Lane

This package owns:

- local anchors from RPG-shaped pressure to existing technique bundles and
  mechanics surfaces
- source-boundary notes that keep RPG vocabulary below owner truth
- feat, progression, and quest-overlay mapping that may later distill into
  smaller technique bundles
- handoff notes to stronger AoA owners when the pressure stops being a
  technique-layer concern

It does not own:

- AoA center RPG law, which belongs in `Agents-of-Abyss`
- role canon or actor identity, which belongs in `aoa-agents`
- skill execution truth, which belongs in `aoa-skills`
- scenario or campaign choreography, which belongs in `aoa-playbooks`
- proof verdicts, which belong in `aoa-evals`
- memory or chronicle canon, which belongs in `aoa-memo`
- runtime state, unlock ledgers, or session behavior, which belongs in
  `abyss-stack`
- technique bundle meaning, which belongs in `techniques/**/TECHNIQUE.md`

## Start Here

1. Read the repository root `AGENTS.md`, then `mechanics/AGENTS.md`.
2. Read `README.md`, `DIRECTION.md`, `PARTS.md`, and `PROVENANCE.md`.
3. Read the part README for the touched path.
4. When changing status, read `LANDING_LOG.md` and `ROADMAP.md`.
5. When promoting a reusable practice, route it through
   `techniques/**/TECHNIQUE.md` and the normal canonical review path.

## Local Law

- RPG language here is a reader and reflection aid. It must not become hidden
  ontology, rank, permission, routing authority, proof authority, or runtime
  state.
- The local package can map existing techniques and mechanics pressure. It
  must not copy the AoA center RPG mechanic or rewrite sibling owner law.
- A feat, unlock, quest hook, campaign hint, or chronicle cue stays adjunct
  unless a stronger owner accepts it in its own surface.
- Generated reader surfaces remain evidence or projection, not source truth.
- Stable local practice must become a bounded technique bundle before it can
  claim reusable canon.

## Verify

After changing this package, run:

```bash
python -m unittest tests.test_rpg_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
```

If nested AGENTS coverage changes, also run:

```bash
python scripts/validate_nested_agents.py
```
