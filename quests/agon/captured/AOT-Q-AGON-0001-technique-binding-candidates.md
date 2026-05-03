# AOT-Q-AGON-0001: Agon Technique Binding Candidates

source_contract: quest_markdown_contract_v1

## Quest

Receive Wave IV practice candidate requests from `Agents-of-Abyss`.

## Owner Route

Owner route is `mechanics/agon/parts/move-technique-bridge/`. This quest keeps
the requested-only practice candidate source visible without promoting any
candidate into technique canon.

## Next Action

Keep the bridge generated index and validation route aligned with the current
candidate seed. If a candidate is ready for canon, open a separate technique
review instead of changing this quest into promotion authority.

## Acceptance Evidence

- config and generated candidate index are present;
- every candidate remains `requested_not_landed`;
- validation passes;
- no candidate is promoted as a canonical technique by this quest.

## Stop-lines

- Do not grant live Agon move law, arena authority, technique promotion, skill
  promotion, verdict authority, or owner acceptance from this quest.
- Do not treat requested-only candidates as landed bundles.

## Verify

```bash
python mechanics/agon/parts/move-technique-bridge/scripts/build_agon_technique_binding_candidates.py --check
python mechanics/agon/parts/move-technique-bridge/scripts/validate_agon_technique_binding_candidates.py
python -m pytest -q mechanics/agon/parts/move-technique-bridge/tests/test_agon_technique_binding_candidates.py
```
