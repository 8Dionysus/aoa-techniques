---
id: AOA-T-0039
name: baseline-first-additive-profile-benchmarks
domain: evaluation
kind: validation
status: promoted
origin:
  project: atm10-agent
  path: README.md
  note: Extracted from a baseline-first cross-service benchmark path where the baseline profile stays default and richer profiles run as additive comparisons on the same normalized measurement surface.
owners:
  - 8Dionysus
tags:
  - evaluation
  - benchmark
  - baseline
  - additive
  - profile
summary: Benchmark one stable baseline profile first, then compare additive profiles against the same measurement surface and artifact shape so richer profiles stay additive and off the default path.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-23
export_ready: true
relations:
  - type: complements
    target: AOA-T-0035
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# baseline-first-additive-profile-benchmarks

## Intent

Keep comparison discipline honest by running one stable baseline profile first, then comparing additive profiles against the same measurement surface and the same artifact shape.

## When to use

- a baseline profile should anchor the benchmark before any richer profile is compared
- additive profiles need to stay secondary rather than becoming the default path
- comparison results should stay like-for-like across the same summary shape
- additive prework needs to be isolated so it does not blur the baseline measurement
- the reusable object is comparison discipline, not benchmark-suite ownership or product scoring

## When not to use

- the main need is profile composition, runtime rendering, host diagnosis, or service lifecycle control
- you want benchmark-suite governance, promotion policy, or a rolling historical baseline system
- there is no stable baseline profile yet
- additive profiles are still experimental enough that their setup would change the default path
- the result would be used to rank products rather than compare bounded profile shapes

## Inputs

- one stable baseline profile
- one or more additive profiles to compare later
- one normalized measurement surface
- one artifact shape that stays consistent across runs
- one isolated place for additive prework when a richer profile needs extra setup

## Outputs

- one baseline result on the canonical measurement surface
- one or more additive comparison results on the same surface and artifact shape
- explicit deltas that can be read without translating between formats
- a clear note about whether the additive path stayed off the default route

## Core procedure

1. Pick the stable baseline profile and run it first.
2. Confirm the benchmark writes the expected normalized artifact shape.
3. Freeze the measurement surface so additive runs are compared against the same contract.
4. Prepare additive profile prework in an isolated path if richer setup is needed.
5. Run the additive profile against the same surface and same artifact shape.
6. Compare only like-for-like fields and keep the baseline as the reference point.
7. Report the comparison as a bounded benchmark result, not as a ranking or promotion decision.

## Contracts

- the baseline profile runs before any additive comparison
- additive profiles reuse the same measurement surface and artifact shape as the baseline
- additive setup stays isolated from the default path
- the benchmark reports comparison discipline, not product scoring
- the technique stays separate from benchmark-suite ownership, promotion policy, and rolling baseline governance
- the contract is about stable comparison, not about profile composition or runtime execution control

## Risks

### Failure modes

- the additive path quietly becomes the new default path
- the measurement surface drifts so baseline and additive runs are no longer comparable
- a rolling historical baseline sneaks in and replaces the stable baseline-first contract
- benchmark results start reading like product scores instead of bounded comparisons

### Negative effects

- additive prework can create setup overhead if it is not kept separate from the baseline path
- a single shared summary shape can hide mismatched assumptions if the surface is not frozen carefully
- comparison language can overreach into governance or promotion decisions

### Misuse patterns

- using the technique to choose a winner instead of to compare bounded profiles
- letting additive setup mutate the default runtime path
- treating benchmark ownership as if it included promotion policy or suite-wide governance
- widening the technique into render review, host readiness, or lifecycle control

### Detection signals

- the default benchmark path now depends on additive-only setup
- baseline and additive runs no longer produce the same artifact shape
- result discussions use ranking or product-scoring language
- people begin to ask whether the benchmark owns policy decisions beyond comparison

### Mitigations

- keep the baseline profile as the first and default comparison point
- require the same normalized measurement surface for both baseline and additive runs
- isolate additive prework in a separate path or step
- reject any wording that turns the technique into suite governance or product ranking

## Validation

Verify the technique by confirming that:
- the baseline run happens before any additive run
- the additive run uses the same measurement surface and artifact shape as the baseline
- additive prework is isolated when extra setup is needed
- the report states comparison results without implying promotion or product ranking
- the benchmark remains readable as a bounded comparison contract

See `checks/baseline-first-additive-profile-benchmarks-checklist.md`.

## Adaptation notes

What can vary across projects:
- the benchmark command or harness name
- the exact profile labels
- the normalized artifact filename
- the underlying service or dataset family being compared
- whether additive prework lives in a script, workflow step, or operator note

What should stay invariant:
- baseline first, additive second
- the same measurement surface for all compared runs
- the same artifact shape for all compared runs
- additive paths remain secondary and isolated
- the result is a comparison discipline, not a policy surface

Relationship to adjacent techniques:
- unlike `AOA-T-0035 profile-preset-composition`, this technique does not define how profiles are composed
- unlike `AOA-T-0036 render-truth-before-startup`, it does not inspect rendered runtime truth
- unlike `AOA-T-0037 contextual-host-doctor`, it does not diagnose readiness or host drift
- unlike `AOA-T-0038 one-command-service-lifecycle`, it does not start or stop the runtime stack

## Public sanitization notes

The public bundle keeps only the reusable benchmark contract: stable baseline first, additive comparison second, same measurement surface, same artifact shape. Donor-specific service names, workflow paths, and private benchmark labels were generalized.

## Example

See `examples/minimal-baseline-first-additive-profile-benchmarks.md`.

## Checks

See `checks/baseline-first-additive-profile-benchmarks-checklist.md`.

## Promotion history

- shaped from a baseline-first benchmark path in `atm10-agent`
- reinforced by a profile-composition posture in `abyss-stack`
- promoted to `aoa-techniques` on 2026-03-23 as a bounded evaluation technique for stable baseline-plus-additive comparisons

## Future evolution

- add a second donor lineage that uses the same baseline-first comparison rule
- add an example with a non-service benchmark family
- add a note on how to keep additive prework isolated when the richer profile has extra setup
