# Canonical Readiness

## Technique
- id: AOA-T-0018
- name: markdown-technique-section-lift

## Verdict
- stronger defer after cross-context reinforcement, still promoted

## Evidence summary
- origin evidence: the bundle came from the section-manifest layer and the KAG source-lift guidance, so it already has a bounded generated-output anchor
- first downstream consumer: `aoa-skills` provides live donor evidence for the same contract through `docs/BRIDGE_SPEC.md` and `generated/skill_catalog.json`, where technique selection is pinned by `source_ref` and bounded by `use_sections`
- second markdown-first consumer: `aoa-evals/docs/README.md` and `generated/eval_sections.full.json` now show the same source-owned section-lift discipline in a second bundle family, with bounded section expansion over authored eval markdown
- routing reinforcement: `aoa-routing/README.md` now points expand actions at `aoa-techniques/generated/technique_sections.full.json`, `aoa-skills/generated/skill_sections.full.json`, and `aoa-evals/generated/eval_sections.full.json`, proving that the section surfaces are real cross-repo expand-time targets rather than one local helper
- validation strength: the bundle now has stable sections, examples, checks, one bridge-style downstream consumer, one second markdown-first bundle-family consumer, and one thin-router consumer that keeps section lift in the `pick -> inspect -> expand` path without collapsing into metadata or provenance work

## Default-use rationale
- this remains the right default when bundle-level routing is no longer enough and section lookup still needs to stay derived from markdown rather than from a metadata-first store
- it is narrower than any metadata-spine technique because the core contract is still section meaning, not routing fields
- it is narrower than provenance and relation lift because its job is still "which section should I inspect next?" rather than "why is this technique trusted?" or "what sits next to it?"
- the new evidence now shows that the same lift remains useful outside this public canon, but this first evidence wave still stops short of a status flip while the current technique-named scope is rechecked against the broader bundle-family reuse

## Fresh public-safety check
- review date: 2026-03-23
- result: pass
- sanitization still holds: the bundle keeps the reusable section-lift contract and avoids repo-local implementation trivia
- public reuse check: the pattern remains understandable without hidden automation or private source files

## Remaining gaps
- the second live markdown-first consumer now exists, so the remaining gap is no longer cross-context evidence breadth
- the next honest question is whether the current technique-named contract should stay narrow around `TECHNIQUE.md`-shaped section authority or whether the evidence now points to a later generic bundle-section sibling
- a future canonical decision should still show that section lift remains an expand-time routing surface and does not drift into metadata-spine semantics, provenance lift, or a generic graph-facing bundle program

## Recommendation
- keep `AOA-T-0018` `promoted`
- keep the status unchanged in this Wave A pass, but treat the bundle as materially strengthened and reopen the next canonical decision from the new cross-context baseline rather than from the old single-bridge baseline
