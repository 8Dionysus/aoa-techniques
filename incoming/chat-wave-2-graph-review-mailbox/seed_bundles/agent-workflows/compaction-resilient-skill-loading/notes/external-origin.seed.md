# external-origin seed - compaction-resilient-skill-loading

## Donor spine

- joshuadavidthomas/opencode-agent-skills

## Bounded pattern extracted

- Preserve or reload bounded skill availability after session compaction from a canonical source.

## What stays out

- full context composition doctrine
- unmanaged prompt stuffing
- donor product semantics
- general memory behavior

## Why narrower than the donor

- this seed isolates one post-compaction skill recovery seam
- it leaves general context management and broader product behavior behind
- it does not claim the donor repo should be imported wholesale

## Expected evidence package if landed later

- `TECHNIQUE.md`
- `notes/external-origin.md`
- one minimal example or checklist
- release-path generated surfaces only after source markdown is accepted
