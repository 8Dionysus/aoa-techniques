# Origin Evidence

## Technique

- id: AOA-T-0099
- name: isolated-service-stop-on-shared-substrate

## Source project

- name: abyss-stack
- source files:
  - `docs/TOS_GRAPH_CURATION.md`
  - `compose/profiles/curation.txt`

## Evidence

- The `tos-graph` owner-first landing established one bounded helper service inside a wider curation profile with shared substrate services that remained useful after the helper itself no longer needed to stay live.
- The reviewed closeout for that route stopped only the helper service after live verification while keeping shared substrate services alive for continued continuity and proof.
- The resulting pattern is smaller than full profile teardown and stronger than vague "just stop the thing" folklore because it requires explicit target naming, substrate naming, and post-stop checks for both absence and continuity.

## Interpretation

- The reusable core is not `tos-graph` itself; it is the bounded operational seam where one service can be stopped without widening into unnecessary teardown.
- The technique is source-backed because the owner route already exercised this stop posture in a live reviewed run, and the public bundle keeps only the reusable contract while removing machine-local detail.
