# Semantic Review Guide

This guide defines the bounded contract behind the semantic-review family.

Use it when the question is how authored semantic review docs relate to their generated manifest and current downstream consumers, without turning semantic reviews into status automation or graph semantics.

See also:
- [Start Here](START_HERE.md)
- [Selection Patterns](SELECTION_PATTERNS.md)
- [`../generated/semantic_review_manifest.json`](../generated/semantic_review_manifest.json)
- [Documentation Map](README.md)

This family uses one stable shape:

- authoritative source:
  - authored `*_SEMANTIC_REVIEW.md` docs
- reader model:
  - the review docs themselves
  - there is no separate generated reader surface in this wave
- derived manifests:
  - `generated/semantic_review_manifest.json`
  - `generated/semantic_review_manifest.min.json`
- current downstream consumer:
  - review-backed working sets in `SELECTION_PATTERNS.md`
- what it must not become:
  - a policy engine
  - a status driver
  - graph semantics
  - a replacement for bundle-local notes or explicit human review

## Source Contract

Each semantic review doc stays human-authored and cluster-bounded.

It is allowed to answer:

- do these nearby techniques still read as distinct?
- where is the current watch seam?
- is the cluster stable enough to keep as-is, or should a later refresh split or expand it?

It is not allowed to:

- change bundle status by itself
- replace canonical-readiness notes
- define runtime routing policy beyond the bounded working sets already consumed from authored review docs

## Derived Manifest Role

The semantic-review manifest is a derived lookup aid over authored review docs.

It can expose:

- review path
- reviewed techniques
- cluster title
- next-step summary

It must not become the source of truth for review meaning.
If the manifest and authored review doc disagree, fix the authored review doc or regenerate the manifest.

## Boundaries

- Semantic reviews remain human review surfaces first.
- They can justify bounded working sets, but they do not auto-promote, auto-demote, or rank techniques.
- They stay distinct from shadow reviews, which focus on caution seams rather than semantic distinctness.
- They stay distinct from bundle-local notes, which own bundle-specific promotion or caution posture.

## Regeneration

When semantic review docs change, regenerate and validate with:

- `python scripts/build_semantic_review_manifest.py`
- `python scripts/build_catalog.py`
- `python scripts/validate_repo.py`
