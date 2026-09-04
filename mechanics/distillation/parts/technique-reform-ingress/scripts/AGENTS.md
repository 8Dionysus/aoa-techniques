# AGENTS.md

## Applies to

This card applies to
`mechanics/distillation/parts/technique-reform-ingress/scripts/` and every descendant unless a nearer
`AGENTS.md` narrows the path.

## Role

This directory holds one-owner technique-reform report builders for the
Distillation part.

These scripts may rebuild scout or projection reports under the same
`technique-reform-ingress` part. They do not own repo-wide generated readers,
frontmatter truth, schema truth, or path migration authority.

Keep imports repo-relative and deterministic. If a script needs shared parsing
or validation helpers, import them from root `scripts/validate_repo.py` rather
than copying logic into the part.

## Read before editing

Read:

Inherit [../../../AGENTS.md](../../../AGENTS.md#read-before-editing); use the local part route.

## Boundaries

Inherited mechanics boundary: do not override stronger sources; see [mechanics/AGENTS.md](../../../../AGENTS.md#boundaries); local role remains above.

## Validation

Inherit [../../../../AGENTS.md](../../../../AGENTS.md#validation): `mechanics/part-local`; see [VALIDATION.md](../../../../../VALIDATION.md) and `config/validation_lanes.json`. Local `mechanics/distillation/parts/technique-reform-ingress/scripts/AGENTS.md`: bounded active part/promotion boundary.
## Closeout

Local delta `mechanics/distillation/parts/technique-reform-ingress/scripts/AGENTS.md`: name the bounded active part and state whether promotion remains outside this package.
