---
id: AOA-T-0019
name: frontmatter-metadata-spine
domain: docs
status: promoted
origin:
  project: aoa-techniques
  path: scripts/build_catalog.py
  note: Extracted from the current catalog layer and metadata-spine guidance to keep routing metadata bounded while markdown bundles hold the real technique meaning.
owners:
  - 8Dionysus
tags:
  - docs
  - kag
  - metadata
  - frontmatter
  - catalog
summary: Treat bounded frontmatter and derived catalog outputs as a metadata spine for bundle routing without replacing markdown meaning or growing schema past current needs.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-19
export_ready: true
relations:
  - type: complements
    target: AOA-T-0018
  - type: used_together_for
    target: AOA-T-0020
  - type: used_together_for
    target: AOA-T-0021
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# frontmatter-metadata-spine

## Intent

Use shallow frontmatter and derived catalog outputs as a stable metadata spine for bundle identity, routing, and review posture without pretending that frontmatter already contains the technique's full knowledge.

## When to use

- markdown-first repositories that need a small machine-readable layer for lookup or routing
- corpora where domain, status, summary, evidence handles, and direct relations should be visible without opening every bundle first
- generated catalog or selection surfaces that must stay derived from authoritative markdown
- KAG-oriented work that needs bundle-level metadata handles before section or provenance consumers go deeper

## When not to use

- systems that want full section meaning, rationale, or caution language to live in metadata
- repos where frontmatter is still unstable or overloaded with project-local details
- cases where the next step is graph behavior, section IDs, schema expansion, or a metadata-first source of truth rather than bounded routing metadata
- workflows that would hand-edit the derived catalog instead of regenerating it

## Inputs

- bounded frontmatter on each authoritative bundle
- a validator or generator that can project frontmatter into a derived catalog
- current routing questions such as lookup by status, domain, review posture, or direct adjacency
- explicit agreement that markdown sections still hold the real technique meaning

## Outputs

- stable bundle-level metadata handles
- derived catalog entries for lookup and navigation
- explicit separation between metadata and section meaning
- reusable routing surface for later bounded consumers

## Core procedure

1. Keep only bundle identity, review posture, summary, evidence handles, and direct adjacency in frontmatter.
2. Generate a catalog from that frontmatter rather than maintaining a second hand-authored metadata source.
3. Use the catalog for bundle lookup, status routing, or direct-edge hints.
4. Route any question about section meaning, caution language, or provenance argument back to markdown sections and note files.
5. Add new metadata only when the routing problem cannot be solved by the current bounded spine and markdown authority still remains primary.
6. Rebuild the catalog whenever source frontmatter changes.

## Contracts

- frontmatter stays shallow and bounded
- the catalog remains fully derived from authoritative markdown-frontmatter
- metadata supports routing and lookup, not full knowledge replacement
- caution language, section meaning, and provenance interpretation remain in markdown
- the technique does not require schema expansion, a new `kag` domain, or a replacement for markdown authority

## Risks

### Failure modes

- frontmatter widens until it starts carrying section meaning or policy semantics that belong in markdown
- maintainers edit the derived catalog directly and break metadata-source parity
- routing questions pile up faster than the spine can answer, but the response is to add fields instead of narrowing the metadata problem

### Negative effects

- a clean catalog can create false confidence that the corpus is fully machine-readable when important meaning still lives only in authored markdown
- teams can start optimizing metadata shape before proving that the current catalog actually helps navigation or review
- shallow metadata can hide ambiguity if consumers forget to read the underlying technique or evidence notes

### Misuse patterns

- treating the catalog as a replacement for reading `TECHNIQUE.md`
- adding new fields because a future KAG layer might want them, rather than because current bounded routing needs them
- moving caution, relation rationale, or section payloads into frontmatter for convenience

### Detection signals

- proposed metadata additions mostly duplicate section prose or note content
- contributors ask to fix generated catalog data without touching source frontmatter
- the same routing question still requires opening markdown, but the response is more metadata churn rather than a better bundle or guide
- consumers interpret the metadata spine as a graph or policy surface instead of a bounded routing layer

### Mitigations

- keep metadata changes tied to one concrete routing problem at a time
- regenerate and validate derived catalog outputs instead of editing them by hand
- move meaning questions back to markdown bundles and notes before adding fields
- stop widening the spine when the next request is really for section lift, provenance lift, or relation review

## Validation

Verify the technique by confirming that:
- bundle identity and routing fields are visible in frontmatter
- derived catalog entries match source frontmatter
- the catalog helps answer bounded routing questions such as status, domain, or direct adjacency
- questions about deeper meaning still route back to markdown sections or notes
- no schema or frontmatter widening was needed beyond the bounded metadata spine

See `checks/metadata-spine-checklist.md` and `examples/frontmatter-to-catalog-entry.md`.
For repo-grounded origin evidence, see `notes/origin-evidence.md`.

## Adaptation notes

What can vary across projects:
- the exact bounded field set used for routing
- the catalog filename or projection format
- which repo-level navigation surfaces consume the metadata spine
- how often the catalog is rebuilt

What should stay invariant:
- metadata remains shallow
- the catalog is derived, not hand-maintained
- markdown sections still hold the real technique meaning
- the spine is justified by current routing value, not by future graph ambition

Do not widen the technique into richer schema just because later KAG work exists. The point is a bounded metadata spine, not metadata-first authorship or a replacement for markdown authority.

## Public sanitization notes

This public version generalizes the current metadata-spine contract and strips repo-specific implementation details that do not affect the reusable pattern. It does not claim that a graph platform or richer schema already exists.

## Example

See `examples/frontmatter-to-catalog-entry.md` for a small frontmatter block and the corresponding derived catalog entry.

## Checks

See `checks/metadata-spine-checklist.md`.

## Promotion history

- shaped inside `aoa-techniques` while the markdown-frontmatter-v2 catalog layer became the repo's metadata spine
- extracted into first public reusable form on 2026-03-19 as part of the initial KAG/source-lift family wave

## Future evolution

- strengthen second-context evidence once another markdown-first corpus adopts the same bounded metadata spine
- clarify when a routing problem should move to section lift or provenance lift instead of widening frontmatter
- keep schema/frontmatter expansion deferred until shallow metadata stops being enough
