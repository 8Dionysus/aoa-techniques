# Changelog

All notable changes to `aoa-techniques` will be documented in this file.

The format is intentionally simple and human-first.

## [Unreleased]

Mainline corpus growth and validator hardening after `v0.1.0`.

### Added

- `AOA-T-0014` through `AOA-T-0022`, bringing the published corpus to 22 techniques (`13` canonical, `9` promoted)
- the first public five-technique KAG/source-lift family inside the existing `docs` domain:
  - `AOA-T-0018 markdown-technique-section-lift`
  - `AOA-T-0019 frontmatter-metadata-spine`
  - `AOA-T-0020 evidence-note-provenance-lift`
  - `AOA-T-0021 bounded-relation-lift-for-kag`
  - `AOA-T-0022 risk-and-negative-effect-lift`

### Changed

- canon-strengthening wave now records explicit `canonical-readiness` outcomes across the non-KAG promoted target set, promotes `AOA-T-0004`, `AOA-T-0014`, and `AOA-T-0015` to `canonical`, and adds canonical-only `adverse-effects-review` notes for those newly promoted bundles
- KAG family maturity wave now adds `second-context-adaptation` plus `canonical-readiness` notes to `AOA-T-0018` through `AOA-T-0022`, keeps all five `promoted`, and adds `KAG_SOURCE_LIFT_SEMANTIC_REVIEW.md` as the shared family review surface
- `SELECTION_PATTERNS.md` working sets are now validator-checked against their linked semantic review maps
- new generated `docs/TECHNIQUE_CAPSULES.md` now provides a human reader surface over local runtime capsule cards grouped by domain and status order
- new generated `generated/technique_capsules.min.json` now keeps the capsule family on a strict min projection without replacing the full runtime payload
- new authored `docs/TECHNIQUE_CAPSULE_GUIDE.md` now defines the capsule source contract and runtime-only boundaries outside the KAG/source-lift family
- new generated `docs/REPO_DOC_SURFACES.md` now routes the authoritative public docs/status layer by bounded roles instead of filesystem guessing
- new generated `generated/repo_doc_surface_manifest.json` now lifts the 10 authoritative repo docs/status files into derived docs/status routing knowledge only
- new authored `docs/REPO_DOC_SURFACE_LIFT_GUIDE.md` now defines the bounded source contract and explicit exclusions for that docs/status layer
- new generated `docs/TECHNIQUE_SECTIONS.md`, `docs/TECHNIQUE_CHECKLISTS.md`, `docs/TECHNIQUE_EXAMPLES.md`, and `docs/EVIDENCE_NOTE_SURFACES.md` now provide reader-facing routing surfaces for the existing section, checklist, example, and evidence-note manifest families
- new authored `docs/TECHNIQUE_SECTION_LIFT_GUIDE.md`, `docs/TECHNIQUE_CHECKLIST_LIFT_GUIDE.md`, and `docs/TECHNIQUE_EXAMPLE_LIFT_GUIDE.md` now define the bounded contracts for those source classes, and `EVIDENCE_NOTE_PROVENANCE_GUIDE.md` now covers the evidence-note reader companion explicitly
- new generated `docs/SHADOW_PATTERNS.md` now provides one canonical-only shadow operating surface over typed `adverse_effects_review` notes
- new generated `generated/shadow_review_manifest.json` now lifts authored shadow-review docs into derived review knowledge without turning caution into policy metadata
- `EVALUATION_CHAIN_SHADOW_REVIEW.md` now adds the second canonical shadow-review pilot for `AOA-T-0003` and `AOA-T-0007`
- `docs/SHADOW_PATTERNS.md` now exposes both published-summary and evaluation-chain review-backed shadow working sets plus new evaluation-chain shadow questions
- the published-summary cluster now has an authored `PUBLISHED_SUMMARY_SHADOW_REVIEW.md` plus sharper caution wording across `AOA-T-0006`, `AOA-T-0008`, `AOA-T-0010`, and `AOA-T-0011`
- all published techniques now use the same richer `## Risks` subsection contract
- all `canonical` techniques now carry a typed `adverse_effects_review` note, and the evidence-note manifest exposes that canonical-only caution supplement without adding generated caution outputs
- bounded public-hygiene validation now blocks obvious local paths, loopback-only hosts, and token or private-key markers on public-authored and generated surfaces
- `DOCS_BOUNDARY_SEMANTIC_REVIEW.md` and semantic review manifests now reflect that a richer relation consumer has already landed
- KAG-oriented repo guides now link directly to the corresponding reusable technique bundles for section lift, metadata spine, provenance lift, and bounded relation lift
- shadow/caution repo guides now point to `risk-and-negative-effect-lift` as the current reusable markdown-first caution implementation surface
- local validation no longer dirties `git status` with Python cache artifacts

### Validation

- `python -m unittest discover -s tests`
- `python scripts/validate_repo.py`
- `python scripts/build_repo_doc_surface_manifest.py`
- `python scripts/build_catalog.py`
- `python scripts/build_shadow_review_manifest.py`
- `python scripts/build_capsules.py`
- `python scripts/build_section_manifest.py`
- `python scripts/build_checklist_manifest.py`
- `python scripts/build_example_manifest.py`
- `python scripts/build_evidence_note_manifest.py`
- `python scripts/build_github_review_template_manifest.py`
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
