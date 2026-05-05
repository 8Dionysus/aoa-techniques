# minimal-lightweight-snapshot

This example shows how a repository can keep top-level status docs lightweight without losing operational detail.

## `README`

- one-sentence project description
- quick links to `TODO`, `PLANS`, `RUNBOOK`, `DECISIONS`, and the latest session snapshot
- 5-10 short current-status bullets
- no long run lists or copied metric history

## `MANIFEST`

- current date
- target platform or runtime
- active capabilities
- canonical docs map
- short data or commit policy

## Canonical detail stays elsewhere

- active execution state lives in `TODO`
- goals and milestones live in `PLANS`
- runnable commands live in `RUNBOOK`
- architecture and policy changes live in `DECISIONS`
- detailed chronology and run evidence live in `SESSION_*`

## Anti-drift rule

If a top-level snapshot starts collecting long test counts, many run IDs, or detailed troubleshooting notes, move that detail back to its canonical document and leave only a short link or summary line.
