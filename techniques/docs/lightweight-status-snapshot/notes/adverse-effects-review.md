# Adverse Effects Review

## Technique
- id: AOA-T-0009
- name: lightweight-status-snapshot

## Review focus
- current role: default top-level snapshot discipline once canonical homes for detailed truth already exist
- current watch seam: keep entrypoint docs short without making orientation or current-state discovery harder

## Failure modes
- the snapshot becomes too thin to point readers toward the right current detail
- outward links go stale after the doc map evolves

## Negative effects
- aggressive trimming can make operational truth harder to find even while the entrypoint docs look cleaner
- cleanup can hide unresolved routing gaps by removing detail faster than the repo learns where that detail belongs

## Misuse patterns
- deleting detail instead of routing it to canonical homes
- treating short `README` or `MANIFEST` files as the goal even when navigability gets worse

## Detection signals
- new readers still cannot find detailed current state quickly even though entrypoint docs are short
- teams keep re-adding summary prose because the snapshot no longer feels sufficient for orientation

## Mitigations
- restore just enough orientation context to make the snapshot navigable before adding back long chronology
- fix canonical links and routing first instead of letting cleanliness stand in for usability

## Recommendation
- keep current `canonical` status and use this note as the watch surface for navigability loss disguised as entrypoint cleanliness
