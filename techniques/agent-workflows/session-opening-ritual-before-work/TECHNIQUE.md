---
id: AOA-T-0060
name: session-opening-ritual-before-work
domain: agent-workflows
kind: handoff
status: promoted
origin:
  project: thebasedcapital/nightcrawler
  path: README.md + skills/nightcrawler-episode.md
  note: Adapted from Nightcrawler's mandatory session-opening ritual to keep pre-mutation state reading and baseline verification explicit without importing the donor's mission loop, task picking, or runtime orchestration.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - session-start
  - handoff
  - baseline
  - verification
summary: Start a resumed or handed-off session with one visible read-and-verify ritual before the first mutation so work begins from current state rather than stale assumptions.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-28
export_ready: true
relations:
  - type: complements
    target: AOA-T-0057
evidence:
  - kind: external_origin
    path: notes/external-origin.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: external_review
    path: notes/external-import-review.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# session-opening-ritual-before-work

## Intent

Start a resumed or handed-off session with one visible read-and-verify ritual before the first mutation so work begins from current state rather than stale assumptions, optimistic memory, or inherited momentum.

## When to use

- work is resuming after a session boundary, handoff, or context gap
- a new operator or agent needs to align with current repo state before editing
- the next step depends on whether the expected baseline still matches visible reality
- the reusable object is one bounded pre-work ritual, not a total mission boot stack

## When not to use

- work is continuing inside one uninterrupted session and the current state is already in view
- there is no meaningful handoff, baseline, or state surface to re-read
- the main missing seam is concrete git-backed claim verification, packet authoring, task selection, or a full baseline test gate
- the pattern only makes sense when bundled with a whole orchestrator, runtime, or project-methodology stack

## Inputs

- one current handoff, recent summary, or other session-start context surface
- one visible repo-state surface such as status, target files, or current branch state
- one upcoming work item that should not start until the baseline is trusted

## Outputs

- one explicit starting baseline for the resumed session
- one visible note of any mismatch between expected and actual state
- one decision to proceed, restage, or re-scope before editing

## Core procedure

1. Before the first mutation, read the current handoff, summary, or equivalent session-start surface.
2. Inspect one visible baseline surface such as working-tree status, target files, or another current-state signal that matters to the next step.
3. Compare the expected starting point against what the repo or artifact surface actually shows.
4. Record any mismatch explicitly instead of carrying the inherited narrative forward unchanged.
5. Start work only after the baseline is trusted enough to explain the first honest move.
6. Keep the ritual narrow enough that it remains one pre-work read-and-verify seam rather than a task router, test suite, handoff packet template, or orchestration framework.
7. Route packet authoring, claim-by-claim git verification, task prioritization, and broader startup or mission doctrine to sibling techniques when they become the real center of gravity.

## Contracts

- the resumed session includes a visible read step before the first mutation
- at least one current-state surface is checked before continuation trusts the inherited baseline
- mismatches between expected and actual state stay explicit
- the first real move can be explained from the verified starting baseline
- the technique stays smaller than handoff authoring, git-backed claim verification, task selection, test-gating doctrine, and full project boot stacks

Relationship to adjacent techniques: unlike [AOA-T-0057](../structured-handoff-before-compaction/TECHNIQUE.md), this technique does not write the handoff packet; it consumes whatever starting context already exists. Unlike [AOA-T-0059](../git-verified-handoff-claims/TECHNIQUE.md), it does not perform a claim-by-claim git verdict on concrete handoff assertions; it owns the broader pre-mutation ritual that says a session must visibly re-read and re-check baseline state before acting. Unlike [AOA-T-0001](../plan-diff-apply-verify-report/TECHNIQUE.md), it does not own the full change loop through apply, verify, and report. It also stays smaller than total startup doctrine because it does not choose tasks, manage budgets, run orchestration loops, or define a general mission protocol.

## Risks

### Failure modes

- the ritual becomes a symbolic checklist and no real baseline is actually checked
- the inherited summary is read but not compared against current repo state
- the baseline stays too vague to catch a real mismatch before edits begin

### Negative effects

- the workflow can gain ceremony when the work is small enough that no real session gap exists
- contributors may overtrust the opening ritual and skip deeper verification that a particular claim still needs
- the seam can drift into a total startup framework if every pre-work concern gets folded into it

### Misuse patterns

- treating any opening checklist as equivalent even when no real state verification happens
- widening the technique into task picking, baseline test mandates, or mission-governance doctrine
- using the ritual as a substitute for writing a real handoff packet or for verifying concrete git claims

### Detection signals

- edits begin before any visible read or state check occurs
- the operator cannot name what current-state surface was checked
- a mismatch is discovered later even though the opening ritual supposedly completed
- the bundle starts accreting task routing, test commands, or orchestration rules unrelated to the narrow session-start seam

### Mitigations

- require one visible read step and one visible current-state check before mutation
- keep mismatch notes explicit and carry them into the revised starting plan
- route detailed git verification, packet authoring, and broader startup policy to sibling bundles
- use a lighter path when there is no real cross-session gap to recover from

## Validation

Verify the technique by confirming that:
- the opening ritual happens before the first mutation
- at least one explicit current-state surface is checked, not just reread from memory
- mismatches can be named and can stop or redirect work
- the first honest move can be explained from the verified baseline
- the technique still makes sense without task-routing doctrine, baseline test suites, or a full orchestrator stack

See `checks/session-opening-ritual-before-work-checklist.md`.

## Adaptation notes

What can vary across projects:
- which starting context surfaces are read first, such as a handoff note, issue summary, task sheet, or state file
- which baseline check is used, such as `git status`, target-file inspection, branch comparison, or another visible state signal
- where mismatch notes are recorded
- whether the ritual is for same-user session recovery or cross-agent continuation
- how much evidence is enough before the session may proceed

What should stay invariant:
- the read-and-verify step happens before mutation
- the session start trusts visible current state over inherited assumptions
- mismatches remain explicit
- the ritual stays short enough to remain a bounded opening seam

Project-shaped details that should not be treated as invariant:
- one `STATE.json`, `MISSION.md`, or `tasks.json` contract
- launchd supervision, overnight mission framing, or budget caps
- one mandatory test or lint suite at session start
- one task-priority policy or autonomous planning loop
- one orchestrator runtime, CLI wrapper, or collaboration mode

## Public sanitization notes

This import narrows the donor to one bounded pattern: before a resumed session starts changing code, read the current context and verify one visible baseline so work begins from reality rather than inherited narration. Task picking, baseline test gates, handoff writing, immutable task trackers, launchd supervision, overnight mission loops, and broader orchestration semantics were intentionally left out of the public contract.

## Example

See `examples/minimal-session-opening-ritual-before-work.md`.

## Checks

See `checks/session-opening-ritual-before-work-checklist.md`.

## Promotion history

- adapted from open-source `thebasedcapital/nightcrawler`
- staged through the chat wave 3 handoff-bounded-continuation lane inside `aoa-techniques`
- promoted into `aoa-techniques` on 2026-03-28 as a bounded external-import technique for pre-mutation session-start reading and baseline verification

## Future evolution

- keep handoff authoring separate instead of widening this bundle into a total continuation protocol
- keep concrete git-backed claim verification separate instead of turning the opening ritual into a review bundle
- keep task picking, baseline test doctrine, and runtime startup stacks separate instead of importing a whole mission framework
