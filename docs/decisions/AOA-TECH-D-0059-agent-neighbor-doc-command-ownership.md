# Agent Neighbor Doc Command Ownership

Status: accepted

Date: 2026-05-17

## Index Metadata

- Decision ID: AOA-TECH-D-0059
- Original date: 2026-05-17
- Surface classes: agent route
- Technique axes: agent mesh
- Mechanic parents: none
- Guard families: AGENTS/mesh
- Posture: accepted

## Context

After the AGENTS mesh reached canonical shape, several neighboring README and
guide surfaces still carried agent-only command lanes, editing read orders,
stop-lines, or validation blocks.

That made the repository look orderly by directory while still forcing agents
to reconcile the same instruction class in two places. The problem was most
visible in Spark lane docs, examples, root legacy, decision/review/selection
README files, source-lift guides, guardrail protocols, and mechanic package
cards.

## Options considered

- Keep short validation pointers in every neighboring README for local
  convenience.
- Move only repeated command blocks and leave package-card `### Validation`
  headings as compatibility with the older mechanic-card standard.
- Treat the nearest `AGENTS.md` as the owner of agent read order, validation,
  closeout, and editing stop-lines, while neighboring docs keep source role,
  route meaning, contract meaning, and historical evidence.

## Decision

Agent operation belongs in the nearest `AGENTS.md`.

Neighboring README and guide surfaces should keep:

- role and purpose
- source contract
- route map
- source/derived boundary
- historical or template content when that is the document's authored meaning

The nearest `AGENTS.md` should keep:

- read-before-editing order
- validation command lanes
- closeout expectations
- stop-lines that constrain agent editing rather than define the source object
- local report and skipped-check expectations

Mechanic package README cards no longer carry a `### Validation` heading. The
package card answers what the mechanic is, when to use it, what enters or
leaves, what it must not claim, and where to route next. The package
`AGENTS.md` owns exact commands.

## Rationale

This keeps entry docs light enough to read while preserving the full command
surface for agents. It also prevents stale command copies from surviving in
README files after the local AGENTS route changes.

Some docs may still contain validation as authored content: pull request
templates, release docs, historical receipts, generated-reader warnings,
technique templates, and decision records may name validation when that is part
of the object itself rather than agent-local command law.

## Consequences

- Mechanic package-card tests now enforce the no-`### Validation` package-card
  shape.
- Source-lift and guardrail guide contracts point back to local AGENTS for
  executable command lanes.
- Legacy and example README files stay descriptive, while local AGENTS files
  carry stop-lines, validation, and closeout.
- Future neighboring docs should not reintroduce command blocks unless the
  document itself is a release route, template, historical receipt, generated
  surface, or other source object whose meaning includes that validation
  content.

## Source surfaces

- [DESIGN.AGENTS](../../DESIGN.AGENTS.md)
- [Root AGENTS](../../AGENTS.md)
- [Mechanics AGENTS](../../mechanics/AGENTS.md)
- [Mechanics README](../../mechanics/README.md)
- [Source Lift AGENTS](../source-lift/AGENTS.md)
- [Guardrails AGENTS](../guardrails/AGENTS.md)
- [Root Legacy AGENTS](https://github.com/8Dionysus/aoa-techniques/tree/feffba63dc22fd921512ba5a3ff1b5d78606f93b/legacy/AGENTS.md)

## Follow-up route

Use [AGENTS_MESH_PROTOCOL](../guardrails/AGENTS_MESH_PROTOCOL.md) when the
shape of agent cards changes. Use this decision when a neighboring README or
guide starts accumulating read order, validation command blocks, or closeout
requirements that belong to the nearest `AGENTS.md`.

## Verification

Verify with:

Verification was routed through the targeted owner checks and repository validation lanes.
