# AGENTS.md

## Applies to

This card applies to `techniques/tool-use/` and every descendant unless a nearer
`AGENTS.md` narrows the path.

## Role

`tool-use/` stores technique bundles whose primary placement question is how an
agent, caller, or bounded workflow meets tools, gateways, APIs, connectors, or
tool metadata through one reviewable surface.

This is a tree trunk, not a frontmatter domain. Technique bundles here may keep
their existing `domain` and `kind` values when the reviewed move is only path
architecture.

## Current Shelves

Current shelves:

- `tool-gateway/`: one bounded MCP gateway proxy seam in front of configured
  upstream tool surfaces, with visible metadata and mediation boundaries

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

Keep the tool-use object small and inspectable:

- name the caller-facing surface
- name what metadata, capability shape, or mediation boundary is visible
- keep runtime lifecycle, registry publication, marketplace curation, trust
  scoring, and security-scanner breadth outside the technique unless they are
  truly subordinate to the one tool-use move
- preserve the difference between a portable technique and an owning runtime,
  skill, connector, or product surface

Use `docs/TECHNIQUE_TREE_CONTRACT.md` before adding another shelf here.

Do not add `tree_path` frontmatter merely because a bundle lives under this
trunk. Do not rename trunks or shelves without a reviewed projection and a
bounded migration receipt.

If the object becomes a concrete executable workflow, route it to `aoa-skills`
or the owning repository. If it becomes proof authority, route it to
`aoa-evals` or a proof surface. If it becomes runtime connector ownership,
deployment, API product policy, or marketplace governance, route it away from
this trunk.

## Validation

After changing tool-use techniques, run:

- `python scripts/validate_nested_agents.py`
- `python scripts/validate_repo.py`

Run `python scripts/release_check.py` when generated catalogs or reader
surfaces changed.

## Closeout

Report the trunk, shelf, and bundle paths changed; whether path,
frontmatter, generated catalogs, or reader surfaces changed; checks run; checks
skipped; and any remaining owner-route risk.
