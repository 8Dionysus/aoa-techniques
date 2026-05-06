# Review-Evidence Tree Pilot Receipt

Date: 2026-05-05

## Status

Landed.

## Reviewed Source

- [Review-Evidence Direct-Read Migration Review](../../mechanics/distillation/parts/technique-reform-ingress/reviews/review-evidence-direct-read-migration-review.md)
- [Technique Tree Contract](../../docs/TECHNIQUE_TREE_CONTRACT.md)
- [Technique Reform Ingress](../../mechanics/distillation/parts/technique-reform-ingress/README.md)

## Movement

Twenty-second authored path migration:

| technique | old path | new path |
|---|---|---|
| `AOA-T-0107` | `techniques/agent-workflows/single-locus-claim-challenge/` | `techniques/proof/review-evidence/single-locus-claim-challenge/` |
| `AOA-T-0105` | `techniques/agent-workflows/single-missing-evidence-request/` | `techniques/proof/review-evidence/single-missing-evidence-request/` |
| `AOA-T-0106` | `techniques/docs/single-scoped-evidence-reference/` | `techniques/proof/review-evidence/single-scoped-evidence-reference/` |

## Preserved

- IDs stayed unchanged.
- `domain` stayed unchanged as `agent-workflows` for `AOA-T-0107` and
  `AOA-T-0105`.
- `domain` stayed unchanged as `docs` for `AOA-T-0106`.
- `kind` stayed unchanged as `guardrail` for `AOA-T-0107` and `AOA-T-0105`.
- `kind` stayed unchanged as `artifact` for `AOA-T-0106`.
- All three bundles stayed `promoted`; path movement did not imply canonical
  promotion.
- Evidence, relations, checks, examples, notes, maturity, validation-strength
  metadata, and public-safety posture moved with each bundle.
- No `tree_path`, `family`, capability, substrate, execution-profile, or risk
  frontmatter was added.

## Boundary

This receipt records path accounting only.

`review-evidence` remains a proof shelf for bounded review evidence: one
claim-locus challenge, one missing-evidence request, and one scoped evidence
reference. It does not become proof verdict authority, eval-suite ownership,
review-board workflow, Agon move law, actor eligibility, evidence adequacy
scoring, source-truth transfer, route mutation, memory write, runtime behavior,
KAG promotion, ToS canon, or skill activation.

## Verification Lane

Expected validation for the migration wave:

```bash
python -m unittest tests.test_distillation_mechanics_topology tests.test_root_legacy_topology tests.test_roadmap_parity
python scripts/validate_nested_agents.py
python scripts/validate_repo.py
python scripts/release_check.py
```
