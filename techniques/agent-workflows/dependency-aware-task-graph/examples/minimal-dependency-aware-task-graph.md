# Minimal dependency-aware-task-graph example

Suppose a landing workflow has four bounded tasks:

- `review-overlap`
- `draft-bundle`
- `sync-shared-surfaces`
- `run-release-check`

Dependencies:

- `draft-bundle` depends on `review-overlap`
- `sync-shared-surfaces` depends on `draft-bundle`
- `run-release-check` depends on `sync-shared-surfaces`

Current state:

- `review-overlap`: open
- `draft-bundle`: open
- `sync-shared-surfaces`: open
- `run-release-check`: open

Derived ready frontier:

- `review-overlap`

After `review-overlap` completes, the graph changes:

- `review-overlap`: done
- `draft-bundle`: open
- `sync-shared-surfaces`: open
- `run-release-check`: open

New derived ready frontier:

- `draft-bundle`

The point of the example is that the next safe step comes from explicit dependency state, not from whoever remembers the workflow best.
