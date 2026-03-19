# Second Context Adaptation

## Technique
- id: AOA-T-0015
- name: contract-test-design

## Target project
- name: aoa-techniques
- environment: public documentation repository for reusable engineering techniques
- runtime: human+agent contribution workflow over reviewable repository changes

## What changed
- adaptation path: the origin-specific boundary pattern was extracted from a larger draft wave into one focused promoted evaluation bundle
- boundary surface: project-specific service and workflow edges were rewritten as repo-agnostic contract framing over observable inputs, outputs, and failure behavior
- support surfaces: the public form now includes an explicit checklist, a minimal boundary example, an origin note, and derived repository manifests
- operating assumptions: downstream expectations must be reviewable in public-safe language rather than carried implicitly in private implementation context

## What stayed invariant
- contract: the important validation surface is still the consumer-visible boundary rather than hidden internals
- reasoning: downstream assumptions remain explicit when they materially shape the contract
- reporting: the result still states what the contract guarantees and what remains outside that guarantee

## Risks introduced by adaptation
- the technique can drift into generic "stronger tests" language if future examples stop centering one observable boundary
- overlap pressure with invariant-oriented validation can blur the pattern if later notes describe broad coverage instead of contract-surface guarantees
- public generalization can weaken the role of downstream consumers if future wording keeps only the interface shape and drops the consumer perspective

## Evidence
- The focused landing into `aoa-techniques` kept the pattern separate from both bounded execution discipline and invariant-oriented coverage broadening.
- The public checklist and minimal example still center observable contract behavior, downstream assumptions, and refactor freedom behind the boundary.
- The later `Skill-Support Semantic Review` kept `AOA-T-0015` distinct as a boundary-contract technique and identified its watch seam with `AOA-T-0017` without collapsing the two patterns.

## Result
- verdict: works
- note: the technique remained distinct and reusable after public bundle shaping into `aoa-techniques`
