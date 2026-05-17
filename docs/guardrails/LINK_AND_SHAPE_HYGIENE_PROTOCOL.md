# Link And Shape Hygiene Protocol

This protocol keeps local links, Markdown shape, and moved-path repairs
checkable inside `aoa-techniques`.

It does not author technique meaning, review doctrine, mechanic truth, or
generated-output meaning. It only protects the map so readers and agents can
reach the stronger source.

## Scope

This protocol covers these failure modes:

- local Markdown links that point to files or directories that no longer exist
- old flat `docs/*.md` links after a guide family moves into a district
- route surfaces that cite concrete targets as inert code spans instead of
  active links
- generated reader companions that stop linking back to authored source
  contracts
- new docs districts added without route guidance or validation pressure

External links are outside this guardrail. They may be reviewed separately, but
this repository's local hygiene gate does not fetch the network.

## Local Link Law

Local links should point to the nearest stable owner surface.

A local Markdown link is valid when:

1. the target path exists inside the repository;
2. the target does not escape the repository root;
3. generated readers link back to authored source contracts;
4. historical references are either preserved as legacy material or left as
   non-link provenance when they intentionally point to another repository.

When a guide family moves, update active links to the new district path in the
same change. Do not leave compatibility stubs in flat `docs/` unless a current
consumer truly requires them.

## Shape Law

Entry and district surfaces should remain readable:

- one top-level heading
- stable second-level sections when the surface has more than one role
- final newline
- no giant one-line public entry documents
- no generated reader edited by hand when a builder owns it

Shape checks are deliberately narrow for now. Add stricter machine checks only
when a real recurring failure needs enforcement.

## Guarded Surfaces

The active local-link check covers root Markdown files and `docs/**/*.md`.
It intentionally excludes external URL health and legacy-path interpretation.

For broader generated freshness, use the source builders and release check named
by [AGENTS](AGENTS.md#validation).

## Check Route

Use [Hygiene Guardrail Index](HYGIENE_GUARDRAIL_INDEX.md) for the current check
lane and [AGENTS](AGENTS.md#validation) for executable commands.
