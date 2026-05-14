# AGENTS.md

## Applies to

This card applies to `examples/` and all descendants unless a nearer
`AGENTS.md` narrows the path.

## Role

`examples/` demonstrates technique use without becoming the technique canon.

Examples should remain minimal, public-safe, and tied to a source technique,
schema, or docs surface. They are allowed to teach, not to invent new doctrine.

Root examples are for repo-wide or public-entry examples. Mechanic-local
examples paired with mechanic schemas belong under
`mechanics/<slug>/parts/<part>/examples/` beside the part that owns and
interprets them.

## Read before editing

Read root `AGENTS.md`, `docs/START_HERE.md`, the source technique, schema, or
docs surface that the example illustrates, and any generated manifest that
indexes examples.

## Boundaries

- Keep the adaptation boundary explicit when an example shows adaptation.
- Put promotion, maturity, or portability claims back into the owning technique
  docs.
- No secrets, real credentials, private repositories, or unreduced session
  transcripts.
- Do not use examples to smuggle mechanic-local contracts into root examples.

## Validation

Verify with:

```bash
python scripts/build_example_manifest.py
python scripts/validate_repo.py
python scripts/validate_semantic_agents.py
```

## Closeout

Report changed examples, owning technique or contract surface, generated
example manifest status, public-safe review, checks run, and checks skipped.
