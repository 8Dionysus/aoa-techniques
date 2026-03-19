# Frontmatter Metadata Spine Guide

This guide defines the bounded contract for `frontmatter-metadata-spine`.

Use it when the repository already works as authoritative markdown, but the next question is how current frontmatter and the derived catalog can serve as a metadata spine for later KAG entrypoints without pretending that metadata already contains the technique's full knowledge payload.

This guide is metadata-first. It does not add new frontmatter fields, generated KAG outputs, or section-level extraction logic.

See also:
- [Documentation Map](README.md)
- [KAG Source Lift Guide](KAG_SOURCE_LIFT_GUIDE.md)
- [`frontmatter-metadata-spine`](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md)

## Role Split

Keep the current source surfaces distinct:

- frontmatter carries bundle identity, bounded review posture, publication safety, and direct adjacency hints
- markdown sections carry the actual technique knowledge
- generated catalog outputs remain derived metadata surfaces rather than replacement sources

That split is the current metadata-spine contract.

## Stable Metadata Surfaces

The existing frontmatter already exposes a bounded metadata spine:

- `id`, `name`, `domain`, `status`, `summary`
- `maturity_score`, `rigor_level`, `reversibility`, `review_required`, `validation_strength`, `public_safety_reviewed_at`, `export_ready`
- `relations`
- `evidence.kind` and `evidence.path`

Treat these as stable metadata handles for bundle-level routing, not as substitutes for reading the underlying markdown sections.

## Current Metadata-Spine Outputs

The current metadata-spine outputs already exist:

- `generated/technique_catalog.min.json`
- `generated/technique_catalog.json`

They are useful today for:

- bundle lookup
- status and domain routing
- review and evidence-posture hints
- direct adjacency hints from `relations`
- provenance handles into note surfaces through `evidence`

They stay derived from markdown-frontmatter-v2 and should not become hand-maintained sources of truth.

## What Metadata Is Not

Current frontmatter and catalog outputs should not be treated as:

- section-level content units
- graph-ready semantics
- relation rationale
- shadow/caution knowledge itself
- a reason to widen metadata before the source-lift family proves it is needed

If a question needs section meaning, detailed caution language, or nuanced provenance explanation, the answer still lives in markdown sections and note files.
That includes risk, failure, and negative-effect meaning: the metadata spine can point to those surfaces later, but it does not replace the authored `Risks` section.

## Explicitly Deferred

Not part of this wave:

- no schema or frontmatter expansion
- no generated KAG artifacts beyond the existing catalog
- no script changes
- no relation-rationale metadata
- no section IDs
- no caution/shadow fields
- no new `kag` domain

The current job is to keep the bounded metadata spine explicit both as a repo rule and as the reusable technique captured in [`frontmatter-metadata-spine`](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md), without reopening whether markdown or metadata is authoritative.
