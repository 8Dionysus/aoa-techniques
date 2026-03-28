# External Technique Candidates - Chat Wave 3

This doc records the active handoff and bounded continuation wave staged from the external chat wave pack.

Use it when the question is not "which landed technique should I open?", but "which Wave 3 candidate already landed cleanly, and which related candidate stayed explicitly out of the handoff lane?"

This is a staging and decision surface.
It does not create a canonical bundle or authorize import by itself.

## Scope

- this wave tracks `7` source-pack candidates
- `6` are already landed
- `0` are active draft-now seed lanes
- `1` is an explicit exclusion
- generic phase-sync remains in the live queue docs and is not absorbed here

## Landed From This Wave

| candidate | landed bundle | boundary kept | what stayed out |
|---|---|---|---|
| `structured-handoff-before-compaction` | [AOA-T-0057](../../../techniques/agent-workflows/structured-handoff-before-compaction/TECHNIQUE.md) | write one structured continuation packet before compaction or rollover | transcript packaging, mailbox delivery semantics, broad phase governance, full orchestration doctrine |
| `receipt-confirmed-handoff-packet` | [AOA-T-0058](../../../techniques/agent-workflows/receipt-confirmed-handoff-packet/TECHNIQUE.md) | require visible receipt of a handoff packet before continuation | mailbox transport, packet authoring, task-routing platforms, broad approval workflow doctrine |
| `git-verified-handoff-claims` | [AOA-T-0059](../../../techniques/agent-workflows/git-verified-handoff-claims/TECHNIQUE.md) | verify concrete handoff claims against visible git state before continuation | generic code review, full provenance frameworks, witness-trace publication doctrine |
| `session-opening-ritual-before-work` | [AOA-T-0060](../../../techniques/agent-workflows/session-opening-ritual-before-work/TECHNIQUE.md) | require one visible read-and-verify ritual before the first mutation in a resumed session | task picking, startup test doctrine, handoff authoring, and full boot or orchestration stacks |
| `cross-repo-resource-map-bootstrap` | [AOA-T-0061](../../../techniques/agent-workflows/cross-repo-resource-map-bootstrap/TECHNIQUE.md) | bootstrap multi-repo continuation from one explicit repo-and-resource map | semantic context mapping, architecture inventories, and full workspace-platform doctrine |
| `episode-bounded-agent-loop` | [AOA-T-0062](../../../techniques/agent-workflows/episode-bounded-agent-loop/TECHNIQUE.md) | divide longer work into checkpointed episodes with explicit continue, stop, or escalate decisions | startup ritual doctrine, handoff packet structure, and full autonomous-platform semantics |

## Active Seed Lane

No active draft-now seed candidates remain in Wave 3.

## Explicit Exclusion

| candidate | why excluded now | next honest move |
|---|---|---|
| `governed-action-surfaces` | belongs to a later governed-action family, not the handoff lane | reopen only in a separate future governed-action wave |

## Notes

- this wave owns handoff contracts, not generic phase-sync
- `structured-handoff-before-compaction`, `receipt-confirmed-handoff-packet`, `git-verified-handoff-claims`, `session-opening-ritual-before-work`, `cross-repo-resource-map-bootstrap`, and `episode-bounded-agent-loop` now exit the seed lane as landed `AOA-T-0057`, `AOA-T-0058`, `AOA-T-0059`, `AOA-T-0060`, `AOA-T-0061`, and `AOA-T-0062`
- keep mailbox transport and handoff receipt distinct so Wave 2 and Wave 3 stay separable
- keep every seed smaller than an orchestration or governance stack
