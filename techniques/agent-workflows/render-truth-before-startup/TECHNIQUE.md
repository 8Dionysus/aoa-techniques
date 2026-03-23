---
id: AOA-T-0036
name: render-truth-before-startup
domain: agent-workflows
status: promoted
origin:
  project: abyss-stack
  path: docs/RENDER_TRUTH.md
  note: Extracted from a local runtime workflow that renders the actual composed service and config view before startup so operators can review what Compose really sees.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - runtime-truth
  - preflight
  - render
  - reviewable
summary: Render the actual composed runtime truth before startup so operators review the effective service and config view instead of relying only on declared profiles.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-22
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

# render-truth-before-startup

## Intent

Expose the actual composed runtime truth before startup so operators can review the effective service set and rendered config instead of inferring final behavior from declared profiles or module lists alone.

## When to use

- layered profiles or presets can change the final runtime view in ways that are hard to infer from declarations alone
- overlays or additive runtime layers may add, replace, or reshape services before startup
- operators need one read-only pre-start review seam before a local runtime is launched
- a workflow should catch surprising service composition before containers or processes start
- the real reusable value is the pre-start rendered truth step, not lifecycle control or post-start validation

## When not to use

- the main need is profile and preset composition itself rather than the final composed view
- the main need is host readiness or environment preflight checks
- the main need is startup, waiting, smoke, or internal probes after the runtime is already live
- the rendered output cannot be handled locally with appropriate care for secret-bearing material
- the workflow would turn the render step into a generic config export or publication surface

## Inputs

- one selected profile, preset, or equivalent bounded runtime selection
- one composition engine that can render the final service or config view before startup
- one local review path for service-list output or full rendered config
- one local handling rule for secret-bearing rendered material

## Outputs

- one pre-start view of the actual effective service set
- one optional full rendered config for deeper local review
- earlier visibility into overlays, merges, or surprising service activation
- one clear handoff from review into later startup or readiness steps

## Core procedure

1. Resolve the selected profile, preset, or equivalent runtime choice through the existing composition layer.
2. Render the effective service list from the actual composed runtime view before any startup step runs.
3. Render the full composed config locally when deeper inspection is needed.
4. Treat the full rendered config as potentially secret-bearing and keep it in a local controlled path.
5. Review the rendered service set or config for unexpected merges, overlays, missing services, or surprising additions.
6. Use the render output to answer "what will actually start" before answering "is the host ready" or "did startup succeed".
7. Hand off to startup, wait, smoke, or doctor-style checks only after the rendered truth has been reviewed.

## Contracts

- the render step shows the actual composed runtime view rather than only declared module, profile, or preset intent
- the render step happens before startup
- the technique stays read-only and review-oriented
- the service-list render is the lightweight default, while the full rendered config is optional and more sensitive
- full rendered config is treated as potentially secret-bearing local material rather than a shareable artifact
- composition ownership remains with `AOA-T-0035`; readiness, smoke, and lifecycle ownership remain with sibling techniques
- the technique does not widen into generic config publication, deployment orchestration, or startup control

Relationship to adjacent techniques: unlike `AOA-T-0035`, this technique owns the actual composed runtime view after selection resolves, not the module-profile-preset composition contract itself. Unlike `AOA-T-0032`, it is a local pre-start review step rather than a CI-facing report.

## Risks

### Failure modes

- teams inspect declared profiles and skip the actual rendered view even when overlays can change the final result
- rendered config gets treated like a harmless debug artifact and leaks local sensitive values
- the render step becomes a token gesture that no one reviews before startup
- operators mistake rendered truth for proof that the host is ready or that the runtime will be healthy after launch

### Negative effects

- a render step adds extra friction to very small runtime changes
- full rendered config can overwhelm reviewers when the service-list view would have been enough
- local rendered files can linger longer than intended and become accidental sensitive artifacts
- the rendered output can create false confidence that the runtime is safe to start even when readiness and health remain unchecked

### Misuse patterns

- committing or publishing full rendered config
- widening the technique into doctor checks, smoke checks, or lifecycle wrappers
- using rendered output as the new canonical source of truth instead of as a pre-start inspection seam
- forcing full config rendering every time when a service-list render would have answered the real question

### Detection signals

- startup surprises keep happening even though a render step supposedly exists
- rendered files begin showing up in version control or share-prep flows
- contributors talk about `up`, `wait`, or `smoke` more than about what the render actually exposed
- the service list and full config render are both available, but reviewers still cannot answer what the final runtime will start

### Mitigations

- make the pre-start review question explicit: what does the runtime actually resolve to right now
- use service-list rendering as the first pass and reserve full config rendering for deeper local review
- keep rendered config local, controlled, and ephemeral where possible
- route readiness, smoke, and lifecycle concerns into sibling techniques instead of stretching this one
- treat repeated startup surprise after a render step as evidence that the render output is not actually being reviewed

## Validation

Verify the technique by confirming that:
- the selected runtime can be rendered before startup
- the effective service list comes from the actual composed runtime view rather than from docs or module narration alone
- a full rendered config path exists for deeper local review when needed
- the bundle states that full rendered config may be secret-bearing
- the workflow hands off to startup or readiness checks rather than pretending the render step replaced them

See `checks/render-truth-before-startup-checklist.md`.

## Adaptation notes

What can vary across projects:
- the names of the render commands
- whether the render surface exposes services, full config, or both
- the local file path used for deeper rendered-config review
- the composition engine behind the render step

What should stay invariant:
- the rendered view comes from the actual composed runtime
- the render happens before startup
- the step stays read-only and review-oriented
- secret-bearing rendered config stays local and controlled

Project-shaped details that should not be treated as invariant:
- exact compose tooling
- exact profile or preset names
- systemd, wrapper, or deployment path assumptions
- post-start doctor, smoke, probe, or lifecycle commands

## Public sanitization notes

This public bundle keeps only the reusable pre-start render-review contract. Donor-specific service names, ports, deployed paths, and local secret material handling were generalized so the technique stays portable and public-safe.

## Example

See `examples/minimal-render-truth-before-startup.md`.

## Checks

See `checks/render-truth-before-startup-checklist.md`.

## Promotion history

- extracted from `abyss-stack`
- promoted to `aoa-techniques` on 2026-03-22 as a bounded agent-workflow technique for pre-start rendered runtime review

## Future evolution

- keep `contextual-host-doctor` as the readiness sibling rather than turning render review into host-preflight doctrine
- keep `one-command-service-lifecycle` as the lifecycle sibling rather than absorbing startup control into this technique
- add a second live context if another runtime stack uses the same pre-start rendered-truth seam
