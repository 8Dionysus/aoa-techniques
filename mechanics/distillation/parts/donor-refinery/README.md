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

Donor intake stays portable: owner references and AoA context explain boundary
and provenance. The extracted candidate still has to stand as one bounded
practice outside OS Abyss.

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

## Atom/Topology Gate

Before a donor-derived candidate can leave this package for bundle drafting,
the active surface must be able to name the candidate's gate packet.

The atom/topology side of the packet is:

- `atomic_move_note`: the one executable move being extracted
- `atomic_move_status`: whether the move is named, landed, inherited, or still
  not named cleanly
- likely `domain` and primary `kind`
- likely family, or why no stable family exists yet
- `capability_class`, `substrate`, `execution_profile`, and `risk_posture`
- nearest landed technique, alternative, or conflict point

These fields classify the candidate for extraction. They do not promote future
topology axes into current technique frontmatter authority.

## Boundary And Portability Gate

The boundary side of the same packet is:

- `higher_law`: the source owner or layer whose authority and stop lines matter
  for extraction
- `local_route`: the `aoa-techniques` path for extraction, hold, overlap,
  incubation, import, or rejection
- `bridge_stop_line`: what must not cross into technique canon
- `portable_core`: what remains useful outside OS Abyss
- `aoa_only_context`: what stays as local integration or provenance context
- donor exclusions: what is intentionally left behind

These registry field names are compact route metadata, not a section template
for every mechanic. If the boundary cannot be named without importing the
donor's whole system, keep the material in the relevant ledger or incubation
lane.

## Gate Verdicts

Use one narrow verdict per candidate:

- `pass_to_import_runbook`: the packet is clear enough to draft through the
  external import runbook
- `ledger_hold`: the pattern may matter, but evidence or naming is still too
  weak
- `overlap_hold`: the candidate is too close to an existing technique or active
  repo surface
- `layer_incubation`: a sibling layer must stabilize its own public-safe
  contract before extraction here
- `not_technique_shaped`: the material is still substrate, architecture,
  runtime, role, or doctrine rather than one technique atom

Do not fill missing packet fields by inference just to move a donor forward.
The refinery may classify and hold material, but it does not create technique
bundles or release bundle-local review gates.
