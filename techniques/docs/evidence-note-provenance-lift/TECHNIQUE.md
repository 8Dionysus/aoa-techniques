---
id: AOA-T-0020
name: evidence-note-provenance-lift
domain: docs
status: promoted
origin:
  project: aoa-techniques
  path: scripts/build_evidence_note_manifest.py
  note: Extracted from the current evidence-note manifest layer and provenance guidance to keep note-kind and note-path provenance typed and reachable without flattening them into a note graph.
owners:
  - 8Dionysus
tags:
  - docs
  - kag
  - provenance
  - evidence-notes
  - manifests
summary: Use typed evidence note kinds and note paths as bounded provenance handles in derived manifests without flattening them into a note graph.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-19
export_ready: true
relations:
  - type: requires
    target: AOA-T-0019
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# evidence-note-provenance-lift

## Intent

Lift typed evidence notes into a bounded provenance surface so readers and tooling can find supporting origin, transfer, or review context through explicit note kind and note path handles without collapsing notes into one merged graph.

## When to use

- repositories where technique bundles already point to typed supporting notes
- provenance questions such as origin proof, second-context evidence, readiness review, canonical adverse-effects review, or external import review
- generated entrypoints that should expose note kinds and paths without replacing the note body
- KAG-oriented work that needs note-level handles before any cross-note graph program exists

## When not to use

- systems that have no stable note kinds or no explicit note paths
- cases where the real need is note IDs, cross-note graph semantics, or machine-extracted proof objects
- repositories that want to flatten all provenance meaning into frontmatter
- workflows where maintainers would rather edit generated note manifests than update the notes themselves

## Inputs

- typed evidence handles such as `evidence.kind` and `evidence.path`
- bounded note files under `notes/`
- recurring note shapes where they already exist
- one derived provenance surface such as an evidence-note manifest

## Outputs

- bounded provenance handles for supporting notes
- derived note manifest entries
- preserved note-level authorship and context
- reusable note-kind map for origin, transfer, readiness, or import review surfaces

## Core procedure

1. Keep the supporting notes as authored markdown under `notes/`.
2. Point to those notes from bundle metadata through typed evidence handles.
3. Lift the note layer into a derived manifest that preserves note kind, path, and bounded content shape.
4. Keep opaque notes opaque when they do not share a reusable typed structure.
5. Use the derived manifest for provenance lookup, not for replacing the note body.
6. Route interpretation and public-safety reasoning back to the underlying note when meaning matters.

## Contracts

- note paths and note kinds remain explicit
- note meaning stays in authored markdown
- derived provenance output preserves note-level context rather than flattening all notes into one schema
- supporting notes stay bounded to reviewable kinds such as origin, second context, readiness, canonical adverse-effects review, or external review
- the technique does not require note IDs, graph semantics, or a new source of truth

## Risks

### Failure modes

- note kinds drift until the manifest can no longer tell which provenance kind a note is meant to play
- flattening pressure strips interpretation or review nuance out of the note body
- contributors start treating the manifest entry as the note itself

### Negative effects

- a clean provenance surface can hide how much judgment still lives in the authored note text
- repeated typed notes can tempt maintainers into premature rigidity or over-schemafication
- provenance lookup can feel complete even when only one origin note exists and second-context evidence is still absent

### Misuse patterns

- turning note kinds into graph nodes with stable IDs before the note layer proves it needs them
- extracting verdicts, scoring, or relation rationale from notes just because a manifest exists
- using opaque support notes as a reason to widen note metadata instead of narrowing the review question

### Detection signals

- contributors ask for note-meaning changes by editing the manifest rather than the note body
- note kinds multiply faster than reviewers can explain their distinct purposes
- flattened manifest fields lose the argument or interpretation that made the note trustworthy
- provenance questions now depend on cross-note graph logic rather than on bounded note lookup

### Mitigations

- keep note kinds small and review-shaped
- preserve authored note text as the place where interpretation and public-safety reasoning live
- add new note kinds only when one current kind is clearly overloaded
- stop at bounded provenance handles when the next request is really for a graph or scoring layer

## Validation

Verify the technique by confirming that:
- bundles point to supporting notes through explicit `evidence.kind` and `evidence.path`
- note kinds remain understandable and bounded
- the derived provenance surface can be rebuilt from note markdown
- readers can use the manifest to find the right supporting note without losing note-level context
- note meaning still routes back to authored markdown instead of flattened metadata

See `checks/evidence-note-provenance-checklist.md` and `examples/evidence-note-to-manifest.md`.
For repo-grounded origin evidence, see `notes/origin-evidence.md`.

## Adaptation notes

What can vary across projects:
- which note kinds are present
- whether some notes are fully typed or intentionally opaque
- the manifest format used for provenance lookup
- the exact note filename conventions

What should stay invariant:
- note kinds remain explicit
- notes remain authored markdown
- manifest output stays derived and bounded
- provenance lift does not become a note graph or proof-object system

This technique sits downstream from a bounded metadata spine. If note lookup stops being enough and the next request is graph behavior, that is a different wave.

## Public sanitization notes

This public version keeps the reusable provenance split and removes any implication that note manifests already provide a full trust engine. The pattern is about bounded lookup into supporting markdown notes.

## Example

See `examples/evidence-note-to-manifest.md` for a small evidence array plus supporting note surface and the corresponding derived manifest excerpt.

## Checks

See `checks/evidence-note-provenance-checklist.md`.

## Promotion history

- shaped inside `aoa-techniques` while the evidence-note manifest layer was introduced as a bounded provenance surface
- extracted into first public reusable form on 2026-03-19 as part of the initial KAG/source-lift family wave

## Future evolution

- strengthen second-context evidence once the same bounded provenance pattern appears in another markdown-first corpus
- clarify when a new note kind is warranted versus when an existing kind should stay broader
- keep note IDs, cross-note graphs, and flattened trust semantics deferred
