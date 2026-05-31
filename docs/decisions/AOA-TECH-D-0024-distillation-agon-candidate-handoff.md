# Distillation Agon Candidate Handoff

Date: 2026-05-03

## Index Metadata

- Decision ID: AOA-TECH-D-0024
- Original date: 2026-05-03
- Surface classes: mechanic package
- Technique axes: mechanic bridge, source-lift
- Mechanic parents: agon, distillation
- Guard families: mechanic topology
- Posture: accepted

## Status

Accepted.

## Context

Agon in `aoa-techniques` already held two requested-only candidate registries:
Wave IV move-binding practice candidates and Wave XV epistemic practice
candidates. Distillation already owned candidate intake gates, structured
ledgers, and provenance-preserving narrowing, but no active bridge explained how
Agon pressure should move into Distillation before a technique bundle is
drafted.

Without a bridge, future agents had two bad choices: promote directly from Agon
candidate registries, or duplicate Agon source law inside Distillation.

## Decision

Create `mechanics/distillation/parts/agon-candidate-handoff/` as a
Distillation-owned lane map over Agon requested-only candidates.

The part keeps a source registry and generated compact index that cover all `22`
current Agon technique-side candidates: `12` move-binding candidates and `10`
epistemic candidates. The builder validates each row against the Agon generated
source registries and keeps the handoff in three lanes:

- `first_narrowing_watch`
- `source_boundary_hold`
- `owner_route_hold`

Agon remains the source route for requested-only candidate status and Agon law.
Distillation owns only the narrowing lane. `techniques/` owns any future bundle
after normal atom, topology, evidence, example, checklist, and review surfaces
land.

## Alternatives

- Put the lane map inside `mechanics/agon/`.
  Rejected because the missing function is Distillation narrowing, not Agon
  source ownership.
- Add Agon rows to the external or cross-layer candidate ledgers.
  Rejected because those ledgers already carry specific donor/source universes;
  mixing Agon pressure into them would blur provenance and reopen old counts.
- Draft one or more Agon techniques directly.
  Rejected because the current registries are requested-only and still need
  atom/topology and portability gates.

## Consequences

- Future Agon technique work starts from a complete, checked `12 + 10` lane map
  instead of manual registry reading.
- The generated handoff index is evidence only; it cannot accept Agon
  candidates, define lawful moves, or promote technique bundles.
- The first real extraction pass should choose one candidate from
  `first_narrowing_watch` and write a gate card before drafting a bundle.
- If Agon source registries change, the handoff builder should fail until the
  Distillation lane map is updated intentionally.

## Verification

Expected checks:

```bash
python mechanics/distillation/parts/agon-candidate-handoff/scripts/build_agon_candidate_handoff.py --check
python mechanics/distillation/parts/agon-candidate-handoff/scripts/validate_agon_candidate_handoff.py
python -m pytest -q mechanics/distillation/parts/agon-candidate-handoff/tests/test_agon_candidate_handoff.py
python -m unittest tests.test_distillation_mechanics_topology tests.test_agon_mechanics_topology
python scripts/validate_repo.py
python -m unittest discover -s tests
```
