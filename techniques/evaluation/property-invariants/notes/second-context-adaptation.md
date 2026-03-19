# Second Context Adaptation

## Technique
- id: AOA-T-0017
- name: property-invariants

## Target project
- name: aoa-techniques
- environment: public documentation repository for reusable engineering techniques
- runtime: human+agent contribution workflow over reviewable repository changes

## What changed
- adaptation path: the invariant-first validation pattern was extracted into one focused public evaluation bundle after the skill-support split rather than remaining implicit inside a broader testing wave
- validation framing: origin-specific validation pressure was rewritten as repo-agnostic invariant language over stable truths, bounded input strategy, and explicit reporting of what the property proves
- support surfaces: the public form now includes a bounded checklist, a minimal example, an origin note, and derived repository manifests
- operating assumptions: contributors need a reusable way to broaden coverage beyond a few fixed examples without hiding the meaning of the invariant behind tool-specific detail

## What stayed invariant
- contract: the technique still starts from one meaningful invariant rather than from random generation by itself
- coverage shape: the goal remains broader behavioral coverage than handpicked examples alone while keeping the input strategy bounded enough to review
- reporting: the result still states what the invariant actually constrains and what remains outside that proof surface

## Risks introduced by adaptation
- the technique can drift into generic "stronger tests" language if future examples stop centering one meaningful invariant and bounded input assumptions
- weak invariants can look impressive in public packaging while failing to constrain real behavior
- overlap pressure with contract-surface validation can blur the pattern if later notes describe broad coverage without keeping the invariant-centered distinction explicit

## Evidence
- The focused landing into `aoa-techniques` kept the pattern separate from boundary-contract validation and bounded execution discipline rather than leaving it inside one mixed skill-support branch.
- The public checklist and minimal example still center invariant strength, bounded input assumptions, and honest reporting instead of treating generator breadth as value by itself.
- The later `Skill-Support Semantic Review` kept `AOA-T-0015` vs `AOA-T-0017` as a watch seam while still preserving `AOA-T-0017` as a distinct invariant-oriented coverage technique.

## Result
- verdict: works
- note: the technique remained distinct and reusable after public shaping into `aoa-techniques` without collapsing into generic contract-test or broad-testing language
