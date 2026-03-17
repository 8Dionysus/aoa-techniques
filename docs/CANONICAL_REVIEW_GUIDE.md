# Canonical Review Guide

This guide defines the bounded review contract for `promoted -> canonical` decisions.

Use it when a technique already looks strong and reusable, but the repo still needs one explicit decision about whether it is the default recommendation within its bounded scope.

This guide is review-first. It does not auto-promote techniques from frontmatter metadata, generated catalog fields, or validator results.

## Outcomes

Canonical review should end in one of two outcomes only:

- `approve for canonical promotion`
- `defer for now`

Use `approve for canonical promotion` when the technique already reads as the natural default within its bounded scope.

Use `defer for now` when the technique is strong and reusable but still reads as an optional companion, a context-shaped pattern, or an under-validated default.

## Review Axes

| axis | approve signal | defer signal |
|---|---|---|
| reuse beyond origin | The technique has clear reuse evidence beyond the first project, or a second context that reinforces the same bounded contract. | Evidence still comes mostly from one origin, or the second context is too thin to show real transfer. |
| stronger validation than initial promotion baseline | Examples, checks, readiness notes, or later reviews show stronger validation than the first promoted bundle alone. | Validation still looks close to the initial promotion floor, with little reinforcement beyond basic structure. |
| clear default-use rationale within bounded scope | The bundle explains when this should be the default choice, and nearby alternatives still have narrower fallback roles. | The technique still reads like one good option among peers, without a crisp reason it should be the default. |
| adaptation notes separate invariant core from project-shaped detail | Adaptation notes make the transferable contract obvious and keep origin-shaped details subordinate. | Adaptation still depends too much on one project's layout, runtime, or operating habits. |
| fresh public-safety recheck | The current public bundle remains sanitized, bounded, and safe to recommend more broadly. | Public-safety questions remain unresolved, or the bundle still carries details that are too project-shaped for wider default recommendation. |

## Metadata Is Informative, Not Decisive

Stage 1 metadata can support canonical review, but it does not decide it.

- `maturity_score` can hint that a technique is approaching canonical strength.
- `validation_strength` can show whether reinforcement moved beyond the first promotion baseline.
- `review_required` can show whether normal adoption still expects explicit human review.
- `export_ready` only concerns Stage 1 catalog publication safety.

None of these fields auto-promote a technique. Canonical promotion still requires an explicit human review outcome.

See also: [CANONICAL_RUBRIC.md](CANONICAL_RUBRIC.md).

## Review Notes

Canonical review should stay bounded and concrete.

- Review the bundle as published today, not an imagined future rewrite.
- Name one recommendation only: approve now or defer for now.
- If deferred, name the smallest concrete remaining gap rather than a broad wish list.
- If approved, make the default-use rationale explicit enough that later reviewers do not have to infer it from scattered notes.

The existing `notes/canonical-readiness.md` surface remains the authoritative place to record bundle-level review outcomes.
