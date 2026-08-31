# AGENTS.md

## Applies to

This card applies to `stats/` and all descendants.

## Role

`stats/` is the owner-local measurement port for the public technique canon.
It defines technique-domain questions, populations, measures, evidence refs,
and authority ceilings while remaining compatible with the central
`aoa-stats` protocol.

It does not own cross-repository aggregation, technique status, promotion
decisions, eval verdicts, usage surveillance, skill adoption, or runtime truth.

## Read before editing

1. Root `AGENTS.md`, `DESIGN.md`, and `docs/TECHNIQUE_ATOM_CONTRACT.md`.
2. The owner source and consuming mechanic named by the measurement.
3. The central `aoa-stats` measurement and local-port contracts.
Read `README.md` only when the selected task needs its human map; do not preload unrelated maps.

## Boundaries

- Derive only from public owner surfaces and retain portable evidence refs.
- Keep packet refs repository-relative and raw evidence content out of packets.
- Treat generated readiness as a projection of technique bundles, not as
  technique meaning or a promotion verdict.
- Keep live/reference posture explicit; the current export is reference-only.
- Do not add a measure without a real owner question and a named consumer.

## Validation

Inherit parent validation: source-fast/generated/advisory; see [VALIDATION.md](../VALIDATION.md) and config/validation_lanes.json.

## Closeout

Report the question, population, source revision, reference/live posture,
authority ceiling, owner readiness evidence inspected, whether the reference
packet was refreshed, and which validation route ran.
