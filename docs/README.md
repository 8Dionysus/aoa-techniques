# Documentation Map

This file is the human-first entrypoint for the repository's `docs/` surface.

Use it when you want to understand **which doc to open next** without guessing from filenames alone.

## Start Here

Choose the path that matches your question:

- I need to pick a technique now:
  - [Technique Selection](TECHNIQUE_SELECTION.md)
  - [Selection Patterns](SELECTION_PATTERNS.md)
- I need a small local runtime card for one technique:
  - [Technique Capsules](TECHNIQUE_CAPSULES.md)
  - [Technique Capsule Guide](TECHNIQUE_CAPSULE_GUIDE.md)
  - [`../generated/technique_capsules.json`](../generated/technique_capsules.json)
  - [`../generated/technique_capsules.min.json`](../generated/technique_capsules.min.json)
- I need to understand status, review posture, or canonical promotion:
  - [Canonical Rubric](CANONICAL_RUBRIC.md)
  - [Canonical Review Guide](CANONICAL_REVIEW_GUIDE.md)
- I need to understand the repo's markdown-first caution discipline:
  - [Shadow Patterns](SHADOW_PATTERNS.md)
  - [Technique Shadow Guide](TECHNIQUE_SHADOW_GUIDE.md)
  - [Risk And Negative-Effect Lift Guide](RISK_AND_NEGATIVE_EFFECT_LIFT_GUIDE.md)
  - [Published-Summary Shadow Review](PUBLISHED_SUMMARY_SHADOW_REVIEW.md)
  - [Evaluation-Chain Shadow Review](EVALUATION_CHAIN_SHADOW_REVIEW.md)
  - [`risk-and-negative-effect-lift`](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md)
  - one canonical bundle plus its `notes/adverse-effects-review.md`
- I need to navigate the authoritative repo docs/status layer:
  - [Repo Doc Surfaces](REPO_DOC_SURFACES.md)
  - [Repo Doc Surface Lift Guide](REPO_DOC_SURFACE_LIFT_GUIDE.md)
  - [`../generated/repo_doc_surface_manifest.json`](../generated/repo_doc_surface_manifest.json)
- I need to understand KAG-oriented lift boundaries:
  - [KAG Source Lift Guide](KAG_SOURCE_LIFT_GUIDE.md)
  - [Frontmatter Metadata Spine Guide](FRONTMATTER_METADATA_SPINE_GUIDE.md)
  - [Bounded Relation Lift Guide](BOUNDED_RELATION_LIFT_GUIDE.md)
  - [Evidence Note Provenance Guide](EVIDENCE_NOTE_PROVENANCE_GUIDE.md)
- I need the first reusable KAG/source-lift techniques:
  - [`markdown-technique-section-lift`](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md)
  - [`frontmatter-metadata-spine`](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md)
  - [`evidence-note-provenance-lift`](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md)
  - [`bounded-relation-lift-for-kag`](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md)
- I need to inspect the semantic-review pilots:
  - [Published-Summary Semantic Review](PUBLISHED_SUMMARY_SEMANTIC_REVIEW.md)
  - [Evaluation-Chain Semantic Review](EVALUATION_CHAIN_SEMANTIC_REVIEW.md)
  - [Docs Boundary Semantic Review](DOCS_BOUNDARY_SEMANTIC_REVIEW.md)
  - [Intent-Chain Semantic Review](INTENT_CHAIN_SEMANTIC_REVIEW.md)
  - [Instruction-Surface Semantic Review](INSTRUCTION_SURFACE_SEMANTIC_REVIEW.md)
  - [Skill-Support Semantic Review](SKILL_SUPPORT_SEMANTIC_REVIEW.md)
- I need release process guidance:
  - [Releasing `aoa-techniques`](RELEASING.md)

## Surface Types

### Generated reader surfaces

These are reader-facing navigation artifacts derived from authoritative markdown and generated data.

- [Technique Selection](TECHNIQUE_SELECTION.md)
  - use when you need one bounded choice by domain, status, validation strength, or nearby relations
- [Selection Patterns](SELECTION_PATTERNS.md)
  - use when direct adjacency is not enough and you want validator-backed starting points, common next moves, or review-backed working sets
- [Shadow Patterns](SHADOW_PATTERNS.md)
  - use when you need one bounded answer to where a canonical technique can quietly make the system worse and which watch seam to inspect first
- [Repo Doc Surfaces](REPO_DOC_SURFACES.md)
  - use when you need one bounded answer to which authoritative repo doc/status surface to open next

### Local runtime cards

These are small local derived cards for runtime lookup. They stay subordinate to the authored bundles, stay outside the KAG/source-lift family, and do not replace section-level manifests.

- [Technique Capsules](TECHNIQUE_CAPSULES.md)
  - use when you want one reader-facing local runtime card surface grouped by domain and bounded runtime fields
- [`../generated/technique_capsules.json`](../generated/technique_capsules.json)
  - use when one bounded technique card is enough for local lookup, dispatch, or runtime orientation
- [`../generated/technique_capsules.min.json`](../generated/technique_capsules.min.json)
  - use when a strict min projection is enough for lightweight local runtime lookup
- [Technique Capsule Guide](TECHNIQUE_CAPSULE_GUIDE.md)
  - use when you need the capsule source contract, field boundaries, or runtime-only scope explained before consuming the generated surfaces

### Generated docs/status manifests

These are derived docs/status source-lift surfaces. They stay subordinate to the authored public docs and do not replace those docs as the source of truth.

- [`../generated/repo_doc_surface_manifest.json`](../generated/repo_doc_surface_manifest.json)
  - use when the 10 authoritative repo docs/status files should be lifted into bounded routing knowledge only

### Generated review manifests

These are derived review-knowledge surfaces for KAG/source-lift lookup. They stay subordinate to the authored docs and do not replace the human review surfaces.

- [`../generated/shadow_review_manifest.json`](../generated/shadow_review_manifest.json)
  - use when canonical shadow-review pilots should be lifted as derived review knowledge without turning caution into policy metadata
- [`../generated/semantic_review_manifest.json`](../generated/semantic_review_manifest.json)
  - use when authored semantic-review pilots should be lifted as derived boundary-review knowledge only
- [`../generated/github_review_template_manifest.json`](../generated/github_review_template_manifest.json)
  - use when GitHub issue or PR review templates should be lifted as derived intake knowledge only

### Authored review and governance guides

These are human-authored guides that define bounded review, metadata, and documentation discipline.

- [Canonical Rubric](CANONICAL_RUBRIC.md)
- [Canonical Review Guide](CANONICAL_REVIEW_GUIDE.md)
- [Technique Capsule Guide](TECHNIQUE_CAPSULE_GUIDE.md)
- [Repo Doc Surface Lift Guide](REPO_DOC_SURFACE_LIFT_GUIDE.md)
- [Technique Shadow Guide](TECHNIQUE_SHADOW_GUIDE.md)
- [Releasing `aoa-techniques`](RELEASING.md)

### Shadow-review pilots

These review-only docs inspect where caution language is most likely to blur neighboring canonical techniques or create false confidence.

- [Published-Summary Shadow Review](PUBLISHED_SUMMARY_SHADOW_REVIEW.md)
- [Evaluation-Chain Shadow Review](EVALUATION_CHAIN_SHADOW_REVIEW.md)

### KAG-oriented boundary guides

These guides explain what the repo can already support as a future lift surface and what remains intentionally deferred.

- [KAG Source Lift Guide](KAG_SOURCE_LIFT_GUIDE.md)
- [Frontmatter Metadata Spine Guide](FRONTMATTER_METADATA_SPINE_GUIDE.md)
- [Bounded Relation Lift Guide](BOUNDED_RELATION_LIFT_GUIDE.md)
- [Evidence Note Provenance Guide](EVIDENCE_NOTE_PROVENANCE_GUIDE.md)
- [Risk And Negative-Effect Lift Guide](RISK_AND_NEGATIVE_EFFECT_LIFT_GUIDE.md)

### Reusable lift techniques

These are reusable technique bundles extracted from the repo's current generated and caution layers without widening into a graph platform or policy engine.

- [`markdown-technique-section-lift`](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md)
  - use when stable markdown sections should become one bounded derived lookup surface
- [`frontmatter-metadata-spine`](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md)
  - use when bundle routing needs shallow frontmatter plus a derived catalog, not richer schema
- [`evidence-note-provenance-lift`](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md)
  - use when typed supporting notes should act as provenance handles without becoming a note graph
- [`bounded-relation-lift-for-kag`](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md)
  - use when direct relations should power bounded adjacency hints without graph semantics
- [`risk-and-negative-effect-lift`](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md)
  - use when richer `Risks` language should act as bounded caution lookup without becoming metadata or scoring

### Semantic-review pilots

These review-only docs test whether nearby techniques still read as distinct, bounded patterns rather than one blurred package.

- [Published-Summary Semantic Review](PUBLISHED_SUMMARY_SEMANTIC_REVIEW.md)
- [Evaluation-Chain Semantic Review](EVALUATION_CHAIN_SEMANTIC_REVIEW.md)
- [Docs Boundary Semantic Review](DOCS_BOUNDARY_SEMANTIC_REVIEW.md)
- [Intent-Chain Semantic Review](INTENT_CHAIN_SEMANTIC_REVIEW.md)
- [Instruction-Surface Semantic Review](INSTRUCTION_SURFACE_SEMANTIC_REVIEW.md)
- [Skill-Support Semantic Review](SKILL_SUPPORT_SEMANTIC_REVIEW.md)

## Recommended Reading Paths

### New reader path

1. [README](../README.md)
2. [TECHNIQUE_INDEX](../TECHNIQUE_INDEX.md)
3. [Technique Selection](TECHNIQUE_SELECTION.md)
4. one concrete `TECHNIQUE.md` bundle

### Reviewer path

1. [Canonical Rubric](CANONICAL_RUBRIC.md)
2. [Canonical Review Guide](CANONICAL_REVIEW_GUIDE.md)
3. [Shadow Patterns](SHADOW_PATTERNS.md) when the question is about caution seams rather than technique choice
4. one technique bundle plus its `notes/`; for `canonical` bundles include `canonical-readiness.md` and `adverse-effects-review.md`
5. a relevant semantic-review or shadow-review pilot if the technique sits inside a reviewed cluster

### KAG / lift path

1. [KAG Source Lift Guide](KAG_SOURCE_LIFT_GUIDE.md)
2. [Repo Doc Surface Lift Guide](REPO_DOC_SURFACE_LIFT_GUIDE.md)
3. [`../generated/repo_doc_surface_manifest.json`](../generated/repo_doc_surface_manifest.json)
4. [Frontmatter Metadata Spine Guide](FRONTMATTER_METADATA_SPINE_GUIDE.md)
5. [Bounded Relation Lift Guide](BOUNDED_RELATION_LIFT_GUIDE.md)
6. [Evidence Note Provenance Guide](EVIDENCE_NOTE_PROVENANCE_GUIDE.md)
7. [Risk And Negative-Effect Lift Guide](RISK_AND_NEGATIVE_EFFECT_LIFT_GUIDE.md)
8. [`../generated/shadow_review_manifest.json`](../generated/shadow_review_manifest.json)
9. one of the reusable lift bundles in `../techniques/docs/` that matches the concrete question, including `risk-and-negative-effect-lift` for markdown-first caution lookup

## Companion Repository Surfaces

These are outside `docs/` but matter when navigating the repo:

- [README](../README.md)
- [TECHNIQUE_INDEX](../TECHNIQUE_INDEX.md)
- [CONTRIBUTING](../CONTRIBUTING.md)
- [AGENTS](../AGENTS.md)
- [WALKTHROUGH](../WALKTHROUGH.md)
- [CHANGELOG](../CHANGELOG.md)

## Notes

- Prefer generated reader surfaces when the question is "what should I inspect next?"
- Prefer `REPO_DOC_SURFACES.md` when the question is "which authoritative repo doc should I open next?"
- Prefer `SHADOW_PATTERNS.md` when the question is "where can this canonical technique fail quietly or create false confidence?"
- Prefer authored guides when the question is "what does this repo mean by this rule or boundary?"
- Prefer semantic-review pilots when the question is "are these nearby techniques still meaningfully distinct?"
