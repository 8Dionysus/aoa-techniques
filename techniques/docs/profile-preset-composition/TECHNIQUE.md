---
id: AOA-T-0035
name: profile-preset-composition
domain: docs
kind: composition
status: promoted
origin:
  project: abyss-stack
  path: docs/PROFILES.md
  note: Extracted from a layered runtime-composition practice that keeps modules, profiles, and presets reviewable without flattening operating modes into one opaque launcher surface.
owners:
  - 8Dionysus
tags:
  - docs
  - runtime-composition
  - profiles
  - presets
  - reviewable
summary: Compose small reusable profiles into named presets so runtime posture stays reviewable without flattening composition into one opaque config or launcher doctrine.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-22
export_ready: true
relations:
  - type: complements
    target: AOA-T-0012
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# profile-preset-composition

## Intent

Keep runtime posture reviewable by separating atomic modules, ordered profiles, and named presets into explicit layers instead of hiding common operating modes inside one large merged configuration.

## When to use

- a stack has several reusable runtime pieces that need legible grouping
- optional layers should compose onto a base runtime path without one giant config file
- common multi-profile operating modes need stable names
- operators should inspect resolved profiles and modules before launch
- the reusable object is the composition contract itself rather than render, startup, or health-check behavior

## When not to use

- one small static stack does not need profile or preset layers
- the main need is pre-start rendered truth for the exact active runtime
- the main need is profile-scoped readiness checks or one-command lifecycle control
- profile and preset names would only hide a simpler direct module list
- the composition scheme depends on implicit discovery instead of explicit bounded lists

## Inputs

- atomic runtime units such as modules or equivalent small building blocks
- named profiles that list modules in activation order
- named presets that list profiles in activation order
- one explicit resolution rule for ordering and duplicate handling
- one read-only inspection path that shows the resolved result before launch

## Outputs

- explicit ownership for the module, profile, and preset layers
- reviewable profile and preset definitions
- repeatable resolved profile and module order
- stable names for common runtime postures
- an inspection-first composition surface before launch

## Core procedure

1. Define the smallest reusable runtime pieces as modules or equivalent atomic units.
2. Group those units into small named profiles that list modules in activation order.
3. Group common multi-profile operating modes into presets that list profile names in activation order.
4. Resolve preset-expanded profiles first and append directly selected profiles afterward.
5. Keep duplicate profiles and duplicate modules only once, at first appearance.
6. Store profile and preset definitions in simple diff-friendly lists rather than in one opaque merged config.
7. Expose read-only inspection surfaces that show resolved presets, profiles, modules, paths, or expected endpoints before launch.
8. Fail fast when a referenced profile or module is missing instead of silently degrading the resolved stack.

## Contracts

- the module, profile, and preset layers each have explicit ownership
- profiles own ordered module lists; presets own ordered profile lists
- preset expansion happens before direct profile additions
- duplicate profiles and modules are kept once, at first appearance
- composition stays reviewable as simple bounded definitions rather than one giant merged launcher surface
- the technique owns layered runtime posture composition, not render, startup, smoke, doctor, or lifecycle actions
- inspection-before-run is part of the contract, but live environment truth and readiness verdicts remain separate sibling techniques

Relationship to adjacent techniques: unlike `AOA-T-0012`, this technique stops at layered runtime composition and read-only inspection rather than deterministic generation of one rendered artifact.

## Risks

### Failure modes

- unrelated concerns get stuffed into one oversized profile or preset
- preset names become convenient labels for combinations whose real layer ownership is no longer clear
- missing references or implicit dependencies survive until launch time because the composition contract is not checked early
- teams use preset names without any reliable way to inspect the resolved profile and module order first

### Negative effects

- extra composition layers can add ceremony for small stacks that do not need them
- stable preset names can make a runtime posture look simpler than it really is
- reviewable lists can still create false confidence if contributors can recite preset names but cannot explain what expands underneath them
- too many weak profiles or presets can turn a clean layering contract into naming clutter

### Misuse patterns

- treating the technique as a generic launcher or platform doctrine
- letting presets become the only place new capability enters instead of adding capability module-first
- widening the bundle into rendered config review, startup flows, or lifecycle wrappers
- encoding secret-bearing host detail or donor-specific deployment roots into what should be portable composition definitions

### Detection signals

- reviewers cannot say why a capability belongs at the module, profile, or preset layer
- the same preset label is used repeatedly while its underlying profile expansion remains implicit
- contributors talk about startup, waiting, smoke, or doctor commands more than the composition contract itself
- composition definitions are no longer small or diff-friendly enough to review as bounded lists

### Mitigations

- require module-first inclusion before adding profile or preset membership
- collapse weak profiles or presets whose names do not protect a real reusable posture
- keep one visible inspection path for resolved presets, profiles, and modules before launch
- fail fast on missing references and ambiguous ownership
- split render, readiness, and lifecycle behavior into sibling techniques instead of widening this bundle

## Validation

Verify the technique by confirming that:
- module, profile, and preset ownership are all explicit
- preset-expanded profiles resolve before direct profile additions
- duplicate profiles and modules are deduped at first appearance
- profile and preset definitions stay small and reviewable
- a read-only inspection path exists before launch
- the bundle does not drift into rendered runtime truth, doctor-style readiness, or lifecycle control

See `checks/profile-preset-composition-checklist.md`.

## Adaptation notes

What can vary across projects:
- the names of modules, profiles, and presets
- whether selectors are repeated flags, comma-separated lists, or another explicit syntax
- the exact storage format for the lists
- the names of the inspection commands or scripts

What should stay invariant:
- module, profile, and preset ownership remains explicit
- preset-expanded profiles resolve before direct profile additions
- duplicate profiles and modules are kept once, at first appearance
- inspection happens before launch rather than only after failure

Project-shaped details that should not be treated as invariant:
- exact ports, hostnames, or deployment roots
- provider-specific compose tooling
- donor-specific profile names such as `agentic` or `intel`
- render, startup, health-check, or lifecycle commands that live outside this composition contract

## Public sanitization notes

This public bundle keeps only the reusable layer contract: modules compose into profiles, profiles compose into presets, and the resolved posture stays inspectable before launch. Donor-specific ports, host paths, compose roots, service names, and lifecycle commands were reduced or generalized.

## Example

See `examples/minimal-profile-preset-composition.md`.

## Checks

See `checks/profile-preset-composition-checklist.md`.

## Promotion history

- extracted from `abyss-stack`
- promoted to `aoa-techniques` on 2026-03-22 as a bounded docs technique for layered runtime composition

## Future evolution

- keep `render-truth-before-startup` as the rendered-runtime sibling rather than widening this bundle into pre-start render review
- keep `contextual-host-doctor` as the readiness sibling rather than turning composition into health-check policy
- keep `one-command-service-lifecycle` as the lifecycle sibling rather than absorbing launch or control doctrine
