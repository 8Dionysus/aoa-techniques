# Technique Candidate Bridge

This part decides how Experience pressure can move toward atomic technique
bundles without copying AoA-center law into `aoa-techniques`.

Use it when a local Experience part looks reusable, but the next honest step is
still to classify the candidate rather than draft a `techniques/**/TECHNIQUE.md`
bundle immediately.

It does not change technique status. A technique becomes canonical or promoted
only in its own bundle.

## Inputs

- one local Experience part
- the nearest AoA-center Experience part or owner request signal
- the reusable move that might become one technique
- nearest existing technique bundles, if any
- stronger owner routes and stop-lines
- portability note for use outside OS Abyss

## Outputs

- one candidate verdict: `extract_watch`, `narrow_more`, `hold_overlap`,
  `route_to_owner`, or `mechanics_only`
- one nearest existing bundle or owner surface to check first
- one stop-line that prevents authority transfer
- one next review move

## Current Candidate Readout

| Local part | Center pressure | Current verdict | Nearest anchor | Next move |
|---|---|---|---|---|
| `authority-resolution` | Governance Polis and Runtime Boundary both separate capability, authority, and activation. | `extract_watch` | [owner-layer-triage](../../../../techniques/agent-workflows/owner-layer-triage/TECHNIQUE.md), [nearest-wrong-target-rejection](../../../../techniques/agent-workflows/nearest-wrong-target-rejection/TECHNIQUE.md), [recommendation-truth-vs-host-actionability](../../../../techniques/instruction/capability-boundary/recommendation-truth-vs-host-actionability/TECHNIQUE.md) | Test whether a `capability-authority-separation-check` atom is distinct from owner placement and host-actionability checks. |
| `sealed-decision` | Governance Polis names appeals, stays, precedents, and authority resolver language. | `extract_watch` | [decision-rationale-recording](../../../../techniques/instruction/docs-boundary/decision-rationale-recording/TECHNIQUE.md), [fail-closed-evidence-gate](../../../../techniques/agent-workflows/fail-closed-evidence-gate/TECHNIQUE.md) | Test whether a sealed evidence packet is smaller than proof verdicts and broader decision rationale. |
| `governance-precedent` | Governance Polis names decision tables, policy registry routes, appeal or stay routes, and precedent hints. | `narrow_more` | [local-pattern-adoption-gate](../../../../techniques/agent-workflows/local-pattern-adoption-gate/TECHNIQUE.md), [decision-fork-cards](../../../../techniques/agent-workflows/decision-fork-cards/TECHNIQUE.md) | Split precedent capture from local adoption and from appeal handling before drafting. |
| `appeal-reasoning` | Governance Polis names appeal, stay, quarantine, dispute, and overturn pressure. | `narrow_more` | [fail-closed-evidence-gate](../../../../techniques/agent-workflows/fail-closed-evidence-gate/TECHNIQUE.md), [decision-rationale-recording](../../../../techniques/instruction/docs-boundary/decision-rationale-recording/TECHNIQUE.md) | Name one reusable appeal packet, or keep it as governance mechanics. |
| `scope-boundary` | Office Operations, Service Mesh, Release Deployment, and Runtime Boundary all touch live activation stop-lines. | `hold_overlap` | [confirmation-gated-mutating-action](../../../../techniques/execution/agent-workflows-core/confirmation-gated-mutating-action/TECHNIQUE.md), [workspace-root-ingress-and-mutation-gate](../../../../techniques/agent-workflows/workspace-root-ingress-and-mutation-gate/TECHNIQUE.md) | Hold until office, release, and runtime authority are separated from the reusable scope check. |
| `handoff-compression` | Office Operations and Continuity Context both touch role-pair handoff, replay, and re-entry. | `hold_overlap` | [structured-handoff-before-compaction](../../../../techniques/continuity/handoff-continuation/structured-handoff-before-compaction/TECHNIQUE.md), [receipt-confirmed-handoff-packet](../../../../techniques/continuity/handoff-continuation/receipt-confirmed-handoff-packet/TECHNIQUE.md), [git-verified-handoff-claims](../../../../techniques/continuity/handoff-continuation/git-verified-handoff-claims/TECHNIQUE.md) | Hold until the atom is smaller than live office handoff and existing handoff bundles. |
| `service-clarity` | Service Mesh and Release Deployment touch service operation, compatibility, rollout, and runtime owner requests. | `hold_overlap` | [one-command-service-lifecycle](../../../../techniques/agent-workflows/one-command-service-lifecycle/TECHNIQUE.md), [isolated-service-stop-on-shared-substrate](../../../../techniques/recovery/antifragility-recovery/isolated-service-stop-on-shared-substrate/TECHNIQUE.md) | Hold until a portable service-clarity move is separate from service runtime and release choreography. |

## Bridge Rules

- Start from the local part and candidate atom, not from the full center
  mechanic.
- If the candidate cannot name one atomic move, keep it in `narrow_more` or
  `mechanics_only`.
- If the candidate mainly changes runtime, role, release, proof, memory,
  routing, or ToS behavior, use `route_to_owner` or `hold_overlap`.
- If an existing bundle already answers the move, use that bundle instead of
  redrafting Experience doctrine.
- If the move is portable, it must still make sense without OS Abyss offices,
  release trains, runtime services, or owner-request queues.

## Stop-lines

- no live office activation
- no release approval
- no runtime truth or dispatch authority
- no proof verdicts before `aoa-evals`
- no role or handoff authority before `aoa-agents`
- no hidden memory or recall authority before `aoa-memo`
- no Tree-of-Sophia write authority
- no automatic technique promotion

## Strongest Next Thread

The cleanest next Experience extraction candidate is `authority-resolution`.
Its likely atom is a capability-versus-authority check: before an agent acts or
recommends action, name what is technically possible, who is authorized to
decide, and which owner surface can accept or reject the move.

Keep that next pass separate from owner-layer placement. The question is not
"which repository owns this reusable unit?" but "does capability imply
authority here?".
