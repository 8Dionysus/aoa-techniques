# Changelog

All notable changes to `aoa-techniques` will be documented in this file.

The format is intentionally simple and human-first.

## [0.1.0] - 2026-03-17

First public baseline release.

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
