# AGENTS.md

## Applies to

This card applies to `examples/` and all descendants unless a nearer
`AGENTS.md` narrows the path.

## Role

`examples/` demonstrates technique use without becoming technique canon.

Examples should remain minimal, public-safe, and tied to a source technique,
schema, docs surface, or generated companion. They are allowed to teach, not to
invent new doctrine.

Root examples are for repo-wide or public-entry examples. Technique-local
examples belong inside the owning technique bundle. Mechanic-local examples
paired with mechanic schemas belong under
`mechanics/<slug>/parts/<part>/examples/` beside the part that owns and
interprets them.

## Read before editing

Read root `AGENTS.md`, `docs/START_HERE.md`, the source technique, schema, or
docs surface that the example illustrates, and any
generated manifest that indexes examples.
Read `README.md` only when the selected task needs its human map; do not preload unrelated maps.

## Boundaries

- Keep the adaptation boundary explicit when an example shows adaptation.
- Put promotion, maturity, or portability claims back into the owning technique
  docs.
- No secrets, real credentials, private repositories, or unreduced session
  transcripts.
- Do not use examples to smuggle mechanic-local contracts into root examples.

## Required Shape

Every root example Markdown file outside `README.md` and `AGENTS.md` must
include:

- `## Source Surfaces`
- `## Demonstrates`
- `## Boundary`
- `## Checks`
- `## Closeout`

The local README must index every root example file.

## Validation

Inherit parent validation: source-fast/generated/release; see [VALIDATION.md](../VALIDATION.md) and config/validation_lanes.json.

## Closeout

Report changed examples, owning technique or contract surface, generated
example manifest status, public-safe review, checks run, and checks skipped.
