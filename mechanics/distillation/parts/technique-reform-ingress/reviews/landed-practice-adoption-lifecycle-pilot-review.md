# Landed Practice-Adoption-Lifecycle Pilot Review

Source packet:
[Technique Reform Ingress](../README.md)

Migration receipt:
[Practice-Adoption-Lifecycle Tree Pilot Receipt](../../../../../legacy/receipts/2026-05-05-practice-adoption-lifecycle-tree-pilot.md)

Previous review:
[Practice-Adoption-Lifecycle Direct-Read Migration Review](practice-adoption-lifecycle-direct-read-migration-review.md)

Split closeout:
[Automation-Governance Split Expansion Closeout](automation-governance-split-expansion-closeout.md)

Tree contract:
[Technique Tree Contract](../../../../../docs/TECHNIQUE_TREE_CONTRACT.md)

Generated lens:
[Technique Tree Projection](../reports/technique_tree_projection.md)

Status: pilot-validated, split-tail-closed, no path migration, not `tree_path`
frontmatter.

## Verdict

The landed `governance/practice-adoption-lifecycle` shelf holds.

The migration made the three leaves easier to find without changing their
meaning. `AOA-T-0101`, `AOA-T-0103`, and `AOA-T-0104` still carry
`domain: agent-workflows` and `status: promoted`, while preserving their
separate `kind` values: `guardrail`, `assessment`, and `handoff`. The shelf
now says what the direct-read review proved: these are governance-facing moves
for local practice adoption, retention, and obsolescence posture before an
owner surface treats a practice as durable, still active, or ready for
owner-routed review.

The shelf does not create Method-growth law, local owner consent, deletion,
deprecation execution, proof authority, memory truth, skill activation, route
mutation, runtime change, permanent practice retention, sibling owner
acceptance, KAG promotion, ToS canon, broad orchestration governance, or
acceptance of the queued `tool-use/tool-gateway` singleton hold.

## Post-Migration Evidence

| technique | landed path | preserved posture |
|---|---|---|
| `AOA-T-0101` | `techniques/governance/practice-adoption-lifecycle/local-pattern-adoption-gate/` | `domain: agent-workflows`, `kind: guardrail`, `status: promoted` |
| `AOA-T-0103` | `techniques/governance/practice-adoption-lifecycle/adopted-practice-retention-review/` | `domain: agent-workflows`, `kind: assessment`, `status: promoted` |
| `AOA-T-0104` | `techniques/governance/practice-adoption-lifecycle/superseded-practice-obsolescence-route/` | `domain: agent-workflows`, `kind: handoff`, `status: promoted` |

## What Improved

- `techniques/governance/AGENTS.md` now names
  `practice-adoption-lifecycle/` as a bounded shelf without importing
  Method-growth law or owner-local retirement authority.
- `techniques/agent-workflows/AGENTS.md` now has one remaining representative:
  `mcp-gateway-proxy`.
- Active adjacent links now resolve to the moved practice lifecycle leaves and
  to already-landed `decision-routing`, `promotion-boundary`, and Method-growth
  mechanics anchors.
- The generated tree projection no longer has `split-review-needed` rows; the
  old `automation-governance` label remains only scout lineage over three
  landed governance shelves.

## Automation Split Accounting

| split | shelf | techniques | result |
|---|---|---|---|
| A | `governance/automation-readiness` | `AOA-T-0086`, `AOA-T-0087`, `AOA-T-0088` | landed |
| B | `governance/promotion-boundary` | `AOA-T-0089`, `AOA-T-0090`, `AOA-T-0102` | landed |
| C | `governance/practice-adoption-lifecycle` | `AOA-T-0101`, `AOA-T-0103`, `AOA-T-0104` | landed |

No projected automation-governance ID remains unaccounted. The rejected bulk
`governance/automation-governance` shelf stays rejected; its useful remnant is
the evidence that the governance trunk needed three smaller shelves instead of
one broad automation bucket.

## Watch Lines

- `AOA-T-0101` can still drift into generic owner approval if one local
  behavior surface and rollback or quarantine posture are not named.
- `AOA-T-0103` can still drift into permanent retention if current evidence,
  owner fit, support cost, and next review posture are not checked.
- `AOA-T-0104` can still drift into deletion or deprecation execution if the
  owner receipt target, source evidence, and retained lesson disappear.
- Method-growth remains provenance and lifecycle context, not imported law
  inside this technique shelf.
- `tool-use/tool-gateway` remains a singleton hold, not a migration accepted by
  this review.

## Next Honest Move

Run the direct-read singleton review for `tool-use/tool-gateway`.

Read `AOA-T-0065 mcp-gateway-proxy`, its support files, the singleton-hold
projection row, the current `agent-workflows` route card, and the future
`tool-use` trunk contract before deciding whether the gateway can become an
acceptable singleton shelf, should remain held until a neighbor/import lands,
or needs a narrower route. Do not move files in the review step.
