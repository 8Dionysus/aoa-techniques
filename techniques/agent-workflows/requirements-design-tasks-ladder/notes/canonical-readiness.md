# Canonical Readiness

## Technique
- id: AOA-T-0055
- name: requirements-design-tasks-ladder

## Verdict
- bounded defer for now

## Evidence summary
- external origin: the imported technique has a bounded donor contract and explicit exclusions around command suites, template ecosystems, steering, project memory, validation commands, and methodology doctrine
- second context: `aoa-techniques` now records the same requirement -> design -> task ladder as a documentation-first adaptation with one example and one checklist
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- validation strength: the bundle now carries one checklist, one example, a clean external-origin note, and one documentation-first second context, but it still lacks a live adopter beyond the donor methodology family

## Default-use rationale
- this is the right promoted default when the main problem is keeping requirement, design, and task layers visibly distinct before execution starts
- it remains narrower than [AOA-T-0001](../../plan-diff-apply-verify-report/TECHNIQUE.md) because it stops before apply, verify, and report
- it also remains narrower than [AOA-T-0049](../../dependency-aware-task-graph/TECHNIQUE.md) because it derives tasks from design without taking on task dependency coordination

## Fresh public-safety check
- review date: 2026-03-28
- result: pass
- sanitization still holds: the bundle keeps only the reusable three-layer ladder and excludes donor-specific commands, templates, project-memory surfaces, and wider methodology packaging
- public reuse check: the example, checklist, and adaptation notes remain understandable without hidden donor-repo context

## Remaining gaps
- the smallest remaining gap is still one live second context beyond the donor and documentation-first adaptation
- specifically, the bundle still needs another public workflow surface that treats requirement -> design -> task separation as a reusable object without widening into a full methodology stack

## Recommendation
- keep `AOA-T-0055` `promoted`
- defer canonical promotion until another live adopter confirms that the requirements-design-tasks ladder survives outside the donor methodology family
