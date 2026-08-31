# AGENTS.md

## Applies to

This card applies to `techniques/tool-use/` and every descendant unless a nearer
`AGENTS.md` narrows the path.

## Role

`tool-use/` stores technique bundles whose primary placement question is how an
agent, caller, or bounded workflow meets tools, gateways, APIs, connectors, or
tool metadata through one reviewable surface.

Current `tool-use` trunk: shared placement applies; local role and shelves are the delta.
## Current Shelves

Current shelves:

- `tool-gateway/`: one bounded MCP gateway proxy seam in front of configured
  upstream tool surfaces, with visible metadata and mediation boundaries

## Read before editing

Use shared order in [techniques/AGENTS.md](../AGENTS.md#read-before-editing); inspect `tool-use` role and its target bundle.
## Trunk Rules

Placement contract: [techniques/AGENTS.md](../AGENTS.md#closeout); local `tool-use` shelf and boundary delta follows.
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


If the object becomes a concrete executable workflow, route it to `aoa-skills`
or the owning repository. If it becomes proof authority, route it to
`aoa-evals` or a proof surface. If it becomes runtime connector ownership,
deployment, API product policy, or marketplace governance, route it away from
this trunk.

Do not widen this lane beyond its caller-facing mediation seam.

`tool-use` path placement follows the parent contract; renames need its reviewed projection and bounded receipt.
## Validation

Inherit [techniques/AGENTS.md](../AGENTS.md#validation): `source-fast`; see [VALIDATION.md](../../VALIDATION.md) and `config/validation_lanes.json`. Local `techniques/tool-use/AGENTS.md`.
## Closeout

Local delta `techniques/tool-use/AGENTS.md`: state placement/frontmatter/generated-reader changes or route-only guidance.
