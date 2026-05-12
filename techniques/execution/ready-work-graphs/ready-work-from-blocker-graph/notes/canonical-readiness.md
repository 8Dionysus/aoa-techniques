# Canonical Readiness

## Technique

- id: AOA-T-0050
- name: ready-work-from-blocker-graph

## Verdict

- approve for canonical promotion

## Evidence summary

- external origin: the imported technique has a bounded donor contract and explicit exclusions around tracker product breadth, graph authoring, ranking doctrine, and runtime specifics
- second context: `aoa-techniques` now records the same ready-frontier contract as a documentation-first landing aid with one example and one checklist
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- Taskwarrior provides exact-fit public reinforcement: blocked and blocking tasks are reportable, unblocked tasks can be surfaced separately, and completing a prerequisite removes `BLOCKED` state from downstream work
- validation strength: the bundle now carries a checklist, an example, a clean external-origin note, a documentation-first second context, and public live reinforcement beyond the donor repository

## Default-use rationale

- this is the right promoted default when the main reusable object is blocker-aware next-work derivation over an existing dependency graph
- it remains distinct from `AOA-T-0049`, which owns the graph as the working surface rather than the derived ready frontier
- it is now the natural default when a workflow needs the next work queue to come from blocker-free state before any secondary prioritization, ranking, staffing, or broader tracker behavior

## Fresh public-safety check

- review date: 2026-05-12
- result: pass
- sanitization still holds: the bundle keeps only the reusable blocker-aware ready-frontier contract and excludes donor-specific tracker/runtime breadth
- public reuse check: the external reinforcement is from public Taskwarrior documentation and tests, not private queues, hidden boards, or local project state

## Remaining gaps

- future work can add examples for agent-specific next-work frontiers, but no blocker remains for canonical status
- the boundary from `AOA-T-0049` should stay explicit so canonical review does not collapse graph authoring, queue derivation, ranking, dispatch, and tracker behavior together

## Recommendation

- move `AOA-T-0050` to `canonical`
- add an adverse-effects review to preserve the caution boundary after promotion
