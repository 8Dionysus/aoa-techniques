# Releasing `aoa-techniques`

This repository is released as a public documentation-and-technique corpus.

Releases should stay small, explicit, and easy to verify.

## Release goals

A release should make it easy to answer:

- what changed
- why it matters
- how it was validated
- what is intentionally not included

## Recommended release flow

1. Confirm the target release scope.
2. Update `CHANGELOG.md`.
3. Run local validation:
   - `python -m unittest discover -s tests`
   - `python scripts/validate_repo.py`
4. Confirm `TECHNIQUE_INDEX.md` matches the current published catalog.
5. Confirm generated docs and manifests are up to date if the release includes generated artifacts.
6. Review public-safety hygiene:
   - no secrets
   - no internal-only URLs
   - no private infrastructure details
   - no raw sensitive logs
7. Merge the release-prep PR to `main`.
8. Create a Git tag such as `v0.1.0`.
9. Publish GitHub release notes using the matching changelog section or a clearly equivalent human-first shape.

## Release note shape

Recommended GitHub release note sections:

- summary
- added
- included in this release
- validation
- notes or not included

Exact headings do not need to be rigid, but the changelog entry and the published GitHub release should answer the same release-goal questions in roughly the same shape.

## Versioning guidance

Suggested interpretation:

- `0.x.y` for early public shaping and structure refinement
- `1.0.0` only when repository structure, contribution path, and validation surface feel stable enough to promise a durable public baseline

## What not to optimize yet

Do not overbuild release machinery too early.

For now, avoid:

- registry packaging theater without a real package artifact
- automated policy claims that exceed current validation
- heavyweight semantic version promises unsupported by the repo's current purpose

## Current stance

Right now, `aoa-techniques` is best released as:

- a curated public corpus
- a reusable technique library
- a validated repo structure
- a documented contribution and promotion path
