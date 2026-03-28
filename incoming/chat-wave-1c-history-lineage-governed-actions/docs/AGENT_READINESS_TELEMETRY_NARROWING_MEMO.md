# Narrowing Memo - agent-readiness-telemetry

This memo records the current narrowing result for the remaining Wave 1C candidate `agent-readiness-telemetry`.

It is a staging note only.
It does not create a canonical bundle or authorize import by itself.

## Candidate chosen

- `agent-readiness-telemetry`
- donor: `git-ai-project/git-ai`

## Overlap watch

- [AOA-T-0032](../../../techniques/evaluation/context-report-for-ci/TECHNIQUE.md)
- [AOA-T-0010](../../../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md)
- [AOA-T-0067](../../../techniques/history/transcript-linked-code-lineage/TECHNIQUE.md)

## Boundary statement

The current donor evidence does not yet expose one standalone readiness-telemetry contract smaller than broader analytics product behavior.

What is public today is a mixed observability cluster:

- the donor README talks about accepted, committed, and deployed AI code
- those metrics naturally pull toward dashboards, scorecards, and program-level evaluation
- the same donor keeps lineage, retrieval, and telemetry close together instead of surfacing one isolated readiness metric contract

That is useful observability posture, but it is not yet one sharply bounded technique in the `aoa-techniques` sense.

The narrowest plausible extraction target is:

- a bounded telemetry slice that measures whether agent-produced changes are ready enough to move forward

Even that smaller target is not stable enough yet, because the donor still presents the evidence mainly as a broader analytics story rather than as one reviewable telemetry artifact or verdict contract smaller than existing evaluation techniques.

## What stays out

- contributor or model scorecards
- broader productivity or deployment analytics
- lineage lookup already bounded by [AOA-T-0067](../../../techniques/history/transcript-linked-code-lineage/TECHNIQUE.md)
- generic dashboard product behavior
- speculative claims that readiness telemetry is already one cleanly bounded artifact or verdict contract

## Evidence snapshot

- the donor README highlights accepted, committed, and deployed AI code statistics
- those metrics sit inside a wider provenance and analytics posture rather than inside one standalone readiness object
- the same donor surfaces lineage and `/ask` retrieval closely beside telemetry, which increases drift pressure toward a larger product surface
- existing evaluation siblings already hold cleaner bounded contracts around reports and snapshots

## Verdict

- keep `agent-readiness-telemetry` in the `narrowing-only` lane
- do not create a bundle yet
- do not assign a technique ID yet

## Honest reopen trigger

Reopen this candidate only if the donor or a second public context can say, in plain language:

- what the readiness telemetry artifact or verdict is
- which fields belong to that bounded object
- how it stays smaller than analytics dashboards and smaller than provenance or retrieval product behavior
- why the reusable center is a readiness telemetry contract rather than a broader scorecard

## Files touched or proposed

- touched: this memo
- touched: Wave 1C staging docs and registry to link the memo and keep the narrowing lane honest
- not proposed yet: no `TECHNIQUE.md`, no bundle-local example, no checklist seed, no note package

## Whether operator approval is needed

- no operator approval needed to keep this candidate in narrowing-only state
- operator approval is required before any future move from this memo into a real technique bundle
