# Canonical Readiness

## Technique
- id: AOA-T-0106
- name: single-scoped-evidence-reference

## Verdict
- approved for canonical promotion

## Evidence summary
- origin evidence is strong enough to justify a promoted public bundle
- Agon lawful move grammar defines `offer_evidence_reference` as providing a reviewable reference or artifact pointer without claiming final proof
- the audit evidence ledger contract keeps evidence lists, freshness posture, confidence limits, and proof routes separate from verdicts or memory truth
- the eval prebinding uses `offer_evidence_reference` inside an evidence-floor precheck while blocking truth decisions and ToS promotion


## Default-use rationale
- Use this as the default one-reference artifact when an available source can support a bounded review claim only under explicit limits.
- the second context proves the same move outside the original extraction packet while preserving portability and owner boundaries
- It is not proof, source-truth transfer, eval adequacy, or a multi-source provenance pack.

## Fresh public-safety check
- review date: 2026-05-13
- result: pass
- sanitization still holds: public wording keeps the reusable technique atom while stripping local command wrappers, private session detail, and neighboring owner authority

## Remaining gaps
- no canonical blocker remains for this promotion wave; future non-AoA external adoption can widen evidence but is not required for this bounded canonical review
- downstream evidence ref: `repo:Agents-of-Abyss/mechanics/agon/parts/lawful-move-grammar/config/agon_lawful_moves.seed.json` hash `645ac975da7f41caf80e529919185f5daf6034b7`
- downstream evidence ref: `repo:Agents-of-Abyss/mechanics/audit/parts/evidence-ledger/CONTRACT.md` hash `1429e709c5ac4c788f4487dd203e8713f149c3e2`
- downstream evidence ref: `repo:aoa-evals/config/agon_eval_prebindings.seed.json` hash `1ea8d841cf7892d712a91d156373a763688a7dcb`
- boundary preserved: one reference carries relevance, support scope, support limit, and reliance condition only
- boundary preserved: downstream consumers are evidence and adaptation references, not hidden runtime dependencies for standalone reuse

## Recommendation
- move `AOA-T-0106` to `canonical`
