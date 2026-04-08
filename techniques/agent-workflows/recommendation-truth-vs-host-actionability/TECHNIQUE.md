---
id: AOA-T-0093
name: recommendation-truth-vs-host-actionability
domain: agent-workflows
kind: guardrail
status: promoted
origin:
  project: aoa-sdk + Dionysus
  path: src/aoa_sdk/skills/detector.py + src/aoa_sdk/models.py + src/aoa_sdk/cli/main.py + docs/skill-runtime-recommendation-gap.md + docs/skill-runtime-recommendation-gap-fix-spec.md + Dionysus/reports/ecosystem-audits/2026-04-06.aoa-sdk.skill-runtime-recommendation-gap-fix-session-harvest.md
  note: Extracted from a live skill-runtime seam repair where router recommendation truth stayed authoritative while host actionability moved to explicit availability annotation and canonical install-root discovery.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - control-plane
  - recommendation
  - actionability
  - skills
summary: Keep router recommendation truth separate from host actionability so non-executable recommendations stay visible, canonical install roots stay authoritative, and runnable actions do not masquerade as merely relevant advice.
maturity_score: 3
rigor_level: bounded
reversibility: moderate
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-04-06
export_ready: true
relations:
  - type: complements
    target: AOA-T-0091
  - type: complements
    target: AOA-T-0042
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# recommendation-truth-vs-host-actionability

## Intent

Keep router recommendation truth and host actionability separate so control-plane reports stay honest, activation only reflects what the current host can execute, and missing local installs do not erase semantically relevant guidance.

## When to use

- a control plane recommends skills, capabilities, or bounded workflow objects from a corpus that may be larger than the current host install
- the system needs to preserve why an item was recommended even when the host cannot execute it directly
- `activate_now`, `must_confirm`, and `suggest_next` need honest actionability semantics rather than one blended relevance score
- canonical install roots or explicit host manifests exist and must determine executability separately from routing logic
- risk gates still need to stay visible even when the host only has a manual fallback path

## When not to use

- every recommended object is always bundled with the same runtime and host executability can never diverge
- the real need is upstream source readiness before publication rather than local host actionability after recommendation
- the real need is discovery-query design, marketplace curation, or registry policy instead of control-plane honesty
- the real need is skill-command ownership or docs routing rather than runtime availability semantics
- the system has no meaningful distinction between auto-activation, explicit confirmation, and non-executable guidance

## Inputs

- one router recommendation result such as `activate_now`, `must_confirm`, and `suggest_next`
- one explicit host inventory source or one ordered install-root discovery rule
- one small precedence rule between manual overrides and auto-discovered roots
- one availability annotation shape that can represent executable, router-only, and unknown states
- one report surface that exposes both recommendation reasoning and host actionability

## Outputs

- one annotated recommendation report where each item keeps both its routing reason and its host-availability state
- one explicit actionability-gap surface for items that remain relevant but are not directly executable
- one `activate_now` set constrained to host-executable items only
- one visible record of which inventory source or install root determined executability
- one clearer operator decision about whether to execute, confirm manually, install, or defer

## Core procedure

1. Produce the recommendation result from routing logic before consulting host inventory.
2. Resolve host inventory separately through explicit overrides or a small ordered set of canonical install roots.
3. Annotate each recommended item with a host-availability state such as `host-executable`, `router-only`, or `unknown`, plus the inventory source that produced the verdict.
4. Treat `router-only` as a real semantic recommendation state, not as invalidity or irrelevance.
5. Keep `activate_now` limited to `host-executable` items. If an auto-activated item is not executable, demote it out of `activate_now` and surface the gap explicitly.
6. Leave `must_confirm` and `suggest_next` visible even when an item is `router-only`, especially when manual fallback is still allowed or operator attention is still required.
7. Emit one clear report-level note when host inventory was missing, partial, or auto-discovered so reviewers can tell how actionability was resolved.
8. Keep inventory precedence explicit and small; do not infer executability from repo-export theater, stale assumptions, or hidden local state.
9. If a required risk gate is only `router-only` and no safe manual path exists, stop and surface that impossibility instead of pretending the gate passed.

## Contracts

- router recommendation truth is computed separately from host executability
- host inventory source and precedence remain explicit
- `activate_now` requires `host-executable`
- `router-only` is not treated as invalid, irrelevant, or silently dropped
- `must_confirm` remains visible and actionable even when an item is not directly executable
- `unknown` remains a visible state instead of collapsing into either success or absence
- the technique stays smaller than discovery doctrine, marketplace curation, registry governance, or upstream-health policy

Relationship to adjacent techniques: unlike [AOA-T-0042](../../evaluation/upstream-skill-health-checking/TECHNIQUE.md), this technique does not ask whether an upstream source is publishable or reachable; it governs local host actionability after recommendation already happened. Unlike [AOA-T-0091](../workspace-root-ingress-and-mutation-gate/TECHNIQUE.md), it does not decide when ingress and guard run; it governs the truth split inside their reports. Unlike [AOA-T-0064](../../docs/capability-discovery/TECHNIQUE.md), it does not own discovery-query semantics; it starts after one bounded recommendation set already exists.

## Risks

### Failure modes

- host actionability leaks back into recommendation truth, so relevant items disappear when they are merely unavailable
- auto-discovered install roots silently override explicit host manifests or operator-provided overrides
- `activate_now` still includes non-executable items, so the control plane overstates what can run
- `router-only` items are hidden instead of being surfaced as actionable gaps
- the system treats one repo-local export surface as if it were the canonical proof of host executability

### Negative effects

- the technique adds annotation and reporting overhead for very small systems
- a more honest split can feel stricter or noisier because non-executable items stay visible
- canonical install-root discovery adds one more precedence surface that contributors need to understand

### Misuse patterns

- treating `router-only` as a broken-skill verdict instead of a local actionability verdict
- collapsing `unknown` into `false` to make reports look simpler
- widening the bundle into marketplace, registry, or trust policy
- hardcoding one repository's install paths as universal invariants

### Detection signals

- a report cannot explain why an item was recommended separately from why it is or is not executable
- `activate_now` contains items marked non-executable
- missing host inventory causes the system to drop semantically relevant recommendations entirely
- `must_confirm` items disappear when they are router-only instead of remaining visible
- reviewers cannot tell which install root or manifest produced the host-availability verdict

### Mitigations

- require one explicit availability annotation and one explicit source field per item
- keep precedence between overrides and auto-discovery small and readable
- emit `actionability_gaps` instead of silently filtering router-only items away
- fail closed when a required risk gate has no honest executable or manual path
- keep host-actionability rules adjacent to, but separate from, discovery and upstream-health doctrine

## Validation

Verify the technique by confirming that:
- a recommendation can remain visible even when it is not directly executable on the host
- `activate_now` contains only `host-executable` items
- an originally auto-activated router-only item is demoted and surfaced as an actionability gap
- explicit host overrides take precedence over auto-discovered install roots when both exist
- canonical install roots are checked in declared order
- a router-only `must_confirm` item remains visible instead of disappearing
- the report states whether host inventory was explicit, auto-discovered, or missing

See `checks/recommendation-truth-vs-host-actionability-checklist.md`.

## Adaptation notes

What can vary across projects:
- the exact report format
- the exact host-inventory carrier such as CLI flags, manifest files, or runtime inspection
- the ordered install roots and how they are discovered
- the exact status labels used for host availability
- whether manual fallback is modeled as a separate field or inferred from context

What should stay invariant:
- recommendation truth is produced independently from host actionability
- host actionability is annotated explicitly rather than implied
- `activate_now` is reserved for host-executable items
- router-only recommendations remain visible
- inventory precedence remains explicit and reviewable

Project-shaped details that should not be treated as invariant:
- exact paths such as `.agents/skills`
- one workspace root such as `/srv`
- one exact CLI spelling such as `aoa skills detect`
- one exact JSON key such as `host_inventory_provided`
- one exact trio of labels such as `host-executable`, `router-only`, and `unknown`

AoA adaptation example:
- route skill relevance through the detector first
- resolve host actionability from explicit host manifests or canonical repo, workspace, and user install roots
- demote non-executable auto-actions out of `activate_now`
- keep router-only gates visible in `must_confirm` instead of pretending the host already satisfied them

## Public sanitization notes

This public bundle keeps only the reusable control-plane law: recommendation truth and host actionability are separate surfaces, and reports must preserve both. AoA-specific path names, CLI output details, local install quirks, and session-local debugging context were reduced to adaptation examples or left out.

## Example

See `examples/minimal-recommendation-truth-vs-host-actionability.md`.

## Checks

See `checks/recommendation-truth-vs-host-actionability-checklist.md`.

## Promotion history

- born from the `aoa-sdk` skill-runtime recommendation-gap repair on 2026-04-06
- harvested in `Dionysus` as a surviving control-plane law on 2026-04-06
- promoted into `aoa-techniques` on 2026-04-06 as a bounded recommendation-versus-executability split for skill control planes

## Future evolution

- keep upstream source readiness in `AOA-T-0042` instead of widening this bundle into publish-time health doctrine
- keep workspace ingress and mutation posture in `AOA-T-0091` instead of making this a general session-start technique
- revisit stricter fail-fast posture for router-only risk gates only after another live host context proves the same seam outside the current `aoa-sdk` lineage
