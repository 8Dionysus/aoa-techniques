# Canonical Readiness

## Technique
- id: AOA-T-0018
- name: markdown-technique-section-lift

## Verdict
- stronger defer, still promoted

## Evidence summary
- origin evidence: the bundle came from the section-manifest layer and the KAG source-lift guidance, so it already has a bounded generated-output anchor
- second context: `aoa-skills` now provides live donor evidence for the same contract through `docs/BRIDGE_SPEC.md` and `generated/skill_catalog.json`, where technique selection is pinned by `source_ref` and bounded by `use_sections`
- validation strength: the bundle has stable sections, examples, and checks, and the bridge flow shows the technique can survive a committed downstream consumer, but the proof set still stops at that bridge pattern rather than a second markdown-first consumer

## Default-use rationale
- this remains the right default when section lookup needs to stay derived from markdown rather than from a metadata-first store
- it is narrower than any metadata-spine technique because the core contract is still section meaning, not routing fields
- the bundle should stay promoted until another repository proves that the same lift remains useful outside this public canon

## Fresh public-safety check
- review date: 2026-03-20
- result: pass
- sanitization still holds: the bundle keeps the reusable section-lift contract and avoids repo-local implementation trivia
- public reuse check: the pattern remains understandable without hidden automation or private source files

## Remaining gaps
- the smallest remaining gap is a second live markdown-first consumer that is independent of the current `aoa-skills` bridge pattern
- a future canonical review should show that stable heading lift survives repeated use without turning into metadata-spine semantics

## Recommendation
- keep `AOA-T-0018` `promoted`
- defer canonical promotion until the technique proves itself in a second live markdown-first context beyond the current bridge pattern
