# Landed Capability-Registry Pilot Review

Source packet:
[Technique Reform Ingress](../README.md)

Migration review:
[Capability-Registry Direct-Read Migration Review](capability-registry-direct-read-migration-review.md)

Migration receipt:
[Capability-Registry Tree Pilot Receipt](../../../../../legacy/receipts/2026-05-04-capability-registry-tree-pilot.md)

Generated lens:
[Technique Tree Projection](../../../../../reports/technique_tree_projection.md)

Tree contract:
[Technique Tree Contract](../../../../../docs/TECHNIQUE_TREE_CONTRACT.md)

Status: pilot-validated, choose `capability-boundary` for direct-read migration
review, not path migration, not `tree_path` frontmatter.

## Verdict

Accept the landed `capability-registry` pilot as a successful eighth tree
migration and the third successful shelf under the `instruction` trunk.

The shelf stayed legible after landing. Three docs-domain techniques now sit
under one capability-registry neighborhood, while IDs, `domain`, `kind`,
status, evidence, notes, examples, checks, relations, and public-safety posture
stayed unchanged. The move improved browsing without turning capability specs,
registry-facing entries, and bounded lookup into registry product doctrine,
discovery ranking, trust policy, marketplace curation, graph semantics,
runtime resolution, skill acceptance, or agent-role authority.

This review does not move another shelf. It confirms that the next honest tree
slice should run a direct-read review for `capability-boundary`, because the
instruction trunk has now held instruction surfaces, document boundaries, and a
capability registry chain. The next pressure should test whether skill-command
ownership, primary input provenance, and recommendation-vs-host-actionability
form one bounded capability-boundary shelf without importing marketplace
curation, upstream-health validation, routing policy, KAG graph semantics, or
runtime execution doctrine.

## Sources Read

- [AOA-T-0025 capability-spec-versioning](../../../../../techniques/instruction/capability-registry/capability-spec-versioning/TECHNIQUE.md)
- [AOA-T-0063 versioned-agent-registry-contract](../../../../../techniques/instruction/capability-registry/versioned-agent-registry-contract/TECHNIQUE.md)
- [AOA-T-0064 capability-discovery](../../../../../techniques/instruction/capability-registry/capability-discovery/TECHNIQUE.md)
- [AOA-T-0040 skill-vs-command-boundary](../../../../../techniques/instruction/capability-boundary/skill-vs-command-boundary/TECHNIQUE.md)
- [AOA-T-0043 multi-source-primary-input-provenance](../../../../../techniques/instruction/capability-boundary/multi-source-primary-input-provenance/TECHNIQUE.md)
- [AOA-T-0093 recommendation-truth-vs-host-actionability](../../../../../techniques/instruction/capability-boundary/recommendation-truth-vs-host-actionability/TECHNIQUE.md)
- [AOA-T-0041 skill-marketplace-curation](../../../../../techniques/instruction/skill-discovery/skill-marketplace-curation/TECHNIQUE.md)
- [AOA-T-0042 upstream-skill-health-checking](../../../../../techniques/instruction/skill-discovery/upstream-skill-health-checking/TECHNIQUE.md)
- [Instruction route card](../../../../../techniques/instruction/AGENTS.md)
- [Docs route card](../../../../../techniques/docs/AGENTS.md)
- [Root legacy index](../../../../../legacy/INDEX.md)
- [Capability-registry tree pilot receipt](../../../../../legacy/receipts/2026-05-04-capability-registry-tree-pilot.md)
- [Technique tree projection rows for `capability-registry`,
  `capability-boundary`, and `skill-discovery`](../../../../../reports/technique_tree_projection.md)
- [Landed docs-boundary pilot review](landed-docs-boundary-pilot-review.md)
- `python scripts/release_check.py` result recorded in the migration receipt

## Landed Shape Read

| check | result | reading |
|---|---|---|
| current path | `techniques/instruction/capability-registry/` | the active path now matches the projected trunk and shelf |
| frontmatter truth | unchanged | all three leaves keep `domain: docs`; `kind` remains `artifact` or `discovery` as authored |
| route card | present | `techniques/instruction/AGENTS.md` now names `instruction-surface/`, `docs-boundary/`, and `capability-registry/` without becoming registry doctrine |
| root legacy | receipt only | active bundles moved directly between authored homes; `legacy/` preserves accounting |
| generated surfaces | rebuilt | catalogs, capsules, manifests, reports, source-owned KAG exports, and reader surfaces point at current paths |
| mechanics links | repaired | Distillation, Audit, and incoming active references route to current authored paths; legacy raw links remain historical receipts |
| validation | green | release check covered unit tests, nested AGENTS coverage, repository parity, and regenerated surfaces |

## What The Eighth Pilot Proved

- `instruction/` can hold a capability-facing shelf without becoming a
  capability registry, skill marketplace, or agent-role policy surface.
- A shelf can mix `artifact` and `discovery` when the shared browsing question
  is a capability surface chain rather than one move kind.
- Broad `docs/` can shrink again while moved leaves still keep `domain: docs`
  as their frontmatter truth.
- The three leaves stay distinct after moving: capability contract,
  registry-facing entry, and lookup contract did not collapse into one
  framework bundle.
- Route-card economy still works. The useful bridge is a compact local shelf
  statement, not a heavy law block repeated through every moved bundle.
- Standalone portability is stronger after the move: external builders can
  reuse one capability-registry technique without deploying OS Abyss or
  accepting AoA registry, routing, or runtime doctrine.

## Remaining Weaknesses

- The generated projection still labels landed shelves with candidate-style
  statuses. That remains tolerable while projection status is non-authoritative,
  but later generated status language may need a separate review if it starts
  confusing readers.
- `instruction/` now has three landed shelves, but it is not a complete
  instruction taxonomy.
- `capability-boundary` is cross-domain: it mixes docs-domain boundary
  guardrails with one agent-workflow guardrail about local host actionability.
  That makes it interesting, but it requires direct reading before any path
  move.
- `skill-discovery` still carries marketplace curation and upstream-health
  pressure. It may become a clean shelf, but it should wait behind the
  capability-boundary read.
- Proof, governance, runtime, and owner-closeout shelves still test stronger
  authority surfaces than this instruction-side progression should take next.

## Ninth Shelf Choice

Choose `capability-boundary` for the next direct-read migration review.

Projected shelf:

| technique | current path | proposed path |
|---|---|---|
| `AOA-T-0040` | `techniques/docs/skill-vs-command-boundary/` | `techniques/instruction/capability-boundary/skill-vs-command-boundary/` |
| `AOA-T-0043` | `techniques/docs/multi-source-primary-input-provenance/` | `techniques/instruction/capability-boundary/multi-source-primary-input-provenance/` |
| `AOA-T-0093` | `techniques/agent-workflows/recommendation-truth-vs-host-actionability/` | `techniques/instruction/capability-boundary/recommendation-truth-vs-host-actionability/` |

Reason:

`capability-boundary` is the cleanest next review target because it checks the
boundary around capability meaning after the capability-registry chain has
landed. `AOA-T-0040` separates reusable skill capability from command
invocation. `AOA-T-0043` keeps primary and supporting source inputs visible
before downstream synthesis or selection depends on them. `AOA-T-0093` keeps
semantic recommendation truth separate from what the current host can actually
execute. Together they ask one useful question: when a capability-like object
is named, sourced, recommended, or invoked, what boundary keeps it honest?

Why direct-read first:

The generated projection marks all three rows as `boundary-watch`, and that is
right. The shelf crosses `docs` and `agent-workflows`, touches host
actionability, and sits next to skill discovery, upstream health, routing,
runtime execution, and KAG/source provenance. A direct-read review must decide
whether the shared boundary is real enough before any path migration.

Why not `skill-discovery` first:

`skill-discovery` is smaller, but it mixes editorial marketplace curation with
upstream source-readiness validation. That is a good later read after the
capability-boundary review clarifies what belongs to capability meaning,
recommendation truth, and host actionability.

Why not proof, governance, runtime, or owner-closeout shelves first:

Those shelves test stronger authority surfaces. The tree should finish this
instruction-side capability-boundary review before taking on proof,
governance, runtime, or closeout semantics.

## Stop Lines

- Do not move `capability-boundary` from this review alone.
- Do not add `tree_path`, `family`, or scout topology axes to frontmatter.
- Do not move `skill-discovery`, proof, governance, runtime, owner-closeout, or
  other capability-adjacent shelves in the same wave.
- Do not treat `capability-boundary` as skill marketplace curation, upstream
  health validation, routing policy, KAG graph semantics, runtime execution
  doctrine, host inventory policy, or agent-role authority.
- Do not collapse skill-command ownership, primary input provenance, and
  recommendation-vs-host-actionability into one mega-technique.
- Keep authored bundle markdown and frontmatter stronger than generated
  projection rows.

## Next Honest Move

Run a direct-read migration review for `capability-boundary`.

Read `AOA-T-0040`, `AOA-T-0043`, and `AOA-T-0093`; inspect their skill-command
ownership, primary-input provenance, recommendation/actionability boundary,
route-card needs, owner-authority stop-lines, and whether
`techniques/instruction/capability-boundary/` is clearer than their current
paths before any move.
