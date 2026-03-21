# Confirmation Gated Mutating Action Checklist

- Name the proposed mutation before any write or execution step runs.
- Keep read or plan work separate from the confirmed mutation.
- Require one visible confirmation before the mutating action starts.
- Make the confirmation text specific enough to match the actual change.
- Stop after the confirmed mutation instead of chaining a hidden follow-up loop.
- Escalate to a broader workflow technique when the task now needs multiple steps.
