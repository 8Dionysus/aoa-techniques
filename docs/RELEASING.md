# Releasing `aoa-techniques`

This repository is released as a public documentation-and-technique corpus.

Releases should stay small, explicit, and easy to verify.

See also:
- [Documentation Map](README.md)
- [Technique Capsule Guide](TECHNIQUE_CAPSULE_GUIDE.md)
- [CHANGELOG](../CHANGELOG.md)

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
   - `python scripts/build_repo_doc_surface_manifest.py`
   - `python scripts/build_catalog.py`
   - `python scripts/build_capsules.py`
   - `python scripts/build_section_manifest.py`
   - `python scripts/build_checklist_manifest.py`
   - `python scripts/build_example_manifest.py`
   - `python scripts/build_evidence_note_manifest.py`
   - `python scripts/build_github_review_template_manifest.py`
   - `python scripts/build_semantic_review_manifest.py`
   - `python scripts/build_shadow_review_manifest.py`
   - `python -m unittest discover -s tests`
   - `python scripts/validate_repo.py`
   - `git diff --exit-code`
4. Confirm `TECHNIQUE_INDEX.md` matches the current published catalog.
5. Confirm generated docs and manifests are up to date if the release includes generated artifacts.
   - This now includes the local runtime capsule family: `generated/technique_capsules.json`, `generated/technique_capsules.min.json`, and `docs/TECHNIQUE_CAPSULES.md`.
   - Use `TECHNIQUE_CAPSULE_GUIDE.md` as the authored contract reference when checking that the runtime card family stayed bounded.
   - This now also includes the KAG/source-lift reader companions for sections, checklists, examples, and evidence notes:
     - `generated/technique_section_manifest.json` and `docs/TECHNIQUE_SECTIONS.md`
     - `generated/technique_checklist_manifest.json` and `docs/TECHNIQUE_CHECKLISTS.md`
     - `generated/technique_example_manifest.json` and `docs/TECHNIQUE_EXAMPLES.md`
     - `generated/technique_evidence_note_manifest.json` and `docs/EVIDENCE_NOTE_SURFACES.md`
   - Use `TECHNIQUE_SECTION_LIFT_GUIDE.md`, `TECHNIQUE_CHECKLIST_LIFT_GUIDE.md`, `TECHNIQUE_EXAMPLE_LIFT_GUIDE.md`, and `EVIDENCE_NOTE_PROVENANCE_GUIDE.md` as the authored contract references when checking that those KAG/source-lift reader families stayed bounded.
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
