---
id: AOA-T-0029
name: nested-rule-loading
domain: docs
status: promoted
origin:
  project: ruler
  path: README.md
  note: Adapted from the open-source ruler project, which supports nested rule layers with explicit precedence while keeping source ownership one-way and canonical.
owners:
  - 8Dionysus
tags:
  - docs
  - hierarchy
  - precedence
  - rule-loading
  - anti-drift
summary: Load hierarchical rule layers with explicit precedence so nested additions stay subordinate to one canonical source of ownership.
maturity_score: 3
rigor_level: bounded
reversibility: moderate
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-21
export_ready: true
relations:
  - type: complements
    target: AOA-T-0013
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

# nested-rule-loading

## Intent

Load rule content through a hierarchy of layers so shared defaults, scoped overrides, and explicit precedence can coexist without turning nested layers into independent sources of truth.

## When to use

- repositories or instruction trees that already organize rules into parent and nested layers
- projects that need explicit precedence between shared defaults and scoped local additions
- workflows where the issue is layer loading order, not broad multi-target distribution
- cases where nested layers should remain subordinate to one canonical source of ownership

## When not to use

- repositories that only need one flat instruction surface
- workflows where the real need is one canonical rule source fanning out to multiple managed targets
- projects that cannot keep precedence rules explicit and reviewable
- cases where the broader need is MCP propagation, skills propagation, or other product-width orchestration

## Inputs

- one canonical rule source that owns shared meaning
- one or more nested rule layers that add scoped content
- one explicit precedence order between parent and child layers
- one loading step that resolves the hierarchy without hand-merging every layer

## Outputs

- layered rule output with deterministic precedence
- shared defaults preserved at the canonical layer
- scoped nested additions kept visible and subordinate
- lower drift risk when parent rules evolve

## Core procedure

1. Author the shared rule core in one canonical source.
2. Place nested layers only where scoped additions or overrides are needed.
3. Define the precedence order explicitly before relying on the loaded result.
4. Load parent rules and nested layers in the declared order rather than by implicit filesystem accident.
5. Keep each nested layer subordinate to the canonical source of ownership.
6. Re-run the loader whenever shared rules or precedence rules change.
7. Review the final layered output together with the source hierarchy so ownership stays legible.

## Contracts

- one canonical source owns the shared meaning
- nested layers are scoped additions, not independent canonical homes
- precedence is explicit and reviewable
- the same hierarchy and loading rules produce the same resolved rule order
- nested layers must not silently become the source of truth
- this technique stays centered on hierarchical loading, not on multi-target propagation or broader orchestration

Relationship to adjacent techniques: unlike `AOA-T-0013`, this technique is about hierarchical rule loading and explicit precedence inside a layered tree rather than one canonical rule source fanning out to many managed targets. It complements `AOA-T-0013` by handling the nested-layer case without widening into multi-target distribution.

## Risks

### Failure modes

- precedence becomes implicit, so nested layers override parent meaning in ways reviewers cannot predict
- nested layers start behaving like independent canonical sources instead of scoped subordinate layers
- the loading order drifts from the documented hierarchy and the resolved rule set no longer matches the source tree

### Negative effects

- hierarchical loading can hide simple rule changes behind multiple layers when the precedence contract is not obvious
- nested overrides can make the resolved output look stable while the ownership boundary has already blurred
- maintainers may add more layer-specific exceptions instead of narrowing the shared rule core

### Misuse patterns

- widening the technique into full rule distribution across unrelated targets
- using nested loading as a substitute for explicit source ownership
- hiding MCP, skills, or installer behavior inside the same contract
- letting nested layers accumulate special-case policy until the hierarchy becomes unreadable

### Detection signals

- reviewers cannot explain why one rule wins over another without implementation details
- a nested layer starts carrying meaning that should clearly live in the parent canonical source
- the same hierarchy resolves differently after small unrelated edits
- the team talks more about target behavior than about the declared precedence rules

### Mitigations

- keep precedence explicit and documented alongside the hierarchy
- re-route shared meaning back into the canonical source instead of multiplying nested overrides
- limit nested layers to scoped additions that remain easy to trace
- split broader propagation or product behavior into separate techniques if it starts to dominate the contract

## Validation

Verify the technique by confirming that:
- one canonical source is still the owner of shared meaning
- nested layers resolve in the documented precedence order
- removing a nested layer only removes its scoped additions
- nested layers remain subordinate to the canonical source
- the resolved output is repeatable from the declared hierarchy

See `checks/nested-rule-loading-checklist.md`.

## Adaptation notes

What can vary across projects:
- the file layout used for parent and nested rule layers
- the exact loader or build step that resolves the hierarchy
- the amount of scoped override each nested layer is allowed to carry
- the syntax used to describe precedence

What should stay invariant:
- one canonical source owns the shared rule meaning
- nested layers remain subordinate and scoped
- precedence is explicit rather than implicit
- the technique stays about hierarchical loading, not a general propagation or orchestration system

Project-shaped details that should not be treated as invariant:
- exact directory names in the donor repository
- CLI packaging or install flow
- MCP propagation
- skills propagation
- broader product features around the loader

## Public sanitization notes

This import narrows the donor repository to one bounded pattern: hierarchical rule loading with explicit precedence and one-way source ownership. MCP propagation, skills propagation, installer behavior, and broader product-width detail were intentionally left out of the public technique contract.

## Example

See `examples/minimal-nested-rule-loading.md` and `examples/concrete-hierarchical-rule-loading.md`.

## Checks

See `checks/nested-rule-loading-checklist.md`.

## Promotion history

- adapted from open-source `ruler`
- promoted into `aoa-techniques` on 2026-03-21 as a bounded external-import technique for hierarchical rule loading with explicit precedence

## Future evolution

- split out a sibling for nested loading plus target propagation if a future repository proves both contracts are reusable together
- split out a dedicated precedence-mapping sibling if explicit resolution rules become reusable beyond layered rule loading
- add a stronger second live context if another public repository adopts the same hierarchical rule-loading contract
