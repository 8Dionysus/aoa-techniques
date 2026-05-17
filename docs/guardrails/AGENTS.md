# AGENTS.md

## Applies to

This card applies to `docs/guardrails/` and every descendant unless a nearer
`AGENTS.md` narrows the path.

## Role

`docs/guardrails/` owns checkable guardrail law for repository route shape,
agent-card coverage, generated freshness hooks, and related validation posture.

It supports the technique canon. It does not author technique meaning,
mechanic truth, generated meaning, or sibling-owner authority.

## Read before editing

Read root `AGENTS.md`, `DESIGN.md`, `DESIGN.AGENTS.md`, `docs/AGENTS.md`, and
`docs/ROOT_SURFACE_LAW.md` before changing guardrail surfaces.

For AGENTS mesh work, also read:

- `AGENTS_MESH_PROTOCOL.md`
- `AGENTS_MESH_INDEX.md`
- `../../config/agents_mesh.json`
- `../../scripts/agents_mesh_common.py`

For docs-root topology or flat-surface cleanup, also read:

- `THEMATIC_DISTRICT_PROTOCOL.md`
- `CURRENT_SURFACE_INDEX.md`

For link, shape, or moved-path hygiene, also read:

- `LINK_AND_SHAPE_HYGIENE_PROTOCOL.md`
- `HYGIENE_GUARDRAIL_INDEX.md`

## Boundaries

- Do not add prose-only guardrails that release checks cannot observe.
- Do not let generated mirrors become source authority.
- Do not use guardrails to move technique, mechanic, proof, skill, routing,
  memory, playbook, runtime, or ToS truth into this repository.
- Do not hide durable directory growth without either a local `AGENTS.md` card,
  a registered exemption, or a documented temporary route.

## Validation

For AGENTS mesh changes, run:

```bash
python scripts/validate_agents_md_shape.py
python scripts/validate_agents_mesh.py
python scripts/build_agents_mesh_index.py --check
python scripts/validate_agents_mesh_index.py
```

For broader route, generated, or public-facing changes, run:

```bash
python -m unittest tests.test_docs_surface_guardrails
python scripts/release_check.py
```

## Closeout

Report changed guardrail surfaces, generated mirrors rebuilt or checked,
validators run, validators skipped, remaining canonical-shape risk, and whether
any future exception needs an explicit migration cleanup route.
