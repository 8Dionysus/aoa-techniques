# AGENTS.md

## Applies to

This card applies to Distillation active parts until a nearer `AGENTS.md`
narrows the lane.

## Role

Each child directory owns one active Distillation part. Part READMEs are current
operating surfaces, not raw donor archives.

## Read before editing

Read:

Inherit [../AGENTS.md](../AGENTS.md#read-before-editing); use the local part route.

## Boundaries

- Keep part changes bounded to that part's role.
- Update `../PARTS.md` when a part is added, renamed, or retired.
- Update `../PROVENANCE.md` when source evidence changes the part's behavior.
- Before shortening a ledger, preserve recovery by recording its exact
  pre-change Git commit and original path in `../PROVENANCE.md` or the
  retirement decision; do not create an archive-only copy.
- Do not promote a candidate into `techniques/` from inside a part without the
  normal bundle evidence and validation path.

## Validation

Inherit [../../AGENTS.md](../../AGENTS.md#validation): `mechanics/part-local`; see [VALIDATION.md](../../../VALIDATION.md) and `config/validation_lanes.json`. Local `mechanics/distillation/parts/AGENTS.md`: bounded active part/promotion boundary.
## Closeout

Local delta `mechanics/distillation/parts/AGENTS.md`: name the bounded active part and state whether promotion remains outside this package.
