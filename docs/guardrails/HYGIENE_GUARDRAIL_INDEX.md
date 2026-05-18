# Hygiene Guardrail Index

This index names the current link and Markdown-shape guardrails for
`aoa-techniques`.

The human law lives in
[Link And Shape Hygiene Protocol](LINK_AND_SHAPE_HYGIENE_PROTOCOL.md).

## Guardrail Table

| Guardrail | Primary check surface | Source input | Status |
|---|---|---|---|
| Local root/docs Markdown links | [test_docs_surface_guardrails.py](../../tests/test_docs_surface_guardrails.py) | root Markdown plus `docs/**/*.md` | active |
| Flat docs surface coverage | [test_docs_surface_guardrails.py](../../tests/test_docs_surface_guardrails.py) | `docs/*.md` plus [Current Surface Index](CURRENT_SURFACE_INDEX.md) | active |
| Thematic district placement | [test_docs_surface_guardrails.py](../../tests/test_docs_surface_guardrails.py) | [Thematic District Protocol](THEMATIC_DISTRICT_PROTOCOL.md) | active |
| Generated reader parity | [validate_repo.py](../../scripts/validate_repo.py) | builders, docs readers, generated JSON | active |
| Release-wide freshness | [release_check.py](../../scripts/release_check.py) | all registered builders and validators | active |

Exact command lanes live in [docs/guardrails AGENTS](AGENTS.md#validation)
and root [AGENTS](../../AGENTS.md#validation).

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
