# Repo Doc Surface Lift Guide

This guide defines the bounded contract for lifting the repository's authoritative public docs/status layer into one manifest pair and one generated reader surface.

Use it when the question is not about technique bundles themselves, but about which authored public repo doc should anchor navigation, contribution, safety, or release/status lookup.

This source class stays repo-surface-first. It does not add new schema fields, new frontmatter, or a new `kag` domain.

See also:
- [Start Here](START_HERE.md)
- [Documentation Map](README.md)
- [KAG Source Lift Guide](KAG_SOURCE_LIFT_GUIDE.md)
- [`source-of-truth-layout`](../techniques/docs/source-of-truth-layout/TECHNIQUE.md)
- [`lightweight-status-snapshot`](../techniques/docs/lightweight-status-snapshot/TECHNIQUE.md)
- [`markdown-technique-section-lift`](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md)

This family uses one stable shape:

- authoritative source: the current bounded set of authored public docs/status files
- reader companion: `docs/REPO_DOC_SURFACES.md`
- derived manifests: `generated/repo_doc_surface_manifest.json` and `generated/repo_doc_surface_manifest.min.json`
- what it must not become: a status-policy engine, release-policy engine, or catch-all docs index for deeper guides

## Bounded Source Set

For this first docs/status wave, the authoritative source set is exactly:

- `README.md`
- `docs/START_HERE.md`
- `TECHNIQUE_INDEX.md`
- `AGENTS.md`
- `CONTRIBUTING.md`
- `SECURITY.md`
- `WALKTHROUGH.md`
- `CODE_OF_CONDUCT.md`
- `CHANGELOG.md`
- `docs/README.md`
- `docs/RELEASING.md`

## Reader Companion And Derived Manifests

The generated outputs for this source class are:

- `generated/repo_doc_surface_manifest.json`
- `generated/repo_doc_surface_manifest.min.json`
- `docs/REPO_DOC_SURFACES.md`

Those outputs stay derived from authored markdown. They are routing aids only.

## Manifest Contract

Each manifest entry stays small and explicit:

- `doc_id`
- `doc_path`
- `title`
- `surface_group`
- `bounded_role`
- `top_level_sections`

The current surface groups are:

- `entrypoint/map`
- `contribution/policy`
- `walkthrough/context`
- `status/release`

## Boundaries

Not part of this current docs/status wave:

- local planning docs such as `TODO.md`, `PLANS.md`, and `ROADMAP.md`
- deeper guide docs beyond `docs/START_HERE.md`, `docs/README.md`, and `docs/RELEASING.md`
- semantic-review and shadow-review markdown docs
- a new source of truth for repo status
- a status-policy engine, release-policy engine, or graph layer

The meaning remains in the authored docs themselves.

## Validation

Regenerate and verify this source class with:

- `python scripts/build_repo_doc_surface_manifest.py`
- `python scripts/release_check.py`
- `python -m unittest discover -s tests`
- `python scripts/validate_repo.py`
