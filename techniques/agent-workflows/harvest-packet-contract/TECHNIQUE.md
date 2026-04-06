---
id: AOA-T-0077
name: harvest-packet-contract
domain: agent-workflows
status: promoted
origin:
  project: aoa-skills
  path: skills/aoa-session-donor-harvest/SKILL.md + skills/aoa-session-donor-harvest/references/harvest-packet-contract.md
  note: Extracted from the aoa-session-donor-harvest family where a bounded HARVEST_PACKET keeps reviewed session outputs explicit without collapsing later family seams into one catch-all packet.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - packet-contract
  - harvest
  - reviewed-session
  - post-session
summary: Keep one bounded HARVEST_PACKET contract over a reviewed session so downstream routing, diagnosis, repair, progression, and quest seams can consume explicit packet fields without silently replacing one another.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-04-05
export_ready: true
relations:
  - type: complements
    target: AOA-T-0075
  - type: complements
    target: AOA-T-0076
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# harvest-packet-contract

## Intent

Keep one bounded `HARVEST_PACKET` contract over a reviewed session artifact so
later family seams can consume one explicit packet shape instead of reopening
chat memory or stuffing all post-session meaning into one oversized recap.

## When to use

- a reviewed session already produced reusable extracts and needs one explicit packet shape
- later family seams such as owner placement, forks, diagnosis, repair, progression, or quest follow-up should read from one bounded packet
- the workflow needs required fields and optional extensions without pretending the packet is a sovereign routing layer
- reviewers need to confirm what the nucleus packet owns and what it merely points toward

## When not to use

- the session is still live or not yet reviewed
- the real task is donor extraction, owner placement, diagnosis, repair, progression, or quest promotion itself
- the packet would only repeat a generic session recap with no bounded extracts
- the contract would widen into memory canon, routing authority, or a dashboard schema

## Inputs

- one reviewed session reference
- one or more reviewed source artifacts
- one bounded extract record for each kept reusable unit
- optional follow-on family signals such as fork cards, diagnosis, repair candidates, progression, or quest hooks

## Outputs

- one `HARVEST_PACKET` with required packet fields
- one normalized extract shape for each kept reusable unit
- optional bounded extension fields for later family seams
- one explicit rule that optional family fields remain pointers rather than replacements for sibling seams

## Core procedure

1. Start from a reviewed session reference and reviewed source artifacts.
2. Keep the required packet spine small: `session_ref`, `reviewed_artifacts`, and `extracts`.
3. Record one bounded extract per reusable unit rather than one merged narrative block.
4. Require extract fields that keep meaning reviewable: title, kind, summary, evidence refs, repeat signal, owner hint, next surface, and nearest wrong target.
5. Allow optional packet fields such as frictions, deferrals, fork cards, diagnosis, repair candidates, progression, quest hooks, or chronicle hints only when they remain clearly subordinate.
6. Reject packet shapes that silently replace donor extraction, routing, diagnosis, repair, progression, or final quest verdicts.
7. Keep the packet readable as a nucleus artifact that hands off to later seams instead of becoming one permanent truth surface.

## Contracts

- the packet starts after review
- the required spine stays small and explicit
- each extract remains one bounded reusable unit
- optional fields can point to later family seams but must not replace them
- the packet is a source-owned post-session nucleus, not memory canon or routing authority
- later family seams may consume the packet, but they still own their own verdicts

Relationship to adjacent techniques: unlike [AOA-T-0075](../session-donor-harvest/TECHNIQUE.md), this technique does not decide which reusable units survive donor extraction; it only keeps the resulting packet shape bounded. Unlike [AOA-T-0076](../owner-layer-triage/TECHNIQUE.md), it does not decide one owner verdict over one bounded unit. It should stay smaller than any later fork, diagnosis, repair, progression, or quest seam that the packet may reference.

## Risks

### Failure modes

- the packet becomes a recap blob instead of a bounded extract container
- optional fields start carrying hidden routing or promotion verdicts
- extract records lose the fields needed for later review and handoff

### Negative effects

- overgrown packets can blur boundaries between the family seams
- teams may mistake packet completeness for proof that every later seam is already closed
- packet schema churn can create fake sophistication without clearer review

### Misuse patterns

- treating the packet as a memory object or universal session database
- stuffing unresolved diagnosis, repair, or progression doctrine into free-form notes
- emitting one packet before donor extraction is honestly done
- replacing sibling seams with packet subfields instead of keeping them explicit

### Detection signals

- extract records do not name bounded reusable units
- optional family fields read like hidden verdicts rather than pointers
- reviewers cannot tell which packet fields are required and which are optional
- the packet grows into a large schema before the family seams are stable

### Mitigations

- keep the required spine fixed and small
- require one bounded extract record per kept reusable unit
- preserve optional fields as adjuncts rather than replacements
- keep later family seams explicit even when the packet links to them

## Validation

Verify the technique by confirming that:
- the packet starts from reviewed material
- the required fields are explicit and present
- each extract record remains bounded and reviewable
- optional family fields remain clearly subordinate
- the packet does not silently replace routing, diagnosis, repair, progression, or quest verdicts

See `checks/harvest-packet-contract-checklist.md`.

## Adaptation notes

What can vary across projects:
- the exact packet filename or storage path
- how reviewed artifacts are referenced
- the names of optional family fields
- whether extract records keep owner hints as repo names, owner shapes, or another bounded target vocabulary

What should stay invariant:
- the packet starts only after review
- the required spine remains small
- extract records stay bounded and evidence-backed
- optional family fields remain subordinate to later explicit seams

Project-shaped details that should not be treated as invariant:
- one repo naming convention
- one packet serialization format
- one specific session index or memory store
- one project's downstream owner map

AoA adaptation example:
- the donor nucleus usually emits a `HARVEST_PACKET`
- owner-layer hints may later feed `AOA-T-0076`
- forks, diagnosis, repair, progression, and quest seams remain separate follow-on steps

## Public sanitization notes

This public bundle keeps only the reusable packet contract: one reviewed session reference, one reviewed-artifact list, one bounded extract array, and clearly subordinate optional family fields. AoA repo names, local storage paths, and skill invocation wrappers were reduced to adaptation examples or kept out of the invariant core.

## Example

See `examples/minimal-harvest-packet-contract.md`.

## Checks

See `checks/harvest-packet-contract-checklist.md`.

## Promotion history

- born in `aoa-skills` as the packet-contract seam inside `aoa-session-donor-harvest`
- extracted into `aoa-techniques` on 2026-04-05 as a bounded reviewed-session packet contract

## Future evolution

- keep donor extraction separate through `AOA-T-0075`
- keep later family seams explicit instead of growing packet authority
- add a second live context that uses the same bounded packet nucleus outside the current AoA session-harvest lineage
