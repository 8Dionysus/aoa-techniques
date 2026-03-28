# minimal example seed

Graph state:
- `review-overlap` = done
- `draft-technique` = ready
- `sync-shared-docs` = blocked by `draft-technique`

Derived ready queue:
- `draft-technique`

Blocked:
- `sync-shared-docs` because `draft-technique` is not done

The point of the example is that the queue remains explainable from blocker state.
