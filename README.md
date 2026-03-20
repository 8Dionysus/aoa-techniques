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

## Quick routes

- if you need bounded execution workflows built from techniques, go to [aoa-skills](https://github.com/8Dionysus/aoa-skills)
- if you need portable proof surfaces for quality or boundary claims, go to [aoa-evals](https://github.com/8Dionysus/aoa-evals)
- if you need the smallest next surface by task type, go to [aoa-routing](https://github.com/8Dionysus/aoa-routing)
- if you need the ecosystem layer map and federation center, go to [Agents-of-Abyss](https://github.com/8Dionysus/Agents-of-Abyss)

## Deeper routes

- for one end-to-end origin-to-public example, read `WALKTHROUGH.md`
- for generated navigation and chooser surfaces, open `docs/TECHNIQUE_SELECTION.md`, `docs/SELECTION_PATTERNS.md`, and `docs/SHADOW_PATTERNS.md`
- for runtime cards and capsule contracts, open `docs/TECHNIQUE_CAPSULES.md`, `generated/technique_capsules.json`, `generated/technique_capsules.min.json`, and `docs/TECHNIQUE_CAPSULE_GUIDE.md`
- for repo-doc routing, source-lift readers and manifests, and reusable lift guides, open `docs/REPO_DOC_SURFACES.md`, `generated/repo_doc_surface_manifest.json`, `docs/REPO_DOC_SURFACE_LIFT_GUIDE.md`, `docs/TECHNIQUE_SECTIONS.md`, `docs/TECHNIQUE_CHECKLISTS.md`, `docs/TECHNIQUE_EXAMPLES.md`, `docs/EVIDENCE_NOTE_SURFACES.md`, `generated/technique_section_manifest.json`, `generated/technique_checklist_manifest.json`, `generated/technique_example_manifest.json`, `generated/technique_evidence_note_manifest.json`, `docs/TECHNIQUE_SECTION_LIFT_GUIDE.md`, `docs/TECHNIQUE_CHECKLIST_LIFT_GUIDE.md`, `docs/TECHNIQUE_EXAMPLE_LIFT_GUIDE.md`, `docs/EVIDENCE_NOTE_PROVENANCE_GUIDE.md`, and the reusable lift family under `techniques/docs/`, including `techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md`
- for review and shadow surfaces, open `generated/shadow_review_manifest.json`, canonical `notes/adverse-effects-review.md`, `docs/PUBLISHED_SUMMARY_SHADOW_REVIEW.md`, `docs/EVALUATION_CHAIN_SHADOW_REVIEW.md`, `docs/PUBLISHED_SUMMARY_SEMANTIC_REVIEW.md`, `docs/EVALUATION_CHAIN_SEMANTIC_REVIEW.md`, `docs/DOCS_BOUNDARY_SEMANTIC_REVIEW.md`, and `docs/KAG_SOURCE_LIFT_SEMANTIC_REVIEW.md`

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
- `techniques/<domain>/<technique>/notes/` — optional evidence notes such as second-context adaptations, canonical-readiness reviews, or canonical adverse-effects reviews
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
