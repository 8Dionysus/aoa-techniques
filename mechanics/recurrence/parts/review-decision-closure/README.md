# Review Decision Closure

This part names how recurrence-fed technique beacons can close as review
decisions without mutating technique status.

Technique beacons may point at candidate intake, overlap holds, or
canonical-pressure surfaces. A decision packet may record `accept`, `reject`,
`defer`, `reanchor`, `split`, `merge`, or `suppress`, but it does not change
technique status by itself.

## Closure Routes

- For `canonical_pressure`, point at the owner review note or
  promotion-readiness matrix followthrough.
- For `new_technique_candidate`, keep SDK lineage provisional until
  `aoa-techniques` assigns a candidate or landed technique ref.
- For `overlap_hold`, keep the hold open until the decision surface names a
  separable atomic move or routes the material away from technique canon.

## Stop-lines

- Do not let a recurrence beacon become review.
- Do not let a generated registry entry become candidate acceptance.
- Do not let a decision packet mutate frontmatter status.
- Do not treat suppress, merge, split, or reanchor as deletion of provenance.

## Provenance

This part preserves the pre-split
`RECURRENCE_REVIEW_DECISION_CLOSURE.md` surface. See
[Provenance](../../PROVENANCE.md).
