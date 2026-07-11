# aoa-techniques Local KAG Provider

`kag/` exposes the current `aoa-techniques` KAG provider packet as portable
source-linked records.

## Operating Card

| Field | Route |
| --- | --- |
| role | local KAG provider for technique source-lift surfaces |
| records | `nodes/`, `edges/`, `indexes/`, `projections/`, `receipts/` |
| manifest | `manifest.json` |
| source route | authored technique bundle and source-owned KAG export |
| consumer route | `aoa-kag` registry/composition, `abyss-stack`, MCP resources |
| owner return | `docs/source-lift/KAG_EXPORT.md` and the `AOA-T-0043` technique bundle |

## Record Classes

| Class | Current record |
| --- | --- |
| node | KAG export capsule and source technique bundle |
| edge | KAG export returns to the source bundle |
| index | repository source, entity, artifact, and event indexes |
| projection | MCP-readable source-return packet |
| receipt | validator receipt for current KAG export parity |

Runtime graph and vector stores consume these records downstream through their
own owner routes. Git holds the compact provider packet and source-return
handles.
