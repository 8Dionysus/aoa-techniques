# AGENTS.md

## Applies to

This card applies to Audit active parts until a nearer `AGENTS.md` narrows the
lane.

## Role

Each child directory owns one active Audit part. Part READMEs are current
operating surfaces, not raw archives.

## Read before editing

Read:

1. repository root `AGENTS.md`
2. `mechanics/AGENTS.md`
3. `mechanics/audit/AGENTS.md`
4. `mechanics/audit/PARTS.md`
Read `README.md` only when the selected task needs its human map; do not preload unrelated maps.

## Boundaries

- Keep part changes bounded to that part's role.
- Update `../PARTS.md` when a part is added, renamed, or retired.
- Update `../PROVENANCE.md` when source evidence changes the part's behavior.
- Preserve pre-prune source accounting in `../legacy/raw/` before shortening a
  ledger or runbook.
- Do not change technique status from inside a part without bundle-local
  canonical evidence and the normal validation path.

## Validation

Select the narrowest owner route: `mechanics/part-local` for part-local work; add `source-fast` for authored routes or `generated` for projections. See [VALIDATION.md](../../../VALIDATION.md); exact order is `config/validation_lanes.json`; focused procedure stays with the nearest owner. Report checks, skips, and blockers.

## Closeout

Report the mechanic package, part, legacy surface, or helper changed;
whether source, generated, schema, example, or test surfaces moved; checks run;
checks skipped; and the next owner route.
