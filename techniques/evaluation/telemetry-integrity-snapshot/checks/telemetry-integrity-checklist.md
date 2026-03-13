# telemetry-integrity-checklist

- required source presence and schema health are checked explicitly
- telemetry or mismatch counters are surfaced in the snapshot
- latest alias and nested history copy are both validated
- anti-double-count rules confirm the history path differs from the latest alias
- optional guardrail consistency is reported explicitly as available, attention, or not available
- the snapshot emits a concise integrity decision with reason codes
- the helper remains diagnostic and read-only rather than creating a hidden hard gate
