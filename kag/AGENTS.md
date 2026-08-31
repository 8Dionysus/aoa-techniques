# AGENTS.md

## Applies to

This card applies to `kag/` and every nested path.

## Role

`kag/` is the repo-local KAG provider home for `aoa-techniques`.

It publishes portable, source-linked KAG records derived from the public
technique canon and the source-owned KAG export. Technique meaning remains in
`techniques/`; this home gives `aoa-kag`, `abyss-stack`, and MCP consumers
stable handles back to the owning bundles and source-lift docs.

## Operating Card

| Field | Route |
| --- | --- |
| input | `generated/kag_export.min.json`, `docs/source-lift/KAG_EXPORT.md`, source technique bundle |
| output | local manifest, portable records, source-return projection, validation receipt |
| owner | `kag/AGENTS.md`, `kag/README.md`, `kag/manifest.json` |
| next route | source bundle -> KAG export builder/validator -> `aoa-kag` registry/composition |
| validation | source-fast lane, generated KAG export checks, release lane when generated surfaces move |

## Read before editing

Read:

1. root `AGENTS.md`
2. `docs/ROOT_SURFACE_LAW.md`
3. `docs/source-lift/KAG_EXPORT.md`
4. `generated/AGENTS.md` for generated export posture
5. source technique bundle named by the touched record
6. `aoa-kag/kag/LOCAL_SUBTREE_PROTOCOL.md` for shared provider contract shape
Read `README.md` only when the selected task needs its human map; do not preload unrelated maps.

## Source Routes

- `generated/kag_export.min.json`
- `docs/source-lift/KAG_EXPORT.md`
- `techniques/instruction/capability-boundary/multi-source-primary-input-provenance/TECHNIQUE.md`
- `scripts/build_kag_export.py`
- `scripts/validators/projection_kag.py`

## Boundaries

Do not treat `kag/` records as technique bundle meaning, generated export
authority, proof verdicts, routing policy, or runtime storage. Route meaning
changes to `techniques/`, generated parity to `generated/`, and shared KAG
contract changes to `aoa-kag`.

## Validation

Inherit parent validation: source-fast/generated/release; see [VALIDATION.md](../VALIDATION.md) and config/validation_lanes.json.

## Closeout

Report changed KAG records, source-return surfaces, validation run, and any
generated export that should be rebuilt before consumers read the provider.
