# Donor-Harvest Tree Pilot Receipt

Date: 2026-05-05

## Status

Landed.

## Reviewed Source

- [Donor-Harvest Direct-Read Migration Review](../../mechanics/distillation/parts/technique-reform-ingress/reviews/donor-harvest-direct-read-migration-review.md)
- [Technique Tree Contract](../../docs/TECHNIQUE_TREE_CONTRACT.md)
- [Technique Reform Ingress](../../mechanics/distillation/parts/technique-reform-ingress/README.md)

## Movement

Nineteenth authored path migration:

| technique | old path | new path |
|---|---|---|
| `AOA-T-0075` | `techniques/agent-workflows/session-donor-harvest/` | `techniques/continuity/donor-harvest/session-donor-harvest/` |
| `AOA-T-0077` | `techniques/agent-workflows/harvest-packet-contract/` | `techniques/continuity/donor-harvest/harvest-packet-contract/` |
| `AOA-T-0084` | `techniques/agent-workflows/progression-evidence-lift/` | `techniques/continuity/donor-harvest/progression-evidence-lift/` |
| `AOA-T-0085` | `techniques/agent-workflows/multi-axis-quest-overlay/` | `techniques/continuity/donor-harvest/multi-axis-quest-overlay/` |

## Preserved

- IDs stayed unchanged.
- `domain` stayed unchanged as `agent-workflows`.
- `kind` stayed unchanged for every bundle.
- `AOA-T-0075`, `AOA-T-0077`, `AOA-T-0084`, and `AOA-T-0085` stayed
  `promoted`; path movement did not imply canonical promotion.
- `AOA-T-0077` stayed `kind: handoff`.
- `AOA-T-0075`, `AOA-T-0084`, and `AOA-T-0085` stayed `kind: lift`.
- Evidence, relations, checks, examples, notes, maturity, validation-strength
  metadata, and public-safety posture moved with each bundle.
- No `tree_path`, `family`, capability, substrate, execution-profile, or risk
  frontmatter was added.

## Boundary

This receipt records path accounting only.

`donor-harvest` remains a continuity shelf for reviewed-session donor packs,
harvest-packet contracts, progression evidence deltas, and adjunct quest
overlays that survive a session boundary as inspectable evidence. It does not
become memory authority, playbook quest authority, progression doctrine, owner
routing, role progression, stats ownership, session-closeout automation,
neighboring continuity or governance authority, or a reason to move all
remaining `agent-workflows` leaves.

## Verification Lane

Expected validation for the migration wave:

```bash
python -m unittest tests.test_distillation_mechanics_topology tests.test_root_legacy_topology tests.test_roadmap_parity
python scripts/validate_nested_agents.py
python scripts/validate_repo.py
python scripts/release_check.py
```
