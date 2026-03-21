# Technique Example Lift Guide

This guide defines the bounded contract for the example source-lift family.

Use it when the repository already has authored example files under technique bundles, but the next question is how to expose them as derived example knowledge without turning them into scenario graphs, executable tests, or richer step extraction.

See also:
- [Start Here](START_HERE.md)
- [Technique Examples](TECHNIQUE_EXAMPLES.md)
- [KAG Source Lift Guide](KAG_SOURCE_LIFT_GUIDE.md)
- [Documentation Map](README.md)

This family uses one stable shape:

- authoritative source: authored example markdown under `examples/`
- reader companion: `TECHNIQUE_EXAMPLES.md`
- derived manifests: `generated/technique_example_manifest.json` and `generated/technique_example_manifest.min.json`
- what it must not become: scenario graphs, executable tests, richer step extraction, or replacement example authorship

## Source Contract

The current example lift stays bundle-local and markdown-first:

- example files live under `examples/`
- each example keeps one authored title
- example bodies remain authored markdown
- the generated layer routes readers back to the example file instead of replacing it

## Reader Companion And Derived Manifests

The generated outputs for this source class are:

- `generated/technique_example_manifest.json`
- `generated/technique_example_manifest.min.json`
- `docs/TECHNIQUE_EXAMPLES.md`

Those outputs stay derived from authored example markdown and source bundles.

## Reader Surface Contract

`TECHNIQUE_EXAMPLES.md` stays domain-first and technique-first.

For each example it shows only:

- example title
- whether body content is present
- example path
- source routing back to the technique bundle

It does not inline full example bodies into the generated reader surface.

## Boundaries

Example lift does not become:

- scenario graphs
- executable tests
- richer step extraction
- a replacement for the authored example file

If a reader needs the actual narrative, commands, or sample payloads, the answer still lives in the example markdown.

## Validation

Regenerate and verify this source class with:

- `python scripts/build_example_manifest.py`
- `python scripts/release_check.py`
- `python -m unittest discover -s tests`
- `python scripts/validate_repo.py`
