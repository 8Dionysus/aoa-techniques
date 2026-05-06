# minimal example seed

Nodes:
- `draft-technique`
- `review-overlap`
- `sync-shared-docs`

Edges:
- `review-overlap -> draft-technique`
- `draft-technique -> sync-shared-docs`

Derived ready frontier:
- `review-overlap`

The point of the example is that ready work is computed from explicit blockers instead of being implied by chat history.
