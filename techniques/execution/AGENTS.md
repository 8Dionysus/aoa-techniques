# AGENTS.md

## Applies to

This card applies to `techniques/execution/` and every descendant unless a nearer
`AGENTS.md` narrows the path.

## Role

`execution/` stores technique bundles whose primary placement question is how
bounded work becomes ready, sequenced, attempted, checked, or closed without
turning into hidden orchestration or project-local runtime law.

This is a tree trunk, not a frontmatter domain. Technique bundles here may keep
their existing `domain` and `kind` values when the reviewed move is only path
architecture.

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

Read:

1. repository root `AGENTS.md`
2. `techniques/AGENTS.md`
3. `docs/TECHNIQUE_TREE_CONTRACT.md`
4. `docs/TECHNIQUE_TOPOLOGY_CONTRACT.md`
5. the target bundle `TECHNIQUE.md` and local notes/checks/examples

## Trunk Rules

Keep this card as tree route guidance for the trunk. Technique bundle meaning
stays in each `TECHNIQUE.md`; path placement alone does not change frontmatter
truth or owner authority.

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

Do not add `tree_path` frontmatter merely because a bundle lives under this
trunk. Do not rename trunks or shelves without a reviewed projection and a
bounded migration receipt.

## Validation

After changing execution techniques, run:

- `python scripts/validate_nested_agents.py`
- `python scripts/validate_repo.py`

Run `python scripts/release_check.py` when generated catalogs or reader
surfaces changed.

## Closeout

Report the trunk, shelf, and bundle paths changed; whether path,
frontmatter, generated catalogs, or reader surfaces changed; checks run; checks
skipped; and any remaining owner-route risk.
