# Review Guides

This district holds active review, maturity, semantic-review, and caution
contracts for `aoa-techniques`.

Use it when the question is how to interpret readiness metadata, promotion
review, semantic review packets, or shadow/caution language without turning
those surfaces into technique meaning or generated policy.

## Surfaces

| Surface | Role |
|---|---|
| [Canonical Rubric](CANONICAL_RUBRIC.md) | explains current frontmatter review fields, relation types, and evidence-note kinds |
| [Canonical Review Guide](CANONICAL_REVIEW_GUIDE.md) | bounds `promoted -> canonical` review decisions |
| [Semantic Review Guide](SEMANTIC_REVIEW_GUIDE.md) | explains authored semantic-review packets and their generated manifest |
| [Technique Shadow Guide](TECHNIQUE_SHADOW_GUIDE.md) | governs markdown-first caution language and shadow-review escalation |

## Owner Split

Authored technique meaning remains in `../../techniques/**/TECHNIQUE.md`.
Mechanic-owned review packets remain under
`../../mechanics/distillation/parts/technique-reform-ingress/reviews/`.
Generated manifests and reader companions remain derived outputs under
`../../generated/` and `../readers/`.

This district owns how those review surfaces should be read together. It does
not own promotion evidence ledgers, external evidence work, or proof doctrine.

## Reading Routes

Promotion and maturity route:

1. [Canonical Rubric](CANONICAL_RUBRIC.md)
2. [Canonical Review Guide](CANONICAL_REVIEW_GUIDE.md)
3. [Audit Mechanic](../../mechanics/audit/README.md)
4. [Mechanics Atlas](../../mechanics/README.md)

Semantic and caution route:

1. [Semantic Review Guide](SEMANTIC_REVIEW_GUIDE.md)
2. [Technique Shadow Guide](TECHNIQUE_SHADOW_GUIDE.md)
3. [Review Readers](../readers/review/README.md)
4. [Distillation Review Packet Atlas](../../mechanics/distillation/parts/technique-reform-ingress/reviews/README.md)

Agent read order, validation, and closeout live in [AGENTS](AGENTS.md).
