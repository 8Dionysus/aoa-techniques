# Minimal Versionable Session Transcripts

Start from an already-saved session artifact and package only the transcript needed for one review thread.

Existing saved history:

```text
.specstory/history/2026-03-23-codex-fix-session.md
.specstory/history/2026-03-23-codex-followup-session.md
```

Curated export for one PR:

```text
docs/review-transcripts/pr-118-auth-flow-transcript.md
```

Example transcript header:

```md
# PR 118 Transcript

- source_sessions:
  - 2026-03-23-codex-fix-session
  - 2026-03-23-codex-followup-session
- exported_at: 2026-03-23T18:40:00Z
- purpose: review and handoff

## Context

This transcript packages the two saved sessions that led to the auth-flow change.
Irrelevant shell noise was removed, and one reviewer note was added before commit.
```

The important behavior is post-capture transcript packaging:

- the source sessions were already saved before this technique began
- one review unit intentionally combines the two relevant conversations
- the exported transcript carries stable metadata for commit and comparison
- a reviewer can trim or annotate before sharing
- repository rules and decisions still stay in authored docs instead of moving into the transcript
