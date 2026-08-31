# AGENTS.md

## Applies to

This card applies to `generated/` and all descendants unless a nearer
`AGENTS.md` narrows the path.

## Role

`generated/` stores committed derived reader surfaces built from authored
sources elsewhere in the repository.

Representative surfaces include `generated/technique_catalog.json`,
`generated/technique_promotion_readiness.min.json`,
`generated/technique_capsules.json`, `generated/repo_doc_surface_manifest.json`,
`generated/kag_export.json`, `generated/agents_mesh.min.json`, the section and
checklist manifests, the example and evidence-note manifests, and the
semantic/shadow review manifests.
The OS Abyss artifact envelope for `generated/kag_export.min.json` lives under
`docs/source-lift/artifact-bundles/`; it validates transport provenance without
making the generated capsule stronger than authored technique bundles.

## Read before editing

Read root `AGENTS.md`, the local source doc or builder that owns the generated
surface, and `docs/START_HERE.md`.

For AGENTS mesh mirrors, read `DESIGN.AGENTS.md`,
`docs/guardrails/AGENTS_MESH_PROTOCOL.md`, `config/agents_mesh.json`, and
`scripts/build_agents_mesh_index.py`.
Read `README.md` only when the selected task needs its human map; do not preload unrelated maps.

## Boundaries

- Do not hand-edit files in this directory as if they were canonical prose.
- Change the owning source object or generator, then regenerate the derived
  output.
- Keep minified and full surfaces aligned where both exist.
- Keep generated wording subordinate to authored bundle meaning, docs meaning,
  and review meaning.
- Do not treat candidate-bridge indexes or AGENTS mesh mirrors as promoted
  technique catalogs or canonical practice bundles.
- Do not store secret-bearing exports or hidden provenance.

## Validation

Select the narrowest owner route: `source-fast` for source routes; add `generated` for declared projections. See [VALIDATION.md](../VALIDATION.md); exact order is `config/validation_lanes.json`; focused procedure stays with the nearest owner. Report checks, skips, and blockers.

## Closeout

Report generated surfaces rebuilt, source surfaces or builders changed,
freshness checks run, freshness checks skipped, and whether any generated
mirror still carries migration status.
