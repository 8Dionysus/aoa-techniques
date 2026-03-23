# Documentation Map

This file is the human-first entrypoint for the repository's `docs/` surface.

Use it when you want to understand **which doc to open next** without guessing from filenames alone.

If you want one repo-owned entrypoint before this deeper docs map, open [Start Here](START_HERE.md).

## Start Here

Choose the path that matches your question:

- I need one repo-only entrypoint first:
  - [Start Here](START_HERE.md)
- I need to pick a technique now:
  - [Technique Selection Guide](TECHNIQUE_SELECTION_GUIDE.md)
  - [Technique Selection](TECHNIQUE_SELECTION.md)
  - [Selection Patterns](SELECTION_PATTERNS.md)
- I need a small local runtime card for one technique:
  - [Technique Capsules](TECHNIQUE_CAPSULES.md)
  - [Technique Capsule Guide](TECHNIQUE_CAPSULE_GUIDE.md)
  - [`../generated/technique_capsules.json`](../generated/technique_capsules.json)
  - [`../generated/technique_capsules.min.json`](../generated/technique_capsules.min.json)
- I need to understand status, review posture, or canonical promotion:
  - [Start Here](START_HERE.md)
  - [Canonical Rubric](CANONICAL_RUBRIC.md)
  - [Canonical Review Guide](CANONICAL_REVIEW_GUIDE.md)
  - [Promotion Readiness Matrix](PROMOTION_READINESS_MATRIX.md)
  - [Promotion Wave A Runbook](PROMOTION_WAVE_A_RUNBOOK.md)
  - [Donor Refinery Rubric](DONOR_REFINERY_RUBRIC.md)
  - [External Import Runbook](EXTERNAL_IMPORT_RUNBOOK.md)
  - [Long-Gap Canon Design](LONG_GAP_CANON_DESIGN.md)
  - [Deep Audit Roadmap](DEEP_AUDIT_ROADMAP.md)
  - [External Technique Candidates](EXTERNAL_TECHNIQUE_CANDIDATES.md)
  - [Cross-Layer Technique Candidates](CROSS_LAYER_TECHNIQUE_CANDIDATES.md)
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
  - [Technique Sections](TECHNIQUE_SECTIONS.md)
  - [`../generated/technique_sections.full.json`](../generated/technique_sections.full.json)
  - [Technique Section Lift Guide](TECHNIQUE_SECTION_LIFT_GUIDE.md)
  - [Technique Checklists](TECHNIQUE_CHECKLISTS.md)
  - [Technique Checklist Lift Guide](TECHNIQUE_CHECKLIST_LIFT_GUIDE.md)
  - [Technique Examples](TECHNIQUE_EXAMPLES.md)
  - [Technique Example Lift Guide](TECHNIQUE_EXAMPLE_LIFT_GUIDE.md)
  - [Evidence Note Surfaces](EVIDENCE_NOTE_SURFACES.md)
  - [Frontmatter Metadata Spine Guide](FRONTMATTER_METADATA_SPINE_GUIDE.md)
  - [Bounded Relation Lift Guide](BOUNDED_RELATION_LIFT_GUIDE.md)
  - [Evidence Note Provenance Guide](EVIDENCE_NOTE_PROVENANCE_GUIDE.md)
- I need the current reusable KAG/source-lift techniques:
  - [`markdown-technique-section-lift`](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md)
  - [`frontmatter-metadata-spine`](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md)
  - [`evidence-note-provenance-lift`](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md)
  - [`bounded-relation-lift-for-kag`](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md)
  - [`risk-and-negative-effect-lift`](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md)
  - [`repo-doc-surface-lift`](../techniques/docs/repo-doc-surface-lift/TECHNIQUE.md)
  - [`github-review-template-lift`](../techniques/docs/github-review-template-lift/TECHNIQUE.md)
  - [`semantic-review-surface-lift`](../techniques/docs/semantic-review-surface-lift/TECHNIQUE.md)
- I need to inspect the semantic-review pilots:
  - [Semantic Review Guide](SEMANTIC_REVIEW_GUIDE.md)
  - [Agent-Workflows Core Semantic Review](AGENT_WORKFLOWS_CORE_SEMANTIC_REVIEW.md)
  - [Published-Summary Semantic Review](PUBLISHED_SUMMARY_SEMANTIC_REVIEW.md)
  - [Evaluation-Chain Semantic Review](EVALUATION_CHAIN_SEMANTIC_REVIEW.md)
  - [Docs Boundary Semantic Review](DOCS_BOUNDARY_SEMANTIC_REVIEW.md)
  - [Intent-Chain Semantic Review](INTENT_CHAIN_SEMANTIC_REVIEW.md)
  - [Instruction-Surface Semantic Review](INSTRUCTION_SURFACE_SEMANTIC_REVIEW.md)
  - [Skill-Support Semantic Review](SKILL_SUPPORT_SEMANTIC_REVIEW.md)
  - [KAG Source Lift Semantic Review](KAG_SOURCE_LIFT_SEMANTIC_REVIEW.md)
- I need release process guidance:
  - [Start Here](START_HERE.md)
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

### Generated KAG/source-lift readers

These are reader-facing navigation artifacts derived from the current KAG/source-lift manifest families. They stay subordinate to authored markdown and do not become scoring, execution, or graph layers.

- [Technique Sections](TECHNIQUE_SECTIONS.md)
  - use when you need one heading-first router over the first 10 lifted `TECHNIQUE.md` sections
- [`../generated/technique_sections.full.json`](../generated/technique_sections.full.json)
  - use when a local runtime needs exact source-owned section payloads for bounded expand-time reads
- [Technique Checklists](TECHNIQUE_CHECKLISTS.md)
  - use when you need one bounded checklist inventory by domain and technique
- [Technique Examples](TECHNIQUE_EXAMPLES.md)
  - use when you need one bounded example inventory without opening each example body first
- [Evidence Note Surfaces](EVIDENCE_NOTE_SURFACES.md)
  - use when you need note-kind routing, note-shape awareness, or a bounded inventory of evidence-note surfaces

### Generated KAG/source-lift manifests

These are the current bounded JSON lift surfaces behind the reader companions above.

- [`../generated/technique_section_manifest.json`](../generated/technique_section_manifest.json)
  - use when the first 10 lifted `TECHNIQUE.md` sections should stay machine-readable and order-stable
- [`../generated/technique_checklist_manifest.json`](../generated/technique_checklist_manifest.json)
  - use when checklist inventories should stay derived validation knowledge only
- [`../generated/technique_example_manifest.json`](../generated/technique_example_manifest.json)
  - use when example inventories should stay derived example knowledge only
- [`../generated/technique_evidence_note_manifest.json`](../generated/technique_evidence_note_manifest.json)
  - use when typed and opaque note surfaces should stay derived provenance knowledge only

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
  - use when the 11 authoritative repo docs/status files should be lifted into bounded routing knowledge only

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

- [Start Here](START_HERE.md)
- [Canonical Rubric](CANONICAL_RUBRIC.md)
- [Canonical Review Guide](CANONICAL_REVIEW_GUIDE.md)
- [Promotion Readiness Matrix](PROMOTION_READINESS_MATRIX.md)
- [Promotion Wave A Runbook](PROMOTION_WAVE_A_RUNBOOK.md)
- [Donor Refinery Rubric](DONOR_REFINERY_RUBRIC.md)
- [Long-Gap Canon Design](LONG_GAP_CANON_DESIGN.md)
- [Deep Audit Roadmap](DEEP_AUDIT_ROADMAP.md)
- [External Technique Candidates](EXTERNAL_TECHNIQUE_CANDIDATES.md)
- [Cross-Layer Technique Candidates](CROSS_LAYER_TECHNIQUE_CANDIDATES.md)
- [External Import Runbook](EXTERNAL_IMPORT_RUNBOOK.md)
- [Technique Selection Guide](TECHNIQUE_SELECTION_GUIDE.md)
- [Semantic Review Guide](SEMANTIC_REVIEW_GUIDE.md)
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
- [Technique Section Lift Guide](TECHNIQUE_SECTION_LIFT_GUIDE.md)
- [Technique Checklist Lift Guide](TECHNIQUE_CHECKLIST_LIFT_GUIDE.md)
- [Technique Example Lift Guide](TECHNIQUE_EXAMPLE_LIFT_GUIDE.md)
- [Frontmatter Metadata Spine Guide](FRONTMATTER_METADATA_SPINE_GUIDE.md)
- [Bounded Relation Lift Guide](BOUNDED_RELATION_LIFT_GUIDE.md)
- [Evidence Note Provenance Guide](EVIDENCE_NOTE_PROVENANCE_GUIDE.md)
- [Risk And Negative-Effect Lift Guide](RISK_AND_NEGATIVE_EFFECT_LIFT_GUIDE.md)

### Reusable lift techniques

These are reusable technique bundles extracted from the repo's current generated and caution layers without widening into a graph platform or policy engine.

- [`markdown-technique-section-lift`](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md)
  - use when stable markdown sections should become one bounded derived lookup surface
- [`frontmatter-metadata-spine`](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md)
  - use when bundle routing needs the canonical shallow metadata spine plus a derived catalog, not richer schema
- [`evidence-note-provenance-lift`](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md)
  - use when typed supporting notes should act as provenance handles without becoming a note graph
- [`bounded-relation-lift-for-kag`](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md)
  - use when direct relations should power bounded adjacency hints without graph semantics
- [`risk-and-negative-effect-lift`](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md)
  - use when richer `Risks` language should act as bounded caution lookup without becoming metadata or scoring
- [`repo-doc-surface-lift`](../techniques/docs/repo-doc-surface-lift/TECHNIQUE.md)
  - use when the authoritative public repo docs/status layer should become one bounded derived routing surface
- [`github-review-template-lift`](../techniques/docs/github-review-template-lift/TECHNIQUE.md)
  - use when authored GitHub issue and pull-request templates should become one bounded intake lookup surface
- [`semantic-review-surface-lift`](../techniques/docs/semantic-review-surface-lift/TECHNIQUE.md)
  - use when authored semantic-review docs should become one bounded review-knowledge lookup surface without automation

### KAG/source-lift family review

This review-only doc currently keeps the first five core KAG/source-lift techniques distinct while staying subordinate to authored markdown, with two canonical anchors plus three promoted companions.

- [KAG Source Lift Semantic Review](KAG_SOURCE_LIFT_SEMANTIC_REVIEW.md)
  - use when the family seams between section lift, metadata spine, provenance lift, relation lift, and markdown-first caution lift need one bounded review surface

Later repo-surface, intake-surface, and review-surface lifts stay outside that family review until a wider family seam justifies refreshing it.

### Semantic-review pilots

These review-only docs test whether nearby techniques still read as distinct, bounded patterns rather than one blurred package.

- [Agent-Workflows Core Semantic Review](AGENT_WORKFLOWS_CORE_SEMANTIC_REVIEW.md)
- [Published-Summary Semantic Review](PUBLISHED_SUMMARY_SEMANTIC_REVIEW.md)
- [Evaluation-Chain Semantic Review](EVALUATION_CHAIN_SEMANTIC_REVIEW.md)
- [Docs Boundary Semantic Review](DOCS_BOUNDARY_SEMANTIC_REVIEW.md)
- [Intent-Chain Semantic Review](INTENT_CHAIN_SEMANTIC_REVIEW.md)
- [Instruction-Surface Semantic Review](INSTRUCTION_SURFACE_SEMANTIC_REVIEW.md)
- [Skill-Support Semantic Review](SKILL_SUPPORT_SEMANTIC_REVIEW.md)

## Recommended Reading Paths

### New reader path

1. [README](../README.md)
2. [Start Here](START_HERE.md)
3. [TECHNIQUE_INDEX](../TECHNIQUE_INDEX.md)
4. [Technique Selection](TECHNIQUE_SELECTION.md)
5. one concrete `TECHNIQUE.md` bundle

### Reviewer path

1. [Start Here](START_HERE.md)
2. [Canonical Rubric](CANONICAL_RUBRIC.md)
3. [Canonical Review Guide](CANONICAL_REVIEW_GUIDE.md)
4. [Shadow Patterns](SHADOW_PATTERNS.md) when the question is about caution seams rather than technique choice
5. one technique bundle plus its `notes/`; for `canonical` bundles include `canonical-readiness.md` and `adverse-effects-review.md`
6. a relevant semantic-review or shadow-review pilot if the technique sits inside a reviewed cluster

### KAG / lift path

1. [Start Here](START_HERE.md)
2. [KAG Source Lift Guide](KAG_SOURCE_LIFT_GUIDE.md)
3. one family guide such as [Technique Section Lift Guide](TECHNIQUE_SECTION_LIFT_GUIDE.md), [Frontmatter Metadata Spine Guide](FRONTMATTER_METADATA_SPINE_GUIDE.md), [Evidence Note Provenance Guide](EVIDENCE_NOTE_PROVENANCE_GUIDE.md), [Bounded Relation Lift Guide](BOUNDED_RELATION_LIFT_GUIDE.md), or [Risk And Negative-Effect Lift Guide](RISK_AND_NEGATIVE_EFFECT_LIFT_GUIDE.md)
4. one reader or manifest such as [Technique Sections](TECHNIQUE_SECTIONS.md), [Technique Checklists](TECHNIQUE_CHECKLISTS.md), [Technique Examples](TECHNIQUE_EXAMPLES.md), [Evidence Note Surfaces](EVIDENCE_NOTE_SURFACES.md), or [`../generated/repo_doc_surface_manifest.json`](../generated/repo_doc_surface_manifest.json)
5. one reusable lift bundle in `../techniques/docs/` if the concrete question still needs it

## Companion Repository Surfaces

These are outside `docs/` but matter when navigating the repo:

- [README](../README.md)
- [TECHNIQUE_INDEX](../TECHNIQUE_INDEX.md)
- [CONTRIBUTING](../CONTRIBUTING.md)
- [AGENTS](../AGENTS.md)
- [WALKTHROUGH](../WALKTHROUGH.md)
- [CHANGELOG](../CHANGELOG.md)

## Notes

- Prefer [Start Here](START_HERE.md) when the question is "where should I begin inside this repo before choosing a deeper surface?"
- Prefer generated reader surfaces when the question is "what should I inspect next?"
- Prefer `TECHNIQUE_SECTIONS.md` when the question is "which published techniques expose this lifted section heading?"
- Prefer `../generated/technique_sections.full.json` when the question is "which exact technique section should I expand next?"
- Prefer `TECHNIQUE_CHECKLISTS.md` when the question is "which technique already publishes a reusable checklist?"
- Prefer `TECHNIQUE_EXAMPLES.md` when the question is "which technique already has a reusable example surface?"
- Prefer `EVIDENCE_NOTE_SURFACES.md` when the question is "which note kind or note shape should I inspect next?"
- Prefer `REPO_DOC_SURFACES.md` when the question is "which authoritative repo doc should I open next?"
- Prefer `SHADOW_PATTERNS.md` when the question is "where can this canonical technique fail quietly or create false confidence?"
- Prefer authored guides when the question is "what does this repo mean by this rule or boundary?"
- Prefer semantic-review pilots when the question is "are these nearby techniques still meaningfully distinct?"

The current runtime path is:

`pick -> inspect -> expand -> object use`
