# Technique-canon statistics

This directory is the owner-local stats port for `aoa-techniques`. It names
measurements whose domain meaning belongs to the public practice canon and
hands their portable contracts and evidence refs to `aoa-stats`.

The port does not observe private use, infer technique quality, decide
promotion, or replace authored `TECHNIQUE.md` status and review evidence.

## Current question

`aoa-techniques/published-promotion-readiness-pass-ratio` asks what fraction of
the current published, non-deprecated readiness records carry
`readiness_passed: true` in the owner-generated promotion-readiness projection.

The consumer is the Audit promotion-readiness route. The statistic helps that
route notice cohort-level movement without turning a ratio into a status
change or proof claim.

## Reference derivation

The denominator is every record in
`generated/technique_promotion_readiness.min.json`. The numerator is the subset
whose owner-generated `readiness_passed` field is true. The current packet is a
source-revision census, not live telemetry.

`readiness_passed` means only that the projection found none of its declared
local blockers: a promoted bundle without its canonical-readiness note, or a
canonical bundle without its adverse-effects review. It does not establish
quality, effectiveness, adoption, external validation, skill lift, eval
success, runtime use, or permission to change technique status.

## Owner routes

- `port.manifest.json` owns the local question and measurement contract.
- `packets/` contains the revision-bound public reference packet.
- `generated/technique_promotion_readiness.min.json` is the derived owner
  evidence surface.
- `techniques/**/TECHNIQUE.md` and their typed notes remain authored truth.
- `mechanics/audit/parts/promotion-readiness-matrix/` owns the consuming audit
  route.
