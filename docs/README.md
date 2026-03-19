# Documentation Map

This file is the human-first entrypoint for the repository's `docs/` surface.

Use it when you want to understand **which doc to open next** without guessing from filenames alone.

## Start Here

Choose the path that matches your question:

- I need to pick a technique now:
  - [Technique Selection](TECHNIQUE_SELECTION.md)
  - [Selection Patterns](SELECTION_PATTERNS.md)
- I need to understand status, review posture, or canonical promotion:
  - [Canonical Rubric](CANONICAL_RUBRIC.md)
  - [Canonical Review Guide](CANONICAL_REVIEW_GUIDE.md)
- I need to understand the repo's markdown-first caution discipline:
  - [Technique Shadow Guide](TECHNIQUE_SHADOW_GUIDE.md)
  - [Risk And Negative-Effect Lift Guide](RISK_AND_NEGATIVE_EFFECT_LIFT_GUIDE.md)
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

### Authored review and governance guides

These are human-authored guides that define bounded review, metadata, and documentation discipline.

- [Canonical Rubric](CANONICAL_RUBRIC.md)
- [Canonical Review Guide](CANONICAL_REVIEW_GUIDE.md)
- [Technique Shadow Guide](TECHNIQUE_SHADOW_GUIDE.md)
- [Releasing `aoa-techniques`](RELEASING.md)

### KAG-oriented boundary guides

These guides explain what the repo can already support as a future lift surface and what remains intentionally deferred.

- [KAG Source Lift Guide](KAG_SOURCE_LIFT_GUIDE.md)
- [Frontmatter Metadata Spine Guide](FRONTMATTER_METADATA_SPINE_GUIDE.md)
- [Bounded Relation Lift Guide](BOUNDED_RELATION_LIFT_GUIDE.md)
- [Evidence Note Provenance Guide](EVIDENCE_NOTE_PROVENANCE_GUIDE.md)
- [Risk And Negative-Effect Lift Guide](RISK_AND_NEGATIVE_EFFECT_LIFT_GUIDE.md)

### First KAG/source-lift techniques

These are reusable technique bundles extracted from the repo's current generated layer without widening into a graph platform.

- [`markdown-technique-section-lift`](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md)
  - use when stable markdown sections should become one bounded derived lookup surface
- [`frontmatter-metadata-spine`](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md)
  - use when bundle routing needs shallow frontmatter plus a derived catalog, not richer schema
- [`evidence-note-provenance-lift`](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md)
  - use when typed supporting notes should act as provenance handles without becoming a note graph
- [`bounded-relation-lift-for-kag`](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md)
  - use when direct relations should power bounded adjacency hints without graph semantics

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
3. one technique bundle plus its `notes/`
4. a relevant semantic-review pilot if the technique sits inside a reviewed cluster

### KAG / lift path

1. [KAG Source Lift Guide](KAG_SOURCE_LIFT_GUIDE.md)
2. [Frontmatter Metadata Spine Guide](FRONTMATTER_METADATA_SPINE_GUIDE.md)
3. [Bounded Relation Lift Guide](BOUNDED_RELATION_LIFT_GUIDE.md)
4. [Evidence Note Provenance Guide](EVIDENCE_NOTE_PROVENANCE_GUIDE.md)
5. [Risk And Negative-Effect Lift Guide](RISK_AND_NEGATIVE_EFFECT_LIFT_GUIDE.md)
6. one of the quartet bundles in `../techniques/docs/` that matches the concrete lift question

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
- Prefer authored guides when the question is "what does this repo mean by this rule or boundary?"
- Prefer semantic-review pilots when the question is "are these nearby techniques still meaningfully distinct?"
