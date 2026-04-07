---
id: AOA-T-0096
name: pinned-validation-matrix-before-generated-publish
domain: agent-workflows
status: promoted
origin:
  project: aoa-routing + aoa-skills + Dionysus
  path: scripts/build_router.py + tests/test_live_workspace_contracts.py + scripts/publish_core_skill_receipts.py + reports/ecosystem-audits/2026-04-07.cross-repo.surface-detection-wave-rollout-session-harvest.md
  note: Extracted from the surface-detection second-wave landing where local generated rebuilds stayed honest only after validation matched workflow-pinned sibling refs instead of assuming the current workspace main branches.
owners:
  - 8Dionysus
tags:
  - agent-workflows
  - generated-surfaces
  - ci
  - validation
  - publish
summary: Rebuild generated outputs against the same workflow-pinned sibling refs that CI will validate before publish so local green does not overstate merge-readiness.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-04-07
export_ready: true
relations:
  - type: complements
    target: AOA-T-0001
  - type: complements
    target: AOA-T-0042
  - type: complements
    target: AOA-T-0091
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# pinned-validation-matrix-before-generated-publish

## Intent

Rebuild and validate generated outputs against the same workflow-pinned sibling
refs, mirrored surfaces, or bounded upstream inputs that CI will actually read
before publish so local green does not overstate merge-readiness.

## When to use

- the repo publishes generated files or snapshots that depend on sibling repos
  or other bounded upstream surfaces
- CI or release checks validate those outputs against pinned refs rather than
  whatever currently happens to be checked out locally
- local rebuilds look clean against workspace `main`, but publish confidence
  still depends on a narrower validation matrix
- the reusable object is one bounded publish-hygiene law, not a full release
  playbook or automation system

## When not to use

- the generated outputs are fully single-repo and CI reads only the current
  checkout
- the task is ordinary code validation rather than generated-surface publish
  posture
- the route is really one broader ordered-wave playbook or release cutover
  rather than one publish guardrail
- the needed matrix still depends on private runner state or unrevealed inputs
  that cannot be named publicly

## Inputs

- one owner repo that is about to publish generated outputs
- one explicit list of workflow-pinned sibling refs, mirrored inputs, or
  bounded upstream surfaces
- one rebuild or `--check` path that can run against those pinned inputs
- one decision point for publish, defer, or repair

## Outputs

- one local validation pass that matches the workflow-pinned matrix closely
  enough to predict CI honestly
- one generated diff or clean-state result produced against those pinned inputs
- one clearer publish decision grounded in the same inputs CI will use

## Core procedure

1. Start by naming the generated outputs that are about to publish and the
   workflow-pinned sibling refs or mirrored inputs that CI actually validates.
2. Read the workflow or validator contract first; do not substitute local
   workspace `main` by habit.
3. Sync, pin, or otherwise emulate those exact sibling refs locally before the
   rebuild or `--check` pass begins.
4. Rebuild or validate the generated outputs against that pinned matrix rather
   than against whatever happens to be newest in the workspace.
5. If the pinned-matrix pass fails, repair the generated outputs, supporting
   mirrors, or docs against that same bounded matrix instead of widening into
   unrelated cleanup.
6. Publish only after the pinned-matrix pass and the repo-native validators
   agree that the generated outputs are honest.
7. If the route still needs broader merge-order choreography, hand off to a
   playbook or ordered-wave workflow instead of widening this technique.

## Contracts

- the workflow-pinned validation matrix is explicit before rebuild begins
- local workspace state never silently substitutes for pinned refs
- generated publish waits for the pinned-matrix pass, not just a workspace-only
  green check
- repairs stay bounded to the inputs that the workflow actually reads
- the technique stays smaller than full release automation, split-wave playbook
  doctrine, or CI platform design

Relationship to adjacent techniques: unlike
[AOA-T-0001](../plan-diff-apply-verify-report/TECHNIQUE.md), this technique is
not the whole change protocol; it adds one stricter publish rule around pinned
validation inputs for generated outputs. Unlike
[AOA-T-0042](../../evaluation/upstream-skill-health-checking/TECHNIQUE.md), it
does not score upstream readiness in the abstract; it reproduces the exact
publish-time matrix that generated-surface CI will read. Unlike
[AOA-T-0091](../workspace-root-ingress-and-mutation-gate/TECHNIQUE.md), it does
not govern session start or mutation gating; it acts later, when generated
publish honesty is on the line.

## Risks

### Failure modes

- local rebuilds go green against workspace state while CI still reads older or
  pinned sibling refs and fails
- contributors fix the generated files but not the mirrored sources or schemas
  that the workflow actually consumes
- the route widens into broad cross-repo cleanup because the pinned matrix was
  never named sharply enough

### Negative effects

- the technique adds setup overhead before each generated publish
- reproducing pinned refs locally can feel slower than trusting current
  workspace `main`
- public docs can understate how easy it is to overtrust a convenient local
  rebuild

### Misuse patterns

- assuming “latest local sibling checkout” is equivalent to the workflow matrix
- running only repo-local validators while skipping the pinned cross-repo
  rebuild
- using this technique as generic CI debugging advice outside generated publish
  posture
- widening the bundle into full release choreography or automation doctrine

### Detection signals

- CI fails on generated-surface drift that local rebuilds never saw
- the publish route cannot name which sibling refs or mirrored files the
  workflow actually used
- fixes keep landing in generated snapshots while the upstream mirrored
  contract still drifts
- reviewers cannot tell whether the final green state came from pinned inputs
  or from ad hoc workspace state

### Mitigations

- require the pinned validation inputs to be named before rebuild begins
- run the rebuild or `--check` pass against those exact inputs
- keep repair scope bounded to the workflow-consumed mirrors, schemas, docs, or
  generated snapshots
- stop and hand off to an ordered-wave route when the publish path becomes
  broader than one bounded generated-surface closure

## Validation

Verify the technique by confirming that:

- the workflow-pinned sibling refs or mirrored inputs were named explicitly
- the local rebuild or `--check` pass used that same matrix
- generated outputs stayed aligned after the pinned-matrix pass
- repo-native validators also stayed green
- the final publish claim now matches what CI will actually read

See `checks/pinned-validation-matrix-before-generated-publish-checklist.md`.

## Adaptation notes

What can vary across projects:

- the exact workflow system or CI runner
- whether the pinned inputs are sibling repos, mirrored JSON surfaces, schema
  files, or release artifacts
- the exact rebuild command or validation command
- whether the pinned refs are branches, tags, raw URLs, or copied mirrors

What should stay invariant:

- the publish matrix is read before rebuild begins
- the same pinned inputs are used locally before publish
- generated publish waits for that pinned-matrix pass
- the route stays honest about what CI will really validate

Project-shaped details that should not be treated as invariant:

- one repo name such as `aoa-routing` or `aoa-skills`
- one exact validator like `python scripts/build_router.py --check`
- one exact sibling path such as `/srv/aoa-playbooks`
- one exact GitHub Actions workflow file or runner image

AoA adaptation example:

- inspect which sibling surfaces or schema mirrors the workflow reads
- rebuild the generated outputs against those pinned inputs before publish
- repair the bounded mirrors or snapshots that drifted
- publish only after the pinned-matrix pass and repo-native validators agree

## Public sanitization notes

This public bundle keeps only the reusable publish-hygiene law: reproduce the
workflow-pinned matrix first, then rebuild and validate generated outputs
against it. Private runner setup, unrevealed credentials, and project-specific
release bureaucracy were intentionally stripped.

## Example

See `examples/minimal-pinned-validation-matrix-before-generated-publish.md`.

## Checks

See `checks/pinned-validation-matrix-before-generated-publish-checklist.md`.

## Promotion history

- born from the 2026-04-07 surface-detection second-wave landing, where
  `aoa-routing` and `aoa-skills` each needed CI-tail repairs around the
  workflow's real validation inputs before publish could close honestly
- promoted into `aoa-techniques` on 2026-04-07 as a bounded generated-publish
  hygiene technique

## Future evolution

- collect one more non-identical generated-surface repo where the same
  publish-matrix rule holds
- keep split-wave choreography in `aoa-playbooks` instead of widening this
  technique into a release or rollout playbook
- revisit canonical readiness only after the technique proves portable beyond
  the current AoA generated-surface family
