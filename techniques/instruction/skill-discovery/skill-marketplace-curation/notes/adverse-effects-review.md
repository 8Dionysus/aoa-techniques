# Adverse Effects Review

## Technique
- id: AOA-T-0041
- name: skill-marketplace-curation

## Review focus
- current role: canonical default for a bounded editorial discovery layer over upstream-owned skill sources
- current watch seam: keep the bundle centered on local discoverability and editorial grouping rather than mirror provenance, source health, installer behavior, registry governance, trust scoring, or capability ownership

## Failure modes
- the curated catalog starts acting as the canonical source for the underlying skills
- entries are copied into a list without enough editorial grouping, summaries, or source links to add real discovery value
- installability, safety, popularity, or compatibility claims appear without a separate owning review surface
- categories and featured rows become hidden ranking policy rather than lightweight navigation

## Negative effects
- canonical status can encourage broad skill catalogs that are easy to browse but hard to verify
- curated lists can launder weak or stale upstream skills by placing them beside stronger entries
- editorial grouping can bias users toward visible entries without recording why they were selected
- discovery surfaces can become large enough that maintenance becomes registry work in disguise

## Misuse patterns
- using curation as a substitute for upstream mirroring provenance, source-readiness checks, or security review
- treating category placement as proof of quality or trust
- mixing installer commands and registry payload details into the editorial catalog contract
- hiding upstream ownership behind local descriptions and badges

## Detection signals
- entries lack visible upstream source links or clear ownership
- catalog language talks about install, trust, score, or verification more than discovery and grouping
- maintainers cannot explain the editorial reason an entry is listed
- users treat the curated list as the authoritative skill source instead of a navigation layer

## Mitigations
- keep source ownership and outbound links visible for each curated entry
- keep curation descriptions short, editorial, and separate from install or trust claims
- route source health, mirroring provenance, security review, and registry governance to sibling techniques
- periodically prune or mark stale entries rather than expanding the catalog indefinitely
- revisit canonical status if the technique is used mainly for registry operation or ranking rather than editorial discoverability

## Recommendation
- keep current `canonical` status and use this note as the watch surface for catalog authority drift, thin curation, hidden ranking, and install or trust overreach
