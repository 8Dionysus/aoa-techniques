# Minimal commit-triggered-background-review example

Trigger:

- commit `abc1234`

Review artifact fields:

- `commit_ref`
- `review_scope`
- `findings[]`
- `generated_at`

Minimal contract:

- the commit boundary is visible
- the review runs after that boundary
- findings remain read-only output
- any later fix step is separate from this artifact

The point of the example is that the review output is an artifact tied to a visible commit boundary, not an automatic rewrite or merge loop.
