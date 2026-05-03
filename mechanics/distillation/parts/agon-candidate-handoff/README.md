# Agon Candidate Handoff

This part maps Agon requested-only practice pressure into Distillation lanes
before any technique bundle is drafted.

Use it when the question is:

- which Agon candidate can survive as one portable practice move;
- which candidate still depends on Agon source vocabulary, state, or owner law;
- which candidate must route to a stronger owner before `aoa-techniques` can
  honestly extract a technique.

It is a handoff and narrowing surface. It does not promote Agon candidates,
create technique bundles, accept an AoA owner request, or import Agon law into
portable technique canon.

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

## Structured Registry

- [config/agon_candidate_handoff.seed.json](config/agon_candidate_handoff.seed.json)
  carries the complete handoff lane map.
- [generated/agon_candidate_handoff.min.json](generated/agon_candidate_handoff.min.json)
  is derived evidence for counts, source coverage, and first-narrowing watch.
- [schemas/](schemas/) and [examples/](examples/) document the expected shape.
- [scripts/build_agon_candidate_handoff.py](scripts/build_agon_candidate_handoff.py)
  builds the derived index and verifies every entry still exists in the Agon
  source registries.
- [scripts/validate_agon_candidate_handoff.py](scripts/validate_agon_candidate_handoff.py)
  runs the source-coverage validator.

Validation:

```bash
python mechanics/distillation/parts/agon-candidate-handoff/scripts/build_agon_candidate_handoff.py --check
python mechanics/distillation/parts/agon-candidate-handoff/scripts/validate_agon_candidate_handoff.py
python -m pytest -q mechanics/distillation/parts/agon-candidate-handoff/tests/test_agon_candidate_handoff.py
```

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

## Stop Line

This part must not define Agon law, create skill workflows, issue proof
verdicts, write scars, mutate rank or trust, start arena runtime, promote KAG,
write ToS canon, or turn requested candidates into promoted techniques.
