# Selector Relation Wave A Proof Execution Review

Source packet: [Technique Reform Ingress](../README.md)

Temporary plan:
[Temporary Selector Relation Long-Pass Plan](../TEMP_SELECTOR_RELATION_LONG_PASS_PLAN.md)

Prior calibration packets:
[Topology Selector Handoff-Continuation Pilot](topology-selector-handoff-continuation-mini-pilot.md),
[Relations Composition Handoff-Continuation Pilot](relations-composition-handoff-continuation-pilot.md),
[Handoff-Continuation Direct Relation Repair](handoff-continuation-direct-relation-repair.md)

Status: Wave A selector/relation review, with one accepted direct repair
candidate routed to
[Ready-Work-Graphs Direct Relation Repair](ready-work-graphs-direct-relation-repair.md).

## Verdict

Wave A is a good first long-pass wave.

The four shelves in scope already have enough authored clarity for a selector
to choose the right leaf after `domain`, `kind`, and tree placement find the
neighborhood:

- `proof/evaluation-chain`
- `proof/published-summary`
- `execution/intent-chain`
- `execution/ready-work-graphs`

The proof-side and intent-chain relations are already strong enough. They use
`requires`, `used_together_for`, `shares_contract_with`, and `complements` in
ways that match the bundle contracts.

The only source relation that needs strengthening in this wave is
`AOA-T-0050` -> `AOA-T-0049`. `AOA-T-0050` derives ready work from an existing
blocker graph. `AOA-T-0049` owns the local dependency graph contract. That is
object dependency, not ordinary adjacency, so the direct repair should move
from `complements AOA-T-0049` to `requires AOA-T-0049`.

No other bundle relation, status, `domain`, `kind`, path, scout axis, schema,
or generated rule should change from this wave.

## Phase 01 Inventory Result

The re-entry inventory confirmed the long-pass queue from current files rather
than session memory:

| shelf density | shelf |
|---:|---|
| `8` | `knowledge-lift/kag-source-lift` |
| `7` | `instruction/instruction-surface` |
| `7` | `continuity/handoff-continuation` |
| `6` | `history/history-artifacts` |
| `5` | `proof/owner-truth-closeout` |
| `5` | `ingest/media-ingest` |
| `5` | `execution/agent-workflows-core` |
| `4` | `recovery/diagnosis-repair`, `recovery/antifragility-recovery`, `proof/published-summary`, `instruction/docs-boundary`, `execution/runtime-truth-lifecycle`, `continuity/donor-harvest` |
| `3` | `proof/skill-support`, `proof/review-evidence`, `proof/evaluation-chain`, `instruction/capability-registry`, `instruction/capability-boundary`, `governance/promotion-boundary`, `governance/practice-adoption-lifecycle`, `governance/decision-routing`, `governance/automation-readiness`, `execution/ready-work-graphs`, `continuity/review-compaction` |
| `2` | `instruction/skill-discovery`, `governance/approval-evidence`, `execution/intent-chain` |
| `1` | `tool-use/tool-gateway` |

This supports the wave order in the temporary plan. Wave A stays small enough
to calibrate review rhythm while still touching real relation pressure.

## Sources Read

Direct bundle reads:

- [AOA-T-0003 contract-first-smoke-summary](../../../../../techniques/proof/evaluation-chain/contract-first-smoke-summary/TECHNIQUE.md)
- [AOA-T-0007 signal-first-gate-promotion](../../../../../techniques/proof/evaluation-chain/signal-first-gate-promotion/TECHNIQUE.md)
- [AOA-T-0032 context-report-for-ci](../../../../../techniques/proof/evaluation-chain/context-report-for-ci/TECHNIQUE.md)
- [AOA-T-0006 latest-alias-plus-history-copy](../../../../../techniques/proof/published-summary/latest-alias-plus-history-copy/TECHNIQUE.md)
- [AOA-T-0008 published-summary-remediation-snapshot](../../../../../techniques/proof/published-summary/published-summary-remediation-snapshot/TECHNIQUE.md)
- [AOA-T-0010 telemetry-integrity-snapshot](../../../../../techniques/proof/published-summary/telemetry-integrity-snapshot/TECHNIQUE.md)
- [AOA-T-0011 required-vs-optional-source-rendering](../../../../../techniques/proof/published-summary/required-vs-optional-source-rendering/TECHNIQUE.md)
- [AOA-T-0004 intent-plan-dry-run-contract-chain](../../../../../techniques/execution/intent-chain/intent-plan-dry-run-contract-chain/TECHNIQUE.md)
- [AOA-T-0005 new-intent-rollout-checklist](../../../../../techniques/execution/intent-chain/new-intent-rollout-checklist/TECHNIQUE.md)
- [AOA-T-0049 dependency-aware-task-graph](../../../../../techniques/execution/ready-work-graphs/dependency-aware-task-graph/TECHNIQUE.md)
- [AOA-T-0050 ready-work-from-blocker-graph](../../../../../techniques/execution/ready-work-graphs/ready-work-from-blocker-graph/TECHNIQUE.md)
- [AOA-T-0055 requirements-design-tasks-ladder](../../../../../techniques/execution/ready-work-graphs/requirements-design-tasks-ladder/TECHNIQUE.md)

Supporting review and generated surfaces:

- [Technique Selection](../../../../../docs/TECHNIQUE_SELECTION.md)
- [Selection Patterns](../../../../../docs/SELECTION_PATTERNS.md)
- [Technique Topology Scout](../../../../../reports/technique_topology_scout.md)
- [Evaluation-Chain Semantic Review](../../../../../docs/EVALUATION_CHAIN_SEMANTIC_REVIEW.md)
- [Published-Summary Semantic Review](../../../../../docs/PUBLISHED_SUMMARY_SEMANTIC_REVIEW.md)
- [Intent-Chain Semantic Review](../../../../../docs/INTENT_CHAIN_SEMANTIC_REVIEW.md)
- [Ready-Work-Graphs Direct-Read Migration Review](ready-work-graphs-direct-read-migration-review.md)
- [Landed Ready-Work-Graphs Pilot Review](landed-ready-work-graphs-pilot-review.md)

## Selector Prompts

| selector prompt | first correct pick | why adjacent leaves lose |
|---|---|---|
| "A smoke path needs one stable machine-readable output so CI and agents stop scraping logs." | `AOA-T-0003` | latest/history storage, gate rollout, and downstream rendering all assume a summary already exists |
| "An observed check should move from report-only to one narrow hard gate while diagnostics remain published." | `AOA-T-0007` | summary production alone is upstream; storage layout alone does not own staged enforcement |
| "A context composition job needs a CI-facing source coverage and token drift report." | `AOA-T-0032` | it observes composition quality; it does not compose context or aggregate published remediation summaries |
| "A summary producer needs a stable latest alias and a per-run history copy without double counting." | `AOA-T-0006` | remediation, integrity, and rendering policies consume published summaries but do not own storage layout |
| "Several published summaries should become one bounded follow-up backlog." | `AOA-T-0008` | integrity verdict asks whether interpretation is trustworthy; rendering policy handles required/optional source behavior |
| "Several published summaries need one trust verdict over telemetry and artifact-layout invariants." | `AOA-T-0010` | remediation asks what to follow up; rendering policy does not validate integrity |
| "A report should fail on required summary sources but degrade gracefully when optional sources are absent." | `AOA-T-0011` | remediation and integrity may be optional inputs; this leaf owns consumer rendering policy |
| "An automation system needs to turn intent into a plan, run dry-run only, and publish contract artifacts." | `AOA-T-0004` | rollout checklist assumes this chain already exists; plan-diff-apply governs the later implementation change |
| "One new intent type must be added to an existing dry-run chain without drift." | `AOA-T-0005` | it extends an existing chain; it does not define the base chain |
| "Multi-step work needs explicit task nodes and blocker edges so readiness is not memory-based." | `AOA-T-0049` | ready queue derivation assumes a graph; requirements/design/task ladder is pre-graph planning |
| "There is already a blocker graph; derive the next queue from blocker-free nodes." | `AOA-T-0050` | graph authoring is upstream; full execution workflow and broad prioritization stay outside this leaf |
| "Planning needs distinct requirements, design, and task layers before implementation." | `AOA-T-0055` | graph and queue leaves coordinate ready work; this leaf owns the pre-execution planning ladder |

## Relation Read

| relation | verdict | reason |
|---|---|---|
| `AOA-T-0003 used_together_for AOA-T-0006` | keep | summary production can pair naturally with latest/history storage without requiring storage for every smoke summary |
| `AOA-T-0003 used_together_for AOA-T-0007` | keep | the summary producer often travels with staged gate promotion but remains independently useful |
| `AOA-T-0006 requires AOA-T-0003` | keep | latest/history storage needs an existing summary payload |
| `AOA-T-0006 used_together_for AOA-T-0007` | keep | storage and gate rollout often share an operating path without the storage leaf owning promotion |
| `AOA-T-0006 shares_contract_with AOA-T-0008` | keep | both rely on stable published summaries, but remediation is not a storage-layout dependency in the reverse direction |
| `AOA-T-0006 shares_contract_with AOA-T-0010` | keep | both rely on stable published summaries, while integrity remains its own diagnostic layer |
| `AOA-T-0007 requires AOA-T-0003` | keep | staged promotion needs a summary-producing signal |
| `AOA-T-0007 requires AOA-T-0006` | keep | promotion readiness depends on trustworthy latest/history accumulation |
| `AOA-T-0008 requires AOA-T-0006` | keep | remediation snapshot reads published latest summaries |
| `AOA-T-0010 requires AOA-T-0006` | keep | integrity verdict checks published summary layout and invariants |
| `AOA-T-0011 complements AOA-T-0008` | keep | rendering policy consumes optional remediation surfaces without requiring that exact artifact in every use |
| `AOA-T-0011 complements AOA-T-0010` | keep | rendering policy consumes optional integrity surfaces without becoming integrity validation |
| `AOA-T-0004 used_together_for AOA-T-0005` | keep | base chain and rollout checklist travel together, but the base chain does not require a new rollout |
| `AOA-T-0005 requires AOA-T-0004` | keep | rollout checklist explicitly assumes an existing intent-plan-dry-run chain |
| `AOA-T-0049 complements AOA-T-0001` | keep | graph coordination supports a bounded execution workflow but is not the workflow itself |
| `AOA-T-0050 complements AOA-T-0049` | repair | ready queue derivation requires an existing blocker graph, and `AOA-T-0049` owns that local graph contract |
| `AOA-T-0050 complements AOA-T-0001` | keep | selecting ready work supports later plan/diff/apply/verify/report without requiring that exact workflow |
| `AOA-T-0055 complements AOA-T-0001` | keep | planning ladder prepares implementation but does not require the full execution protocol as an object dependency |

## Repair Gate

Accepted:

| bundle | old edge | new edge | why |
|---|---|---|---|
| `AOA-T-0050` | `complements AOA-T-0049` | `requires AOA-T-0049` | the ready queue technique takes an explicit blocker graph as input; `AOA-T-0049` owns the local dependency graph contract |

Held:

| pressure | hold reason |
|---|---|
| `AOA-T-0011 requires AOA-T-0008` or `AOA-T-0010` | optional remediation and integrity surfaces are common examples, not mandatory inputs for every required/optional rendering policy |
| `AOA-T-0049 requires AOA-T-0055` | task graphs can be authored without a requirements/design/tasks ladder; the ladder is a useful planning neighbor, not a strict prerequisite |
| `AOA-T-0055 requires AOA-T-0001` | later execution needs a separate workflow, but this planning ladder does not require the `AOA-T-0001` protocol to exist first |
| new sequence vocabulary | existing `requires`, `complements`, `used_together_for`, and `shares_contract_with` are sufficient for Wave A |

## Axis Usefulness

| axis | value in Wave A | limit |
|---|---|---|
| `domain` | separates proof/evaluation leaves from execution leaves | not enough to choose inside `evaluation` or `agent-workflows` alone |
| `kind` | helps distinguish validation, guardrail, artifact, lift, and workflow shape | several execution leaves remain `workflow`, so shelf and relation read still matter |
| tree shelf | provides the most useful neighborhood boundary | shelf placement does not prove relation direction |
| `execution_profile` | correctly shows small read-only proof leaves versus orchestration-heavy published-summary leaves | still scout suitability, not local model proof |
| `risk_posture` | helps protect mutating/public-share summary patterns from being treated as simple checks | not a substitute for reading contracts |
| `relations` | strong for selector next-step routing when direct dependency exists | must remain direct edges, not graph traversal or ranking |

## What Changed

- `AOA-T-0050` is routed to a direct relation repair from
  `complements AOA-T-0049` to `requires AOA-T-0049`.

## What Did Not Change

- no relation schema migration;
- no new relation types;
- no relation rationale fields;
- no generated graph behavior, traversal, scoring, or ranking;
- no status, `domain`, `kind`, path, family, capability, substrate,
  execution-profile, risk, maturity, evidence, or owner changes;
- no empirical small-agent proof claim.

## Public-Safety Read

The review uses existing public bundle text, generated public repo surfaces, and
sanitized review language. It does not include private paths, secrets,
operational hostnames, internal runtime details, or non-public donor material.

## Next Honest Move

Land Wave A with the `AOA-T-0050` direct relation repair, regenerated relation
consumers, and narrow validation.

After landing, continue the temporary plan with Wave B:
`instruction/instruction-surface`, `knowledge-lift/kag-source-lift`,
`instruction/docs-boundary`, and `proof/skill-support`.

