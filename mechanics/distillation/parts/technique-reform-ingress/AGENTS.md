# AGENTS.md

## Applies to

This card applies to
`mechanics/distillation/parts/technique-reform-ingress/` and every descendant
unless a nearer `AGENTS.md` narrows the path.

## Role

`technique-reform-ingress/` is the active Distillation part for bounded reform
waves over technique classification, selection, topology scouting, tree
projection, template posture, execution-profile scouting, portability bridge,
and owner-boundary bridge review.

The part README is the current contour and route index. Review packets are
authored human-review memory. Config, data, scripts, and reports each have
nearer cards for their local generated or builder surfaces.

Keep command authority here or in the nearer local card. Part README and review
packets may point to this card for current validation lanes. Historical review
packets may preserve exact commands only as evidence or receipt content, not as
current agent-local command law.

## Read before editing

Read:

1. repository root `AGENTS.md`
2. `DESIGN.md`
3. `DESIGN.AGENTS.md`
4. `mechanics/AGENTS.md`
5. `mechanics/distillation/AGENTS.md`
6. `mechanics/distillation/PARTS.md`
7. this part README
8. the nearest local `AGENTS.md` for `config/`, `data/`, `reports/`,
   `reviews/`, or `scripts/` when touching that district

## Boundaries

- Do not treat a reform review, scout report, tree projection, or working plan
  as technique source truth.
- Do not hand-edit generated reports or reader mirrors when a builder owns
  the surface.
- Do not promote scout axes such as `family`, `execution_profile`, or richer
  relations into schema or frontmatter truth from this part alone.
- Do not let this part claim skill execution, eval verdict, routing product,
  memory truth, KAG graph authority, playbook choreography, runtime behavior,
  or sibling-owner acceptance.
- Do not put reusable technique meaning only in review prose; repair or extend
  the source-authored technique bundle when the atom itself changes.
- Do not put current validation command lanes in the part README. Keep them in
  this card or the nearer district card.

## Validation

For review-only or README contour changes, run:

```bash
python -m unittest discover -s mechanics/distillation/tests
python scripts/validate_repo.py
```

For generated report, tree, topology, capsule, catalog, or public reader
changes, also run the owning builder or the release gate:

```bash
python scripts/release_check.py
```

For AGENTS coverage or route-card changes under this part, also run:

```bash
python scripts/validate_agents_md_shape.py
python scripts/validate_agents_mesh.py
python scripts/build_agents_mesh_index.py --check
python scripts/validate_agents_mesh_index.py
```

## Closeout

Report which reform lane changed, whether source, review, config, data,
script, report, generated, test, or AGENTS surfaces moved, which checks ran,
which checks were skipped, whether command authority stayed in AGENTS, and the
next owner route.
