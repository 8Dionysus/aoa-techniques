# AGENTS.md

## Applies to

This card applies to
`mechanics/distillation/parts/technique-reform-ingress/reviews/` and every
descendant unless a nearer `AGENTS.md` narrows the path.

## Role

`reviews/` holds authored review packets, closeout ledgers, repair receipts,
working-plan provenance, semantic review packets, and shadow review packets for
Technique Reform Ingress.

These files are evidence and human judgment memory. They can explain what was
read, what was repaired, what was deferred, and what validation evidence existed
when a lane landed. They do not own current command routes, generated report
truth, technique source truth, schema migration authority, or sibling-repo
acceptance.

New review prose should link current validation or rebuild instructions to this
card, the parent part `AGENTS.md`, or a nearer `config/`, `data/`, `reports/`,
or `scripts/` card. Keep exact commands inside review packets only when the
command is part of historical receipt evidence, a preserved superseded working
plan, or the review object's authored meaning.

## Read before editing

Read:

1. repository root `AGENTS.md`
2. `DESIGN.md`
3. `DESIGN.AGENTS.md`
4. `mechanics/AGENTS.md`
5. `mechanics/distillation/AGENTS.md`
6. `mechanics/distillation/parts/AGENTS.md`
7. `mechanics/distillation/parts/technique-reform-ingress/AGENTS.md`
8. the part README
9. the touched review packet family README when present

## Boundaries

- Do not convert a review packet into a current runbook or command lane.
- Do not preserve a temporary plan in a part root; keep superseded working
  plans here as provenance and point them to their durable closeout ledger.
- Do not hand-edit generated reports or generated reader mirrors from review
  prose.
- Do not claim frontmatter, schema, relation, topology, route, skill, eval,
  runtime, memory, KAG, playbook, or sibling-owner authority from a review
  packet.
- Do not let review evidence override `TECHNIQUE.md` source bundles, local
  contracts, or active route cards.

## Validation

For review-only changes, run:

```bash
python -m unittest discover -s mechanics/distillation/tests
python scripts/validate_repo.py
```

For review changes that alter generated/public reader interpretation, AGENTS
coverage, or release posture, also run the matching parent checks:

```bash
python scripts/release_check.py
python scripts/validate_agents_md_shape.py
python scripts/validate_agents_mesh.py
python scripts/build_agents_mesh_index.py --check
python scripts/validate_agents_mesh_index.py
```

## Closeout

Report the review packet family changed, whether a temporary working plan was
promoted, moved, retired, or preserved as provenance, whether any source or
generated surface moved, which checks ran, which checks were skipped, and where
current command authority lives.
