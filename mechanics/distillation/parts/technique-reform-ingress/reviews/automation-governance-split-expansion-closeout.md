# Automation-Governance Split Expansion Closeout

Source packet:
[Technique Reform Ingress](../README.md)

Split review:
[Automation-Governance Direct-Read Split Review](automation-governance-direct-read-split-review.md)

Generated lens:
[Technique Tree Projection](../../../../../reports/technique_tree_projection.md)

Tree contract:
[Technique Tree Contract](../../../../../docs/TECHNIQUE_TREE_CONTRACT.md)

Status: split-expanded, no path migration, not `tree_path` frontmatter.

## Verdict

Close the bulk `governance/automation-governance` route as rejected and expand
the remaining migration lane into three split candidates.

No technique bundle moves in this closeout. The purpose is route control: the
direct-read split review proved that one nine-leaf shelf would hide three
different governance questions, so the next migration work must proceed by
smaller candidate shelves.

## Activated Split Sequence

| order | candidate shelf | techniques | current paths | next action |
|---|---|---|---|---|
| A | `governance/automation-readiness` | `AOA-T-0086`, `AOA-T-0087`, `AOA-T-0088` | `techniques/agent-workflows/automation-fit-matrix/`, `techniques/agent-workflows/human-loop-to-first-landing/`, `techniques/agent-workflows/approval-sensitivity-check/` | direct-read review before any movement |
| B | `governance/promotion-boundary` | `AOA-T-0089`, `AOA-T-0090`, `AOA-T-0102` | `techniques/agent-workflows/quest-unit-promotion-review/`, `techniques/agent-workflows/nearest-wrong-target-rejection/`, `techniques/agent-workflows/skill-proposal-handoff-packet/` | wait until Candidate A lands or is held |
| C | `governance/practice-adoption-lifecycle` | `AOA-T-0101`, `AOA-T-0103`, `AOA-T-0104` | `techniques/agent-workflows/local-pattern-adoption-gate/`, `techniques/agent-workflows/adopted-practice-retention-review/`, `techniques/agent-workflows/superseded-practice-obsolescence-route/` | wait until Candidate B lands or is held |

## Why Candidate A Goes First

`automation-readiness` is the smallest and most directly automation-facing
split. It starts before promotion, adoption, retention, or obsolescence:
classify whether one recurring route has automation fit, choose the first
honest automation-facing landing, then surface checkpoint burden when approval
or rollback posture is too heavy. It can be reviewed and migrated without
deciding the later quest-promotion, skill-proposal, or Method-growth adoption
tail.

## Route Effects

- The `automation-governance` name remains a reviewed pressure label from the
  generated projection and split review, not a bulk shelf path.
- Candidate shelves may live under `techniques/governance/` if their direct
  reviews accept them.
- Current `domain: agent-workflows` and current `kind` values remain the
  authoritative frontmatter for all nine bundles until and unless a separate
  frontmatter reform happens later.
- The reserved split steps are now active in order: Candidate A review,
  Candidate A migration, Candidate A landed review, Candidate B review,
  Candidate B migration or hold, Candidate B landed review or hold closeout,
  Candidate C review, Candidate C migration or hold, Candidate C landed review
  or hold closeout.

## Stop Lines

- Do not move files from this closeout.
- Do not add `tree_path`, `family`, capability, substrate, execution-profile,
  or risk frontmatter.
- Do not treat split candidate names as canonical frontmatter.
- Do not treat Candidate A review as acceptance of Candidate B or Candidate C.
- Do not treat `automation-readiness` as automation policy authority, seed
  canon, implementation approval, scheduler doctrine, hidden automation
  governance, or runtime behavior.
- Do not treat `promotion-boundary` as skill acceptance, skill activation,
  quest/playbook promotion doctrine, role contract law, proof verdict, memory
  write, or routing policy.
- Do not treat `practice-adoption-lifecycle` as Method-growth law, local owner
  consent, deletion, deprecation execution, proof authority, memory truth,
  skill activation, route mutation, runtime change, or permanent practice
  retention.

## Next Honest Move

Run a direct-read review for Candidate A:
`governance/automation-readiness`.

Read `AOA-T-0086`, `AOA-T-0087`, and `AOA-T-0088` directly, including
support files, canonical readiness notes, relation edges, current
`agent-workflows` and `governance` route cards, and the split review before
any twenty-fifth shelf movement.
