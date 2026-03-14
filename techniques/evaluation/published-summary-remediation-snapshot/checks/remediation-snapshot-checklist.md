# remediation-snapshot-checklist

- reads only latest published summary aliases
- does not replay history or recompute trend state
- uses one fixed documented bucket set
- applies an explicit cap to each bucket
- reports missing or stale inputs explicitly
- keeps source summary references on emitted candidates
- the same cap, determinism, and source-traceability rules still hold when latest summaries are published as object-store keys
- remains read-only with respect to source artifacts and upstream behavior
