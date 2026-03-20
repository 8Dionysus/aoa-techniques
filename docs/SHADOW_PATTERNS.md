# Shadow Patterns

This file is generated from authoritative `TECHNIQUE.md` bundles plus typed canonical `adverse_effects_review` notes.
Do not edit it by hand; run `python scripts/build_catalog.py`.

Use this surface when the main question is not which technique to choose, but where a canonical technique can quietly make the system worse and which watch seam to inspect first.

This surface is canonical-only. It stays bounded to authored markdown, typed adverse-effects notes, one working set, and validator-backed prompts. It does not do scoring, policy routing, or generated caution metadata.

See also:
- [Technique Shadow Guide](TECHNIQUE_SHADOW_GUIDE.md)
- [Risk And Negative-Effect Lift Guide](RISK_AND_NEGATIVE_EFFECT_LIFT_GUIDE.md)
- [Published-Summary Shadow Review](PUBLISHED_SUMMARY_SHADOW_REVIEW.md)

## Working Set

### Published-summary shadow cluster

- Techniques: [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md), [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md), [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md), [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md)
- Review: [PUBLISHED_SUMMARY_SHADOW_REVIEW.md](PUBLISHED_SUMMARY_SHADOW_REVIEW.md)
- Why grouped: Canonical storage, remediation, integrity, and rendering techniques whose caution language now shares one bounded shadow watch surface.

| technique | current role | watch seam | main failure mode | note |
|---|---|---|---|---|
| [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) | default storage contract for stable latest alias plus nested history copy | keep a clean latest alias from masking history-trust drift, and keep storage complexity subordinate to one stable latest-plus-history contract | the latest alias looks healthy while nested history parity or reader precedence is already drifting | [Adverse Effects Review](../techniques/evaluation/latest-alias-plus-history-copy/notes/adverse-effects-review.md) |
| [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) | canonical downstream remediation rollup over latest published summaries | keep remediation follow-up distinct from integrity verdicts and rendering policy while holding bucket policy to one bounded reviewable surface | remediation output starts reading like an integrity verdict or rendering instruction | [Adverse Effects Review](../techniques/evaluation/published-summary-remediation-snapshot/notes/adverse-effects-review.md) |
| [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) | canonical diagnostic trust layer over published summaries and downstream rollups | preserve the helper's diagnostic-only role, keep optional checks subordinate to required-source health, and keep stricter enforcement as a separate rollout decision | optional consistency noise starts crowding out required-source health and dual-write coherence | [Adverse Effects Review](../techniques/evaluation/telemetry-integrity-snapshot/notes/adverse-effects-review.md) |
| [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) | canonical rendering policy for required versus optional summary sources | keep the policy reusable and readable enough that warning traffic does not become ambient noise and the bundle does not collapse into a published-summary appendix | an actually critical source is misclassified as optional and stays there long enough to distort interpretation | [Adverse Effects Review](../techniques/evaluation/required-vs-optional-source-rendering/notes/adverse-effects-review.md) |

## Common Shadow Questions

| question | inspect first | why |
|---|---|---|
| I need to check whether the latest summary looks clean while history trust is already broken | [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) | Start with the latest-plus-history storage contract and its alias/history false-confidence seam. |
| I need to stop remediation output from drifting into integrity or rendering policy | [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) | Inspect the bounded remediation rollup before widening backlog language into trust verdicts or renderer instructions. |
| I need to keep a diagnostic helper from turning into an implicit enforcement gate | [AOA-T-0010](../techniques/evaluation/telemetry-integrity-snapshot/TECHNIQUE.md) | Inspect the diagnostic-only trust layer and its optional-check noise seam before any stricter rollout decision. |
| I need optional-source warnings to stay visible without becoming noisy or package-shaped | [AOA-T-0011](../techniques/evaluation/required-vs-optional-source-rendering/TECHNIQUE.md) | Inspect the required-versus-optional rendering policy and its warning-fatigue plus package-appendix seam. |

## Boundaries

- The source of meaning stays in the full technique bundle and its typed adverse-effects review note.
- This surface is a bounded lookup aid for canonical watch seams, not a permission to skip `TECHNIQUE.md`.
- If a question needs scoring, policy tiers, or machine-readable caution exports, that is a later wave.
