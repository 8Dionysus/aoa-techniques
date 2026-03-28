# Adverse Effects Review

## Technique
- id: AOA-T-0053
- name: local-first-session-index

## Review focus
- current role: canonical default for derivative local searchable indexing over already-saved session artifacts
- current watch seam: keep the index local, rebuildable, and subordinate to the saved artifacts instead of letting dashboard, sync, or memory behavior become the real contract

## Failure modes
- teams start treating the index as the authoritative history layer instead of a derivative lookup surface
- results no longer point back to stable source artifacts, so review stops at snippets or metadata
- canonical pressure widens the bundle into hosted dashboards, analytics, or remote-sync product behavior instead of preserving the local-first derivative index

## Negative effects
- a fast index can tempt operators to act on summaries or snippets without reopening the source artifact when nuance matters
- indexed metadata can flatten session context too aggressively and hide what the original artifact actually contained
- a polished local database can feel more authoritative than the files it was derived from

## Misuse patterns
- mixing capture, indexing, transcript packaging, and dashboard analytics into one technique
- using the index as memory recall, ranking policy, or instruction authority
- treating remote sync or team-wide viewer features as if they were part of the invariant local-first contract

## Detection signals
- search hits no longer expose stable source paths, IDs, or equivalent references back to saved artifacts
- the index cannot be rebuilt from local artifacts alone
- design discussions drift toward dashboards, sync, analytics, or memory features more than toward derivative lookup
- users act on index summaries without reopening the original artifact for real review

## Mitigations
- keep stable source references in every useful hit
- make rebuild-from-local-artifacts part of the validation story
- preserve the habit of reopening source artifacts when review or reuse matters
- split dashboards, remote sync, and memory behavior into narrower sibling techniques instead of widening this one

## Recommendation
- keep current `canonical` status and use this note as the watch surface for index-as-authority drift, source-reference loss, and dashboard or memory creep
