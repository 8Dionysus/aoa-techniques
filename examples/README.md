# Examples District

This directory holds public-safe worked examples for `aoa-techniques`.

Root examples show how a reader or agent can apply technique-canon contracts in
a concrete situation. They demonstrate route shape, posture, and use while
technique bundles, docs contracts, generated surfaces, validators, tests, and
owner repositories keep authority.

## Placement

| Example kind | Home |
|---|---|
| Repo-wide public-entry, placement, or technique-canon walkthrough | `examples/` |
| Technique-local usage example | owning `techniques/**/examples/` |
| Mechanic behavior, mechanic schema instance, or part-local usage | `mechanics/<slug>/.../examples/` |
| Sibling repository implementation or runtime usage | owning sibling repository |
| Proof, regression, or acceptance fixture | `tests/`, `schemas/`, generated validators, or owner proof surface |

## Current Examples

| Example | Demonstrates | Source surfaces |
|---|---|---|
| [plan-diff-apply-verify-report-walkthrough.md](plan-diff-apply-verify-report-walkthrough.md) | how `AOA-T-0001` moved from origin practice to published portable technique evidence | [Technique](../techniques/execution/agent-workflows-core/plan-diff-apply-verify-report/TECHNIQUE.md), [second-context adaptation](../techniques/execution/agent-workflows-core/plan-diff-apply-verify-report/notes/second-context-adaptation.md), [canonical readiness](../techniques/execution/agent-workflows-core/plan-diff-apply-verify-report/notes/canonical-readiness.md) |

## Example Shape

Each root example names:

- the source surfaces it illustrates
- the route, placement, or technique-canon behavior it demonstrates
- the boundary that keeps the example illustrative
- the local checks or AGENTS validation path to use after related edits

Agent read order, placement checks, validation, and closeout live in
[AGENTS](AGENTS.md).
