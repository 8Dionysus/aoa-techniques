# AGENTS.md

## Applies to

This card applies to `docs/` and all descendants unless a nearer `AGENTS.md`
narrows the path.

## Role

`docs/` holds current doctrine, route contracts, reader maps, generated-reader
interpretation, release guidance, and public review posture for the technique
canon.

It does not own technique bundle meaning, generated output meaning, mechanic
package behavior, or sibling-repo authority.

## Read before editing

Read root `AGENTS.md`, `README.md`, `CHARTER.md`, `DESIGN.md`,
`DESIGN.AGENTS.md`, and `docs/START_HERE.md` before broad docs changes.

For root or docs-root placement, read `docs/ROOT_SURFACE_LAW.md`. For agent
mesh work, read `docs/guardrails/AGENTS_MESH_PROTOCOL.md` and
`docs/guardrails/AGENTS_MESH_INDEX.md`.

## Boundaries

- Keep flat docs current and route-oriented; move historical evidence to
  decisions, legacy, mechanic-local lineage, or generated surfaces.
- Do not duplicate technique meaning outside the source bundle.
- Do not let generated-reader docs become source authority.
- Do not import skill, eval, routing, memory, playbook, role, runtime, stats,
  ToS, or AoA-center truth into this repo.

## Validation

Run the narrowest relevant checks. Common docs paths include:

```bash
python scripts/build_repo_doc_surface_manifest.py
python scripts/validate_agents_md_shape.py
python scripts/validate_agents_mesh.py
python scripts/validate_repo.py
```

For broad route, release, generated, or public-facing changes, run:

```bash
python scripts/release_check.py
```

## Closeout

Report changed docs, source surfaces consulted, generated readers rebuilt or
left untouched, checks run, checks skipped, remaining route risk, and whether a
decision note was added or judged unnecessary.
