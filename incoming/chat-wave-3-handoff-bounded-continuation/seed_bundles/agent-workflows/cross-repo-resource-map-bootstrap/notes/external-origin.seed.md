# external-origin seed - cross-repo-resource-map-bootstrap

## Donor spine

- yan5xu/code-relay

## Bounded pattern extracted

- Bootstrap cross-repo work with one explicit map of repos, resources, and their current roles.

## What stays out

- monorepo management doctrine
- general architecture mapping
- platform coordination semantics
- donor runtime behavior

## Why narrower than the donor

- this seed isolates one bounded cross-repo bootstrap map
- it leaves broader coordination systems and architecture views behind
- it does not claim the donor repo should be imported wholesale

## Expected evidence package if landed later

- `TECHNIQUE.md`
- `notes/external-origin.md`
- one minimal example or checklist
- release-path generated surfaces only after source markdown is accepted
