# Agon Landing Log

This ledger records checked landings for the `aoa-techniques` side of Agon
mechanics.

## 2026-05-01 - Active/legacy split

Scope:

- recorded immutable Wave IV and Wave XV recovery paths in `PROVENANCE.md`
- moved current Agon behavior into active `parts/`
- added `DIRECTION.md`, `PARTS.md`, and `PROVENANCE.md` accounting
- kept requested candidate posture unchanged

Stop-lines preserved:

- requested candidates are not promoted techniques
- `aoa-techniques` does not define Agon lawful move vocabulary
- no skill workflow, proof verdict, scar, retention, rank, arena, KAG, memory, or
  ToS authority is created here

Validation lane:

Both Agon parts passed their owner builders, validators, and targeted tests,
followed by repository validation and the repository test suite.

## 2026-05-03 - Distillation candidate handoff route

Scope:

- added a downstream route from Agon requested-only candidate registries to
  [Distillation Agon Candidate Handoff](../distillation/parts/agon-candidate-handoff/README.md)
- kept Agon candidate source registries unchanged
- kept the handoff as Distillation lane accounting, not Agon acceptance

Stop-lines preserved:

- no candidate status changed
- no lawful move vocabulary, arena/session law, proof verdict, scar, rank,
  KAG, ToS, runtime, memory, routing, or skill authority moved into
  `aoa-techniques`

Validation lane:

The handoff part passed its owner builder, validator, targeted part-local tests,
and the affected mechanic suites.
