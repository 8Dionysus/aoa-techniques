---
id: AOA-T-0091
name: workspace-root-ingress-and-mutation-gate
domain: agent-workflows
status: promoted
origin:
  project: aoa-sdk + 8Dionysus
  path: src/aoa_sdk/skills/detector.py + src/aoa_sdk/cli/main.py + docs/WORKSPACE_INSTALL.md + /srv/AGENTS.md
  note: Extracted from the workspace-foundation landing wave where federated AoA work starts through an explicit ingress pass and risky mutation is gated through a second workspace-aware guard pass.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - workspace
  - ingress
  - mutation-gate
  - federation
summary: Enter federated workspaces through one explicit ingress pass and gate risky mutation through one explicit guard pass so session posture stays reviewable instead of hiding in operator memory.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-04-06
export_ready: true
relations:
  - type: complements
    target: AOA-T-0060
  - type: complements
    target: AOA-T-0028
  - type: complements
    target: AOA-T-0061
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# workspace-root-ingress-and-mutation-gate

## Intent

Enter federated workspaces through one explicit ingress pass and require one explicit guard pass before risky mutation so session posture stays visible, reviewable, and anchored to the workspace root instead of hiding in operator memory.

## When to use

- work starts from a sibling workspace that contains several related repositories under one root
- the next step depends on choosing one primary repo root while still respecting workspace-level guidance
- the operator or agent needs a visible readout of relevant skills, must-confirm gates, and blocked actions before changing code, config, runtime, or shared artifacts
- the reusable object is one bounded session posture law for federated work, not a total startup platform or mission framework

## When not to use

- the task is truly single-repo and no meaningful workspace-root posture exists
- the main need is just one opening read-and-verify ritual without any workspace-specific guard seam
- the workflow already lives inside a narrower confirmed mutation contract and does not need a separate ingress pass
- the route would widen into workspace installation, repo bootstrap, or full closeout orchestration doctrine

## Inputs

- one workspace root
- one primary repo root or one explicit reason to keep the workspace root primary for now
- one short statement of intent for the current pass
- one mutation surface classification when mutation is actually planned

## Outputs

- one explicit ingress report for the current workspace and repo root
- one explicit guard report before risky mutation
- one visible list of `activate_now`, `must_confirm`, `suggest_next`, and `blocked_actions`
- one clearer operator decision to proceed, confirm, defer, or reroute before mutation

## Core procedure

1. Start by naming the workspace root and the primary repo root for the current pass.
2. Before substantial work, run one ingress pass against that repo root from the workspace root.
3. Read the returned `activate_now`, `must_confirm`, `suggest_next`, and `blocked_actions` instead of carrying session posture implicitly.
4. If the task stays read-only, continue from the ingress report without inventing a second guard step.
5. Before risky, mutating, infra, runtime, repo-config, or public-share actions, run one guard pass with the intended mutation surface.
6. Treat `must_confirm` and `blocked_actions` as real gates rather than as decorative hints.
7. Allow safe auto-activation only where the detector already permits it; keep `explicit-only` skills visible instead of silently firing them.
8. Keep closeout, post-session growth chains, and owner-layer authorship outside this technique unless they become the actual route anchor.

## Contracts

- the workspace root is explicit before ingress runs
- one primary repo root is named for the current pass, even when it is temporarily the workspace root itself
- ingress happens before substantial work
- guard happens before risky mutation, not after
- `must_confirm` and `blocked_actions` remain actionable gates
- the technique stays smaller than workspace install doctrine, repo bootstrap, closeout routing, and owner-layer authorship

Relationship to adjacent techniques: unlike [AOA-T-0060](../session-opening-ritual-before-work/TECHNIQUE.md), this technique does not own the general “read current state before work” ritual for any resumed session; it owns the workspace-root posture where ingress and pre-mutation guard are explicit control-plane passes. Unlike [AOA-T-0028](../confirmation-gated-mutating-action/TECHNIQUE.md), it does not replace the local confirmation seam around one concrete mutation; it prepares the workspace-aware gate posture before mutation is even allowed. Unlike [AOA-T-0061](../cross-repo-resource-map-bootstrap/TECHNIQUE.md), it does not author a cross-repo map artifact; it governs how an active session should enter and guard work once a federated workspace already exists.

## Risks

### Failure modes

- ingress becomes symbolic and nobody actually reads the returned posture
- guard runs too late, after mutation is already underway
- the workspace root and repo root stay implicit, so the reports are generated against the wrong surface

### Negative effects

- the technique can add ceremony when the task is tiny or obviously read-only
- contributors may overtrust detector output and skip deeper repo-specific reasoning
- a workspace law can drift into a project-specific launcher if too many install or runtime details accumulate inside it

### Misuse patterns

- treating any startup command as equivalent to ingress even when no structured posture is returned
- using guard as a retrospective explanation after mutation already happened
- widening the bundle into full workspace install, closeout, or skill-governance doctrine

### Detection signals

- the operator cannot name which repo root ingress targeted
- risky mutation happens with no visible guard report
- `must_confirm` items are silently skipped
- the technique starts accumulating install instructions, repo-local overlays, or full closeout routes as invariants

### Mitigations

- require one explicit workspace root and repo root per pass
- keep ingress and guard outputs visible in the session trail
- stop when `blocked_actions` or unresolved `must_confirm` items apply
- route install doctrine, bootstrap, and closeout behavior to sibling bundles once they become the real center of gravity

## Validation

Verify the technique by confirming that:
- ingress runs before substantial work begins
- the current repo root and workspace root are explicit
- risky mutation triggers a guard pass before mutation starts
- `must_confirm` and `blocked_actions` remain visible and actionable
- the technique still makes sense without importing workspace install or closeout doctrine

See `checks/workspace-root-ingress-and-mutation-gate-checklist.md`.

## Adaptation notes

What can vary across projects:
- the exact CLI or API used to run ingress and guard
- whether reports are written to JSON files, logs, terminal output, or another reviewable artifact
- the set of mutation-surface labels
- how the workspace root and repo root are discovered

What should stay invariant:
- one ingress pass happens before substantial workspace work
- one guard pass happens before risky mutation
- the workspace root and primary repo root are explicit
- the returned gate posture stays visible rather than hidden in memory

Project-shaped details that should not be treated as invariant:
- `/srv` as the workspace root
- one specific foundation profile name
- one exact path like `.aoa/skill-dispatch`
- one exact command spelling such as `aoa skills enter` or `aoa skills guard`
- one specific host wrapper or local runtime shell script

AoA adaptation example:
- choose one primary `repo_root` under the sibling workspace
- run ingress from the workspace root before substantial work
- run guard before code, infra, runtime, repo-config, or public-share mutation
- keep explicit-only skill activations visible instead of silently auto-running them

## Public sanitization notes

This public bundle keeps only the reusable posture law: explicit workspace ingress before work and explicit pre-mutation guard before risky change. AoA path names, foundation rollout details, root ownership repair, closeout telemetry, and local wrapper specifics were reduced to adaptation notes or kept out of the invariant core.

## Example

See `examples/minimal-workspace-root-ingress-and-mutation-gate.md`.

## Checks

See `checks/workspace-root-ingress-and-mutation-gate-checklist.md`.

## Promotion history

- born in the AoA workspace-foundation landing wave across `aoa-sdk`, `8Dionysus`, and `/srv` root guidance
- extracted into `aoa-techniques` on 2026-04-06 as a bounded workspace posture technique for explicit ingress and pre-mutation guard passes

## Future evolution

- keep workspace installation and bootstrap doctrine separate instead of widening this technique into full landing guidance
- keep local confirmation seams separate instead of replacing narrower mutation-gate techniques
- add a second live context outside the current AoA sibling workspace once another federated project uses the same ingress-plus-guard posture
