# Canonical Readiness

## Technique
- id: AOA-T-0066
- name: transcript-replay-artifact

## Verdict
- approve for canonical promotion

## Evidence summary
- external origin: the imported technique has a bounded donor contract and explicit exclusions around hosted viewers, dashboards, publish flows, and replay-product breadth
- second context: `aoa-techniques` now records the same replay-artifact contract as a documentation-first adaptation with one example and one checklist
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- `dataprofessor/cortex-replay` provides exact-fit public reinforcement beyond the original Claude/Codex/Cursor viewer family: it converts already-saved Cortex Code JSON session transcripts into one self-contained interactive HTML replay, supports listing saved sessions, selecting the most recent or a specific saved session, filtering turns and time ranges, adding bookmarks, controlling playback speed, hiding thinking or tool-call blocks, and redacting secrets before output
- Snowflake's public Cortex Code replay guide independently frames the same workflow for a different AI coding assistant surface: sessions are already saved as JSON transcripts, `cortex-replay` generates a self-contained interactive HTML replay, and the output can be opened locally, shared, or embedded without depending on a hosted replay service
- validation strength: the bundle now carries one checklist, one example, a clean external-origin note, a documentation-first second context, and public cross-context reinforcement for the same post-capture replay-artifact contract

## Default-use rationale
- this is the right canonical default when the main problem is replaying already-saved session history for review without reopening capture semantics or widening into viewer-product doctrine
- it remains narrower than [AOA-T-0044](../versionable-session-transcripts/TECHNIQUE.md) because it owns replayable flow rather than readable Markdown transcript packaging
- it also remains narrower than [AOA-T-0053](../local-first-session-index/TECHNIQUE.md) because it does not build a general lookup layer across many saved sessions
- it is now strong enough as a canonical default because Cortex Replay repeats the same saved-session-to-replay shape in a separate live assistant ecosystem while still letting this bundle reject Cortex-specific session directories, skill installation, themes, live demos, embedded iframes, hosted publishing, dashboard behavior, and broader viewer-platform semantics

## Fresh public-safety check
- review date: 2026-05-12
- result: pass
- sanitization still holds: the bundle keeps only the reusable replay seam and excludes hosted sharing, dashboards, editors, and product packaging
- public reuse check: the example, checklist, and adaptation notes remain understandable without hidden donor-repo context; the inspected `dataprofessor/cortex-replay` source is MIT licensed and no source code, private session data, local directory names, session IDs, local account details, hosted URLs, or product-specific setup instructions were copied into the technique

## Remaining gaps
- no blocker remains for canonical status
- future replay sources can reinforce the default, but they must preserve the narrow boundary: already-saved session artifacts, one replay transformation, preserved order or flow cues, derivative replay output, source-artifact authority, and explicit separation from capture, packaging, indexing, witness forensics, hosted sharing, dashboards, editors, and replay platforms

## Recommendation
- move `AOA-T-0066` to `canonical`
- add an adverse-effects review to preserve the boundary between transcript replay, transcript packaging, local indexing, witness tracing, hosted viewers, dashboards, publishing, and product platform semantics
