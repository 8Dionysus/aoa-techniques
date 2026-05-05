# Agent-Workflows-Core Direct-Read Migration Review

Source packet:
[Technique Reform Ingress](../README.md)

Previous landed review:
[Landed Intent-Chain Pilot Review](landed-intent-chain-pilot-review.md)

Generated lens:
[Technique Tree Projection](../../../../../reports/technique_tree_projection.md)

Tree contract:
[Technique Tree Contract](../../../../../docs/TECHNIQUE_TREE_CONTRACT.md)

Status: accepted-for-eighteenth-migration-pilot, not path migration, not
`tree_path` frontmatter.

## Verdict

Accept `execution/agent-workflows-core` as the eighteenth bounded migration
pilot.

Move exactly `AOA-T-0001`, `AOA-T-0014`, `AOA-T-0023`, `AOA-T-0028`, and
`AOA-T-0031` in the next migration step, if and only if the move preserves
IDs, `domain`, `kind`, status, relations, evidence, support files, and
public-safety posture. This review does not move files.

The shelf is coherent because the five leaves form the portable execution
backbone for visible, bounded, reviewable agent work:

- `AOA-T-0001` owns the general plan -> diff -> apply -> verify -> report
  loop for non-trivial repository work.
- `AOA-T-0014` owns one behavior slice inside implementation when tests should
  constrain the change before refactor expansion.
- `AOA-T-0023` owns the stateless single-shot fast path before a task widens
  into a multi-step workflow.
- `AOA-T-0028` owns the explicit confirmation seam before one mutating action.
- `AOA-T-0031` owns shell-visible composability through stdin, stdout, files,
  and pipes.

This acceptance does not make `agent-workflows-core` generic agent doctrine,
shell policy, product policy, approval policy, autonomous orchestration,
hidden agent scheduling, runtime lifecycle law, or broad methodology doctrine.
It stays a technique shelf for keeping agent work explicit, bounded,
reviewable, and easy to hand off to a narrower sibling technique when the
task's center changes.

## Sources Read

- [AOA-T-0001 plan-diff-apply-verify-report](../../../../../techniques/execution/agent-workflows-core/plan-diff-apply-verify-report/TECHNIQUE.md)
- [AOA-T-0001 checklist](../../../../../techniques/execution/agent-workflows-core/plan-diff-apply-verify-report/checks/review-checklist.md)
- AOA-T-0001 support notes:
  [canonical readiness](../../../../../techniques/execution/agent-workflows-core/plan-diff-apply-verify-report/notes/canonical-readiness.md),
  [second context](../../../../../techniques/execution/agent-workflows-core/plan-diff-apply-verify-report/notes/second-context-adaptation.md),
  and
  [adverse effects](../../../../../techniques/execution/agent-workflows-core/plan-diff-apply-verify-report/notes/adverse-effects-review.md)
- [AOA-T-0014 tdd-slice](../../../../../techniques/execution/agent-workflows-core/tdd-slice/TECHNIQUE.md)
- [AOA-T-0014 checklist](../../../../../techniques/execution/agent-workflows-core/tdd-slice/checks/tdd-slice-checklist.md)
- AOA-T-0014 support notes:
  [origin evidence](../../../../../techniques/execution/agent-workflows-core/tdd-slice/notes/origin-evidence.md),
  [second context](../../../../../techniques/execution/agent-workflows-core/tdd-slice/notes/second-context-adaptation.md),
  [canonical readiness](../../../../../techniques/execution/agent-workflows-core/tdd-slice/notes/canonical-readiness.md),
  and
  [adverse effects](../../../../../techniques/execution/agent-workflows-core/tdd-slice/notes/adverse-effects-review.md)
- [AOA-T-0023 stateless-single-shot-agent](../../../../../techniques/execution/agent-workflows-core/stateless-single-shot-agent/TECHNIQUE.md)
- [AOA-T-0023 checklist](../../../../../techniques/execution/agent-workflows-core/stateless-single-shot-agent/checks/stateless-single-shot-agent-checklist.md)
- AOA-T-0023 support notes:
  [external origin](../../../../../techniques/execution/agent-workflows-core/stateless-single-shot-agent/notes/external-origin.md),
  [second context](../../../../../techniques/execution/agent-workflows-core/stateless-single-shot-agent/notes/second-context-adaptation.md),
  [external import review](../../../../../techniques/execution/agent-workflows-core/stateless-single-shot-agent/notes/external-import-review.md),
  [canonical readiness](../../../../../techniques/execution/agent-workflows-core/stateless-single-shot-agent/notes/canonical-readiness.md),
  and
  [adverse effects](../../../../../techniques/execution/agent-workflows-core/stateless-single-shot-agent/notes/adverse-effects-review.md)
- [AOA-T-0028 confirmation-gated-mutating-action](../../../../../techniques/execution/agent-workflows-core/confirmation-gated-mutating-action/TECHNIQUE.md)
- [AOA-T-0028 checklist](../../../../../techniques/execution/agent-workflows-core/confirmation-gated-mutating-action/checks/confirmation-gated-mutating-action-checklist.md)
- AOA-T-0028 support notes:
  [external origin](../../../../../techniques/execution/agent-workflows-core/confirmation-gated-mutating-action/notes/external-origin.md),
  [second context](../../../../../techniques/execution/agent-workflows-core/confirmation-gated-mutating-action/notes/second-context-adaptation.md),
  [external import review](../../../../../techniques/execution/agent-workflows-core/confirmation-gated-mutating-action/notes/external-import-review.md),
  [canonical readiness](../../../../../techniques/execution/agent-workflows-core/confirmation-gated-mutating-action/notes/canonical-readiness.md),
  and
  [adverse effects](../../../../../techniques/execution/agent-workflows-core/confirmation-gated-mutating-action/notes/adverse-effects-review.md)
- [AOA-T-0031 shell-composable-agent-invocation](../../../../../techniques/execution/agent-workflows-core/shell-composable-agent-invocation/TECHNIQUE.md)
- [AOA-T-0031 checklist](../../../../../techniques/execution/agent-workflows-core/shell-composable-agent-invocation/checks/shell-composable-agent-invocation-checklist.md)
- AOA-T-0031 support notes:
  [external origin](../../../../../techniques/execution/agent-workflows-core/shell-composable-agent-invocation/notes/external-origin.md),
  [second context](../../../../../techniques/execution/agent-workflows-core/shell-composable-agent-invocation/notes/second-context-adaptation.md),
  [external import review](../../../../../techniques/execution/agent-workflows-core/shell-composable-agent-invocation/notes/external-import-review.md),
  [canonical readiness](../../../../../techniques/execution/agent-workflows-core/shell-composable-agent-invocation/notes/canonical-readiness.md),
  and
  [adverse effects](../../../../../techniques/execution/agent-workflows-core/shell-composable-agent-invocation/notes/adverse-effects-review.md)
- [Agent-workflows route card](../../../../../techniques/agent-workflows/AGENTS.md)
- [Execution route card](../../../../../techniques/execution/AGENTS.md)
- [Agent-workflows core semantic review](../../../../../docs/AGENT_WORKFLOWS_CORE_SEMANTIC_REVIEW.md)
- [Kind ambiguity review for `AOA-T-0028`](second-kind-ambiguity-review-pack.md)
- [Technique family scout rows for `agent-workflows-core`](../../../../../reports/technique_family_scout.md)
- [Technique topology scout rows for `agent-workflows-core`](../../../../../reports/technique_topology_scout.md)
- [Technique tree projection rows for `agent-workflows-core`](../../../../../reports/technique_tree_projection.md)

## Direct Bundle Read

| technique | current posture | shelf read |
|---|---|---|
| `AOA-T-0001` | `domain: agent-workflows`, `kind: workflow`, `status: canonical`, `validation_strength: cross_context` | general execution backbone for scoped changes, explicit validation, rollback thinking, and final report |
| `AOA-T-0014` | `domain: agent-workflows`, `kind: workflow`, `status: canonical`, `validation_strength: cross_context` | bounded behavior-slice discipline when tests should constrain one implementation change |
| `AOA-T-0023` | `domain: agent-workflows`, `kind: workflow`, `status: canonical`, `validation_strength: cross_context` | shell-side stateless single-shot fast path before a task needs broader workflow orchestration |
| `AOA-T-0028` | `domain: agent-workflows`, `kind: guardrail`, `status: canonical`, `validation_strength: cross_context` | explicit confirmation seam before one mutating action, not a full workflow replacement |
| `AOA-T-0031` | `domain: agent-workflows`, `kind: composition`, `status: canonical`, `validation_strength: cross_context` | shell-visible one-shot composability through stdin, stdout, files, and pipes |

The relation spine is useful:

- `AOA-T-0001` complements `AOA-T-0004` and `AOA-T-0005`, which are now the
  narrower `intent-chain` shelf.
- `AOA-T-0014` complements `AOA-T-0001`.
- `AOA-T-0028` complements `AOA-T-0023`.
- `AOA-T-0031` complements `AOA-T-0023`.

The support files keep the same split. `AOA-T-0001` and `AOA-T-0014` center
multi-step repository work and one bounded implementation slice. `AOA-T-0023`,
`AOA-T-0028`, and `AOA-T-0031` center one-shot shell-side work, explicit
mutation confirmation, and shell composability. That makes the shell-facing
cluster visible inside the shelf, but does not require a separate shelf yet:
the shared browsing question is still how a portable agent work unit stays
bounded before it becomes hidden autonomy or runtime-specific orchestration.

## Why The Earlier Broad-Shelf Hold No Longer Blocks

Earlier landed reviews held `agent-workflows-core` back because it was too
large to become the first execution precedent. That was correct.

It no longer blocks this direct-read step because `ready-work-graphs` and
`intent-chain` are already landed and reviewed under `execution/`. The trunk
now has two smaller precedents with route-card stop lines. `agent-workflows-core`
can be reviewed as the next, wider execution shelf without being allowed to
move by adjacency.

The direct read also changes the old semantic-review pressure. The older
`AGENT_WORKFLOWS_CORE_SEMANTIC_REVIEW.md` remains useful for the backbone
seams around `AOA-T-0001`, `AOA-T-0004`, and `AOA-T-0014`, but it is not the
current migration source of truth for this shelf because `AOA-T-0004` has
already moved to `intent-chain` and the projected shelf now includes
`AOA-T-0023`, `AOA-T-0028`, and `AOA-T-0031`.

## Execution Trunk Fit

The shelf belongs under `execution` because it answers how bounded agent work
is planned, sliced, invoked, confirmed, composed, verified, and stopped before
it turns into hidden autonomy.

Fit signals:

- stable generated projection: `execution` trunk, `agent-workflows-core` shelf,
  `candidate` review status
- all five leaves are canonical
- direct relation pairs already keep the broad workflow backbone, bounded
  implementation slice, single-shot fast path, confirmation seam, and shell
  composability distinct
- route-card alignment: execution can store bounded work that is prepared,
  sequenced, attempted, checked, or closed without becoming hidden
  orchestration

Watch signals:

- `AOA-T-0001` can become generic process doctrine if concrete verification
  and reviewable diffs stop being central.
- `AOA-T-0014` can become ritualized TDD if the behavior slice is not clear.
- `AOA-T-0023` can become a hidden loop if "single-shot" stops being enforced.
- `AOA-T-0028` can drift toward `workflow`; keep `guardrail` because the
  explicit confirmation seam is the center.
- `AOA-T-0031` can drift into generic shell advice or product-specific CLI
  doctrine if shell-visible composition stops being central.

## Proposed Move

Move exactly these five bundles in the next step:

| technique | current path | proposed path |
|---|---|---|
| `AOA-T-0001` | `techniques/agent-workflows/plan-diff-apply-verify-report/` | `techniques/execution/agent-workflows-core/plan-diff-apply-verify-report/` |
| `AOA-T-0014` | `techniques/agent-workflows/tdd-slice/` | `techniques/execution/agent-workflows-core/tdd-slice/` |
| `AOA-T-0023` | `techniques/agent-workflows/stateless-single-shot-agent/` | `techniques/execution/agent-workflows-core/stateless-single-shot-agent/` |
| `AOA-T-0028` | `techniques/agent-workflows/confirmation-gated-mutating-action/` | `techniques/execution/agent-workflows-core/confirmation-gated-mutating-action/` |
| `AOA-T-0031` | `techniques/agent-workflows/shell-composable-agent-invocation/` | `techniques/execution/agent-workflows-core/shell-composable-agent-invocation/` |

Migration requirements:

- preserve `domain: agent-workflows`
- preserve each `kind`, including `AOA-T-0028` as `guardrail` and
  `AOA-T-0031` as `composition`
- preserve canonical status for all five leaves
- preserve relation and evidence metadata
- move checks, examples, and notes with each bundle
- extend route-card wording only as much as `execution/agent-workflows-core`
  needs
- add a root legacy receipt
- repair authored links and rebuild generated surfaces

## Stop Lines

- Do not move files from this review pack alone.
- Do not add `tree_path`, `family`, capability, substrate,
  execution-profile, or risk frontmatter.
- Do not change `domain`, `kind`, ID, status, maturity, evidence, or relation
  metadata.
- Do not remap `AOA-T-0028` from `guardrail` to `workflow`; the confirmation
  seam remains the reusable object.
- Do not treat `agent-workflows-core` as generic agent doctrine, shell policy,
  product policy, approval policy, autonomous orchestration, hidden agent
  scheduling, runtime lifecycle law, broad methodology doctrine, or a reason to
  move all remaining `agent-workflows` leaves.
- Do not move `runtime-truth-lifecycle`, tool-use, continuity, governance,
  proof, owner-truth, review-evidence, automation-governance, or neighboring
  shelves in the same wave.
- Keep generated projection weaker than authored bundle meaning.

## Next Honest Move

Run the eighteenth migration pilot.

Use `git mv` to move exactly `AOA-T-0001`, `AOA-T-0014`, `AOA-T-0023`,
`AOA-T-0028`, and `AOA-T-0031` into
`techniques/execution/agent-workflows-core/`; preserve frontmatter; carry all
support files; repair authored links; add root legacy receipt accounting;
update route, roadmap, changelog, landing-log, and tree-contract surfaces;
rebuild generated outputs; validate; commit, push, wait for PR checks, and
merge.
