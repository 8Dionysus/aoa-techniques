# Narrowing Memo - signed-trace-artifacts

This memo records the current narrowing result for the remaining Wave 1C candidate `signed-trace-artifacts`.

It is a staging note only.
It does not create a canonical bundle or authorize import by itself.

## Candidate chosen

- `signed-trace-artifacts`
- donor: `Clyra-AI/gait`

## Overlap watch

- [AOA-T-0045](../../../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md)
- [AOA-T-0068](../../../techniques/agent-workflows/fail-closed-evidence-gate/TECHNIQUE.md)

## Boundary statement

The current donor evidence does not yet expose one standalone signed-trace artifact contract smaller than broader pack, trust, and evidence-platform doctrine.

What is public today is a mixed evidence cluster:

- the donor talks about signed packs, callpacks, and related portable evidence objects
- signing semantics are closely coupled to broader verify and governance surfaces
- the same donor keeps execution gates, durable jobs, and pack portability near the trace language

That is useful evidence posture, but it is not yet one sharply bounded technique in the `aoa-techniques` sense.

The narrowest plausible extraction target is:

- one reviewable trace artifact that carries explicit integrity or signing proof without expanding into a broader pack platform

Even that smaller target is not stable enough yet, because the donor still presents the live surface mainly as a broader evidence-pack and trust substrate rather than as one reusable signed trace artifact contract smaller than [AOA-T-0045](../../../techniques/history/witness-trace-as-reviewable-artifact/TECHNIQUE.md).

## What stays out

- pack, callpack, and broader evidence-container doctrine
- PKI, trust, and verification platform breadth
- execution-gate semantics already bounded by [AOA-T-0068](../../../techniques/agent-workflows/fail-closed-evidence-gate/TECHNIQUE.md)
- scheduler and durable-job semantics
- speculative claims that signed traces already exist as one sharply bounded public artifact contract

## Evidence snapshot

- the donor pack specification describes broader signed evidence envelopes rather than one small trace object
- the surrounding docs keep signing closely coupled to verify and policy surfaces
- the donor's live bounded seams for this wave were cleaner at the fail-closed gate and durable-job layers than at the signed-trace layer
- existing history witness surfaces still provide the more honest bounded artifact contract for now

## Verdict

- keep `signed-trace-artifacts` in the `narrowing-only` lane
- do not create a bundle yet
- do not assign a technique ID yet

## Honest reopen trigger

Reopen this candidate only if the donor or a second public context can say, in plain language:

- what the signed trace object is
- which integrity or signing fields are part of the bounded contract
- how the object stays smaller than pack-platform doctrine and smaller than generic trust or PKI systems
- why the reusable center is a signed trace artifact rather than a broader portable evidence platform

## Files touched or proposed

- touched: this memo
- touched: Wave 1C staging docs and registry to link the memo and keep the narrowing lane honest
- not proposed yet: no `TECHNIQUE.md`, no bundle-local example, no checklist seed, no note package

## Whether operator approval is needed

- no operator approval needed to keep this candidate in narrowing-only state
- operator approval is required before any future move from this memo into a real technique bundle
