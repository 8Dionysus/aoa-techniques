# KAG Source Lift Guide

This guide defines the first bounded repo-level contract for `canonical technique source -> generated KAG layer`.

Use it when the repository already looks strong as structured markdown, but the next question is how to lift that source into later KAG-friendly outputs without pretending the repo is already a graph platform or section-level schema.

This guide is source-first. It does not add new schema fields, generated KAG artifacts, or bundle-level section IDs.

## What Already Exists

The current repository is already strong enough for `technique-as-node` KAG because it has:

- bounded frontmatter that acts as a metadata spine
- canonical section headings in `TECHNIQUE.md`
- small typed `relations`
- explicit evidence-note kinds and paths
- generated catalog outputs that stay derived from authoritative markdown

That is enough to treat the repo as a strong upstream source. It is not yet a finished `section-level` KAG schema.

## First Bounded Family Member

The first KAG-oriented family member should be `markdown-technique-section-lift`.

Its job is narrow:

- treat one `TECHNIQUE.md` bundle as the canonical source
- identify stable sections that later generated layers may lift into bounded section-level units
- preserve the current markdown authority instead of replacing it

This is a source-lift discipline, not a graph engine.

See also: [FRONTMATTER_METADATA_SPINE_GUIDE.md](FRONTMATTER_METADATA_SPINE_GUIDE.md) for the second bounded family member, which clarifies how existing frontmatter and derived catalog outputs already act as the current metadata spine for bundle-level KAG entrypoints.

## Stable Source Surfaces

For the first source-lift wave, treat these surfaces as stable:

| source surface | bounded role |
|---|---|
| frontmatter | metadata spine for bundle identity, status, bounded review posture, and direct relations |
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

That makes shadow/caution lifting a later possibility, but not a reason to add machine-readable shadow fields yet.

## Explicitly Deferred

Not part of this first wave:

- no new `kag` domain
- no bundle-level section IDs
- no schema or frontmatter expansion
- no `build_kag` or similar script
- no generated KAG artifacts
- no relation-rationale layer
- no graph inference, scoring, or selector-engine behavior

The first public move is to publish how the current markdown canon can act as upstream for later generated KAG layers. Implementation and extraction can come later as separate bounded techniques.
