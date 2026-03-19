# Adverse Effects Review

## Technique
- id: AOA-T-0001
- name: plan-diff-apply-verify-report

## Review focus
- current role: default safe workflow for non-trivial agent or human-plus-agent changes
- current watch seam: keep concrete verification stronger than ceremony and keep the report subordinate to the diff

## Failure modes
- validation becomes symbolic while the workflow still reports success
- the plan and report stay present even when the real diff no longer proves the stated scope

## Negative effects
- full workflow ceremony can slow low-risk edits that do not need the same safety loop
- reporting overhead can crowd out direct diff readability if the summary becomes the main review surface

## Misuse patterns
- applying the full workflow to trivial wording or formatting edits by habit
- treating the final report as a substitute for a readable diff and named validation evidence

## Detection signals
- success reports describe validation generically instead of naming concrete checks and results
- contributors invoke the full workflow for edits with no meaningful operational consequence

## Mitigations
- use a lighter workflow when the change has no meaningful operational impact
- require validation lines to name what ran and what result was observed before the change is treated as complete

## Recommendation
- keep current `canonical` status and use this note as the watch surface for ceremony creep or symbolic `VERIFY` language
