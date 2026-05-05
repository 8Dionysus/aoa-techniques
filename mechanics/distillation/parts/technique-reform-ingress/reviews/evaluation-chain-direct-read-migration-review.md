# Evaluation-Chain Direct-Read Migration Review

Source packet:
[Technique Reform Ingress](../README.md)

Preceding landed review:
[Landed Skill-Support Pilot Review](landed-skill-support-pilot-review.md)

Generated lens:
[Technique Tree Projection](../../../../../reports/technique_tree_projection.md)

Tree contract:
[Technique Tree Contract](../../../../../docs/TECHNIQUE_TREE_CONTRACT.md)

Status: accepted-for-twelfth-migration-pilot, not path migration, not
`tree_path` frontmatter.

## Verdict

Accept `evaluation-chain` as the twelfth bounded tree migration pilot.

Direct reading confirms that `AOA-T-0003`, `AOA-T-0007`, and `AOA-T-0032`
form one proof-facing evaluation shelf. The shelf gives agents a narrow chain:
produce one machine-readable validation contract, promote one observed signal
through an explicit staged gate only after the summary contract is stable, and
emit one read-only CI report that makes context-composition coverage and drift
visible without becoming the composition or remediation engine.

The shelf is stronger than `skill-support`, so its path must stay humble.
`evaluation-chain` is not CI ownership, release policy, eval-suite authority,
proof verdict law, mandatory testing doctrine, or generic quality gate
doctrine. `AOA-T-0003` remains a validation summary producer, `AOA-T-0007`
remains a staged guardrail for one narrow promotion surface, and `AOA-T-0032`
remains a CI-facing read-only context report. The future path would only make
that chain easier to browse under `techniques/proof/evaluation-chain/` while
keeping `domain`, `kind`, status, IDs, evidence, relations, examples, checks,
and public-safety posture unchanged.

This review does not move files. It only authorizes a later migration wave to
move exactly these three bundles into `techniques/proof/evaluation-chain/` if
that wave also updates route cards, root legacy receipts, authored links,
generated surfaces, and validation.

## Sources Read

- [AOA-T-0003 contract-first-smoke-summary](../../../../../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md)
- [AOA-T-0003 checklist](../../../../../techniques/evaluation/contract-first-smoke-summary/checks/summary-contract-checklist.md)
- [AOA-T-0003 minimal example](../../../../../techniques/evaluation/contract-first-smoke-summary/examples/minimal-smoke-summary-flow.md)
- [AOA-T-0003 canonical readiness](../../../../../techniques/evaluation/contract-first-smoke-summary/notes/canonical-readiness.md)
- [AOA-T-0003 adverse effects review](../../../../../techniques/evaluation/contract-first-smoke-summary/notes/adverse-effects-review.md)
- [AOA-T-0003 origin evidence](../../../../../techniques/evaluation/contract-first-smoke-summary/notes/origin-evidence.md)
- [AOA-T-0003 second context adaptation](../../../../../techniques/evaluation/contract-first-smoke-summary/notes/second-context-adaptation.md)
- [AOA-T-0007 signal-first-gate-promotion](../../../../../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md)
- [AOA-T-0007 checklist](../../../../../techniques/evaluation/signal-first-gate-promotion/checks/gate-promotion-checklist.md)
- [AOA-T-0007 minimal example](../../../../../techniques/evaluation/signal-first-gate-promotion/examples/minimal-signal-first-rollout.md)
- [AOA-T-0007 concrete example](../../../../../techniques/evaluation/signal-first-gate-promotion/examples/concrete-repo-validation-rollout.md)
- [AOA-T-0007 canonical readiness](../../../../../techniques/evaluation/signal-first-gate-promotion/notes/canonical-readiness.md)
- [AOA-T-0007 adverse effects review](../../../../../techniques/evaluation/signal-first-gate-promotion/notes/adverse-effects-review.md)
- [AOA-T-0007 origin evidence](../../../../../techniques/evaluation/signal-first-gate-promotion/notes/origin-evidence.md)
- [AOA-T-0007 second context adaptation](../../../../../techniques/evaluation/signal-first-gate-promotion/notes/second-context-adaptation.md)
- [AOA-T-0032 context-report-for-ci](../../../../../techniques/evaluation/context-report-for-ci/TECHNIQUE.md)
- [AOA-T-0032 checklist](../../../../../techniques/evaluation/context-report-for-ci/checks/context-report-for-ci-checklist.md)
- [AOA-T-0032 minimal example](../../../../../techniques/evaluation/context-report-for-ci/examples/minimal-context-report-for-ci.md)
- [AOA-T-0032 concrete example](../../../../../techniques/evaluation/context-report-for-ci/examples/concrete-context-composition-ci-report.md)
- [AOA-T-0032 canonical readiness](../../../../../techniques/evaluation/context-report-for-ci/notes/canonical-readiness.md)
- [AOA-T-0032 external import review](../../../../../techniques/evaluation/context-report-for-ci/notes/external-import-review.md)
- [AOA-T-0032 external origin](../../../../../techniques/evaluation/context-report-for-ci/notes/external-origin.md)
- [AOA-T-0032 second context adaptation](../../../../../techniques/evaluation/context-report-for-ci/notes/second-context-adaptation.md)
- [Evaluation route card](../../../../../techniques/evaluation/AGENTS.md)
- [Proof route card](../../../../../techniques/proof/AGENTS.md)
- [Techniques route card](../../../../../techniques/AGENTS.md)
- [Technique family seed row for `evaluation-chain`](../../../../../config/technique_family_seed.yaml)
- [Technique tree projection rows for `evaluation-chain`](../../../../../reports/technique_tree_projection.md)
- [Technique family scout rows for `evaluation-chain`](../../../../../reports/technique_family_scout.md)
- [Technique topology scout rows for `evaluation-chain`](../../../../../reports/technique_topology_scout.md)
- [Landed skill-support pilot review](landed-skill-support-pilot-review.md)

## Direct Bundle Read

| technique | current path | domain | kind | direct-read result |
|---|---|---|---|---|
| `AOA-T-0003` | `techniques/evaluation/contract-first-smoke-summary/` | `evaluation` | `validation` | produces one stable machine-readable smoke or probe summary with explicit status and enough observed fields for diagnosis |
| `AOA-T-0007` | `techniques/evaluation/signal-first-gate-promotion/` | `evaluation` | `guardrail` | stages one observed validation signal from `signal_only` toward one explicitly chosen strict surface while preserving diagnostics |
| `AOA-T-0032` | `techniques/evaluation/context-report-for-ci/` | `evaluation` | `validation` | emits a read-only CI-facing report for context-composition coverage, token drift, and related checks without doing composition or remediation |

The kinds are mixed, and that is the point of this shelf. The browsing
question is not "which validation kind is this?" It is "how does a validation
signal become reviewable, promotable, and visible to CI without silently
becoming policy?"

## Why The Shelf Holds

- `AOA-T-0003` supplies the producer-layer contract: one summary path, one
  explicit status, and enough observed fields that downstream consumers do not
  scrape logs.
- `AOA-T-0007` supplies the cautious promotion move once a summary-producing
  signal exists and the team needs a narrow strict surface rather than broad
  fail-fast drift.
- `AOA-T-0032` supplies the CI-facing context report once context composition
  needs visibility without moving composition, remediation, provider telemetry,
  or runtime monitoring into the report.
- The prerequisites and relations stay honest: `AOA-T-0007` requires
  `AOA-T-0003`, while `AOA-T-0032` complements context-composition work
  without replacing it.
- Two leaves are canonical and one is promoted. That is acceptable for a path
  pilot because the move changes browsing placement only, not status.
- The support files keep the leaves distinct: summary contracts reject log
  scraping, gate promotion rejects hidden broad enforcement, and CI context
  reporting rejects composition-engine or remediation drift.

## Proof Trunk Fit

`proof/` is the better trunk because the shelf shapes evidence that other
systems may read: a machine-readable summary, a staged promotion signal, and a
CI-facing report. These are proof-facing practice moves, even though their
frontmatter remains `domain: evaluation`.

The future shelf name should remain `evaluation-chain`, not `ci-gates` or
`quality-proof`. Direct reading shows a chain of evidence surfaces, not an
owner policy stack. The path should help readers find adjacent validation
contracts without implying that location under `proof/` proves the software or
grants a repository the right to enforce a gate.

## Boundary Watch Accepted

The projection marks `evaluation-chain` as `candidate`, but direct reading
confirms real authority pressure:

- `AOA-T-0003` can drift into downstream storage, history, rollup, or gate
  ownership if the summary contract is treated as the whole proof system.
- `AOA-T-0007` carries the highest risk because it can become release policy,
  hidden governance, or broad irreversible enforcement if strict mode leaks
  beyond the chosen narrow surface.
- `AOA-T-0032` can drift into composition, remediation, provider telemetry,
  or generic observability if the report starts prescribing fixes or acting as
  a hidden engine.

The shelf is accepted because each bundle already names those risks and keeps
its executable move narrow. The later migration must preserve the chain while
leaving owner policy outside the shelf.

## Proposed Move

Move exactly these three bundles in the migration wave:

| technique | current path | proposed path |
|---|---|---|
| `AOA-T-0003` | `techniques/evaluation/contract-first-smoke-summary/` | `techniques/proof/evaluation-chain/contract-first-smoke-summary/` |
| `AOA-T-0007` | `techniques/evaluation/signal-first-gate-promotion/` | `techniques/proof/evaluation-chain/signal-first-gate-promotion/` |
| `AOA-T-0032` | `techniques/evaluation/context-report-for-ci/` | `techniques/proof/evaluation-chain/context-report-for-ci/` |

Keep `domain`, `kind`, status, IDs, evidence, relations, maturity,
validation-strength metadata, and public-safety posture unchanged.

## Migration Blast Radius

A later migration wave should expect to update:

- `techniques/proof/AGENTS.md`, because this would become the second landed
  proof-side trunk shelf and the first stronger evaluation-chain shelf
- `techniques/evaluation/AGENTS.md` where representative bundle lists still
  name the old homes
- root `legacy/receipts/` and `legacy/INDEX.md` accounting for the authored
  path migration
- authored relations and adjacent references from evaluation, instruction,
  CI, summary, context-composition, and proof-adjacent surfaces
- generated catalogs, capsules, manifests, reports, KAG exports, docs readers,
  and source-lift surfaces after the path move
- mechanics review rows and tests that still point to the old homes
- release-check output touched by regenerated indexes and reports

Do not create mechanic-style `parts/` packages or shelf READMEs for these
technique leaves.

## Why Not Neighbor Shelves In This Wave

`published-summary` should wait because it centers on published surface
storage, remediation, integrity, and rendering rather than the validation
signal chain itself.

`review-evidence` should wait because it carries missing-evidence,
claim-challenge, review-state, and release-note pressure that can overclaim
proof authority.

`owner-truth-closeout` should wait because it moves closer to owner-truth law
and closeout verdicts than this evidence-chain shelf needs.

Governance, automation, and runtime shelves should wait because they add
approval, policy, operational, or lifecycle authority pressure that would make
this twelfth pilot too broad.

## Stop Lines

- Do not move files from this review pack alone.
- Do not add `tree_path`, `family`, capability, substrate, execution-profile,
  or risk frontmatter.
- Do not move `published-summary`, `review-evidence`,
  `owner-truth-closeout`, runtime, governance, automation, or other proof-side
  shelves in the same wave.
- Do not treat `evaluation-chain` as CI ownership, release policy, eval-suite
  authority, proof verdict law, mandatory testing doctrine, generic quality
  gate doctrine, or owner acceptance.
- Do not collapse summary-contract generation, staged signal promotion, and CI
  context reporting into one mega-technique.
- Do not promote `AOA-T-0032` to canonical status during path migration.
- Do not make strict enforcement broader merely because the shelf sits under
  `proof/`.
- Keep generated projection weaker than authored bundle meaning.

## Next Honest Move

Run the twelfth pilot migration.

Move exactly `AOA-T-0003`, `AOA-T-0007`, and `AOA-T-0032` into
`techniques/proof/evaluation-chain/`; update the compact proof trunk route
card; preserve a root `legacy/receipts/` migration receipt; repair authored
links; rebuild generated surfaces; and validate with the narrow tree-pilot
tests plus `python scripts/release_check.py`.
