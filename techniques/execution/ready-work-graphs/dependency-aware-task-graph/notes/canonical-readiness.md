# Canonical Readiness

## Technique

- id: AOA-T-0049
- name: dependency-aware-task-graph

## Verdict

- approve for canonical promotion

## Evidence summary

- external origin: the imported technique has a bounded donor contract and explicit exclusions around memory semantics, tracker product breadth, graph-link taxonomy, and runtime specifics
- second context: `aoa-techniques` now records the same dependency-graph contract as a documentation-first landing aid with one example and one checklist
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- Taskwarrior provides exact-fit public reinforcement: dependency edges block downstream tasks, cycles are rejected, `BLOCKED` / `BLOCKING` state is derivable, and completing a prerequisite unblocks dependent work
- validation strength: the bundle now carries a checklist, an example, a clean external-origin note, a documentation-first second context, and public live reinforcement beyond the donor repository

## Default-use rationale

- this is the right promoted default when the main reusable object is an explicit dependency graph that makes blocked and ready work visible for bounded coding tasks
- it remains distinct from `AOA-T-0001`, which owns the broader change protocol rather than the dependency surface that feeds next-step selection
- it is now the natural default when a bounded workflow needs explicit prerequisite edges and blocker-aware ready work without adopting a full tracker, memory, dispatch, or staffing doctrine

## Fresh public-safety check

- review date: 2026-05-12
- result: pass
- sanitization still holds: the bundle keeps only the reusable blocker-aware dependency-graph contract and excludes donor-specific tracker/runtime breadth
- public reuse check: the external reinforcement is from public Taskwarrior documentation, tests, and dependency implementation, not private issue trackers or hidden project boards

## Remaining gaps

- future work can add more examples for agent-specific work graphs, but no blocker remains for canonical status
- the boundary from ready-frontier-only siblings should stay sharp so canonical review does not collapse graph authoring, queue derivation, ranking, dispatch, and tracker behavior together

## Recommendation

- move `AOA-T-0049` to `canonical`
- add an adverse-effects review to preserve the caution boundary after promotion
