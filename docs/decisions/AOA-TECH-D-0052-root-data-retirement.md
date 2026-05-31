# Root Data Retirement

Date: 2026-05-14

Status: accepted

## Index Metadata

- Decision ID: AOA-TECH-D-0052
- Original date: 2026-05-14
- Surface classes: root/topology
- Technique axes: topology
- Mechanic parents: none
- Guard families: root surface
- Posture: accepted

## Context

After the technique-reform scout inputs moved into the Distillation
`technique-reform-ingress` part, root `data/` contained only its route card.
No active repo-wide dataset, authored corpus, generated companion, schema
contract, example packet, or preserved receipt still required that district.

Keeping an empty root `data/` reservation makes later mechanics work look like
it has a ready root shelf even when a stronger owner home exists.

## Decision

Delete root `data/` and remove it from the allowed root district list and
semantic AGENTS validator.

Future data-like material should choose the stronger owner home first:

- `mechanics/<slug>/parts/<part>/data/` for mechanic-local inputs or overlays
- `legacy/` for public-safe preserved repo-wide receipts or archive material
- `generated/` for reproducible derived outputs
- `schemas/` for repo-wide machine contracts
- `examples/` for repo-wide public example packets

Root `data/` may be reintroduced only by a new decision when a concrete
repo-wide data contract exists and no stronger existing district fits.

## Consequences

- The repository root no longer advertises an unused data shelf.
- `scripts/validate_semantic_agents.py` no longer requires `data/AGENTS.md`.
- Mechanic-local and generated data pressure is routed to owner homes instead
  of an empty root district.

## Verification

```bash
python scripts/validate_semantic_agents.py
python scripts/validate_repo.py
python scripts/release_check.py
git diff --check
```
