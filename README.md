# aoa-techniques

Public library of reusable techniques for coding agents and humans.

`aoa-techniques` is the public practice canon of AoA. It is not a snippet dump and not an “awesome list”. A technique here is a minimal reproducible unit of engineering practice: a workflow, validation pattern, safety protocol, documentation layout, evaluation loop, or transfer method that can travel cleanly across projects.

> Current release: `v0.4.1`. See [CHANGELOG](CHANGELOG.md) for release notes.

## Start here

Use the shortest route by need:

- repo-owned entrypoint: `docs/START_HERE.md`
- one full bundle end to end: `techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md`
- current technique map: `TECHNIQUE_INDEX.md`
- current direction and hardening waves: `docs/START_HERE.md` and `ROADMAP.md`
- verify current repo state: `python scripts/validate_repo.py` and `python -m unittest discover -s tests`
- release-prep parity path: `docs/RELEASING.md`, `python scripts/release_check.py`, and `git status -sb`
- deeper docs map: `docs/README.md`
- authoring template: `templates/TECHNIQUE.template.md`
- contribution path: `CONTRIBUTING.md`

## Quick routes

- repo layer position and neighboring repos: `docs/ECOSYSTEM_CONTEXT.md`
- current technique map, docs map, and generated catalog: `TECHNIQUE_INDEX.md`, `docs/README.md`, and `generated/technique_catalog.min.json`
- via negativa pruning checklist: `docs/VIA_NEGATIVA_CHECKLIST.md`
- frontmatter routing axes and kind doctrine: `docs/DOMAIN_MAP.md`, `docs/TECHNIQUE_KIND_GUIDE.md`, `docs/TECHNIQUE_KIND_HANDOFF_PACK.md`, `generated/technique_kind_manifest.min.json`, `config/technique_kind_registry.yaml`, `data/technique_kind_wave1.yaml`, `reports/wave1_kind_counts.md`, and `docs/TECHNIQUE_KINDS_SEED.md`
- feat-reader and runtime-card surfaces: `docs/TECHNIQUE_FEAT_MODEL.md`, `generated/technique_feat_cards.min.example.json`, `docs/TECHNIQUE_CAPSULES.md`, and `generated/technique_capsules.min.json`
- status, review, and promotion posture: `docs/CANONICAL_RUBRIC.md`, `docs/CANONICAL_REVIEW_GUIDE.md`, `docs/PROMOTION_READINESS_MATRIX.md`, `generated/technique_promotion_readiness.min.json`, and `docs/RELEASING.md`
- one end-to-end example path: `WALKTHROUGH.md`
- bounded execution and proof neighbors: [`aoa-skills`](https://github.com/8Dionysus/aoa-skills) and [`aoa-evals`](https://github.com/8Dionysus/aoa-evals)
- navigation and ecosystem map: [`aoa-routing`](https://github.com/8Dionysus/aoa-routing) and [`Agents-of-Abyss`](https://github.com/8Dionysus/Agents-of-Abyss)

## Deeper routes

- donor intake, refinement, and promotion: `docs/DONOR_REFINERY_RUBRIC.md`, `docs/EXTERNAL_IMPORT_RUNBOOK.md`, `docs/CROSS_LAYER_TECHNIQUE_CANDIDATES.md`, `docs/PROMOTION_READINESS_MATRIX.md`, `docs/PROMOTION_WAVE_A_RUNBOOK.md`, `docs/EXTERNAL_EVIDENCE_SPRINT_RUNBOOK.md`, and `docs/EXTERNAL_EVIDENCE_LEDGER.md`
- selection and chooser surfaces: `docs/TECHNIQUE_SELECTION_GUIDE.md`, `docs/TECHNIQUE_SELECTION.md`, and `docs/SELECTION_PATTERNS.md`
- runtime cards and capsule surfaces: `docs/TECHNIQUE_CAPSULES.md`, `generated/technique_capsules.json`, `generated/technique_capsules.min.json`, and `docs/TECHNIQUE_CAPSULE_GUIDE.md`
- repo-doc routing and authoritative doc/status manifests: `docs/REPO_DOC_SURFACES.md`, `generated/repo_doc_surface_manifest.json`, and `docs/REPO_DOC_SURFACE_LIFT_GUIDE.md`
- source-lift, KAG, and section families: `docs/KAG_EXPORT.md`, `generated/kag_export.json`, `generated/kag_export.min.json`, `docs/KAG_SOURCE_LIFT_GUIDE.md`, `docs/TECHNIQUE_SECTIONS.md`, `generated/technique_sections.full.json`, `docs/TECHNIQUE_CHECKLISTS.md`, `docs/TECHNIQUE_EXAMPLES.md`, `docs/EVIDENCE_NOTE_SURFACES.md`, `generated/technique_section_manifest.json`, `generated/technique_checklist_manifest.json`, `generated/technique_example_manifest.json`, `generated/technique_evidence_note_manifest.json`, `docs/TECHNIQUE_SECTION_LIFT_GUIDE.md`, `docs/TECHNIQUE_CHECKLIST_LIFT_GUIDE.md`, `docs/TECHNIQUE_EXAMPLE_LIFT_GUIDE.md`, and `docs/EVIDENCE_NOTE_PROVENANCE_GUIDE.md`
- review and shadow surfaces: `docs/SHADOW_PATTERNS.md`, `docs/PUBLISHED_SUMMARY_SHADOW_REVIEW.md`, `docs/EVALUATION_CHAIN_SHADOW_REVIEW.md`, `generated/shadow_review_manifest.json`, `generated/semantic_review_manifest.json`, and `docs/KAG_SOURCE_LIFT_SEMANTIC_REVIEW.md`
- public readiness lens for the published corpus: `generated/technique_promotion_readiness.min.json`
- owner-local live receipt publication for closeout/stats integration: `scripts/publish_live_receipts.py` and `.aoa/live_receipts/technique-receipts.jsonl`
- current verify and release-prep path: `python scripts/validate_repo.py`, `python -m unittest discover -s tests`, `docs/RELEASING.md`, `python scripts/release_check.py`, and `git status -sb`

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
- project-only dumps
- undocumented scripts
- objects that belong as skills, evals, routing logic, role contracts, or playbooks

## Core principles

- public-safe reusable practice over project-local residue
- bounded, reviewable contracts over vague lore
- source-linked promotion over raw copying
- linked docs and generated surfaces over oversized root inventories

## Maturity model

This repository primarily exposes public techniques in `promoted`,
`canonical`, and `deprecated` states. Earlier incubation may happen elsewhere,
but the root here should point to curated public canon rather than replaying the
full intake history.

## Repository structure

- `techniques/` for published technique bundles
- `templates/` for technique authoring and promotion scaffolds
- `generated/` for derived catalogs, capsules, source-lift, and review surfaces
- `docs/` for doctrine, intake, release, selection, and shadow surfaces
- `scripts/` and `tests/` for validation and generation helpers

## Intended users

- coding agents
- solo builders
- infra and product engineers
- teams building reusable operational knowledge

## What a good technique includes

A strong technique should include:

- clear intent and usage boundaries
- explicit inputs, outputs, and risks
- validation method
- adaptation notes when portability needs them
- enough structure to be promoted, reviewed, and reused

## Contribution model

`aoa-techniques` owns practice meaning, while neighboring repos own execution,
proof, routing, role, and scenario composition. If a reusable contract can be
extracted cleanly from a neighboring layer, it belongs here once it becomes
public-safe, bounded, and portable.

The current runtime path for public technique use remains:

`pick -> inspect -> expand -> object use`

## License

Apache-2.0
