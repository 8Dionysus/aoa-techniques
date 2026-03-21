# KAG Source Lift Guide

This guide defines the first bounded repo-level contract for `canonical technique source -> generated KAG layer`.

Use it when the repository already looks strong as structured markdown, but the next question is how to lift that source into later KAG-friendly outputs without pretending the repo is already a graph platform or section-level schema.

This guide is source-first. It allows a small bounded set of generated lift surfaces while still avoiding new schema fields, graph behavior, or bundle-level section IDs.

See also:
- [Documentation Map](README.md)
- [`markdown-technique-section-lift`](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md)
- [`frontmatter-metadata-spine`](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md)
- [`evidence-note-provenance-lift`](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md)
- [`bounded-relation-lift-for-kag`](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md)
- [`risk-and-negative-effect-lift`](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md)
- [Repo Doc Surface Lift Guide](REPO_DOC_SURFACE_LIFT_GUIDE.md)

## What Already Exists

The current repository is already strong enough for `technique-as-node` KAG because it has:

- bounded frontmatter that acts as a metadata spine
- canonical section headings in `TECHNIQUE.md`
- small typed `relations`
- explicit evidence-note kinds and paths
- generated catalog outputs that stay derived from authoritative markdown
- a companion family review surface that keeps the reusable source-lift techniques distinct

That is enough to treat the repo as a strong upstream source. It is not yet a finished `section-level` KAG schema.

Within the current reusable family, [`frontmatter-metadata-spine`](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) is now the canonical bundle-level metadata entrypoint. [`markdown-technique-section-lift`](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md), [`evidence-note-provenance-lift`](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md), [`bounded-relation-lift-for-kag`](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md), and [`risk-and-negative-effect-lift`](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) remain narrower promoted companions.

## First Bounded Family Member

The first KAG-oriented family member should be `markdown-technique-section-lift`.

Its job is narrow:

- treat one `TECHNIQUE.md` bundle as the canonical source
- identify stable sections that later generated layers may lift into bounded section-level units
- preserve the current markdown authority instead of replacing it

This is a source-lift discipline, not a graph engine.

The first implementation-oriented extraction pilot now stays equally narrow:

- `generated/technique_section_manifest.json`
- `generated/technique_section_manifest.min.json`
- `docs/TECHNIQUE_SECTIONS.md`
- `docs/TECHNIQUE_SECTION_LIFT_GUIDE.md`

Those files stay derived from authoritative markdown and expose only the first 10 KAG target sections. Their reader companion is heading-first and routing-only. They do not add graph, rationale, search, or scoring behavior.

The next implementation-oriented source-class pilot now stays equally bounded:

- `generated/technique_checklist_manifest.json`
- `generated/technique_checklist_manifest.min.json`
- `docs/TECHNIQUE_CHECKLISTS.md`
- `docs/TECHNIQUE_CHECKLIST_LIFT_GUIDE.md`

Those files lift authored validation checklists into derived validation knowledge only, and their reader companion stays inventory-first rather than policy-first. They are not executable policy, hard-gate semantics, or a new scoring layer.

The next implementation-oriented source-class pilot after checklists now stays equally bounded:

- `generated/technique_example_manifest.json`
- `generated/technique_example_manifest.min.json`
- `docs/TECHNIQUE_EXAMPLES.md`
- `docs/TECHNIQUE_EXAMPLE_LIFT_GUIDE.md`

Those files lift authored example narratives into derived example knowledge only, and their reader companion stays inventory-first without inlining full example bodies. They are not scenario graphs, executable tests, or a richer step-extraction layer yet.

The next implementation-oriented source-class pilot after examples now stays equally bounded:

- `generated/technique_evidence_note_manifest.json`
- `generated/technique_evidence_note_manifest.min.json`
- `docs/EVIDENCE_NOTE_SURFACES.md`

Those files lift authored evidence notes into derived provenance knowledge only, and their reader companion stays kind-first and routing-first. They do not add note IDs, note-graph behavior, relation rationale, or flattened note semantics.

They now include the canonical-only `adverse_effects_review` note role as one more typed note scope, but that still does not make caution machine-readable policy or generated caution output.

The five reusable lift techniques now have a companion review surface in `docs/KAG_SOURCE_LIFT_SEMANTIC_REVIEW.md`, which keeps the section, metadata, provenance, relation, and caution seams separate without turning the family into a graph or policy program.

The next implementation-oriented source-class pilot after evidence notes now stays equally bounded:

- `generated/github_review_template_manifest.json`
- `generated/github_review_template_manifest.min.json`

Those files lift authored GitHub issue and pull-request review templates into derived intake knowledge only. They do not replace the human-first templates or turn review prompts into a policy engine.

The next implementation-oriented source-class pilot after GitHub review templates now stays equally bounded:

- `generated/semantic_review_manifest.json`
- `generated/semantic_review_manifest.min.json`

Those files lift authored repo-level semantic review docs into derived review knowledge only. They do not replace the markdown review surfaces, infer verdict policy, or turn semantic review into a graph engine.

The next implementation-oriented source-class pilot after semantic review docs now stays equally bounded:

- `generated/shadow_review_manifest.json`
- `generated/shadow_review_manifest.min.json`

Those files lift authored repo-level shadow review docs into derived caution-review knowledge only. They do not replace the markdown review surfaces, infer caution policy, or turn shadow seams into generated metadata.

The next implementation-oriented source-class pilot after shadow review docs now stays equally bounded:

- `generated/repo_doc_surface_manifest.json`
- `generated/repo_doc_surface_manifest.min.json`

Those files lift the authoritative public docs/status layer into derived routing knowledge only. They stay bounded to `README.md`, `TECHNIQUE_INDEX.md`, `AGENTS.md`, `CONTRIBUTING.md`, `SECURITY.md`, `WALKTHROUGH.md`, `CODE_OF_CONDUCT.md`, `CHANGELOG.md`, `docs/README.md`, and `docs/RELEASING.md`.

Their human reader companion is `docs/REPO_DOC_SURFACES.md`, and the source-class contract lives in `docs/REPO_DOC_SURFACE_LIFT_GUIDE.md`. This still does not create a status-policy engine, broaden the source set to local planning docs, or pull deeper guide/review docs into the same manifest.

## Stable Source Surfaces

For the first source-lift wave, treat these surfaces as stable:

| source surface | bounded role |
|---|---|
| frontmatter | canonical metadata spine for bundle identity, status, bounded review posture, and direct relations |
| `TECHNIQUE.md` section headings | stable human-authored content boundaries for later section-level extraction |
| `relations` | direct typed edges only, without rationale expansion or multi-hop inference |
| `evidence.kind` and `evidence.path` | provenance handles that point to supporting note surfaces without pulling them into one merged graph yet |

## First Section-Level Targets

The first bounded section-level target surface should stay conceptual and markdown-shaped.

Treat sections like these as the current lift candidates:

- `Intent`
- `When to use`
- `When not to use`
- `Inputs`
- `Outputs`
- `Core procedure`
- `Contracts`
- `Risks`
- `Validation`
- `Adaptation notes`

`Risks` is now a stronger caution source because the repo already has the shadow-language contract for:

- `Failure modes`
- `Negative effects`
- `Misuse patterns`
- `Detection signals`
- `Mitigations`

That makes shadow/caution lifting a bounded reusable companion surface now captured in [`risk-and-negative-effect-lift`](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md), and canonical bundles can now add one typed adverse-effects review note as a bounded review supplement. It is still not a reason to add machine-readable shadow fields or generated caution outputs.

## Explicitly Deferred

Not part of this first wave:

- no new `kag` domain
- no bundle-level section IDs
- no schema or frontmatter expansion
- no `build_kag` or similar script
- no generated KAG artifacts beyond the bounded section, checklist, example, evidence note, GitHub review template, semantic review, shadow review, and repo doc surface manifests
- no relation-rationale layer
- no graph inference, scoring, or selector-engine behavior

The first public move was to publish how the current markdown canon can act as upstream for later generated KAG layers. The current reusable family now keeps that order bounded: section lift first, metadata spine and provenance lift alongside the current manifests, bounded direct-relation lift without graph behavior, semantic and shadow review manifests as derived review knowledge only, repo-doc/status surfaces as derived routing knowledge only, markdown-first caution lift without metadata or generated caution outputs, and a companion family review surface that keeps the five techniques readable as one bounded source-lift family.
