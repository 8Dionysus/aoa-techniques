# Agent-Workflows-Core Tree Pilot Receipt

Date: 2026-05-05

## Status

Landed.

## Reviewed Source

- [Agent-Workflows-Core Direct-Read Migration Review](../../mechanics/distillation/parts/technique-reform-ingress/reviews/agent-workflows-core-direct-read-migration-review.md)
- [Technique Tree Contract](../../docs/TECHNIQUE_TREE_CONTRACT.md)
- [Technique Reform Ingress](../../mechanics/distillation/parts/technique-reform-ingress/README.md)

## Movement

Eighteenth authored path migration:

| technique | old path | new path |
|---|---|---|
| `AOA-T-0001` | `techniques/agent-workflows/plan-diff-apply-verify-report/` | `techniques/execution/agent-workflows-core/plan-diff-apply-verify-report/` |
| `AOA-T-0014` | `techniques/agent-workflows/tdd-slice/` | `techniques/execution/agent-workflows-core/tdd-slice/` |
| `AOA-T-0023` | `techniques/agent-workflows/stateless-single-shot-agent/` | `techniques/execution/agent-workflows-core/stateless-single-shot-agent/` |
| `AOA-T-0028` | `techniques/agent-workflows/confirmation-gated-mutating-action/` | `techniques/execution/agent-workflows-core/confirmation-gated-mutating-action/` |
| `AOA-T-0031` | `techniques/agent-workflows/shell-composable-agent-invocation/` | `techniques/execution/agent-workflows-core/shell-composable-agent-invocation/` |

## Preserved

- IDs stayed unchanged.
- `domain` stayed unchanged as `agent-workflows`.
- `kind` stayed unchanged for every bundle.
- `AOA-T-0001`, `AOA-T-0014`, `AOA-T-0023`, `AOA-T-0028`, and
  `AOA-T-0031` stayed `canonical`.
- `AOA-T-0028` stayed `kind: guardrail`.
- `AOA-T-0031` stayed `kind: composition`.
- Evidence, relations, checks, examples, notes, maturity, validation-strength
  metadata, and public-safety posture moved with each bundle.
- No `tree_path`, `family`, capability, substrate, execution-profile, or risk
  frontmatter was added.

## Boundary

This receipt records path accounting only.

`agent-workflows-core` remains a technique shelf for visible, bounded,
reviewable agent work: planning, slicing, single-shot invocation, explicit
confirmation, shell-visible composition, validation, and stop points. It does
not become generic agent doctrine, shell policy, product policy, approval
policy, autonomous orchestration, hidden agent scheduling, runtime lifecycle
law, broad methodology doctrine, or a reason to move all remaining
`agent-workflows` leaves.

## Verification Lane

Expected validation for the migration wave:

The archived route covered its targeted owner checks and repository validation lanes.
