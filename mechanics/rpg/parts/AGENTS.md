# AGENTS.md

## Applies to

This card applies to `mechanics/rpg/parts/` and every descendant unless a nearer
`AGENTS.md` narrows the path.

## Role

`parts/` holds the active RPG anchor maps for this repo. Each part names one
local pressure area and the stronger owner boundaries around it.

## Read before editing

Read:

1. repository root `AGENTS.md`
2. `mechanics/AGENTS.md`
3. `mechanics/rpg/AGENTS.md`
4. `mechanics/rpg/PARTS.md`
5. the touched part README, schema, example, script, report, or test

## Boundaries

- Parts map candidate pressure. They do not create technique canon.
- Part READMEs may cite existing technique bundles and mechanics surfaces, but
  they must not move source truth out of those homes.
- If a part becomes an executable, repeatable practice, promote one atomic
  move into `techniques/` instead of expanding the part indefinitely.
- RPG language remains adjunct to owner truth, proof, memory, routing, runtime,
  role, skill, playbook, and quest authority.

## Validation

Run:

```bash
python -m unittest discover -s mechanics/rpg/tests
```

## Closeout

Report the mechanic package, part, legacy surface, or helper changed;
whether source, generated, schema, example, or test surfaces moved; checks run;
checks skipped; and the next owner route.
