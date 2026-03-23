# Evidence Note Provenance Guide

This guide defines the bounded contract for `evidence-note-provenance-lift`.

Use it when the repository already has typed evidence notes and explicit note paths, but the next question is how those notes can serve as provenance handles for later KAG-oriented layers without pretending they already form a merged note graph.

This guide is provenance-first. It allows one bounded generated evidence-note manifest family plus one reader companion while still avoiding note IDs, schema fields, or cross-note graph semantics.

See also:
- [Start Here](START_HERE.md)
- [Documentation Map](README.md)
- [KAG Source Lift Guide](KAG_SOURCE_LIFT_GUIDE.md)
- [Evidence Note Surfaces](EVIDENCE_NOTE_SURFACES.md)
- [`../templates/ORIGIN_EVIDENCE.template.md`](../templates/ORIGIN_EVIDENCE.template.md)
- [`../templates/ADAPTATION_NOTE.template.md`](../templates/ADAPTATION_NOTE.template.md)
- [`../templates/PROMOTION_NOTE.template.md`](../templates/PROMOTION_NOTE.template.md)
- [`../templates/ADVERSE_EFFECTS_REVIEW.template.md`](../templates/ADVERSE_EFFECTS_REVIEW.template.md)
- [`../templates/EXTERNAL_ORIGIN.template.md`](../templates/EXTERNAL_ORIGIN.template.md)
- [`../templates/EXTERNAL_REVIEW.template.md`](../templates/EXTERNAL_REVIEW.template.md)
- [`evidence-note-provenance-lift`](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md)

This family uses one stable shape:

- authoritative source: authored evidence notes plus bounded `evidence.kind` and `evidence.path`
- reader companion: `EVIDENCE_NOTE_SURFACES.md`
- derived manifests: `generated/technique_evidence_note_manifest.json` and `generated/technique_evidence_note_manifest.min.json`
- what it must not become: note IDs, note-graph behavior, relation rationale, or flattened proof metadata

## Current Note Roles

The current evidence-note layer already separates note roles in a useful way:

| evidence kind | bounded role |
|---|---|
| `origin_evidence` | source-backed origin proof for a technique born in a real project |
| `second_context` | bounded transfer or reuse reinforcement beyond the origin |
| `canonical_readiness` | review-oriented readiness or canonical-review decision surface |
| `adverse_effects_review` | canonical-only caution review supplement over an already-authored `Risks` section |
| `external_origin` | donor provenance for a bounded external import |
| `external_review` | explicit bounded verdict for an external import wave |
| `support_note` | other bounded explanatory note such as transfer boundaries or rollout triage |

These note kinds are already enough to act as provenance handles into supporting knowledge. They are not a merged note graph.

## Stable Provenance Handles

For the current provenance layer, treat these handles as stable:

- `evidence.kind`
- `evidence.path`
- note filename and location under `notes/`
- recurring note-level section shapes where they already exist

The path plus kind pairing is the current provenance contract. It lets bundle metadata point to the right supporting note without collapsing all note content into frontmatter.

## Current Authoring Aids

Use the current templates to keep note shapes reviewable and predictable without turning them into machine-first forms:

- `origin_evidence` -> `../templates/ORIGIN_EVIDENCE.template.md`
- `second_context` -> `../templates/ADAPTATION_NOTE.template.md`
- `canonical_readiness` -> `../templates/PROMOTION_NOTE.template.md`
- `adverse_effects_review` -> `../templates/ADVERSE_EFFECTS_REVIEW.template.md`
- `external_origin` -> `../templates/EXTERNAL_ORIGIN.template.md`
- `external_review` -> `../templates/EXTERNAL_REVIEW.template.md`

## Recurring Note Shapes

Many evidence notes already use recurring authored section patterns.

Common examples today:

- origin evidence notes:
  - `Technique`
  - `Source project`
  - `Evidence`
  - `Interpretation`
- second-context adaptation notes:
  - `Technique`
  - `Target project`
  - `What changed`
  - `What stayed invariant`
  - `Risks introduced by adaptation`
  - `Evidence`
  - `Result`
- canonical readiness notes:
  - `Technique`
  - `Verdict`
  - `Evidence summary`
  - `Default-use rationale`
  - `Fresh public-safety check`
  - `Remaining gaps`
  - `Recommendation`
- adverse-effects review notes:
  - `Technique`
  - `Review focus`
  - `Failure modes`
  - `Negative effects`
  - `Misuse patterns`
  - `Detection signals`
  - `Mitigations`
  - `Recommendation`
- external-origin provenance notes:
  - `Source`
  - `What changed`
  - `Public-safety review`
  - `Review notes`
- external-review notes:
  - `Technique`
  - `Verdict`
  - `Evidence summary`
  - `Boundedness check`
  - `Provenance readability`
  - `Remaining gaps`
  - `Recommendation`

These recurring shapes are useful because they keep provenance reviewable and legible without turning notes into rigid machine-first forms.

For the current normalization pass, keep the section titles stable and sharpen the content inside them.
Do not invent richer note metadata just because a note body still needs clearer wording.
If one note kind starts drifting, fix the authored shape first, then regenerate the manifest.

Starter markdown templates for the main recurring note kinds now live under `templates/`:

- `ORIGIN_EVIDENCE.template.md`
- `ADAPTATION_NOTE.template.md`
- `PROMOTION_NOTE.template.md`
- `ADVERSE_EFFECTS_REVIEW.template.md`
- `EXTERNAL_ORIGIN.template.md`
- `EXTERNAL_REVIEW.template.md`

Use them as maintainers' starting shapes only. They do not replace existing authored notes as the source of truth.

## Bounded Use

Treat the current evidence-note layer as useful for:

- provenance lookup from bundle metadata into supporting review notes
- understanding why a technique is trusted, transferred, promoted, or imported
- keeping canonical shadow review explicit without flattening caution into metadata
- keeping supporting evidence typed without flattening it into bundle frontmatter
- later generated provenance entrypoints that still preserve note-level authorship and context

That is a provenance layer, not a note graph platform.

## First Generated Provenance Lift

The first implementation-oriented lift now stays equally bounded:

- `generated/technique_evidence_note_manifest.json`
- `generated/technique_evidence_note_manifest.min.json`
- `docs/EVIDENCE_NOTE_SURFACES.md`

Those files stay derived from authoritative note markdown.

They only do three bounded things:

- keep `support_note` files opaque at file level
- lift repeated typed note kinds through exact `##` section order
- preserve section content as ordered `fields`, `items`, or fallback `markdown`

That now includes the canonical-only `adverse_effects_review` note role as a typed review surface in the manifest, while still keeping caution meaning in authored markdown.

They do not flatten note meaning into one top-level machine schema.

`EVIDENCE_NOTE_SURFACES.md` is the human reader companion for that same source class. It stays kind-first and routing-first. It only exposes note kind, title, note path, note shape, owning technique, and bounded routing signals such as fixed section scopes or opaque-body handling.

## What Evidence Notes Are Not

Current evidence notes should not be treated as:

- cross-note graph nodes with stable IDs
- relation-rationale metadata
- machine-extracted proof objects
- replacements for the main `TECHNIQUE.md` contract
- reasons to widen schema before the current note roles stop being enough

If a reviewer needs the actual argument, interpretation, or public-safety rationale, the answer still lives inside the note body.

## Explicitly Deferred

Not part of this wave:

- no note IDs
- no cross-note graph layer
- no relation-rationale metadata
- no flattened top-level note semantics like `verdict`, `source_project`, or note scoring
- no bundle or generated catalog changes beyond the bounded evidence note manifest

The current job is to keep the evidence-note provenance layer explicit and bounded, and the reusable technique now lives in [`evidence-note-provenance-lift`](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) while the derived manifest still preserves note-level authorship and context across origin, transfer, readiness, external provenance, external review, and canonical adverse-effects review notes.

This guide remains the authoritative contract doc for both the evidence-note manifest family and `EVIDENCE_NOTE_SURFACES.md`.

Regenerate and verify this source class with:

- `python scripts/build_evidence_note_manifest.py`
- `python scripts/release_check.py`
- `python -m unittest discover -s tests`
- `python scripts/validate_repo.py`
