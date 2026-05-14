# AGENTS.md

## Guidance for `examples/`

`examples/` demonstrates technique use without becoming the technique canon.

Examples should remain minimal, public-safe, and tied to a source technique, schema, or docs surface. They are allowed to teach, not to invent new doctrine.

Root examples are for repo-wide or public-entry examples. Mechanic-local
examples paired with mechanic schemas belong under
`mechanics/<slug>/parts/<part>/examples/` beside the part that owns and
interprets them.

When an example shows an adaptation, keep the adaptation boundary explicit. Put promotion, maturity, or portability claims back into the owning technique docs.

No secrets, real credentials, private repositories, or unreduced session transcripts.

Verify with:

```bash
python scripts/validate_repo.py
python scripts/validate_semantic_agents.py
```
