# Adverse Effects Review

## Technique
- id: AOA-T-0044
- name: versionable-session-transcripts

## Review focus
- current role: canonical default for packaging already-saved session history into readable, versionable transcript artifacts
- current watch seam: keep the bundle strictly post-capture and transcript-shaped rather than letting capture, hosted sharing, search, or instruction-authority behavior become the real center of gravity

## Failure modes
- teams relabel raw autosave or chat-history persistence as if it already satisfied the transcript-packaging contract
- transcript packages become giant undifferentiated dumps with no bounded review unit
- canonical pressure widens the technique into transcript dashboards, hosted sharing, or history-to-rules behavior instead of preserving the readable artifact seam

## Negative effects
- transcript versioning can create noisy diffs and review overhead when a smaller summary would have been enough
- portable transcript artifacts can tempt teams to over-share raw history before sanitization or boundary review
- easy export can make transcript artifacts feel authoritative enough to displace authored rules, summaries, or decisions

## Misuse patterns
- treating raw saved session files as if they were already the exported review artifact
- using transcript packages as canonical repository instructions or policy notes
- folding transcript search, log viewing, or witness-trace semantics into the same bundle instead of preserving sibling boundaries

## Detection signals
- contributors cannot explain what the transcript package adds beyond `save sessions locally`
- exported artifacts are too large or too unstructured to support review, diffing, or citation
- transcripts start appearing where authored rules, decisions, or summaries should have remained the canonical object
- new guidance focuses more on viewer features or hosted sharing than on post-capture readable packaging

## Mitigations
- keep one explicit seam between capture and transcript packaging
- package one bounded review or handoff unit at a time instead of exporting undifferentiated history dumps
- redact or annotate before wider sharing when the raw transcript is not public-safe enough
- keep rules, decisions, memory behavior, and witness semantics in sibling techniques or other layers

## Recommendation
- keep current `canonical` status and use this note as the watch surface for capture creep, transcript-as-policy misuse, and drift into hosted viewer or witness-trace breadth
