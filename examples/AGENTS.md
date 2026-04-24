# AGENTS.md

## Guidance for `examples/`

`examples/` demonstrates technique use without becoming the technique canon.

Examples should remain minimal, public-safe, and tied to a source technique, schema, or docs surface. They are allowed to teach, not to invent new doctrine.

When an example shows an adaptation, keep the adaptation boundary explicit. Put promotion, maturity, or portability claims back into the owning technique docs.

No secrets, real credentials, private repositories, or unreduced session transcripts.

Verify with:

```bash
python scripts/validate_repo.py
python scripts/validate_semantic_agents.py
```
