# AGENTS.md

## Applies to

This card applies to `techniques/execution/` and every descendant unless a nearer
`AGENTS.md` narrows the path.

## Role

`execution/` stores technique bundles whose primary placement question is how
bounded work becomes ready, sequenced, attempted, checked, or closed without
turning into hidden orchestration or project-local runtime law.

Current `execution` trunk: shared placement applies; local role and shelves are the delta.
## Current Shelves

Current shelves:

- `ready-work-graphs/`: dependency graph authoring, blocker-free ready frontier
  derivation, and requirement-to-design-to-task layering that make the next
  bounded work slice visible before execution.
- `intent-chain/`: artifact-first intent normalization, dry-run contract
  checking, and one-new-intent rollout discipline before any real action path
  is trusted.
- `agent-workflows-core/`: visible, bounded, reviewable agent-work backbone,
  bounded implementation slices, stateless single-shot fast paths, explicit
  confirmation seams, and shell-composable one-shot invocation.
- `runtime-truth-lifecycle/`: pre-start rendered runtime truth, one-command
  local service lifecycle, selector-aware host readiness, and baseline-first
  additive profile comparison without becoming runtime owner law.

## Read before editing

Use shared order in [techniques/AGENTS.md](../AGENTS.md#read-before-editing); inspect `execution` role and its target bundle.
## Trunk Rules

Placement contract: [techniques/AGENTS.md](../AGENTS.md#closeout); local `execution` shelf and boundary delta follows.
## Boundaries

Keep execution-facing techniques narrow and explicit:

- what input state makes work ready
- what the technique prepares, chooses, performs, or closes
- what later validation, proof, dispatch, scheduling, runtime, or owner-policy
  surface remains outside the bundle

Do not turn an execution technique into project-management doctrine, staffing
policy, backlog governance, generic agent doctrine, shell policy, product
policy, approval policy, autonomous orchestration, hidden agent scheduling,
runtime lifecycle law, deployment ownership, monitoring platform doctrine, host
policy, smoke-test law, benchmark-suite governance, product scoring, proof
authority, `aoa-evals` verdict authority, router ownership, API contract
authority, real-action permission, automation governance, CI policy, or a broad
methodology stack.

Use `docs/TECHNIQUE_TREE_CONTRACT.md` before adding another shelf here.

`execution` path placement follows the parent contract; renames need its reviewed projection and bounded receipt.
## Validation

Inherit [techniques/AGENTS.md](../AGENTS.md#validation): `source-fast`; see [VALIDATION.md](../../VALIDATION.md) and `config/validation_lanes.json`. Local `techniques/execution/AGENTS.md`.
## Closeout

Local delta `techniques/execution/AGENTS.md`: state placement/frontmatter/generated-reader changes or route-only guidance.
