# fail-closed-evidence-gate checklist

- [ ] the gate sits directly before a real mutating or side-effect boundary
- [ ] non-allow verdicts actually block side effects rather than only warning
- [ ] explicit allow is required before execution continues
- [ ] one evidence artifact survives the verdict with enough context for later review
- [ ] the example stays smaller than a full policy platform, durable-job system, or witness-trace stack
- [ ] human confirmation, trace signing, and broader governance semantics stay outside the invariant core
- [ ] ambiguous verdicts are not treated as allow by default
- [ ] the public wording remains reusable and sanitized
