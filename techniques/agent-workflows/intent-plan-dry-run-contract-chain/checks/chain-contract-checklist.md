# Chain Contract Checklist

Use this checklist to validate whether a workflow really follows `intent-plan-dry-run-contract-chain`.

- The intent payload is well-formed and validated before planning.
- A normalized plan artifact is written.
- The plan artifact exists before dry-run execution starts.
- The execution step is dry-run only and performs no real side effects.
- Chain artifacts such as `run.json`, plan output, link summary, and contract summary exist.
- Contract-check reads artifacts directly rather than depending on log scraping.
- Contract-check validates expected intent routing or equivalent dispatch rules.
- Required traceability metadata is preserved and surfaced when policy requires it.
- Missing artifacts or routing mismatches produce an explicit fail verdict.
- Exit behavior is explicit and blocks progression to any real execution path.
