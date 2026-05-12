# Adverse Effects Review

## Technique
- id: AOA-T-0068
- name: fail-closed-evidence-gate

## Review focus
- promotion from `promoted` to `canonical` after exact-fit public reinforcement from `mvar-security/clawzero`, with OpenAI Agents SDK guardrails used only as supporting boundary-semantics evidence
- confirm that the bundle remains one fail-closed execution-boundary gate with reviewable evidence, not a broad policy platform, security product, human approval loop, durable job orchestrator, or witness-signing framework

## Failure modes
- advisory checks are described as fail-closed even though side effects can still happen
- parallel or post-hoc guardrails are treated as sufficient for side-effect prevention when they can run too late
- evidence records prove that a check ran, but not that the mutating action was actually blocked
- broad policy platforms, attack-pack harnesses, witness-signing infrastructure, or compliance suites become hidden requirements for the technique

## Negative effects
- fail-closed gates add friction and can block legitimate local work when the verdict surface is too coarse
- shallow evidence can create false confidence by showing a block label without enough context to review the blocked action
- over-broad gates can push simple human-confirmation needs into heavier machine-policy or security-platform machinery

## Misuse patterns
- using this bundle as a substitute for [AOA-T-0028](../../../../execution/agent-workflows-core/confirmation-gated-mutating-action/TECHNIQUE.md) when the actual need is explicit human confirmation before mutation
- using this bundle as a substitute for [AOA-T-0045](../../../../history/history-artifacts/witness-trace-as-reviewable-artifact/TECHNIQUE.md) when the actual need is a fuller run trace with ordered events and state deltas
- using this bundle as a substitute for [approval-bound-durable-jobs](../../approval-bound-durable-jobs/TECHNIQUE.md) when the actual need is checkpoint, pause, approval, and resume across longer-running work
- importing attack demonstrations, policy-profile matrices, adapter-specific command names, signed-witness chains, compliance export formats, or framework setup as invariant requirements

## Detection signals
- the gate can emit a non-allow verdict while the action still executes
- examples say "blocked" but do not name the candidate action, verdict, and evidence surface
- implementation advice centers policy authoring, security products, signed receipts, or attack-pack validation more than one boundary immediately before side effects
- reviewers cannot tell whether ambiguous, missing, or errored verdicts default to block rather than allow

## Mitigations
- require explicit allow before side effects continue
- treat missing, ambiguous, failed, or non-allow verdicts as blocked until a bounded review resolves them
- keep one concise evidence record for the verdict and basis, while routing full traces, signed witness chains, compliance exports, and durable job state to sibling techniques
- document coverage limits when a framework guardrail only applies to certain tool types, execution modes, or pipeline stages

## Recommendation
- safe to promote as a canonical agent-workflow guardrail when the gate sits directly before a mutating boundary, non-allow blocks execution, and a reviewable evidence surface survives the verdict
- keep future revisions narrow: do not absorb human approval, durable orchestration, total policy-platform governance, signed-witness infrastructure, attack harnesses, or broad security-product semantics into this bundle
