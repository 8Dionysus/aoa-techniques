# Technique Tree Contract

Date: 2026-05-04

## Index Metadata

- Decision ID: AOA-TECH-D-0041
- Original date: 2026-05-04
- Surface classes: technique tree
- Technique axes: tree
- Mechanic parents: none
- Guard families: technique tree
- Posture: accepted

## Status

Accepted

## Context

`aoa-techniques` already has an atom contract and a topology contract. The atom
contract keeps one technique small. The topology contract keeps classification
faceted so `domain`, `kind`, family, capability, substrate, execution profile,
risk posture, and relations do not collapse into one overloaded tag system.

That still leaves a repository-structure problem. The current
`techniques/<domain>/<slug>/` layout works for the first public corpus, but it
does not give enough room for a library meant to grow toward `1000+` techniques.
Broad folders such as `agent-workflows` and `docs` are useful review lanes, but
they will become hard to browse if they also carry the entire root architecture.

## Options

- Keep the current domain-folder layout as the long-term structure and rely on
  generated facets for all deeper navigation.
- Make one topology axis, such as `kind` or `family`, the directory tree.
- Add a separate tree contract: a root placement spine with trunks, shelves,
  and leaf bundles, while keeping current frontmatter and scout axes distinct.

## Decision

Add `docs/TECHNIQUE_TREE_CONTRACT.md` as the repo-owned guide for future
`techniques/` directory architecture.

The tree contract defines a target path shape:

```text
techniques/<trunk>/<shelf>/<technique-slug>/
```

The contract treats the tree as authored placement structure, not as a full
classification record. `domain` and `kind` remain current frontmatter truth.
Family and the other topology axes remain scout/design surfaces until reviewed
promotion work says otherwise.

## Consequences

Future reform can design a beautiful scalable root tree without pretending that
all bundles are ready to move immediately.

The first implementation must be projection-first: generate or review proposed
tree paths, check them against bundle meaning, pilot one bounded subtree, then
move files only with regenerated catalogs, capsules, docs, validators, and
decision records.

The tradeoff is one more contract for contributors to understand. The gain is
that path architecture stops being implied by the current domain folders and
becomes a deliberate part of canon-scale design.
