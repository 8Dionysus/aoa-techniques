# Origin Evidence

## Technique
- id: AOA-T-0048
- name: semantic-review-surface-lift

## Source project
- name: aoa-techniques
- source files:
  - `docs/SEMANTIC_REVIEW_GUIDE.md`
  - `generated/semantic_review_manifest.json`
  - `docs/SELECTION_PATTERNS.md`

## Evidence
- `docs/SEMANTIC_REVIEW_GUIDE.md` defines the bounded contract for authored semantic-review docs and explicitly keeps them human-authored and cluster-bounded
- `generated/semantic_review_manifest.json` shows the current repo already consumes those authored review docs as derived lookup knowledge
- `docs/SELECTION_PATTERNS.md` shows review-backed working sets as a real downstream consumer of the authored review surface

## Interpretation
- the reusable pattern already exists in a live public repository as review-doc-first source lift with a derived manifest and a selection consumer
- the technique is not speculative; it is a compact generalization of the semantic-review behavior that `aoa-techniques` already uses
