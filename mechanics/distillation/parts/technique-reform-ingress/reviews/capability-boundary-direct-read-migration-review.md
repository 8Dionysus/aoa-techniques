# Capability-Boundary Direct-Read Migration Review

Source packet:
[Technique Reform Ingress](../README.md)

Preceding landed review:
[Landed Capability-Registry Pilot Review](landed-capability-registry-pilot-review.md)

Generated lens:
[Technique Tree Projection](../../../../../reports/technique_tree_projection.md)

Tree contract:
[Technique Tree Contract](../../../../../docs/TECHNIQUE_TREE_CONTRACT.md)

Status: accepted-for-ninth-migration-pilot, not path migration, not
`tree_path` frontmatter.

## Verdict

Accept `capability-boundary` as the ninth bounded tree migration pilot.

Direct reading confirms that `AOA-T-0040`, `AOA-T-0043`, and `AOA-T-0093`
form one browseable instruction-side shelf: each leaf prevents a
capability-like object from gaining false authority at a boundary. One
separates reusable skill meaning from command invocation, one keeps primary
source input visible before bridge use, and one separates semantic
recommendation truth from current host actionability.

The shelf is cross-domain today, but the move tests the tree contract rather
than frontmatter ownership. `domain: docs` and `domain: agent-workflows` remain
true for their current review lanes. The proposed path answers a browsing
question: where should a reader find compact guardrails that keep capability
meaning, source priority, recommendation truth, and executable action from
collapsing into each other?

This review does not move files. It only authorizes a later migration wave to
move exactly these three bundles into
`techniques/instruction/capability-boundary/` if that wave also updates route
cards, root legacy receipts, authored links, generated surfaces, and
validation.

## Sources Read

- [AOA-T-0040 skill-vs-command-boundary](../../../../../techniques/instruction/capability-boundary/skill-vs-command-boundary/TECHNIQUE.md)
- [AOA-T-0040 checklist](../../../../../techniques/instruction/capability-boundary/skill-vs-command-boundary/checks/skill-vs-command-boundary-checklist.md)
- [AOA-T-0040 minimal example](../../../../../techniques/instruction/capability-boundary/skill-vs-command-boundary/examples/minimal-skill-vs-command-boundary.md)
- [AOA-T-0040 evidence notes](../../../../../techniques/instruction/capability-boundary/skill-vs-command-boundary/notes/canonical-readiness.md)
- [AOA-T-0043 multi-source-primary-input-provenance](../../../../../techniques/instruction/capability-boundary/multi-source-primary-input-provenance/TECHNIQUE.md)
- [AOA-T-0043 checklist](../../../../../techniques/instruction/capability-boundary/multi-source-primary-input-provenance/checks/multi-source-primary-input-provenance-checklist.md)
- [AOA-T-0043 minimal example](../../../../../techniques/instruction/capability-boundary/multi-source-primary-input-provenance/examples/minimal-multi-source-primary-input-provenance.md)
- [AOA-T-0043 evidence notes](../../../../../techniques/instruction/capability-boundary/multi-source-primary-input-provenance/notes/canonical-readiness.md)
- [AOA-T-0093 recommendation-truth-vs-host-actionability](../../../../../techniques/instruction/capability-boundary/recommendation-truth-vs-host-actionability/TECHNIQUE.md)
- [AOA-T-0093 checklist](../../../../../techniques/instruction/capability-boundary/recommendation-truth-vs-host-actionability/checks/recommendation-truth-vs-host-actionability-checklist.md)
- [AOA-T-0093 minimal example](../../../../../techniques/instruction/capability-boundary/recommendation-truth-vs-host-actionability/examples/minimal-recommendation-truth-vs-host-actionability.md)
- [AOA-T-0093 evidence notes](../../../../../techniques/instruction/capability-boundary/recommendation-truth-vs-host-actionability/notes/canonical-readiness.md)
- [Docs route card](../../../../../techniques/docs/AGENTS.md)
- [Agent-workflows route card](../../../../../techniques/agent-workflows/AGENTS.md)
- [Instruction route card](../../../../../techniques/instruction/AGENTS.md)
- [AOA-T-0041 skill-marketplace-curation](../../../../../techniques/docs/skill-marketplace-curation/TECHNIQUE.md)
- [AOA-T-0042 upstream-skill-health-checking](../../../../../techniques/evaluation/upstream-skill-health-checking/TECHNIQUE.md)
- [Technique family scout rows for `capability-boundary` and
  `skill-discovery`](../../../../../reports/technique_family_scout.md)
- [Technique topology scout rows for `capability-boundary`](../../../../../reports/technique_topology_scout.md)
- [Technique tree projection rows for `capability-boundary` and
  `skill-discovery`](../../../../../reports/technique_tree_projection.md)
- [Landed capability-registry pilot review](landed-capability-registry-pilot-review.md)

## Direct Bundle Read

| technique | current path | domain | kind | direct-read result |
|---|---|---|---|---|
| `AOA-T-0040` | `techniques/docs/skill-vs-command-boundary/` | `docs` | `guardrail` | keeps reusable skill capability separate from command invocation, arguments, output shape, routing, marketplace, and shell doctrine |
| `AOA-T-0043` | `techniques/docs/multi-source-primary-input-provenance/` | `docs` | `guardrail` | keeps one primary source input visible against supporting inputs without becoming graph traversal, ranking, relation semantics, or bridge architecture |
| `AOA-T-0093` | `techniques/agent-workflows/recommendation-truth-vs-host-actionability/` | `agent-workflows` | `guardrail` | keeps router recommendation truth visible while host-executable action stays separately annotated and bounded |

All three are promoted guardrails with source-backed evidence. That matters:
this shelf is not mixing move kinds. It is mixing owner lanes around one
capability-boundary question.

## Why The Shelf Holds

- `AOA-T-0040` protects the boundary between reusable capability meaning and
  user-facing invocation.
- `AOA-T-0043` protects the boundary between primary source authority and
  supporting context before a downstream bridge, summary, or selector depends
  on the combined surface.
- `AOA-T-0093` protects the boundary between semantic recommendation and what
  the current host can actually execute.
- The examples all keep the boundary visible in compact artifacts rather than
  hiding it in generated metadata or local runtime assumptions.
- The checklists all reject neighboring authority: routing policy,
  marketplace curation, graph semantics, registry doctrine, upstream-health
  validation, and runtime execution law.
- The canonical-readiness notes keep all three bundles promoted, not
  canonical, which fits a migration pilot: path clarity can improve without
  claiming default-use status.

## Instruction Trunk Fit

`instruction/` is the better trunk because the shelf shapes the instruction
surfaces that tell an agent or human what a capability-like object means and
what it does not authorize.

This does not turn the three leaves into prompt doctrine. The path is useful
because it gathers boundary guardrails around capability meaning:

- skill artifacts can be reused without becoming command wrappers
- primary source inputs can stay visible before synthesis or selection
- recommendation reports can preserve relevance without pretending unavailable
  actions are runnable

Keeping `AOA-T-0093` in `agent-workflows` was reasonable before the tree
started landing, because its procedure is a control-plane workflow guardrail.
Moving it under `instruction/capability-boundary/` would be a path-architecture
choice only: it should keep `domain: agent-workflows`, `kind: guardrail`,
status, ID, relations, and evidence unchanged.

## Boundary Watch Accepted

The generated projection was right to mark this shelf `boundary-watch`.
Capability boundary language is easy to overgrow. Direct reading accepts the
shelf only because all three leaves repeatedly refuse adjacent authority:

- no skill marketplace curation
- no upstream health validation
- no routing policy or recommendation ranking
- no KAG graph semantics or bridge architecture doctrine
- no runtime execution doctrine or host inventory policy
- no registry product doctrine or capability-spec ownership
- no command product design, shell-command doctrine, or agent-role authority

That makes the shelf viable, but it also makes the later migration stop-lines
important.

## Proposed Move

Move exactly these three bundles in the migration wave:

| technique | current path | proposed path |
|---|---|---|
| `AOA-T-0040` | `techniques/docs/skill-vs-command-boundary/` | `techniques/instruction/capability-boundary/skill-vs-command-boundary/` |
| `AOA-T-0043` | `techniques/docs/multi-source-primary-input-provenance/` | `techniques/instruction/capability-boundary/multi-source-primary-input-provenance/` |
| `AOA-T-0093` | `techniques/agent-workflows/recommendation-truth-vs-host-actionability/` | `techniques/instruction/capability-boundary/recommendation-truth-vs-host-actionability/` |

Keep `domain`, `kind`, status, IDs, evidence, relations, and public-safety
posture unchanged.

## Migration Blast Radius

A later migration wave should expect to update:

- authored links from `AOA-T-0093` to its evaluation, capability-discovery,
  and agent-workflow siblings
- authored links into `AOA-T-0040` and `AOA-T-0043` from selection, handoff,
  proof, and KAG-derived reader surfaces
- `techniques/instruction/AGENTS.md` current scope and domain rules, because
  `instruction/` would gain a fourth landed shelf
- root `legacy/receipts/` and `legacy/INDEX.md` accounting for the authored
  path migration
- generated catalogs, capsules, manifests, reports, KAG exports, docs readers,
  and source-lift surfaces after the path move
- active mechanics review rows that still point to old homes
- release-check output touched by regenerated indexes and reports

Do not create mechanic-style `parts/` packages or shelf READMEs for these
technique leaves.

## Why Not Neighbor Shelves In This Wave

`skill-discovery` should wait. Direct reading confirms that
`AOA-T-0041` is editorial marketplace curation and `AOA-T-0042` is upstream
source-readiness validation. They are near this shelf, but they answer what can
be discovered or surfaced, not where capability meaning and actionability stop.

Proof, governance, runtime, owner-closeout, and automation-governance shelves
should also wait. They carry stronger verdict, approval, execution, or owner
truth pressure than this instruction-side boundary pilot needs.

## Stop Lines

- Do not move files from this review pack alone.
- Do not add `tree_path`, `family`, capability, substrate, execution-profile,
  or risk frontmatter.
- Do not move `skill-discovery`, proof, governance, runtime, owner-closeout,
  automation-governance, or other capability-adjacent shelves in the same wave.
- Do not turn `capability-boundary` into skill marketplace curation, upstream
  health validation, routing policy, recommendation ranking, KAG graph
  semantics, bridge architecture doctrine, runtime execution doctrine, host
  inventory policy, command product design, shell doctrine, registry product
  doctrine, or agent-role authority.
- Do not collapse the three leaves into one mega-technique; the shelf holds
  because skill-command ownership, source-input priority, and
  recommendation-actionability stay distinct.
- Do not change canonical/promoted status, maturity, evidence, or
  public-safety posture during the path migration.
- Keep generated projection weaker than authored bundle meaning.

## Next Honest Move

Run the ninth pilot migration.

Move exactly `AOA-T-0040`, `AOA-T-0043`, and `AOA-T-0093` into
`techniques/instruction/capability-boundary/`; add the compact
`capability-boundary/` shelf scope to `techniques/instruction/AGENTS.md`;
preserve a root `legacy/receipts/` migration receipt; repair authored links;
rebuild generated surfaces; and validate with the narrow tree-pilot tests plus
`python scripts/release_check.py`.
