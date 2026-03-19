# aoa-techniques

Public library of reusable techniques for coding agents and humans.

`aoa-techniques` is not a snippet dump and not an “awesome list”.
It is a curated collection of **reproducible techniques**:
workflows, validation patterns, safety protocols, documentation layouts,
evaluation loops, and cross-repo transfer methods.

A technique here is a minimal reproducible unit of engineering practice.

## Start here

If you are new to this repository, follow this short path:

1. Read `TECHNIQUE_INDEX.md` to see the current technique map.
2. Open `docs/README.md` for a human-first map of the repository docs surface and recommended reading paths.
3. Open `techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md` to see one full technique end to end.
4. Use `templates/TECHNIQUE.template.md` as the starting point for authoring a new technique.
5. Follow `CONTRIBUTING.md` for the contribution and PR path.

See also: `WALKTHROUGH.md` for a short example of how one real practice became a published technique and then proved reusable in a second context.
See also: `docs/TECHNIQUE_SELECTION.md` for the generated chooser by domain, status, validation strength, and direct relation hints.
See also: `docs/SELECTION_PATTERNS.md` for the generated navigation surface built from direct relations, validator-backed navigation specs, and review-backed working sets.
See also: `docs/PUBLISHED_SUMMARY_SEMANTIC_REVIEW.md` for the first bounded semantic review pilot over a tightly related canonical cluster.
See also: `docs/EVALUATION_CHAIN_SEMANTIC_REVIEW.md` for the second bounded semantic review pilot over the upstream evaluation-chain pair.
See also: `docs/DOCS_BOUNDARY_SEMANTIC_REVIEW.md` for the third bounded semantic review pilot over the docs layout-versus-snapshot pair.

## What belongs here

Good candidates:
- agent workflows
- validation patterns
- documentation structures
- evaluation and monitoring loops
- safety and sanitization patterns
- infra operation techniques
- cross-repo promotion and reuse patterns

Bad candidates:
- random snippets
- private project hacks without adaptation notes
- secret-bearing configs
- raw logs
- undocumented scripts
- anything that only works in one private environment and was not generalized

## Core principles

- truth and reproducibility over legend
- publish techniques, not accidents
- small reversible patterns are preferred
- human meaning, agent acceleration
- public by design, sanitized by default
- origin matters
- validation matters
- adaptation notes matter

## Maturity model

This repository primarily stores techniques in these public states:

- `promoted`
- `canonical`
- `deprecated`

In this repository:

- `promoted` means reusable and public-safe, but not yet the default choice.
- `canonical` means recommended by default after reuse evidence, stronger validation, and a clear default-use rationale.
- `deprecated` means historically preserved, with a replacement or caution note when possible.

Earlier stages such as `seed` and `proven` may exist in source projects,
but only curated public techniques should live here.

## Repository structure

- `techniques/` — published technique bundles grouped by domain
- `techniques/<domain>/<technique>/notes/` — optional evidence notes such as second-context adaptations or canonical-readiness reviews
- `templates/` — templates for technique authoring and promotion
- `TECHNIQUE_INDEX.md` — repository-wide technique map
- `schemas/` — optional machine-readable schemas
- `scripts/` — repo validation helpers

## Intended users

- coding agents
- solo builders
- infra engineers
- product engineers
- AI workflow designers
- teams that want reusable operational knowledge

## What a good technique includes

A strong technique should have:
- clear intent
- usage boundaries
- inputs and outputs
- risks
- validation method
- adaptation notes
- maturity status
- origin and promotion history

## Contribution model

A technique is usually born in a real project, validated there,
sanitized, documented, and then promoted into this public repository.

In short:

`project -> validation -> sanitization -> promotion -> public canon`

## License

Apache-2.0
