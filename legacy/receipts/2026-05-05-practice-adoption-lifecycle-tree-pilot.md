# Practice-Adoption-Lifecycle Tree Pilot Receipt

Date: 2026-05-05

## Status

Landed.

## Reviewed Source

- [Practice-Adoption-Lifecycle Direct-Read Migration Review](../../mechanics/distillation/parts/technique-reform-ingress/reviews/practice-adoption-lifecycle-direct-read-migration-review.md)
- [Technique Tree Contract](../../docs/TECHNIQUE_TREE_CONTRACT.md)
- [Technique Reform Ingress](../../mechanics/distillation/parts/technique-reform-ingress/README.md)

## Movement

Twenty-seventh authored path migration:

| technique | old path | new path |
|---|---|---|
| `AOA-T-0101` | `techniques/agent-workflows/local-pattern-adoption-gate/` | `techniques/governance/practice-adoption-lifecycle/local-pattern-adoption-gate/` |
| `AOA-T-0103` | `techniques/agent-workflows/adopted-practice-retention-review/` | `techniques/governance/practice-adoption-lifecycle/adopted-practice-retention-review/` |
| `AOA-T-0104` | `techniques/agent-workflows/superseded-practice-obsolescence-route/` | `techniques/governance/practice-adoption-lifecycle/superseded-practice-obsolescence-route/` |

## Preserved

- IDs stayed unchanged.
- `domain` stayed unchanged as `agent-workflows` for all three bundles.
- `kind` stayed unchanged as `guardrail`, `assessment`, and `handoff`
  respectively.
- All three bundles stayed `promoted`; path movement did not imply canonical
  promotion.
- Evidence, relations, checks, examples, notes, maturity, validation-strength
  metadata, and public-safety posture moved with each bundle.
- No `tree_path`, `family`, capability, substrate, execution-profile, or risk
  frontmatter was added.

## Boundary

This receipt records path accounting only.

`practice-adoption-lifecycle` remains a governance shelf for local adoption,
retention, and obsolescence posture before an owner surface treats a practice
as durable, active, superseded, or ready for deprecation review. It does not
become Method-growth law, local owner consent, deletion, deprecation
execution, proof authority, memory truth, skill activation, route mutation,
runtime change, permanent practice retention, sibling owner acceptance, KAG
promotion, ToS canon, broad orchestration governance, or a move for the queued
`tool-use/tool-gateway` singleton.

## Verification Lane

Expected validation for the migration wave:

```bash
python -m unittest tests.test_distillation_mechanics_topology tests.test_root_legacy_topology tests.test_roadmap_parity
python scripts/validate_nested_agents.py
python scripts/validate_repo.py
python scripts/release_check.py
```
