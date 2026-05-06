# Landed Approval-Evidence Pilot Review

Source packet:
[Technique Reform Ingress](../README.md)

Migration review:
[Approval-Evidence Direct-Read Migration Review](approval-evidence-direct-read-migration-review.md)

Migration receipt:
[Approval-Evidence Tree Pilot Receipt](../../../../../legacy/receipts/2026-05-05-approval-evidence-tree-pilot.md)

Generated lens:
[Technique Tree Projection](../../../../../reports/technique_tree_projection.md)

Tree contract:
[Technique Tree Contract](../../../../../docs/TECHNIQUE_TREE_CONTRACT.md)

Status: pilot-validated, choose `proof/review-evidence` for direct-read
migration review, not path migration, not `tree_path` frontmatter.

## Verdict

Accept the landed `approval-evidence` pilot as a successful twenty-first tree
migration and the second successful shelf under the `governance` trunk.

The shelf stayed coherent after landing. The two leaves now sit under one
governance neighborhood where the common object is approval-shaped boundary
evidence before mutation or continuation: one fail-closed execution verdict
gate and one durable approval seam. IDs, `domain`, `kind`, status, evidence,
notes, examples, checks, relations, maturity, validation-strength metadata, and
public-safety posture stayed unchanged.

This review does not move another shelf. It confirms that the next honest tree
slice should run a direct-read review for `proof/review-evidence`.

## Sources Read

- [AOA-T-0068 fail-closed-evidence-gate](../../../../../techniques/governance/approval-evidence/fail-closed-evidence-gate/TECHNIQUE.md)
- [AOA-T-0068 checklist](../../../../../techniques/governance/approval-evidence/fail-closed-evidence-gate/checks/fail-closed-evidence-gate-checklist.md)
- [AOA-T-0068 canonical readiness](../../../../../techniques/governance/approval-evidence/fail-closed-evidence-gate/notes/canonical-readiness.md)
- [AOA-T-0069 approval-bound-durable-jobs](../../../../../techniques/governance/approval-evidence/approval-bound-durable-jobs/TECHNIQUE.md)
- [AOA-T-0069 checklist](../../../../../techniques/governance/approval-evidence/approval-bound-durable-jobs/checks/approval-bound-durable-jobs-checklist.md)
- [AOA-T-0069 canonical readiness](../../../../../techniques/governance/approval-evidence/approval-bound-durable-jobs/notes/canonical-readiness.md)
- [Governance route card](../../../../../techniques/governance/AGENTS.md)
- [Approval-evidence tree pilot receipt](../../../../../legacy/receipts/2026-05-05-approval-evidence-tree-pilot.md)
- [Approval-evidence direct-read migration review](approval-evidence-direct-read-migration-review.md)
- [Technique family scout rows for `approval-evidence` and `review-evidence`](../../../../../reports/technique_family_scout.md)
- [Technique topology scout rows for `approval-evidence` and `review-evidence`](../../../../../reports/technique_topology_scout.md)
- [Technique tree projection rows for `approval-evidence` and `review-evidence`](../../../../../reports/technique_tree_projection.md)
- [AOA-T-0105 single-missing-evidence-request](../../../../../techniques/agent-workflows/single-missing-evidence-request/TECHNIQUE.md)
- [AOA-T-0105 canonical readiness](../../../../../techniques/agent-workflows/single-missing-evidence-request/notes/canonical-readiness.md)
- [AOA-T-0107 single-locus-claim-challenge](../../../../../techniques/agent-workflows/single-locus-claim-challenge/TECHNIQUE.md)
- [AOA-T-0107 canonical readiness](../../../../../techniques/agent-workflows/single-locus-claim-challenge/notes/canonical-readiness.md)
- [AOA-T-0106 single-scoped-evidence-reference](../../../../../techniques/docs/single-scoped-evidence-reference/TECHNIQUE.md)
- [AOA-T-0106 canonical readiness](../../../../../techniques/docs/single-scoped-evidence-reference/notes/canonical-readiness.md)
- [Proof route card](../../../../../techniques/proof/AGENTS.md)
- [Docs route card](../../../../../techniques/docs/AGENTS.md)

## Landed Shape Read

| check | result | reading |
|---|---|---|
| current path | `techniques/governance/approval-evidence/` | the active path now matches the projected `governance` trunk and `approval-evidence` shelf |
| frontmatter truth | unchanged | `AOA-T-0068` remains `domain: agent-workflows`, `kind: guardrail`, `status: promoted`; `AOA-T-0069` remains `domain: agent-workflows`, `kind: handoff`, `status: promoted` |
| route card | present | `techniques/governance/AGENTS.md` names `approval-evidence/` while keeping governance as a tree trunk, not a frontmatter domain |
| root legacy | receipt only | active bundles moved directly between authored homes; `legacy/` preserves path accounting |
| generated surfaces | rebuilt | catalogs, capsules, manifests, reports, source-owned KAG exports, and reader surfaces point at current paths |
| link repair | complete enough for this stage | active mechanics surfaces, incoming public donor notes, review packets, and generated readers route to current authored paths; old paths remain only in receipts, tests, and migration accounting |
| validation | green | release check covered unit tests, nested AGENTS coverage, repository parity, generated parity, tree projection parity, and source-owned KAG export parity |

## What The Twenty-First Pilot Proved

- `governance/` can hold approval-shaped boundary evidence without becoming
  approval policy, security framework authority, runtime job-runner ownership,
  scheduler doctrine, queue ownership, or broad orchestration governance.
- The shelf improves browsing because immediate fail-closed execution gates and
  longer-running durable approval seams are now neighbors instead of isolated
  broad `agent-workflows` leaves.
- Path placement can preserve `domain: agent-workflows`, distinct `kind`
  values, promoted status, support files, and canonical readiness holds.
- The shelf gives small agents a compact local route: block mutation unless
  allow is explicit, or hold longer-running work at a visible durable approval
  seam.
- Generated projection rows converged on current paths after migration without
  becoming `tree_path` frontmatter truth.

## Remaining Weaknesses

- `AOA-T-0068` can still become policy-engine or security-constitution
  doctrine if the one bounded fail-closed execution seam weakens.
- `AOA-T-0069` can still become scheduler, queue, or orchestration-platform
  doctrine if durable job identity absorbs broad background-work semantics.
- The two leaves can still collapse into one vague approval pattern if
  immediate boundary verdicts and durable pause/resume semantics are not kept
  distinct.
- The governance trunk has two landed shelves now, but future governance
  shelves must still earn their own direct-read review rather than inheriting
  decision-routing or approval-evidence acceptance.
- Both leaves remain promoted rather than canonical; their readiness notes
  still ask for another independent downstream context before default-use
  promotion.
- Future relation work should improve cross-shelf browsing without adding
  `tree_path`, `family`, capability, substrate, execution-profile, or risk
  frontmatter.

## Twenty-Second Shelf Choice

Choose `proof/review-evidence` for the next direct-read migration review.

Projected shelf:

| technique | current path | proposed path |
|---|---|---|
| `AOA-T-0105` | `techniques/agent-workflows/single-missing-evidence-request/` | `techniques/proof/review-evidence/single-missing-evidence-request/` |
| `AOA-T-0107` | `techniques/agent-workflows/single-locus-claim-challenge/` | `techniques/proof/review-evidence/single-locus-claim-challenge/` |
| `AOA-T-0106` | `techniques/docs/single-scoped-evidence-reference/` | `techniques/proof/review-evidence/single-scoped-evidence-reference/` |

Reason:

`review-evidence` is the next clean proof-facing shelf after the two governance
shelves. It gathers one request for a missing evidence object, one pressure
move against a vulnerable claim locus, and one scoped reference artifact around
the proof-trunk question of how review state gets evidence support without
becoming proof verdict authority.

Why direct-read first:

The three leaves are promoted rather than canonical, span `agent-workflows` and
`docs`, and were extracted from Distillation Agon handoff gates. The review must
verify whether they form one review-evidence shelf without importing Agon move
law, proof verdict authority, eval adequacy checks, review-board workflow,
route mutation, memory writes, runtime behavior, KAG promotion, ToS canon, or
skill activation.

Why not neighboring shelves first:

`runtime-truth-lifecycle`, `owner-truth-closeout`, `automation-governance`,
and `tool-gateway` carry heavier runtime, owner, split, governance, or
singleton pressure. `review-evidence` is the smaller next proof test because it
has exactly three promoted leaves, a clear projection, and an explicit
boundary-watch posture.

## Stop Lines

- Do not move `proof/review-evidence` from this review alone.
- Do not add `tree_path`, `family`, capability, substrate, execution-profile,
  or risk frontmatter.
- Do not change `domain`, `kind`, ID, status, maturity, evidence, or relation
  metadata.
- Do not treat `approval-evidence` as approval policy, security framework
  authority, runtime job-runner ownership, scheduler doctrine, queue ownership,
  trust-platform semantics, or broad orchestration governance.
- Do not treat `review-evidence` as proof verdict authority, eval-suite
  ownership, review-board workflow, Agon move law, actor eligibility,
  route mutation, memory write, runtime behavior, KAG promotion, ToS canon, or
  skill activation.
- Keep generated projection weaker than authored bundle meaning.

## Next Honest Move

Run a direct-read migration review for `proof/review-evidence`.

Read `AOA-T-0105`, `AOA-T-0107`, and `AOA-T-0106` directly, including their
support files, origin evidence, canonical readiness notes, relation edges, and
current `agent-workflows`, `docs`, and `proof` route context, before any
twenty-second shelf movement.
