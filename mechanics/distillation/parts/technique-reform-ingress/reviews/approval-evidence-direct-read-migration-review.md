# Approval-Evidence Direct-Read Migration Review

Source packet:
[Technique Reform Ingress](../README.md)

Previous landed review:
[Landed Decision-Routing Pilot Review](landed-decision-routing-pilot-review.md)

Generated lens:
[Technique Tree Projection](../reports/technique_tree_projection.md)

Tree contract:
[Technique Tree Contract](../../../../../docs/TECHNIQUE_TREE_CONTRACT.md)

Status: accepted-for-twenty-first-migration-pilot, not path migration, not
`tree_path` frontmatter.

## Verdict

Accept `governance/approval-evidence` as the twenty-first bounded migration
pilot.

The shelf holds after direct reading, but only as approval evidence around
bounded action and continuation. `AOA-T-0068` owns one fail-closed verdict
boundary before mutation and preserves evidence for allowed or blocked paths.
`AOA-T-0069` owns one durable job identity that pauses at an explicit approval
seam and resumes from durable state. Together they form a small governance
neighborhood for approval-shaped evidence without becoming approval law,
security framework authority, or runtime orchestration ownership.

The acceptance is narrow. It does not canonically promote these bundles, does
not change their `domain`, `kind`, status, evidence, relations, maturity, or
public-safety posture, and does not move files from this review pack alone.

## Sources Read

- [AOA-T-0068 fail-closed-evidence-gate](../../../../../techniques/governance/approval-evidence/fail-closed-evidence-gate/TECHNIQUE.md)
- [AOA-T-0068 checklist](../../../../../techniques/governance/approval-evidence/fail-closed-evidence-gate/checks/fail-closed-evidence-gate-checklist.md)
- [AOA-T-0068 example](../../../../../techniques/governance/approval-evidence/fail-closed-evidence-gate/examples/minimal-fail-closed-evidence-gate.md)
- [AOA-T-0068 external origin](../../../../../techniques/governance/approval-evidence/fail-closed-evidence-gate/notes/external-origin.md)
- [AOA-T-0068 external import review](../../../../../techniques/governance/approval-evidence/fail-closed-evidence-gate/notes/external-import-review.md)
- [AOA-T-0068 second context adaptation](../../../../../techniques/governance/approval-evidence/fail-closed-evidence-gate/notes/second-context-adaptation.md)
- [AOA-T-0068 canonical readiness](../../../../../techniques/governance/approval-evidence/fail-closed-evidence-gate/notes/canonical-readiness.md)
- [AOA-T-0069 approval-bound-durable-jobs](../../../../../techniques/governance/approval-evidence/approval-bound-durable-jobs/TECHNIQUE.md)
- [AOA-T-0069 checklist](../../../../../techniques/governance/approval-evidence/approval-bound-durable-jobs/checks/approval-bound-durable-jobs-checklist.md)
- [AOA-T-0069 example](../../../../../techniques/governance/approval-evidence/approval-bound-durable-jobs/examples/minimal-approval-bound-durable-jobs.md)
- [AOA-T-0069 external origin](../../../../../techniques/governance/approval-evidence/approval-bound-durable-jobs/notes/external-origin.md)
- [AOA-T-0069 external import review](../../../../../techniques/governance/approval-evidence/approval-bound-durable-jobs/notes/external-import-review.md)
- [AOA-T-0069 second context adaptation](../../../../../techniques/governance/approval-evidence/approval-bound-durable-jobs/notes/second-context-adaptation.md)
- [AOA-T-0069 canonical readiness](../../../../../techniques/governance/approval-evidence/approval-bound-durable-jobs/notes/canonical-readiness.md)
- [Governance route card](../../../../../techniques/governance/AGENTS.md)
- [Agent-workflows route card](../../../../../techniques/agent-workflows/AGENTS.md)
- [Technique family scout rows for `approval-evidence`](../reports/technique_family_scout.md)
- [Technique topology scout rows for `approval-evidence`](../reports/technique_topology_scout.md)
- [Technique tree projection rows for `approval-evidence`](../reports/technique_tree_projection.md)
- [Landed decision-routing pilot review](landed-decision-routing-pilot-review.md)

## Direct Bundle Read

| technique | current posture | shelf read |
|---|---|---|
| `AOA-T-0068` | `domain: agent-workflows`, `kind: guardrail`, `status: promoted` | blocks a mutating boundary unless an explicit allow verdict exists, while preserving one reviewable evidence artifact for the blocked or allowed path |
| `AOA-T-0069` | `domain: agent-workflows`, `kind: handoff`, `status: promoted` | preserves one longer-running job identity across pause, approval, and resume so continuation waits on explicit approval and durable state rather than hidden memory |

## Why This Shelf Holds

- The common object is explicit approval-shaped evidence around action
  continuation, not generic governance authority.
- The two leaves are distinct but adjacent: `AOA-T-0068` handles one immediate
  fail-closed execution boundary; `AOA-T-0069` handles one longer-running
  durable approval seam.
- Both leaves preserve reviewability while refusing broader policy, scheduler,
  trust-platform, or orchestration semantics.
- Both leaves already carry public-safe external import evidence, examples,
  checklists, and canonical readiness holds.
- The shelf gives small or orchestrated agents a clear boundary-watch
  neighborhood before mutation or continuation.

## Governance Trunk Fit

The projected `governance` trunk should hold techniques where the primary
browsing question is how choices, approvals, control posture, and automation
boundaries stay explicit before action.

`approval-evidence` fits that trunk only as boundary evidence. It does not
define approval policy, security frameworks, trust products, runtime job
runners, schedulers, queue products, or broad orchestration governance. The
path placement should improve tree browsing while preserving `domain:
agent-workflows` and the current `kind` truth for both leaves.

## Watch Signals

- `AOA-T-0068` can drift into a policy engine or security constitution if the
  evidence gate stops being one bounded fail-closed execution seam.
- `AOA-T-0069` can drift into scheduler or queue-platform doctrine if durable
  job identity starts absorbing broad orchestration semantics.
- The two leaves can collapse into one vague approval pattern if immediate
  boundary verdicts and durable pause/resume semantics are not kept distinct.
- Both leaves remain promoted, not canonical; future canonical review still
  needs another independent live adopter beyond the donor family.
- Migration should not turn the current `boundary-watch` projection marker into
  frontmatter truth.

## Proposed Move

| technique | current path | proposed path |
|---|---|---|
| `AOA-T-0068` | `techniques/agent-workflows/fail-closed-evidence-gate/` | `techniques/governance/approval-evidence/fail-closed-evidence-gate/` |
| `AOA-T-0069` | `techniques/agent-workflows/approval-bound-durable-jobs/` | `techniques/governance/approval-evidence/approval-bound-durable-jobs/` |

## Migration Requirements

- Move exactly the two accepted bundles and their support files.
- Keep IDs, `domain`, `kind`, status, maturity, evidence, relations,
  validation-strength metadata, public-safety posture, examples, checks, and
  notes unchanged.
- Update `techniques/governance/AGENTS.md` to name `approval-evidence/` as a
  boundary-evidence shelf without turning it into approval policy, runtime
  ownership, scheduler doctrine, or security framework authority.
- Preserve root legacy accounting in one receipt.
- Repair active authored links that point to the old broad paths.
- Rebuild generated catalogs, capsules, manifests, projection reports, source
  readers, and KAG exports through existing builders.
- Validate with the narrow distillation/root legacy/roadmap tests and the full
  release check before commit.

## Stop Lines

- Do not move files from this review pack alone.
- Do not add `tree_path`, `family`, capability, substrate, execution-profile,
  or risk frontmatter.
- Do not change `domain`, `kind`, ID, status, maturity, evidence, or relation
  metadata.
- Do not promote the two bundles to canonical status.
- Do not treat `approval-evidence` as approval policy, security framework
  authority, trust-platform semantics, runtime job-runner ownership, scheduler
  doctrine, queue-product ownership, or broad orchestration governance.
- Do not collapse immediate fail-closed boundary gates into durable job
  continuation, or durable approval seams into one-shot gate verdicts.
- Do not move `proof/review-evidence`, `execution/runtime-truth-lifecycle`,
  `proof/owner-truth-closeout`, `governance/automation-governance`, or
  `tool-use/tool-gateway` in this pilot.

## Next Honest Move

Run the twenty-first migration pilot.

Move exactly `AOA-T-0068` and `AOA-T-0069` into
`techniques/governance/approval-evidence/` only after path movement,
support-file carry, governance route card update, root legacy receipt, link
repair, generated rebuild, validation, commit, push, PR checks, and merge are
handled together.
