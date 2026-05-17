# Evidence Note Provenance Guide

This guide defines the bounded contract for `evidence-note-provenance-lift`.

Use it when the repository has typed evidence notes and explicit note paths,
and the next question is how those notes can serve as provenance handles for
later KAG-oriented layers without becoming a merged note graph.

This guide is provenance-first. It allows one generated evidence-note manifest
family plus one reader companion while avoiding note IDs, schema fields,
cross-note graph semantics, and flattened proof metadata.

See also:
- [Start Here](../START_HERE.md)
- [Documentation Map](../README.md)
- [KAG Source Lift Guide](KAG_SOURCE_LIFT_GUIDE.md)
- [Evidence Note Surfaces](../readers/source-lift/EVIDENCE_NOTE_SURFACES.md)
- [`templates/ORIGIN_EVIDENCE.template.md`](../../templates/ORIGIN_EVIDENCE.template.md)
- [`templates/ADAPTATION_NOTE.template.md`](../../templates/ADAPTATION_NOTE.template.md)
- [`templates/PROMOTION_NOTE.template.md`](../../templates/PROMOTION_NOTE.template.md)
- [`templates/ADVERSE_EFFECTS_REVIEW.template.md`](../../templates/ADVERSE_EFFECTS_REVIEW.template.md)
- [`templates/EXTERNAL_ORIGIN.template.md`](../../templates/EXTERNAL_ORIGIN.template.md)
- [`templates/EXTERNAL_REVIEW.template.md`](../../templates/EXTERNAL_REVIEW.template.md)
- [`evidence-note-provenance-lift`](../../techniques/knowledge-lift/kag-source-lift/evidence-note-provenance-lift/TECHNIQUE.md)

## Current Note Roles

| Evidence kind | Bounded role | Template when starting fresh |
|---|---|---|
| `origin_evidence` | source-backed origin proof for a technique born in a real project | `ORIGIN_EVIDENCE.template.md` |
| `second_context` | transfer or reuse reinforcement beyond the origin | `ADAPTATION_NOTE.template.md` |
| `canonical_readiness` | review-oriented readiness or canonical-review decision surface | `PROMOTION_NOTE.template.md` |
| `adverse_effects_review` | canonical-only caution supplement over authored `Risks` | `ADVERSE_EFFECTS_REVIEW.template.md` |
| `external_origin` | donor provenance for a bounded external import | `EXTERNAL_ORIGIN.template.md` |
| `external_review` | bounded verdict for an external import wave | `EXTERNAL_REVIEW.template.md` |
| `support_note` | other bounded explanatory note | no fixed typed shape |

These note kinds are provenance handles. They are not a merged note graph.

## Stable Provenance Handles

The current provenance contract is the pairing of `evidence.kind` and
`evidence.path`, plus the note filename and location under `notes/`.

Recurring note-level section shapes are useful where they already exist, but
the path plus kind pairing is the stable handle. If a note body drifts, fix the
authored note first, then regenerate the manifest.

## Current Authoring Aids

Starter templates live under [templates](../../templates/):

- `ORIGIN_EVIDENCE.template.md`
- `ADAPTATION_NOTE.template.md`
- `PROMOTION_NOTE.template.md`
- `ADVERSE_EFFECTS_REVIEW.template.md`
- `EXTERNAL_ORIGIN.template.md`
- `EXTERNAL_REVIEW.template.md`

Use them as maintainers' starting shapes only. They do not replace existing
authored notes as source truth.

## Recurring Note Shapes

Common section shapes:

| Note kind | Typical sections |
|---|---|
| origin evidence | `Technique`, `Source project`, `Evidence`, `Interpretation` |
| second-context adaptation | `Technique`, `Target project`, `What changed`, `What stayed invariant`, `Risks introduced by adaptation`, `Evidence`, `Result` |
| canonical readiness | `Technique`, `Verdict`, `Evidence summary`, `Default-use rationale`, `Fresh public-safety check`, `Remaining gaps`, `Recommendation` |
| adverse-effects review | `Technique`, `Review focus`, `Failure modes`, `Negative effects`, `Misuse patterns`, `Detection signals`, `Mitigations`, `Recommendation` |
| external-origin provenance | `Source`, `What changed`, `Public-safety review`, `Review notes` |
| external review | `Technique`, `Verdict`, `Evidence summary`, `Boundedness check`, `Provenance readability`, `Remaining gaps`, `Recommendation` |

Keep these titles stable when the note kind already uses them. Do not invent
richer note metadata just because prose needs sharpening.

## Bounded Use

Use the evidence-note layer for provenance lookup, trust/reuse/promotion/import
context, canonical shadow review supplements, and later generated provenance
entrypoints that preserve note authorship.

That is a provenance layer, not a note graph platform.

## First Generated Provenance Lift

The generated family is:

- `generated/technique_evidence_note_manifest.json`
- `generated/technique_evidence_note_manifest.min.json`
- [EVIDENCE_NOTE_SURFACES.md](../readers/source-lift/EVIDENCE_NOTE_SURFACES.md)

Those files stay derived from authoritative note markdown. They keep
`support_note` files opaque at file level, lift repeated typed note kinds
through exact `##` section order, and preserve section content as ordered
`fields`, `items`, or fallback `markdown`.

`docs/readers/source-lift/EVIDENCE_NOTE_SURFACES.md` is the human reader
companion for that same source class. It exposes note kind, title, note path,
note shape, owning technique, and bounded routing signals. It does not flatten
note prose, review arguments, or caution language into the reader.

## What Evidence Notes Are Not

Current evidence notes are not cross-note graph nodes with stable IDs,
relation-rationale metadata, machine-extracted proof objects, replacements for
the main `TECHNIQUE.md` contract, or reasons to widen schema before the current
note roles stop being enough.

If a reviewer needs the argument, interpretation, or public-safety rationale,
the answer still lives inside the note body.

## Explicitly Deferred

Not part of this wave:

- no note IDs
- no cross-note graph layer
- no relation-rationale metadata
- no flattened top-level note semantics like `verdict`, `source_project`, or
  note scoring
- no bundle or generated catalog changes beyond the bounded evidence-note
  manifest

This guide remains the authoritative contract doc for both the evidence-note
manifest family and `docs/readers/source-lift/EVIDENCE_NOTE_SURFACES.md`.

Agent validation and regeneration routes live in [AGENTS](AGENTS.md).
