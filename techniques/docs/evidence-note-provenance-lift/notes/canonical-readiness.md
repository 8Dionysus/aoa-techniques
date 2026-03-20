# Canonical Readiness

## Technique
- id: AOA-T-0020
- name: evidence-note-provenance-lift

## Verdict
- defer for now

## Evidence summary
- origin evidence: the bundle already has a typed manifest anchor for note-kind and note-path provenance
- second context: the adaptation note shows the technique clearly enough to stay reusable, but it still reads as a repo-local provenance sketch rather than a live cross-repo proof
- validation strength: the bundle already has a checklist, an example, and explicit note-path routing, but it still lacks another markdown-first corpus proving the same note-kind contract in practice

## Default-use rationale
- this remains the right default when supporting notes should stay reachable by kind and path without becoming a note graph
- it is narrower than any proof-object or graph layer because the core contract is still provenance lookup, not relation inference
- the bundle should stay promoted until another repository proves that the same note-kind split remains useful outside this public canon

## Fresh public-safety check
- review date: 2026-03-20
- result: pass
- sanitization still holds: the bundle keeps the reusable provenance pattern and strips repo-local implementation trivia
- public reuse check: the pattern remains understandable without hidden automation or private source files

## Remaining gaps
- the main missing proof is live reuse in another markdown-first repository
- a future canonical review should show that typed note kinds and note paths survive repeated use without turning into graph semantics or flattened metadata

## Recommendation
- keep `AOA-T-0020` `promoted`
- defer canonical promotion until the technique proves itself in a live reuse context beyond the current repo-local sketch
