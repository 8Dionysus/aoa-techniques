# Evidence Note Provenance Guide

This guide defines the bounded contract for `evidence-note-provenance-lift`.

Use it when the repository already has typed evidence notes and explicit note paths, but the next question is how those notes can serve as provenance handles for later KAG-oriented layers without pretending they already form a merged note graph.

This guide is provenance-first. It allows one bounded generated evidence-note manifest while still avoiding note IDs, schema fields, or cross-note graph semantics.

## Current Note Roles

The current evidence-note layer already separates note roles in a useful way:

| evidence kind | bounded role |
|---|---|
| `origin_evidence` | source-backed origin proof for a technique born in a real project |
| `second_context` | bounded transfer or reuse reinforcement beyond the origin |
| `canonical_readiness` | review-oriented readiness or canonical-review decision surface |
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

## Recurring Note Shapes

Many evidence notes already use review-shaped recurring section patterns.

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
- external provenance and review notes:
  - donor/source identity
  - what changed
  - public-safety review
  - bounded verdict or recommendation

These recurring shapes are useful because they keep provenance reviewable and legible without turning notes into rigid machine-first forms.

## Bounded Use

Treat the current evidence-note layer as useful for:

- provenance lookup from bundle metadata into supporting review notes
- understanding why a technique is trusted, transferred, promoted, or imported
- keeping supporting evidence typed without flattening it into bundle frontmatter
- later generated provenance entrypoints that still preserve note-level authorship and context

That is a provenance layer, not a note graph platform.

## First Generated Provenance Lift

The first implementation-oriented lift now stays equally bounded:

- `generated/technique_evidence_note_manifest.json`
- `generated/technique_evidence_note_manifest.min.json`

Those files stay derived from authoritative note markdown.

They only do three bounded things:

- keep `support_note` files opaque at file level
- lift repeated typed note kinds through exact `##` section order
- preserve section content as ordered `fields`, `items`, or fallback `markdown`

They do not flatten note meaning into one top-level machine schema.

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

- no note schema expansion
- no note IDs
- no cross-note graph layer
- no relation-rationale metadata
- no flattened top-level note semantics like `verdict`, `source_project`, or note scoring
- no bundle or generated catalog changes beyond the bounded evidence note manifest

The current job is to keep the evidence-note provenance layer explicit and bounded while allowing one derived manifest that still preserves note-level authorship and context.
