# Adverse Effects Review

## Technique
- id: AOA-T-0043
- name: multi-source-primary-input-provenance

## Review focus
- current role: canonical default for marking one primary source input and supporting inputs when a bridge or docs surface combines multiple source materials
- current watch seam: keep the bundle centered on visible source-priority ordering rather than graph semantics, evidence grading, retrieval ranking, proof doctrine, or note-provenance metadata

## Failure modes
- all inputs are flattened into an equal list and the source that anchors the surface disappears
- supporting inputs quietly become hidden primary sources because the authored markdown does not preserve priority
- primary/supporting labels are misread as trust scores or retrieval ranking
- downstream readers reorder or summarize sources without carrying the priority relation forward

## Negative effects
- canonical status can make authors over-label inputs even when priority does not matter
- explicit priority can make a surface feel less neutral if writers do not explain why the primary input anchors the contract
- supporting sources may be underused when readers treat them as merely decorative
- a simple ordering rule can attract broader evidence-quality debates that belong elsewhere

## Misuse patterns
- using primary/supporting labels to encode trust score, evidence grade, or search ranking
- treating note provenance handles as enough to prove multi-source input priority
- expanding bridge surfaces into graph traversal, synthesis policy, or proof-fit assessment
- naming several primary inputs because choosing one anchor is uncomfortable

## Detection signals
- reviewers cannot answer which source anchors the surface after reading it
- downstream docs cite supporting inputs as if they owned the main meaning
- discussions shift toward ranking, retrieval, graph export, or proof scoring
- the priority order appears only in generated metadata, not in authored markdown

## Mitigations
- name exactly one primary input when the bridge needs priority
- name supporting inputs as useful but secondary to the primary anchor
- keep the order visible in authored markdown and preserve it in downstream reader surfaces
- route evidence grade, ranking, traversal, graph export, and proof-fit work to sibling techniques or owner repos
- revisit canonical status if the bundle starts being used as a ranking or proof doctrine shortcut

## Recommendation
- keep current `canonical` status and use this note as the watch surface for source flattening, hidden ranking, over-labeling, and bridge drift into graph or proof authority
