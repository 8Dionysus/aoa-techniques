# Adverse Effects Review

## Technique
- id: AOA-T-0049
- name: dependency-aware-task-graph

## Review focus
- current role: canonical default for modeling bounded multi-step work as explicit dependency nodes and blocker edges before choosing ready execution slices
- current watch seam: keep the bundle centered on prerequisite edges, blocked reasons, ready frontier recomputation, and reviewable work slices rather than widening into memory, dispatch, ranking, staffing, full tracker, or project-management doctrine

## Failure modes
- graph nodes become vague themes instead of reviewable work slices
- dependency edges encode preference or narrative order rather than true blockers
- stale edges keep work blocked after the prerequisite is actually complete
- cycles or hidden dependencies make the ready frontier misleading
- the graph becomes a source of proof instead of a coordination surface feeding later review and validation

## Negative effects
- graph upkeep can slow simple work that needs only one bounded task
- a clean graph can create false precision when completion signals are weak
- teams can spend more effort curating dependency state than finishing work
- the graph can pull in tracker, memory, dashboard, urgency, dispatch, or staffing expectations if the boundary is not guarded

## Misuse patterns
- treating every backlog item as a graph node even when no blocker relation matters
- using graph state as a substitute for implementation review, tests, or release checks
- hiding manual overrides or priority choices inside dependency edges
- folding knowledge links, memory semantics, reporting, notifications, or task ownership policy into the graph contract

## Detection signals
- many nodes have no clear completion condition
- blocked tasks cannot name the unmet prerequisite that keeps them closed
- the ready frontier cannot be recomputed from visible graph state
- dependency changes are made after the fact to justify a chosen next step
- reviewers argue about ranking, ownership, or schedule before the blocker truth is even clear

## Mitigations
- keep nodes small enough to review and close
- require explicit blocker edges and named blocked reasons
- recompute the ready frontier after real state changes
- keep graph authoring separate from ready-queue derivation, ranking, dispatch, memory, and project-management surfaces
- route correctness claims to implementation review and validation instead of the graph itself

## Recommendation
- move `AOA-T-0049` to `canonical` and use this note as the watch surface for graph-as-tracker drift, graph-as-memory drift, hidden-priority drift, stale-blocker drift, and proof-surface drift
