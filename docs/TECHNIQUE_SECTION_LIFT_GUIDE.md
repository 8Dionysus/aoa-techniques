# Technique Section Lift Guide

This guide defines the bounded contract for `markdown-technique-section-lift`.

Use it when the repository already has stable `TECHNIQUE.md` structure, but the next question is how the first lifted sections can become a derived routing surface without turning section markdown into IDs, scoring, or graph behavior.

See also:
- [Start Here](START_HERE.md)
- [Technique Sections](TECHNIQUE_SECTIONS.md)
- [KAG Source Lift Guide](KAG_SOURCE_LIFT_GUIDE.md)
- [`markdown-technique-section-lift`](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md)
- [Documentation Map](README.md)

This family uses one stable shape:

- authoritative source: authored `TECHNIQUE.md` markdown with stable heading order
- reader companion: `TECHNIQUE_SECTIONS.md`
- derived manifests: `generated/technique_section_manifest.json` and `generated/technique_section_manifest.min.json`
- what it must not become: section IDs, section scoring, search expansion, or graph behavior

## Source Contract

The current section-lift contract is intentionally narrow:

- one authored `TECHNIQUE.md` bundle remains the source of truth
- only the first 10 lifted headings are in scope
- lifted headings stay in fixed order
- the generated surface routes readers back to the source bundle instead of replacing it

The current lifted heading set is:

- `Intent`
- `When to use`
- `When not to use`
- `Inputs`
- `Outputs`
- `Core procedure`
- `Contracts`
- `Risks`
- `Validation`
- `Adaptation notes`

## Reader Companion And Derived Manifests

The generated outputs for this source class are:

- `generated/technique_section_manifest.json`
- `generated/technique_section_manifest.min.json`
- `docs/TECHNIQUE_SECTIONS.md`

Those outputs stay derived from authored markdown and remain routing aids only.

## Reader Surface Contract

`TECHNIQUE_SECTIONS.md` stays heading-first, not technique-first.

For each lifted heading, it shows only:

- which techniques expose the heading
- domain and status context
- section order
- source routing back to `TECHNIQUE.md`

It does not dump full lifted section markdown into the generated reader surface.

## Boundaries

Not part of this wave:

- section IDs
- section scoring
- search expansion
- graph behavior
- replacing the authored bundle with generated section payloads

The meaning remains in the source markdown.

## Validation

Regenerate and verify this source class with:

- `python scripts/build_section_manifest.py`
- `python scripts/release_check.py`
- `python -m unittest discover -s tests`
- `python scripts/validate_repo.py`
