# Adverse Effects Review

## Technique
- id: AOA-T-0026
- name: session-capture-as-repo-artifact

## Review focus
- current role: canonical default for first-save AI coding session capture as reviewable, project-visible history artifacts
- current watch seam: keep the bundle centered on deliberate artifact capture and project visibility rather than letting ignored local logs, memory systems, transcript export, search, or instruction authority become the real contract

## Failure modes
- teams commit raw session logs accidentally and later treat the accident as proof of good artifact discipline
- ignored local chat-history files are mistaken for versioned project history even though they are not reviewable through the repository
- captured sessions quietly become the de facto instruction source because stronger authored rules, decisions, or summaries are not maintained
- canonical pressure widens the technique into transcript packaging, local search, cloud sync, or memory recall instead of preserving first-save capture

## Negative effects
- saved sessions can create large, noisy, or sensitive artifacts when a short summary or decision note would have been enough
- local session history increases review, redaction, retention, and storage burden
- easy artifact capture can tempt teams to publish private reasoning, credentials, paths, or internal chronology before sanitization
- project-visible history can feel more authoritative than authored source-of-truth docs if the boundary is not kept explicit

## Misuse patterns
- treating every tool-created history file as commit-worthy without review
- using session artifacts as canonical repository policy, future-agent instructions, or memory substrate
- folding transcript export, indexing, dashboarding, or hosted sharing into the capture technique
- using captured history to bypass decision records, handoff packets, or maintained status surfaces

## Detection signals
- contributors cannot explain which session artifacts are safe to retain, redact, share, or delete
- repository rules start linking to session history where authored docs or decisions should be the source of truth
- the saved artifact layer cannot be inspected without a cloud account, hidden runtime state, or a tool-specific search database
- new guidance focuses more on search, memory, or transcript viewer features than on first-save artifact discipline

## Mitigations
- choose one explicit project-scoped artifact home and one review path before broad capture
- review, redact, or summarize before committing or sharing raw session history
- keep authored rules, decisions, status, summaries, memory objects, and transcript packages in their own surfaces
- treat ignored local logs as adjacent evidence only until a project deliberately retains them as reviewable artifacts
- split search, indexing, transcript packaging, cloud sync, and history-to-instructions behavior into sibling techniques or owning repos

## Recommendation
- keep current `canonical` status and use this note as the watch surface for accidental log commits, capture-as-policy drift, ignored-local-state confusion, and expansion into memory, search, transcript, or instruction authority
