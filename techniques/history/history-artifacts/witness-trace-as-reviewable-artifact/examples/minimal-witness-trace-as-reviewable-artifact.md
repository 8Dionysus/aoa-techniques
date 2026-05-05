# Minimal Witness Trace As Reviewable Artifact

Use one structured trace plus one compact summary to preserve a nontrivial run before any downstream writeback.

Example witness artifact:

```json
{
  "run_id": "run-2026-03-23-auth-fix",
  "goal": "repair auth callback flow without losing provider fallback",
  "bounded_status": "completed_with_review_flags",
  "time_window": "2026-03-23T17:10:00Z/2026-03-23T17:42:00Z",
  "steps": [
    {
      "index": 1,
      "step_kind": "inspect",
      "intent": "trace current callback handling",
      "tool_visibility": "repo read",
      "observation": "fallback branch skips nonce reset",
      "state_delta": null
    },
    {
      "index": 2,
      "step_kind": "edit",
      "intent": "restore nonce reset in fallback branch",
      "tool_visibility": "file patch",
      "observation": "callback path updated",
      "state_delta": "auth callback logic changed"
    }
  ],
  "review_notes": [
    "manual provider fallback test still needed"
  ]
}
```

Example summary:

```md
# Witness Summary

- run goal: repair auth callback flow without losing provider fallback
- main result: fallback branch now restores nonce reset
- review flags: manual fallback test still needed
- inspect next: callback path plus fallback provider behavior
```

The important behavior is artifact-first review posture:

- the trace preserves ordered steps, tool visibility, and state deltas
- the summary tells a reviewer what to inspect next
- the artifact survives before any memory writeback or promotion route
- this is not a new memory object and not just a transcript export
