# gate-promotion-checklist

- signal-only mode publishes machine-readable output
- strict mode is introduced only on an explicit enforcement surface
- readiness uses history rather than a single run
- governance makes `go` or `hold` explicit
- progress reports the remaining gap to promotion
- diagnostics still publish when the strict surface fails
- non-promoted surfaces do not silently inherit strict failure behavior
