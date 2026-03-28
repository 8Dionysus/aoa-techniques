# External Origin Note

## Source

- source_repo: `https://github.com/steveyegge/beads`
- source_license: MIT
- inspired_by: not used in this import
- adapted_from: `README.md`, `cmd/bd/ready.go`, `internal/storage/issueops/ready_work.go`, `internal/storage/dependency_queries.go`, and `docs/graph-links.md`

## What changed

- what_changed: narrowed the donor repository to one bounded pattern: explicit dependency nodes plus blocker-aware ready-work derivation for coding tasks
- invariant core kept: task dependencies are explicit, blocked work can be explained by unmet prerequisites, and ready work is derived from current graph state instead of remembered informally
- project-shaped details removed or generalized: persistent memory framing, Dolt-backed issue tracking, molecule and epic hierarchy features, graph-link taxonomy beyond blocking, auto-claim flows, CLI-specific behavior, and donor runtime or storage details

## Public-safety review

- secrets or tokens removed: none from the donor surfaces used for this import
- private paths, URLs, or IDs removed: donor-specific task IDs, command flags, storage internals, and runtime references were generalized away
- environment-specific assumptions generalized: the public technique does not depend on Go, Dolt, the `bd` CLI, or one tracker implementation
- remaining public-safety concerns: the main risk is contract widening into memory-system or project-management doctrine, not data leakage

## Review notes

- why this adaptation is reusable here: multi-step agent coding work often needs blocker-aware coordination without carrying a full tracker platform or long-lived memory substrate
- limits or follow-up review concerns: this first import intentionally excludes knowledge-graph features, automated claiming or dispatch, hierarchy-heavy planning, and persistent memory semantics
