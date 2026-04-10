# Repo Doc Surfaces

This file is generated from the authoritative public docs/status layer only.
Do not edit it by hand; run `python scripts/build_repo_doc_surface_manifest.py`.

Use this surface when the main question is which public repo doc to open next for orientation, contribution rules, public-safety expectations, or release/status context.

It stays bounded to the current authored docs/status source set. It excludes local planning files such as `TODO.md`, `PLANS.md`, and `ROADMAP.md`, plus deeper guide/review docs that belong to later waves.

See also:
- [Start Here](START_HERE.md)
- [Repo Doc Surface Lift Guide](REPO_DOC_SURFACE_LIFT_GUIDE.md)
- [Full repo doc surface manifest](../generated/repo_doc_surface_manifest.json)
- [Documentation Map](README.md)
- [KAG Source Lift Guide](KAG_SOURCE_LIFT_GUIDE.md)

## Quick Navigation

| question | open | why |
|---|---|---|
| Where should I start if I am new to the repository? | [aoa-techniques](../README.md) (`README.md`), [Start Here](START_HERE.md) (`docs/START_HERE.md`), [TECHNIQUE_INDEX](../TECHNIQUE_INDEX.md) (`TECHNIQUE_INDEX.md`) | Start with the root README, then use Start Here and the technique index for bounded navigation. |
| Where is the repo-only self-serve route before deeper guides split out? | [Start Here](START_HERE.md) (`docs/START_HERE.md`), [Documentation Map](README.md) (`docs/README.md`) | Use Start Here for the shortest repo-owned route, then open the docs map only when you need the deeper guide and generated-surface tree. |
| Where is this repository positioned inside the AoA layer map? | [Ecosystem Context](ECOSYSTEM_CONTEXT.md) (`docs/ECOSYSTEM_CONTEXT.md`), [Start Here](START_HERE.md) (`docs/START_HERE.md`) | Use Ecosystem Context for the repo-owned layer-position note, then Start Here when you want the shortest bounded route through the rest of the public surface. |
| Where do contribution rules and PR boundaries live? | [Contributing to aoa-techniques](../CONTRIBUTING.md) (`CONTRIBUTING.md`), [AGENTS.md](../AGENTS.md) (`AGENTS.md`) | Use CONTRIBUTING for the public PR path and AGENTS for the repo's public-safe PLAN -> DIFF -> VERIFY -> REPORT doctrine. |
| Where do public-safety expectations and contributor conduct live? | [SECURITY.md](../SECURITY.md) (`SECURITY.md`), [AGENTS.md](../AGENTS.md) (`AGENTS.md`), [Code of Conduct](../CODE_OF_CONDUCT.md) (`CODE_OF_CONDUCT.md`) | Use SECURITY for disclosure and hygiene, AGENTS for public-repo authoring discipline, and the Code of Conduct for collaboration expectations. |
| Where do release flow and status history live? | [Changelog](../CHANGELOG.md) (`CHANGELOG.md`), [Releasing `aoa-techniques`](RELEASING.md) (`docs/RELEASING.md`) | Use CHANGELOG for current history and RELEASING for the bounded validation path behind public corpus updates. |

## Entrypoint / Map

Open these first when the question is where to start or which public repo map or self-serve entrypoint should anchor the next read.

| doc | bounded role | top-level sections |
|---|---|---|
| [aoa-techniques](../README.md) (`README.md`) | root entrypoint for repository purpose, scope, and first-read routing | `Start here`, `Quick routes`, `Deeper routes`, `What belongs here`, `Core principles`, `Maturity model`, `Repository structure`, `Intended users`, `What a good technique includes`, `Contribution model`, `License` |
| [Start Here](START_HERE.md) (`docs/START_HERE.md`) | repo-owned self-serve entrypoint for route selection, corpus posture, and stay-here versus leave-here decisions | `What This Repo Is`, `If You Need One Technique Now`, `If You Need To Understand Maturity And Review`, `If You Need Derived Surfaces`, `Current Corpus Posture`, `Repo-Only Operating Contract`, `When To Leave This Repo`, `Release And Validation` |
| [Ecosystem Context](ECOSYSTEM_CONTEXT.md) (`docs/ECOSYSTEM_CONTEXT.md`) | repo-owned positioning note for the AoA ontology spine, neighboring layer boundaries, and why scenario-level method stays in aoa-playbooks | `Why This Repo Exists`, `Ontology Spine Inheritance`, `Method And Neighboring Layers`, `Boundary Reminder` |
| [TECHNIQUE_INDEX](../TECHNIQUE_INDEX.md) (`TECHNIQUE_INDEX.md`) | public corpus map by status, technique id, and domain | `Canonical techniques`, `Promoted techniques`, `Deprecated techniques`, `Notes` |
| [Documentation Map](README.md) (`docs/README.md`) | docs-layer map for deeper guides, generated surfaces, and recommended reading paths after the main entrypoint | `Start Here`, `Surface Types`, `Recommended Reading Paths`, `Companion Repository Surfaces`, `Notes` |

## Contribution / Policy

Use these when the question is how to contribute safely, publicly, and within the repo's current review posture.

| doc | bounded role | top-level sections |
|---|---|---|
| [AGENTS.md](../AGENTS.md) (`AGENTS.md`) | contributor doctrine for public-safe planning, focused diffs, verification, and reporting | `Purpose`, `Owns`, `Does not own`, `Core rules`, `Growth posture`, `Read this first`, `Primary objects`, `Hard NO`, `Contribution doctrine`, `Validation` |
| [Contributing to aoa-techniques](../CONTRIBUTING.md) (`CONTRIBUTING.md`) | public contribution path, review criteria, and status-transition rules | `What belongs here`, `Before opening a PR`, `External provenance`, `GitHub intake surfaces`, `Preferred PR scope`, `Recommended PR title format`, `Review criteria`, `Status transitions`, `Security` |
| [SECURITY.md](../SECURITY.md) (`SECURITY.md`) | private reporting route and public-hygiene security expectations | `Purpose`, `Report privately if you find`, `Do not post publicly`, `Security expectations for contributors`, `Public hygiene checklist` |
| [Code of Conduct](../CODE_OF_CONDUCT.md) (`CODE_OF_CONDUCT.md`) | public collaboration and enforcement expectations for contributors | `Our standard`, `Enforcement` |

## Walkthrough / Context

Use this when you need one concrete end-to-end example of how a real practice became a published technique here.

| doc | bounded role | top-level sections |
|---|---|---|
| [Walkthrough: AOA-T-0001](../WALKTHROUGH.md) (`WALKTHROUGH.md`) | one end-to-end example of origin practice, publication, reuse, and why the repo stores techniques this way | `1. Origin practice`, `2. Published technique`, `3. Reuse evidence`, `4. Second-context adaptation`, `5. Why this matters here` |

## Status / Release

Use these when the question is what changed, what is currently unreleased, and how the public release path is validated.

| doc | bounded role | top-level sections |
|---|---|---|
| [Changelog](../CHANGELOG.md) (`CHANGELOG.md`) | release and unreleased status history for the public corpus | `[Unreleased]`, `[0.4.0] - 2026-04-10`, `[0.3.0] - 2026-04-01`, `[0.2.0] - 2026-03-23`, `[0.1.0] - 2026-03-17` |
| [Releasing `aoa-techniques`](RELEASING.md) (`docs/RELEASING.md`) | bounded release flow and validation path for public docs and technique updates | `Release goals`, `Recommended release flow`, `Release note shape`, `Versioning guidance`, `What not to optimize yet`, `Current stance` |

## Boundaries

- The source of meaning stays in the authored docs themselves.
- The bounded source set is exactly the 12 authoritative public docs/status files named in `REPO_DOC_SURFACE_LIFT_GUIDE.md`.
- This surface and its manifest are routing aids only. They do not become a new source of truth or a status-policy engine.
