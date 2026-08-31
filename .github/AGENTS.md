# AGENTS.md

## Applies to

This card applies to `.github/` and all descendants unless a nearer
`AGENTS.md` narrows the path.

## Role

`.github/` holds GitHub-native automation, issue and pull request templates,
workflow files, CODEOWNERS, and repository platform configuration for
`aoa-techniques`.

It supports the public technique-canon contribution route. It does not author
technique meaning, mechanic law, generated truth, or release authority by
itself.

## Read before editing

Read root `AGENTS.md`, `CONTRIBUTING.md`, `docs/ROOT_SURFACE_LAW.md`, and any
workflow-local comments before changing automation or review templates.

For technique intake, also read `docs/TECHNIQUE_ATOM_CONTRACT.md`,
`docs/TECHNIQUE_TOPOLOGY_CONTRACT.md`, and the relevant GitHub issue or pull
request template.

For mechanic-facing intake, also read `mechanics/AGENTS.md` and the nearest
mechanic package card.
Read `README.md` only when the selected task needs its human map; do not preload unrelated maps.

## Boundaries

- Do not encode doctrine in GitHub files that is absent from source docs.
- Do not make CI green by weakening the guardrail being checked.
- Do not add mutation, release, or deployment behavior without an explicit
  human-visible path.
- Do not let issue templates, PR templates, CODEOWNERS, or generated template
  manifests replace authored technique, mechanic, or contribution surfaces.

## Platform sync

Keep `.github/CODEOWNERS`, `.github/PULL_REQUEST_TEMPLATE.md`, issue templates,
and workflow expectations aligned with the root route card, contribution path,
mechanics atlas, and current source-owned validation path.

The branch, PR, CI, and merge route is owned by the root `AGENTS.md` GitHub
landing workflow. This district keeps the GitHub-native files aligned with that
route.

`Repo Validation` is the growth-safe PR and moving-main gate. Release and
nightly checks live in separate workflow files and lane modes; do not make the
full release gate the default pull-request workflow.

GitHub issue and pull request templates are human-first intake surfaces.
`generated/github_review_template_manifest*.json` is derived review-template
evidence only and must be rebuilt from the authored templates, not edited as
source truth.

## Validation

Select the narrowest owner route: `source-fast` for authored or route-card work; add `generated` for projections and `release` only for release posture. See [VALIDATION.md](../VALIDATION.md); exact order is `config/validation_lanes.json`; focused procedure stays with the nearest owner. Report checks, skips, and blockers.

## Closeout

Report changed GitHub-native files, source surfaces consulted, generated files
rebuilt or not rebuilt, checks run, checks skipped, and whether the root
GitHub landing route, contribution path, CODEOWNERS map, or generated template
manifest moved.
