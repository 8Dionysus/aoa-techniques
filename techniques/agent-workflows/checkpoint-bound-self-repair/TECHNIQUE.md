---
id: AOA-T-0083
name: checkpoint-bound-self-repair
domain: agent-workflows
kind: recovery
status: promoted
origin:
  project: aoa-skills
  path: skills/aoa-session-self-repair/SKILL.md + skills/aoa-session-self-repair/references/checkpoint-bridge.md
  note: Extracted from the aoa-session-self-repair skill where repair packets must remain behind explicit checkpoint posture instead of feeling like silent self-mutation.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - checkpoint
  - repair
  - rollback
  - approval
summary: Keep self-repair behind explicit checkpoint posture with approval, rollback, health checks, iteration limits, and improvement-log visibility so repair stays reviewable instead of feeling like silent self-modification.
maturity_score: 3
rigor_level: bounded
reversibility: moderate
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-04-05
export_ready: true
relations:
  - type: complements
    target: AOA-T-0082
  - type: complements
    target: AOA-T-0028
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# checkpoint-bound-self-repair

## Intent

Keep self-repair behind explicit checkpoint posture so bounded repair stays
reviewable and reversible instead of feeling like silent self-modification.

## When to use

- a bounded repair shape already exists
- the repair may touch important system surfaces
- reviewers need explicit approval, rollback, health-check, and iteration-limit posture
- the route must remain smaller than one general governance framework while still protecting against silent mutation

## When not to use

- no reviewed diagnosis or repair shape exists yet
- the work is a small non-sensitive edit that does not need a self-repair frame
- the route is trying to bypass approval, rollback, or post-change verification
- the real need is just branch posture or generic confirmation before mutation

## Inputs

- one bounded repair shape
- relevant policy or constitution checks
- approval posture
- rollback anchor
- health-check path
- bounded iteration limit
- improvement-log target

## Outputs

- one checkpoint-bound repair packet
- one explicit approval or confirmation requirement
- one rollback marker
- one post-change health check
- one bounded iteration limit
- one explicit improvement-log or audit stub

## Core procedure

1. Start from a bounded repair shape rather than from free self-improvement language.
2. Require a visible policy or constitution check before important mutation.
3. Require an explicit approval or confirmation seam when the repair is meaningful.
4. Name a rollback marker before the repair executes.
5. Name the health check that will verify the repair afterward.
6. Keep a bounded iteration limit so repair does not turn into hidden retry loops.
7. Write an improvement-log or audit stub so the mutation remains reviewable later.

## Contracts

- self-repair is not free self-modification
- important mutations require checkpoint posture
- rollback and health-check cues remain explicit
- bounded iteration limits prevent hidden retry loops
- improvement logging remains part of the repair contract
- role-law and proof-law changes may need handoff to other owner layers

Relationship to adjacent techniques: unlike [AOA-T-0082](../repair-shape-from-diagnosis/TECHNIQUE.md), this technique does not choose the repair shape itself; it governs the checkpoint posture around an already chosen repair. Unlike [AOA-T-0028](../confirmation-gated-mutating-action/TECHNIQUE.md), it is narrower and more specialized: it governs a self-repair packet with rollback, health-check, and improvement-log posture rather than a general confirmation seam before any mutation.

## Risks

### Failure modes

- checkpoint posture is partial and one critical field is missing
- the repair still feels automatic because approval or rollback is implicit
- iteration loops hide repeated failed self-repair attempts

### Negative effects

- too much checkpoint ceremony can slow obviously safe tiny repairs
- teams may over-trust the checkpoint stack and stop questioning whether the repair should happen at all
- improvement logs can become ceremonial if they are never reread

### Misuse patterns

- using checkpoint posture as a substitute for repair shaping
- treating approval as optional for meaningful self-repair
- hiding doctrine edits behind repair language
- using retries as pseudo-progress instead of escalation

### Detection signals

- rollback anchors or health checks are missing
- no iteration limit is named for a risky repair loop
- reviewers cannot find the improvement-log stub afterward
- repair packets change important surfaces with no visible checkpoint gate

### Mitigations

- require all checkpoint fields for meaningful repairs
- keep escalation available when retries fail
- preserve improvement-log visibility
- keep general mutation confirmation and self-repair checkpoint posture distinct

## Validation

Verify the technique by confirming that:
- a bounded repair shape exists first
- checkpoint fields are all explicit
- rollback and health-check posture are present
- iteration limits and improvement logging are visible
- the repair does not feel like silent self-mutation

See `checks/checkpoint-bound-self-repair-checklist.md`.

## Adaptation notes

What can vary across projects:
- the names of policy or constitution checks
- the approval mechanism
- the rollback-anchor format
- the health-check surface
- the improvement-log location

What should stay invariant:
- checkpoint posture stays explicit
- rollback and health checks remain visible
- iteration stays bounded
- self-repair never feels silent

Project-shaped details that should not be treated as invariant:
- one approval bot or command
- one log filename
- one repo layout
- one governance stack

AoA adaptation example:
- common checkpoint fields include constitution check, approval gate, rollback marker, health check, iteration limit, and improvement-log stub
- role-law changes often hand off to `aoa-agents`, and proof-law changes often hand off to `aoa-evals`

## Public sanitization notes

This public bundle keeps only the reusable self-repair checkpoint seam: visible policy fit, approval, rollback, health checks, bounded retries, and improvement logging. AoA repo names, local approval commands, and skill wrappers were reduced to adaptation examples or kept out of the invariant core.

## Example

See `examples/minimal-checkpoint-bound-self-repair.md`.

## Checks

See `checks/checkpoint-bound-self-repair-checklist.md`.

## Promotion history

- born in `aoa-skills` as the checkpoint-bridge half of `aoa-session-self-repair`
- extracted into `aoa-techniques` on 2026-04-05 as a bounded self-repair checkpoint technique

## Future evolution

- keep repair shaping separate through `AOA-T-0082`
- keep general mutation confirmation separate through `AOA-T-0028`
- add a second live context that uses the same checkpoint-bound self-repair seam outside the current AoA session-harvest lineage
