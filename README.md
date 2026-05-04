# aoa-techniques

Public library of reusable techniques for coding agents and humans.

`aoa-techniques` is the public practice canon of AoA. It is not a snippet dump
and not an "awesome list". A technique here is an atomic executable move: one
minimal reproducible unit of engineering practice that can be classified,
templated, verified, and handed to a small agent after orchestration supplies the
right context.

This repo has a dual posture:

- standalone public library: a builder should be able to take one technique,
  capsule, or bundle into their own agent system without deploying OS Abyss or
  the whole AoA ecosystem
- AoA organ: inside OS Abyss, the same authored techniques keep stable IDs,
  topology, provenance, review posture, mechanics, and generated surfaces for
  sibling repos to consume

AoA references are allowed to explain provenance, owner law, or neighboring
responsibilities. They should not make the core technique unusable for an
external reader who only wants the bounded practice.

> Current release: `v0.4.2`. See [CHANGELOG](CHANGELOG.md) for release notes.

## What this repo does

| Function | Surface |
|---|---|
| Names the practice-canon boundary | [CHARTER](CHARTER.md) |
| Opens the shortest public route | [Start Here](docs/START_HERE.md) |
| Defines what counts as one technique | [Technique Atom Contract](docs/TECHNIQUE_ATOM_CONTRACT.md) |
| Defines the classification topology | [Technique Topology Contract](docs/TECHNIQUE_TOPOLOGY_CONTRACT.md) |
| Defines the scalable corpus tree shape | [Technique Tree Contract](docs/TECHNIQUE_TREE_CONTRACT.md) |
| Maps the public corpus | [TECHNIQUE_INDEX](TECHNIQUE_INDEX.md) |
| Keeps root and docs placement legible | [Root Surface Law](docs/ROOT_SURFACE_LAW.md) |
| Preserves repo-wide provenance after active distillation | [Root Legacy](legacy/README.md) |
| Holds repo-level direction without becoming an audit ledger | [ROADMAP](ROADMAP.md) |
| Tracks durable canon obligations | [QUESTBOOK](QUESTBOOK.md) |

This repository is strongest when it keeps reusable practice small, portable,
and well-classified. It is weakest when it tries to become the skill, proof,
routing, memory, playbook, or runtime layer.

## Start here

Use the shortest route by need:

- repo-owned entrypoint: `docs/START_HERE.md`
- authority boundary: `CHARTER.md`
- atomic technique contract: `docs/TECHNIQUE_ATOM_CONTRACT.md`
- classification topology contract: `docs/TECHNIQUE_TOPOLOGY_CONTRACT.md`
- scalable corpus tree contract: `docs/TECHNIQUE_TREE_CONTRACT.md`
- root and docs placement law: `docs/ROOT_SURFACE_LAW.md`
- repo-wide provenance, archives, and migration receipts: `legacy/README.md`
- one full bundle end to end: `techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md`
- current technique map: `TECHNIQUE_INDEX.md`
- current direction: `ROADMAP.md`
- durable obligations: `QUESTBOOK.md`
- AoA cross-mechanics for technique movement: `mechanics/README.md`
- verify current repo state: `python scripts/validate_repo.py` and `python -m unittest discover -s tests`
- release-prep parity path: `docs/RELEASING.md`, `python scripts/release_check.py`, and `git status -sb`
- deeper docs map: `docs/README.md`
- authoring template: `templates/TECHNIQUE.template.md`
- contribution path: `CONTRIBUTING.md`

## Quick routes

- repo authority, layer position, and neighboring repos: `CHARTER.md` and `docs/ECOSYSTEM_CONTEXT.md`
- current technique map, docs map, and generated catalog: `TECHNIQUE_INDEX.md`, `docs/README.md`, and `generated/technique_catalog.min.json`
- via negativa pruning checklist: `docs/VIA_NEGATIVA_CHECKLIST.md`
- frontmatter routing axes, topology, tree architecture, and kind doctrine: `docs/TECHNIQUE_TOPOLOGY_CONTRACT.md`, `docs/TECHNIQUE_TREE_CONTRACT.md`, `docs/DOMAIN_MAP.md`, `docs/TECHNIQUE_KIND_GUIDE.md`, `docs/TECHNIQUE_KIND_HANDOFF_PACK.md`, `generated/technique_kind_manifest.min.json`, `config/technique_kind_registry.yaml`, `config/technique_family_seed.yaml`, `config/technique_topology_axes.yaml`, `data/technique_kind_wave1.yaml`, `reports/technique_family_scout.md`, `reports/technique_topology_scout.md`, `reports/wave1_kind_counts.md`, and `docs/TECHNIQUE_KINDS_SEED.md`
- atomicity and small-agent authoring contract: `docs/TECHNIQUE_ATOM_CONTRACT.md`
- feat-reader and runtime-card surfaces: `mechanics/growth-cycle/parts/technique-feat-model/README.md`, `generated/technique_feat_cards.min.example.json`, `docs/TECHNIQUE_CAPSULES.md`, and `generated/technique_capsules.min.json`
- status, review, and promotion posture: `docs/CANONICAL_RUBRIC.md`, `docs/CANONICAL_REVIEW_GUIDE.md`, `mechanics/audit/parts/promotion-readiness-matrix/README.md`, `generated/technique_promotion_readiness.min.json`, and `docs/RELEASING.md`
- Agon practice-candidate bridge: `mechanics/agon/parts/move-technique-bridge/README.md`, `mechanics/agon/LANDING_LOG.md`, `mechanics/agon/PROVENANCE.md`, `mechanics/agon/parts/move-technique-bridge/generated/agon_technique_binding_candidates.min.json`, `python mechanics/agon/parts/move-technique-bridge/scripts/build_agon_technique_binding_candidates.py --check`, `python mechanics/agon/parts/move-technique-bridge/scripts/validate_agon_technique_binding_candidates.py`, and `python -m pytest -q mechanics/agon/parts/move-technique-bridge/tests/test_agon_technique_binding_candidates.py`
- one end-to-end example path: `WALKTHROUGH.md`
- bounded execution and proof neighbors: [`aoa-skills`](https://github.com/8Dionysus/aoa-skills) and [`aoa-evals`](https://github.com/8Dionysus/aoa-evals)
- navigation and ecosystem map: [`aoa-routing`](https://github.com/8Dionysus/aoa-routing) and [`Agents-of-Abyss`](https://github.com/8Dionysus/Agents-of-Abyss)

## Deeper routes

- donor intake, refinement, and promotion: `mechanics/distillation/parts/donor-refinery/README.md`, `mechanics/distillation/parts/external-import-runbook/README.md`, `mechanics/distillation/parts/cross-layer-candidate-ledger/README.md`, `mechanics/audit/parts/promotion-readiness-matrix/README.md`, `mechanics/audit/parts/promotion-wave-a-runbook/README.md`, `mechanics/audit/parts/external-evidence-sprint-runbook/README.md`, and `mechanics/audit/parts/external-evidence-ledger/README.md`
- Agon owner-binding companion surfaces: `mechanics/agon/parts/move-technique-bridge/README.md`, `mechanics/agon/PARTS.md`, `mechanics/agon/PROVENANCE.md`, `mechanics/agon/parts/move-technique-bridge/config/agon_technique_binding_candidates.seed.json`, and `mechanics/agon/parts/move-technique-bridge/generated/agon_technique_binding_candidates.min.json`
- selection and chooser surfaces: `docs/TECHNIQUE_SELECTION_GUIDE.md`, `docs/TECHNIQUE_SELECTION.md`, and `docs/SELECTION_PATTERNS.md`
- runtime cards and capsule surfaces: `docs/TECHNIQUE_CAPSULES.md`, `generated/technique_capsules.json`, `generated/technique_capsules.min.json`, and `docs/TECHNIQUE_CAPSULE_GUIDE.md`
- root placement, root legacy, repo-doc routing, and authoritative doc/status manifests: `docs/ROOT_SURFACE_LAW.md`, `legacy/README.md`, `docs/REPO_DOC_SURFACES.md`, `generated/repo_doc_surface_manifest.json`, and `docs/REPO_DOC_SURFACE_LIFT_GUIDE.md`
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

- standalone portability without requiring a full OS Abyss deployment
- AoA organ fidelity without hiding local dependencies inside portable practice
- public-safe reusable practice over project-local residue
- atomic executable moves over chains disguised as techniques
- deliberate tree architecture plus faceted topology over overloaded buckets
- source-of-truth separation over root-file sprawl
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
- `legacy/` for public-safe repo-wide provenance, archive, and migration receipts
- `mechanics/` for AoA cross-mechanic movement surfaces around technique canon
- `docs/` for orientation, review doctrine, release, selection, generated-reader interpretation, and shadow surfaces
- `scripts/` and `tests/` for validation and generation helpers

## Intended users

- coding agents
- solo builders
- infra and product engineers
- teams building reusable operational knowledge

## What a good technique includes

A strong technique should include:

- clear intent and usage boundaries
- one atomic move that can be executed from a compact runtime card
- topology fit across `domain`, `kind`, and any reviewed future axes
- explicit inputs, outputs, and risks
- validation method
- adaptation notes when portability needs them
- enough structure to be promoted, reviewed, and reused

## Contribution model

`aoa-techniques` owns practice meaning, while neighboring repos own execution,
proof, routing, role, and scenario composition. If one atomic reusable contract
can be extracted cleanly from a neighboring layer, it belongs here once it
becomes public-safe, bounded, and portable.

The current runtime path for public technique use remains:

`pick -> inspect -> expand -> object use`

## License

Apache-2.0
