# Decision Note: Root Markdown Surface Slimming

Status: accepted
Date: 2026-05-14

## Context

The old root Markdown set was mostly allowed by `docs/ROOT_SURFACE_LAW.md`, but
some old root files had started carrying the wrong kind of weight.

`README.md` re-indexed deep mechanic runbooks, generated reader paths, semantic
and shadow review artifacts, and one-owner reports. `ROADMAP.md` preserved a
long tree-migration breadcrumb chain after the migration had already been
distilled into Distillation reviews, ledgers, and package roadmaps. Tests also
required some of that root over-indexing, which made the maze harder to remove
safely.

The `Agents-of-Abyss` center pattern separates the same concerns: root roadmap
keeps horizon direction, changelog keeps release history, mechanic landings and
legacy receipts preserve detail, and decision records explain why the route was
chosen.

## Options considered

1. Keep the root files as they were, preserving every deep route directly in
   `README.md` and every migration breadcrumb directly in `ROADMAP.md`.
2. Delete old root Markdown files that had accumulated noise.
3. Keep the allowed root Markdown file set, slim active root surfaces back to
   their roles, and preserve the old tree-migration breadcrumb chain as a
   Distillation legacy receipt.

## Decision

Keep the old root Markdown file set, but slim the active route surfaces:

- `README.md` stays a compact public front door and route chooser.
- `ROADMAP.md` stays a live repo-direction surface, not a migration ledger.
- Deep runbooks, review packets, scout reports, generated readers, semantic
  reviews, shadow reviews, and migration details stay discoverable through
  `docs/README.md`, `docs/REPO_DOC_SURFACES.md`, generated manifests, and
  owner-local `mechanics/**` surfaces.
- The old root roadmap breadcrumb chain is preserved as
  `mechanics/distillation/legacy/raw/ROOT_ROADMAP_TREE_MIGRATION_BREADCRUMBS_2026-05-14.md`
  so historical migration assertions do not require re-bloating the live root
  roadmap.
- Tests should protect this boundary by checking that root points to the
  correct maps and contracts, not by forcing every deep route into root prose.

## Rationale

Deleting root Markdown files would remove legitimate public entry, authority,
direction, obligation, release, contribution, legal, example, and agent-route
roles. Keeping the old text would preserve discoverability at the cost of
making root surfaces unreliable as first routes.

The chosen path keeps the root file set stable while moving density to the
surfaces that can interpret it. It also matches the AoA center split without
copying center authority into the technique canon: root direction stays in
`ROADMAP.md`, release-visible history stays in `CHANGELOG.md`, and historical
tree migration evidence stays with Distillation legacy.

## Consequences

- Root readers get a shorter entry path.
- Mechanic and generated detail remains available, but the owner surface must
  carry the detail and its interpretation.
- Future additions should not treat "discoverable from root" as "listed
  directly in `README.md`".
- Historical migration tests read a preserved receipt instead of using the live
  root roadmap as an archive.

## Source surfaces

- `README.md`
- `ROADMAP.md`
- `CHANGELOG.md`
- `docs/ROOT_SURFACE_LAW.md`
- `docs/README.md`
- `docs/REPO_DOC_SURFACES.md`
- `mechanics/distillation/ROADMAP.md`
- `mechanics/distillation/parts/technique-reform-ingress/reviews/final-tree-migration-ledger.md`
- `mechanics/distillation/parts/technique-reform-ingress/reviews/whole-tree-closeout-review.md`
- `mechanics/distillation/legacy/raw/ROOT_ROADMAP_TREE_MIGRATION_BREADCRUMBS_2026-05-14.md`

## Follow-up route

Revisit this decision if root `README.md` becomes too thin to route a new
reader, if root `ROADMAP.md` starts carrying mechanic-local ledgers again, or
if a generated/docs map no longer makes deep surfaces discoverable.

## Verification

This decision is validated by the root Markdown cleanup, updated tests for the
new root-entry contract, rebuilt repo-doc manifests, and `scripts/release_check.py`.
