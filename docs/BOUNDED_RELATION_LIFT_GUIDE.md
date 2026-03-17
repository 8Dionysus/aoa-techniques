# Bounded Relation Lift Guide

This guide defines the bounded contract for `bounded-relation-lift-for-kag`.

Use it when the repository already has typed direct `relations`, but the next question is how those edges can serve as later KAG-oriented graph inputs without pretending they already carry relation rationale, graph behavior, or multi-hop semantics.

This guide is edge-first. It does not add new relation types, relation-rationale fields, graph traversal rules, or generated graph artifacts.

## Role Split

Keep the current relation surfaces distinct:

- `relations` carry direct typed adjacency between bundles
- semantic reviews and generated selection surfaces provide bounded human-reviewed context around those edges
- markdown bundles remain the authoritative source for why a relation exists

That split is the current relation-lift contract.

## Stable Relation Surfaces

The current relation layer is already stable enough for bounded direct-edge lifting:

- `type`
- `target`
- allowed relation types:
  - `requires`
  - `complements`
  - `supersedes`
  - `conflicts_with`
  - `used_together_for`
  - `derived_from`
  - `shares_contract_with`

Treat these as direct typed edges only. They are useful because the vocabulary is intentionally small and review-shaped.

## Current Relation Consumers

The current repository already has bounded relation consumers:

- `generated/technique_catalog.json`
- `generated/technique_catalog.min.json`
- `docs/TECHNIQUE_SELECTION.md`
- `docs/SELECTION_PATTERNS.md`

They use relations today for:

- direct adjacency hints
- neighboring technique inspection
- bounded working-set construction
- one-step navigation around current bundle contracts

That is already enough to justify later graph-edge lifting. It is not a reason to add more semantics yet.

## What Relations Are Not

Current relations should not be treated as:

- relation rationale
- weighted edges
- transitive graph truth
- multi-hop traversal policy
- a reason to widen the relation vocabulary before current direct-edge use stops being enough

If a reviewer needs the explanation for why two techniques relate, the answer still lives in markdown bundles, review notes, and bounded selection surfaces.

## Explicitly Deferred

Not part of this wave:

- no new relation types
- no relation-rationale metadata
- no graph inference
- no scoring or ranking logic
- no multi-hop traversal policy
- no generated graph artifacts
- no bundle or generated catalog changes

The current job is only to make the bounded direct-edge layer explicit so later KAG-oriented waves can lift those edges without reopening whether relations are already a graph platform.
