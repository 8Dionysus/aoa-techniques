# Portability Bridge Handoff-Continuation Mini-Pilot

Source packet: [Technique Reform Ingress](../README.md)

Prior shelf reviews:
[Handoff-Continuation Direct-Read Migration Review](handoff-continuation-direct-read-migration-review.md),
[Landed Handoff-Continuation Pilot Review](landed-handoff-continuation-pilot-review.md),
[Topology Selector Handoff-Continuation Mini-Pilot](topology-selector-handoff-continuation-mini-pilot.md),
[Relations Composition Handoff-Continuation Pilot](relations-composition-handoff-continuation-pilot.md),
[Handoff-Continuation Direct Relation Repair](handoff-continuation-direct-relation-repair.md)

Status: targeted portability bridge mini-pilot, not source rewrite, not schema
migration, not OS Abyss adapter, not empirical small-agent proof.

## Verdict

The `continuity/handoff-continuation` shelf is a good first portability bridge
pilot because it carries real AoA-shaped pressure without needing AoA as a
runtime dependency. All seven leaves can be taken by an outside user when the
orchestrator supplies ordinary local equivalents: a channel, a handoff artifact,
a visible receipt surface, git evidence, a start-context surface, a repo list,
or an episode checkpoint.

No technique bundle needs repair in this mini-pilot. The current text already
keeps the portable atom separate from donor-system details. Project-shaped
references remain acceptable when they are provenance, relation IDs, examples,
or cautions. They would become defects only if a technique required OS Abyss,
Agents-of-Abyss doctrine, hidden memory, routing, KAG, evals, skills, runtime
services, or a specific agent platform to execute the atomic move.

This establishes the rhythm for the future portability long pass: direct-read a
shelf, name the generic adapter surfaces an external adopter must supply, check
for hidden system dependencies, and patch technique source only when standalone
execution is actually blocked.

## Sources Read

- [AOA-T-0056 channelized-agent-mailbox](../../../../../techniques/continuity/handoff-continuation/channelized-agent-mailbox/TECHNIQUE.md)
- [AOA-T-0057 structured-handoff-before-compaction](../../../../../techniques/continuity/handoff-continuation/structured-handoff-before-compaction/TECHNIQUE.md)
- [AOA-T-0058 receipt-confirmed-handoff-packet](../../../../../techniques/continuity/handoff-continuation/receipt-confirmed-handoff-packet/TECHNIQUE.md)
- [AOA-T-0059 git-verified-handoff-claims](../../../../../techniques/continuity/handoff-continuation/git-verified-handoff-claims/TECHNIQUE.md)
- [AOA-T-0060 session-opening-ritual-before-work](../../../../../techniques/continuity/handoff-continuation/session-opening-ritual-before-work/TECHNIQUE.md)
- [AOA-T-0061 cross-repo-resource-map-bootstrap](../../../../../techniques/continuity/handoff-continuation/cross-repo-resource-map-bootstrap/TECHNIQUE.md)
- [AOA-T-0062 episode-bounded-agent-loop](../../../../../techniques/continuity/handoff-continuation/episode-bounded-agent-loop/TECHNIQUE.md)
- repo and nested `AGENTS.md` route cards for `aoa-techniques`, mechanics,
  Distillation technique-reform ingress, and continuity techniques
- supporting `checks/`, `examples/`, and `notes/` files for the seven bundles
- [Bundle Anatomy Corpus Synthesis](bundle-anatomy-corpus-synthesis.md)
- [Execution Profile Truth Boundary Pilot](execution-profile-truth-boundary-pilot.md)
- [Selector Relation Long-Pass Closeout Ledger](selector-relation-long-pass-closeout-ledger.md)

## Portability Read

| technique | external adopter can take | adapter context needed | hidden dependency verdict |
|---|---|---|---|
| `AOA-T-0056` `channelized-agent-mailbox` | a durable named message channel with replay and explicit ack | storage for ordered messages, replay cursor, and ack state | portable-ready; no donor `.acomm`, MCP, SDK, or messaging platform required |
| `AOA-T-0057` `structured-handoff-before-compaction` | one pre-boundary handoff packet before context loss | artifact location plus completed, blocked, next, and reference fields | portable-ready; no OS Abyss memory, compactor, or agent runtime required |
| `AOA-T-0058` `receipt-confirmed-handoff-packet` | explicit receiver acceptance before continuation | existing packet, receiver identity, and visible receipt surface | portable-ready; receipt is not tied to a chat system or task tracker |
| `AOA-T-0059` `git-verified-handoff-claims` | git-backed trust check over handoff claims | local repo state, diff, commit, or file anchors to verify | portable-ready for git-backed work; do not use when no version-control evidence exists |
| `AOA-T-0060` `session-opening-ritual-before-work` | resumed-session baseline read before first mutation | current task context plus a visible state check such as branch, files, or worktree | portable-ready; no Nightcrawler, AoA state file, or launch ritual required |
| `AOA-T-0061` `cross-repo-resource-map-bootstrap` | task-bounded first-look map across several repos | repo names, owner hints, relevant paths, and first-read notes | portable-ready; not a Code Relay resource map or workspace encyclopedia |
| `AOA-T-0062` `episode-bounded-agent-loop` | long work segmented into checkpoints and continue/stop/escalate decisions | episode goal, checkpoint artifact, stop rule, and escalation target | portable-ready; not runtime supervision, budget law, or autonomous platform control |

## Boundary Read

Acceptable local references:

- `AOA-T-*` relation IDs and bundle identifiers;
- `8Dionysus` or AoA provenance where it explains where the technique came
  from;
- project-shaped examples that are clearly examples, not required substrate;
- cautions that prevent hidden runtime, memory, routing, eval, or skill
  authority from being smuggled into technique meaning.

Not acceptable as mandatory execution context:

- OS Abyss deployment, workspace bootstrap, or AoA constitutional authority;
- hidden memory, KAG truth, routing policy, playbook choreography, or eval
  verdicts;
- Nightcrawler, Code Relay, AgenticComm, AGOR, aX, launchd, or any other donor
  runtime service;
- a sibling repo becoming owner of the technique atom before the technique is
  explicitly routed there.

This shelf currently stays on the acceptable side. Its AoA-shaped language is
mostly lineage, relation, or example context. The portable atom remains the
local move an external system can adapt.

## Repair Gate

No bundle-local repair is accepted by this mini-pilot.

Held, not defects:

| hold | why it stays held |
|---|---|
| standard adapter card | useful if the long pass finds repeated external-adopter confusion, but not justified from one shelf |
| bundle source wording | current seven leaves already separate invariant move from project-shaped detail |
| empirical small-agent proof | belongs to a later eval-owned harness, not a portability review packet |
| generated scout updates | no source input changed and no generated portability field exists |

## Repeatable Portability Rhythm

Use this rhythm for the future portability long pass:

1. choose one shelf with real `portability-watch` pressure;
2. read its route cards, all leaf `TECHNIQUE.md` files, and supporting
   `checks/`, `examples/`, and `notes/`;
3. read prior migration, bundle-anatomy, selector, relation, and closeout
   packets for that shelf;
4. for each leaf, name the external-adopter object, the adapter context needed,
   and the hidden dependency test;
5. separate acceptable provenance and examples from mandatory donor-system
   dependencies;
6. patch source only when the atom cannot be executed outside OS Abyss;
7. record held owner routes without importing skill, eval, routing, memory,
   runtime, or playbook authority;
8. update the reform ingress index and run the narrow mechanics validation;
9. commit, push, PR, wait for repo validation, merge, and return to clean
   `main`.

## Stop Lines

- Do not remove AoA provenance merely to look generic.
- Do not add a loud bridge block to every technique.
- Do not promote a portability axis into frontmatter from this packet.
- Do not claim empirical 2-4B execution proof.
- Do not route technique meaning to `aoa-skills`, `aoa-evals`, `aoa-routing`,
  `aoa-memo`, `aoa-kag`, `aoa-playbooks`, or runtime owners from review
  pressure alone.
- Do not convert examples into mandatory platform requirements.

## Next Honest Move

Create the portability long-pass rhythm plan from this packet, then start with
the highest-pressure shelves rather than all `portability-watch` rows at once.
Good first wave candidates are `history/history-artifacts`,
`ingest/media-ingest`, `continuity/donor-harvest`, and
`recovery/antifragility-recovery`, because each has portable technique value
plus visible risk of being mistaken for memory, media-platform, donor-harvest,
or runtime doctrine.

## Validation

Passed locally:

1. the diff hygiene check
2. public-share grep over the changed review surfaces
3. the targeted tests
4. repository validation
5. the release lane
