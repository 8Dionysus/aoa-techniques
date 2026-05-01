# Technique Atom Contract

This guide defines what `aoa-techniques` means by one technique.

Use it when authoring, reviewing, distilling, selecting, or templating a
candidate and the real question is whether the object is one reusable technique
or a larger workflow object that belongs in another AoA layer.

Use [Technique Topology Contract](TECHNIQUE_TOPOLOGY_CONTRACT.md) next when the
question is where the atomic technique belongs in the larger classification
map.

## Core Contract

A technique is one atomic executable move.

It should be:

- compact enough to explain in one sentence
- narrow enough to classify with one `domain` and one primary `kind`
- concrete enough to execute from a template or capsule
- bounded enough to verify with one local check, smoke, example, or review cue
- portable enough to reuse outside the origin project after public-safe
  sanitization

A technique may have several steps, but those steps must serve one move. If the
candidate needs several independent outcomes, a persistent role, long-running
state, orchestration policy, or scenario composition, it is no longer one
technique.

## Standalone Portability Target

`aoa-techniques` is part of OS Abyss, but a technique must not require OS Abyss
to be useful.

A builder should be able to take one technique, capsule, or bundle into another
agent system and still understand:

- the move to perform
- the inputs to provide
- the output to return
- the stop line
- the validation signal
- the risks and owner-boundary cautions

AoA-specific law, provenance, generated surfaces, or sibling-repo consumers may
be linked, but they should behave as context and integration help rather than
as hidden runtime dependencies for the portable practice.

## Small-Agent Target

The target shape is not only human readability. A well-shaped technique should
be usable by a small agent after a larger orchestrator has selected the
technique and supplied the relevant local context.

As a design target, a 2-4B model should be able to execute the technique when it
receives:

- the compact technique card or relevant `TECHNIQUE.md` section
- the local task frame
- the required inputs
- the expected output shape
- the stop line and validation signal

This does not mean every small model can autonomously choose the right
technique. Selection, routing, context packing, and multi-technique composition
may belong to larger agents, skills, playbooks, or routing layers. The technique
itself must still stay small enough to execute once selected.

## Scale Target

The repository should be able to grow toward `1000+` techniques without turning
into a pile of broad mini-skills.

That requires:

- one atomic move per bundle
- `domain` as the first routing axis
- one primary `kind` as the second routing axis
- topology axes that keep family, capability, substrate, execution profile,
  risk posture, and relations distinct instead of overloading `domain`
- tags only for nuance
- concise summaries that work in generated catalogs
- capsules that preserve the smallest runtime card shape
- examples and checks that prove the move without smuggling in a whole workflow

If a future classification scheme cannot handle many hundreds of techniques,
the scheme is too weak. If one technique needs many pages of orchestration
before it can be used, the technique is too large.

## Not A Skill

A skill can orchestrate. A technique should not.

Route away from `aoa-techniques` when the candidate is mainly:

- a multi-step execution workflow with state, retries, or tool orchestration:
  use `aoa-skills`
- verdict doctrine, benchmark proof, or claim scoring: use `aoa-evals`
- dispatch policy, selector logic, or recommendation behavior: use
  `aoa-routing`
- scenario composition, campaign shape, or recurring play: use `aoa-playbooks`
- role identity, handoff posture, or agent contract: use `aoa-agents`
- memory, recall, KAG substrate, runtime, or infrastructure ownership: use the
  owning layer
- candidate movement, donor intake, promotion readiness, or cross-mechanic
  process: keep it in `mechanics/` until one atomic practice can be extracted

## Authoring Checks

Before drafting or accepting a technique, answer these checks:

- Can the technique name one move without using "and then" as the center?
- Can a reader identify the inputs and outputs without reading origin lore?
- Does the core procedure stay subordinate to that one move?
- Does the validation section name one smallest honest check?
- Does the risk section name how this move fails or gets misused?
- Can generated capsules compress it without losing the executable center?
- Would a small agent still know when to stop, return, or ask for help?

If the answer is no, narrow the candidate before promotion.

## Distillation Rule

Donor material should be reduced to one reusable move before it becomes a
technique bundle.

Preserve donor lineage, origin notes, and excluded doctrine, but do not import
the donor's whole system. If the donor contains several good moves, split them
into separate candidates and let `mechanics/distillation/` keep the accounting
until each one is ready.

## Template And Capsule Implication

The template should force the author to name the atomic move, the smallest
successful procedure, the inputs, the outputs, the contracts, the risks, and the
minimal validation signal.

Capsules should preserve that executable center for local runtime lookup. They
are not a replacement for the bundle, but they are a core pressure test: if the
capsule cannot carry the move, the bundle is probably too broad or too vague.

## Review Outcome

When a candidate fails this contract, do not patch around the failure with more
prose. Choose one of these outcomes:

- split the candidate into multiple techniques
- narrow it to the smallest reusable move
- keep it in a mechanic as a candidate
- route it to the owning repo as a skill, eval, routing object, playbook, role,
  memory object, KAG object, or runtime object

The repo can grow large only if each technique stays small.
