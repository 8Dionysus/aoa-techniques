# Adverse Effects Review

## Technique
- id: AOA-T-0002
- name: source-of-truth-layout

## Review focus
- current role: default repository layout pattern for canonical homes and update-routing rules
- current watch seam: keep the role map useful for routing without turning small repositories into document choreography systems

## Failure modes
- the role map no longer routes recurring updates to one obvious canonical home
- contributors bypass the layout and duplicate the same status or policy across multiple primary documents
- a repository keeps its named role map but still needs manual coordination before ordinary updates feel safe to land

## Negative effects
- over-structuring can add maintenance cost faster than it removes drift
- a repository can look orderly while change friction quietly rises
- a tidy-looking docs surface can create false order while duplicate summaries and routing ambiguity keep returning underneath it

## Misuse patterns
- treating the full recommended role map as mandatory even when a smaller repo needs a reduced variant
- adding more docs instead of simplifying or collapsing roles that no longer prevent drift
- responding to routing confusion by introducing another coordination surface instead of removing competing canonical homes

## Detection signals
- the same status or policy update keeps appearing in more than one primary document
- contributors repeatedly ask where a recurring update belongs because the routing rule is no longer obvious
- a sample update still requires side-channel negotiation even though the repository looks clean and fully mapped

## Mitigations
- shrink the role map for smaller repositories instead of preserving a larger operational layout by habit
- refresh or simplify canonical-home rules whenever duplicate-summary relapse appears
- collapse roles or remove low-value docs before adding another structure layer to explain the same routing problem

## Recommendation
- keep current `canonical` status and use this note as the watch surface for false order, duplicate-summary relapse, and layout growth that adds coordination cost without routing value
