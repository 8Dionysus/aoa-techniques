# Canonical Readiness

## Technique
- id: AOA-T-0105
- name: single-missing-evidence-request

## Verdict
- approved for canonical promotion

## Evidence summary
- origin evidence is strong enough to justify a promoted public bundle
- Agon lawful move grammar defines `request_evidence` as asking for support needed to keep a claim alive while blocking fabrication and final proof verdicts
- the center audit evidence ledger separately owns missing-evidence notes without turning them into proof or memory
- the costly-closure trial uses `request_evidence` only as a pre-protocol closure blocker and owner-review artifact


## Default-use rationale
- Use this as the default single-object request when one missing evidence item could change or block a bounded review state.
- the second context proves the same move outside the original extraction packet while preserving portability and owner boundaries
- It is not Agon law, proof sufficiency, broad research, or a verdict against the claim.

## Fresh public-safety check
- review date: 2026-05-13
- result: pass
- sanitization still holds: public wording keeps the reusable technique atom while stripping local command wrappers, private session detail, and neighboring owner authority

## Remaining gaps
- no canonical blocker remains for this promotion wave; future non-AoA external adoption can widen evidence but is not required for this bounded canonical review
- downstream evidence ref: `repo:Agents-of-Abyss/mechanics/agon/parts/lawful-move-grammar/config/agon_lawful_moves.seed.json` hash `645ac975da7f41caf80e529919185f5daf6034b7`
- downstream evidence ref: `repo:Agents-of-Abyss/mechanics/audit/parts/evidence-ledger/README.md` hash `9a7aa42f7c30838378bc73dd25d99f9942dd2cf5`
- downstream evidence ref: `repo:aoa-playbooks/playbooks/agon-costly-closure-trial/PLAYBOOK.md` hash `5482481100fb67187b420f22c44835435b74332e`
- boundary preserved: one missing object is requested; absence blocks or narrows review without proving failure
- boundary preserved: downstream consumers are evidence and adaptation references, not hidden runtime dependencies for standalone reuse

## Recommendation
- move `AOA-T-0105` to `canonical`
