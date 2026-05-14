# Selector Relation Wave E Continuity Recovery Review

Source packet: [Technique Reform Ingress](../README.md)

Closeout ledger:
[Selector Relation Long-Pass Closeout Ledger](selector-relation-long-pass-closeout-ledger.md)

Prior wave:
[Selector Relation Wave D Governance Split Review](selector-relation-wave-d-governance-split-review.md)

Status: Wave E selector/relation review, with one accepted direct relation
repair routed to
[Diagnosis-Repair Direct Relation Repair](diagnosis-repair-direct-relation-repair.md).

## Verdict

Wave E keeps the continuity and recovery shelves legible while accepting one
small relation repair inside `recovery/diagnosis-repair`.

The shelves in scope stay separate:

- `continuity/review-compaction`
- `continuity/donor-harvest`
- `recovery/diagnosis-repair`
- `recovery/antifragility-recovery`

Direct reading confirms that review compaction preserves review or capability
context across compression boundaries, donor harvest preserves reviewed-session
objects across closeout, diagnosis-repair turns reviewed friction into bounded
repair shape, and antifragility-recovery keeps stress events receipt-backed and
weaker than normal operation.

One direct relation repair is justified: `AOA-T-0082 requires AOA-T-0081`.
`AOA-T-0082` explicitly starts from a reviewed diagnosis packet, and
`AOA-T-0081` owns that local diagnosis-packet contract. The edge is an object
dependency only. It does not turn taxonomy, diagnosis, repair shape, checkpoint
posture, approval, or recovery into one permission chain.

No other bundle relation, status, `domain`, `kind`, path, scout axis, schema,
or generated graph behavior should change from this wave.

## Sources Read

Direct bundle reads:

- [AOA-T-0051 commit-triggered-background-review](../../../../../techniques/continuity/review-compaction/commit-triggered-background-review/TECHNIQUE.md)
- [AOA-T-0052 review-findings-compaction](../../../../../techniques/continuity/review-compaction/review-findings-compaction/TECHNIQUE.md)
- [AOA-T-0054 compaction-resilient-skill-loading](../../../../../techniques/continuity/review-compaction/compaction-resilient-skill-loading/TECHNIQUE.md)
- [AOA-T-0075 session-donor-harvest](../../../../../techniques/continuity/donor-harvest/session-donor-harvest/TECHNIQUE.md)
- [AOA-T-0077 harvest-packet-contract](../../../../../techniques/continuity/donor-harvest/harvest-packet-contract/TECHNIQUE.md)
- [AOA-T-0084 progression-evidence-lift](../../../../../techniques/continuity/donor-harvest/progression-evidence-lift/TECHNIQUE.md)
- [AOA-T-0085 multi-axis-quest-overlay](../../../../../techniques/continuity/donor-harvest/multi-axis-quest-overlay/TECHNIQUE.md)
- [AOA-T-0080 session-drift-taxonomy](../../../../../techniques/recovery/diagnosis-repair/session-drift-taxonomy/TECHNIQUE.md)
- [AOA-T-0081 diagnosis-from-reviewed-evidence](../../../../../techniques/recovery/diagnosis-repair/diagnosis-from-reviewed-evidence/TECHNIQUE.md)
- [AOA-T-0082 repair-shape-from-diagnosis](../../../../../techniques/recovery/diagnosis-repair/repair-shape-from-diagnosis/TECHNIQUE.md)
- [AOA-T-0083 checkpoint-bound-self-repair](../../../../../techniques/recovery/diagnosis-repair/checkpoint-bound-self-repair/TECHNIQUE.md)
- [AOA-T-0097 degrade-reground-recover](../../../../../techniques/recovery/antifragility-recovery/degrade-reground-recover/TECHNIQUE.md)
- [AOA-T-0098 receipt-first-failure-analysis](../../../../../techniques/recovery/antifragility-recovery/receipt-first-failure-analysis/TECHNIQUE.md)
- [AOA-T-0099 isolated-service-stop-on-shared-substrate](../../../../../techniques/recovery/antifragility-recovery/isolated-service-stop-on-shared-substrate/TECHNIQUE.md)
- [AOA-T-0100 stress-receipt-reground-closeout](../../../../../techniques/recovery/antifragility-recovery/stress-receipt-reground-closeout/TECHNIQUE.md)

Supporting review and generated surfaces:

- [Technique Selection](../../../../../docs/TECHNIQUE_SELECTION.md)
- [Technique Topology Scout](../reports/technique_topology_scout.md)
- [Technique Tree Projection](../reports/technique_tree_projection.md)
- [Review-Compaction Direct-Read Migration Review](review-compaction-direct-read-migration-review.md)
- [Landed Review-Compaction Pilot Review](landed-review-compaction-pilot-review.md)
- [Donor-Harvest Direct-Read Migration Review](donor-harvest-direct-read-migration-review.md)
- [Landed Donor-Harvest Pilot Review](landed-donor-harvest-pilot-review.md)
- [Diagnosis-Repair Direct-Read Migration Review](diagnosis-repair-direct-read-migration-review.md)
- [Landed Diagnosis-Repair Pilot Review](landed-diagnosis-repair-pilot-review.md)
- [Antifragility-Recovery Direct-Read Migration Review](antifragility-recovery-direct-read-migration-review.md)
- [Landed Antifragility-Recovery Pilot Review](landed-antifragility-recovery-pilot-review.md)
- [Topology Selector Handoff-Continuation Mini-Pilot](topology-selector-handoff-continuation-mini-pilot.md)
- [Relations Composition Handoff-Continuation Pilot](relations-composition-handoff-continuation-pilot.md)
- [Handoff-Continuation Direct Relation Repair](handoff-continuation-direct-relation-repair.md)

## Selector Prompts

| selector prompt | first correct pick | why adjacent leaves lose |
|---|---|---|
| "A commit boundary should start a bounded background review whose findings survive as an artifact." | `AOA-T-0051` | review findings compaction starts after findings exist; change protocol is broader |
| "Several review runs produced repeated or stale findings that need one current surface." | `AOA-T-0052` | background review launches a run; audit closeout owns owner fix and proof |
| "After context compaction, the agent needs to restore only needed skill availability from canonical sources." | `AOA-T-0054` | handoff packets carry work state; this restores capability discoverability |
| "A reviewed session artifact may contain reusable practice, workflow, or scenario candidates." | `AOA-T-0075` | harvest-packet contract preserves shape after extraction; owner triage chooses a target |
| "A downstream reader needs a compact `HARVEST_PACKET` spine over reviewed extracts." | `AOA-T-0077` | donor harvest chooses candidates; decision fork cards choose routes from a surfaced packet or equivalent evidence |
| "Reviewed session evidence should become a bounded multi-axis progression delta." | `AOA-T-0084` | quest overlay is optional reflection; donor harvest extracts reusable units |
| "A bounded progression or route reflection needs a small quest-shaped overlay without owner authority." | `AOA-T-0085` | progression lift owns the evidence delta; decision fork cards own visible route alternatives |
| "Repeated post-session friction needs a bounded drift label before probable causes are claimed." | `AOA-T-0080` | diagnosis packet owns symptoms, causes, owner hints, and unknowns |
| "Reviewed friction evidence should become one diagnosis packet without mutation." | `AOA-T-0081` | taxonomy is optional classifier; repair shaping starts only after diagnosis exists |
| "A reviewed diagnosis packet must become the smallest honest repair shape." | `AOA-T-0082` | diagnosis explains the problem; checkpoint-bound self-repair governs later repair posture |
| "A chosen repair shape needs approval, rollback, health checks, and iteration limits visible." | `AOA-T-0083` | repair shaping chooses the artifact; approval sensitivity is automation-candidate posture |
| "A degraded helper path can continue only in a weaker, source-regrounded mode." | `AOA-T-0097` | failure analysis is post-event review; stress closeout is broader route closeout |
| "Failure review should begin from owner-local stress receipts and separate facts from hypotheses." | `AOA-T-0098` | degraded recovery may produce receipts; contract tests are proof-design neighbors |
| "One runtime-adjacent service must stop while shared substrate continuity remains verified." | `AOA-T-0099` | degraded-mode recovery is broader; lifecycle start/stop is not substrate-specific recovery closeout |
| "A bounded stress event needs receipt, smallest honest continuation or hold, regrounding, and reviewed closeout." | `AOA-T-0100` | degraded recovery owns the immediate posture; failure analysis owns later receipt-first review |

## Relation Read

| relation | verdict | reason |
|---|---|---|
| `AOA-T-0051 complements AOA-T-0001` | keep | background review can sit after a change protocol, but commit-triggered review is narrower and can be wired by equivalent commit discipline |
| `AOA-T-0052 complements AOA-T-0051` | keep | compaction needs review findings, not necessarily the commit-triggered review producer |
| `AOA-T-0054 complements AOA-T-0040` | keep | capability boundary supports skill reloading, but post-compaction recovery can read equivalent canonical skill surfaces |
| `AOA-T-0075 complements AOA-T-0076` | keep | owner-layer triage commonly follows donor extraction, but donor harvest can stop at candidates |
| `AOA-T-0075 complements AOA-T-0044` | keep | versionable transcripts can feed harvest, but reviewed session artifacts can arrive through other stable surfaces |
| `AOA-T-0077 complements AOA-T-0075` | keep | harvest-packet shape often follows extraction, but the packet can be assembled from reviewed extracts already in hand |
| `AOA-T-0077 complements AOA-T-0076` | keep | owner triage can consume packet fields without turning the packet into owner routing |
| `AOA-T-0084 complements AOA-T-0085` | keep | progression delta and quest overlay pair well, but overlay remains optional and weaker than the reviewed base |
| `AOA-T-0084 complements AOA-T-0075` | keep | donor harvest can feed progression lift, but progression can start from reviewed session evidence directly |
| `AOA-T-0085 complements AOA-T-0084` | keep | the overlay usually needs a bounded base, but that base can be progression delta or equivalent route reflection |
| `AOA-T-0085 complements AOA-T-0078` | keep | route cards can feed reflection without making quest overlay route authority |
| `AOA-T-0080 complements AOA-T-0081` | keep | taxonomy helps diagnosis, but diagnosis can start from reviewed symptoms without a separate taxonomy pass |
| `AOA-T-0080 complements AOA-T-0076` | keep | owner hints may use placement discipline; drift taxonomy does not own owner routing |
| `AOA-T-0081 complements AOA-T-0080` | keep | taxonomy is useful but optional input to diagnosis |
| `AOA-T-0081 complements AOA-T-0082` | keep | diagnosis often feeds repair shaping, but diagnosis can end as read-only evidence |
| `AOA-T-0082 requires AOA-T-0081` | repair | repair-shape-from-diagnosis explicitly requires a reviewed diagnosis packet and `AOA-T-0081` owns the local packet contract |
| `AOA-T-0082 complements AOA-T-0083` | keep | checkpoint posture follows some repair shapes, but repair shaping should not own approval or iteration posture |
| `AOA-T-0083 complements AOA-T-0082` | keep | checkpoint-bound self-repair needs a bounded repair shape, but that shape can come from equivalent reviewed repair planning |
| `AOA-T-0083 complements AOA-T-0028` | keep | checkpoint posture and confirmation-gated mutation are adjacent approval seams, not the same gate |
| `AOA-T-0097 complements AOA-T-0098` | keep | degraded recovery emits receipts that can feed failure analysis, but analysis can start from any owner-local receipt set |
| `AOA-T-0098 complements AOA-T-0097` | keep | receipt-first review often follows degraded recovery, but it should not require this exact degraded-mode technique |
| `AOA-T-0098 complements AOA-T-0015` | keep | contract-test design can support future checks, while failure analysis remains receipt-first review |
| `AOA-T-0099 complements AOA-T-0097` | keep | isolated stop may be one degraded recovery case, but it is a bounded mutation seam with its own target/substrate contract |
| `AOA-T-0100 complements AOA-T-0097` | keep | stress closeout can include degraded continuation, but it owns a broader closeout lane |
| `AOA-T-0100 complements AOA-T-0098` | keep | receipt-first analysis can follow closeout, but closeout itself should not compute a later proof verdict |

## Repair Gate

Accepted:

| bundle | old edge | new edge | why |
|---|---|---|---|
| `AOA-T-0082` | `complements AOA-T-0081` | `requires AOA-T-0081` | the technique starts from one reviewed diagnosis packet, and `AOA-T-0081` owns the local diagnosis-packet contract |

Held:

| pressure | hold reason |
|---|---|
| `AOA-T-0052 requires AOA-T-0051` | review findings can come from any stable reviewed pass, not only commit-triggered background review |
| `AOA-T-0077 requires AOA-T-0075` | the packet needs reviewed extracts, not necessarily this exact donor-harvest extraction technique |
| `AOA-T-0084 requires AOA-T-0075` | progression lift can start from reviewed session evidence or a harvest packet |
| `AOA-T-0085 requires AOA-T-0084` | quest overlay needs a bounded base, but the base can be an equivalent route or progression reflection |
| `AOA-T-0081 requires AOA-T-0080` | drift taxonomy is useful but optional; diagnosis can proceed from reviewed symptoms directly |
| `AOA-T-0083 requires AOA-T-0082` | checkpoint posture wraps a bounded repair shape, which can come from equivalent reviewed planning; do not turn repair into a full permission chain |
| `AOA-T-0098 requires AOA-T-0097` | failure analysis starts from receipts, not necessarily this exact degraded-mode producer |
| `AOA-T-0100 requires AOA-T-0097` or `AOA-T-0098` | stress closeout can use degraded posture and later receipt review, but it owns its own closeout sequence and does not compute later proof |
| new sequence vocabulary | Wave E needs one `requires` object edge, not new `follows`, `precedes`, lifecycle, or receipt-chain relation types |

## Axis Usefulness

| axis | value in Wave E | limit |
|---|---|---|
| `domain` | shows that continuity and recovery shelves still carry `agent-workflows`, `system-recovery`, and `validation-patterns` frontmatter truth | cannot choose the right leaf inside migrated tree shelves |
| `kind` | separates workflow, handoff, lift, assessment, recovery, and validation shapes | cannot alone distinguish reviewed-session donor packets from progression or recovery packets |
| tree shelf | strongest first selector neighborhood for compaction, donor objects, diagnosis repair, and stress recovery | shelf placement does not create one mandatory sequence |
| `execution_profile` | highlights small-agent candidates in donor and continuity packets while keeping recovery orchestration visible | scout suitability, not empirical local-agent proof |
| `risk_posture` | helps prevent approval, mutation, degraded-mode, and external-evidence pressure from being hidden | risk posture cannot justify a relation without direct object dependency |
| `relations` | useful for one-step object and neighbor inspection | should remain direct edges, not full recovery flow, approval ladder, proof verdict, or memory truth |

## What Changed

- added this Wave E review packet;
- routed one direct repair:
  `AOA-T-0082 requires AOA-T-0081`;
- preserved review compaction, donor harvest, diagnosis-repair, and
  antifragility-recovery as distinct selector neighborhoods.

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

The review uses existing public bundle text, generated public repo surfaces,
and sanitized review language. It avoids non-public donor material, live
machine details, operational endpoints, and local environment specifics.
Recovery, approval, receipt, runtime, and public-share terms are review
subjects only; they do not expose operational detail.

## Next Honest Move

Land Wave E with the `AOA-T-0082` direct relation repair, regenerated relation
consumers, and narrow validation.

After landing, continue the temporary plan with Wave F:
`instruction/capability-registry`, `instruction/capability-boundary`,
`instruction/skill-discovery`, `ingest/media-ingest`, and
`history/history-artifacts`.
