# AGENTS.md

## Applies to

This card applies to Distillation active parts until a nearer `AGENTS.md`
narrows the lane.

## Role

Each child directory owns one active Distillation part. Part READMEs are current
operating surfaces, not raw donor archives.

## Read before editing

Read:

1. repository root `AGENTS.md`
2. `mechanics/AGENTS.md`
3. `mechanics/distillation/AGENTS.md`
4. `mechanics/distillation/PARTS.md`
Read `README.md` only when the selected task needs its human map; do not preload unrelated maps.

## Boundaries

- Keep part changes bounded to that part's role.
- Update `../PARTS.md` when a part is added, renamed, or retired.
- Update `../PROVENANCE.md` when source evidence changes the part's behavior.
- Preserve pre-prune source accounting in `../legacy/raw/` before shortening a
  ledger.
- Do not promote a candidate into `techniques/` from inside a part without the
  normal bundle evidence and validation path.

## Validation

Inherit [../../AGENTS.md](../../AGENTS.md#validation): `mechanics/part-local`; see [VALIDATION.md](../../../VALIDATION.md) and `config/validation_lanes.json`. Local `mechanics/distillation/parts/AGENTS.md`: bounded active part/promotion boundary.
## Closeout

Local delta `mechanics/distillation/parts/AGENTS.md`: name the bounded active part and state whether promotion remains outside this package.
