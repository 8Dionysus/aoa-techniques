# Adverse Effects Review

## Technique
- id: AOA-T-0040
- name: skill-vs-command-boundary

## Review focus
- current role: canonical default for separating reusable skill meaning from user-facing command invocation and command-local workflow entrypoints
- current watch seam: keep the bundle centered on the skill-command ownership split rather than marketplace curation, one-source fan-out, shell doctrine, routing policy, or product-specific command design

## Failure modes
- command files copy full skill meaning until the reusable capability only exists inside invocation wrappers
- a skill becomes command-specific because arguments, output formatting, and user-timing constraints are written into the shared artifact
- platforms that expose skills through slash invocation make reviewers forget that invocation syntax and reusable meaning are still different review questions
- side-effectful task skills are auto-invoked because invocation control is not reviewed separately from skill content

## Negative effects
- canonical status can encourage teams to split tiny one-off prompts into skills and commands even when no reusable capability exists
- strict separation can create duplicate wording if the command cannot reference the skill cleanly
- command wrappers can hide important constraints if reviewers only inspect the shared skill artifact
- skill reuse can become brittle when several commands depend on unstated command-local assumptions

## Misuse patterns
- treating every slash command as proof of reusable skill meaning
- folding command syntax, shell commands, routing hints, or marketplace metadata into the reusable skill contract
- using the technique for cross-agent propagation that belongs to `AOA-T-0027`
- claiming the boundary is satisfied when skill and command artifacts duplicate each other without a reference rule

## Detection signals
- the same procedure appears in both skill and command files with small uncontrolled variations
- reviewers cannot identify which artifact owns reusable guidance and which artifact owns invocation behavior
- command arguments or output requirements become prerequisites for reading the skill
- routing or marketplace discussions dominate a review that should be about skill meaning and command entry

## Mitigations
- keep one explicit rule for how a command references or invokes the reusable skill
- keep skill bodies focused on reusable capability and command files focused on user-facing invocation details
- use invocation-control fields or local policy for side-effectful actions instead of hiding timing constraints in prose
- route propagation, marketplace curation, shell composability, and routing hints to sibling techniques
- revisit canonical status if platforms collapse the distinction so far that invocation control becomes the real reusable object

## Recommendation
- keep current `canonical` status and use this note as the watch surface for duplicated guidance, command-local skill drift, unsafe auto-invocation, and widening into routing or shell-command doctrine
