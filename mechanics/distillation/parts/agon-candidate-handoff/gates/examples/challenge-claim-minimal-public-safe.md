# Challenge Claim Minimal Public-Safe Example

Candidate:
`candidate:aoa-techniques:agon/challenge-claim-practice`

Gate card:
[challenge-claim-practice](../challenge-claim-practice.md)

Status: gate-example-landed, not a technique bundle.

## Public Safety

This example uses a fictional repository review. It contains no private logs,
credentials, operational incidents, user data, live runtime state, proof
verdict, memory write, route decision, or Agon arena action.

## Bounded Frame

Review state:

- target claim: "the generated docs readers are complete because release check
  passed"
- available context: release check passed, but the claim does not name which
  generated reader contains the new entry
- acceptable pressure: challenge the completeness claim at the reader-coverage
  locus, then ask for one support question
- forbidden move: declare the claim false or demand broad research

## Agent Move

The small agent returns one challenged claim:

```text
Challenge: the claim "the generated docs readers are complete because release
check passed" is too broad for the evidence named so far.

Vulnerable locus: "generated docs readers are complete" needs a reader-level
support surface, not only the aggregate release-check pass.

Pressure reason: a green release check can show the build is valid while still
leaving the reviewer unable to inspect which reader exposes the new entry.

Next support question: name one generated reader or manifest entry that exposes
the new technique, or narrow the claim to "release validation passed."

Stop condition: this is a bounded challenge, not a proof verdict; do not treat
the challenged claim as false unless a separate validation check proves it.
```

## Why This Is The Atom

The move challenges one claim, names one vulnerable locus, states one pressure
reason, and asks one next support question. It does not decide correctness,
rank the claim, write memory, open a route, or start a workflow.

## Stop Lines

- Do not define Agon stance move law.
- Do not issue proof, verdict, route, memory, rank, scar, KAG, ToS, runtime, or
  skill effects.
- Do not turn one challenged claim into a broad debate.
- Do not turn this example into a technique bundle without a checklist,
  evidence note, and bundle-readiness review.
