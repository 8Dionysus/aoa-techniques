# AGENTS.md

## Applies to

This card applies to `scripts/validators/` and all validator owner modules
inside it.

## Role

`scripts/validators/` owns repo-local validator implementation modules for
`scripts/validate_repo.py`.

`scripts/validate_repo.py` remains the compatibility CLI and re-export adapter.
The owner modules here carry rule implementation:

- `common.py` stores shared models, constants, schema parsing, and parser
  helpers.
- `source_contracts.py` validates authored technique and repo-source contracts.
- `projection_parity.py` is a compatibility re-export facade for projection
  validators.
- `projection_catalog.py` validates catalog, reader, review-template, repo-doc,
  kind, capsule, section, checklist, example, and evidence-note parity.
- `projection_decisions.py` validates generated decision index parity.
- `projection_agents_mesh.py` validates generated AGENTS mesh parity.
- `projection_mechanics.py` validates mechanic report projections.
- `projection_kag.py` validates KAG export parity.
- `projection_intelligence.py` validates Technique Intelligence registry, DAG,
  and reader parity.
- `questbook.py` validates quest source topology and quest projections.
- `public_hygiene.py` validates public surface hygiene.
- `orchestrator.py` owns validate-repo call order and status output.

## Read before editing

Read root `AGENTS.md`, `scripts/AGENTS.md`,
`docs/validation/VALIDATOR_TOPOLOGY.md`,
`docs/validation/validator_inventory.json`, and the source or generated
surface consumed by the validator you are changing.
Read `README.md` only when the selected task needs its human map; do not preload unrelated maps.

## Boundaries

- Keep `scripts/validate_repo.py` thin; do not put rule logic back into the
  adapter.
- Do not duplicate one rule across owner modules. Move the rule to the module
  that owns the source boundary it protects.
- Generated validators in `projection_*.py` check rebuild parity only. They
  must not define technique source meaning, frontmatter truth, or route
  doctrine.
- Source validators in `source_contracts.py` may collect and interpret authored
  source, but they should not own generated freshness.
- `orchestrator.py` may order checks and print status, but it should not own
  individual rule semantics.

## Validation

Select the narrowest owner route: `source-fast` for focused source/validator work; add `generated` for projections. See [VALIDATION.md](../../VALIDATION.md); exact order is `config/validation_lanes.json`; focused procedure stays with the nearest owner. Report checks, skips, and blockers.

## Closeout

Report which validator owner module changed, whether the change touched source
meaning or projection parity, and exactly which focused and release checks ran.
