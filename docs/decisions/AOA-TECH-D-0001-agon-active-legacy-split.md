# Split Agon Mechanics Into Active Parts And Legacy Provenance

Status: accepted
Date: 2026-05-01

## Index Metadata

- Decision ID: AOA-TECH-D-0001
- Original date: 2026-05-01
- Surface classes: mechanic package, legacy/provenance
- Technique axes: mechanic bridge
- Mechanic parents: agon
- Guard families: mechanic topology, legacy/provenance
- Posture: accepted

## Context

The first `mechanics/` split moved Agon-shaped files out of flat `docs/`, but it
left active contracts, wave receipts, and recurrence notes side by side in the
package root. That preserved paths, but it did not yet reproduce the AoA
mechanics pattern used in `Agents-of-Abyss`: preserve wave/source material in
`legacy`, then build active route surfaces through `PROVENANCE`, `PARTS`, and
part-local docs.

## Options

- Keep the simple package root and treat Wave IV / Wave XV files as normal active
  docs.
- Move only the wave files to `legacy/raw/` and leave the active route informal.
- Build the first complete owner-local Agon package shape: active parts,
  provenance bridge, landing log, and legacy accounting.

## Decision

Use the complete active/legacy split for `mechanics/agon/` as the first
one-mechanic pass.

The active route now lives in:

- `mechanics/agon/README.md`
- `mechanics/agon/DIRECTION.md`
- `mechanics/agon/PARTS.md`
- `mechanics/agon/parts/`
- `mechanics/agon/LANDING_LOG.md`
- `mechanics/agon/PROVENANCE.md`

The preserved wave receipts now live in:

- `mechanics/agon/legacy/raw/AGON_WAVE4_TECHNIQUE_LANDING.md`
- `mechanics/agon/legacy/raw/AGON_WAVE15_TECHNIQUES_LANDING.md`

## Consequences

- Routine Agon technique-side work should start from the active route, not raw
  wave files.
- Raw wave receipts remain preserved and mapped through `legacy/INDEX.md` and
  `PROVENANCE.md`.
- Requested candidates remain requested only; this split does not promote a
  technique bundle.
- Agon-specific source registries, generated indexes, schemas, examples, scripts, tests, and
  recurrence manifests were moved into part-local homes in the follow-up
  artifact-topology pass recorded in
  `docs/decisions/AOA-TECH-D-0002-agon-part-local-artifacts.md`.
