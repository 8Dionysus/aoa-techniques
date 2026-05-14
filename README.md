# aoa-techniques

Public library of reusable techniques for coding agents and humans.

`aoa-techniques` is the public practice canon of AoA. It is not a snippet dump
and not an "awesome list". A technique here is one atomic executable move: a
small, reproducible unit of engineering practice that can be classified,
templated, verified, and handed to a small agent after orchestration supplies
the right context.

The repository has a dual posture:

- standalone public library: a builder can reuse one technique, capsule, or
  bundle without deploying OS Abyss or the whole AoA ecosystem
- AoA organ: the same authored techniques keep stable IDs, topology,
  provenance, review posture, mechanics, and generated companions for sibling
  repos to consume

AoA references may explain provenance, owner law, or neighboring
responsibilities. They should not make the core technique unusable for an
external reader who only wants the bounded practice.

> Current release: `v0.4.2`. See [CHANGELOG](CHANGELOG.md) for release notes.

## Start Here

Use the shortest route by need:

| Need | Open |
|---|---|
| first public route | `docs/START_HERE.md` |
| repo boundary | `CHARTER.md` |
| ecosystem placement | `docs/ECOSYSTEM_CONTEXT.md` |
| one concrete bundle | `techniques/execution/agent-workflows-core/plan-diff-apply-verify-report/TECHNIQUE.md` |
| current technique map | `TECHNIQUE_INDEX.md` |
| authoring contract | `docs/TECHNIQUE_ATOM_CONTRACT.md` |
| classification and kind guidance | `docs/TECHNIQUE_TOPOLOGY_CONTRACT.md`, `docs/TECHNIQUE_KIND_GUIDE.md`, `docs/TECHNIQUE_KIND_HANDOFF_PACK.md` |
| corpus tree contract | `docs/TECHNIQUE_TREE_CONTRACT.md` |
| compact runtime cards | `docs/TECHNIQUE_CAPSULES.md` |
| root placement law | `docs/ROOT_SURFACE_LAW.md` |
| full docs map | `docs/README.md`, `docs/REPO_DOC_SURFACES.md`, `generated/repo_doc_surface_manifest.json`, `docs/REPO_DOC_SURFACE_LIFT_GUIDE.md` |
| current direction | `ROADMAP.md` |
| durable obligations | `QUESTBOOK.md` |
| contribution path | `CONTRIBUTING.md` |

Deep mechanic runbooks, review packets, ledgers, scout reports, generated
readers, and shadow or semantic review artifacts are intentionally not
re-indexed here. Start from the docs map or the owning `mechanics/<slug>/`
route when you need that detail.

## Root Surfaces

| Surface | Role |
|---|---|
| `README.md` | public front door and route chooser |
| `CHARTER.md` | authority boundary for the practice canon |
| `DESIGN.md` | system form of the practice canon |
| `DESIGN.AGENTS.md` | agent-facing surface design |
| `AGENTS.md` | local agent route card and validation posture |
| `TECHNIQUE_INDEX.md` | public corpus map by ID, status, domain, kind, and path |
| `ROADMAP.md` | repo-level direction and horizons |
| `QUESTBOOK.md` | durable obligations and parked work |
| `CHANGELOG.md` | release history |
| `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md` | public contribution, security, and conduct surfaces |
| `WALKTHROUGH.md` | one thin end-to-end example |

Root surfaces route to stronger owners. They do not absorb mechanic-local
operating detail, generated truth, sibling-repo implementation truth, or raw
history.

## What Belongs Here

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
- objects that belong as skills, evals, routing logic, role contracts,
  playbooks, memory objects, or runtime behavior

## Repository Shape

- `techniques/` for published technique bundles
- `templates/` for technique authoring and promotion scaffolds
- `docs/` for orientation, contracts, review doctrine, release, selection, and
  generated-reader interpretation
- `generated/` for reproducible catalogs, capsules, source-lift, and review
  companions
- `mechanics/` for AoA cross-mechanic movement surfaces around technique canon
- `legacy/` for public-safe repo-wide provenance, archive, and migration
  receipts after active distillation
- `.agents/` for agent-facing companion lanes and local route support
- `scripts/` for repo-wide builders and validators
- `tests/` for repo-wide validation; mechanic-owned checks live under
  `mechanics/**/tests/` or the owning part

## Validation

Use the narrowest check that matches the change. The common repo checks are:

```bash
python scripts/validate_repo.py
python scripts/run_tests.py
python scripts/release_check.py
git status -sb
```

When source docs feed generated companions, rebuild the matching generated
surface before validating.

## License

Apache-2.0
