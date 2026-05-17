# Canonical Readiness

## Technique

- id: AOA-T-0055
- name: requirements-design-tasks-ladder

## Verdict

- approve for canonical promotion

## Evidence summary

- external origin: the imported technique has a bounded donor contract and explicit exclusions around command suites, template ecosystems, steering, project memory, validation commands, and methodology doctrine
- second context: `aoa-techniques` records the same requirement -> design -> task ladder as a documentation-first adaptation with one example and one checklist
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- SpecForge-Agent provides exact-fit public reinforcement: a `PlanAgent` creates `requirements.md`, a `DesignAgent` creates `design.md` from approved requirements, a `TasksAgent` reads both design and requirements before writing `tasks.md`, and end-to-end tests check the three artifacts before implementation
- GitHub Spec Kit provides supporting boundary evidence through its visible `spec.md` -> `plan.md` -> `tasks.md` spine, but its broader SDD command suite, constitution gates, hooks, research documents, and implementation flow remain excluded
- validation strength: the bundle now carries a checklist, an example, a clean external-origin note, a documentation-first second context, and public live reinforcement beyond the donor repository

## Default-use rationale

- this is the right canonical default when the main problem is preserving a visible planning ladder before implementation starts
- it remains narrower than [AOA-T-0001](../../../agent-workflows-core/plan-diff-apply-verify-report/TECHNIQUE.md) because it stops before apply, verify, and report
- it remains narrower than [AOA-T-0049](../../dependency-aware-task-graph/TECHNIQUE.md) and [AOA-T-0050](../ready-work-from-blocker-graph/TECHNIQUE.md) because it does not author blocker graphs, compute ready frontiers, rank work, or coordinate execution
- it is now the natural default when a bounded workflow needs requirements, design, and tasks to remain distinct and traceable without adopting a full SDD, agent-platform, approval, or implementation framework

## Fresh public-safety check

- review date: 2026-05-12
- result: pass
- sanitization still holds: the bundle keeps only the reusable three-layer ladder and excludes donor-specific commands, templates, project-memory surfaces, and wider methodology packaging
- public reuse check: the external reinforcement comes from public MIT-licensed repositories and visible documentation, source code, and e2e tests rather than private project artifacts or hidden workflow state

## Remaining gaps

- future work can add examples from non-agent planning practices, but no blocker remains for canonical status
- the boundary from methodology, approval flow, task execution, memory, command suites, and task-graph siblings should stay explicit so canonical review does not collapse the ladder into a larger workflow stack

## Recommendation

- move `AOA-T-0055` to `canonical`
- add an adverse-effects review to preserve the caution boundary after promotion
