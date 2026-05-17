# Selector Relation Wave D Governance Split Review

Source packet: [Technique Reform Ingress](../README.md)

Closeout ledger:
[Selector Relation Long-Pass Closeout Ledger](selector-relation-long-pass-closeout-ledger.md)

Prior wave:
[Selector Relation Wave C Execution Owner Review](selector-relation-wave-c-execution-owner-review.md)

Status: Wave D selector/relation review, with one accepted direct relation
repair routed to
[Practice-Adoption-Lifecycle Direct Relation Repair](practice-adoption-lifecycle-direct-relation-repair.md).

## Verdict

Wave D holds the governance split.

The four shelves in scope should stay separate:

- `governance/decision-routing`
- `governance/automation-readiness`
- `governance/promotion-boundary`
- `governance/practice-adoption-lifecycle`

Direct reading confirms the earlier split work. These shelves share a broad
before-action governance posture, but they do not share one object. Decision
routing keeps choices legible, automation readiness classifies and lands one
automation-facing candidate, promotion boundary protects owner-target moments,
and practice adoption lifecycle reviews local adoption, retention, and
obsolescence posture.

One direct relation repair is justified inside the practice-adoption lifecycle:
`AOA-T-0103 used_together_for AOA-T-0104`. The retention review can emit
`route_to_obsolescence`, while the obsolescence route packet owns the bounded
handoff that follows that verdict. This is an operating-path relation, not a
strict prerequisite.

No other bundle relation, status, `domain`, `kind`, path, scout axis, schema,
or generated graph behavior should change from this wave.

## Sources Read

Direct bundle reads:

- [AOA-T-0076 owner-layer-triage](../../../../../techniques/governance/decision-routing/owner-layer-triage/TECHNIQUE.md)
- [AOA-T-0078 decision-fork-cards](../../../../../techniques/governance/decision-routing/decision-fork-cards/TECHNIQUE.md)
- [AOA-T-0079 risk-passport-lift](../../../../../techniques/governance/decision-routing/risk-passport-lift/TECHNIQUE.md)
- [AOA-T-0086 automation-fit-matrix](../../../../../techniques/governance/automation-readiness/automation-fit-matrix/TECHNIQUE.md)
- [AOA-T-0087 human-loop-to-first-landing](../../../../../techniques/governance/automation-readiness/human-loop-to-first-landing/TECHNIQUE.md)
- [AOA-T-0088 approval-sensitivity-check](../../../../../techniques/governance/automation-readiness/approval-sensitivity-check/TECHNIQUE.md)
- [AOA-T-0089 quest-unit-promotion-review](../../../../../techniques/governance/promotion-boundary/quest-unit-promotion-review/TECHNIQUE.md)
- [AOA-T-0090 nearest-wrong-target-rejection](../../../../../techniques/governance/promotion-boundary/nearest-wrong-target-rejection/TECHNIQUE.md)
- [AOA-T-0102 skill-proposal-handoff-packet](../../../../../techniques/governance/promotion-boundary/skill-proposal-handoff-packet/TECHNIQUE.md)
- [AOA-T-0101 local-pattern-adoption-gate](../../../../../techniques/governance/practice-adoption-lifecycle/local-pattern-adoption-gate/TECHNIQUE.md)
- [AOA-T-0103 adopted-practice-retention-review](../../../../../techniques/governance/practice-adoption-lifecycle/adopted-practice-retention-review/TECHNIQUE.md)
- [AOA-T-0104 superseded-practice-obsolescence-route](../../../../../techniques/governance/practice-adoption-lifecycle/superseded-practice-obsolescence-route/TECHNIQUE.md)

Supporting review and generated surfaces:

- [Technique Selection](../../../../../docs/readers/selection/TECHNIQUE_SELECTION.md)
- [Selection Patterns](../../../../../docs/readers/selection/SELECTION_PATTERNS.md)
- [Technique Selection Guide](../../../../../docs/selection/TECHNIQUE_SELECTION_GUIDE.md)
- [Technique Topology Scout](../reports/technique_topology_scout.md)
- [Technique Tree Projection](../reports/technique_tree_projection.md)
- [Automation-Governance Direct-Read Split Review](automation-governance-direct-read-split-review.md)
- [Automation-Governance Split Expansion Closeout](automation-governance-split-expansion-closeout.md)
- [Decision-Routing Direct-Read Migration Review](decision-routing-direct-read-migration-review.md)
- [Landed Decision-Routing Pilot Review](landed-decision-routing-pilot-review.md)
- [Automation-Readiness Direct-Read Migration Review](automation-readiness-direct-read-migration-review.md)
- [Landed Automation-Readiness Pilot Review](landed-automation-readiness-pilot-review.md)
- [Promotion-Boundary Direct-Read Migration Review](promotion-boundary-direct-read-migration-review.md)
- [Landed Promotion-Boundary Pilot Review](landed-promotion-boundary-pilot-review.md)
- [Practice-Adoption-Lifecycle Direct-Read Migration Review](practice-adoption-lifecycle-direct-read-migration-review.md)
- [Landed Practice-Adoption-Lifecycle Pilot Review](landed-practice-adoption-lifecycle-pilot-review.md)

## Selector Prompts

| selector prompt | first correct pick | why adjacent leaves lose |
|---|---|---|
| "One isolated reusable unit needs a primary owner layer and the nearest wrong owner named." | `AOA-T-0076` | quest promotion starts after repeated quest evidence; local adoption already assumes one local behavior surface |
| "A reviewed source leaves several materially different next routes and the alternatives must stay visible." | `AOA-T-0078` | owner triage picks one primary owner; risk passport annotates a route after routes are explicit |
| "An explicit route needs small difficulty, risk, control-mode, delegate-tier, and stop-condition posture." | `AOA-T-0079` | fork cards create the route set; approval sensitivity is automation-candidate specific |
| "A recurring manual route needs an evidence-backed automation fit verdict before anyone calls it seed-ready." | `AOA-T-0086` | first landing assumes enough readiness evidence; approval sensitivity owns checkpoint burden |
| "A recurring human loop needs the first honest automation-facing landing: skill, playbook seed, technique candidate, repair, or defer." | `AOA-T-0087` | generic owner triage is broader; skill proposal handoff assumes skill-shaped pressure already exists |
| "An automation candidate may cross approval, rollback, hidden-authority, or self-change boundaries." | `AOA-T-0088` | confirmation gate is generic mutation pause; checkpoint-bound repair builds a later repair packet |
| "One repeated reviewed quest unit needs a bounded keep-or-promote verdict." | `AOA-T-0089` | nearest-wrong rejection sharpens a chosen verdict; owner triage is an earlier generic placement pass |
| "A plausible chosen target needs the nearest tempting wrong target rejected explicitly." | `AOA-T-0090` | promotion review chooses the verdict; local adoption gate emits adopt, shadow, quarantine, defer, or reject posture |
| "Technique-side adoption pressure should become one skill proposal packet without accepting or activating a skill." | `AOA-T-0102` | skill-vs-command boundary separates shaped capability objects; first landing chooses whether skill proposal is even the right destination |
| "A shared pattern might become local behavior and needs consent, compatibility, rollback, and retention watch first." | `AOA-T-0101` | owner triage chooses first owner shape; retention review starts only after adoption or shadow use |
| "An adopted or shadowed practice needs current evidence review before it stays active." | `AOA-T-0103` | adoption gate is upstream; obsolescence route follows only when retention cannot honestly keep the practice active as-is |
| "A practice should not remain active as-is and needs a supersede, merge, reanchor, defer, drop, or deprecation-review route packet." | `AOA-T-0104` | retention review asks whether to keep active; this handoff packet preserves owner receipt and retained lesson before any status change |

## Split Shelf Read

| shelf | should own | should not absorb |
|---|---|---|
| `decision-routing` | one choice-support neighborhood: owner verdict, route fork cards, and route passports | automation fit, skill proposal, local adoption, retention, or obsolescence lifecycle |
| `automation-readiness` | readiness, first landing, and approval/checkpoint burden before automation-facing lift | final promotion verdicts, skill acceptance, route policy, scheduler doctrine, or Method-growth adoption lifecycle |
| `promotion-boundary` | owner-target verdict pressure, nearest-wrong-target rejection, and skill-proposal handoff posture | automation fit matrices, local adoption consent, retention, deprecation execution, proof, memory, role, or route authority |
| `practice-adoption-lifecycle` | local adoption, post-adoption retention, and obsolescence route packets for one practice surface | Method-growth law, skill activation, proof authority, memory truth, route mutation, runtime behavior, or permanent retention |

## Relation Read

| relation | verdict | reason |
|---|---|---|
| `AOA-T-0076 complements AOA-T-0075` | keep | owner triage starts after one unit is isolated; donor harvest is one common upstream, not mandatory for every candidate |
| `AOA-T-0076 complements AOA-T-0016` | keep | context mapping can clarify boundaries, but owner-layer triage is one placement verdict, not a full bounded-context artifact |
| `AOA-T-0078 complements AOA-T-0079` | keep | fork cards and risk passports often travel together without making passport fields part of card authorship |
| `AOA-T-0078 complements AOA-T-0077` | keep | a harvest packet can feed branch cards, but a reviewed session artifact can also be enough |
| `AOA-T-0079 complements AOA-T-0078` | keep | route passport needs an explicit route, not necessarily this exact fork-card technique |
| `AOA-T-0079 complements AOA-T-0083` | keep | risk posture can point toward checkpoint-bound repair, but does not build the repair packet |
| `AOA-T-0086 complements AOA-T-0087` | keep | readiness classification commonly feeds first landing, but first landing can start from equivalent readiness evidence |
| `AOA-T-0086 complements AOA-T-0088` | keep | fit matrix includes approval sensitivity as one row, while approval-sensitivity check owns a narrower checkpoint-burden read |
| `AOA-T-0087 complements AOA-T-0086` | keep | first landing asks for readiness classification or equivalent evidence without requiring the exact fit-matrix bundle |
| `AOA-T-0087 complements AOA-T-0076` | keep | automation first landing is owner-aware but narrower than generic owner-layer triage |
| `AOA-T-0088 complements AOA-T-0028` | keep | approval sensitivity is automation-candidate posture; confirmation gate is a generic mutation seam |
| `AOA-T-0088 complements AOA-T-0083` | keep | checkpoint-required posture can route to checkpoint-bound repair without creating the repair packet itself |
| `AOA-T-0089 complements AOA-T-0090` | keep | final promotion verdict and nearest-wrong rejection should stay adjacent without making rejection a separate prerequisite in every verdict |
| `AOA-T-0089 complements AOA-T-0076` | keep | quest promotion is later and narrower than generic owner-layer triage |
| `AOA-T-0090 complements AOA-T-0089` | keep | nearest-wrong rejection can sharpen promotion review, but it can also sharpen other chosen owner verdicts |
| `AOA-T-0090 complements AOA-T-0076` | keep | owner triage already names one nearest wrong target, while this guardrail isolates that rejection move |
| `AOA-T-0101 complements AOA-T-0076` | keep | adoption gate assumes a local owner surface is in view but does not require generic owner-layer triage as the source |
| `AOA-T-0101 complements AOA-T-0090` | keep | nearest-wrong rejection can clarify adoption pressure, but adoption gate owns adopt/shadow/quarantine/defer/reject posture |
| `AOA-T-0102 complements AOA-T-0040` | keep | skill proposal handoff can benefit from skill-vs-command boundary, but it stops before skill acceptance or command design |
| `AOA-T-0102 complements AOA-T-0087` | keep | first landing can choose a skill-shaped destination, while this packet assumes skill proposal pressure already exists |
| `AOA-T-0102 complements AOA-T-0101` | keep | local adoption pressure can expose skill-shaped needs, but a skill proposal can also come from a technique candidate before local adoption |
| `AOA-T-0103 complements AOA-T-0101` | keep | retention starts after adoption or shadow use, but the upstream record can be equivalent local owner evidence |
| `AOA-T-0103 complements AOA-T-0090` | keep | nearest-wrong rejection can clarify retention choices, but retention owns the current evidence review |
| `AOA-T-0103 used_together_for AOA-T-0104` | repair | `route_to_obsolescence` is an explicit retention verdict and `AOA-T-0104` owns the route packet that can follow it |
| `AOA-T-0104 used_together_for AOA-T-0103` | keep | obsolescence routing normally follows retention review without requiring that every obsolescence pressure come from this exact review |
| `AOA-T-0104 complements AOA-T-0090` | keep | nearest-wrong rejection can clarify route labels, but obsolescence packet owns owner receipt, source evidence, rollback, and retained lesson |
| `AOA-T-0104 complements AOA-T-0076` | keep | owner-layer triage is generic placement; obsolescence route targets an already-owned practice under retirement pressure |

## Repair Gate

Accepted:

| bundle | old edge | new edge | why |
|---|---|---|---|
| `AOA-T-0103` | no direct edge to `AOA-T-0104` | `used_together_for AOA-T-0104` | retention review can emit `route_to_obsolescence`; obsolescence route packet owns the bounded handoff that follows that verdict |

Held:

| pressure | hold reason |
|---|---|
| `AOA-T-0087 requires AOA-T-0086` | first landing asks for readiness classification or equivalent evidence; it should not require the exact fit-matrix bundle |
| `AOA-T-0088 requires AOA-T-0086` | approval sensitivity should not re-create a hidden automation-readiness chain; the fit matrix already points toward the approval check |
| `AOA-T-0089 requires AOA-T-0090` | promotion review should keep rejection visible, but a verdict can carry nearest-wrong reasoning inline without requiring a separate guardrail invocation |
| `AOA-T-0102 requires AOA-T-0101` | skill proposal can follow adoption pressure, but it can also start from a technique candidate or equivalent adoption review |
| `AOA-T-0103 requires AOA-T-0101` | retention needs an adoption or shadow-use record, not necessarily the local-pattern-adoption-gate technique itself |
| `AOA-T-0104 requires AOA-T-0103` | obsolescence usually follows retention, but another owner review may already provide equivalent obsolescence pressure |
| broad `automation-governance` relation weave | the rejected bulk shelf should not be reintroduced as cross-shelf dependency law |
| new sequence vocabulary | Wave D needs one bounded `used_together_for` repair, not new `follows`, `precedes`, or lifecycle relation types |

## Axis Usefulness

| axis | value in Wave D | limit |
|---|---|---|
| `domain` | all twelve leaves remain `agent-workflows`, proving domain alone cannot navigate governance split shelves | not a path or family substitute |
| `kind` | separates assessment, guardrail, and handoff shapes inside governance | not enough to distinguish owner triage, automation fit, promotion verdict, and retention review |
| tree shelf | strongest human and agent neighborhood boundary for the split shelves | shelf placement does not create one lifecycle or automation-governance law |
| `execution_profile` | surfaces small-agent candidates such as nearest-wrong rejection and skill-proposal packet | scout suitability, not empirical local-agent proof |
| `risk_posture` | highlights approval, public-share, degraded, mutating, and irreversible pressure | cannot decide relation direction by itself |
| `relations` | useful for one-step adjacent routing and exact object/flow dependency | should remain bounded direct edges, not graph traversal, scheduling, or owner authority |

## What Changed

- added this Wave D review packet;
- routed one direct repair:
  `AOA-T-0103 used_together_for AOA-T-0104`;
- preserved the four governance split shelves as distinct selector
  neighborhoods.

## What Did Not Change

- no relation schema migration;
- no new relation types;
- no relation rationale fields;
- no generated graph behavior, traversal, scoring, or ranking;
- no status, `domain`, `kind`, path, family, capability, substrate,
  execution-profile, risk, maturity, evidence, or owner changes;
- no canonical promotion;
- no empirical small-agent proof claim.

## Public-Safety Read

The review uses existing public bundle text, generated public repo surfaces, and
sanitized review language. It does not include credential material, non-public
topology, operational hostnames, internal runtime details, or non-public donor
material. Governance, approval, skill, route, memory, runtime, and public-share
terms are review subjects only; they do not expose operational details.

## Next Honest Move

Land Wave D with the `AOA-T-0103` direct relation repair, regenerated relation
consumers, and narrow validation.

After landing, continue the temporary plan with Wave E:
`continuity/review-compaction`, `continuity/donor-harvest`,
`recovery/diagnosis-repair`, and `recovery/antifragility-recovery`.
