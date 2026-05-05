# Capability-Registry Direct-Read Migration Review

Source packet:
[Technique Reform Ingress](../README.md)

Preceding landed review:
[Landed Docs-Boundary Pilot Review](landed-docs-boundary-pilot-review.md)

Generated lens:
[Technique Tree Projection](../../../../../reports/technique_tree_projection.md)

Tree contract:
[Technique Tree Contract](../../../../../docs/TECHNIQUE_TREE_CONTRACT.md)

Status: accepted-for-eighth-migration-pilot, not path migration, not
`tree_path` frontmatter.

## Verdict

Accept `capability-registry` as the eighth bounded tree migration pilot.

Direct reading confirms that `AOA-T-0025`, `AOA-T-0063`, and `AOA-T-0064`
form one browseable instruction-side shelf: a capability contract is versioned,
a registry-facing entry publishes a named versioned record, and a lookup
contract discovers already-published records. The three leaves stay separate,
but the reader benefits from finding them in one capability-registry
neighborhood instead of hunting across broad `docs/`.

This review does not move files. It only authorizes a later migration wave to
move exactly these three bundles into
`techniques/instruction/capability-registry/` if that wave also updates route
cards, root legacy receipts, links, generated surfaces, and validation.

## Sources Read

- [AOA-T-0025 capability-spec-versioning](../../../../../techniques/docs/capability-spec-versioning/TECHNIQUE.md)
- [AOA-T-0025 checklist](../../../../../techniques/docs/capability-spec-versioning/checks/capability-spec-versioning-checklist.md)
- [AOA-T-0025 minimal example](../../../../../techniques/docs/capability-spec-versioning/examples/minimal-capability-spec-versioning.md)
- [AOA-T-0025 compatibility example](../../../../../techniques/docs/capability-spec-versioning/examples/concrete-capability-upgrade-with-compat-window.md)
- [AOA-T-0025 evidence notes](../../../../../techniques/docs/capability-spec-versioning/notes/canonical-readiness.md)
- [AOA-T-0063 versioned-agent-registry-contract](../../../../../techniques/docs/versioned-agent-registry-contract/TECHNIQUE.md)
- [AOA-T-0063 checklist](../../../../../techniques/docs/versioned-agent-registry-contract/checks/versioned-agent-registry-contract-checklist.md)
- [AOA-T-0063 minimal example](../../../../../techniques/docs/versioned-agent-registry-contract/examples/minimal-versioned-agent-registry-contract.md)
- [AOA-T-0063 evidence notes](../../../../../techniques/docs/versioned-agent-registry-contract/notes/canonical-readiness.md)
- [AOA-T-0064 capability-discovery](../../../../../techniques/docs/capability-discovery/TECHNIQUE.md)
- [AOA-T-0064 checklist](../../../../../techniques/docs/capability-discovery/checks/capability-discovery-checklist.md)
- [AOA-T-0064 minimal example](../../../../../techniques/docs/capability-discovery/examples/minimal-capability-discovery.md)
- [AOA-T-0064 evidence notes](../../../../../techniques/docs/capability-discovery/notes/canonical-readiness.md)
- [Docs route card](../../../../../techniques/docs/AGENTS.md)
- [Instruction route card](../../../../../techniques/instruction/AGENTS.md)
- [Landed docs-boundary pilot review](landed-docs-boundary-pilot-review.md)
- [Technique tree projection rows for `capability-registry`,
  `capability-boundary`, and `skill-discovery`](../../../../../reports/technique_tree_projection.md)

## Direct Bundle Read

| technique | current path | kind | direct-read result |
|---|---|---|---|
| `AOA-T-0025` | `techniques/docs/capability-spec-versioning/` | `artifact` | one named capability stays explicit through a versioned spec with inputs, outputs, invariants, and compatibility notes |
| `AOA-T-0063` | `techniques/docs/versioned-agent-registry-contract/` | `artifact` | one registry-facing entry publishes a named versioned record with stable reference and bounded metadata |
| `AOA-T-0064` | `techniques/docs/capability-discovery/` | `discovery` | one bounded query surface locates already-published capability records with explicit fields, match rules, and result shape |

The kinds are mixed, but the shelf is not pretending to be one move kind. It is
a path neighborhood for one capability-registry chain.

## Why The Shelf Holds

- `AOA-T-0025` owns the capability contract itself and explicitly refuses
  registry, orchestration, persistence, and routing breadth.
- `AOA-T-0063` complements `AOA-T-0025` by owning the publication entry, not
  the full capability spec and not the discovery layer.
- `AOA-T-0064` complements `AOA-T-0063` by owning lookup over already-published
  entries, not publication, ranking, curation, or trust verdicts.
- The examples preserve the same layering: spec example, registry-entry
  example, then query/response example.
- The checklists independently guard the same boundary by keeping runtime,
  marketplace, trust, graph, and product semantics out of the leaf contracts.
- The canonical-readiness notes all keep the bundles promoted rather than
  canonical, which fits a migration pilot: path clarity can improve before any
  stronger quality or default-use status changes.

## Instruction Trunk Fit

`instruction/` is the better trunk because these bundles shape agent-facing
capability surfaces: what a capability contract says, how a versioned record is
published, and how lookup asks for records. They are documentation-domain
techniques today, but their browsing question is capability instruction and
registry surface legibility rather than generic documentation craft.

The `docs/` route card remains correct for their current home until migration.
It already warns against smuggling graph semantics, runtime orchestration, and
repo-specific workflow into docs techniques. The `instruction/` route card is
also ready to host a new shelf if the migration wave adds a compact local scope
bullet and keeps this trunk from becoming skill marketplace policy or runtime
role law.

## Boundary Watch Accepted

The generated projection was right to label this shelf `boundary-watch`.
Capability registry language easily grows too wide. Direct reading accepts the
shelf only because the three bundles repeatedly keep neighboring authority out:

- no registry product doctrine
- no discovery ranking
- no marketplace curation
- no trust or signature policy
- no graph semantics
- no runtime capability resolution
- no role, skill-acceptance, or governance authority

That makes the shelf viable, but also makes the migration stop-lines important.

## Proposed Move

Move exactly these three bundles in the migration wave:

| technique | current path | proposed path |
|---|---|---|
| `AOA-T-0025` | `techniques/docs/capability-spec-versioning/` | `techniques/instruction/capability-registry/capability-spec-versioning/` |
| `AOA-T-0063` | `techniques/docs/versioned-agent-registry-contract/` | `techniques/instruction/capability-registry/versioned-agent-registry-contract/` |
| `AOA-T-0064` | `techniques/docs/capability-discovery/` | `techniques/instruction/capability-registry/capability-discovery/` |

Keep `domain`, `kind`, status, IDs, evidence, relations, and public-safety
posture unchanged.

## Why Not Neighbor Shelves In This Wave

`capability-boundary` should wait because its projected rows mix
host-actionability, skill-command ownership, and multi-source provenance. That
is a real neighboring pressure, but it is more cross-owner than this
spec-entry-query chain.

`skill-discovery` should wait because it mixes marketplace curation and
upstream-health validation. That may become an instruction shelf, but it needs
its own direct-read review before any path move.

Proof, governance, runtime, and owner-closeout shelves should wait because they
test stronger authority surfaces than this migration needs.

## Stop Lines

- Do not move files from this review pack alone.
- Do not add `tree_path`, `family`, capability, substrate, execution-profile,
  or risk frontmatter.
- Do not move `capability-boundary`, `skill-discovery`, proof, governance,
  runtime, or owner-closeout shelves in the same wave.
- Do not turn `capability-registry` into registry product doctrine, discovery
  ranking, marketplace curation, trust policy, graph semantics, runtime
  resolution, skill acceptance, or agent-role authority.
- Do not collapse the three leaves into one technique; the shelf holds because
  spec, entry publication, and lookup remain distinct.
- Do not change canonical/promoted status, maturity, evidence, or
  public-safety posture during the path migration.
- Keep generated projection weaker than authored bundle meaning.

## Next Honest Move

Run the eighth pilot migration.

Move exactly `AOA-T-0025`, `AOA-T-0063`, and `AOA-T-0064` into
`techniques/instruction/capability-registry/`; add the compact
`capability-registry/` shelf scope to `techniques/instruction/AGENTS.md`;
preserve a root `legacy/receipts/` migration receipt; repair authored links;
rebuild generated surfaces; and validate with the narrow tree-pilot tests plus
`python scripts/release_check.py`.
