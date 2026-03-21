# Second Context Adaptation

## Technique
- id: AOA-T-0020
- name: evidence-note-provenance-lift

## Target project
- name: aoa-techniques
- environment: public technique canon with typed supporting notes and derived manifests
- runtime: markdown-first repository where provenance lookup must stay readable to humans and agents

## What changed
- note kinds: the public form now mirrors a live donor pattern from `aoa-evals`, where bundle `eval.yaml` files carry typed `evidence` arrays made of `kind` plus `path` handles instead of one generic support bucket
- paths: the public form keeps note paths explicit so each supporting note remains independently reachable, and the donor validator checks that each evidence path actually exists on disk
- dependencies: the adaptation is grounded in committed `aoa-evals` bundle manifests, the generated `eval_catalog.json` lift, and `scripts/validate_repo.py`, not in repo-local sketch language or graph semantics
- operating assumptions: a public repository can expose provenance handles for note lookup while still leaving the note body as the place where interpretation lives

## What stayed invariant
- contract: provenance remains note-kind plus note-path lookup
- validation logic: readers can find the supporting note without losing the authored note text
- safety rules: the manifest stays derived and does not become the source of truth for note meaning

## Risks introduced by adaptation
- note kinds can still multiply if future bundles start splitting provenance roles too finely
- a derived manifest can look complete even when the supporting note text still carries the real judgment
- if the note kind layer becomes too clever, maintainers may start expecting graph semantics that the technique does not claim
- the current live donor proof is still one markdown-first eval corpus; the next reuse step has to come from a second non-eval corpus using the same typed lift

## Evidence
- `aoa-evals/bundles/aoa-bounded-change-quality/eval.yaml` and sibling bundles use `evidence` arrays with explicit `kind` and `path` pairs
- `aoa-evals/generated/eval_catalog.json` lifts those evidence entries as typed provenance handles instead of flattening them into free-form prose
- `aoa-evals/scripts/validate_repo.py` enforces evidence path existence and bounded evidence-kind contracts, including status-specific kinds and support-note constraints
- `AOA-T-0018 markdown-technique-section-lift` and `AOA-T-0019 frontmatter-metadata-spine` still fit the same public pattern by keeping derived lookup shallow while leaving real meaning in markdown

## Result
- works as a bounded transfer from a live `aoa-evals` donor corpus, with the remaining gap narrowed to a second markdown-first corpus proving the same typed note lift
