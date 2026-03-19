# Adverse Effects Review

## Technique
- id: AOA-T-0006
- name: latest-alias-plus-history-copy

## Review focus
- current role: default storage contract for stable latest alias plus nested history copy
- current watch seam: keep downstream remediation and integrity consumers subordinate to storage invariants rather than letting them redefine the contract

## Failure modes
- latest alias and nested history drift because only one write path updates or one write quietly fails
- collectors double-count runs by mixing top-level alias data with nested history rows

## Negative effects
- dual-write layout adds reader-policy and migration complexity even when the summary payload stays simple
- a clean latest alias can create false confidence while historical accumulation is already broken

## Misuse patterns
- treating the pattern as a generic archival strategy instead of one bounded latest-plus-history contract
- adding extra alias layers or unofficial scan paths instead of enforcing one stable reader precedence

## Detection signals
- latest alias and history copy disagree on schema, status, or reported paths
- trend outputs jump unexpectedly after migration even though recent run summaries still look normal

## Mitigations
- narrow the layout back to one stable alias path and one nested history copy
- gate migration boundaries explicitly and re-establish alias/history parity before adding more storage variants

## Recommendation
- keep current `canonical` status and use this note as the watch surface for storage complexity or downstream-consumer language crowding out alias/history invariants
