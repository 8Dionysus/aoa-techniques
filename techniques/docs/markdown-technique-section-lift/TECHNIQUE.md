---
id: AOA-T-0018
name: markdown-technique-section-lift
domain: docs
status: promoted
origin:
  project: aoa-techniques
  path: scripts/build_section_manifest.py
  note: Extracted from the current section-manifest implementation and KAG source-lift guidance to keep section extraction derived from canonical markdown bundles.
owners:
  - 8Dionysus
tags:
  - docs
  - kag
  - source-lift
  - sections
  - manifests
summary: Lift stable technique markdown sections into derived section-level units while keeping the bundle markdown authoritative.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-19
export_ready: true
relations:
  - type: complements
    target: AOA-T-0019
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
---

# markdown-technique-section-lift

## Intent

Lift stable `TECHNIQUE.md` section boundaries into a derived section-level surface so retrieval and review can target one bounded section without replacing markdown as the source of truth.

## When to use

- repositories with stable technique or pattern documents that already use recurring top-level headings
- generated knowledge or retrieval layers that need section-level routing without inventing new authored section files
- documentation systems where another human or agent should be able to jump directly to `Intent`, `Contracts`, `Risks`, or `Validation`
- KAG-oriented work that needs bounded section lookup before any graph or section-ID program exists

## When not to use

- repos where section headings are still unstable or heavily experimental
- systems that want section-level authorship to move out of the markdown bundle into separate files or metadata
- cases where the real need is graph semantics, ranking, or multi-hop reasoning rather than bounded section lift
- workflows that would treat the manifest as the new editable source of truth

## Inputs

- one authoritative `TECHNIQUE.md` bundle
- a small stable set of top-level section headings worth lifting
- one derived output surface such as a section manifest
- a rebuild path that can regenerate the derived output from markdown

## Outputs

- derived section-level units with preserved order
- explicit section headings that remain traceable to the source bundle
- section lookup surface for review or retrieval
- preserved markdown authority over section meaning

## Core procedure

1. Keep the technique bundle as the only authored source for section meaning.
2. Decide which recurring top-level sections are stable enough to lift.
3. Extract only those sections into a derived manifest or equivalent lookup surface.
4. Preserve the original section order and heading text instead of inventing a second parallel structure.
5. Rebuild the derived output whenever the source bundle changes.
6. Route readers or tooling back to the source markdown path when they need the full meaning of a lifted section.

## Contracts

- the markdown bundle remains the authoritative source of section meaning
- lifted sections stay bounded to an explicit stable scope rather than every possible heading
- derived output preserves section order instead of reinterpreting the document as an unordered field set
- consumers can map a lifted section back to the source bundle and heading
- the technique does not require section IDs, graph edges, or authored section files to work

## Risks

### Failure modes

- unstable or project-shaped headings are lifted too early, so the derived surface changes shape faster than consumers can trust it
- maintainers start editing the derived manifest instead of the bundle markdown and break source-of-truth boundaries
- the lift scope silently widens until the derived output looks like a shadow schema rather than a bounded retrieval surface

### Negative effects

- section-level retrieval can create false confidence that the full technique is understood when a reader has only consumed one bounded section
- a derived manifest can make documents feel more structured while hiding that some meaning still depends on surrounding prose
- teams can over-invest in extraction polish before proving that section-level lookup materially improves review or reuse

### Misuse patterns

- treating section lift as a reason to create a new `kag` domain or a larger graph program
- lifting headings that are too local, temporary, or donor-shaped to be reusable
- flattening full section meaning into metadata or machine-first fields because a manifest already exists

### Detection signals

- reviewers fix the manifest directly instead of fixing `TECHNIQUE.md`
- consumers rely on section snippets but cannot explain how those sections fit into the full bundle contract
- new headings keep appearing only to satisfy extraction rather than to improve the authored document
- the lift starts demanding section IDs, graph semantics, or schema expansion to stay usable

### Mitigations

- keep the lift scope narrow and explicit around stable recurring headings only
- route all meaning changes back through the source bundle and regenerate derived outputs afterward
- drop weak or unstable section targets before adding new derived behavior
- stop at bounded lookup when the next request would require graph behavior rather than better markdown structure

## Validation

Verify the technique by confirming that:
- lifted sections come from one authoritative `TECHNIQUE.md` bundle
- the derived output preserves the expected section order
- the selected headings are stable and explicitly bounded
- consumers can route back from the lifted output to the source bundle and heading
- no new authored source of truth was introduced beyond markdown plus derived artifacts

See `checks/section-lift-checklist.md` and `examples/minimal-section-lift.md`.
For repo-grounded origin evidence, see `notes/origin-evidence.md`.

## Adaptation notes

What can vary across projects:
- the exact stable heading set
- the derived output filename or manifest format
- whether lifted sections are consumed by retrieval, review tooling, or human navigation surfaces
- the rebuild command used to regenerate the derived output

What should stay invariant:
- markdown remains authoritative
- section lift stays derived-only
- lift scope is explicit and bounded
- consumers can still route back to the source bundle

This technique does not require a new `kag` domain. Keep it inside the existing domain that already owns the markdown source vocabulary.

## Public sanitization notes

This public version keeps the reusable lift contract and strips repo-specific implementation trivia such as exact helper names, local scripts, or any implication that a graph engine already exists. The point is bounded section lift from markdown, not a new platform.

## Example

See `examples/minimal-section-lift.md` for a small `TECHNIQUE.md` excerpt and the corresponding derived section-manifest output.

## Checks

See `checks/section-lift-checklist.md`.

## Promotion history

- shaped inside `aoa-techniques` while the section-manifest layer was introduced as a derived source-lift surface
- extracted into first public reusable form on 2026-03-19 as part of the initial KAG/source-lift family wave

## Future evolution

- strengthen second-context evidence once another markdown-first repository uses the same bounded section-lift discipline
- add review guidance for when a section is too unstable to keep in the lifted scope
- keep section IDs and richer graph semantics deferred unless bounded lookup stops being enough
