# Technique Capsule Guide

This guide defines the bounded contract behind the local runtime capsule family.

Capsules are derived lookup cards for local runtime use. They are not KAG/source-lift surfaces, they do not replace `TECHNIQUE.md`, and they do not become a new source of truth.

See also:
- [Technique Capsules](TECHNIQUE_CAPSULES.md)
- [`../generated/technique_capsules.json`](../generated/technique_capsules.json)
- [`../generated/technique_capsules.min.json`](../generated/technique_capsules.min.json)
- [Documentation Map](README.md)

## Source Contract

Every capsule stays bounded to one frontmatter field plus a fixed section set from the canonical bundle:

- frontmatter `summary`
- `## Intent`
- `## When to use`
- `## When not to use`
- `## Inputs`
- `## Outputs`
- `## Contracts`
- `## Risks`
- `## Validation`

The generator may shorten or normalize those sections into runtime-card language, but it must stay derived from the authored bundle and route readers back to that bundle.

## Runtime Surfaces

The capsule family currently exposes four bounded surfaces:

- `../generated/technique_capsules.json`
  - the full local runtime payload
- `../generated/technique_capsules.min.json`
  - the strict min projection for the smallest runtime card shape
- `TECHNIQUE_CAPSULES.md`
  - the human reader surface grouped by `DOMAIN_ORDER` and ordered with `canonical` before `promoted`
- this guide
  - the authored contract and boundary explanation for the family

## Field Intent

The runtime card fields are intentionally narrow:

- `summary`
  - the authored frontmatter summary
- `one_line_intent`
  - one short statement of what the technique is trying to do
- `use_when_short`
  - one short signal for when the technique fits
- `do_not_use_short`
  - one short signal for when the technique does not fit
- `inputs_short`
  - a compact view of what the technique needs
- `outputs_short`
  - a compact view of what the technique produces
- `core_contract_short`
  - the main contract that must remain true
- `main_risk_short`
  - the main failure or misuse seam to watch
- `validation_short`
  - the smallest validation reminder that still routes back to the bundle

## Boundaries

- Capsules are local runtime lookup aids only.
- Capsules do not replace technique selection, semantic review, shadow review, or docs/status routing surfaces.
- Capsules do not become a selector engine, scoring layer, or policy-routing layer.
- Capsules do not expand into a KAG/source-lift family in this wave.

## Regeneration

When the source bundle changes, regenerate the capsule family:

- `python scripts/build_capsules.py`
- `python scripts/validate_repo.py`
