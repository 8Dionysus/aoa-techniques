# Offer Evidence Reference Minimal Public-Safe Example

Candidate:
`candidate:aoa-techniques:agon/offer-evidence-reference-practice`

Gate card:
[offer-evidence-reference-practice](../offer-evidence-reference-practice.md)

Status: gate-example-landed, not a technique bundle.

## Public Safety

This example uses a fictional repository review. It contains no private logs,
credentials, operational incidents, user data, live runtime state, proof
verdict, memory write, route decision, or Agon arena action.

## Bounded Frame

Review state:

- claim under review: "the CLI supports a dry-run flag before write actions"
- current evidence: one public docs page mentions `--dry-run`
- available reference: `docs/cli.md#write-actions`, line or excerpt where
  `--dry-run` is documented
- acceptable use: cite the docs as declared interface evidence, not as runtime
  proof that every write path obeys the flag

## Agent Move

The small agent returns one evidence reference:

```text
Evidence reference: `docs/cli.md#write-actions`, the line documenting
`--dry-run` for write actions.

Relevance: this reference supports the claim that the public CLI interface
declares a dry-run flag before write actions.

Scope and limit: it supports documented interface availability. It does not
prove implementation behavior, test coverage, or runtime enforcement.

Review condition: inspect or quote this one reference before relying on it; if
runtime behavior matters, route that later question to a separate validation
check instead of treating this reference as proof.
```

## Why This Is The Atom

The move offers one evidence reference and states its relevance, scope, limit,
and review condition. It does not diagnose the whole change, prove behavior,
rank the source, promote the candidate, write memory, or start a workflow.

## Stop Lines

- Do not define Agon evidence move law.
- Do not issue proof, verdict, route, memory, rank, scar, KAG, ToS, runtime, or
  skill effects.
- Do not treat one reference as final proof.
- Do not turn this example into a technique bundle without a checklist,
  evidence note, and bundle-local review.
