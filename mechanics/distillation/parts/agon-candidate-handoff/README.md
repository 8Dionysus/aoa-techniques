# Agon Candidate Handoff

This part maps Agon requested-only practice pressure into Distillation lanes
before or beside any technique bundle draft.

Use it when the question is:

- which Agon candidate can survive as one portable practice move;
- which candidate still depends on Agon source vocabulary, state, or owner law;
- which candidate must route to a stronger owner before `aoa-techniques` can
  honestly extract a technique.

It is a handoff and narrowing surface. It does not itself promote Agon
candidates, accept an AoA owner request, or import Agon law into portable
technique canon. When a local bundle lands, this part may point to it as
traceability evidence while keeping the Agon source status unchanged.

## Scope

- accounts for all `12` Wave IV move-binding practice candidates from
  [Agon Move Technique Bridge](../../../agon/parts/move-technique-bridge/README.md)
- accounts for all `10` Wave XV epistemic practice candidates from
  [Agon Epistemic Technique Candidates](../../../agon/parts/epistemic-technique-candidates/README.md)
- keeps the source candidate registries authoritative for requested-only
  status while this part owns only the Distillation lane read

## Lane Summary

| Lane | Count | Meaning |
|---|---:|---|
| `first_narrowing_watch` | `11` | Candidate already names a small practice contour that can receive one atom/topology card before any bundle draft. |
| `source_boundary_hold` | `10` | Candidate still needs Agon source vocabulary, position lifecycle, trace closure, or epistemic context before a portable atom is honest. |
| `owner_route_hold` | `1` | Candidate touches doctrine revision authority and must route stronger-owner evidence before technique extraction. |

No lane means "ready to promote." The strongest lane means "write the next
Distillation gate card and prove the atom is portable."

Current frontier read:

- `3` first-narrowing candidates have complete gate-to-bundle traceability:
  `request_evidence`, `offer_evidence_reference`, and `challenge_claim`.
- `8` first-narrowing candidates remain ungated and are exposed in
  `first_narrowing_frontier` in the generated index.
- [first-narrowing-frontier-review](gates/frontier/first-narrowing-frontier-review.md)
  names the next-gate order and kind-registry watch without promoting any
  candidate.

## Structured Registry

- [config/agon_candidate_handoff.source.json](config/agon_candidate_handoff.source.json)
  carries the complete handoff lane map.
- [generated/agon_candidate_handoff.min.json](generated/agon_candidate_handoff.min.json)
  is derived evidence for counts, source coverage, first-narrowing watch, and
  the remaining ungated frontier.
- [schemas/](schemas/) and [examples/](examples/) document the expected shape.
- [scripts/build_agon_candidate_handoff.py](scripts/build_agon_candidate_handoff.py)
  builds the derived index and verifies every entry still exists in the Agon
  source registries.
- [scripts/validate_agon_candidate_handoff.py](scripts/validate_agon_candidate_handoff.py)
  runs the source-coverage validator.

Validation lane: use [Distillation AGENTS](../../AGENTS.md#validation) for the
exact builder, validator, and test commands.

## Handoff Rule

Agon owns the lawful move or epistemic pressure source. Distillation owns the
narrowing route. `techniques/` owns only the final reusable practice bundle
after the normal atom, topology, evidence, example, checklist, and review path
lands.

## First Narrowing Cluster

Start with small moves that can be described outside live Agon protocol:

- `challenge_claim`
- `request_evidence`
- `offer_evidence_reference`
- `probe_trace`
- `localize_contradiction`
- `deny_closure`
- `inference_chain_attack_practice`
- `explanatory_power_comparison_practice`
- `concept_boundary_probe_practice`
- `counterfactual_pressure_practice`
- `false_consensus_breaking_practice`

For each, the next work is one gate card: atomic move, likely domain, primary
kind, family posture, capability, substrate, execution profile, risk posture,
portable core, AoA-only context, nearest overlaps, proof route, and stop-line.

The current remaining frontier is `probe_trace`, `localize_contradiction`,
`deny_closure`, `inference_chain_attack_practice`,
`explanatory_power_comparison_practice`, `concept_boundary_probe_practice`,
`counterfactual_pressure_practice`, and `false_consensus_breaking_practice`.

## Gate Cards

Gate cards live in [gates](gates/README.md). They are one-candidate checks, not
technique bundles.

Current landed gate:

- [challenge-claim-practice](gates/challenge-claim-practice.md)
- [request-evidence-practice](gates/request-evidence-practice.md)
- [offer-evidence-reference-practice](gates/offer-evidence-reference-practice.md)

Current landed gate example:

- [challenge-claim-minimal-public-safe](gates/examples/challenge-claim-minimal-public-safe.md)
- [request-evidence-minimal-public-safe](gates/examples/request-evidence-minimal-public-safe.md)
- [offer-evidence-reference-minimal-public-safe](gates/examples/offer-evidence-reference-minimal-public-safe.md)

Current landed gate checklist:

- [challenge-claim-gate-checklist](gates/checklists/challenge-claim-gate-checklist.md)
- [request-evidence-gate-checklist](gates/checklists/request-evidence-gate-checklist.md)
- [offer-evidence-reference-gate-checklist](gates/checklists/offer-evidence-reference-gate-checklist.md)

Current landed gate evidence note:

- [challenge-claim-gate-evidence-note](gates/evidence-notes/challenge-claim-gate-evidence-note.md)
- [request-evidence-gate-evidence-note](gates/evidence-notes/request-evidence-gate-evidence-note.md)
- [offer-evidence-reference-gate-evidence-note](gates/evidence-notes/offer-evidence-reference-gate-evidence-note.md)

Current landed bundle readiness review:

- [challenge-claim-bundle-readiness-review](gates/bundle-reviews/challenge-claim-bundle-readiness-review.md)
- [request-evidence-bundle-readiness-review](gates/bundle-reviews/request-evidence-bundle-readiness-review.md)
- [offer-evidence-reference-bundle-readiness-review](gates/bundle-reviews/offer-evidence-reference-bundle-readiness-review.md)

Current landed technique bundle:

- [single-locus-claim-challenge](../../../../techniques/proof/review-evidence/single-locus-claim-challenge/TECHNIQUE.md)
- [single-missing-evidence-request](../../../../techniques/proof/review-evidence/single-missing-evidence-request/TECHNIQUE.md)
- [single-scoped-evidence-reference](../../../../techniques/proof/review-evidence/single-scoped-evidence-reference/TECHNIQUE.md)

## Stop Line

This part must not define Agon law, create skill workflows, issue proof
verdicts, write scars, mutate rank or trust, start arena runtime, promote KAG,
write ToS canon, or by itself turn requested candidates into promoted
techniques.
