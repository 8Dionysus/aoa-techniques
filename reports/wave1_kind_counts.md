# Wave1 kind counts

This report is a seed-side sanity check over the current published catalog mapping.

## Counts by kind

| kind | count |
|---|---:|
| `workflow` | 11 |
| `guardrail` | 11 |
| `validation` | 10 |
| `composition` | 7 |
| `distribution` | 4 |
| `artifact` | 14 |
| `lift` | 11 |
| `discovery` | 2 |
| `handoff` | 11 |
| `ingest` | 5 |
| `assessment` | 9 |
| `recovery` | 3 |

## Counts by domain and kind

| domain | workflow | guardrail | validation | composition | distribution | artifact | lift | discovery | handoff | ingest | assessment | recovery |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agent-workflows | 11 | 6 | 1 | 3 |  | 1 | 2 |  | 11 | 5 | 9 | 2 |
| docs |  | 3 |  | 4 | 4 | 6 | 8 | 2 |  |  |  |  |
| evaluation |  | 2 | 8 |  |  | 1 | 1 |  |  |  |  |  |
| history |  |  |  |  |  | 6 |  |  |  |  |  |  |
| system-recovery |  |  |  |  |  |  |  |  |  |  |  | 1 |
| validation-patterns |  |  | 1 |  |  |  |  |  |  |  |  |  |

## Largest optional families

| family | count |
|---|---:|
| `kag-source-lift` | 8 |
| `instruction-surface` | 7 |
| `handoff-continuation` | 7 |
| `history-artifacts` | 6 |
| `agent-workflows-core` | 5 |
| `media-ingest` | 5 |
| `automation-governance` | 5 |
| `owner-truth-closeout` | 5 |
| `docs-boundary` | 4 |
| `published-summary` | 4 |
| `runtime-truth-lifecycle` | 4 |
| `donor-harvest` | 4 |
| `diagnosis-repair` | 4 |
| `evaluation-chain` | 3 |
| `skill-support` | 3 |
| `capability-registry` | 3 |
| `capability-boundary` | 3 |
| `ready-work-graphs` | 3 |
| `review-compaction` | 3 |
| `decision-routing` | 3 |
| `intent-chain` | 2 |
| `skill-discovery` | 2 |
| `approval-evidence` | 2 |
| `antifragility-recovery` | 2 |
| `tool-gateway` | 1 |

## Notes

- `kind` is intentionally broader than `family`.
- small counts for `discovery` and `recovery` are acceptable because they describe narrower reusable postures, not failure of the axis.
- if any family feels too coarse during landing, adjust the family seed first instead of widening `kind`.
