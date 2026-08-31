# AGENTS.md

## Applies to

This card applies to `techniques/agent-workflows/` and every descendant unless a nearer
`AGENTS.md` narrows the path.

## Role

`agent-workflows/` remains the retained frontmatter review lane for many
reusable workflow techniques, but no active leaf bundle currently lives directly here after the tree pilots.

This is a retained lane, not a current tree shelf. Use it when old links,
frontmatter `domain`, or migration reviews need workflow provenance, then route
new authored leaves into the current tree through
`docs/TECHNIQUE_TREE_CONTRACT.md`.

The former `mcp-gateway-proxy` representative now lives under
`techniques/tool-use/tool-gateway/`. The former local practice lifecycle
representatives now live under
`techniques/governance/practice-adoption-lifecycle/`.

## Read before editing

Read:

1. repository root `AGENTS.md`
2. `techniques/AGENTS.md`
3. `docs/TECHNIQUE_TREE_CONTRACT.md`
4. `docs/TECHNIQUE_TOPOLOGY_CONTRACT.md`
5. the target bundle `TECHNIQUE.md` and local notes/checks/examples
Read `README.md` only when the selected task needs its human map; do not preload unrelated maps.

## Boundaries

Keep the sequence explicit. These techniques should tell a reader what happens
first, what gets checked, and how closure is reported.
Preserve explicit dry-run, diff, verify, and report stages when they are part of
the contract.
Prefer a small reversible slice over a sweeping one-shot flow.

Do not add a new leaf bundle directly under this lane unless a reviewed tree
projection proves that broad workflow placement is again the honest authored
home.

A technique belongs here when the workflow stays reusable across projects and
remains lighter than a live skill or runtime playbook.
If the object starts to encode project-specific operators, shell wrappers, or
deployment posture, route that meaning to `aoa-skills` or the owning runtime
repository instead of widening this technique.

Do not:

- hide required state behind unstated shell assumptions
- hard-code one repo's private paths or hostnames
- blur workflow technique meaning with product policy or role doctrine
- remove the verification step just to make the flow shorter

## Validation

Select the narrowest owner route: `source-fast` for authored or route-card work; add `generated` for projections and `release` only for release posture. See [VALIDATION.md](../../VALIDATION.md); exact order is `config/validation_lanes.json`; focused procedure stays with the nearest owner. Report checks, skips, and blockers.

## Closeout

Report the trunk, shelf, and bundle paths changed; whether path,
frontmatter, generated catalogs, or reader surfaces changed; checks run; checks
skipped; and any remaining owner-route risk.
