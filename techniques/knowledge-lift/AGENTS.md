# AGENTS.md

Guidance for coding agents and humans working under
`techniques/knowledge-lift/`.

## Purpose

`knowledge-lift/` stores technique bundles whose primary placement question is
how authored source surfaces become bounded derived reader knowledge while the
authored source remains authoritative.

This is a tree trunk, not a frontmatter domain. Technique bundles here may keep
their existing `domain` and `kind` values when the reviewed move is only path
architecture.

## Current Shelves

Current shelves:

- `kag-source-lift/`: lifts markdown sections, frontmatter metadata, evidence
  notes, direct relations, caution language, repo-doc surfaces, review
  templates, and semantic-review docs into derived reader surfaces without
  replacing the authored source

## Trunk Rules

Keep the lifted source object explicit:

- what authored markdown, frontmatter, note, template, relation, risk section,
  or review doc remains the source of meaning
- what bounded derived reader surface is produced
- how the reader or generated output routes back to the authored source
- what graph behavior, scoring, policy, generated truth, or automatic verdict
  is refused

Do not turn a knowledge-lift technique into `aoa-kag` owner doctrine, graph
semantics, retrieval policy, proof authority, scoring, status automation,
workflow policy, or a generated source-of-truth replacement.

## Boundary

Use `docs/TECHNIQUE_TREE_CONTRACT.md` before adding another shelf here.

Do not add `tree_path` frontmatter merely because a bundle lives under this
trunk. Do not rename trunks or shelves without a reviewed projection and a
bounded migration receipt.

## Validation

After changing knowledge-lift techniques, run:

- `python scripts/validate_nested_agents.py`
- `python scripts/validate_repo.py`

Run `python scripts/release_check.py` when generated catalogs, source-owned KAG
exports, or reader surfaces changed.
