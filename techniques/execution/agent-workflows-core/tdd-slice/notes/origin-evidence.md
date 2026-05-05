# Origin Evidence

## Technique
- id: AOA-T-0014
- name: tdd-slice

## Source project
- name: atm10-agent
- source files:
  - `atm10-agent/planning-layer/`
  - `atm10-agent/docs/`

## Evidence
- The origin repeatedly needed one bounded implementation slice that could be described in reviewable behavior language before any code was changed.
- The same planning-layer work kept the discipline narrow: write or update the relevant test surface first, implement the smallest passing change, and defer unrelated cleanup to a separate follow-up.
- The origin pressure was specifically human+agent collaboration, where a test-first slice acted as a compact executable contract instead of a long speculative implementation plan.
- Across those uses, the main reusable invariant stayed stable: behavior framing first, minimal implementation second, bounded refactor only after the slice is green.

## Interpretation
- The origin proves this technique as a reusable bounded-change workflow: TDD is valuable here not as ritual, but as a way to keep one behavior slice explicit, reviewable, and resistant to scope drift.
