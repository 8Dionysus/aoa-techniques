# required-vs-optional-rendering-checklist

- required source set and optional source set are documented explicitly
- required missing sources are reported separately from optional missing sources
- required-source failure can fail smoke or strict contract checks
- missing optional sources render as `not available yet`
- invalid optional sources produce warnings without taking down the full surface
- soft-info artifacts such as `brief_md` remain non-blocking unless explicitly promoted
- optional-source tolerance remains observable in non-UI consumers such as JSON reports or CLI summaries
- the surface stays read-only and summary-driven
