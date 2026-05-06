# Practice-Adoption-Lifecycle Direct Relation Repair

Source packet: [Technique Reform Ingress](../README.md)

Wave packet:
[Selector Relation Wave D Governance Split Review](selector-relation-wave-d-governance-split-review.md)

Touched bundle relation:
[AOA-T-0103 adopted-practice-retention-review](../../../../../techniques/governance/practice-adoption-lifecycle/adopted-practice-retention-review/TECHNIQUE.md)

Stable route-packet target:
[AOA-T-0104 superseded-practice-obsolescence-route](../../../../../techniques/governance/practice-adoption-lifecycle/superseded-practice-obsolescence-route/TECHNIQUE.md)

Status: accepted direct relation repair.

## Verdict

Accept `AOA-T-0103 used_together_for AOA-T-0104`.

`AOA-T-0103` owns the current-evidence retention review for one adopted or
shadowed practice. One of its explicit outcomes is `route_to_obsolescence`,
with rollback, quarantine, or obsolescence route posture kept visible.

`AOA-T-0104` owns the route packet that can follow that outcome: supersede,
merge, reanchor, defer, drop, or deprecation review, with owner receipt, source
evidence, rollback or quarantine posture, and retained lesson preserved.

That makes `used_together_for AOA-T-0104` clearer than leaving no outgoing
edge from the retention review. It remains intentionally weaker than
`requires`: retention can end in retain, revise, quarantine, or defer, and
obsolescence pressure can also come from an equivalent owner review.

## Decision Table

| bundle | old edge | new edge | reason |
|---|---|---|---|
| `AOA-T-0103` | no direct edge to `AOA-T-0104` | `used_together_for AOA-T-0104` | `route_to_obsolescence` is a retention verdict and `AOA-T-0104` owns the bounded route packet that may follow it |

## Holds

| bundle | held relation posture | why |
|---|---|---|
| `AOA-T-0101` | keep `complements AOA-T-0076` and `complements AOA-T-0090` | local adoption benefits from owner placement and adjacent-target clarity, but it owns consent, compatibility, rollback, and retention watch |
| `AOA-T-0103` | keep `complements AOA-T-0101` | retention needs an adoption or shadow-use record, not necessarily this exact adoption-gate technique |
| `AOA-T-0103` | keep `complements AOA-T-0090` | nearest-wrong rejection can clarify retention choices without becoming the retention verdict |
| `AOA-T-0104` | keep `used_together_for AOA-T-0103` instead of `requires AOA-T-0103` | obsolescence routing normally follows retention, but another owner review may provide equivalent obsolescence pressure |
| `AOA-T-0104` | keep `complements AOA-T-0090` and `complements AOA-T-0076` | owner-target clarity supports the route packet without replacing owner receipt or retained-lesson posture |

## What Changed

- `AOA-T-0103` frontmatter now has a direct
  `used_together_for AOA-T-0104` relation.
- Generated relation consumers should be rebuilt from source after this repair:
  catalog, selection surfaces, topology scout, KAG export, and release-check
  companions that derive from catalog or frontmatter.

## What Did Not Change

- no new relation types;
- no relation schema migration;
- no relation rationale field;
- no generated graph behavior, traversal, ranking, or selector engine;
- no status, `domain`, `kind`, maturity, validation-strength, evidence, owner,
  or path changes;
- no canonical promotion;
- no empirical small-agent proof or `aoa-evals` verdict.

## Safety Read

This repair strengthens only a bounded operating path:

- retention review can output `route_to_obsolescence`;
- obsolescence routing owns the follow-up route packet.

It does not say adoption is permanent, obsolescence is deletion, route packets
are deprecation execution, retained lessons are memory truth, or a governance
shelf owns Method-growth law, skill activation, route mutation, proof verdicts,
or runtime behavior.

## Stop Lines

- Do not use this repair as precedent for adding future lifecycle relation
  names to frontmatter.
- Do not strengthen `AOA-T-0104` to `requires AOA-T-0103`.
- Do not collapse `adoption`, `retention`, and `obsolescence` into one broad
  Method-growth technique.
- Do not hand-edit generated surfaces. Rebuild them from source.
- Do not treat this as a relation conclusion for remaining continuity,
  recovery, history, ingest, or singleton shelves.

## Next Honest Move

Rebuild generated relation consumers, validate the repository, and land
Wave D.

After Wave D lands, continue the temporary plan with Wave E over continuity
and recovery shelves.

