# AGENTS.md

Route card for `aoa-techniques/mechanics/rpg/parts/`.

## Purpose

`parts/` holds the active RPG anchor maps for this repo. Each part names one
local pressure area and the stronger owner boundaries around it.

## Local Law

- Parts map candidate pressure. They do not create technique canon.
- Part READMEs may cite existing technique bundles and mechanics surfaces, but
  they must not move source truth out of those homes.
- If a part becomes an executable, repeatable practice, promote one atomic
  move into `techniques/` instead of expanding the part indefinitely.
- RPG language remains adjunct to owner truth, proof, memory, routing, runtime,
  role, skill, playbook, and quest authority.

## Verify

Run:

```bash
python -m unittest discover -s mechanics/rpg/tests
```
