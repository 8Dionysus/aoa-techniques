# telemetry-integrity-checklist

- required source presence and schema health are checked explicitly
- telemetry or mismatch counters are surfaced in the snapshot
- latest alias and nested history copy are both validated
- anti-double-count rules confirm the history path differs from the latest alias
- optional guardrail consistency is reported explicitly as available, attention, or not available
- the snapshot emits a concise integrity decision with reason codes
- when several latest summaries feed several downstream decisions, the integrity snapshot is preferred over duplicating trust logic inside each consumer
- object-store publication does not remove the need for explicit required-source health, dual-write checks, and anti-double-count checks
- the helper remains diagnostic and read-only rather than creating a hidden hard gate
