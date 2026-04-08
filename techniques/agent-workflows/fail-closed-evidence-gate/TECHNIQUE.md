---
id: AOA-T-0068
name: fail-closed-evidence-gate
domain: agent-workflows
kind: guardrail
status: promoted
origin:
  project: Clyra-AI/gait
  path: README.md + docs/agent_integration_boundary.md + docs/mcp_capability_matrix.md
  note: Adapted from the open-source gait project, which places a verdict service directly in front of tool execution so non-allow outcomes block side effects and still emit reviewable evidence.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - gate
  - fail-closed
  - evidence
  - approval
summary: Stop mutating execution at the boundary unless an explicit allow verdict exists, and emit reviewable evidence for blocked or allowed paths instead of relying on best-effort warnings.
maturity_score: 3
rigor_level: bounded
reversibility: moderate
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-28
export_ready: true
relations:
  - type: complements
    target: AOA-T-0028
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

# fail-closed-evidence-gate

## Intent

Stop mutating execution at the boundary unless an explicit allow verdict exists, and emit reviewable evidence for blocked or allowed paths instead of relying on best-effort warnings, advisory logs, or silent fallthrough.

## When to use

- tool execution or another mutating boundary should not continue on ambiguous or non-allow outcomes
- the gate should leave behind one reviewable evidence artifact instead of only printing warnings
- callers need a clear distinction between allowed execution and blocked execution
- the reusable object is one fail-closed evidence gate, not a whole security constitution or policy platform

## When not to use

- the path is read-only and no real side effects are at stake
- the real gap is still human confirmation rather than a gate verdict surface
- the system needs a full policy engine, governance stack, or trust platform to make sense
- durable background jobs or long-running approval flows are the real center of gravity
- the gate would degrade into advisory linting that still lets side effects through

## Inputs

- one candidate mutating action or tool call
- one explicit gate surface that can issue an allow or non-allow verdict
- one evidence artifact path or equivalent review surface
- one execution boundary that can actually block side effects when verdicts are non-allow

## Outputs

- one explicit allow or non-allow verdict before side effects continue
- one evidence artifact that records the verdict and the basis for it
- lower risk that warnings or soft failures still allow real mutation
- one reviewable seam between candidate execution and actual side effects

## Core procedure

1. Intercept the candidate mutating action before side effects happen.
2. Send the action through one explicit verdict surface that can return allow or non-allow.
3. Treat every non-allow outcome as a real block on execution rather than as advisory output.
4. Emit one evidence artifact that records the verdict and the bounded context needed for later review.
5. Continue only on explicit allow rather than on silence, partial success, or ambiguous policy output.
6. Keep the evidence gate smaller than a full governance platform, durable job system, or trust constitution.
7. Split out approval-bound continuation, trace signing, or broader policy stacks if they become the real center of gravity.

## Contracts

- the gate sits directly in front of mutating execution
- non-allow verdicts block side effects rather than merely warning
- one evidence artifact survives the verdict for later review
- explicit allow is required for execution to continue
- the technique stays smaller than human confirmation doctrine, durable-job orchestration, and broad policy-platform semantics
- the evidence artifact supports review but does not itself become the whole trace or governance system

Relationship to adjacent techniques: unlike [AOA-T-0028](../confirmation-gated-mutating-action/TECHNIQUE.md), this technique does not center a human confirmation seam; it centers an execution-boundary verdict that fails closed unless allow is explicit. Unlike [AOA-T-0045](../../history/witness-trace-as-reviewable-artifact/TECHNIQUE.md), it does not preserve a fuller run artifact with ordered steps and state-delta semantics. Unlike `approval-bound-durable-jobs`, it does not own multi-step pause and resume across longer-running work; it owns the bounded gate at the side-effect boundary itself.

## Risks

### Failure modes

- the gate says non-allow but side effects still happen
- evidence artifacts are too thin to explain why execution was blocked
- ambiguous verdicts are treated like allow by convenience
- the bundle widens into total policy-platform doctrine

### Negative effects

- fail-closed gates can add friction to fast local workflows
- a strong gate can create false confidence if the evidence artifact is shallow or misleading
- teams may over-route work through the gate when a simpler confirmation seam would have been enough

### Misuse patterns

- treating warning-level output as if it were already fail-closed
- widening the bundle into broad policy governance, trust stacks, or product constitutions
- expecting the evidence artifact to replace fuller witness traces or durable job history
- using the gate as a general code-review substitute

### Detection signals

- reviewers cannot prove that non-allow really blocks side effects
- evidence artifacts do not identify the blocked action or the verdict basis
- discussions drift toward total platform governance rather than one bounded execution seam
- long-running pause, checkpoint, and resume behavior starts creeping into the gate contract

### Mitigations

- keep the execution boundary explicit and test that non-allow truly blocks mutation
- make evidence artifacts concrete enough for later review
- treat ambiguous outcomes as blocked until made explicit
- split durable jobs, signed traces, and broader governance systems into sibling techniques instead of widening this bundle

## Validation

Verify the technique by confirming that:
- the gate sits before a real mutating boundary
- non-allow outcomes actually block side effects
- one evidence artifact records the verdict and the bounded context for review
- explicit allow is required before execution proceeds
- the explanation still makes sense without a full security or governance platform

See `checks/fail-closed-evidence-gate-checklist.md`.

## Adaptation notes

What can vary across projects:
- the verdict carrier such as CLI, service, library call, or MCP surface
- the evidence artifact format
- whether the gate sits in front of one tool call or a small bounded action batch
- the exact non-allow labels used by the project

What should stay invariant:
- the gate is execution-boundary-adjacent
- non-allow blocks side effects
- one evidence artifact survives the verdict
- allow must be explicit

Project-shaped details that should not be treated as invariant:
- one command name or protocol
- donor pack formats or enforcement runtime names
- broader policy-authoring stacks
- total trust, PKI, or compliance frameworks

## Public sanitization notes

This public bundle keeps only the reusable fail-closed seam: place one verdict boundary directly before mutating execution, block non-allow outcomes, and emit one reviewable evidence artifact. Donor-specific policy stacks, pack formats, trust product semantics, and platform governance were intentionally removed or generalized.

## Example

See `examples/minimal-fail-closed-evidence-gate.md`.

## Checks

See `checks/fail-closed-evidence-gate-checklist.md`.

## Promotion history

- adapted from open-source `Clyra-AI/gait`
- landed from the Wave 1C history-lineage-governed-actions shard inside `aoa-techniques`
- promoted into `aoa-techniques` on 2026-03-28 as a bounded external-import technique for fail-closed execution gating with reviewable evidence output

## Future evolution

- keep [AOA-T-0028](../confirmation-gated-mutating-action/TECHNIQUE.md) as the human-confirmation sibling rather than widening this bundle into human approval doctrine
- keep durable multi-step continuation separate rather than absorbing longer-running job orchestration into the gate
- reopen signed evidence as a separate sibling only if it survives without widening back into a full trace or policy platform
