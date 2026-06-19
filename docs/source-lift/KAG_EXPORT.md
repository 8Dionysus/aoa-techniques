# KAG Export

This document records the current source-owned tiny KAG export posture for
`aoa-techniques`.

The export is a bounded capsule for one technique object.
It exists so downstream repositories can consume a source-owned entry surface
without replacing authored technique meaning.

## Current pilot

The current pilot stays intentionally narrow:

- one exported object: `AOA-T-0043`
- one entry surface: `generated/technique_capsules.json`
- one compact consumer surface: `generated/kag_export.min.json`
- one `artifact_identity` block that names the export ABI, producer,
  verification route, public boundary, and consumer expectation
- one source-owned boundary note that keeps markdown authoritative

## Core rule

The export is a guide to the source, not a replacement for the source.

It may expose a bounded question, summaries, section handles, and direct
relation refs for one technique, but authored technique meaning remains in the
corresponding `TECHNIQUE.md` bundle.

The `artifact_identity` block describes the generated export capsule itself. It
does not promote the capsule above the source-authored technique bundle, and it
does not replace KAG owner review.

## Current files

- `generated/kag_export.json`
- `generated/kag_export.min.json`
- `scripts/build_kag_export.py`

## Regeneration

Use [AGENTS](AGENTS.md#validation) for the current regeneration and validation
lane.
