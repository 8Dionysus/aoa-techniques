# AGENTS.md

Guidance for coding agents and humans working under `techniques/governance/`.

## Purpose

`governance/` stores technique bundles whose primary placement question is how
choices, approvals, control posture, or automation boundaries stay explicit
before action.

This is a tree trunk, not a frontmatter domain. Technique bundles here may keep
their existing `domain` and `kind` values when the reviewed move is only path
architecture.

## Current scope

Accepted pilot shelves:

- `decision-routing/`: keeps owner placement, branch choices, and route-risk
  posture visible as local decision support before action

## Domain rules

Keep the governance object explicit:

- what choice or control boundary is being made visible
- what evidence or route object the technique starts from
- what authority the output does and does not claim
- what stop condition prevents advisory structure from becoming policy

Do not turn a governance technique into AoA constitutional authority,
`aoa-routing` ownership, role contract law, runtime dispatch, approval policy,
playbook design, or hidden automation governance.

## Boundary

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
