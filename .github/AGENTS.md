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

For mechanic-facing intake, also read `mechanics/README.md`,
`mechanics/AGENTS.md`, and the nearest mechanic package card.

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

GitHub issue and pull request templates are human-first intake surfaces.
`generated/github_review_template_manifest*.json` is derived review-template
evidence only and must be rebuilt from the authored templates, not edited as
source truth.

## Validation

Run the narrowest relevant checks first. Usual checks for this district:

```bash
python scripts/build_github_review_template_manifest.py
python scripts/validate_nested_agents.py
python scripts/validate_repo.py
```

For broad platform, contribution, generated, or release-facing changes, run:

```bash
python scripts/release_check.py
```

If a listed validator is not present in the checkout yet, report that
explicitly and run the closest available guardrail.

## Closeout

Report changed GitHub-native files, source surfaces consulted, generated files
rebuilt or not rebuilt, checks run, checks skipped, and whether the root
GitHub landing route, contribution path, CODEOWNERS map, or generated template
manifest moved.
