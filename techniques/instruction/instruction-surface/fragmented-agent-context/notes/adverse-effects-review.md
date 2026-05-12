# Adverse Effects Review

## Technique

- id: AOA-T-0030
- name: fragmented-agent-context

## Review focus

- current role: canonical default for bounded fragment-first agent-context authoring before deterministic assembly or reporting becomes the center of gravity
- current watch seam: keep the bundle centered on editable fragment sources rather than generated composition, CI reporting, runtime injection, path-trigger behavior, or rule-toggle policy

## Failure modes

- fragments become arbitrary small files without clear ownership or topic scope
- a combined or generated context becomes the file contributors edit first
- conditional runtime loading distracts reviewers from the authored fragment layer
- fragment count grows until finding the relevant instruction is harder than reading one larger file

## Negative effects

- fragment-first authoring can add navigation friction for small projects
- local fragments can hide duplicate guidance across nearby files
- source partitioning can create a false sense of modularity when the real problem is stale or conflicting content
- canonical status can encourage over-fragmentation before a repository has enough context to justify it

## Misuse patterns

- using the bundle for deterministic composition into one artifact that belongs to `AOA-T-0012`
- using the bundle for CI-facing context reports that belong to `AOA-T-0032`
- treating file-glob activation, rule toggles, or runtime injection as the reusable object
- creating generic catch-all fragments that only move clutter from one file into many files

## Detection signals

- reviewers cannot explain what each fragment owns
- several fragments repeat the same rule with small wording differences
- contributors edit the generated or combined context instead of the source fragments
- discussion focuses on activation mechanics rather than fragment scope, placement, and authorship

## Mitigations

- keep one concern per fragment and name files by owned scope
- merge or delete fragments whose boundaries no longer help reviewers
- route edits back to fragments instead of patching generated or combined context
- keep deterministic assembly, CI reports, runtime injection, path-trigger behavior, and toggle policy in sibling techniques or owner repos
- revisit canonical status if the technique starts being used mainly for fragment quantity rather than clearer source ownership

## Recommendation

- keep current `canonical` status and use this note as the watch surface for over-fragmentation, duplicate guidance, generated-output drift, and sibling-boundary widening around the instruction-surface cluster
