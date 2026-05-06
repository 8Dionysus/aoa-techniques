# Relations Composition Handoff-Continuation Pilot

Source packet: [Technique Reform Ingress](../README.md)

Prior shelf reviews:
[Handoff-Continuation Direct-Read Migration Review](handoff-continuation-direct-read-migration-review.md),
[Landed Handoff-Continuation Pilot Review](landed-handoff-continuation-pilot-review.md),
[Topology Selector Handoff-Continuation Pilot](topology-selector-handoff-continuation-mini-pilot.md)

Relation contracts:
[Bounded Relation Lift Guide](../../../../../docs/BOUNDED_RELATION_LIFT_GUIDE.md),
[Technique Topology Contract](../../../../../docs/TECHNIQUE_TOPOLOGY_CONTRACT.md),
[Selection Patterns](../../../../../docs/SELECTION_PATTERNS.md),
[`relation.schema.json`](../../../../../schemas/relation.schema.json)

Status: targeted relations/composition pilot, not relation schema migration,
not bundle frontmatter mutation, not generated graph behavior.

## Verdict

The selector pressure found in `continuity/handoff-continuation` is real:
several leaves naturally compose in sequence around packet authoring, receipt,
git verification, session opening, cross-repo startup, and checkpointed
episodes.

The current repo relation layer should not grow new types from this pilot. The
allowed vocabulary is already enough for the first useful distinction:

- use `requires` only when one technique usually needs another contract to
  exist first;
- use `used_together_for` only when two techniques commonly travel in one
  operating path without strict dependency;
- use `complements` when adjacency is helpful but dependency would overstate
  the relation;
- leave relation-empty bundles empty when an edge would confuse transport,
  receipt, authorization, or proof.

This pass does not rewrite frontmatter. It carries two exact repair candidates
for a later direct relation repair:

- `AOA-T-0058` may be stronger as `requires AOA-T-0057` because the receipt
  technique explicitly assumes an existing handoff packet.
- `AOA-T-0059` may be stronger as `requires AOA-T-0057` because the git check
  technique explicitly assumes a handoff packet with concrete claims.

The rest of the shelf should stay conservative for now. `AOA-T-0060` and
`AOA-T-0062` can compose with handoff packets, but their contracts are wider
than "this exact packet must already exist." `AOA-T-0056` should remain empty
because mailbox acknowledgment is not handoff receipt or continuation
permission. `AOA-T-0061` should keep its current `complements AOA-T-0016`
edge because it distinguishes concrete cross-repo startup maps from bounded
context modeling without pretending to require the whole context-map method.

## Sources Read

- [AOA-T-0056 channelized-agent-mailbox](../../../../../techniques/continuity/handoff-continuation/channelized-agent-mailbox/TECHNIQUE.md)
- [AOA-T-0057 structured-handoff-before-compaction](../../../../../techniques/continuity/handoff-continuation/structured-handoff-before-compaction/TECHNIQUE.md)
- [AOA-T-0058 receipt-confirmed-handoff-packet](../../../../../techniques/continuity/handoff-continuation/receipt-confirmed-handoff-packet/TECHNIQUE.md)
- [AOA-T-0059 git-verified-handoff-claims](../../../../../techniques/continuity/handoff-continuation/git-verified-handoff-claims/TECHNIQUE.md)
- [AOA-T-0060 session-opening-ritual-before-work](../../../../../techniques/continuity/handoff-continuation/session-opening-ritual-before-work/TECHNIQUE.md)
- [AOA-T-0061 cross-repo-resource-map-bootstrap](../../../../../techniques/continuity/handoff-continuation/cross-repo-resource-map-bootstrap/TECHNIQUE.md)
- [AOA-T-0062 episode-bounded-agent-loop](../../../../../techniques/continuity/handoff-continuation/episode-bounded-agent-loop/TECHNIQUE.md)
- generated catalog and selection rows for `AOA-T-0056` through `AOA-T-0062`
- prior semantic review examples for `requires`, `complements`,
  `used_together_for`, and `shares_contract_with`
- current relation guide, KAG source-lift guide, selection patterns, and
  relation schema

## Current Relation Read

| technique | current relation | read |
|---|---|---|
| `AOA-T-0056` | none | correct hold: mailbox ack is transport handling, not handoff receipt or authorization |
| `AOA-T-0057` | `complements AOA-T-0054` | correct hold: compaction handoff and skill re-seeding strengthen one another without dependency |
| `AOA-T-0058` | `complements AOA-T-0057` | safe but likely weak: receipt assumes an existing handoff packet |
| `AOA-T-0059` | `complements AOA-T-0057` | safe but likely weak: git-claim verification assumes a handoff packet with concrete claims |
| `AOA-T-0060` | `complements AOA-T-0057` | correct hold: it consumes handoff, summary, or another session-start context, not only a structured packet |
| `AOA-T-0061` | `complements AOA-T-0016` | correct hold: concrete repo/resource map sits next to bounded context mapping without requiring it |
| `AOA-T-0062` | `complements AOA-T-0057` | correct hold for now: episode boundaries can use handoff packets, but the loop contract is broader |

Neighboring relation evidence:

- `AOA-T-0069` currently `complements AOA-T-0062`, which keeps durable jobs
  adjacent to checkpointed episodes without merging scheduler or approval
  doctrine into the episode loop.
- `AOA-T-0091` currently `complements AOA-T-0060`, `AOA-T-0028`, and
  `AOA-T-0061`, which correctly links workspace ingress to session opening,
  mutation gating, and cross-repo startup without making any one of them the
  whole workflow.

## Composition Pressure

| sequence pressure | current relation result | pilot verdict |
|---|---|---|
| packet creation before receipt | `0058 complements 0057` | candidate repair to `0058 requires 0057` |
| packet creation before git-claim check | `0059 complements 0057` | candidate repair to `0059 requires 0057` |
| packet before session opening | `0060 complements 0057` | keep: session opening can start from handoff, recent summary, or another session-start surface |
| packet before episode loop | `0062 complements 0057` | keep: episodes read checkpoint state and can use packets, but do not require this one packet technique |
| mailbox delivery before receipt | no relation | keep: delivery ack is explicitly not handoff acceptance |
| cross-repo map before session opening | no direct shelf relation | hold: `0091` already composes session opening and cross-repo startup from outside this shelf |
| bounded context map before cross-repo map | `0061 complements 0016` | keep: useful adjacent theory/object split, not strict prerequisite |

## Relation Type Fit

`requires` is the right future candidate when the downstream technique's own
inputs and contracts name an already-existing object that another technique
owns. Existing semantic reviews use this shape for:

- rollout depending on a stable smoke-summary producer;
- a new intent rollout depending on an existing intent-plan contract;
- KAG relation and provenance lifts depending on the metadata spine.

That pattern fits `AOA-T-0058` and `AOA-T-0059` only if this repo accepts
`AOA-T-0057` as the local handoff-packet contract those techniques usually
need.

`complements` remains correct when the relation helps choice but strict
dependency would overstate the contract. That fits `AOA-T-0060`, `AOA-T-0061`,
and `AOA-T-0062`.

`used_together_for` is not the first repair here. It could describe a common
operating path, but it would not answer the exact pressure the selector found:
"does the downstream move need the packet contract first?" For the two strong
candidates, `requires` is clearer.

## What This Proves

- The selector pilot's relation thread should become a direct relation repair
  question before any new relation vocabulary is invented.
- The current relation schema can express the most useful sequence pressure in
  this shelf through `requires`, without adding `follows` or graph behavior.
- A relation review must read bundle contracts, not only generated adjacency
  rows, because `complements` can be either intentionally conservative or too
  weak.
- Relation edits should be smaller than topology reform: one or two edges,
  generated rebuild, validation, and a review receipt.

## What This Does Not Prove

- no new relation type is justified yet;
- no generated graph, scoring, traversal, or selector engine exists here;
- no bundle frontmatter has been changed by this packet;
- no relation rationale field should be added from this packet;
- no `AOA-T-0060`, `AOA-T-0061`, `AOA-T-0062`, or `AOA-T-0056` relation
  repair is currently justified;
- no empirical small-agent proof or `aoa-evals` verdict is implied.

## Repair Candidates

| candidate | proposed edge | why | stop line |
|---|---|---|---|
| `AOA-T-0058` | `requires AOA-T-0057` | receipt technique requires an existing handoff packet and explicitly stays separate from packet authoring | do not imply receipt is approval, phase permission, mailbox ack, or queue governance |
| `AOA-T-0059` | `requires AOA-T-0057` | git verification technique requires a handoff packet with concrete claims and explicitly stays separate from packet authoring | do not imply git evidence is full proof, code review, or provenance doctrine |

Do not apply these candidates silently. A direct relation repair pass should:

1. reread `AOA-T-0057`, `AOA-T-0058`, and `AOA-T-0059`;
2. decide whether `AOA-T-0057` is the correct local packet contract target;
3. update exactly those relation edges if accepted;
4. rebuild generated catalog and selection surfaces;
5. run the narrow relation and repository validation path;
6. record that no new relation types, graph behavior, or relation rationale
   fields were added.

## Repeatable Relations Pilot Rhythm

Use this rhythm before relation work scales into a long pass:

1. choose one dense shelf already tested by selector prompts;
2. list current direct relations from bundle frontmatter and generated
   selection surfaces;
3. read the inputs, outputs, contracts, and adjacent-technique paragraphs for
   every leaf;
4. separate strict object dependency from ordinary adjacency;
5. prefer existing relation types before proposing new vocabulary;
6. carry exact repair candidates instead of broad relation philosophy;
7. mutate frontmatter only in a separate direct relation repair pass;
8. rebuild generated surfaces only after source relations actually change.

## Stop Lines

- Do not add `follows`, `prerequisite`, `alternative`, `strengthens`, or
  other future relation names to frontmatter in this pass.
- Do not treat relations as graph traversal, ranking, proof, or route policy.
- Do not change generated files by hand.
- Do not let mailbox acknowledgment, handoff receipt, continuation permission,
  and approval collapse into one relation.
- Do not import eval authority, skill workflow, playbook choreography, memory
  truth, runtime behavior, or AoA constitutional law into technique relations.

## Next Honest Move

Run one direct relation repair review for `AOA-T-0058` and `AOA-T-0059` only.

The direct repair should either:

- accept both `requires AOA-T-0057` edges and rebuild generated surfaces; or
- reject the strengthening and record why `complements` remains the least
  misleading relation type.

After that, the same rhythm can scale to a long selector/relation pass across
other dense shelves.
