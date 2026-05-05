# Adverse Effects Review

## Technique
- id: AOA-T-0006
- name: latest-alias-plus-history-copy

## Review focus
- current role: default storage contract for stable latest alias plus nested history copy
- current watch seam: keep a clean latest alias from masking history-trust drift, and keep storage complexity subordinate to one stable latest-plus-history contract

## Failure modes
- the latest alias looks healthy while nested history parity or reader precedence is already drifting
- collectors double-count runs by mixing top-level alias data with nested history rows
- migration or backfill logic quietly crosses the first dual-write boundary and corrupts accumulation trust

## Negative effects
- dual-write layout adds reader-policy and migration complexity even when the summary payload stays simple
- storage variants and migration exceptions can multiply faster than teams re-check historical trust
- a clean latest alias can create false confidence while historical accumulation is already broken

## Misuse patterns
- treating the pattern as a generic archival strategy instead of one bounded latest-plus-history contract
- adding extra alias layers, unofficial scan paths, or retrospective backfill instead of enforcing one stable reader precedence

## Detection signals
- latest alias and history copy disagree on schema, status, or reported paths
- trend outputs jump unexpectedly after migration even though recent run summaries still look normal
- incident review keeps finding the newest summary quickly, but recent totals or streaks stop reconciling with it

## Mitigations
- narrow the layout back to one stable alias path and one nested history copy
- gate migration boundaries explicitly and re-establish alias/history parity before adding more storage variants

## Recommendation
- keep current `canonical` status and use this note as the watch surface for alias/history false confidence or storage-complexity drift crowding out the bounded contract
