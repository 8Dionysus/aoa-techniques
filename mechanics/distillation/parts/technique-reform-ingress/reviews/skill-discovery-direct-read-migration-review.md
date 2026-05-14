# Skill-Discovery Direct-Read Migration Review

Source packet:
[Technique Reform Ingress](../README.md)

Preceding landed review:
[Landed Capability-Boundary Pilot Review](landed-capability-boundary-pilot-review.md)

Generated lens:
[Technique Tree Projection](../reports/technique_tree_projection.md)

Tree contract:
[Technique Tree Contract](../../../../../docs/TECHNIQUE_TREE_CONTRACT.md)

Status: accepted-for-tenth-migration-pilot, not path migration, not
`tree_path` frontmatter.

## Verdict

Accept `skill-discovery` as the tenth bounded tree migration pilot.

Direct reading confirms that `AOA-T-0041` and `AOA-T-0042` form one small
instruction-side shelf around reviewable skill surfacing. `AOA-T-0041` owns a
curated discovery layer over upstream-owned skills. `AOA-T-0042` owns the
pre-surface readiness check that keeps one upstream skill source from silently
entering a catalog or selector when it is unreachable or malformed.

The two leaves stay distinct. The shelf does not merge editorial curation and
source-readiness validation into one mega-technique. It gives readers one
browseable neighborhood for a practical question: before a skill-like object
is shown as selectable, what keeps discovery legible without claiming upstream
ownership, installer behavior, registry policy, trust scoring, security
scanning, routing authority, or execution authority?

This review does not move files. It only authorizes a later migration wave to
move exactly these two bundles into `techniques/instruction/skill-discovery/`
if that wave also updates route cards, root legacy receipts, authored links,
generated surfaces, and validation.

## Sources Read

- [AOA-T-0041 skill-marketplace-curation](../../../../../techniques/instruction/skill-discovery/skill-marketplace-curation/TECHNIQUE.md)
- [AOA-T-0041 checklist](../../../../../techniques/instruction/skill-discovery/skill-marketplace-curation/checks/skill-marketplace-curation-checklist.md)
- [AOA-T-0041 minimal example](../../../../../techniques/instruction/skill-discovery/skill-marketplace-curation/examples/minimal-skill-marketplace-curation.md)
- [AOA-T-0041 canonical readiness](../../../../../techniques/instruction/skill-discovery/skill-marketplace-curation/notes/canonical-readiness.md)
- [AOA-T-0041 external import review](../../../../../techniques/instruction/skill-discovery/skill-marketplace-curation/notes/external-import-review.md)
- [AOA-T-0041 external origin](../../../../../techniques/instruction/skill-discovery/skill-marketplace-curation/notes/external-origin.md)
- [AOA-T-0041 second context adaptation](../../../../../techniques/instruction/skill-discovery/skill-marketplace-curation/notes/second-context-adaptation.md)
- [AOA-T-0042 upstream-skill-health-checking](../../../../../techniques/instruction/skill-discovery/upstream-skill-health-checking/TECHNIQUE.md)
- [AOA-T-0042 checklist](../../../../../techniques/instruction/skill-discovery/upstream-skill-health-checking/checks/upstream-skill-health-checking-checklist.md)
- [AOA-T-0042 minimal example](../../../../../techniques/instruction/skill-discovery/upstream-skill-health-checking/examples/minimal-upstream-skill-health-checking.md)
- [AOA-T-0042 canonical readiness](../../../../../techniques/instruction/skill-discovery/upstream-skill-health-checking/notes/canonical-readiness.md)
- [AOA-T-0042 origin evidence](../../../../../techniques/instruction/skill-discovery/upstream-skill-health-checking/notes/origin-evidence.md)
- [AOA-T-0042 second context adaptation](../../../../../techniques/instruction/skill-discovery/upstream-skill-health-checking/notes/second-context-adaptation.md)
- [Docs route card](../../../../../techniques/docs/AGENTS.md)
- [Evaluation route card](../../../../../techniques/evaluation/AGENTS.md)
- [Instruction route card](../../../../../techniques/instruction/AGENTS.md)
- [Technique family scout row for `skill-discovery`](../../../../../mechanics/distillation/parts/technique-reform-ingress/config/technique_family_scout.yaml)
- [Technique kind overlay row for `AOA-T-0041` and `AOA-T-0042`](../../../../../mechanics/distillation/parts/technique-reform-ingress/data/technique_kind_overlay.yaml)
- [Technique tree projection rows for `skill-discovery`](../reports/technique_tree_projection.md)
- [Technique family scout rows for `skill-discovery`](../reports/technique_family_scout.md)
- [Technique topology scout rows for `skill-discovery`](../reports/technique_topology_scout.md)
- [Landed capability-boundary pilot review](landed-capability-boundary-pilot-review.md)

## Direct Bundle Read

| technique | current path | domain | kind | direct-read result |
|---|---|---|---|---|
| `AOA-T-0041` | `techniques/docs/skill-marketplace-curation/` | `docs` | `discovery` | curates a local discovery surface over upstream-owned skills with visible ownership, editorial grouping, and explicit refusal of sync, installer, registry, routing, and capability ownership |
| `AOA-T-0042` | `techniques/evaluation/upstream-skill-health-checking/` | `evaluation` | `validation` | checks one upstream skill source for reachability and minimal manifest-readiness before selector or catalog surfacing without becoming monitoring, registry governance, trust scoring, security scanning, routing, or curation |

The kinds are mixed, but the shelf is not pretending to be one move kind.
`discovery` and `validation` stay separate because the browsing question is
skill surfacing, not one unified workflow.

## Why The Shelf Holds

- `AOA-T-0041` starts after upstream ownership and sync posture are readable,
  then adds editorial value through grouping, summaries, or selection guidance.
- `AOA-T-0042` starts before catalog or selector surfacing, then decides
  whether one source entry is `ready`, `review`, or `blocked`.
- The two leaves complement each other without taking each other's center:
  curation does not perform readiness checks, and readiness does not decide
  marketplace grouping.
- Both bundles keep upstream ownership visible and refuse to make the local
  surface canonical for skill meaning.
- Both checklists reject adjacent authority: mirroring, sync substrate,
  installer behavior, registry governance, routing policy, command doctrine,
  trust scoring, security scanning, generic monitoring, and capability-spec
  ownership.
- The canonical-readiness notes keep both bundles promoted, not canonical,
  which fits a migration pilot: path clarity can improve without claiming
  default-use status.

## Instruction Trunk Fit

`instruction/` is the better trunk because the shelf shapes how humans and
agents are instructed to discover upstream-owned skills safely enough for
selection. The path question is not "is this docs or evaluation?" The path
question is "where should a reader find compact techniques for surfacing
skills as selectable options without stealing source, registry, or execution
authority?"

The current `docs/` home for `AOA-T-0041` is historically reasonable because
the technique is a discovery document pattern. The current `evaluation/` home
for `AOA-T-0042` is historically reasonable because the technique emits a
bounded readiness verdict. Moving them under
`techniques/instruction/skill-discovery/` would be a path-architecture choice
only: `domain`, `kind`, status, IDs, evidence, relations, examples, checks,
and public-safety posture should stay unchanged.

## Boundary Watch Accepted

The generated projection was right to mark this shelf `boundary-watch`.
`skill-discovery` touches external sources, marketplace language, health
language, registry-adjacent surfaces, and selector pressure. Direct reading
accepts the shelf only because the two leaves repeatedly refuse neighboring
authority:

- no installer behavior or command product doctrine
- no sync substrate or upstream mirroring ownership
- no registry product doctrine, registry governance, or access control
- no routing policy or recommendation ranking
- no trust scoring, security scanning, compliance labeling, or supply-chain
  review
- no generic monitoring, incident response, or uptime dashboard
- no capability-spec ownership or capability registry authority
- no agent-role authority or runtime execution doctrine

That makes the shelf viable, but also makes the later migration stop-lines
important.

## Proposed Move

Move exactly these two bundles in the migration wave:

| technique | current path | proposed path |
|---|---|---|
| `AOA-T-0041` | `techniques/docs/skill-marketplace-curation/` | `techniques/instruction/skill-discovery/skill-marketplace-curation/` |
| `AOA-T-0042` | `techniques/evaluation/upstream-skill-health-checking/` | `techniques/instruction/skill-discovery/upstream-skill-health-checking/` |

Keep `domain`, `kind`, status, IDs, evidence, relations, and public-safety
posture unchanged.

## Migration Blast Radius

A later migration wave should expect to update:

- authored links between `AOA-T-0041`, `AOA-T-0042`, and adjacent mirroring,
  capability-boundary, capability-registry, docs, and evaluation bundles
- `techniques/instruction/AGENTS.md` current scope and domain rules, because
  `instruction/` would gain a fifth landed shelf
- `techniques/docs/AGENTS.md` and `techniques/evaluation/AGENTS.md` only if
  their representative-bundle lists still name the moved bundles
- root `legacy/receipts/` and `legacy/INDEX.md` accounting for the authored
  path migration
- generated catalogs, capsules, manifests, reports, KAG exports, docs readers,
  and source-lift surfaces after the path move
- active mechanics review rows that still point to old homes
- release-check output touched by regenerated indexes and reports

Do not create mechanic-style `parts/` packages or shelf READMEs for these
technique leaves.

## Why Not Neighbor Shelves In This Wave

Proof and skill-support shelves should wait. `AOA-T-0042` is a validation
leaf, but it does not make the whole shelf proof authority; it only checks
source availability and minimal manifest-readiness before surfacing.

Runtime, governance, owner-closeout, and automation-governance shelves should
also wait. They carry stronger execution, approval, owner-truth, or
operational authority than this skill-discovery shelf needs.

Capability-registry and capability-boundary are now landed as neighboring
instruction shelves. They should stay as boundaries around capability records,
skill-command ownership, source priority, and recommendation/actionability
rather than absorbing curated skill discovery or upstream readiness.

## Stop Lines

- Do not move files from this review pack alone.
- Do not add `tree_path`, `family`, capability, substrate, execution-profile,
  or risk frontmatter.
- Do not move proof, skill-support, governance, runtime, owner-closeout,
  automation-governance, or other skill-adjacent shelves in the same wave.
- Do not treat `skill-discovery` as installer behavior, sync substrate,
  registry product doctrine, registry governance, access control, routing
  policy, recommendation ranking, trust scoring, security scanning, compliance
  review, generic monitoring, capability ownership, command doctrine, runtime
  law, or agent-role authority.
- Do not collapse curated marketplace discoverability and upstream health
  checking into one mega-technique; the shelf holds because curation and
  source-readiness validation remain distinct leaves.
- Do not change canonical/promoted status, maturity, evidence, or
  public-safety posture during the path migration.
- Keep generated projection weaker than authored bundle meaning.

## Next Honest Move

Run the tenth pilot migration.

Move exactly `AOA-T-0041` and `AOA-T-0042` into
`techniques/instruction/skill-discovery/`; add the compact
`skill-discovery/` shelf scope to `techniques/instruction/AGENTS.md`; preserve
a root `legacy/receipts/` migration receipt; repair authored links; rebuild
generated surfaces; and validate with the narrow tree-pilot tests plus
`python scripts/release_check.py`.
