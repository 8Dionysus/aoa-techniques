# GitHub Landing And Mechanics Direction Split Correction

Status: accepted

Date: 2026-05-06

## Index Metadata

- Decision ID: AOA-TECH-D-0043
- Original date: 2026-05-06
- Surface classes: release/GitHub
- Technique axes: github landing
- Mechanic parents: none
- Guard families: release/tooling
- Posture: accepted

## Context

`Agents-of-Abyss` has a mature GitHub landing route: root `AGENTS.md` owns the
agent-facing branch, PR, CI, merge, and clean-main sequence, while
`.github/AGENTS.md`, CODEOWNERS, the PR template, and workflows keep the
GitHub-native files aligned with that route.

`aoa-techniques` already had a strong `Repo Validation` workflow and
technique-specific issue templates, but the route was split across
`CONTRIBUTING.md`, a light PR template, and implicit agent practice. It also
had mechanics package roadmaps, but several were honest next-pass notes created
during active distillation rather than stable contour surfaces.

The repository must stay both an AoA organ and a standalone public technique
library. Copying center wording directly would blur that boundary.

An initial local pass introduced a root `mechanics/ROADMAP.md` to carry
mechanics-wide parity pressure. A deeper comparison with `Agents-of-Abyss`
showed that this was the wrong translation. AoA center keeps repo-level
direction in the root roadmap and local future pressure in package roadmaps; the
mechanics root stays an atlas, law, topology, and request/receipt route.

## Options

- Leave the GitHub route implicit and rely on repeated agent memory.
- Copy the AoA `.github` and PR-template shape directly.
- Adapt the AoA pattern: put the agent landing workflow in root `AGENTS.md`,
  add `.github/AGENTS.md` for platform-local files, keep the PR template inside
  the existing generated-template H2 contract, and expand CODEOWNERS to current
  governance-critical surfaces.
- Add a mechanics-wide roadmap for local package parity.
- Keep no root `mechanics/ROADMAP.md`; put repo-level mechanics-to-canon
  direction in root `ROADMAP.md`, and put package-local future pressure in
  `mechanics/<slug>/ROADMAP.md`.

## Decision

Use the adapted AoA pattern.

Root `AGENTS.md` now owns the `aoa-techniques` GitHub landing workflow and
post-change route review. `.github/AGENTS.md` owns the local platform-file
route. The PR template stays within its existing generated manifest contract:
`Summary`, `Validation`, `Notes`, and `Checklist`.

CODEOWNERS now covers governance-critical root files, public docs, GitHub
platform files, mechanics, generated companions, scripts, tests, templates,
techniques, and provenance districts.

Do not keep a root `mechanics/ROADMAP.md`.

Root `ROADMAP.md` owns repo-level technique-canon direction, including the
mechanics-to-canon horizon. `mechanics/README.md` owns the mechanics atlas,
package-card standard, and package-roadmap standard. Package roadmaps own
package-local future pressure. Package `LANDING_LOG.md`, `PROVENANCE.md`, and
`legacy/` preserve checked landings and lineage.

## Rationale

The goal is to make future GitHub landings repeatable for agents without
making `.github/` a hidden source of repository law. The route belongs in root
`AGENTS.md` because agents read it before mutation. `.github/AGENTS.md` keeps
the platform files aligned without duplicating the whole rule.

The PR template could not be expanded with AoA-style top-level sections because
`aoa-techniques` already treats GitHub templates as source-backed generated
inputs. Keeping the four top-level sections preserves validation and still
adds the missing surface, mechanics, generated, and owner-boundary checks.

The mechanics roadmap gap had a different cause: `aoa-techniques` mechanics
were built while the repo was distilling and reforming technique canon. Their
roadmaps lagged behind the current package maturity.

The corrected translation is not to add a new root roadmap under mechanics.
That would create a second future-direction owner between root `ROADMAP.md` and
package roadmaps, and future agents would have to guess which one wins. AoA's
better pattern is quieter: the root names project-level direction, the mechanics
root routes the organ, and each package names its own current contour and next
valid movement.

## Consequences

- Future commit, push, PR, validation, merge, and clean-main work should follow
  root `AGENTS.md`.
- GitHub platform edits should read `.github/AGENTS.md` and keep generated
  GitHub template manifests rebuilt from authored templates.
- Future mechanics-to-canon direction belongs in root `ROADMAP.md`; package
  future pressure belongs in `mechanics/<slug>/ROADMAP.md`.
- `mechanics/README.md` may carry short package standards because it is the
  mechanics atlas. It must not become a hidden backlog.
- The repository keeps `.gitignore` exceptions only for package roadmaps, not
  for a root `mechanics/ROADMAP.md`.
- Future agents should not recreate `mechanics/ROADMAP.md` unless a later
  decision explicitly changes this source-of-truth split.
- This does not make `aoa-techniques` the AoA center, a skill owner, proof
  authority, runtime owner, or owner-acceptance surface.

## Verification

Verified with:

```bash
python scripts/build_github_review_template_manifest.py
python scripts/build_repo_doc_surface_manifest.py
python scripts/validate_nested_agents.py
python scripts/release_check.py
```
