# Contributing to aoa-techniques

Thank you for contributing.

## What belongs here

Good contributions:
- reusable agent workflows
- validation patterns
- safe operational techniques
- documentation patterns
- evaluation and monitoring loops
- cross-repo transfer patterns
- infra safety patterns

Bad contributions:
- random snippets
- private hacks without generalization
- internal-only assumptions
- undocumented scripts
- techniques with no clear validation path

## Before opening a PR

Please make sure:
- the technique is sanitized
- the technique has a clear purpose
- the technique includes a canonical `TECHNIQUE.md`
- examples are public-safe
- risks are documented
- validation exists as a check, smoke, or checklist
- maturity status is set correctly
- origin is stated clearly

## Preferred PR scope

Prefer:
- 1 technique per PR
- or 1 maturity/status transition per PR
- or 1 focused improvement to an existing technique

## Recommended PR title format

- `technique: add <technique-name>`
- `technique: improve <technique-name>`
- `technique: promote <technique-name> to canonical`
- `technique: deprecate <technique-name>`
- `docs: refine templates`
- `repo: improve validation rules`

## Review criteria

PRs are reviewed for:
- reusability
- clarity
- public safety
- validation quality
- adaptation quality
- maturity correctness
- coherence with repository philosophy

## Status transitions

### promoted -> canonical
Should usually demonstrate all of the following:
- reuse evidence beyond the origin project, ideally a second real context
- stronger validation than the initial promotion baseline
- a clear reason the technique should be recommended by default
- adaptation notes that separate invariant core from project-shaped details
- a fresh public-safety review confirming sanitization still holds

Do not mark a technique `canonical` based only on abstraction or preference.

### canonical -> deprecated
Requires:
- a reason
- a replacement if available
- a brief note in index or technique history

## Security

If your contribution reveals a leak, secret, or security-sensitive detail,
do not open a public issue. Use the process in `SECURITY.md`.
