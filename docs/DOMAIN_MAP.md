# Domain Map

This document anchors the bounded meaning of the current `domain` values in technique frontmatter.

## Current domains

| domain | meaning |
|---|---|
| `agent-workflows` | Techniques for how humans and agents coordinate change execution, rollout safety, planning, verification, and reporting. |
| `docs` | Techniques for repository structure, instruction surfaces, context composition, and portable documentation contracts. |
| `evaluation` | Techniques for machine-readable validation outputs, published summaries, diagnostics, integrity checks, and staged enforcement signals. |
| `history` | Techniques for versioned session or history artifacts that stay local-first and reviewable without becoming memory objects, recall surfaces, or instruction authority. |

## Domain rules

- Pick the domain that best matches the technique's primary reusable contract, not every place it may be used.
- Do not create a new domain just to fit one project-shaped bundle.
- If a technique spans multiple areas, choose the domain that should own the default review vocabulary for that technique.
- `history` owns session or transcript artifact discipline only; memory objects, retrieval semantics, and recall surfaces still belong outside this repo's current ownership boundary.
- Adding a new domain later requires updating this file, `schemas/technique.schema.json`, the template, and validator expectations in the same wave.
