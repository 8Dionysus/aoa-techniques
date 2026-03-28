# Minimal ready-work-from-blocker-graph example

Suppose a landing queue is derived from this current state:

- `review-overlap`: done
- `draft-technique`: open and blocker-free
- `sync-shared-docs`: open but blocked by `draft-technique`
- `run-release-check`: open but blocked by `sync-shared-docs`

Derived ready queue:

- `draft-technique`

Blocked exclusions:

- `sync-shared-docs` because `draft-technique` is not done
- `run-release-check` because `sync-shared-docs` is not done

After `draft-technique` completes, the derived frontier changes:

- `sync-shared-docs`

The point of the example is that the queue stays explainable from blocker state instead of being rebuilt from memory or open-task sprawl.
