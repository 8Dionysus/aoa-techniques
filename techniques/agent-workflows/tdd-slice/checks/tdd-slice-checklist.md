# TDD Slice Checklist

Use this checklist to verify that a change really stayed inside a bounded `tdd-slice`.

- The target behavior was stated explicitly before implementation changed.
- The initial test surface targeted observable behavior rather than hidden internals.
- The implementation diff stayed inside the declared slice.
- Refactor work stayed subordinate to making the bounded slice pass.
- Unrelated cleanup was deferred instead of being folded into the same change.
- The final validation step named which tests passed.
- The final report stated both the covered behavior and what remained out of scope.
