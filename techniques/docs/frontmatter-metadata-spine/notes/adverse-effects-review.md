# Adverse Effects Review

## Technique
- id: AOA-T-0019
- name: frontmatter-metadata-spine

## Review focus
- current role: canonical default metadata spine for bundle-level routing and lookup in the KAG/source-lift family
- current watch seam: keep the spine bounded to shallow frontmatter and derived catalog outputs without letting metadata replace markdown meaning

## Failure modes
- frontmatter widens until it starts carrying section meaning, rationale, or policy semantics that belong in markdown
- contributors edit generated catalog files directly and break source-to-derived parity
- routing consumers start treating the metadata spine as a graph layer instead of a bounded lookup surface

## Negative effects
- a successful catalog can create false confidence that the corpus is machine-readable end to end when key meaning still lives only in authored markdown
- schema creep can raise maintenance cost faster than it improves routing
- metadata-first habits can make downstream consumers skip the bundle and evidence notes that still hold the real contract

## Misuse patterns
- adding fields because a future KAG layer might want them instead of because a current routing problem requires them
- fixing generated catalog entries by hand instead of editing frontmatter and regenerating
- using the metadata spine as a substitute for `AOA-T-0018`, `AOA-T-0020`, `AOA-T-0021`, or `AOA-T-0022`

## Detection signals
- proposed metadata changes mostly duplicate section prose or note content
- review comments focus on generated files instead of source frontmatter
- consumers stop opening `TECHNIQUE.md` even when the question is about meaning, caution, or provenance

## Mitigations
- keep metadata additions tied to one concrete routing problem at a time
- regenerate and validate the catalog instead of editing derived outputs by hand
- route section meaning, provenance argument, direct relations, and caution review back to the companion markdown-first techniques

## Recommendation
- keep current `canonical` status and use this note as the watch surface for schema creep, catalog overread, direct generated-file editing, or metadata replacing markdown authority
