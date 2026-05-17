# AGENTS.md

## Applies to

This card applies to `techniques/governance/` and every descendant unless a nearer
`AGENTS.md` narrows the path.

## Role

`governance/` stores technique bundles whose primary placement question is how
choices, approvals, control posture, or automation boundaries stay explicit
before action.

This is a tree trunk, not a frontmatter domain. Technique bundles here may keep
their existing `domain` and `kind` values when the reviewed move is only path
architecture.

## Current Shelves

Current shelves:

- `decision-routing/`: keeps owner placement, branch choices, and route-risk
  posture visible as local decision support before action
- `approval-evidence/`: keeps approval-shaped boundary evidence visible before
  mutation or continuation, while preserving the difference between one
  fail-closed gate and one durable approval seam
- `automation-readiness/`: keeps automation-fit, first honest landing, and
  approval-sensitivity posture visible before a route is treated as
  automation-ready
- `promotion-boundary/`: keeps final promotion verdict, nearest-wrong-target
  rejection, and skill-proposal handoff posture visible before a reusable unit
  is authored in another owner surface
- `practice-adoption-lifecycle/`: keeps local adoption, retention, and
  obsolescence posture visible before a practice becomes durable, stays active,
  or routes toward owner review

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

Keep the governance object explicit:

- what choice or control boundary is being made visible
- what evidence or route object the technique starts from
- what authority the output does and does not claim
- what stop condition prevents advisory structure from becoming policy

Do not turn a governance technique into AoA constitutional authority,
`aoa-routing` ownership, role contract law, runtime dispatch, approval policy,
playbook design, security framework authority, scheduler doctrine, queue
ownership, broad orchestration governance, hidden automation governance, skill
acceptance, skill activation, proof verdict authority, memory truth, or
Method-growth law.

Use `docs/TECHNIQUE_TREE_CONTRACT.md` before adding another shelf here.

Do not add `tree_path` frontmatter merely because a bundle lives under this
trunk. Do not rename trunks or shelves without a reviewed projection and a
bounded migration receipt.

## Validation

After changing governance techniques, run:

- `python scripts/validate_nested_agents.py`
- `python scripts/validate_repo.py`

Run `python scripts/release_check.py` when generated catalogs or reader
surfaces changed.

## Closeout

Report the trunk, shelf, and bundle paths changed; whether path,
frontmatter, generated catalogs, or reader surfaces changed; checks run; checks
skipped; and any remaining owner-route risk.
