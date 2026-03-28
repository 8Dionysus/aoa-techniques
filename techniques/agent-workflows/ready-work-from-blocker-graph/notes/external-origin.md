# External Origin Note

## Source

- source_repo: `https://github.com/steveyegge/beads`
- source_license: MIT
- inspired_by: not used in this import
- adapted_from: `README.md`, `cmd/bd/ready.go`, and `internal/storage/issueops/ready_work.go`

## What changed

- what_changed: narrowed the donor repository to one bounded pattern: derive ready work from blocker-aware graph state instead of treating open work as automatically ready
- invariant core kept: only blocker-free eligible work enters the ready frontier, blocked work stays excluded, and the queue remains explainable from visible graph state
- project-shaped details removed or generalized: tracker product semantics, gate-resume dispatch, claim workflow behavior, hierarchy-heavy planning, broad sort policy, CLI-specific flags, and donor runtime or storage details

## Public-safety review

- secrets or tokens removed: none from the donor surfaces used for this import
- private paths, URLs, or IDs removed: donor-specific issue IDs, flags, storage internals, and runtime references were generalized away
- environment-specific assumptions generalized: the public technique does not depend on Go, Dolt, the `bd` CLI, or one tracker implementation
- remaining public-safety concerns: the main risk is contract widening into prioritization policy or tracker doctrine, not data leakage

## Review notes

- why this adaptation is reusable here: many agent workflows need one honest answer to "what is actually ready now?" without smuggling in full backlog policy or platform semantics
- limits or follow-up review concerns: this first import intentionally excludes graph authoring, ranking doctrine, dispatch features, and hidden override policy
