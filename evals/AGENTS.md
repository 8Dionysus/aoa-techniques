# AGENTS.md

## Applies to

This card applies to `aoa-techniques/evals/` and every file below it.

## Role

This skeleton port captures technique-canon eval pressure before it is accepted,
rejected, or normalized by `aoa-evals`.

`aoa-evals` owns central verdict, scoring, regression, and proof doctrine
authority. This port owns only technique-local intake, cases, fixtures, suites,
reports, and source refs.

## Read before editing

Read the root `AGENTS.md`, then this card, `PORT.yaml`, and the nearest intake,
suites, or reports surface you will touch. For central proof adoption rules,
read the local eval-port standard in `aoa-evals`.
Read `README.md` only when the selected task needs its human map; do not preload unrelated maps.

## Boundaries

- Keep technique bundle meaning, atom contracts, topology, and public practice
  canon in `aoa-techniques`.
- Keep proof doctrine, verdicts, scoring, and regression authority in
  `aoa-evals`.
- Do not treat an intake packet as proof acceptance or a central eval verdict.
- Do not place private traces, secrets, or unreduced operator evidence here.

## Validation

Select the narrowest owner route: `source-fast` for authored or route-card work; add `generated` for projections and `release` only for release posture. See [VALIDATION.md](../VALIDATION.md); exact order is `config/validation_lanes.json`; focused procedure stays with the nearest owner. Report checks, skips, and blockers.

## Closeout

Report changed eval surfaces, current `PORT.yaml` status, validation run, any
skipped central proof adoption, and the next route into `aoa-evals` when needed.
