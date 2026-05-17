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

It may have several steps, but every step must serve the same move. A good
candidate is compact enough to name in one sentence, narrow enough for one
`domain` and one primary `kind`, concrete enough to execute from a template or
capsule, and bounded enough to verify with one local check, smoke, example, or
review cue.

If the object needs several independent outcomes, persistent role behavior,
long-running state, orchestration policy, or scenario composition, it is not one
technique.

## Standalone Portability Target

`aoa-techniques` is part of OS Abyss, but a technique must not require OS Abyss
to be useful.

An external builder should be able to take one technique, capsule, or bundle
and still understand the move, inputs, output, stop line, validation signal,
risks, and owner-boundary cautions. AoA law, provenance, generated readers, and
sibling repos may add context; they must not become hidden runtime dependencies.

## Small-Agent Target

The target is not only human readability. After a larger orchestrator has
selected the technique and supplied local context, a 2-4B model should be able
to execute the move from a compact card or the relevant `TECHNIQUE.md` section.

That small agent needs the task frame, inputs, expected output shape, stop line,
and validation signal. It does not need autonomous selection, routing, context
packing, or multi-technique composition. The technique itself must stay small enough to execute once selected.

## Scale Target

The repository should be able to grow toward `1000+` techniques without turning
into broad mini-skills.

The scale discipline is simple: one move per bundle; `domain` first; one primary
`kind` second; family, capability, substrate, execution profile, risk posture,
and relations kept distinct; tags used only for nuance; summaries and capsules
kept compact; examples and checks proving the move without smuggling in a whole
workflow.

If the classification scheme cannot survive hundreds of techniques, it is too
weak. If one technique needs many pages of orchestration before use, the
technique is too large.

## Not A Skill

A skill can orchestrate. A technique should not.

Route away from `aoa-techniques` when the candidate is mainly:

| Object | Owner |
|---|---|
| multi-step workflow with state, retries, or tools | `aoa-skills` |
| verdict doctrine, benchmark proof, or claim scoring | `aoa-evals` |
| selector logic, dispatch policy, or recommendation behavior | `aoa-routing` |
| scenario composition or recurring play | `aoa-playbooks` |
| role identity, handoff posture, or agent contract | `aoa-agents` |
| memory, KAG, runtime, or infrastructure behavior | the owning layer |
| donor intake, promotion readiness, or candidate movement | `mechanics/` until one atomic practice is extracted |

## Authoring Checks

Before drafting or accepting a technique, check that it can name one move,
expose inputs and outputs without origin lore, keep the procedure subordinate
to that move, name one smallest honest validation signal, describe failure or
misuse, survive capsule compression, and tell a small agent when to stop,
return, or ask for help.

If any answer is no, narrow the candidate before promotion.

### Via negativa checks

Keep a candidate intact only when it is reusable across repositories, has clear
trigger boundaries, risks, and verification guidance, and represents one
materially distinct pattern family.

Merge, move, suppress, quarantine, deprecate, or remove it when it is a near
duplicate, a repo-local runbook fragment, or a repeated philosophy preamble.
Before adding a bundle, ask whether the distinction will still matter after
months of use and whether one canonical technique plus local examples would be
cleaner.

The corpus is healthy when technique count rises slower than meaning density.

## Distillation Rule

Donor material should be reduced to one reusable move before it becomes a
technique bundle.

Preserve lineage, origin notes, and excluded doctrine, but do not import the
donor's whole system. If the donor contains several good moves, split them into
separate candidates and let `mechanics/distillation/` keep the accounting until
each one is ready.

## Template And Capsule Implication

The template should force the author to name the atomic move, smallest
successful procedure, inputs, outputs, contracts, risks, and minimal validation
signal.

Capsules should preserve that executable center for local runtime lookup. They
are not a replacement for the bundle; they are a pressure test. If the capsule
cannot carry the move, the bundle is probably too broad or vague.

## Review Outcome

When a candidate fails this contract, do not patch around the failure with more
prose. Choose one outcome: split it, narrow it, keep it in a mechanic as a
candidate, or route it to the owning repo as a skill, eval, routing object,
playbook, role, memory object, KAG object, or runtime object.

The repo can grow large only if each technique stays small.
