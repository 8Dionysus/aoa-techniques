# Request Evidence Minimal Public-Safe Example

Candidate:
`candidate:aoa-techniques:agon/request-evidence-practice`

Gate card:
[request-evidence-practice](../request-evidence-practice.md)

Status: gate-example-landed, not a technique bundle.

## Public Safety

This example uses a fictional repository review. It contains no private logs,
credentials, operational incidents, user data, live runtime state, proof
verdict, memory write, route decision, or Agon arena action.

## Bounded Frame

Review state:

- claim under review: "the generated compact index was rebuilt after the seed
  registry changed"
- current evidence: the diff shows both seed and generated files changed
- missing evidence: the command receipt for the builder check
- acceptable object: one terminal receipt or CI check line showing the builder
  ran with `--check` against the current branch

## Agent Move

The small agent returns one evidence request:

```text
Please provide the builder-check receipt for the generated compact index.

Evidence object: the command output or CI line for
`python path/to/build_registry.py --check` on the current branch.

Why it matters: the diff shows the source and generated files changed, but this
does not prove the generated index is derived from the current seed rather than
edited by hand.

Return condition: if the receipt passes, the review state can move from
"missing generation evidence" to "generation check observed"; if the receipt is
unavailable, keep the generated index under review and do not treat it as
validated.
```

## Why This Is The Atom

The move asks for one missing evidence object. It does not diagnose the whole
change, judge correctness, ask for broad research, issue proof, promote the
candidate, or start a workflow.

## Stop Lines

- Do not define Agon evidence move law.
- Do not issue proof, verdict, route, memory, rank, scar, KAG, ToS, runtime, or
  skill effects.
- Do not request every possible evidence source when one receipt is enough.
- Do not turn this example into a technique bundle without a checklist,
  evidence note, and bundle-local review.
