# Adverse Effects Review

## Technique
- id: AOA-T-0021
- name: bounded-relation-lift-for-kag

## Review focus
- current role: canonical default for direct typed one-hop relation hints in the KAG/source-lift family
- current watch seam: keep the edge layer bounded to family-scoped adjacency hints instead of letting it drift into graph traversal, ranking, or rationale storage

## Failure modes
- the relation surface widens beyond one-hop direct hints and starts implying multi-step navigation
- new consumers treat typed edges as ranking or transitive truth
- relation vocabulary grows to patch unclear bundle boundaries instead of improving the source docs

## Negative effects
- a useful edge surface can make the repository feel more graph-ready than it really is
- contributors can start opening relation consumers before reading the underlying bundle or review docs
- same-kind relation hints can duplicate semantic-review work if they start answering "why" instead of just "what is adjacent"

## Misuse patterns
- feeding direct relation hints into graph-style traversal or scoring logic
- adding new relation types because one consumer wants richer semantics
- using relation hints as a substitute for semantic review or markdown rationale
- widening the family-scoped surface into open-ended same-kind exploration

## Detection signals
- proposals ask for multi-hop expansion, ranking, or weighted edges
- relation consumers start surfacing techniques outside the bounded KAG/source-lift family without a new source contract
- reviewers ask "why does this edge exist?" and the answer only lives in generated routing output
- `recommended_paths` pressure starts pushing toward same-kind traversal instead of staying dependency-driven

## Mitigations
- keep the relation-hint surface family-scoped and one-hop only
- preserve `recommended_paths` as dependency-driven and separate from relation hints
- route edge rationale back to authored markdown and semantic-review docs
- remove noisy edges before considering any vocabulary growth

## Recommendation
- keep current `canonical` status and use this note as the watch surface for graph creep, relation-vocabulary widening, and source-meaning overread
