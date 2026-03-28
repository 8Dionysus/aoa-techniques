# approval-bound-durable-jobs checklist

- [ ] the job keeps a stable identity across pause and resume
- [ ] checkpoint or status state survives the approval seam
- [ ] continuation does not happen until approval is explicit
- [ ] resume depends on durable state rather than hidden memory
- [ ] the example stays smaller than a scheduler, queue product, or orchestration platform
- [ ] one-shot boundary gates, packet receipt, and broader governance stacks stay outside the invariant core
- [ ] a reviewer can tell whether the job is running, paused, waiting for approval, or completed
- [ ] the public wording remains reusable and sanitized
