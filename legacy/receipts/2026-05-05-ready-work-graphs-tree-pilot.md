# Ready-Work-Graphs Tree Pilot Receipt

Date: 2026-05-05

## Status

Landed.

## Scope

This receipt preserves the sixteenth authored path migration for the technique
tree pilot.

Reviewed packet:
`mechanics/distillation/parts/technique-reform-ingress/reviews/ready-work-graphs-direct-read-migration-review.md`

Tree contract:
`docs/TECHNIQUE_TREE_CONTRACT.md`

## Moves

| Technique | Old path | New path |
|---|---|---|
| `AOA-T-0049` | `techniques/agent-workflows/dependency-aware-task-graph/` | `techniques/execution/ready-work-graphs/dependency-aware-task-graph/` |
| `AOA-T-0050` | `techniques/agent-workflows/ready-work-from-blocker-graph/` | `techniques/execution/ready-work-graphs/ready-work-from-blocker-graph/` |
| `AOA-T-0055` | `techniques/agent-workflows/requirements-design-tasks-ladder/` | `techniques/execution/ready-work-graphs/requirements-design-tasks-ladder/` |

## Preservation Rule

Active technique bundles moved directly from old authored homes to new authored
homes. They did not pass through root `legacy/`.

Root legacy preserves only this migration accounting.

## Invariants

- Keep bundle IDs unchanged.
- Keep `domain`, `kind`, `status`, owners, evidence, relations, checklists,
  examples, notes, maturity, validation-strength metadata, and public-safety
  posture unchanged.
- Preserve all three bundles as `domain: agent-workflows` and
  `kind: workflow`.
- Preserve `AOA-T-0055` as a readiness ladder, not a graph database,
  methodology import, or execution workflow.
- Do not add `tree_path` frontmatter.
- Do not move any other shelf in this wave.
- Keep dependency graph authoring, ready-frontier derivation, and
  requirement/design/task layering as three separate leaf bundles under one
  execution shelf.
- Do not treat `ready-work-graphs` as project-management doctrine,
  scheduling, staffing, dispatch policy, backlog governance, graph database
  doctrine, memory substrate, hidden orchestration, proof of readiness,
  execution validation, or neighboring execution shelf authority.
- Keep authored technique bundles stronger than generated catalogs, capsules,
  manifests, reports, or reader surfaces.

## Validation

- the release lane passed after rebuilding generated surfaces,
  running the full unittest suite, validating nested `AGENTS.md` coverage, and
  validating repository parity.
