# Canonical Rubric

This document defines the Stage 1 machine-readable fields used in `TECHNIQUE.md` frontmatter.

Markdown stays authoritative.
`generated/technique_catalog.json` and `generated/technique_catalog.min.json` are derived outputs built from tracked markdown plus `schemas/`.

## Metadata And Canonical Review

Stage 1 metadata can inform selection and canonical review, but it does not replace explicit review judgment.

- frontmatter fields help reviewers understand maturity, validation posture, and publication safety
- they do not auto-promote a technique to `canonical`
- `promoted -> canonical` decisions should follow the bounded review contract in [CANONICAL_REVIEW_GUIDE.md](CANONICAL_REVIEW_GUIDE.md)

## Field meanings

| field | meaning |
|---|---|
| `maturity_score` | Coarse readiness signal from `1` to `5`. Use `5` for canonical defaults, `4` for strong promoted techniques, `3` for bounded promoted techniques, and lower values only for future early-stage states. |
| `rigor_level` | Contract strictness for normal use. `light` fits advisory patterns, `bounded` fits reusable techniques with explicit limits, `strict` fits techniques that rely on hard invariants or fail-surface discipline. |
| `reversibility` | How hard it is to back the technique out after adoption. `easy` means low-cost rollback, `moderate` means rollback needs planned cleanup, `hard` means rollback changes operator policy or enforcement posture. |
| `review_required` | Whether normal adoption should include explicit human review before the technique becomes a default in a new context. |
| `validation_strength` | Evidence strength. `baseline` means mostly structural validation, `source_backed` means real-project evidence exists, `cross_context` means real-project evidence plus second-context or canonical-review reinforcement exists. |
| `public_safety_reviewed_at` | Most recent public-safety review date for the published technique bundle, formatted as `YYYY-MM-DD`. |
| `export_ready` | Whether the technique is safe to include in Stage 1 structured catalog outputs. This field is about machine-readable publication safety for the committed repo-local catalog, not graph or AoA export. |
| `relations` | Small structured links to other in-repo techniques. Keep the list bounded to direct reusable relationships only. |
| `evidence` | Structured list of tracked note files that justify the technique's current public bundle and review posture. |

## Relation types

Stage 1 keeps relation semantics intentionally small:

| type | use |
|---|---|
| `requires` | The technique assumes another technique's contract or prerequisite surface. |
| `complements` | The techniques are adjacent and commonly used together without one depending on the other. |
| `supersedes` | The technique replaces another technique for the same bounded job. |
| `conflicts_with` | The techniques should not be used together in the same bounded surface. |
| `used_together_for` | The techniques often appear in the same flow for one bounded outcome. |
| `derived_from` | The technique is a direct bounded derivative of another in-repo technique. |
| `shares_contract_with` | The techniques rely on the same data or interface contract without being the same pattern. |

This rubric does not introduce graph inference, scoring automation, or selection engines.

## Evidence kinds

| kind | meaning |
|---|---|
| `origin_evidence` | Source-backed note from the original project context. |
| `second_context` | Bounded adaptation note showing reuse beyond the origin project. |
| `canonical_readiness` | Review-oriented note that records canonical readiness or canonical review results. |
| `external_origin` | Provenance note for a bounded external import. |
| `external_review` | Explicit external-import review verdict for an imported technique. |
| `support_note` | Other tracked support note that materially explains bounded use, rollout, or triage. |

## Stage 1 discipline

Current repo state:

- all currently tracked techniques are `export_ready: true`
- this is intentional for the current corpus and means every published bundle is considered safe for Stage 1 catalog publication
- this does **not** make `export_ready` a useful selector yet; for now it is a publication floor, not a ranking or recommendation signal

Concrete reasons a future technique might be `export_ready: false`:

- the bundle is still public-safe as markdown, but its structured frontmatter or evidence surface is not yet trustworthy enough for machine-readable publication
- the technique has a bounded unresolved publication-safety question that should keep it out of the derived catalog until review closes
- the bundle is intentionally tracked during a transition where Stage 1 structured publication would overstate its readiness or stability

- Keep frontmatter values operational and reviewable.
- Do not treat `relations` as a graph design surface yet.
- Do not treat `export_ready` as permission for AoA, graph, or vector export work.
- Do not treat `export_ready` as a default-use selector while the field remains uniformly true across the current corpus.
- If catalog output drifts from markdown, fix markdown or rerun `python scripts/build_catalog.py`; do not hand-edit generated files.
