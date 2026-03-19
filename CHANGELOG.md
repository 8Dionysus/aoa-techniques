# Changelog

All notable changes to `aoa-techniques` will be documented in this file.

The format is intentionally simple and human-first.

## [Unreleased]

Mainline corpus growth and validator hardening after `v0.1.0`.

### Added

- `AOA-T-0014` through `AOA-T-0022`, bringing the published corpus to 22 techniques (`10` canonical, `12` promoted)
- the first public KAG/source-lift quartet inside the existing `docs` domain:
  - `AOA-T-0018 markdown-technique-section-lift`
  - `AOA-T-0019 frontmatter-metadata-spine`
  - `AOA-T-0020 evidence-note-provenance-lift`
  - `AOA-T-0021 bounded-relation-lift-for-kag`
- the first reusable markdown-first shadow/caution technique inside the existing `docs` domain:
  - `AOA-T-0022 risk-and-negative-effect-lift`

### Changed

- `SELECTION_PATTERNS.md` working sets are now validator-checked against their linked semantic review maps
- all published techniques now use the same richer `## Risks` subsection contract
- bounded public-hygiene validation now blocks obvious local paths, loopback-only hosts, and token or private-key markers on public-authored and generated surfaces
- `DOCS_BOUNDARY_SEMANTIC_REVIEW.md` and semantic review manifests now reflect that a richer relation consumer has already landed
- KAG-oriented repo guides now link directly to the corresponding reusable technique bundles for section lift, metadata spine, provenance lift, and bounded relation lift
- shadow/caution repo guides now point to `risk-and-negative-effect-lift` as the current reusable markdown-first caution implementation surface
- local validation no longer dirties `git status` with Python cache artifacts

### Validation

- `python -m unittest discover -s tests`
- `python scripts/validate_repo.py`
- `python scripts/build_catalog.py`
- `python scripts/build_semantic_review_manifest.py`

## [0.1.0] - 2026-03-17

First public baseline release.

This changelog entry uses the release-prep merge date.
The GitHub release for `v0.1.0` was published on `2026-03-18`.

### Added

- initial public release of `aoa-techniques` as a public library of reusable techniques for coding agents and humans
- repository entry documents: `README.md`, `AGENTS.md`, `CONTRIBUTING.md`, `SECURITY.md`, and `WALKTHROUGH.md`
- repository-wide technique map in `TECHNIQUE_INDEX.md`
- curated public technique catalog containing:
  - 9 `canonical` techniques
  - 4 `promoted` techniques
- public templates, schemas, and validation helpers for technique authoring and promotion

### Included in this release

- technique bundles under `techniques/`
- generated selection and semantic-review navigation surfaces referenced from `README.md`
- bounded KAG-oriented manifest pilot series for:
  - section manifests
  - checklist manifests
  - example manifests
  - evidence-note manifests
  - GitHub review template manifests
  - semantic review manifests

### Validation

Documented local validation path for this release:

- `python -m unittest discover -s tests`
- `python scripts/validate_repo.py`

### Notes

- this is the first public baseline release for the repository
- package publishing to PyPI, npm, or other registries is out of scope for `v0.1.0`
- release emphasis is the curated public technique corpus and its repo-level validation/documentation surface
