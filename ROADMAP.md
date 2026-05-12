# Roadmap

This roadmap tracks the current direction of `aoa-techniques` as a public
practice canon and standalone technique library.

Use it when the question is not "which technique should I open?", but "which
repo-level direction should shape the next change?"

## Authority

Root `ROADMAP.md` owns:

- repo-level direction
- technique-canon horizons
- corpus-scale pressure
- standalone portability pressure
- root entry and source-of-truth pressure
- mechanics-to-canon interface pressure
- concrete future triggers that belong to this repository

It does not own technique status by itself, generated manifest truth, mechanic
local roadmaps, checked mechanic landings, release history, quest state, donor
raw evidence, proof verdicts, or sibling-repository implementation direction.

Use the stronger surface when the change is narrower:

- technique meaning: `techniques/**/TECHNIQUE.md`
- atomicity and portability: `docs/TECHNIQUE_ATOM_CONTRACT.md`
- classification topology: `docs/TECHNIQUE_TOPOLOGY_CONTRACT.md`
- corpus path architecture: `docs/TECHNIQUE_TREE_CONTRACT.md`
- root and docs placement: `docs/ROOT_SURFACE_LAW.md`
- promotion readiness and evidence lanes: `mechanics/audit/parts/`
- donor intake and candidate extraction: `mechanics/distillation/parts/`
- checked mechanic landings: `mechanics/<slug>/LANDING_LOG.md`
- mechanic-local future pressure: `mechanics/<slug>/ROADMAP.md`
- durable obligations: `QUESTBOOK.md` and `quests/`
- released history: `CHANGELOG.md`

The previous closure-audit roadmap is preserved as
`mechanics/audit/legacy/raw/ROOT_CLOSURE_AUDIT_ROADMAP_2026-05-03.md`. Treat it
as historical audit evidence, not the live root direction.

## Update Rule

Update this roadmap when a change moves repo-level direction, corpus topology,
root source-of-truth posture, standalone portability, mechanics-to-canon
interface, or a concrete future trigger for this repository.

Do not update this roadmap for a local mechanic landing, generated refresh,
bundle-local evidence note, quest lifecycle move, release note, or donor ledger
entry unless it changes one of those repo-level directions. Route those changes
to their owning surfaces.

Before closeout, ask: did this change move the practice canon's direction, or
did it only land a local surface?

## Current Direction

`aoa-techniques` is moving from closure-audit hardening into canon-scale
architecture.

The current direction is:

- keep `CHARTER.md`, `README.md`, `docs/START_HERE.md`,
  `docs/TECHNIQUE_ATOM_CONTRACT.md`, `docs/TECHNIQUE_TOPOLOGY_CONTRACT.md`,
  `docs/TECHNIQUE_TREE_CONTRACT.md`, and `docs/ROOT_SURFACE_LAW.md` aligned as
  the root route
- keep the repository usable as a standalone public technique library, not only
  as an OS Abyss organ
- keep each technique as one atomic executable move suitable for templating,
  capsule projection, validation, and small-agent execution after orchestration
  supplies context
- grow toward `1000+` techniques through faceted topology rather than overloaded
  root categories
- keep mechanics active as movement, provenance, review, and candidate routes
  around canon rather than as substitutes for technique bundles
- keep generated catalogs, capsules, source-lift readers, and manifests
  subordinate to authored sources

## Current Checked Contour

The current public corpus is the post-`v0.4.2` working contour: `107` bundles,
`30` canonical, and `77` promoted.

Current anchors:

| Anchor | Surface |
|---|---|
| Repository authority | `CHARTER.md` |
| Public front door | `README.md` |
| Shortest route | `docs/START_HERE.md` |
| Root placement law | `docs/ROOT_SURFACE_LAW.md` |
| Technique atom contract | `docs/TECHNIQUE_ATOM_CONTRACT.md` |
| Technique topology contract | `docs/TECHNIQUE_TOPOLOGY_CONTRACT.md` |
| Technique tree contract | `docs/TECHNIQUE_TREE_CONTRACT.md` |
| Corpus map | `TECHNIQUE_INDEX.md`, `generated/technique_catalog.min.json` |
| Small runtime cards | `docs/TECHNIQUE_CAPSULES.md`, `generated/technique_capsules.min.json` |
| Mechanics atlas | `mechanics/README.md`, `mechanics/AGENTS.md`, `mechanics/*/README.md` |
| Audit and evidence posture | `mechanics/audit/parts/` |
| Donor and candidate extraction | `mechanics/distillation/parts/` |
| Durable obligations | `QUESTBOOK.md`, `quests/` |
| Release history and release path | `CHANGELOG.md`, `docs/RELEASING.md` |

`ROADMAP.md` keeps current direction and future contour. `LANDING_LOG.md`
surfaces keep checked mechanic landings. `CHANGELOG.md` keeps released history.
`QUESTBOOK.md` keeps durable obligations.

## Horizon: Root Clarity

| Field | Direction |
|---|---|
| Current posture | The root now has a clearer authority stack: `README.md`, `CHARTER.md`, `ROADMAP.md`, `QUESTBOOK.md`, `TECHNIQUE_INDEX.md`, and `AGENTS.md` each have separate roles. |
| Next honest move | Keep README and AGENTS short while route law, canon contracts, and generated repo-doc surfaces carry detailed navigation. |
| Guardrail | Root files should not become warehouses for audit history, generated detail, donor ledgers, or mechanic-local runbooks. |

## Horizon: Technique Atom

| Field | Direction |
|---|---|
| Current posture | The technique atom contract names one atomic executable move as the unit of canon. |
| Next honest move | Pressure every new candidate through atom checks before drafting a bundle, especially mechanics candidates and donor imports. |
| Guardrail | Do not patch broad candidates with more prose; split, narrow, keep in mechanics, or route to a stronger owner. |

## Horizon: Corpus Topology

| Field | Direction |
|---|---|
| Current posture | `domain` and `kind` are authoritative frontmatter; family, capability, substrate, execution profile, risk posture, and richer relations are explicit design axes. |
| Next honest move | Enter the long selector/relation pass through `mechanics/distillation/parts/technique-reform-ingress/README.md`, starting from dense shelves where `domain`, `kind`, and tree placement find the neighborhood but not the exact leaf. Keep `config/technique_topology_axes.yaml` and `reports/technique_topology_scout.md` as scout evidence, and strengthen relations only when bundle inputs and contracts justify an existing relation type. |
| Guardrail | Do not turn `agent-workflows`, `docs`, or tags into junk drawers for missing topology. |

## Horizon: Corpus Tree

| Field | Direction |
|---|---|
| Current posture | `docs/TECHNIQUE_TREE_CONTRACT.md` now names the current root tree as trunks, shelves, and leaf bundles. The first full pass landed all `107` bundles under active `techniques/<trunk>/<shelf>/<slug>/` paths, across `10` active bundle trunks and `28` shelves, with `28/28` root legacy receipts, `107/107` current paths matching generated projection paths, no remaining split, singleton, or unassigned hold rows, validator-backed route cards for all current trunks plus retained frontmatter lanes, a final migration ledger, and a completed bundle anatomy closeout that audited all `107` bundles. |
| Next honest move | Keep the landed tree stable while the next reform wave works through selector and relation topology; do not move paths or add `tree_path` frontmatter while relation repair evidence is still being tested shelf by shelf. |
| Guardrail | Do not move all bundles in one wave, make `tree_path` required frontmatter prematurely, or copy the mechanics package shape into technique leaves. |

Historical tree migration breadcrumb row preserved for parity; current closeout above supersedes it as direction:

| Current posture | `docs/TECHNIQUE_TREE_CONTRACT.md` names the future root tree as trunks, shelves, and leaf bundles; `reports/technique_tree_projection.md` gives a non-authoritative full-corpus placement projection; the first landed pilot moved `AOA-T-0051`, `AOA-T-0052`, and `AOA-T-0054` into `techniques/continuity/review-compaction/`, the second landed pilot moved `AOA-T-0056` through `AOA-T-0062` into `techniques/continuity/handoff-continuation/`, the third landed pilot, the first non-continuity migrated shelf, moved `AOA-T-0070` through `AOA-T-0074` into `techniques/ingest/media-ingest/`, the fourth landed pilot moved `AOA-T-0080` through `AOA-T-0083` into `techniques/recovery/diagnosis-repair/`, the fifth landed pilot moved `AOA-T-0012`, `AOA-T-0013`, `AOA-T-0024`, `AOA-T-0027`, `AOA-T-0029`, `AOA-T-0030`, and `AOA-T-0035` into `techniques/instruction/instruction-surface/`, the sixth landed pilot moved `AOA-T-0018`, `AOA-T-0019`, `AOA-T-0020`, `AOA-T-0021`, `AOA-T-0022`, `AOA-T-0046`, and `AOA-T-0048` into `techniques/knowledge-lift/kag-source-lift/`, the seventh landed pilot moved `AOA-T-0002`, `AOA-T-0009`, `AOA-T-0034`, and `AOA-T-0033` into `techniques/instruction/docs-boundary/`, the eighth landed pilot moved `AOA-T-0025`, `AOA-T-0063`, and `AOA-T-0064` into `techniques/instruction/capability-registry/`, the ninth landed pilot moved `AOA-T-0040`, `AOA-T-0043`, and `AOA-T-0093` into `techniques/instruction/capability-boundary/`, the tenth landed pilot moved `AOA-T-0041` and `AOA-T-0042` into `techniques/instruction/skill-discovery/`, the eleventh landed pilot moved `AOA-T-0016`, `AOA-T-0015`, and `AOA-T-0017` into `techniques/proof/skill-support/`, the twelfth landed pilot moved `AOA-T-0003`, `AOA-T-0007`, and `AOA-T-0032` into `techniques/proof/evaluation-chain/`, the thirteenth landed pilot moved `AOA-T-0006`, `AOA-T-0008`, `AOA-T-0010`, and `AOA-T-0011` into `techniques/proof/published-summary/`, the fourteenth landed pilot moved `AOA-T-0044`, `AOA-T-0053`, `AOA-T-0026`, `AOA-T-0045`, `AOA-T-0066`, and `AOA-T-0067` into `techniques/history/history-artifacts/`, the fifteenth landed pilot moved `AOA-T-0097`, `AOA-T-0099`, `AOA-T-0100`, and `AOA-T-0098` into `techniques/recovery/antifragility-recovery/`, the sixteenth landed pilot moved `AOA-T-0049`, `AOA-T-0050`, and `AOA-T-0055` into `techniques/execution/ready-work-graphs/`, the seventeenth landed pilot moved `AOA-T-0004` and `AOA-T-0005` into `techniques/execution/intent-chain/`, the eighteenth landed pilot moved `AOA-T-0001`, `AOA-T-0014`, `AOA-T-0023`, `AOA-T-0028`, and `AOA-T-0031` into `techniques/execution/agent-workflows-core/`, the nineteenth landed pilot moved `AOA-T-0075`, `AOA-T-0077`, `AOA-T-0084`, and `AOA-T-0085` into `techniques/continuity/donor-harvest/`, the twentieth landed pilot moved `AOA-T-0076`, `AOA-T-0078`, and `AOA-T-0079` into `techniques/governance/decision-routing/`, the twenty-first landed pilot moved `AOA-T-0068` and `AOA-T-0069` into `techniques/governance/approval-evidence/`, the twenty-second landed pilot moved `AOA-T-0107`, `AOA-T-0105`, and `AOA-T-0106` into `techniques/proof/review-evidence/`, the twenty-third landed pilot moved `AOA-T-0036`, `AOA-T-0038`, `AOA-T-0037`, and `AOA-T-0039` into `techniques/execution/runtime-truth-lifecycle/`, and the twenty-fourth landed pilot moved `AOA-T-0091`, `AOA-T-0092`, `AOA-T-0095`, `AOA-T-0096`, and `AOA-T-0094` into `techniques/proof/owner-truth-closeout/`; all twenty-four kept frontmatter unchanged. The landed `evaluation-chain` pilot review completed the previous step, "Review the landed `evaluation-chain` pilot before choosing any thirteenth shelf," and chose `published-summary` for direct-read review. The landed `published-summary` pilot review completed the previous step, "Review the landed `published-summary` pilot before choosing any fourteenth shelf," and chose `history-artifacts` for direct-read review. The `history-artifacts` direct-read review completed the previous step, "Run the `history-artifacts` direct-read migration review before any fourteenth shelf migration," and accepted exactly `AOA-T-0044`, `AOA-T-0053`, `AOA-T-0026`, `AOA-T-0045`, `AOA-T-0066`, and `AOA-T-0067` for the fourteenth pilot. The landed `history-artifacts` pilot review completed the previous step, "Review the landed `history-artifacts` pilot before choosing any fifteenth shelf," validates the first history trunk shelf, and chooses `recovery/antifragility-recovery` for direct-read review. The `antifragility-recovery` direct-read review completed the previous step, "Run the `recovery/antifragility-recovery` direct-read migration review before any fifteenth shelf migration," and accepted exactly `AOA-T-0097`, `AOA-T-0099`, `AOA-T-0100`, and `AOA-T-0098` for the fifteenth pilot. The landed `antifragility-recovery` pilot review completed the previous step, "Review the landed `antifragility-recovery` pilot before choosing any sixteenth shelf," validates the second recovery trunk shelf, preserves `AOA-T-0098` as validation-shaped, and chooses `execution/ready-work-graphs` for direct-read review. The `ready-work-graphs` direct-read review completed the previous step, "Run the `execution/ready-work-graphs` direct-read migration review before any sixteenth shelf migration," and accepted exactly `AOA-T-0049`, `AOA-T-0050`, and `AOA-T-0055` for the sixteenth pilot. The sixteenth pilot migration moved those three bundles into `techniques/execution/ready-work-graphs/` with the new execution route card, root legacy receipt, link repair, generated rebuilds, and unchanged frontmatter. The landed `ready-work-graphs` pilot review completed the previous step, "Review the landed `ready-work-graphs` pilot before choosing any seventeenth shelf," validates the first execution trunk shelf, preserves `AOA-T-0055` as a readiness ladder, and chooses `execution/intent-chain` for direct-read review. The `intent-chain` direct-read review completed the previous step, "Run the `execution/intent-chain` direct-read migration review before any seventeenth shelf migration," and accepted exactly `AOA-T-0004` and `AOA-T-0005` for the seventeenth pilot without moving files or changing frontmatter. The seventeenth pilot migration moved those two bundles into `techniques/execution/intent-chain/` with updated execution route card accounting, root legacy receipt, link repair, generated rebuilds, and unchanged frontmatter. The landed `intent-chain` pilot review completed the previous step, "Review the landed `intent-chain` pilot before choosing any eighteenth shelf," validates the second execution trunk shelf, preserves `AOA-T-0005` as promoted, and chooses `execution/agent-workflows-core` for direct-read review. The `agent-workflows-core` direct-read review completed the previous step, "Run the `execution/agent-workflows-core` direct-read migration review before any eighteenth shelf migration," and accepted exactly `AOA-T-0001`, `AOA-T-0014`, `AOA-T-0023`, `AOA-T-0028`, and `AOA-T-0031` for the eighteenth pilot without moving files or changing frontmatter. The eighteenth pilot migration moved those five bundles into `techniques/execution/agent-workflows-core/` with updated execution route card accounting, root legacy receipt, link repair, generated rebuilds, and unchanged frontmatter. The landed `agent-workflows-core` pilot review completed the previous step, "Review the landed `agent-workflows-core` pilot before choosing any nineteenth shelf," validates the third execution trunk shelf, preserves `AOA-T-0028` as `guardrail` and `AOA-T-0031` as `composition`, and chooses `continuity/donor-harvest` for direct-read review. The `donor-harvest` direct-read review completed the previous step, "Run the `continuity/donor-harvest` direct-read migration review before any nineteenth shelf migration," and accepted exactly `AOA-T-0075`, `AOA-T-0077`, `AOA-T-0084`, and `AOA-T-0085` for the nineteenth pilot without moving files or changing frontmatter. The nineteenth pilot migration moved those four bundles into `techniques/continuity/donor-harvest/` with the continuity route card, root legacy receipt, link repair, generated rebuilds, and unchanged frontmatter. The landed `donor-harvest` pilot review completed the previous step, "Review the landed `donor-harvest` pilot before choosing any twentieth shelf," validates the third continuity trunk shelf, preserves `AOA-T-0077` as `handoff` and the other three leaves as `lift`, and chooses `governance/decision-routing` for direct-read review. The `decision-routing` direct-read review completed the previous step, "Run the `governance/decision-routing` direct-read migration review before any twentieth shelf movement," and accepted exactly `AOA-T-0076`, `AOA-T-0078`, and `AOA-T-0079` for the twentieth pilot without moving files or changing frontmatter. The twentieth pilot migration moved those three bundles into `techniques/governance/decision-routing/` with the compact governance route card, root legacy receipt, link repair, generated rebuilds, and unchanged frontmatter. The landed `decision-routing` pilot review completed the previous step, "Review the landed `decision-routing` pilot before choosing any twenty-first shelf," validates the first governance trunk shelf, preserves the shelf as local decision support, and chooses `governance/approval-evidence` for direct-read review. The `approval-evidence` direct-read review completed the previous step, "Run the `governance/approval-evidence` direct-read migration review before any twenty-first shelf movement," and accepted exactly `AOA-T-0068` and `AOA-T-0069` for the twenty-first pilot without moving files or changing frontmatter. The twenty-first pilot migration moved those two bundles into `techniques/governance/approval-evidence/` with support files, governance route-card update, root legacy receipt, link repair, generated rebuilds, and unchanged frontmatter. The landed `approval-evidence` pilot review completed the previous step, "Review the landed `governance/approval-evidence` pilot before choosing any twenty-second shelf," validates the second governance trunk shelf, preserves the immediate gate and durable approval seam as distinct leaves, and chooses `proof/review-evidence` for direct-read review. The `review-evidence` direct-read review completed the previous step, "Run the `proof/review-evidence` direct-read migration review before any twenty-second shelf movement," and accepted exactly `AOA-T-0107`, `AOA-T-0105`, and `AOA-T-0106` for the twenty-second pilot without moving files or changing frontmatter. The twenty-second pilot migration moved those three bundles into `techniques/proof/review-evidence/` with support files, proof route card update, root legacy receipt, link repair, generated rebuilds, and unchanged frontmatter. The landed `review-evidence` pilot review completed the previous step, "Review the landed `proof/review-evidence` pilot before choosing any twenty-third shelf," validates the fourth proof trunk shelf, and chooses `execution/runtime-truth-lifecycle` for direct-read review. The `runtime-truth-lifecycle` direct-read review completed the previous step, "Run the `execution/runtime-truth-lifecycle` direct-read migration review before any twenty-third shelf movement," and accepted exactly `AOA-T-0036`, `AOA-T-0038`, `AOA-T-0037`, and `AOA-T-0039` for the twenty-third pilot without moving files or changing frontmatter. The twenty-third pilot migration moved those four bundles into `techniques/execution/runtime-truth-lifecycle/` with support files, execution route-card update, root legacy receipt, link repair, generated rebuilds, and unchanged frontmatter. The `owner-truth-closeout` direct-read review completed the previous step, "Run the `proof/owner-truth-closeout` direct-read migration review before any twenty-fourth shelf movement," and accepted exactly `AOA-T-0091`, `AOA-T-0092`, `AOA-T-0095`, `AOA-T-0096`, and `AOA-T-0094` for the twenty-fourth pilot without moving files or changing frontmatter. The twenty-fourth pilot migration moved those five bundles into `techniques/proof/owner-truth-closeout/` with proof route-card update, root legacy receipt, link repair, generated rebuilds, and unchanged frontmatter. |

Current latest tree closeout: the whole-tree closeout review validates the
current tree as `107` bundles, `10` trunks, `28` shelves, `107/107` current
path parity, `28/28` root receipts, and zero split/singleton/unassigned holds.
Previous closeout breadcrumb preserved for parity: Run the whole-tree closeout review before route-card consolidation or another reform slice.

Current latest tree route-card consolidation: all current trunk route cards now
name the tree posture as current path architecture, retained
`agent-workflows`, `docs`, and `evaluation` cards now read as frontmatter lanes
rather than direct leaf homes, and `scripts/validate_nested_agents.py` covers
every current trunk plus retained lane.
Previous route-card breadcrumb preserved for parity: Run tree route-card consolidation before another path movement, schema promotion, or reform slice.

Current latest final tree ledger: the final tree migration ledger validates
generated parity, `28/28` shelf receipt coverage, temporary-plan distillation,
and the transition from path migration into technique-bundle reform.
Previous final-ledger breadcrumb preserved for parity: Run the final migration ledger and generated parity pass before another path movement, schema promotion, or reform slice.

Current latest bundle anatomy closeout: the final bundle reform ledger validates
the first post-tree anatomy pass over all `107` bundles, closes the lone
capsule-reader repair cohort, records no schema, path, promotion, route-away,
or legacy receipt tail, and moves next direction toward one chosen targeted
reform slice.
Previous bundle-anatomy breadcrumb preserved for parity: Start
technique-bundle reform with a corpus-wide bundle anatomy and small-agent
usability audit before changing individual leaves.

Current latest tree migration: the `tool-gateway` pilot moved exactly
`AOA-T-0065` into `techniques/tool-use/tool-gateway/` without changing
frontmatter. It completes the previous next honest move: Migrate exactly
`AOA-T-0065` into
`techniques/tool-use/tool-gateway/mcp-gateway-proxy/`.
Current latest tree review: the landed `tool-gateway` pilot review validates
the first `tool-use` shelf, resolves the former singleton hold, and chooses
whole-tree closeout review.
Current latest split review: the `automation-governance` direct-read split
review rejects one bulk shelf and names `governance/automation-readiness`,
`governance/promotion-boundary`, and
`governance/practice-adoption-lifecycle` as split candidates before any
automation-governance path movement.
Current latest split expansion: the automation-governance split-expansion
closeout activates `governance/automation-readiness` as Candidate A over
`AOA-T-0086`, `AOA-T-0087`, and `AOA-T-0088`, with
`governance/promotion-boundary` and `governance/practice-adoption-lifecycle`
queued behind it and no path movement yet.
Current latest direct-read review: the `tool-gateway` direct-read singleton
review accepts exactly `AOA-T-0065` as the twenty-eighth migration pilot and
does not move files or change frontmatter.
Previous landed tool-gateway review breadcrumb preserved for parity: Review the landed `tool-use/tool-gateway` pilot before final consolidation or choosing the next reform slice.
Previous tool-gateway migration breadcrumb preserved for parity: Migrate exactly `AOA-T-0065` into `techniques/tool-use/tool-gateway/mcp-gateway-proxy/`.
Previous tool-gateway breadcrumb preserved for parity: Run the direct-read
singleton review for `tool-use/tool-gateway` before any twenty-eighth movement.
Current latest landed split review: the landed `practice-adoption-lifecycle`
pilot review validates the third split shelf and closes the split tail before
the `tool-use/tool-gateway` singleton review.
Previous Candidate C landed-review breadcrumb preserved for parity: Review the
landed `governance/practice-adoption-lifecycle` pilot before routing the
`tool-use/tool-gateway` singleton or another discovered tail.
Previous Candidate C migration breadcrumb preserved for parity: Migrate exactly `AOA-T-0101`, `AOA-T-0103`, and `AOA-T-0104` into `techniques/governance/practice-adoption-lifecycle/`.
Previous Candidate C breadcrumb preserved for parity: Run the `governance/practice-adoption-lifecycle` direct-read review before any twenty-seventh shelf movement.
Previous Candidate B landed-review breadcrumb preserved for parity: Review the landed `governance/promotion-boundary` pilot before choosing Candidate C or another split-route hold.
Previous Candidate B migration breadcrumb preserved for parity: Migrate exactly `AOA-T-0089`, `AOA-T-0090`, and `AOA-T-0102` into `techniques/governance/promotion-boundary/`.
Previous Candidate B breadcrumb preserved for parity: Run the `governance/promotion-boundary` direct-read review before any twenty-sixth shelf movement.
Previous Candidate A direct-read breadcrumb preserved for parity: the `automation-readiness` direct-read
review accepts exactly `AOA-T-0086`, `AOA-T-0087`, and `AOA-T-0088` as the twenty-fifth migration pilot.
Previous Candidate A tree migration breadcrumb preserved for parity: the `automation-readiness` pilot moved exactly `AOA-T-0086`, `AOA-T-0087`, and `AOA-T-0088` into `techniques/governance/automation-readiness/`.
Previous Candidate A landed-review breadcrumb preserved for parity: Review the landed `governance/automation-readiness` pilot before choosing Candidate B or another split-route hold.
Previous Candidate A migration breadcrumb preserved for parity: Migrate exactly `AOA-T-0086`, `AOA-T-0087`, and `AOA-T-0088` into `techniques/governance/automation-readiness/`.
Previous Candidate A breadcrumb preserved for parity: Run the `governance/automation-readiness` direct-read review before any twenty-fifth shelf movement.
Previous split-expansion breadcrumb preserved for parity: Run the automation-governance split-expansion closeout before any twenty-fifth shelf movement.
Previous split-review breadcrumb preserved for parity: Run the `governance/automation-governance` direct-read split review before any twenty-fifth shelf movement.
Previous breadcrumb preserved for parity: Review the landed `proof/owner-truth-closeout` pilot before choosing any twenty-fifth shelf.
Previous breadcrumb preserved for parity: Review the landed `execution/runtime-truth-lifecycle` pilot before choosing any twenty-fourth shelf.
Previous migration breadcrumb preserved for parity: Migrate exactly `AOA-T-0091`, `AOA-T-0092`, `AOA-T-0095`, `AOA-T-0096`, and `AOA-T-0094` into `techniques/proof/owner-truth-closeout/`.
Previous review breadcrumb preserved for parity: Run the `proof/owner-truth-closeout` direct-read migration review before any twenty-fourth shelf movement.

## Horizon: Small-Agent Usability

| Field | Direction |
|---|---|
| Current posture | Capsules and generated catalogs already provide compact lookup surfaces; the template-modernization long pass is closed across all `107` current bundles with `3` pilot-repaired `proof/skill-support` leaves, `104` held-no-repair rows, no new source rewrites, and optional fixed-slot sections still rejected as a required corpus migration. |
| Next honest move | Move from template-shape review to concrete content-level technique reform only where direct bundle reading finds a real source, selector, relation, portability, owner-boundary, or execution-shape problem. |
| Guardrail | Small-agent usability does not mean autonomous selection; routing and composition may belong to larger agents or neighboring layers. |

## Horizon: Mechanics To Canon

| Field | Direction |
|---|---|
| Current posture | Mechanics packages now keep active routes, parts, provenance, landing logs, package roadmaps, and legacy scaffolds; the root mechanics surface stays an atlas and local law route rather than a second roadmap authority. |
| Next honest move | Use mechanics to preserve lineage and candidate pressure while extracting only one atomic practice at a time into `techniques/`, and keep package roadmaps strong enough for small-agent route choice without importing AoA center authority. |
| Guardrail | Mechanics can prepare canon. They do not replace canon or silently change status. |

## Horizon: Evidence And Promotion

| Field | Direction |
|---|---|
| Current posture | Audit parts carry promotion readiness, evidence sprinting, and searched-lane memory. |
| Next honest move | Keep external-evidence work routed through the Audit and Distillation parts, then update bundle-local notes before shared queues. |
| Guardrail | Root roadmap should name evidence pressure only at the horizon level; ledgers and queue details belong in Audit. |

## Horizon: Standalone Portability

| Field | Direction |
|---|---|
| Current posture | The repository explicitly serves both external builders and AoA sibling repos. |
| Next honest move | Keep AoA references as provenance and integration context while making the portable practice understandable without OS Abyss. |
| Guardrail | Do not let AoA organ fidelity become a hidden dependency for public reuse. |

## Horizon: Generated Companions

| Field | Direction |
|---|---|
| Current posture | Generated catalogs, capsules, source-lift readers, and repo-doc surfaces give machines compact routes over authored sources. |
| Next honest move | Keep generated parity validator-backed whenever source docs, templates, route maps, or surface specs change. |
| Guardrail | Generated outputs route and compress; they do not author technique meaning, root law, or status. |

## When The Time Comes

Use this block for likely repo-level work that is not useful to land until its
trigger is real.

- Promote `family` from scout-only to optional reviewed frontmatter only after
  examples and tie-break rules stay stable across multiple technique waves.
- Use the landed `review-compaction`, `handoff-continuation`, `media-ingest`,
  `diagnosis-repair`, `instruction-surface`, `kag-source-lift`,
  `docs-boundary`, `capability-registry`, `capability-boundary`,
  `skill-discovery`, `skill-support`, `evaluation-chain`,
  `published-summary`, `history-artifacts`, `antifragility-recovery`,
  `ready-work-graphs`, `intent-chain`, `agent-workflows-core`, and
  `donor-harvest` pilots as precedents, and review the landed
  `continuity/donor-harvest` shelf before any other shelf movement or broader
  corpus move.
- Add generated projections for `capability_class`, `substrate`,
  `execution_profile`, and `risk_posture` from
  `config/technique_topology_axes.yaml` only after mechanics candidates prove
  the axes help selection without false precision.
- Use the technique reform ingress packet before any broad classification
  change so the first reform pass stays bounded and evidence-linked.
- Add richer typed relation guidance only when direct relations are repeatedly
  useful for composition, conflict, sequence, or prerequisite routing.
- Split `WALKTHROUGH.md` into a docs or examples district only if one root
  example becomes too large or starts attracting multiple tutorials.
- Add a machine-facing root route capsule only after the human route stabilizes
  enough that a generated companion would reduce real reader load.

An item belongs here only when its trigger is concrete and repo-level. If the
future pressure is mechanic-local, use `mechanics/<slug>/ROADMAP.md`. If it is
a durable obligation, use `QUESTBOOK.md` and `quests/`.

## Standing Direction

Across all horizons:

- keep one technique small
- keep the corpus navigable at scale
- keep portable practice stronger than local lore
- keep mechanics, generated surfaces, and sibling consumers subordinate to
  authored technique truth
- make every route clearer for both humans and small agents
