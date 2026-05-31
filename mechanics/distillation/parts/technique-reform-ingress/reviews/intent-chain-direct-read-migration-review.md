# Intent-Chain Direct-Read Migration Review

Source packet:
[Technique Reform Ingress](../README.md)

Previous landed review:
[Landed Ready-Work-Graphs Pilot Review](landed-ready-work-graphs-pilot-review.md)

Generated lens:
[Technique Tree Projection](../reports/technique_tree_projection.md)

Tree contract:
[Technique Tree Contract](../../../../../docs/TECHNIQUE_TREE_CONTRACT.md)

Status: accepted-for-seventeenth-migration-pilot, not path migration, not
`tree_path` frontmatter.

## Verdict

Accept `execution/intent-chain` as the seventeenth bounded migration pilot.

Move exactly `AOA-T-0004` and `AOA-T-0005` in the next migration step, if and
only if the move preserves IDs, `domain`, `kind`, status, relations, evidence,
support files, and public-safety posture. This review does not move files.

The shelf is coherent because the two leaves form one portable execution
neighborhood:

- `AOA-T-0004` owns the base artifact-first chain: intent normalization,
  plan artifact, dry-run execution artifacts, and machine-readable
  contract-check before any real action path is trusted.
- `AOA-T-0005` owns one bounded extension of that chain: add one new
  `intent_type` through fixture, smoke, strict contract-check, published
  review surface, and regression proof.

This acceptance does not make `intent-chain` router ownership, API contract
authority, runtime dispatch, real-action permission, automation governance, CI
policy, or broad rollout doctrine. It stays a technique shelf for preparing
and checking an intent-shaped execution chain before live action.

## Sources Read

- [AOA-T-0004 intent-plan-dry-run-contract-chain](../../../../../techniques/execution/intent-chain/intent-plan-dry-run-contract-chain/TECHNIQUE.md)
- [AOA-T-0004 checklist](../../../../../techniques/execution/intent-chain/intent-plan-dry-run-contract-chain/checks/chain-contract-checklist.md)
- [AOA-T-0004 examples](../../../../../techniques/execution/intent-chain/intent-plan-dry-run-contract-chain/examples/minimal-intent-chain.md)
  and
  [concrete example](../../../../../techniques/execution/intent-chain/intent-plan-dry-run-contract-chain/examples/concrete-non-ui-intent-chain.md)
- AOA-T-0004 support notes:
  [bounded transfer](../../../../../techniques/execution/intent-chain/intent-plan-dry-run-contract-chain/notes/bounded-transfer.md),
  [origin evidence](../../../../../techniques/execution/intent-chain/intent-plan-dry-run-contract-chain/notes/origin-evidence.md),
  [second context](../../../../../techniques/execution/intent-chain/intent-plan-dry-run-contract-chain/notes/second-context-adaptation.md),
  [canonical readiness](../../../../../techniques/execution/intent-chain/intent-plan-dry-run-contract-chain/notes/canonical-readiness.md),
  and
  [adverse effects](../../../../../techniques/execution/intent-chain/intent-plan-dry-run-contract-chain/notes/adverse-effects-review.md)
- [AOA-T-0005 new-intent-rollout-checklist](../../../../../techniques/execution/intent-chain/new-intent-rollout-checklist/TECHNIQUE.md)
- [AOA-T-0005 checklist](../../../../../techniques/execution/intent-chain/new-intent-rollout-checklist/checks/intent-rollout-checklist.md)
- [AOA-T-0005 examples](../../../../../techniques/execution/intent-chain/new-intent-rollout-checklist/examples/minimal-intent-rollout.md)
  and
  [concrete example](../../../../../techniques/execution/intent-chain/new-intent-rollout-checklist/examples/concrete-non-ui-intent-rollout.md)
- AOA-T-0005 support notes:
  [rollout-failure triage](../../../../../techniques/execution/intent-chain/new-intent-rollout-checklist/notes/rollout-failure-triage.md),
  [origin evidence](../../../../../techniques/execution/intent-chain/new-intent-rollout-checklist/notes/origin-evidence.md),
  [second context](../../../../../techniques/execution/intent-chain/new-intent-rollout-checklist/notes/second-context-adaptation.md),
  and
  [canonical readiness](../../../../../techniques/execution/intent-chain/new-intent-rollout-checklist/notes/canonical-readiness.md)
- [Agent-workflows route card](../../../../../techniques/agent-workflows/AGENTS.md)
- [Execution route card](../../../../../techniques/execution/AGENTS.md)
- [Intent-chain semantic review](../../../../../mechanics/distillation/parts/technique-reform-ingress/reviews/semantic/INTENT_CHAIN_SEMANTIC_REVIEW.md)
- [Agent-workflows core semantic review](../../../../../mechanics/distillation/parts/technique-reform-ingress/reviews/semantic/AGENT_WORKFLOWS_CORE_SEMANTIC_REVIEW.md)
- [AOA-T-0005 kind remap decision](../../../../../docs/decisions/AOA-TECH-D-0036-0005-kind-remap.md)
- [First family shelf review pack](first-family-shelf-review-pack.md)
- [Technique family scout rows for `intent-chain`](../reports/technique_family_scout.md)
- [Technique topology scout rows for `intent-chain`](../reports/technique_topology_scout.md)
- [Technique tree projection rows for `intent-chain`](../reports/technique_tree_projection.md)

## Direct Bundle Read

| technique | current posture | shelf read |
|---|---|---|
| `AOA-T-0004` | `domain: agent-workflows`, `kind: workflow`, `status: canonical`, `validation_strength: cross_context` | base intent-chain contract; artifact-first normalization and dry-run contract-check before real execution |
| `AOA-T-0005` | `domain: agent-workflows`, `kind: workflow`, `status: promoted`, `validation_strength: source_backed` | extension checklist for one new intent type on an already existing chain |

The relation spine is already correct:

- `AOA-T-0004` is `used_together_for` `AOA-T-0005`.
- `AOA-T-0005` `requires` `AOA-T-0004`.
- both complement `AOA-T-0001` without replacing the general
  plan/diff/verify/report backbone.

The support files keep the same division. `AOA-T-0004` centers the invariant
artifact chain and contract verdict. `AOA-T-0005` centers fixture, smoke,
contract-check, artifact publishing, and regression coverage for one new
intent. That is enough for one shelf because the browsing question is shared:
how an intent-shaped execution path becomes reviewable before live action.

## Why The Earlier Small-Shelf Hold No Longer Blocks

The first family shelf review called `intent-chain` coherent but too small to
pilot alone. That was correct before the execution trunk had a landed shelf.

It no longer blocks this step because `ready-work-graphs` is already landed and
reviewed as the first execution trunk shelf. `intent-chain` is now the second
small execution shelf, not the lone proof that the whole execution trunk works.
That makes the pair useful as a compact path migration while still keeping
`agent-workflows-core` and `runtime-truth-lifecycle` out of the wave.

## Execution Trunk Fit

The shelf belongs under `execution` because it answers how bounded work becomes
prepared, checked, and stopped before action. It does not define runtime
ownership or action permission.

Fit signals:

- stable generated projection: `execution` trunk, `intent-chain` shelf,
  `candidate` review status
- direct relation: rollout checklist requires the base chain
- support-file alignment: both bundles are artifact-first and review-surface
  oriented
- route-card alignment: execution can store bounded work that is prepared,
  sequenced, attempted, checked, or closed without becoming hidden
  orchestration

Watch signals:

- `AOA-T-0004` can drift into generic dry-run policy if artifacts and contract
  verdict stop being central.
- `AOA-T-0005` can drift into broad rollout or CI governance if one-new-intent
  scope is lost.
- `AOA-T-0005` remains `promoted`, not canonical; the path move must not imply
  promotion.
- The pair is action-contract-heavy enough that migration should preserve
  router, API, runtime, real-action, CI, and automation-governance stop lines
  explicitly.

## Proposed Move

Move exactly these two bundles in the next step:

| technique | current path | proposed path |
|---|---|---|
| `AOA-T-0004` | `techniques/agent-workflows/intent-plan-dry-run-contract-chain/` | `techniques/execution/intent-chain/intent-plan-dry-run-contract-chain/` |
| `AOA-T-0005` | `techniques/agent-workflows/new-intent-rollout-checklist/` | `techniques/execution/intent-chain/new-intent-rollout-checklist/` |

Migration requirements:

- preserve `domain: agent-workflows`
- preserve `kind: workflow`
- preserve `AOA-T-0004` canonical status and `AOA-T-0005` promoted status
- preserve relation and evidence metadata
- move checks, examples, and notes with each bundle
- add or update route-card wording only as much as `execution/intent-chain`
  needs
- add a root legacy receipt
- repair authored links and rebuild generated surfaces

## Stop Lines

- Do not move files from this review pack alone.
- Do not add `tree_path`, `family`, capability, substrate,
  execution-profile, or risk frontmatter.
- Do not change `domain`, `kind`, ID, status, maturity, evidence, or relation
  metadata.
- Do not promote `AOA-T-0005` to canonical through path movement.
- Do not treat `intent-chain` as router ownership, API contract authority,
  runtime dispatch, real-action permission, automation governance, CI policy,
  broad rollout doctrine, or proof that real execution is safe.
- Do not move `agent-workflows-core`, `runtime-truth-lifecycle`,
  `automation-governance`, `review-evidence`, `owner-truth-closeout`, tool-use,
  or neighboring execution shelves in the same wave.
- Keep generated projection weaker than authored bundle meaning.

## Next Honest Move

Run the seventeenth migration pilot.

Use `git mv` to move exactly `AOA-T-0004` and `AOA-T-0005` into
`techniques/execution/intent-chain/`; preserve frontmatter; carry all support
files; repair authored links; add root legacy receipt accounting; update
route, roadmap, changelog, landing-log, and tree-contract surfaces; rebuild
generated outputs; validate; commit, push, wait for PR checks, and merge.
