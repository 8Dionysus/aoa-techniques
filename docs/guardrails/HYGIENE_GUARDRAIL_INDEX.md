# Hygiene Guardrail Index

This index names the current link and Markdown-shape guardrails for
`aoa-techniques`.

The human law lives in
[Link And Shape Hygiene Protocol](LINK_AND_SHAPE_HYGIENE_PROTOCOL.md).

## Guardrail Table

| Guardrail | Primary check | Source input | Status |
|---|---|---|---|
| Local root/docs Markdown links | `python -m unittest tests.test_docs_surface_guardrails` | root Markdown plus `docs/**/*.md` | active |
| Flat docs surface coverage | `python -m unittest tests.test_docs_surface_guardrails` | `docs/*.md` plus [Current Surface Index](CURRENT_SURFACE_INDEX.md) | active |
| Thematic district placement | `python -m unittest tests.test_docs_surface_guardrails` | [Thematic District Protocol](THEMATIC_DISTRICT_PROTOCOL.md) | active |
| Generated reader parity | `python scripts/validate_repo.py` | builders, docs readers, generated JSON | active |
| Release-wide freshness | `python scripts/release_check.py` | all registered builders and validators | active |

## Success Conditions

The hygiene guardrail is healthy when:

1. active local Markdown links resolve;
2. every flat `docs/*.md` file is named in the current surface index;
3. broad guide families move with route cards, links, tests, and generated
   parity;
4. generated reader companions are rebuilt from source rather than hand-edited;
5. historical references are routed through `legacy/`, `decisions/`, or the
   owning mechanic instead of staying as active docs-root clutter.

## How To Extend

Add a new guardrail only when it has a human law surface and a machine check or
explicit validation route. If the rule cannot yet be checked, put the finding
in the owning decision, roadmap, mechanic review, or legacy receipt instead of
adding decorative guardrail prose.
