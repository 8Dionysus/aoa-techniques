# AGENTS.md

## Applies to

This card applies to `techniques/continuity/` and every descendant unless a nearer
`AGENTS.md` narrows the path.

## Role

`continuity/` stores technique bundles whose primary placement question is how
working context, review truth, handoff state, donor material, or capability
availability survives a state boundary.

This is a tree trunk, not a frontmatter domain. Technique bundles here may keep
their existing `domain` and `kind` values when the reviewed move is only path
architecture.

## Current Shelves

Current shelves:

- `review-compaction/`: preserves or restores review and capability context
  across commit, compaction, or repeated-review boundaries
- `handoff-continuation/`: carries handoff, receipt, verification, startup,
  resource-map, mailbox, and episode-checkpoint seams across session, agent,
  repo, or episode boundaries
- `donor-harvest/`: carries reviewed-session donor packs, harvest-packet
  contracts, progression evidence deltas, and adjunct quest overlays across
  session closeout without granting memory, playbook, or progression authority

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

Keep the continuity object explicit:

- what state crosses the boundary
- what evidence or capability must remain inspectable
- what stale, noisy, or missing context is being reduced
- what the technique refuses to reconstruct or govern

Do not turn a continuity technique into a live skill, phase system, memory
policy, or review verdict contract.

Use `docs/TECHNIQUE_TREE_CONTRACT.md` before adding another shelf here.

Do not add `tree_path` frontmatter merely because a bundle lives under this
trunk. Do not rename trunks or shelves without a reviewed projection and a
bounded migration receipt.

## Validation

After changing continuity techniques, run:

- `python scripts/validate_nested_agents.py`
- `python scripts/validate_repo.py`

Run `python scripts/release_check.py` when generated catalogs or reader
surfaces changed.

## Closeout

Report the trunk, shelf, and bundle paths changed; whether path,
frontmatter, generated catalogs, or reader surfaces changed; checks run; checks
skipped; and any remaining owner-route risk.
