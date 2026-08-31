# AGENTS.md

## Applies to

This card applies to
`mechanics/recurrence/parts/live-observation-producers/scripts/` and every descendant unless a nearer
`AGENTS.md` narrows the path.

## Role

This directory holds one-owner Recurrence helper scripts for live observation
producer inputs.

`publish_live_receipts.py` appends bounded technique-layer receipts to the
owner-local live JSONL log. The log remains observation evidence only; it does
not create candidates, close quests, change technique status, issue proof
verdicts, or claim runtime recurrence authority.

Keep the helper public-safe and repo-relative. Do not add hidden network calls,
ambient credentials, or private session dumps.

## Read before editing

Read:

1. repository root `AGENTS.md`
2. `mechanics/AGENTS.md`
3. `mechanics/recurrence/AGENTS.md`
4. `mechanics/recurrence/PARTS.md`
Read `README.md` only when the selected task needs its human map; do not preload unrelated maps.

## Boundaries

Inherited mechanics boundary: do not override stronger sources; see [mechanics/AGENTS.md](../../../../AGENTS.md#boundaries); local role remains above.

## Validation

Inherit [../../../../AGENTS.md](../../../../AGENTS.md#validation): `mechanics/part-local`; see [VALIDATION.md](../../../../../VALIDATION.md) and `config/validation_lanes.json`. Local `mechanics/recurrence/parts/live-observation-producers/scripts/AGENTS.md`: bounded active part/promotion boundary.
## Closeout

Local delta `mechanics/recurrence/parts/live-observation-producers/scripts/AGENTS.md`: name the bounded active part and state whether promotion remains outside this package.
