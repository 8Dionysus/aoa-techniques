# AGENTS.md

## Applies to

This card applies to `mechanics/questbook/` and every descendant unless a nearer
`AGENTS.md` narrows the path.

## Role

This package owns the `aoa-techniques` side of Questbook: local mechanics
pressure around durable technique obligations, quest source surfaces,
generated quest projections, and harvest/promotion routes that may later feed
technique canon.

It does not own AoA Questbook law, playbook choreography, closure proof,
memory canon, routing behavior, RPG playable reading authority, owner
acceptance, generated quest truth, or technique status changes.

## Read before editing

1. Root `AGENTS.md`.
2. `mechanics/AGENTS.md`.
3. `mechanics/questbook/README.md`.
4. `DIRECTION.md`, `PARTS.md`, `PROVENANCE.md`, and the touched part README.
5. `QUESTBOOK.md`, `quests/`, schemas, or generated quest projections only
   when the task touches their route or source/projection boundary.

## Boundaries

- Keep Questbook here technique-layered: durable obligations around canon
  hardening, donor follow-through, generated/source drift, and harvest
  candidates.
- Treat `QUESTBOOK.md` as the human index, lane-first `quests/` as repo-local
  source quest objects, and generated quest files as projections only.
- Do not move `QUESTBOOK.md`, root `quests/`, schemas, or generated
  projections into this package as part of mechanics cleanup.
- Do not import `Agents-of-Abyss` Questbook law as local implementation
  authority.
- Do not treat quests, generated quest views, route notes, owner requests, or
  harvest pressure as proof, owner acceptance, public closure, playbook truth,
  memory truth, routing authority, or automatic technique promotion.
- If a stable reusable practice emerges, route it into `techniques/` through
  the normal technique review path.

## Validation

Use the root validation path after changes:

```bash
python scripts/validate_repo.py
python scripts/run_tests.py
```

## Closeout

Report the mechanic package, part, legacy surface, or helper changed;
whether source, generated, schema, example, or test surfaces moved; checks run;
checks skipped; and the next owner route.
