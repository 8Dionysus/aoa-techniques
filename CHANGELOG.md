# Changelog

All notable changes to `aoa-techniques` will be documented in this file.

The format is intentionally simple and human-first.

## [Unreleased]

Mainline corpus growth and validator hardening after `v0.1.0`.

### Added

- `AOA-T-0014` through `AOA-T-0034`, bringing the published corpus to 34 techniques (`17` canonical, `17` promoted)
- the first public five-technique KAG/source-lift family inside the existing `docs` domain:
  - `AOA-T-0018 markdown-technique-section-lift`
  - `AOA-T-0019 frontmatter-metadata-spine`
  - `AOA-T-0020 evidence-note-provenance-lift`
- `AOA-T-0021 bounded-relation-lift-for-kag`
- `AOA-T-0022 risk-and-negative-effect-lift`
- one new bounded `history` domain for session/history artifacts that stay local-first and reviewable without widening into `aoa-memo` ownership
- `AOA-T-0027 cross-agent-skill-propagation`
- `AOA-T-0025 capability-spec-versioning`
- `AOA-T-0026 session-capture-as-repo-artifact`
- `AOA-T-0028 confirmation-gated-mutating-action`
- `AOA-T-0029 nested-rule-loading`
- `AOA-T-0030 fragmented-agent-context`
- `AOA-T-0031 shell-composable-agent-invocation`
- `AOA-T-0032 context-report-for-ci`
- `AOA-T-0033 decision-rationale-recording`
- `AOA-T-0034 public-safe-artifact-sanitization`
- `AOA-T-0046 repo-doc-surface-lift`
- `AOA-T-0047 github-review-template-lift`
- `AOA-T-0048 semantic-review-surface-lift`
- `docs/LONG_GAP_CANON_DESIGN.md`, which captures the current design-first donor plan for `AOA-T-0005`, `AOA-T-0013`, and `AOA-T-0022`
- `docs/DEEP_AUDIT_ROADMAP.md`, which turns the current green baseline into a phase-by-phase closure roadmap for structural hardening, corpus meaning, surface usability, governance seams, and next implementation packs
- `docs/EXTERNAL_TECHNIQUE_CANDIDATES.md`, which stages the remaining `22` external donor-derived seed ideas by readiness to distill, overlap, incubation need, or substrate status
- `docs/EXTERNAL_IMPORT_RUNBOOK.md`, which turns bounded donor triage, draft, review, and merge work into one maintainer-facing import path
- `docs/CROSS_LAYER_TECHNIQUE_CANDIDATES.md`, which records the full `seed_donors_inside.md` candidate set without widening the external-only donor backlog
- `docs/TECHNIQUE_SELECTION_GUIDE.md` and `docs/SEMANTIC_REVIEW_GUIDE.md`, which close the missing authored family-contract layer for selection and semantic-review surfaces

### Changed

- shell-agent fast-path follow-up canon wave now promotes `AOA-T-0023 stateless-single-shot-agent` to `canonical`, adds its canonical-only `adverse-effects-review` note, refreshes its second-context and readiness notes around GitHub Copilot CLI's programmatic one-prompt path, and graduates it out of the remaining Wave A queue
- share-prep follow-up canon wave now promotes `AOA-T-0034 public-safe-artifact-sanitization` to `canonical`, adds its canonical-only `adverse-effects-review` note, refreshes its second-context and readiness notes around `Truth-Zeeker-AI-Public`, and graduates it out of the remaining Wave A queue
- instruction-distribution follow-up canon wave now promotes `AOA-T-0013 single-source-rule-distribution` to `canonical`, adds its canonical-only `adverse-effects-review` note, refreshes its second-context and readiness notes around `dyoshikawa/rulesync` plus `EmberAGI/arbitrum-vibekit`, and graduates it out of the remaining Wave A queue
- section-lift follow-up canon wave now promotes `AOA-T-0018 markdown-technique-section-lift` to `canonical`, adds its canonical-only `adverse-effects-review` note, and graduates it out of the active Wave A promotion-readiness queue
- remaining closure program now lands a dedicated `AGENT_WORKFLOWS_CORE_SEMANTIC_REVIEW.md`, merges first donor evidence from `aoa-skills` and `ATM10-Agent`, refreshes `AOA-T-0005`, `AOA-T-0013`, and `AOA-T-0022` second-context and readiness notes, and restages the remaining promoted backlog around one evidence-prep item plus four external-dependency-first items
- external donor intake wave now refreshes `AOA-T-0013` around the bounded `ruler` origin package, records `agents-md` as an overlap hold against `AOA-T-0012`, records `n-skills` as a landed adjacent provenance import rather than closure proof for `AOA-T-0013`, and keeps `AOA-T-0005` plus `AOA-T-0022` frozen until exact-fit external donors exist
- new external seed intake now adds `AOA-T-0023 stateless-single-shot-agent` from `qqqa`, adds `AOA-T-0024 upstream-mirroring-with-provenance` from `n-skills`, and widens the instruction-surface review from a pair into a three-technique cluster
- mixed external seed growth wave now adds `AOA-T-0025 capability-spec-versioning` from `agentic`, adds `AOA-T-0026 session-capture-as-repo-artifact` from `getspecstory`, introduces the bounded `history` domain, records `OpenMemory-Code` as a hold because memory-boundary overlap, and records `agentwise` as an explicit future-import candidate rather than a vague seed
- strict-safe external intake wave now adds `AOA-T-0027 cross-agent-skill-propagation` from `ruler`, adds `AOA-T-0028 confirmation-gated-mutating-action` from `qqqa`, narrows the remaining external candidate backlog from `22` to `20`, and widens the instruction-surface semantic review from a three-technique cluster into a four-technique cluster
- clean top-4 expansion wave now adds `AOA-T-0029 nested-rule-loading` from `ruler`, `AOA-T-0030 fragmented-agent-context` from `agents-md`, `AOA-T-0031 shell-composable-agent-invocation` from `qqqa`, and `AOA-T-0032 context-report-for-ci` from `agents-md`, narrows the remaining external candidate backlog from `20` to `16`, and intentionally keeps `versionable_agent_transcripts` plus `project_memory_bootstrap` out of the immediate wave as history-overlap watch around `AOA-T-0026`
- review coverage refresh wave now adds `docs/AGENT_WORKFLOWS_CORE_SEMANTIC_REVIEW.md`, narrows `docs/SKILL_SUPPORT_SEMANTIC_REVIEW.md` to the remaining skill-support seam cluster, and makes the new canonical-core review discoverable from the semantic-review guide and docs map
- repo-only hardening wave now aligns `README.md`, `docs/README.md`, and `CONTRIBUTING.md` around `docs/START_HERE.md`, the bounded `python scripts/release_check.py` path, and the current deep-audit closure roadmap
- governance and intake hardening wave now adds a narrow `CODEOWNERS` map, sharpens GitHub issue and PR templates around overlap watches, donor exclusions, generated surfaces, and downstream impact, and makes note-template authoring aids discoverable from the docs and contribution path
- `scripts/release_check.py` now compares composite repo state across worktree status, tracked diff, and cached diff so dirty tracked files cannot hide unstable generated drift
- `scripts/validate_repo.py` now treats selection and semantic-review guides as validator-backed family surfaces, widens public-hygiene root scanning beyond root markdown only, and blocks RFC1918 plus internal-suffix URLs on public surfaces
- standalone self-serve program now adds `docs/START_HERE.md` as the repo-owned entrypoint, expands the repo-doc surface family to include it, adds `python scripts/release_check.py` as the bounded release-prep command, and aligns guide vocabulary across repo-doc, capsule, KAG reader, and shadow surface families
- cross-layer intake wave now adds `docs/CROSS_LAYER_TECHNIQUE_CANDIDATES.md`, links it from repo-owned entrypoints, and adds regression coverage so the full 24-name donor-note universe stays discoverable and count-stable
- evidence-harvest wave now records live donor posture for the KAG/source-lift family in `KAG_SOURCE_LIFT_SEMANTIC_REVIEW.md` without changing statuses or validator specs
- hybrid canon completion program now lands committed Stage 1 donor evidence from `aoa-skills` and `aoa-routing`, promotes `AOA-T-0017 property-invariants` and `AOA-T-0021 bounded-relation-lift-for-kag` to `canonical`, adds canonical-only `adverse-effects-review` notes for both bundles, and records the long-gap donor design for `AOA-T-0005`, `AOA-T-0013`, and `AOA-T-0022`
- selective KAG promotion sync now promotes `AOA-T-0019 frontmatter-metadata-spine` to `canonical`, adds a canonical-only `adverse-effects-review` note, and makes it the bounded metadata-spine default for the KAG/source-lift family
- promoted backlog closure wave now gives every remaining promoted target an explicit final verdict, promotes `AOA-T-0016 bounded-context-map` to `canonical`, adds its canonical-only `adverse-effects-review` note, and leaves `AOA-T-0005`, `AOA-T-0013`, `AOA-T-0017`, `AOA-T-0018`, `AOA-T-0020`, `AOA-T-0021`, and `AOA-T-0022` as bounded-defer `promoted` techniques
- canon-strengthening wave now records explicit `canonical-readiness` outcomes across the non-KAG promoted target set, promotes `AOA-T-0004`, `AOA-T-0014`, and `AOA-T-0015` to `canonical`, and adds canonical-only `adverse-effects-review` notes for those newly promoted bundles
- KAG family maturity wave now adds `second-context-adaptation` plus `canonical-readiness` notes to `AOA-T-0018` through `AOA-T-0022`, keeps all five `promoted`, and adds `KAG_SOURCE_LIFT_SEMANTIC_REVIEW.md` as the shared family review surface
- `SELECTION_PATTERNS.md` working sets are now validator-checked against their linked semantic review maps
- new generated `docs/TECHNIQUE_CAPSULES.md` now provides a human reader surface over local runtime capsule cards grouped by domain and status order
- new generated `generated/technique_capsules.min.json` now keeps the capsule family on a strict min projection without replacing the full runtime payload
- new authored `docs/TECHNIQUE_CAPSULE_GUIDE.md` now defines the capsule source contract and runtime-only boundaries outside the KAG/source-lift family
- new generated `docs/REPO_DOC_SURFACES.md` now routes the authoritative public docs/status layer by bounded roles instead of filesystem guessing
- new generated `generated/repo_doc_surface_manifest.json` now lifts the 11 authoritative repo docs/status files into derived docs/status routing knowledge only
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
- local planning docs now treat the markdown-first shadow layer as landed baseline, record the explicit `Risks -> bundle-local adverse-effects-review -> repo-level shadow review only for a real caution-dense canonical cluster` escalation path, and point the next calm KAG/source-lift wave toward runbooks, broader canonical docs beyond repo-doc/status, and status snapshots
- public docs routing now exposes `repo-doc-surface-lift`, `github-review-template-lift`, and `semantic-review-surface-lift` as the second bounded docs-domain source-lift trio without adding new generated family types or a new `kag` domain
- local validation no longer dirties `git status` with Python cache artifacts

### Validation

- `python scripts/release_check.py`
- `python -m unittest discover -s tests`
- `python scripts/validate_repo.py`
- `python scripts/build_repo_doc_surface_manifest.py`
- `python scripts/build_catalog.py`
- `python scripts/build_shadow_review_manifest.py`
- `python scripts/build_capsules.py`
- `python scripts/build_sections.py`
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
