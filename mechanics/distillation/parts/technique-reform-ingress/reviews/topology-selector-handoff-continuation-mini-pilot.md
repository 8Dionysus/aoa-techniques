# Topology Selector Handoff-Continuation Mini-Pilot

Source packet: [Technique Reform Ingress](../README.md)

Prior shelf reviews:
[Handoff-Continuation Direct-Read Migration Review](handoff-continuation-direct-read-migration-review.md),
[Landed Handoff-Continuation Pilot Review](landed-handoff-continuation-pilot-review.md)

Generated lens:
[Technique Topology Scout](../reports/technique_topology_scout.md)

Contracts:
[Technique Atom Contract](../../../../../docs/TECHNIQUE_ATOM_CONTRACT.md),
[Technique Topology Contract](../../../../../docs/TECHNIQUE_TOPOLOGY_CONTRACT.md),
[Technique Selection Guide](../../../../../docs/selection/TECHNIQUE_SELECTION_GUIDE.md),
[Technique Capsule Guide](../../../../../docs/selection/TECHNIQUE_CAPSULE_GUIDE.md)

Status: targeted selector mini-pilot, not schema migration, not frontmatter
promotion, not empirical small-agent proof.

## Verdict

The `continuity/handoff-continuation` shelf is a good first selector pilot
because current `domain` and `kind` intentionally collapse all seven leaves into
one visible neighborhood: `agent-workflows` / `handoff`.

That is correct for current frontmatter truth, but it is not enough for the
future selector problem. A selector needs a second-stage choice once it reaches
this shelf:

- choose `AOA-T-0056` when the object is mailbox transport with replay and ack;
- choose `AOA-T-0057` when the object is the pre-compaction handoff packet;
- choose `AOA-T-0058` when the object is receipt before continuation;
- choose `AOA-T-0059` when the object is git-backed trust checking for handoff
  claims;
- choose `AOA-T-0060` when the object is a resumed-session opening ritual
  before mutation;
- choose `AOA-T-0061` when the object is a bounded cross-repo first-look map;
- choose `AOA-T-0062` when the object is long work segmented into checkpointed
  episodes.

The scout axes help, but only when used in order. `family` / shelf narrows the
neighborhood. `execution_profile` and `risk_posture` then separate packet-like
small-agent candidates from orchestration-bound continuation controls.
`capability_class` and `substrate` add useful color, but they do not yet replace
direct reading or relation guidance.

No bundle repair is needed in this mini-pilot. The useful next thread is
relation topology: the current direct `relations` are enough as adjacency
hints, but selector scenarios show a missing future need for sequence language
such as packet-before-receipt, packet-before-git-check, and
checkpoint-before-next-episode. That relation work should happen as its own
bounded slice, not as a silent frontmatter rewrite here.

## Sources Read

- [AOA-T-0056 channelized-agent-mailbox](../../../../../techniques/continuity/handoff-continuation/channelized-agent-mailbox/TECHNIQUE.md)
- [AOA-T-0057 structured-handoff-before-compaction](../../../../../techniques/continuity/handoff-continuation/structured-handoff-before-compaction/TECHNIQUE.md)
- [AOA-T-0058 receipt-confirmed-handoff-packet](../../../../../techniques/continuity/handoff-continuation/receipt-confirmed-handoff-packet/TECHNIQUE.md)
- [AOA-T-0059 git-verified-handoff-claims](../../../../../techniques/continuity/handoff-continuation/git-verified-handoff-claims/TECHNIQUE.md)
- [AOA-T-0060 session-opening-ritual-before-work](../../../../../techniques/continuity/handoff-continuation/session-opening-ritual-before-work/TECHNIQUE.md)
- [AOA-T-0061 cross-repo-resource-map-bootstrap](../../../../../techniques/continuity/handoff-continuation/cross-repo-resource-map-bootstrap/TECHNIQUE.md)
- [AOA-T-0062 episode-bounded-agent-loop](../../../../../techniques/continuity/handoff-continuation/episode-bounded-agent-loop/TECHNIQUE.md)
- supporting `checks/`, `examples/`, and `notes/` files for the seven bundles
- generated topology scout rows for `AOA-T-0056` through `AOA-T-0062`
- generated capsule entries for `AOA-T-0056` through `AOA-T-0062`
- prior bundle anatomy and execution-profile review packets

## Selector Scenario Read

| selector prompt | first correct pick | why adjacent leaves lose |
|---|---|---|
| "Agents need a durable channel where missed messages can be replayed and explicitly acknowledged." | `AOA-T-0056` | receipt and handoff packets are not transport; session opening is not a mailbox |
| "Before compaction, write the state the next session must read." | `AOA-T-0057` | mailbox delivery, receipt, git checking, and startup rituals all happen around or after the packet |
| "A handoff packet was sent; the receiver must explicitly accept it before work continues." | `AOA-T-0058` | packet authoring and mailbox ack are separate; git verification does not prove receiver acceptance |
| "The handoff claims files were changed; verify that against visible repo state." | `AOA-T-0059` | receipt only proves acceptance; session opening only checks a baseline; full code review is too broad |
| "A resumed session should not edit until it rereads current context and checks baseline state." | `AOA-T-0060` | packet creation and git claim verification are narrower siblings; the full change loop belongs elsewhere |
| "A task spans several repositories; the next agent needs a small first-look map." | `AOA-T-0061` | bounded context mapping is broader; session opening is single-start ritual, not a cross-repo map object |
| "A long agent run needs explicit checkpoints and continue/stop/escalate decisions." | `AOA-T-0062` | packet shape, startup ritual, and mailbox transport are components around episodes, not the episode loop |

## Axis Usefulness

| axis | selector value in this shelf | limit found |
|---|---|---|
| `domain` | keeps all seven under the current `agent-workflows` owner lane | too broad to choose among nearby handoff leaves |
| `kind` | keeps all seven as `handoff` atomic move shape | correct but intentionally too coarse for shelf-local selection |
| `family` / shelf | identifies the right neighborhood: `handoff-continuation` | not frontmatter truth and not enough by itself |
| `capability_class` | distinguishes packet/write, observe/read, mutate/validate pressure after shelf selection | most rows still share `handoff`, so secondary capability must not become a fake primary selector |
| `substrate` | highlights conversation, tool surfaces, history, human approval, runtime, and instruction pressure | `AOA-T-0059` may deserve later substrate review for git/code/shell cues, but not inside this pass |
| `execution_profile` | usefully separates `small-agent` packet checks from `orchestration-required` continuation controls | still scout suitability only, not local model proof |
| `risk_posture` | usefully marks `AOA-T-0060` and `AOA-T-0062` as mutating-context controls even though the technique text starts with reading/checkpointing | needs explanation so "mutating" is not misread as direct side effect inside the technique |
| `relations` | current complements prevent some isolation errors | future selector needs typed sequence or prerequisite language before this becomes a strong composition surface |

## Per-Leaf Selector Packet

| technique | pick cue | execution read | selector caution |
|---|---|---|---|
| `AOA-T-0056` | named channel, ordered replay, explicit ack | `small-agent`, read-only packet possible | ack is not handoff acceptance or memory truth |
| `AOA-T-0057` | pre-compaction continuation packet | `small-agent`, write-shaped packet possible | packet creation is not receipt, git truth, or transcript packaging |
| `AOA-T-0058` | receipt state before continuation | `small-agent`, read-only acceptance seam | delivery or mailbox ack is not receipt-confirmed handoff |
| `AOA-T-0059` | concrete handoff claims checked against git evidence | `small-agent`, read-only trust check with controlled local fixture | not generic code review and not provenance doctrine |
| `AOA-T-0060` | resumed-session read-and-baseline ritual before first mutation | `orchestration-required`, mutating-context guard | not full change loop, task selection, or mandatory test gate |
| `AOA-T-0061` | task-bounded cross-repo resource map | `small-agent`, read-only map possible | not a bounded-context model or workspace encyclopedia |
| `AOA-T-0062` | checkpointed episodes with continue/stop/escalate decisions | `orchestration-required`, mutating-context control | not runtime supervision, budget policy, or autonomous platform |

## What This Proves

- A shelf-local selector pass can add value without another broad audit.
- The future selector should not stop at `domain` and `kind`; those axes remain
  correct but shallow for dense neighborhoods.
- Scout axes are most useful as a second-stage review layer after tree
  placement, not as immediate frontmatter truth.
- Capsule quality is good enough for first-pass human or orchestrator selection
  in this shelf.
- Small-agent readiness should remain a fixture-contract question inside
  `aoa-techniques` until `aoa-evals` owns model execution proof.

## What This Does Not Prove

- no local 2-4B model executed these techniques;
- no eval bundle, runner, fixture, or pass/fail model verdict exists here;
- no `execution_profile`, `risk_posture`, `substrate`, `capability_class`, or
  `family` frontmatter should be added from this packet;
- no technique should be promoted to canonical status from this packet;
- no generated scout rule should be changed from this single shelf;
- no direct relation should be rewritten without a separate relation topology
  slice.

## Repair Queue

No bundle-local repair is required.

Carry these as future review candidates, not current defects:

| candidate | why it matters | route |
|---|---|---|
| `AOA-T-0059` substrate review | the technique depends on visible git state, and generated scout substrate currently reads more like conversation/tool/history than code/shell evidence | future topology scout calibration slice |
| relation sequence guidance | selector scenarios repeatedly need packet-before-receipt, packet-before-git-check, and checkpoint-before-next-episode language | future relations/composition slice |
| risk wording for mutating-context controls | `AOA-T-0060` and `AOA-T-0062` are mutating-context controls, not direct mutation instructions | future selector guidance or scout calibration note |

## Repeatable Mini-Pilot Rhythm

Use this rhythm for the next selector shelf before attempting a long pass:

1. choose one dense shelf where current `domain` and `kind` do not choose a
   single leaf;
2. read every leaf `TECHNIQUE.md`, capsule, checklist, example, and relevant
   notes;
3. write six to ten real selector prompts;
4. pick one first-correct technique for each prompt;
5. record why the nearest adjacent leaves lose;
6. judge which scout axes actually helped selection;
7. record repair candidates without mutating frontmatter or generated rules;
8. update only review surfaces and run the narrow mechanics validation.

## Stop Lines

- Do not run model proof from this packet.
- Do not change technique frontmatter from selector pressure alone.
- Do not add new required axes or schema fields.
- Do not hand-edit generated topology, capsule, or catalog outputs.
- Do not rewrite bundle relations in this mini-pilot.
- Do not import routing policy, eval authority, skill workflow, memory truth, or
  playbook composition into technique meaning.

## Next Honest Move

Run a relations/composition mini-slice over `continuity/handoff-continuation`.

The goal should be to decide whether the future relation topology needs typed
sequence language for this shelf, using the selector prompts above as evidence.
That next slice should still avoid frontmatter migration unless it first
defines the relation contract, owner boundary, validator impact, and generated
surface impact.
