---
id: AOA-T-0040
name: skill-vs-command-boundary
domain: docs
kind: guardrail
status: promoted
origin:
  project: agentic-dev-team
  path: docs/skills.md
  note: Extracted from a plugin structure that keeps reusable skills as capability artifacts while slash commands stay user-facing workflow entrypoints with their own invocation syntax.
owners:
  - 8Dionysus
tags:
  - docs
  - skills
  - commands
  - boundaries
  - capability
summary: Separate reusable skill meaning from user-facing command invocation so shared capability stays portable without collapsing into slash-command syntax or command-specific workflow policy.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-23
export_ready: true
relations:
  - type: complements
    target: AOA-T-0027
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# skill-vs-command-boundary

## Intent

Keep reusable capability meaning in a skill artifact and keep user-facing invocation behavior in a command artifact so shared knowledge does not collapse into command syntax, argument parsing, or command-local workflow steps.

## When to use

- the same capability should survive outside any one user-facing command
- a repository has both reusable skills and explicit command entrypoints
- commands need their own arguments, numbered steps, or structured output
- agents or several commands should be able to reuse the same skill without rewriting it
- the reusable object is the skill-command ownership split rather than distribution, routing, or marketplace policy

## When not to use

- one local command is the whole feature and no reusable capability survives outside it
- the real need is one canonical source propagated to many managed targets
- the real need is upstream mirroring with provenance rather than local capability ownership
- the real need is shell composability, slash-command product design, or routing policy
- the command and skill artifacts would only duplicate each other with no meaningful reuse boundary

## Inputs

- one reusable skill artifact that names patterns, guidelines, or procedure
- one user-facing command artifact that names invocation syntax, arguments, steps, or structured output
- one explicit rule for how the command references or invokes the skill
- one review path that can catch copied or redefined skill meaning inside commands
- one reason the skill should remain meaningful outside the current command wrapper

## Outputs

- clearer ownership of reusable capability meaning
- a command surface that stays bounded to invocation and workflow entry
- lower drift between shared capability and command wrappers
- easier reuse of the same skill across agents or multiple commands
- a cleaner test for whether a new artifact should be a skill, a command, or neither

## Core procedure

1. Identify the part of the capability that should remain reusable outside any one command entrypoint.
2. Write that reusable meaning as a skill artifact with patterns, guidelines, or procedure.
3. Write the user-facing entrypoint as a command artifact that owns invocation name, arguments, numbered steps, and output shape.
4. Let agents or commands reference the skill for how-to knowledge instead of copying its body.
5. Keep command-specific wrappers, guardrails, and output formatting inside the command artifact.
6. If the capability cannot survive without one command's argument shape or workflow, keep it command-local instead of inventing a fake skill.
7. Split propagation, marketplace, routing, and shell-composability concerns into separate sibling techniques when they become the real reusable object.

## Contracts

- the skill owns reusable capability meaning
- the command owns invocation syntax, arguments, workflow steps, and output format
- the same skill can be reused by more than one agent or command without rewriting its core meaning
- a command may invoke or reference a skill without becoming the canonical home of that skill
- command-specific constraints must not silently redefine the base skill boundary
- the technique stays about skill-command artifact ownership, not distribution, marketplace curation, routing policy, or shell-command design

Relationship to adjacent techniques: unlike `AOA-T-0013 single-source-rule-distribution`, this technique does not fan one canonical source out to several managed instruction targets. Unlike `AOA-T-0027 cross-agent-skill-propagation`, it does not govern propagation into multiple targets at all; it decides what should remain a reusable skill before any propagation story begins. Unlike `AOA-T-0024 upstream-mirroring-with-provenance`, it does not mirror upstream-owned content. Unlike `AOA-T-0031 shell-composable-agent-invocation`, it does not define shell I/O boundaries for one-shot command execution.

## Risks

### Failure modes

- command files become the only place where reusable capability meaning actually lives
- skills degrade into thin aliases for commands with no independent reuse value
- the same guidance is copied into both skill and command artifacts and drifts over time
- command-specific constraints quietly redefine what the skill is supposed to mean

### Negative effects

- one extra artifact boundary can add authoring overhead for small systems
- narrowly scoped skills can feel abstract if they have no second consumer yet
- teams can over-split capabilities and create too many tiny skills with little reuse value

### Misuse patterns

- using the technique to justify slash-command taxonomy, routing policy, or marketplace design
- widening the technique into cross-target propagation, installer behavior, or registry semantics
- forcing every workflow command to have a matching skill even when no reusable meaning survives outside the command
- treating shell composability or orchestrator routing as if they were the same boundary problem

### Detection signals

- reviewers cannot explain what the skill owns versus what the command owns
- command docs restate the full skill body instead of referencing it
- a second agent or command cannot use the skill without rewriting its meaning
- discussion focuses on command names and arguments while the reusable capability remains undefined

### Mitigations

- require one short ownership sentence that says what lives in the skill and what lives in the command
- keep invocation syntax, numbered steps, and structured output in the command only
- keep reusable patterns, guidelines, and procedure in the skill only
- decline a separate skill artifact when the capability is truly command-local
- split propagation, routing, marketplace, and shell concerns into separate sibling techniques instead of widening this one

## Validation

Verify the technique by confirming that:
- one skill artifact and one command artifact are named separately
- the skill still makes sense without reading a specific command first
- the command owns arguments, steps, or structured output that do not belong in the skill
- the command references or invokes the skill without copying its full meaning wholesale
- another agent or command can reuse the same skill without changing its core contract
- the bundle does not drift into distribution, propagation, routing, or shell-command doctrine

See `checks/skill-vs-command-boundary-checklist.md`.

## Adaptation notes

What can vary across projects:
- the exact skill file format
- the exact command file format
- whether the command surface is a slash command, subcommand, menu action, or another explicit user-facing entrypoint
- how agents annotate when or why they use a skill
- whether commands invoke skills directly or route through an intermediate orchestrator

What should stay invariant:
- the skill remains the reusable capability artifact
- the command remains the invocation artifact
- commands do not become the canonical home of reusable skill meaning
- the same skill can survive reuse across more than one command or agent

Project-shaped details that should not be treated as invariant:
- slash prefixes such as `/`
- plugin marketplace install flows
- model-routing tables and orchestrator roles
- donor-specific frontmatter keys such as `user-invocable`
- review-agent rosters or inline review pipelines

## Public sanitization notes

This public bundle keeps only the reusable boundary: skill artifacts hold reusable capability meaning, while command artifacts hold user-facing invocation structure. Donor-specific plugin install steps, orchestrator behavior, model routing tables, review-agent catalogs, and command rosters were intentionally left out.

## Example

See `examples/minimal-skill-vs-command-boundary.md`.

## Checks

See `checks/skill-vs-command-boundary-checklist.md`.

## Promotion history

- shaped from `agentic-dev-team`
- adapted with local second-context evidence from `aoa-skills` and `aoa-routing`
- promoted to `aoa-techniques` on 2026-03-23 as a bounded docs technique for separating reusable skill meaning from command invocation surfaces

## Future evolution

- keep `skill-marketplace-curation` as the discovery sibling rather than widening this bundle into catalog policy
- keep `upstream-skill-health-checking` as the upstream-availability sibling rather than turning command surfaces into source-health doctrine
- add another live donor that keeps the same skill-command split outside the current plugin-oriented lineage
