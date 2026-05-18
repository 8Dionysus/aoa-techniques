# Chat History Lineage Governed Actions - Planting Order

This note is for operator-guided staging inside `aoa-techniques`.

## Hard rules

- keep Wave 1C registry-only on the first pass
- do not create candidate bundles from this closed packet
- do not revisit session capture, transcript packaging, or witness export families from this packet
- keep governed-action candidates narrower than platform or policy doctrine

## Landed first

1. `transcript-replay-artifact` is now landed as `AOA-T-0066` by the main agent
2. `transcript-linked-code-lineage` is now landed as `AOA-T-0067` by the main agent
3. `fail-closed-evidence-gate` is now landed as `AOA-T-0068` by the main agent
4. `approval-bound-durable-jobs` is now landed as `AOA-T-0069` by the main agent

## Preferred sequence

5. `agent-readiness-telemetry` is closed without import; see `docs/AGENT_READINESS_TELEMETRY_CLOSEOUT_MEMO.md`
6. `signed-trace-artifacts` is closed without import; see `docs/SIGNED_TRACE_ARTIFACTS_CLOSEOUT_MEMO.md`

Why this order:

- replay and code-lineage were the cleanest history seams
- the fail-closed gate and durable jobs were landable only after their narrower execution boundaries were named clearly
- telemetry and signed traces stayed too wide against existing report, witness, and pack-platform surfaces
- browser and why-retrieval candidates collapsed too easily into app or retrieval product doctrine

Current closeout verdicts:

- keep `agent-readiness-telemetry` out of `techniques/` for now
- keep `signed-trace-artifacts` out of `techniques/` for now
- use `docs/AGENT_READINESS_TELEMETRY_CLOSEOUT_MEMO.md` and `docs/SIGNED_TRACE_ARTIFACTS_CLOSEOUT_MEMO.md` as final packet rationale

## Stop conditions

Stop and leave the shard staged if:

- a history candidate needs capture, memory, or hosted platform semantics to explain itself
- a governed-action candidate still needs policy platform doctrine
- a lineage candidate no longer stays smaller than generic analytics or retrieval
