# Approval-Evidence Tree Pilot Receipt

Date: 2026-05-05

## Status

Landed.

## Reviewed Source

- [Approval-Evidence Direct-Read Migration Review](../../mechanics/distillation/parts/technique-reform-ingress/reviews/approval-evidence-direct-read-migration-review.md)
- [Technique Tree Contract](../../docs/TECHNIQUE_TREE_CONTRACT.md)
- [Technique Reform Ingress](../../mechanics/distillation/parts/technique-reform-ingress/README.md)

## Movement

Twenty-first authored path migration:

| technique | old path | new path |
|---|---|---|
| `AOA-T-0068` | `techniques/agent-workflows/fail-closed-evidence-gate/` | `techniques/governance/approval-evidence/fail-closed-evidence-gate/` |
| `AOA-T-0069` | `techniques/agent-workflows/approval-bound-durable-jobs/` | `techniques/governance/approval-evidence/approval-bound-durable-jobs/` |

## Preserved

- IDs stayed unchanged.
- `domain` stayed unchanged as `agent-workflows`.
- `kind` stayed unchanged as `guardrail` for `AOA-T-0068`.
- `kind` stayed unchanged as `handoff` for `AOA-T-0069`.
- `AOA-T-0068` and `AOA-T-0069` stayed `promoted`; path movement did not
  imply canonical promotion.
- Evidence, relations, checks, examples, notes, maturity, validation-strength
  metadata, and public-safety posture moved with each bundle.
- No `tree_path`, `family`, capability, substrate, execution-profile, or risk
  frontmatter was added.

## Boundary

This receipt records path accounting only.

`approval-evidence` remains a governance shelf for approval-shaped boundary
evidence: one fail-closed execution gate and one durable approval seam. It does
not become approval policy, security framework authority, trust-platform
semantics, runtime job-runner ownership, scheduler doctrine, queue-product
ownership, broad orchestration governance, proof-verdict authority, or a reason
to move all remaining `agent-workflows` leaves.

## Verification Lane

Expected validation for the migration wave:

The archived route covered its targeted owner checks and repository validation lanes.
