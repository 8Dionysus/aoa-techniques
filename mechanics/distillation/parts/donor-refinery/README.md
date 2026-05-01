# Donor Refinery Rubric

This document defines the compact source-first intake rule for external donors in `aoa-techniques`.

Use it when the question is not "is this donor interesting at all?", but:

- what exactly can be extracted here?
- what should stay out?
- is this donor strengthening technique meaning, or trying to smuggle in foreign doctrine?

## Core route

AoA should refine external donors through this chain:

`donor -> repeated pattern -> sanitized technique or skill -> playbook -> eval`

`aoa-techniques` owns the extraction of reusable practice from that chain.
It does not own playbook meaning or eval doctrine.

## Law, Local Route, Bridge

Distillation must keep three layers separate:

- higher law: the source owner or AoA layer that defines authority, meaning,
  and stop-lines
- local route: this package's extraction, hold, overlap, incubation, or import
  path inside `aoa-techniques`
- bridge: a narrow handoff that names the donor input, extracted output shape,
  owner boundary, and stop line

A donor may help OS Abyss, but the extracted technique candidate must still be
portable as a bounded practice. AoA-only law, runtime assumptions, or sibling
repo integration details should stay as provenance or boundary context, not as
hidden requirements for the technique.

## Three intake tests

### Pattern

A donor shows `pattern` when it contributes a repeated operational form that can be named, bounded, sanitized, and reused outside the donor's original mythology.

### Contamination

A donor shows `contamination` when the extracted object widens carelessly because the donor mixes:

- implementation accident with reusable practice
- private environment assumption with portable contract
- orchestration sprawl with bounded technique
- donor-specific wording with actual reusable form

### Foreign doctrine

A donor carries `foreign doctrine` when its identity system, constitution, metaphysics, or total worldview arrives as if AoA should adopt it as canon rather than extract a bounded reusable pattern from it.

Foreign doctrine may still contain useful governance patterns.
But those patterns should be extracted explicitly instead of imported wholesale.

## Accepted bounded donor example

### `ruler` -> bounded origin donor for `AOA-T-0013`

Why accepted:

- it contributes a bounded one-source -> many-target rule-distribution pattern
- the extracted form stays narrower than the donor's total project identity
- the reusable object is the distribution contract, not the donor's worldview

What gets extracted:

- one canonical source
- multiple managed targets
- explicit drift control

What does not get extracted:

- donor-specific identity claims
- extra orchestration semantics beyond the bounded contract

## Self-agent-shaped donor example

### constitution-heavy self-agent donor -> governance pattern only

Why not imported wholesale:

- the donor may bundle agency myth, constitution, role doctrine, runtime assumptions, and identity language into one package
- AoA does not need that whole package as canon

What may still be extracted:

- approval-gate posture
- rollback discipline
- bounded iteration limits
- improvement-log discipline

Correct refinement outcome:

- extract checkpoint governance pattern
- route scenario-level method into `aoa-playbooks`
- keep role contracts in `aoa-agents`
- keep eval posture in `aoa-evals`

Wrong refinement outcome:

- import the donor's constitution as AoA law
- collapse governance pattern into agent mythology
- treat the donor's total doctrine as if it were a reusable technique

## Practical rule

The donor is useful when AoA can say:

- what pattern was extracted
- what was intentionally left behind
- why the resulting technique stays narrower than the donor

If AoA cannot say those three things clearly yet, the donor is still evidence or soil, not canon.

## Extraction Gate

Before a donor-derived candidate can leave this package for bundle drafting,
the active surface should be able to name:

- the atomic move being extracted
- the likely `domain` and primary `kind`
- the likely family, or why no family is stable yet
- the capability class, substrate, execution profile, and risk posture
- the nearest landed technique, alternative, or conflict point
- the source law, local extraction route, and bridge stop line
- what remains portable outside OS Abyss

If these cannot be named without importing the donor's whole system, keep the
material in the relevant ledger or incubation lane.
