# Canonical Readiness

## Technique
- id: AOA-T-0018
- name: markdown-technique-section-lift

## Verdict
- approve for canonical promotion

## Evidence summary
- origin evidence: the bundle came from the section-manifest layer and the KAG source-lift guidance, so it already has a bounded generated-output anchor
- first downstream consumer: `aoa-skills` provides live donor evidence for the same contract through `docs/BRIDGE_SPEC.md` and `generated/skill_catalog.json`, where technique selection is pinned by `source_ref` and bounded by `use_sections`
- second markdown-first consumer: `aoa-evals/docs/README.md` and `generated/eval_sections.full.json` now show the same source-owned section-lift discipline in a second bundle family, with bounded section expansion over authored eval markdown
- routing reinforcement: `aoa-routing/README.md` now points expand actions at `aoa-techniques/generated/technique_sections.full.json`, `aoa-skills/generated/skill_sections.full.json`, and `aoa-evals/generated/eval_sections.full.json`, proving that the section surfaces are real cross-repo expand-time targets rather than one local helper
- validation strength: the bundle now has stable sections, examples, checks, one bridge-style downstream consumer, one second markdown-first bundle-family consumer, one thin-router consumer that keeps section lift in the `pick -> inspect -> expand` path, and a follow-up canonical review that confirms the technique-named scope can stay bounded while becoming the default

## Default-use rationale
- this is now the right default when bundle-level routing has already selected the bundle and the next need is bounded section lookup that stays derived from authored markdown rather than from a metadata-first store
- it remains narrower than any metadata-spine technique because the core contract is still section meaning and section inspection, not bundle identity or routing fields
- it remains narrower than provenance, relation, and caution lift because its job is still "which section should I inspect next?" rather than "why is this technique trusted?", "what sits next to it?", or "what caution language should I inspect?"
- the broader question of a future generic bundle-section sibling is now future-evolution work, not a blocker to using the current `TECHNIQUE.md`-section contract as the canonical default inside this family

## Fresh public-safety check
- review date: 2026-03-23
- result: pass
- sanitization still holds: the bundle keeps the reusable section-lift contract and avoids repo-local implementation trivia
- public reuse check: the pattern remains understandable without hidden automation or private source files

## Remaining gaps
- no blocking gap remains for canonical use as long as the technique stays bounded to stable section lift over authored `TECHNIQUE.md` bundles
- future review should keep watching for generic bundle-section pressure, manifest overread, and sibling-boundary drift into metadata, provenance, relation, or caution work
- section lift should remain an expand-time routing surface and should not drift into metadata-spine semantics, provenance lift, or a generic graph-facing bundle program

## Recommendation
- promote `AOA-T-0018` to `canonical`
- use `AOA-T-0018` as the default section-lift entrypoint for the KAG/source-lift family once bundle-level routing has already selected the bundle and the next need is bounded section inspection
