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

## Negative effects
- over-structuring can add maintenance cost faster than it removes drift
- a repository can look orderly while change friction quietly rises

## Misuse patterns
- treating the full recommended role map as mandatory even when a smaller repo needs a reduced variant
- adding more docs instead of simplifying or collapsing roles that no longer prevent drift

## Detection signals
- the same status or policy update keeps appearing in more than one primary document
- contributors repeatedly ask where a recurring update belongs because the routing rule is no longer obvious

## Mitigations
- shrink the role map for smaller repositories instead of preserving a larger operational layout by habit
- refresh or simplify canonical-home rules whenever duplicate-summary relapse appears

## Recommendation
- keep current `canonical` status and use this note as the watch surface for duplicate-summary relapse or layout growth without routing value
