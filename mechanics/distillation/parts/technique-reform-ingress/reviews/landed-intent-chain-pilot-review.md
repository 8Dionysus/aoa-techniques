# Landed Intent-Chain Pilot Review

Source packet:
[Technique Reform Ingress](../README.md)

Migration review:
[Intent-Chain Direct-Read Migration Review](intent-chain-direct-read-migration-review.md)

Migration receipt:
[Intent-Chain Tree Pilot Receipt](https://github.com/8Dionysus/aoa-techniques/blob/feffba63dc22fd921512ba5a3ff1b5d78606f93b/legacy/receipts/2026-05-05-intent-chain-tree-pilot.md)

Generated lens:
[Technique Tree Projection](../reports/technique_tree_projection.md)

Tree contract:
[Technique Tree Contract](../../../../../docs/TECHNIQUE_TREE_CONTRACT.md)

Status: pilot-validated, choose `execution/agent-workflows-core` for
direct-read migration review, not path migration, not `tree_path` frontmatter.

## Verdict

Accept the landed `intent-chain` pilot as a successful seventeenth tree
migration and the second successful shelf under the `execution` trunk.

The shelf stayed compact after landing. `AOA-T-0004` and `AOA-T-0005` now sit
under one execution-facing neighborhood while IDs, `domain`, `kind`, status,
evidence, notes, examples, checks, relations, maturity, validation-strength
metadata, and public-safety posture stayed unchanged. The migration made the
intent-chain pair easier to find without turning dry-run evidence into real
action permission, router ownership, API contract authority, runtime dispatch,
automation governance, CI policy, broad rollout doctrine, or proof that real
execution is safe.

This review does not move another shelf. It confirms that the next honest tree
slice should run a direct-read review for `execution/agent-workflows-core`.
That review must read the current projected five-leaf shelf directly before
any path movement, because the old semantic review centered only part of the
now-projected shelf and `AOA-T-0004` has already landed under `intent-chain`.

## Sources Read

- [AOA-T-0004 intent-plan-dry-run-contract-chain](../../../../../techniques/execution/intent-chain/intent-plan-dry-run-contract-chain/TECHNIQUE.md)
- [AOA-T-0005 new-intent-rollout-checklist](../../../../../techniques/execution/intent-chain/new-intent-rollout-checklist/TECHNIQUE.md)
- [Execution route card](../../../../../techniques/execution/AGENTS.md)
- [Agent-workflows route card](../../../../../techniques/agent-workflows/AGENTS.md)
- [Intent-chain tree pilot receipt](https://github.com/8Dionysus/aoa-techniques/blob/feffba63dc22fd921512ba5a3ff1b5d78606f93b/legacy/receipts/2026-05-05-intent-chain-tree-pilot.md)
- [Intent-chain direct-read migration review](intent-chain-direct-read-migration-review.md)
- [Intent-chain semantic review](../../../../../mechanics/distillation/parts/technique-reform-ingress/reviews/semantic/INTENT_CHAIN_SEMANTIC_REVIEW.md)
- [Agent-workflows core semantic review](../../../../../mechanics/distillation/parts/technique-reform-ingress/reviews/semantic/AGENT_WORKFLOWS_CORE_SEMANTIC_REVIEW.md)
- [Technique family scout rows for `agent-workflows-core` and `intent-chain`](../reports/technique_family_scout.md)
- [Technique topology scout rows for `agent-workflows-core`](../reports/technique_topology_scout.md)
- [Technique tree projection rows for `agent-workflows-core`](../reports/technique_tree_projection.md)
- [AOA-T-0001 plan-diff-apply-verify-report](../../../../../techniques/execution/agent-workflows-core/plan-diff-apply-verify-report/TECHNIQUE.md)
- [AOA-T-0014 tdd-slice](../../../../../techniques/execution/agent-workflows-core/tdd-slice/TECHNIQUE.md)
- [AOA-T-0023 stateless-single-shot-agent](../../../../../techniques/execution/agent-workflows-core/stateless-single-shot-agent/TECHNIQUE.md)
- [AOA-T-0028 confirmation-gated-mutating-action](../../../../../techniques/execution/agent-workflows-core/confirmation-gated-mutating-action/TECHNIQUE.md)
- [AOA-T-0031 shell-composable-agent-invocation](../../../../../techniques/execution/agent-workflows-core/shell-composable-agent-invocation/TECHNIQUE.md)
- the release lane result recorded in the migration receipt

## Landed Shape Read

| check | result | reading |
|---|---|---|
| current path | `techniques/execution/intent-chain/` | the active path now matches the projected `execution` trunk and `intent-chain` shelf |
| frontmatter truth | unchanged | both leaves remain `domain: agent-workflows` and `kind: workflow`; `AOA-T-0005` remains `promoted` |
| route card | present | `techniques/execution/AGENTS.md` names the second shelf while keeping execution as a tree trunk, not a frontmatter domain |
| root legacy | receipt only | active bundles moved directly between authored homes; `legacy/` preserves accounting |
| generated surfaces | rebuilt | catalogs, capsules, manifests, reports, source-owned KAG exports, and reader surfaces point at current paths |
| link repair | complete enough for this stage | semantic reviews, audit evidence surfaces, active review sources, root docs, and generated readers route to current authored paths; old paths remain only in receipts, legacy raw records, tests, and migration accounting |
| validation | green | release check covered unit tests, nested AGENTS coverage, repository parity, generated parity, tree projection parity, and source-owned KAG export parity |

## What The Seventeenth Pilot Proved

- `execution/` can hold a second small shelf without collapsing into generic
  workflow doctrine.
- The path tree can expose an action-contract-heavy pair while still keeping
  real-action permission and runtime dispatch outside `aoa-techniques`.
- `AOA-T-0005` can stay promoted after path migration; location under
  `execution/` is not status promotion.
- The relation spine stayed useful: `AOA-T-0005` still requires `AOA-T-0004`,
  and both remain adjacent to `AOA-T-0001` without replacing the broader
  plan/diff/verify/report backbone.
- The old small-shelf concern is resolved for `intent-chain`: it is now the
  second execution precedent after `ready-work-graphs`, not the lone proof that
  the trunk works.

## Remaining Weaknesses

- `AOA-T-0004` can still drift into generic dry-run policy if normalized
  artifacts and contract verdicts stop being central.
- `AOA-T-0005` can drift into broad rollout governance or CI policy if the
  one-new-intent scope gets widened.
- The shelf is action-contract-heavy enough that future examples must keep
  dry-run evidence distinct from real execution safety.
- `agent-workflows-core` remains broader than the two previous execution
  shelves and cannot be migrated by adjacency.
- `runtime-truth-lifecycle` still carries runtime and host authority pressure
  and should not inherit intent-chain dry-run language.

## Eighteenth Shelf Choice

Choose `execution/agent-workflows-core` for the next direct-read migration
review.

Projected shelf:

| technique | current path | proposed path |
|---|---|---|
| `AOA-T-0001` | `techniques/agent-workflows/plan-diff-apply-verify-report/` | `techniques/execution/agent-workflows-core/plan-diff-apply-verify-report/` |
| `AOA-T-0014` | `techniques/agent-workflows/tdd-slice/` | `techniques/execution/agent-workflows-core/tdd-slice/` |
| `AOA-T-0023` | `techniques/agent-workflows/stateless-single-shot-agent/` | `techniques/execution/agent-workflows-core/stateless-single-shot-agent/` |
| `AOA-T-0028` | `techniques/agent-workflows/confirmation-gated-mutating-action/` | `techniques/execution/agent-workflows-core/confirmation-gated-mutating-action/` |
| `AOA-T-0031` | `techniques/agent-workflows/shell-composable-agent-invocation/` | `techniques/execution/agent-workflows-core/shell-composable-agent-invocation/` |

Reason:

`agent-workflows-core` is now the most useful execution candidate because two
smaller execution shelves have landed and the projected core is fully
canonical. It covers the reusable work backbone, bounded test slice, shell
single-shot posture, explicit confirmation seam, and shell composability.
Together those leaves describe how agent work is planned, bounded, confirmed,
invoked, and kept from becoming a hidden autonomous loop.

Why direct-read first:

This shelf is wider and more mixed than the last two execution shelves. It
contains `workflow`, `guardrail`, and `composition` leaves; two leaves have
mutating execution profiles; and the older `AGENT_WORKFLOWS_CORE_SEMANTIC_REVIEW`
does not cover the current five-leaf projection. The next review must decide
whether all five belong together or whether the shell-facing cluster should
split before any migration.

Why not the neighboring shelves first:

`runtime-truth-lifecycle` carries runtime, host, lifecycle, service, and
benchmark authority pressure and remains a boundary-watch shelf. `tool-use`
has only one singleton hold. `donor-harvest`, `decision-routing`,
`automation-governance`, `review-evidence`, and `owner-truth-closeout` still
route through continuity, governance, proof, or owner-acceptance pressure
rather than the execution core.

## Stop Lines

- Do not move `execution/agent-workflows-core` from this review alone.
- Do not add `tree_path`, `family`, capability, substrate, execution-profile,
  or risk frontmatter.
- Do not change `domain`, `kind`, ID, status, maturity, evidence, or relation
  metadata.
- Do not treat `agent-workflows-core` as autonomous orchestration, hidden
  agent scheduling, runtime lifecycle law, shell doctrine, product policy,
  approval policy, or broad methodology doctrine.
- Do not move `runtime-truth-lifecycle`, tool-use, continuity, governance,
  proof, owner-truth, review-evidence, automation-governance, or neighboring
  shelves in the same wave.
- Keep generated projection weaker than authored bundle meaning.

## Next Honest Move

Run a direct-read migration review for `execution/agent-workflows-core`.

Read `AOA-T-0001`, `AOA-T-0014`, `AOA-T-0023`, `AOA-T-0028`, and `AOA-T-0031`
directly; inspect their support files, relations, current `agent-workflows`
route card, projection rows, family scout, topology scout, execution route
card, and small-agent selection pressure; decide whether the five leaves
belong together under `techniques/execution/agent-workflows-core/` or need a
pre-migration split; preserve workflow backbone, bounded slice, single-shot,
confirmation, shell-composition, runtime, approval, and hidden-orchestration
stop lines; and do not move any files until that review lands.
