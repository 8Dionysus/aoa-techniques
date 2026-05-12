# Canonical Readiness

## Technique
- id: AOA-T-0068
- name: fail-closed-evidence-gate

## Verdict
- approve for canonical promotion

## Evidence summary
- external origin: the imported technique has a bounded donor contract and explicit exclusions around broader governance stacks, pack formats, durable jobs, and trust-product semantics
- second context: `aoa-techniques` now records the same fail-closed execution seam as a documentation-first adaptation with one example and one checklist
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- `mvar-security/clawzero` provides exact-fit public reinforcement beyond the donor family: it frames the reusable object as a deterministic execution boundary between model output and tool execution, evaluates sink requests before commands or tool calls run, returns explicit allow or block decisions, raises blocked execution in adapters, and generates witness artifacts for later review
- ClawZero's verified-claims and test surfaces reinforce that shell, credential, HTTP, filesystem, LangChain, OpenClaw, MCP, and session-runtime lanes keep block decisions before execution and keep witness or session evidence inspectable
- OpenAI Agents SDK guardrails provide supporting boundary semantics: blocking input guardrails can prevent agent execution before tool calls, tool input guardrails run before custom function tools execute, and `ToolGuardrailFunctionOutput` / `GuardrailFunctionOutput` can carry check details; the bundle keeps SDK coverage limits explicit because parallel input guardrails, hosted tools, built-in execution tools, and handoffs are not a universal fail-closed seam
- validation strength: the bundle now carries one checklist, one example, a clean external-origin note, a documentation-first second context, and public cross-context reinforcement for non-allow outcomes blocking side effects while review evidence survives

## Default-use rationale
- this is the right canonical default when the main problem is blocking mutation on non-allow while preserving reviewable evidence at the boundary
- it remains narrower than [AOA-T-0028](../../../../execution/agent-workflows-core/confirmation-gated-mutating-action/TECHNIQUE.md) because it centers an execution-boundary verdict rather than a human confirmation seam
- it also remains narrower than a durable-jobs surface because it does not own checkpoint, pause, and resume semantics across longer-running work
- it is now strong enough as a canonical default because ClawZero repeats the same execution-boundary gate with explicit decision evidence outside the donor family while letting this bundle reject total policy-platform doctrine, framework-specific adapters, attack-pack governance, signed-witness infrastructure, compliance suites, and human approval flows

## Fresh public-safety check
- review date: 2026-05-12
- result: pass
- sanitization still holds: the bundle keeps only the reusable fail-closed gate and excludes donor-specific policy platforms, pack formats, trust-product breadth, and runtime branding
- public reuse check: the example, checklist, and adaptation notes remain understandable without hidden donor-repo context; the inspected ClawZero source is Apache-2.0 licensed and no source code, attack payloads, local paths, credentials, witness signatures, product setup instructions, or platform-specific runtime wiring were copied into the technique

## Remaining gaps
- no blocker remains for canonical status
- future gate sources can reinforce the default, but they must preserve the narrow boundary: a candidate mutating action, one verdict surface before side effects, explicit non-allow blocking, and one reviewable evidence surface, without importing broad governance platforms, policy authoring stacks, signed-witness infrastructure, attack packs, compliance suites, human approval doctrine, durable job orchestration, or total trust frameworks

## Recommendation
- move `AOA-T-0068` to `canonical`
- add an adverse-effects review to preserve the boundary between fail-closed execution gates, human confirmation, witness traces, durable approval jobs, broad policy engines, and security-platform evidence
