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
- the top-level docs stay short and polished while their routing aliases no longer reflect where current truth actually moved

## Negative effects
- aggressive trimming can make operational truth harder to find even while the entrypoint docs look cleaner
- cleanup can hide unresolved routing gaps by removing detail faster than the repo learns where that detail belongs
- the repo can project false cleanliness while newcomers still cannot orient themselves without side-channel help

## Misuse patterns
- deleting detail instead of routing it to canonical homes
- treating short `README` or `MANIFEST` files as the goal even when navigability gets worse
- leaving stale snapshot links in place because the entrypoint still appears neat and lightweight

## Detection signals
- new readers still cannot find detailed current state quickly even though entrypoint docs are short
- teams keep re-adding summary prose because the snapshot no longer feels sufficient for orientation
- the top-level docs are praised for neatness while review comments still ask where active truth now lives

## Mitigations
- restore just enough orientation context to make the snapshot navigable before adding back long chronology
- fix canonical links and routing first instead of letting cleanliness stand in for usability
- treat stale aliases or broken routing as entrypoint failures and repair them before cutting more prose

## Recommendation
- keep current `canonical` status and use this note as the watch surface for navigability loss, stale routing aliases, and false cleanliness disguised as entrypoint discipline
