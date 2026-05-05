# Review Checklist

Use this checklist to validate whether a change actually followed `plan-diff-apply-verify-report`.

- `PLAN`: the goal, touched surfaces, main risk, and rollback idea are explicit before apply.
- `DIFF`: the change is scoped to the stated goal and avoids unrelated refactors.
- `APPLY`: the implementation matches the declared plan instead of drifting into adjacent work.
- `VERIFY`: at least one concrete check, smoke, or review step is named and its result is reported.
- `REPORT`: the final summary states what changed, what was validated, and how recovery would work.
- `PUBLIC HYGIENE`: examples and notes contain no secrets, private URLs, internal hostnames, or private paths.
