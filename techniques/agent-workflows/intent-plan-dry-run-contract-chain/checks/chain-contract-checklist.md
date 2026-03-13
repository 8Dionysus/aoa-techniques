# Chain Contract Checklist

Use this checklist to validate whether a workflow really follows `intent-plan-dry-run-contract-chain`.

- The intent payload is well-formed and validated before planning.
- A normalized plan artifact is written.
- The execution step is dry-run only and performs no real side effects.
- Chain artifacts such as `run.json`, plan output, and summary files exist.
- Contract-check validates expected intent routing or equivalent dispatch rules.
- Exit behavior is explicit.
- Traceability metadata is preserved when required.
