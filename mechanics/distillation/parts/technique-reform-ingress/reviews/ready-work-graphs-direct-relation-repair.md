# Ready-Work-Graphs Direct Relation Repair

Source packet: [Technique Reform Ingress](../README.md)

Wave packet:
[Selector Relation Wave A Proof Execution Review](selector-relation-wave-a-proof-execution-review.md)

Touched bundle relation:
[AOA-T-0050 ready-work-from-blocker-graph](../../../../../techniques/execution/ready-work-graphs/ready-work-from-blocker-graph/TECHNIQUE.md)

Stable graph target:
[AOA-T-0049 dependency-aware-task-graph](../../../../../techniques/execution/ready-work-graphs/dependency-aware-task-graph/TECHNIQUE.md)

Status: accepted direct relation repair.

## Verdict

Accept `AOA-T-0050 requires AOA-T-0049`.

`AOA-T-0049` owns the local dependency graph contract: explicit task nodes,
dependency or blocker edges, visible blocked reasons, and a recomputable ready
frontier from graph state.

`AOA-T-0050` does not merely sit near that graph contract. Its inputs and
contracts assume an existing dependency or blocker graph before it can derive a
ready queue. The source bundle explicitly says it owns the derived ready queue
over an existing blocker graph and does not own graph authoring itself.

That makes `requires AOA-T-0049` clearer and less misleading than
`complements AOA-T-0049`.

## Decision Table

| bundle | old edge | new edge | reason |
|---|---|---|---|
| `AOA-T-0050` | `complements AOA-T-0049` | `requires AOA-T-0049` | ready-work queue derivation needs an existing blocker/dependency graph contract |

## Holds

| bundle | held relation posture | why |
|---|---|---|
| `AOA-T-0049` | keep `complements AOA-T-0001` | the graph helps bounded execution workflow but does not require the full plan/diff/apply/verify/report protocol |
| `AOA-T-0050` | keep `complements AOA-T-0001` | the derived queue helps choose a later execution slice without requiring that exact workflow as a source object |
| `AOA-T-0055` | keep `complements AOA-T-0001` | the requirements/design/tasks ladder prepares later implementation, but it does not require the execution protocol to exist first |
| `AOA-T-0055` | no direct edge to `AOA-T-0049` or `AOA-T-0050` | it is a planning ladder and should not be collapsed into graph authoring or ready-frontier derivation |

## What Changed

- `AOA-T-0050` frontmatter relation changed from `complements AOA-T-0049` to
  `requires AOA-T-0049`.
- Generated relation consumers should be rebuilt from source after this repair:
  catalog, selection surfaces, topology scout, and release-check companions
  that derive from catalog or frontmatter.

## What Did Not Change

- no new relation types;
- no relation schema migration;
- no relation rationale field;
- no generated graph behavior, traversal, ranking, or selector engine;
- no status, `domain`, `kind`, maturity, validation-strength, evidence, owner,
  or path changes;
- no empirical small-agent proof or `aoa-evals` verdict.

## Safety Read

This repair strengthens only object dependency:

- ready queue derivation needs a blocker/dependency graph;
- `AOA-T-0049` is the local reusable graph-contract technique.

It does not say the graph is a project-management system, memory substrate,
knowledge graph, scheduling engine, staffing policy, ranking policy, dispatch
platform, or proof of work readiness. It does not say `AOA-T-0050` performs the
work it selects.

## Stop Lines

- Do not add `follows`, `produces-input-for`, `consumes-output-of`, or other
  future relation names to frontmatter from this repair.
- Do not strengthen `AOA-T-0055` into a graph prerequisite or graph consumer.
- Do not change `AOA-T-0049` to require `AOA-T-0055`; graph authoring can exist
  without the planning ladder.
- Do not hand-edit generated surfaces. Rebuild them from source.
- Do not treat this as a relation conclusion for the remaining long-pass
  shelves.

## Next Honest Move

Rebuild generated relation consumers, validate the repository, and land Wave A.

After Wave A lands, continue the temporary plan with Wave B over instruction
and knowledge-lift shelves.

