# Origin Evidence

## Technique
- id: AOA-T-0017
- name: property-invariants

## Source project
- name: atm10-agent
- source files:
  - `atm10-agent/planning-layer/`
  - `atm10-agent/docs/`

## Evidence
- The origin repeatedly needed a stronger validation surface than a few handpicked examples when behavior had to remain true across a wider input or state space.
- The same planning-layer work kept reusing one pattern: identify the domain truth that should stay stable, encode it as an invariant-oriented check, and keep the input strategy explicit enough for review.
- In those uses, the reusable value did not come from random generation by itself; it came from expressing a meaningful invariant that constrained future regressions across many cases.
- Across repeated uses, the stable invariant-first discipline remained the same: choose the domain truth carefully, keep the generator or repeated input surface bounded, and report what the property truly proves.

## Interpretation
- The origin proves this technique as a reusable evaluation pattern for broader behavioral coverage: invariants are valuable here because they express stable truths that should survive beyond a narrow example list.
