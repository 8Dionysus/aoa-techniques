# Adverse Effects Review

## Technique
- id: AOA-T-0018
- name: markdown-technique-section-lift

## Review focus
- current role: canonical default section-lift entrypoint for bounded expand-time inspection after bundle-level routing in the KAG/source-lift family
- current watch seam: keep section lift bounded to source-owned stable `TECHNIQUE.md` sections without widening into a generic bundle-section program or replacing metadata, provenance, relation, or caution companions

## Failure modes
- unstable or donor-shaped headings get lifted as if they were long-lived section anchors, so consumers start depending on sections that should still be rewritten freely
- readers or tools treat the lifted section surface as a substitute for the bundle and stop routing back to the authored markdown when the surrounding contract matters
- canonical pressure widens section lift into section IDs, graph behavior, or all-bundle section authority instead of keeping the current technique-specific contract explicit

## Negative effects
- section snippets can create false confidence that one bounded section is enough to understand the whole technique
- an easy expand-time surface can make metadata, provenance, or caution questions drift into the section layer even when those questions belong to sibling techniques
- a successful canonical default can attract requests to widen the lift faster than the authored bundles can keep stable headings meaningful

## Misuse patterns
- using `AOA-T-0018` as a substitute for `AOA-T-0019`, `AOA-T-0020`, `AOA-T-0021`, or `AOA-T-0022`
- adding or renaming headings mainly to satisfy extraction consumers rather than to improve the authored bundle
- fixing generated section surfaces directly instead of updating `TECHNIQUE.md` and regenerating

## Detection signals
- proposals start asking for section IDs, weighted routing, or graph semantics to keep the lift usable
- readers cite lifted sections but cannot explain how those sections fit into the full bundle contract
- section lift starts being chosen for bundle identity, provenance, adjacency, or caution questions that should stop at the sibling surfaces
- review comments focus on generated section output instead of the source markdown headings and prose

## Mitigations
- keep the stable heading set explicit and drop weak section targets before widening the lift
- route bundle identity to `AOA-T-0019`, note provenance to `AOA-T-0020`, direct adjacency to `AOA-T-0021`, and caution lookup to `AOA-T-0022`
- regenerate derived section outputs from markdown instead of hand-editing them
- treat any broader bundle-section request as a candidate sibling technique rather than silently widening `AOA-T-0018`

## Recommendation
- keep current `canonical` status and use this note as the watch surface for generic bundle-section creep, manifest overread, and section lift replacing source markdown authority
