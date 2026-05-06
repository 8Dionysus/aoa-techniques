# Promotion-Boundary Tree Pilot Receipt

Date: 2026-05-05

## Status

Landed.

## Reviewed Source

- [Promotion-Boundary Direct-Read Migration Review](../../mechanics/distillation/parts/technique-reform-ingress/reviews/promotion-boundary-direct-read-migration-review.md)
- [Technique Tree Contract](../../docs/TECHNIQUE_TREE_CONTRACT.md)
- [Technique Reform Ingress](../../mechanics/distillation/parts/technique-reform-ingress/README.md)

## Movement

Twenty-sixth authored path migration:

| technique | old path | new path |
|---|---|---|
| `AOA-T-0089` | `techniques/agent-workflows/quest-unit-promotion-review/` | `techniques/governance/promotion-boundary/quest-unit-promotion-review/` |
| `AOA-T-0090` | `techniques/agent-workflows/nearest-wrong-target-rejection/` | `techniques/governance/promotion-boundary/nearest-wrong-target-rejection/` |
| `AOA-T-0102` | `techniques/agent-workflows/skill-proposal-handoff-packet/` | `techniques/governance/promotion-boundary/skill-proposal-handoff-packet/` |

## Preserved

- IDs stayed unchanged.
- `domain` stayed unchanged as `agent-workflows` for all three bundles.
- `kind` stayed unchanged as `assessment`, `guardrail`, and `handoff`
  respectively.
- All three bundles stayed `promoted`; path movement did not imply canonical
  promotion.
- Evidence, relations, checks, examples, notes, maturity, validation-strength
  metadata, and public-safety posture moved with each bundle.
- No `tree_path`, `family`, capability, substrate, execution-profile, or risk
  frontmatter was added.

## Boundary

This receipt records path accounting only.

`promotion-boundary` remains a governance shelf for promotion verdict,
nearest-wrong-target rejection, and skill-proposal handoff posture before
owner-surface authorship. It does not become skill acceptance, skill
activation, quest/playbook promotion doctrine, role contract law, proof
verdict authority, memory write, routing policy, Method-growth law, local
owner consent, runtime behavior, KAG promotion, ToS canon, broad orchestration
governance, or a move for the queued `practice-adoption-lifecycle` candidate.

## Verification Lane

Expected validation for the migration wave:

```bash
python -m unittest tests.test_distillation_mechanics_topology tests.test_root_legacy_topology tests.test_roadmap_parity
python scripts/validate_nested_agents.py
python scripts/validate_repo.py
python scripts/release_check.py
```
