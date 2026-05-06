# Handoff-Continuation Direct Relation Repair

Source packet: [Technique Reform Ingress](../README.md)

Prior packets:
[Topology Selector Handoff-Continuation Pilot](topology-selector-handoff-continuation-mini-pilot.md),
[Relations Composition Handoff-Continuation Pilot](relations-composition-handoff-continuation-pilot.md)

Touched bundle relations:

- [AOA-T-0058 receipt-confirmed-handoff-packet](../../../../../techniques/continuity/handoff-continuation/receipt-confirmed-handoff-packet/TECHNIQUE.md)
- [AOA-T-0059 git-verified-handoff-claims](../../../../../techniques/continuity/handoff-continuation/git-verified-handoff-claims/TECHNIQUE.md)

Stable packet target:
[AOA-T-0057 structured-handoff-before-compaction](../../../../../techniques/continuity/handoff-continuation/structured-handoff-before-compaction/TECHNIQUE.md)

Status: accepted direct relation repair.

## Verdict

Accept both `requires AOA-T-0057` repairs.

`AOA-T-0057` owns the local structured handoff packet contract: an explicit
continuation artifact written before compaction or rollover, with done,
in-progress, blocked, next-step, and concrete reference fields.

`AOA-T-0058` does not merely sit near that packet contract. Its inputs and
contracts require one existing handoff packet or stable handoff reference
before receipt can be recorded. `requires AOA-T-0057` is therefore more useful
and less misleading than `complements AOA-T-0057`.

`AOA-T-0059` likewise depends on a packet-shaped object with concrete claims,
references, or file anchors before visible git evidence can be compared against
those claims. `requires AOA-T-0057` is the right direct relation because the
git check is downstream from packet existence, not just adjacent to it.

No other relation in `continuity/handoff-continuation` changes in this repair.
The selector/composition pilot already found the rest of the shelf to be
intentional holds.

## Decision Table

| bundle | old edge | new edge | reason |
|---|---|---|---|
| `AOA-T-0058` | `complements AOA-T-0057` | `requires AOA-T-0057` | receipt must identify an existing packet and receiver before continuation opens |
| `AOA-T-0059` | `complements AOA-T-0057` | `requires AOA-T-0057` | claim verification must start from a handoff packet that contains concrete claims |

## Holds

| bundle | held relation posture | why |
|---|---|---|
| `AOA-T-0056` | remain relation-empty | mailbox delivery and ack are not handoff receipt or continuation permission |
| `AOA-T-0060` | keep `complements AOA-T-0057` | session opening can consume handoff, summary, or another session-start surface; it does not require this exact packet contract |
| `AOA-T-0061` | keep `complements AOA-T-0016` | concrete cross-repo startup maps stay adjacent to bounded context mapping without requiring the whole context-map method |
| `AOA-T-0062` | keep `complements AOA-T-0057` | episode loops can use handoff packets, but the loop contract centers checkpointed episodes and continue/stop/escalate decisions |

## What Changed

- `AOA-T-0058` frontmatter relation changed from `complements AOA-T-0057` to
  `requires AOA-T-0057`.
- `AOA-T-0059` frontmatter relation changed from `complements AOA-T-0057` to
  `requires AOA-T-0057`.
- Generated relation consumers should be rebuilt from source after this repair:
  catalog, selection surfaces, KAG export, and any release-check companions
  that derive from the catalog or frontmatter.

## What Did Not Change

- no new relation types;
- no relation schema migration;
- no relation rationale field;
- no generated graph behavior, traversal, ranking, or selector engine;
- no status, `domain`, `kind`, maturity, validation-strength, evidence, owner,
  or path changes;
- no empirical small-agent proof or `aoa-evals` verdict.

## Safety Read

This repair strengthens only object dependency:

- receipt needs packet existence;
- git verification needs packet claims.

It does not say receipt is approval, mailbox acknowledgment, phase permission,
or queue governance. It does not say git evidence is full proof, code review,
or provenance doctrine.

## Stop Lines

- Do not use this repair as precedent for adding `follows`, `prerequisite`,
  `alternative`, or other future relation names to frontmatter.
- Do not strengthen `AOA-T-0060` or `AOA-T-0062` to `requires` from this
  packet; their contracts deliberately remain wider than the packet object.
- Do not hand-edit generated surfaces. Rebuild them from source.
- Do not treat this as a long-pass relation topology conclusion for every
  dense shelf.

## Next Honest Move

Move to the long selector/relation pass.

Start that pass from dense shelves where current `domain`, `kind`, and tree
placement find the neighborhood but not the exact leaf. Use the rhythm proven
here: selector prompts first, relation contract read second, direct repair only
when bundle inputs and contracts justify one existing relation type.
