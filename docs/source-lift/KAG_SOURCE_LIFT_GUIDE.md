# KAG Source Lift Guide

This guide defines the bounded repo-level contract for
`canonical technique source -> generated KAG layer`.

Use it when the repository is already strong as structured markdown and the
next question is how to lift that source into KAG-friendly outputs without
pretending this repo is a graph platform, section schema, or policy engine.

This guide is source-first. Generated lift surfaces may route and summarize;
authored markdown remains authority.

See also:
- [Start Here](../START_HERE.md)
- [Documentation Map](../README.md)
- [`markdown-technique-section-lift`](../../techniques/knowledge-lift/kag-source-lift/markdown-technique-section-lift/TECHNIQUE.md)
- [`frontmatter-metadata-spine`](../../techniques/knowledge-lift/kag-source-lift/frontmatter-metadata-spine/TECHNIQUE.md)
- [`evidence-note-provenance-lift`](../../techniques/knowledge-lift/kag-source-lift/evidence-note-provenance-lift/TECHNIQUE.md)
- [`bounded-relation-lift-for-kag`](../../techniques/knowledge-lift/kag-source-lift/bounded-relation-lift-for-kag/TECHNIQUE.md)
- [`risk-and-negative-effect-lift`](../../techniques/knowledge-lift/kag-source-lift/risk-and-negative-effect-lift/TECHNIQUE.md)
- [`repo-doc-surface-lift`](../../techniques/knowledge-lift/kag-source-lift/repo-doc-surface-lift/TECHNIQUE.md)
- [`github-review-template-lift`](../../techniques/knowledge-lift/kag-source-lift/github-review-template-lift/TECHNIQUE.md)
- [`semantic-review-surface-lift`](../../techniques/knowledge-lift/kag-source-lift/semantic-review-surface-lift/TECHNIQUE.md)
- [Repo Doc Surface Lift Guide](REPO_DOC_SURFACE_LIFT_GUIDE.md)
- [Evidence Note Provenance Guide](EVIDENCE_NOTE_PROVENANCE_GUIDE.md)

## What Already Exists

The current repository is already strong enough for `technique-as-node` KAG
because it has bounded frontmatter, canonical `TECHNIQUE.md` headings, typed
direct `relations`, explicit evidence-note kinds and paths, recurring authored
note shapes, generated catalog outputs, and review surfaces for the reusable
source-lift family.

That is enough to treat the repo as a strong upstream source. It is not a
finished section-level KAG schema.

## First Bounded Family Member

The family anchor is `markdown-technique-section-lift`: treat one
`TECHNIQUE.md` bundle as canonical source, identify stable sections, and
preserve markdown authority.

Current lift classes:

| Source class | Contract | Generated surfaces |
|---|---|---|
| Sections | [TECHNIQUE_SECTION_LIFT_GUIDE.md](TECHNIQUE_SECTION_LIFT_GUIDE.md) | [TECHNIQUE_SECTIONS.md](../readers/source-lift/TECHNIQUE_SECTIONS.md), `generated/technique_section_manifest.json`, `generated/technique_section_manifest.min.json` |
| Checklists | [TECHNIQUE_CHECKLIST_LIFT_GUIDE.md](TECHNIQUE_CHECKLIST_LIFT_GUIDE.md) | [TECHNIQUE_CHECKLISTS.md](../readers/source-lift/TECHNIQUE_CHECKLISTS.md), `generated/technique_checklist_manifest.json`, `generated/technique_checklist_manifest.min.json` |
| Examples | [TECHNIQUE_EXAMPLE_LIFT_GUIDE.md](TECHNIQUE_EXAMPLE_LIFT_GUIDE.md) | [TECHNIQUE_EXAMPLES.md](../readers/source-lift/TECHNIQUE_EXAMPLES.md), `generated/technique_example_manifest.json`, `generated/technique_example_manifest.min.json` |
| Evidence notes | [EVIDENCE_NOTE_PROVENANCE_GUIDE.md](EVIDENCE_NOTE_PROVENANCE_GUIDE.md) | [EVIDENCE_NOTE_SURFACES.md](../readers/source-lift/EVIDENCE_NOTE_SURFACES.md), `generated/technique_evidence_note_manifest.json`, `generated/technique_evidence_note_manifest.min.json` |
| GitHub review templates | template source surfaces | `generated/github_review_template_manifest.json`, `generated/github_review_template_manifest.min.json` |
| Semantic review packets | [SEMANTIC_REVIEW_GUIDE.md](../review/SEMANTIC_REVIEW_GUIDE.md) | `generated/semantic_review_manifest.json`, `generated/semantic_review_manifest.min.json` |
| Shadow review packets | [TECHNIQUE_SHADOW_GUIDE.md](../review/TECHNIQUE_SHADOW_GUIDE.md) | `generated/shadow_review_manifest.json`, `generated/shadow_review_manifest.min.json`, [SHADOW_PATTERNS.md](../readers/review/SHADOW_PATTERNS.md) |
| Repo docs | [REPO_DOC_SURFACE_LIFT_GUIDE.md](REPO_DOC_SURFACE_LIFT_GUIDE.md) | [REPO_DOC_SURFACES.md](../readers/repo/REPO_DOC_SURFACES.md), `generated/repo_doc_surface_manifest.json`, `generated/repo_doc_surface_manifest.min.json` |

The companion family review is
[KAG_SOURCE_LIFT_SEMANTIC_REVIEW.md](../../mechanics/distillation/parts/technique-reform-ingress/reviews/semantic/KAG_SOURCE_LIFT_SEMANTIC_REVIEW.md).
It keeps section, metadata, provenance, relation, and caution seams readable
without turning the family into graph behavior.

## Stable Source Surfaces

Treat these source handles as stable:

| Source surface | Bounded role |
|---|---|
| frontmatter | bundle identity, status, review posture, and direct relation metadata |
| `TECHNIQUE.md` headings | human-authored content boundaries for section lift |
| `relations` | direct typed edges only, without graph inference |
| `evidence.kind` and `evidence.path` | provenance handles into supporting notes |
| repo-doc source set | public route/canon/status source files named by [REPO_DOC_SURFACE_LIFT_GUIDE.md](REPO_DOC_SURFACE_LIFT_GUIDE.md), including [START_HERE.md](../START_HERE.md) |

## First Section-Level Targets

The first section-level targets remain markdown-shaped:

`Intent`, `When to use`, `When not to use`, `Inputs`, `Outputs`,
`Core procedure`, `Contracts`, `Risks`, `Validation`, and `Adaptation notes`.

`Risks` is now a stronger caution source because it carries `Failure modes`,
`Negative effects`, `Misuse patterns`, `Detection signals`, and `Mitigations`.
That supports `risk-and-negative-effect-lift` and the bounded shadow review
surfaces, including `shadow_review_manifest.json`, without creating generated
caution policy.

## Explicitly Deferred

Not part of this wave:

- no new `kag` domain
- no bundle-level section IDs
- no schema or frontmatter expansion
- no generated KAG artifacts beyond the bounded source classes named above
- no relation-rationale layer
- no graph inference, scoring, search expansion, selector engine, or policy
  routing behavior

The current job is to keep source lift readable, bounded, and weaker than the
authored technique canon.
