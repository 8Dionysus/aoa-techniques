# Temporary Selector Relation Long-Pass Plan

Source packet: [Technique Reform Ingress](README.md)

Status: temporary working plan. This file is a rhythm anchor for the next
selector/relation long pass. It is not a review packet, not bundle authority,
not a schema migration, not a generated surface, and not a frontmatter
promotion plan.

Disposition rule: when the long pass closes, distill the stage log, durable
verdicts, repair decisions, holds, and next-route guidance into review packets
and a closeout ledger, then remove this temporary plan in the closeout wave.

## Current Entry State

- corpus: `107` current bundles
- tree: `10` trunks, `28` shelves, `107` leaf bundles
- current authoritative frontmatter axes: `domain`, `kind`, direct
  `relations`
- scout/design axes: `family`, `capability_class`, `substrate`,
  `execution_profile`, `risk_posture`
- selector pilot already landed:
  `continuity/handoff-continuation`
- relation pilot already landed:
  `continuity/handoff-continuation`
- direct relation repair already landed:
  `AOA-T-0058 requires AOA-T-0057` and
  `AOA-T-0059 requires AOA-T-0057`
- no new relation types, graph behavior, ranking, schema fields, status,
  domain, kind, or path changes are currently authorized
- empirical small-agent proof remains routed to `aoa-evals`, not this pass

## Purpose

Run a long, careful selector/relation pass across the current technique tree.
The pass should test whether a reader or orchestrator can select the correct
leaf inside dense shelves after `domain`, `kind`, and tree placement have found
the neighborhood.

The pass should also identify direct relation repairs only when bundle inputs,
outputs, contracts, or validation sections justify one existing relation type.

The intended result is not a bulk rewrite. The intended result is a disciplined
sequence of shelf-local review packets, exact repair gates, and closeout
evidence strong enough to support later technique restructuring.

## Working Law

1. Authored bundle meaning outranks generated projections.
2. `domain` and `kind` remain current frontmatter truth.
3. The tree path is current authored placement, not a required frontmatter
   field.
4. Scout axes are review pressure only.
5. Relations are direct typed edges only.
6. Selector prompts are evidence for review, not automatic mutation.
7. Repair candidates must name exact bundles, exact old/new edges, and exact
   source-contract evidence.
8. No new relation vocabulary may be introduced inside this long pass.
9. No model-proof claim may be made from static review.
10. Every durable wave must leave a review packet or an explicit no-repair
    receipt.

## Relation Type Discipline

Use only existing relation types:

- `requires`: one technique usually needs another contract or object already
  present.
- `complements`: the two techniques strengthen each other without strict
  dependency.
- `supersedes`: one technique intentionally replaces an older technique.
- `conflicts_with`: using both would create a false or unsafe operating path.
- `used_together_for`: the pair commonly appears in one operating path without
  strict dependency.
- `derived_from`: one technique was lifted from another source technique or
  pattern.
- `shares_contract_with`: neighboring techniques rely on the same bounded
  contract but do different work.

Hold pressure instead of mutating when the desired relation sounds like
`follows`, `alternative`, `narrows`, `generalizes`, `produces-input-for`, or
`consumes-output-of`. Those names may become future design evidence, but not
frontmatter in this pass.

## Context Recovery Procedure

Use this when context compacts or another agent resumes the pass.

1. Read repository root `AGENTS.md`.
2. Read `aoa-techniques/AGENTS.md`.
3. Read `mechanics/AGENTS.md`.
4. Read `mechanics/distillation/AGENTS.md`.
5. Read this file.
6. Read `mechanics/distillation/parts/technique-reform-ingress/README.md`.
7. Read the latest review packet listed in the stage log.
8. Run `git status --short --branch`.
9. Rebuild only the minimum local context needed for the current wave.
10. Continue from the first unchecked stage entry; do not restart the broad
    audit unless the stage log proves the plan is stale.

## Checkpoint Rhythm

At the start of each phase:

1. Mark the phase as active in the stage log.
2. Name the exact shelves or bundles in scope.
3. Name the surfaces to read.
4. Name the mutation stop line before editing.

Inside each shelf:

1. Read every `TECHNIQUE.md` in the shelf.
2. Read `checks/`, `examples/`, and `notes/` only when they clarify selector
   or relation pressure.
3. Read generated catalog, selection, scout, and capsule rows as secondary
   evidence.
4. Write selector prompts before judging relation edits.
5. Record why adjacent leaves lose.
6. Separate selection confusion from relation mutation.
7. Carry holds explicitly.

At the end of each wave:

1. Write or update one review packet under `reviews/`.
2. If source relations changed, rebuild generated catalog/selection surfaces
   from source.
3. Run the narrow validation named by touched surfaces.
4. Update this plan's stage log.
5. If the wave is complete and durable, land it cleanly through the established
   commit, push, and merge rhythm before starting the next wave.

## Branch Rules

If selector prompts fail because summaries or capsule rows are weak:

1. confirm whether `TECHNIQUE.md` itself is clear;
2. if source is clear, route to generated-reader or capsule-builder repair;
3. if source is unclear, carry a bundle-local repair candidate;
4. do not rewrite template shape broadly.

If relation pressure repeats across three or more shelves:

1. finish the current wave;
2. write a schema-pressure note in the wave review;
3. do not add new relation types;
4. reserve any vocabulary expansion for a later decision and validator wave.

If a shelf exposes hidden dependency on AoA center, skills, evals, routing,
memory, runtime, KAG, playbooks, agents, or stats:

1. record the owner-boundary route;
2. repair wording only when the technique itself becomes more portable;
3. do not import sibling-owner authority into technique meaning.

If a shelf is already clean:

1. record the clean selector result;
2. record relation holds;
3. move on without cosmetic edits.

If a direct relation repair is justified:

1. reread the exact source and target bundles;
2. name the old and new relation;
3. prove the relation with inputs, outputs, procedure, validation, or adjacent
   technique wording;
4. change only the exact relation edge;
5. rebuild generated consumers;
6. write a direct repair receipt.

## Stage Log

Use statuses: `pending`, `active`, `blocked`, `landed`, `distilled`.

| stage | status | durable output |
|---|---|---|
| 00 plan seed | landed | this temporary plan |
| 01 re-entry inventory | landed | inventory section in Wave A review |
| 02 Wave A selector/relation review | landed | [selector-relation-wave-a-proof-execution-review](reviews/selector-relation-wave-a-proof-execution-review.md) |
| 03 Wave A repair gate | landed | [ready-work-graphs-direct-relation-repair](reviews/ready-work-graphs-direct-relation-repair.md) |
| 04 Wave B selector/relation review | landed | [selector-relation-wave-b-instruction-knowledge-review](reviews/selector-relation-wave-b-instruction-knowledge-review.md) |
| 05 Wave B repair gate | landed | explicit no-repair hold in [selector-relation-wave-b-instruction-knowledge-review](reviews/selector-relation-wave-b-instruction-knowledge-review.md) |
| 06 Wave C selector/relation review | pending | Wave C review packet |
| 07 Wave C repair gate | pending | direct repair packet or explicit no-repair hold |
| 08 Wave D selector/relation review | pending | Wave D review packet |
| 09 Wave D repair gate | pending | direct repair packet or explicit no-repair hold |
| 10 Wave E selector/relation review | pending | Wave E review packet |
| 11 Wave E repair gate | pending | direct repair packet or explicit no-repair hold |
| 12 Wave F selector/relation review | pending | Wave F review packet |
| 13 Wave F repair gate | pending | direct repair packet or explicit no-repair hold |
| 14 residual singleton and cross-wave scan | pending | residual scan review |
| 15 closeout ledger | pending | final selector/relation closeout |
| 16 temporary plan disposition | pending | this file removed after distillation |

## Phase 00: Plan Seed

Goal: create the temporary rhythm anchor.

Steps:

1. Confirm the repo is clean before the file is created.
2. Read the latest selector pilot, relation pilot, direct relation repair, and
   execution-profile closeout.
3. Confirm current shelf list and density from the authored tree.
4. Confirm relation contract from `docs/BOUNDED_RELATION_LIFT_GUIDE.md`,
   `docs/TECHNIQUE_TOPOLOGY_CONTRACT.md`,
   `docs/TECHNIQUE_SELECTION_GUIDE.md`, and generated selection surfaces.
5. Create this file in the part root using the existing `TEMP_...` convention.
6. Run markdown/diff validation.
7. Stop after reporting the created plan unless the user has also asked to
   start Phase 01.

Exit condition: this file exists, names the wave order, and can recover the
long pass after context compaction.

## Phase 01: Re-Entry Inventory

Goal: rebuild exact current scope before the first wave.

Steps:

1. Reread this file.
2. Reread the current `technique-reform-ingress/README.md` latest contour.
3. List all current shelves with counts.
4. List current direct relations grouped by source shelf.
5. Identify shelves where `domain`, `kind`, and path find a neighborhood but
   not a single obvious leaf.
6. Compare generated `TECHNIQUE_SELECTION.md`, `SELECTION_PATTERNS.md`, and
   `reports/technique_topology_scout.md` against shelf-local reading needs.
7. Mark shelves as:
   - dense review needed;
   - relation pressure likely;
   - clean singleton or low-density hold;
   - owner-boundary watch.
8. Do not mutate bundles in this phase.
9. Update the stage log with inventory completion.

Exit condition: Wave A scope is confirmed against current files, not memory.

## Wave A: Proof And Execution Calibration

Scope:

- `proof/evaluation-chain`
- `proof/published-summary`
- `execution/intent-chain`
- `execution/ready-work-graphs`

Why first: these shelves already have strong selection surfaces and known
sequence pressure around summary production, promotion, rollout, and ready-work
graphs. They are small enough to calibrate long-pass rhythm without becoming
toy examples.

Steps:

1. Read all leaf `TECHNIQUE.md` files in the four shelves.
2. Read existing semantic reviews referenced by `SELECTION_PATTERNS.md`.
3. Read generated catalog and selection rows for each leaf.
4. Write six to ten selector prompts across the wave.
5. For each prompt, pick the first correct technique.
6. Record why nearby leaves lose.
7. Identify where `requires`, `used_together_for`, or `complements` already
   answer the selector path.
8. Identify any relation that is too weak or too strong.
9. Decide whether any exact relation repair is justified.
10. Write Wave A review packet.
11. If relation source changed, rebuild generated surfaces.
12. Run narrow validation.
13. Update this plan.
14. Land the wave if durable changes exist.

Repair gate:

- Accept only exact relation repairs supported by bundle contracts.
- Hold any pressure that needs new vocabulary or graph behavior.
- Do not change status, domain, kind, path, maturity, or scout axes.

## Wave B: Instruction And Knowledge-Lift Selector Stress

Scope:

- `instruction/instruction-surface`
- `knowledge-lift/kag-source-lift`
- `instruction/docs-boundary`
- `proof/skill-support`

Why second: these are dense and semantically close to the reusable-technique
identity of the repo. They test whether selector prompts can separate
instruction assembly, source-of-truth boundaries, KAG lifts, and skill-support
proof helpers without collapsing everything into docs doctrine.

Steps:

1. Read all leaf `TECHNIQUE.md` files in scope.
2. Read generated scout rows for capability, substrate, execution profile, and
   risk posture.
3. Read relation rows for KAG/source-lift and skill-support leaves.
4. Write selector prompts for:
   - deterministic context composition;
   - single-source fan-out;
   - nested rule loading;
   - source-of-truth layout;
   - KAG section lift;
   - metadata spine;
   - bounded relation lift;
   - contract test design;
   - property invariants;
   - bounded context mapping.
5. For every prompt, record the chosen leaf and nearest losing leaves.
6. Separate technique portability from AoA-specific instruction surfaces.
7. Identify relation candidates only when a leaf requires an object another
   leaf owns.
8. Check whether existing `shares_contract_with` or `used_together_for`
   semantics would be clearer than `complements`.
9. Write Wave B review packet.
10. Run repair gate.
11. Rebuild and validate if relations change.
12. Update this plan and land the wave if durable.

Repair gate:

- Do not turn KAG owner authority into technique graph authority.
- Do not make docs-boundary source-of-truth law into global AoA doctrine.
- Do not add rationale fields to relations.

## Wave C: Execution Core And Owner-Truth Boundary

Scope:

- `execution/agent-workflows-core`
- `execution/runtime-truth-lifecycle`
- `proof/owner-truth-closeout`
- `governance/approval-evidence`

Why third: these shelves carry high operational pressure. They need relation
discipline so plan/apply/verify/report, mutation gates, runtime truth, owner
closeout, and approval evidence stay adjacent without becoming one giant
workflow.

Steps:

1. Read all leaf bundles in scope.
2. Read checks/examples for mutating or approval-sensitive leaves.
3. Write selector prompts for:
   - plan/diff/apply/verify/report;
   - TDD slice;
   - confirmation-gated mutation;
   - shell-composable invocation;
   - runtime truth capture;
   - owner-truth closeout;
   - approval evidence receipt.
4. Record first correct picks and losing neighbors.
5. Mark relations that support safe preconditions.
6. Mark relations that would overstate approval, proof, runtime, or owner
   authority.
7. Decide whether direct relation repairs are needed.
8. Write Wave C review packet.
9. Run repair gate, rebuild, validate, update plan, and land if durable.

Repair gate:

- Keep approval evidence distinct from permission to mutate.
- Keep runtime truth lifecycle distinct from runtime ownership.
- Keep owner-truth closeout distinct from AoA constitutional authority.

## Wave D: Governance Split Shelves

Scope:

- `governance/decision-routing`
- `governance/automation-readiness`
- `governance/promotion-boundary`
- `governance/practice-adoption-lifecycle`

Why fourth: these shelves were already split out of a rejected bulk
automation-governance shelf. They need selector/relation review that preserves
the split and prevents hidden re-merging.

Steps:

1. Read all governance split leaves.
2. Reread automation-governance split review if needed for boundary memory.
3. Write selector prompts for:
   - local decision routing;
   - automation readiness;
   - promotion boundary;
   - practice adoption lifecycle.
4. Record why each split shelf should not absorb the others.
5. Check relation pressure across the split shelves.
6. Identify any false `requires` pressure that would recreate the rejected
   bulk shelf.
7. Identify any `used_together_for` candidate that helps operating path
   without ownership collapse.
8. Write Wave D review packet.
9. Run repair gate, rebuild, validate, update plan, and land if durable.

Repair gate:

- Do not create broad automation governance doctrine.
- Do not promote techniques to canonical status from this pass.
- Do not import playbook, runtime, memory, or role-contract authority.

## Wave E: Continuity And Recovery

Scope:

- `continuity/review-compaction`
- `continuity/donor-harvest`
- `recovery/diagnosis-repair`
- `recovery/antifragility-recovery`

Why fifth: handoff-continuation already proved the rhythm. This wave tests the
remaining continuity and recovery shelves where receipt, diagnosis, harvest,
compaction, and antifragility can easily blur.

Steps:

1. Read all leaf bundles in scope.
2. Reread handoff-continuation selector and relation packets for calibration.
3. Write selector prompts for:
   - review compaction;
   - donor harvest;
   - diagnosis before repair;
   - antifragility recovery;
   - failure receipts;
   - degraded continuation.
4. Record first correct picks and losing neighbors.
5. Identify relation candidates around evidence-before-repair,
   harvest-before-continuation, and receipt-before-closeout.
6. Reject any relation that turns evidence, approval, and repair into one
   permission chain.
7. Write Wave E review packet.
8. Run repair gate, rebuild, validate, update plan, and land if durable.

Repair gate:

- Keep recovery technique meaning narrower than system recovery ownership.
- Keep donor harvest distinct from memory truth and final provenance law.
- Keep review compaction distinct from handoff receipt.

## Wave F: Instruction Capability Tail, Media, History

Scope:

- `instruction/capability-registry`
- `instruction/capability-boundary`
- `instruction/skill-discovery`
- `ingest/media-ingest`
- `history/history-artifacts`

Why sixth: this wave combines remaining dense/medium shelves that test
external artifacts, registries, capabilities, media, and history without
promoting those neighboring owner systems into technique authority.

Steps:

1. Read all leaf bundles in scope.
2. Read examples/checks for media and history leaves where object shape matters.
3. Write selector prompts for:
   - capability registry entry;
   - capability boundary;
   - skill discovery;
   - media ingest;
   - history artifact capture;
   - local session indexing.
4. Record first correct picks and losing neighbors.
5. Identify object dependency edges, especially where one technique produces
   an artifact another validates or indexes.
6. Check for portability pressure where external systems are named.
7. Write Wave F review packet.
8. Run repair gate, rebuild, validate, update plan, and land if durable.

Repair gate:

- Do not create registry product doctrine.
- Do not import skill installer behavior.
- Do not treat history artifacts as memory truth.
- Do not turn media ingest into general data-platform ownership.

## Phase 14: Residual Singleton And Cross-Wave Scan

Scope:

- `tool-use/tool-gateway`
- any low-density shelves not adequately covered by earlier waves
- relation candidates held from Waves A through F

Steps:

1. Read singleton and residual leaf bundles directly.
2. Confirm whether singleton shelves need only no-repair receipts.
3. Re-scan all held relation candidates.
4. Group holds by reason:
   - new vocabulary pressure;
   - insufficient source-contract evidence;
   - sibling-owner boundary;
   - generated-reader issue;
   - bundle-local wording issue;
   - future empirical eval need.
5. Confirm that every changed relation has generated parity.
6. Confirm no hand-edited generated surfaces remain.
7. Confirm no broad template or frontmatter migration slipped in.
8. Write residual scan review.
9. Update this plan.
10. Land if durable.

Exit condition: no shelf remains unaccounted for in selector/relation scope.

## Phase 15: Closeout Ledger

Goal: turn the temporary rhythm into durable review memory.

Steps:

1. Read every wave packet.
2. Read every direct repair packet.
3. Count shelves covered.
4. Count bundles read.
5. Count selector prompts written.
6. Count relation repairs accepted.
7. Count relation repairs rejected or held.
8. Count generated surfaces rebuilt.
9. Count validations run.
10. Confirm no unauthorized schema, status, domain, kind, path, scout-axis, or
    relation-type changes happened.
11. Summarize lessons about selector axes.
12. Summarize lessons about relation composition.
13. Name any future decision notes needed.
14. Name any future schema-pressure thread.
15. Name any future bundle-local repair cohort.
16. Name any future eval-owner route.
17. Write final selector/relation closeout ledger under `reviews/`.
18. Update `technique-reform-ingress/README.md` with the new contour.
19. Run repository-level validation.
20. Land the closeout.

Exit condition: durable review surfaces explain the long pass without needing
this temporary plan.

## Phase 16: Temporary Plan Disposition

Goal: remove scratch authority after distillation.

Steps:

1. Confirm the closeout ledger quotes or summarizes all needed stage-log
   facts.
2. Confirm no active review packet links to this file as durable authority.
3. Remove this file in the closeout wave.
4. Mention removal in the closeout ledger.
5. Validate and land.

Exit condition: this file no longer exists, and the closeout ledger is the
durable resume surface.

## Validation Menu

Always choose the narrowest check that matches the surface changed.

For temporary plan-only edits:

```bash
git diff --check
python -m unittest tests.test_distillation_mechanics_topology
```

For relation source changes:

```bash
python scripts/build_catalog.py
python scripts/build_topology_scout.py
python -m unittest tests.test_distillation_mechanics_topology
python scripts/validate_repo.py
python scripts/release_check.py
```

For review-only wave packets:

```bash
python -m unittest tests.test_distillation_mechanics_topology
python scripts/validate_repo.py
```

For closeout:

```bash
python scripts/build_catalog.py
python scripts/build_topology_scout.py
python -m unittest tests.test_distillation_mechanics_topology
python scripts/validate_repo.py
python scripts/release_check.py
```

## Durable Output Checklist

By the end of the long pass, the repo should have:

- review coverage for every in-scope shelf;
- clear selector prompts for dense shelves;
- explicit losing-neighbor explanations;
- exact relation repairs where justified;
- explicit relation holds where not justified;
- no unauthorized new relation vocabulary;
- no generated hand edits;
- no hidden sibling-owner import;
- no empirical model-proof claim;
- one closeout ledger that lets the next agent continue technique reform.
