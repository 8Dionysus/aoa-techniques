# external-origin seed - local-first-session-index

## Donor spine

- wesm/agentsview

## Bounded pattern extracted

- Build a local searchable index over already-saved session artifacts and keep references back to the source artifacts.

## What stays out

- session capture behavior
- cloud memory or recall systems
- hosted dashboard doctrine
- donor product semantics

## Why narrower than the donor

- this seed isolates one local indexing surface over existing artifacts
- it leaves capture, cloud sync, and wider product behavior behind
- it does not claim the donor repo should be imported wholesale

## Expected evidence package if landed later

- `TECHNIQUE.md`
- `notes/external-origin.md`
- one minimal example or checklist
- release-path generated surfaces only after source markdown is accepted
