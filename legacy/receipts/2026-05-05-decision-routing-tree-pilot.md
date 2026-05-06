# Decision-Routing Tree Pilot Receipt

Date: 2026-05-05

## Status

Landed.

## Reviewed Source

- [Decision-Routing Direct-Read Migration Review](../../mechanics/distillation/parts/technique-reform-ingress/reviews/decision-routing-direct-read-migration-review.md)
- [Technique Tree Contract](../../docs/TECHNIQUE_TREE_CONTRACT.md)
- [Technique Reform Ingress](../../mechanics/distillation/parts/technique-reform-ingress/README.md)

## Movement

Twentieth authored path migration:

| technique | old path | new path |
|---|---|---|
| `AOA-T-0076` | `techniques/agent-workflows/owner-layer-triage/` | `techniques/governance/decision-routing/owner-layer-triage/` |
| `AOA-T-0078` | `techniques/agent-workflows/decision-fork-cards/` | `techniques/governance/decision-routing/decision-fork-cards/` |
| `AOA-T-0079` | `techniques/agent-workflows/risk-passport-lift/` | `techniques/governance/decision-routing/risk-passport-lift/` |

## Preserved

- IDs stayed unchanged.
- `domain` stayed unchanged as `agent-workflows`.
- `kind` stayed unchanged as `assessment` for every bundle.
- `AOA-T-0076`, `AOA-T-0078`, and `AOA-T-0079` stayed `promoted`; path
  movement did not imply canonical promotion.
- Evidence, relations, checks, examples, notes, maturity, validation-strength
  metadata, and public-safety posture moved with each bundle.
- No `tree_path`, `family`, capability, substrate, execution-profile, or risk
  frontmatter was added.

## Boundary

This receipt records path accounting only.

`decision-routing` remains a governance shelf for local decision support:
owner-layer verdicts, explicit branch cards, and small route-risk passports
before action. It does not become AoA constitutional authority, `aoa-routing`
ownership, role contract law, runtime dispatch, approval policy, playbook
design, hidden automation governance, risk scoring doctrine, context-map
doctrine, neighboring governance authority, or a reason to move all remaining
`agent-workflows` leaves.

## Verification Lane

Expected validation for the migration wave:

```bash
python -m unittest tests.test_distillation_mechanics_topology tests.test_root_legacy_topology tests.test_roadmap_parity
python scripts/validate_nested_agents.py
python scripts/validate_repo.py
python scripts/release_check.py
```
