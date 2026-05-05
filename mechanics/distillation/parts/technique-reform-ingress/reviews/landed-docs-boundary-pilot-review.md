# Landed Docs-Boundary Pilot Review

Source packet:
[Technique Reform Ingress](../README.md)

Migration review:
[Docs-Boundary Direct-Read Migration Review](docs-boundary-direct-read-migration-review.md)

Migration receipt:
[Docs-Boundary Tree Pilot Receipt](../../../../../legacy/receipts/2026-05-04-docs-boundary-tree-pilot.md)

Generated lens:
[Technique Tree Projection](../../../../../reports/technique_tree_projection.md)

Tree contract:
[Technique Tree Contract](../../../../../docs/TECHNIQUE_TREE_CONTRACT.md)

Status: pilot-validated, choose `capability-registry` for direct-read
migration review, not path migration, not `tree_path` frontmatter.

## Verdict

Accept the landed `docs-boundary` pilot as a successful seventh tree migration
and the second successful shelf under the `instruction` trunk.

The shelf stayed legible after landing. Four docs-domain techniques now sit
under one document-boundary neighborhood, while IDs, `domain`, `kind`, status,
evidence, notes, examples, checks, relations, and public-safety posture stayed
unchanged. The move improved browsing without turning source-of-truth layout,
status snapshots, public-safe share preparation, and decision rationale into
one governance doctrine or architecture taxonomy.

This review does not move another shelf. It confirms that the next honest tree
slice should run a direct-read review for `capability-registry`, because the
instruction trunk has now held both instruction-surface and document-boundary
practice. The next pressure should test whether capability specs, registry
entries, and discovery queries form one bounded capability-registry shelf
without importing registry product doctrine, ranking, trust policy, runtime
resolution, or marketplace curation.

## Sources Read

- [AOA-T-0002 source-of-truth-layout](../../../../../techniques/instruction/docs-boundary/source-of-truth-layout/TECHNIQUE.md)
- [AOA-T-0009 lightweight-status-snapshot](../../../../../techniques/instruction/docs-boundary/lightweight-status-snapshot/TECHNIQUE.md)
- [AOA-T-0034 public-safe-artifact-sanitization](../../../../../techniques/instruction/docs-boundary/public-safe-artifact-sanitization/TECHNIQUE.md)
- [AOA-T-0033 decision-rationale-recording](../../../../../techniques/instruction/docs-boundary/decision-rationale-recording/TECHNIQUE.md)
- [AOA-T-0025 capability-spec-versioning](../../../../../techniques/docs/capability-spec-versioning/TECHNIQUE.md)
- [AOA-T-0063 versioned-agent-registry-contract](../../../../../techniques/docs/versioned-agent-registry-contract/TECHNIQUE.md)
- [AOA-T-0064 capability-discovery](../../../../../techniques/docs/capability-discovery/TECHNIQUE.md)
- [Instruction route card](../../../../../techniques/instruction/AGENTS.md)
- [Docs route card](../../../../../techniques/docs/AGENTS.md)
- [Root legacy index](../../../../../legacy/INDEX.md)
- [Docs-boundary tree pilot receipt](../../../../../legacy/receipts/2026-05-04-docs-boundary-tree-pilot.md)
- [Technique tree projection rows for `docs-boundary`,
  `capability-registry`, `capability-boundary`, and `skill-discovery`](../../../../../reports/technique_tree_projection.md)
- [First family shelf review pack](first-family-shelf-review-pack.md)
- [First tree projection review pack](first-tree-projection-review-pack.md)
- [Landed kag-source-lift pilot review](landed-kag-source-lift-pilot-review.md)
- `python scripts/release_check.py` result recorded in the migration receipt

## Landed Shape Read

| check | result | reading |
|---|---|---|
| current path | `techniques/instruction/docs-boundary/` | the active path now matches the projected trunk and shelf |
| frontmatter truth | unchanged | all four leaves keep `domain: docs`; `kind` remains `artifact` or `guardrail` as authored |
| route card | present | `techniques/instruction/AGENTS.md` now names `instruction-surface/` and `docs-boundary/` without becoming a governance surface |
| root legacy | receipt only | active bundles moved directly between authored homes; `legacy/` preserves accounting |
| generated surfaces | rebuilt | catalogs, capsules, manifests, reports, source-owned KAG exports, and reader surfaces point at current paths |
| mechanics links | repaired | Distillation, Audit, Experience, and Agon active references route to current authored paths; legacy raw links remain historical receipts |
| validation | green | release check covered unit tests, nested AGENTS coverage, repository parity, and regenerated surfaces |

## What The Seventh Pilot Proved

- `instruction/` can hold more than one shelf without becoming a frontmatter
  domain or an AoA constitutional surface.
- A document-boundary shelf can mix `artifact` and `guardrail` when the shared
  browsing question is boundary maintenance rather than move shape.
- Broad `docs/` can shrink honestly: moved leaves keep `domain: docs`, while
  the remaining docs folder stays useful for still-unmigrated docs-domain
  bundles.
- Root `legacy/receipts/` remains enough for path-migration accounting; active
  bundles did not need to pass through legacy.
- Route-card economy matters. The useful bridge is the local shelf statement,
  not a repeated law block inserted into every technique.
- Standalone portability is stronger after the move: external builders can
  reuse one document-boundary technique without deploying OS Abyss or accepting
  AoA governance doctrine.

## Remaining Weaknesses

- The generated projection still labels landed shelves with candidate-style
  review statuses. That remains tolerable while projection status is
  non-authoritative, but later generated status language needs a separate
  review if it starts confusing readers.
- `instruction/` now has two landed shelves, but it is not a complete
  instruction taxonomy.
- `capability-registry`, `capability-boundary`, and `skill-discovery` still
  carry stronger capability, skill, registry, marketplace, and upstream-health
  authority pressure than `docs-boundary` did.
- `docs/` still contains several boundary-watch shelves. That is acceptable
  until each one gets direct reading and a migration receipt.

## Eighth Shelf Choice

Choose `capability-registry` for the next direct-read migration review.

Projected shelf:

| technique | current path | proposed path |
|---|---|---|
| `AOA-T-0025` | `techniques/docs/capability-spec-versioning/` | `techniques/instruction/capability-registry/capability-spec-versioning/` |
| `AOA-T-0063` | `techniques/docs/versioned-agent-registry-contract/` | `techniques/instruction/capability-registry/versioned-agent-registry-contract/` |
| `AOA-T-0064` | `techniques/docs/capability-discovery/` | `techniques/instruction/capability-registry/capability-discovery/` |

Reason:

`capability-registry` is the cleanest next review target because the three
leaves form a bounded sequence: a capability contract is versioned, a
registry-facing entry publishes a named versioned record, and discovery queries
already-published entries. All three are docs-domain techniques that shape
agent-facing capability surfaces, which fits the instruction trunk better than
the broad `docs/` folder if direct reading confirms the boundaries.

Why direct-read first:

The generated projection marks these rows as `boundary-watch`, and that is
right. The shelf touches registry, discovery, and capability language, so the
next step must read the bundles directly and keep registry product semantics,
ranking, trust policy, marketplace curation, graph semantics, and runtime
resolution outside the move before any path migration is allowed.

Why not `capability-boundary` or `skill-discovery` first:

`capability-boundary` mixes host-actionability, skill-command ownership, and
multi-source provenance. `skill-discovery` mixes marketplace curation with
upstream-health validation. Both may be real shelves, but their owner pressure
is more cross-cutting than the capability-registry chain.

Why not proof, governance, runtime, or owner-closeout shelves first:

Those shelves test stronger authority surfaces. The tree should finish this
instruction-side capability-registry review before taking on proof,
governance, runtime, or closeout semantics.

## Stop Lines

- Do not move `capability-registry` from this review alone.
- Do not add `tree_path`, `family`, or scout topology axes to frontmatter.
- Do not move `capability-boundary`, `skill-discovery`, proof, governance,
  runtime, or owner-closeout shelves in the same wave.
- Do not treat `capability-registry` as registry product doctrine, discovery
  ranking, trust policy, marketplace curation, graph semantics, runtime
  resolution, or agent-role authority.
- Keep capability specs, registry entries, and discovery queries as separate
  leaves unless direct reading proves a different boundary.
- Keep authored bundle markdown and frontmatter stronger than generated
  projection rows.

## Next Honest Move

Run a direct-read migration review for `capability-registry`.

Read `AOA-T-0025`, `AOA-T-0063`, and `AOA-T-0064`; inspect their capability
contract, registry-entry, and discovery-query boundaries, route-card needs,
owner-authority stop-lines, and whether
`techniques/instruction/capability-registry/` is clearer than the current broad
`docs/` folder.
