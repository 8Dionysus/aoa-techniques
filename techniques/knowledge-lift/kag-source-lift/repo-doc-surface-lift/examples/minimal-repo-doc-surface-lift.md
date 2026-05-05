# Minimal Repo Doc Surface Lift

This example shows how a bounded public repo-doc set can become a derived routing surface without replacing the authored docs.

## Bounded source set

- `README.md`
- `docs/START_HERE.md`
- `TECHNIQUE_INDEX.md`
- `AGENTS.md`
- `CONTRIBUTING.md`
- `SECURITY.md`
- `WALKTHROUGH.md`
- `CODE_OF_CONDUCT.md`
- `CHANGELOG.md`
- `docs/README.md`
- `docs/RELEASING.md`

## Example routing

- A new contributor asks where to begin: open `README.md` or `docs/START_HERE.md`.
- Someone wants to understand how to contribute: open `CONTRIBUTING.md`.
- A safety question comes up: open `SECURITY.md`.
- A release question comes up: open `docs/RELEASING.md`.
- Someone wants the public history of changes: open `CHANGELOG.md`.
- A deeper planning question appears: do not route it through this surface; keep it in `TODO.md`, `PLANS.md`, or `ROADMAP.md` outside the source class.

## Anti-drift rule

If the surface starts pulling in planning docs or deeper review guides, it is no longer bounded repo-doc routing.
If a question needs the full meaning of a doc, the reader surface should point back to the authored markdown instead of trying to answer everything itself.
