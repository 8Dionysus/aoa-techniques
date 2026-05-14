# Experience Provenance Bridge

This is the active-first bridge from current Experience parts back to the
pre-split Experience seed surfaces. Use it when auditing how source pressure
feeds an active part, not when you need the current operating contract.

## Current Route First

Start with the active surfaces:

- [README](README.md)
- [DIRECTION](DIRECTION.md)
- [PARTS](PARTS.md)
- [parts](parts/)
- [LANDING_LOG](LANDING_LOG.md)

If those surfaces answer the task, stop there. Do not pull old flat paths into
the active route just because they existed before this split.

## Source Map

| Evidence source | Active route | Distilled signal |
|---|---|---|
| Pre-split flat `GOVERNANCE_TECHNIQUE_PRECEDENT.md` | [parts/governance-precedent](parts/governance-precedent/README.md) | Governance techniques are documented as reviewable precedent, not forced local adoption. |
| Pre-split flat `AUTHORITY_RESOLUTION_TECHNIQUES.md` | [parts/authority-resolution](parts/authority-resolution/README.md) | Actor capability and governance authority stay separate; owner meaning remains owner-local. |
| Pre-split flat `APPEAL_REASONING_TECHNIQUES.md` | [parts/appeal-reasoning](parts/appeal-reasoning/README.md) | Appeals and overturns require evidence, decision refs, and explicit authority. |
| Pre-split flat `SEALED_DECISION_TECHNIQUES.md` | [parts/sealed-decision](parts/sealed-decision/README.md) | Commit/reveal, hash-chain review, and tamper-detection practice remain reviewable and owner-local. |
| Pre-split flat `SCOPE_BOUNDARY_TECHNIQUE.md` | [parts/scope-boundary](parts/scope-boundary/README.md) | Office/service scope consumes upstream gates without becoming release approval or runtime ToS write authority. |
| Pre-split flat `HANDOFF_COMPRESSION_TECHNIQUE.md` | [parts/handoff-compression](parts/handoff-compression/README.md) | Handoff compression remains owner-local contract behavior, not live office execution. |
| Pre-split flat `SERVICE_CLARITY_TECHNIQUE.md` | [parts/service-clarity](parts/service-clarity/README.md) | Service clarity remains bounded by owner consent and upstream runtime stop-lines. |

## Contract Packet Bridge

These previous root schema/example packets now travel with the Experience part
that interprets them. Their old internal local-host JSON identifiers were
replaced with public part-local schema URLs; field semantics stayed unchanged.

| Previous root packet | Active route | Distilled signal |
|---|---|---|
| `schemas/appeal_reasoning_step_v1.json` plus `examples/appeal_reasoning_step.example.json` | [parts/appeal-reasoning](parts/appeal-reasoning/README.md) | Appeal reasoning contract evidence belongs beside the appeal part. |
| `schemas/technique_governance_precedent_v1.json` plus `examples/technique_governance_precedent.example.json` | [parts/governance-precedent](parts/governance-precedent/README.md) | Governance precedent contract evidence belongs beside the governance-precedent part. |
| `schemas/sealed_decision_technique_note_v1.json` plus `examples/sealed_decision_technique_note_v1.example.json` | [parts/sealed-decision](parts/sealed-decision/README.md) | Sealed-decision note contract evidence belongs beside the sealed-decision part. |
| `schemas/scope_boundary_technique_note_v1.json` plus `examples/scope_boundary_technique_note_v1.example.json` | [parts/scope-boundary](parts/scope-boundary/README.md) | Scope-boundary contract evidence belongs beside the scope-boundary part. |
| `schemas/handoff_compression_technique_note_v1.json` plus `examples/handoff_compression_technique_note_v1.example.json` | [parts/handoff-compression](parts/handoff-compression/README.md) | Handoff-compression contract evidence belongs beside the handoff-compression part. |
| `schemas/service_clarity_technique_note_v1.json` plus `examples/service_clarity_technique_note_v1.example.json` | [parts/service-clarity](parts/service-clarity/README.md) | Service-clarity contract evidence belongs beside the service-clarity part. |

## Center Context Bridge

| Context source | Active route | Distilled signal |
|---|---|---|
| AoA-center Experience `PARTS.md`, `DIRECTION.md`, `OWNER_REQUESTS.md`, and part contracts | [parts/technique-candidate-bridge](parts/technique-candidate-bridge/README.md) | Local Experience parts must be classified before extraction; center law supplies stop-lines and owner routes, not technique canon. |

## Legacy Posture

The pre-split files were compact active seed surfaces rather than large wave
receipts. Their content moved into part-local active homes. The
[legacy scaffold](legacy/README.md) is present for source-to-active accounting,
and its current raw inventory is empty.

## Experience Rule

When source evidence changes current behavior, update the relevant active part
first, then update this bridge and `LANDING_LOG.md`. Active part docs must not
become runtime authority, release approval, or hidden ToS write permission.
