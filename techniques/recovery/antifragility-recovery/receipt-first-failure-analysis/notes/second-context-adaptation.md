# Second Context Adaptation

## Technique
- id: AOA-T-0098
- name: receipt-first-failure-analysis

## Target project
- any owner repo that already has one source-owned receipt surface, one bounded failure family worth reviewing, and one explicit place to record adaptation deltas or follow-up proof

## What changed
- the receipt schema can change
- the stressor family vocabulary can change
- the remediation surfaces can change
- the downstream proof surfaces can change

## What stayed invariant
- review starts from the receipt instead of later summary language
- fact versus hypothesis stays explicit
- the change candidate stays narrow
- the improvement check is named before stronger claims are made

## Risks introduced by adaptation
- a target project may have receipts that are too weak to support useful analysis even though the shape exists
- the pattern can be widened into generic incident review if the bounded family is not named clearly
- downstream proof surfaces can be overused until they eclipse the owner-local receipt

## Evidence
- the origin antifragility landing showed the pattern can stay compact while still producing a reviewable next-step shape
- the receipt-first discipline remained stable even though the surrounding proof and stats layers were intentionally kept downstream

## Result
- the pattern transfers cleanly to other owner repos when receipt ownership is already clear and the review stays bounded to one named failure family
