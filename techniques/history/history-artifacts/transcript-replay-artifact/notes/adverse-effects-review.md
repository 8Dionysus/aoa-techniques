# Adverse Effects Review

## Technique
- id: AOA-T-0066
- name: transcript-replay-artifact

## Review focus
- promotion from `promoted` to `canonical` after exact-fit public reinforcement from `dataprofessor/cortex-replay` and Snowflake's public Cortex Code replay guide
- failure cases where post-capture replay is mistaken for first-save capture, transcript packaging, local indexing, witness tracing, hosted sharing, dashboards, editors, or a replay platform

## Failure modes
- the replay artifact loses the source-artifact reference and quietly becomes the only history surface
- replay generation starts from live capture or runtime monitoring instead of an already-saved session artifact
- visual replay polish hides missing turns, redacted context, or dropped tool-call results
- hosted sharing, live demos, embedded viewers, or dashboard products become more central than the replay artifact
- replay is treated as proof of state changes even though it lacks witness-level state deltas, review flags, or run-forensics semantics

## Negative effects
- replay can add packaging work where a plain transcript would be easier to review
- a polished replay can overstate fidelity after filtering, time-window trimming, or secret redaction
- reviewers may treat convenient playback as source truth and stop opening the saved transcript or capture artifact
- replay-product features can pull the technique into accounts, publishing, analytics, or collaboration behavior

## Misuse patterns
- using replay as a substitute for [AOA-T-0044](../versionable-session-transcripts/TECHNIQUE.md), [AOA-T-0053](../local-first-session-index/TECHNIQUE.md), or [AOA-T-0045](../witness-trace-as-reviewable-artifact/TECHNIQUE.md)
- importing skill installation, CLI packaging, theme systems, live demos, iframe embedding, or hosted viewer URLs as technique requirements
- treating replay controls, playback speed, bookmarks, or UI chrome as the invariant instead of source-derived ordered flow
- publishing replay artifacts before public-safe redaction and source-scope review

## Detection signals
- the replay artifact cannot identify which saved session or transcript family it came from
- the explanation starts with viewer product features instead of post-capture transformation and source-artifact authority
- reviewers expect search, indexing, analytics, dashboard, witness, or proof behavior from the replay object
- replay examples include private session IDs, local directory paths, account names, hosted share links, or unsanitized secrets
- a replay source supports only hosted viewing or dashboards and cannot emit one bounded derivative artifact

## Mitigations
- keep replay derivative and source-linked: saved session artifacts remain authoritative
- preserve order, turn boundaries, timestamps, or equivalent flow cues that make replay materially different from plain transcript text
- record filtering, redaction, hidden thinking, hidden tool calls, or time-window choices as limitations of the replay
- route transcript packaging, history indexing, witness tracing, hosted publishing, editor/dashboard behavior, and memory doctrine to sibling surfaces
- reject replay evidence that cannot survive without accounts, hosted services, dashboards, or product-specific viewer semantics

## Recommendation
- safe to promote as a canonical history technique when the implementation starts from already-saved session artifacts, emits one bounded replay artifact, preserves reviewable flow cues, and keeps source-artifact authority visible
- use this note as the watch surface for capture creep, viewer-product creep, hosted-sharing creep, replay-as-proof overclaim, and replay replacing saved transcript authority
