# Decision Note: Docs Surface Guardrails And Tree Contract Slimming

Status: accepted
Date: 2026-05-16

## Index Metadata

- Decision ID: AOA-TECH-D-0058
- Original date: 2026-05-16
- Surface classes: docs route
- Technique axes: topology
- Mechanic parents: none
- Guard families: docs route
- Posture: accepted

## Context

The `docs/` root had become legible only after already knowing the repository.
[Documentation Map](../README.md) carried long duplicate route lists,
[Start Here](../START_HERE.md) repeated deeper map work, and
[Technique Tree Contract](../TECHNIQUE_TREE_CONTRACT.md) mixed current path law
with a full historical migration ledger.

The repository already has better owner homes for the dense material:
[decisions](./) for rationale, [legacy](../../legacy/) for public-safe
repo-wide receipts, [mechanics](../../mechanics/) for operating evidence, and
[generated](../../generated/) for reproducible JSON companions. The missing
piece was a docs-local topology rule that makes flat `docs/*.md` surfaces prove
why they still belong at the docs root.

## Options considered

1. Leave the docs root as-is and rely on existing filenames and tests.
2. Move generated readers and old compatibility docs into new subdirectories in
   one broad migration.
3. Add docs-root guardrails, index every current flat docs file, slim entry
   maps, and split the active tree contract from historical migration detail.

## Decision

Adopt option 3.

- Add [Thematic District Protocol](../guardrails/THEMATIC_DISTRICT_PROTOCOL.md)
  as docs-root topology law.
- Add [Current Surface Index](../guardrails/CURRENT_SURFACE_INDEX.md) as the
  current explanation for every flat `docs/*.md` surface.
- Keep generated Markdown readers flat only until their family has a named
  `docs/readers/` district.
- Move the repeated KAG/source-lift authored guide family into
  [Source-Lift Guides](../source-lift/README.md) once the generated readers
  have their own district.
- Move the review, maturity, semantic-review, and caution guide family into
  [Review Guides](../review/README.md) once those guides form a real district
  rather than isolated flat docs-root contracts.
- Move the selection, kind, handoff, and capsule guide family into
  [Selection Guides](../selection/README.md) once those guides form a real
  chooser/compact-use district.
- Keep generated JSON under [generated](../../generated/).
- Slim [Start Here](../START_HERE.md) and [Documentation Map](../README.md)
  back to route surfaces.
- Keep [Technique Tree Contract](../TECHNIQUE_TREE_CONTRACT.md) as current path
  law and route historical wave detail to the [Final Tree Migration Ledger](../../mechanics/distillation/parts/technique-reform-ingress/reviews/final-tree-migration-ledger.md),
  [Root Legacy Index](../../legacy/INDEX.md), and [legacy receipts](../../legacy/receipts/).

## Rationale

A broad directory migration would create churn across builders, generated
manifests, release docs, and tests before the current file roles were explicit.
Leaving the flat root alone would preserve the maze.

The chosen path makes the current structure reviewable first. It gives future
agents a map for deciding which flat docs are still justified and which should
move later, while keeping the active route docs compact enough for public
readers and small agents.

## Consequences

- Flat docs files now have a checkable index surface.
- Historical tree migration detail no longer bloats the active tree contract.
- Generated Markdown readers remain discoverable, but their authority boundary
  is explicit.
- `TECHNIQUE_KIND_BASELINE.md` was folded into the living
  [Technique Kind Guide](../selection/TECHNIQUE_KIND_GUIDE.md).
- `VIA_NEGATIVA_CHECKLIST.md` was folded into the active
  [Technique Atom Contract](../TECHNIQUE_ATOM_CONTRACT.md).
- Bulky generated Markdown readers moved under [Generated Readers](../readers/README.md):
  source-lift readers under [Source-Lift Readers](../readers/source-lift/README.md),
  the kind reader under [Kind Readers](../readers/kind/README.md), and the
  capsule reader under [Runtime Readers](../readers/runtime/README.md), the
  selection readers under [Selection Readers](../readers/selection/README.md),
  the shadow reader under [Review Readers](../readers/review/README.md), and
  the repo-doc reader under [Repo-Doc Readers](../readers/repo/README.md).
- KAG/source-lift authored guides moved under [Source-Lift Guides](../source-lift/README.md),
  so repeated section, checklist, example, evidence-note, metadata, relation,
  caution, repo-doc, and export contracts no longer sit as flat docs-root
  siblings.
- Review guide contracts moved under [Review Guides](../review/README.md), so
  canonical rubric, canonical promotion review, semantic-review interpretation,
  and shadow/caution guidance now have one district route instead of four flat
  docs-root siblings.
- Selection guide contracts moved under [Selection Guides](../selection/README.md),
  so chooser, kind, handoff, and capsule guidance now has one district route
  instead of four flat docs-root siblings.
- `AGENTS_ROOT_REFERENCE.md` was archived under
  [legacy/archive](../../legacy/archive/AGENTS_ROOT_REFERENCE.md) after the
  root card stopped using it as current route law.
- The old root `WALKTHROUGH.md` moved into
  [examples](../../examples/README.md), because the walkthrough is a worked
  example rather than root authority.
- [Documentation Map](../README.md) is now a route map instead of a duplicate
  directory encyclopedia, and [Decisions District](./README.md) indexes every
  decision record so rationale lookup does not depend on filename guessing.
- The repo-doc reader source set narrowed to `20` public route/canon/status
  files; root examples stay discoverable through [examples](../../examples/README.md)
  rather than the authoritative repo-doc manifest.
- Future generated-reader directory migrations should move one family at a
  time with builder, test, and link updates in the same change.

## Source surfaces

- [Documentation Map](../README.md)
- [Start Here](../START_HERE.md)
- [Root Surface Law](../ROOT_SURFACE_LAW.md)
- [Technique Atom Contract](../TECHNIQUE_ATOM_CONTRACT.md)
- [Technique Kind Guide](../selection/TECHNIQUE_KIND_GUIDE.md)
- [Selection Guides](../selection/README.md)
- [Technique Tree Contract](../TECHNIQUE_TREE_CONTRACT.md)
- [Generated Readers](../readers/README.md)
- [Review Guides](../review/README.md)
- [Source-Lift Guides](../source-lift/README.md)
- [Source-Lift Readers](../readers/source-lift/README.md)
- [Thematic District Protocol](../guardrails/THEMATIC_DISTRICT_PROTOCOL.md)
- [Current Surface Index](../guardrails/CURRENT_SURFACE_INDEX.md)
- [Link And Shape Hygiene Protocol](../guardrails/LINK_AND_SHAPE_HYGIENE_PROTOCOL.md)
- [Hygiene Guardrail Index](../guardrails/HYGIENE_GUARDRAIL_INDEX.md)
- [Final Tree Migration Ledger](../../mechanics/distillation/parts/technique-reform-ingress/reviews/final-tree-migration-ledger.md)
- [Root Legacy Index](../../legacy/INDEX.md)
- [Archived AGENTS Root Reference](../../legacy/archive/AGENTS_ROOT_REFERENCE.md)
- [Examples District](../../examples/README.md)
- [Plan-Diff-Apply-Verify-Report Walkthrough](../../examples/plan-diff-apply-verify-report-walkthrough.md)
- [Decisions District](./README.md)

## Follow-up route

Use [Current Surface Index](../guardrails/CURRENT_SURFACE_INDEX.md) before the
next docs-root cleanup. Move any remaining broad guide family only when it has
a durable district role, route card, link migration, and validator/test update
in the same change.

## Verification

Validate with:

```bash
python -m unittest tests.test_docs_surface_guardrails
python scripts/validate_repo.py
python scripts/run_tests.py
```
