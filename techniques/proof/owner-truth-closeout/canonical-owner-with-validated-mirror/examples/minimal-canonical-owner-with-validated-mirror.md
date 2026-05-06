# Minimal Canonical Owner With Validated Mirror

Use one canonical contract plus one legal mirror.

- canonical copy:
  - lives in the owner repository
  - declares the owning repository explicitly
  - carries the bounded vocabulary that consumers must accept
- mirror copy:
  - names the canonical source explicitly
  - stays byte-for-byte or semantically equivalent on owner metadata and allowed vocabulary
  - does not become the convenient place for local contract edits
- consumer validation:
  - reads the canonical vocabulary
  - rejects unknown tokens before building downstream views

If rollout ordering, owner activation, or live publisher recovery becomes the main problem, treat that as a separate playbook rather than widening this technique.
