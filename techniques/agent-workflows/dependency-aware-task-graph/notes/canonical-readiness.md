# Canonical Readiness

## Technique

- id: AOA-T-0049
- name: dependency-aware-task-graph

## Verdict

- bounded defer for now

## Evidence summary

- external origin: the imported technique has a bounded donor contract and explicit exclusions around memory semantics, tracker product breadth, graph-link taxonomy, and runtime specifics
- second context: `aoa-techniques` now records the same dependency-graph contract as a documentation-first landing aid with one example and one checklist
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- validation strength: the bundle now carries a checklist, an example, a clean external-origin note, and one documentation-first second context, but it still lacks a live adopter beyond the donor repository

## Default-use rationale

- this is the right promoted default when the main reusable object is an explicit dependency graph that makes blocked and ready work visible for bounded coding tasks
- it remains distinct from `AOA-T-0001`, which owns the broader change protocol rather than the dependency surface that feeds next-step selection
- it should stay narrower than full tracker, memory, dispatch, or staffing doctrine even if those features sit nearby in some donors

## Fresh public-safety check

- review date: 2026-03-27
- result: pass
- sanitization still holds: the bundle keeps only the reusable blocker-aware dependency-graph contract and excludes donor-specific tracker/runtime breadth
- public reuse check: the example, checklist, and adaptation notes remain understandable without hidden donor-repo context

## Remaining gaps

- the smallest remaining gap is still one live second context beyond the donor and documentation-first adaptation
- specifically, the bundle still needs another public workflow surface where explicit dependency edges determine ready work in practice
- the boundary from any future ready-frontier-only sibling should stay sharp so canonical review does not collapse adjacent graph techniques together

## Recommendation

- keep `AOA-T-0049` `promoted`
- defer canonical promotion until another live adopter confirms that the same bounded dependency-graph contract survives outside the donor repository
