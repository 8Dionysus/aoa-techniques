# Minimal Doc Routing

This example shows how a repository can route common updates without duplicating status across many files.

## Document map

- `README` keeps a short project overview and links to canonical docs.
- `MANIFEST` keeps a compact machine/human snapshot.
- `TODO` tracks active work.
- `PLANS` tracks goals, milestones, and risks.
- `DECISIONS` records architecture and policy changes.
- `RUNBOOK` stores runnable commands and operating procedures.
- `SESSION_2026-03-13` stores detailed run history for the day.

## Example routing

- A new architectural rule is added: write it to `DECISIONS`.
- The startup command changes: update `RUNBOOK`.
- The team begins a new active task: update `TODO`.
- A milestone moves from planned to complete: update `PLANS`.
- A smoke run finishes and produces detailed notes: append the result to `SESSION_2026-03-13`.
- The top-level project status changes: keep the summary short in `README` or `MANIFEST` and link to the detailed docs instead of copying long history.

## Anti-drift rule

If the same status paragraph starts appearing in `README`, `TODO`, and `PLANS`, move the detail back to its canonical home and leave only short references elsewhere.
