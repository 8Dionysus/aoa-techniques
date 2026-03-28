# Codex Handoff - Personal Ingest Wave 2

You are operating inside `aoa-techniques` under explicit human control.

## Your job

Use the staging surfaces in `incoming/personal-ingest-wave-2/` to help the operator land **one** bounded technique candidate at a time.

## Read first

1. `README.md` at repo root
2. `docs/DONOR_REFINERY_RUBRIC.md`
3. `docs/EXTERNAL_IMPORT_RUNBOOK.md`
4. `TECHNIQUE_INDEX.md`
5. `incoming/personal-ingest-wave-2/docs/EXTERNAL_TECHNIQUE_CANDIDATES_PERSONAL_INGEST_WAVE_2.md`
6. `incoming/personal-ingest-wave-2/docs/PERSONAL_INGEST_WAVE_2_PLANTING_ORDER.md`

## Operating posture

- treat this pack as staging soil, not merge authority
- do not land more than one candidate per pass
- prefer source markdown edits over generated-surface churn
- keep technique wording public-safe, bounded, and donor-narrow
- keep auth, runtime, memory, and scenario doctrine out unless the operator explicitly asks for cross-layer routing notes

## Per-candidate route

For one candidate chosen by the operator:

1. Compare the candidate against `TECHNIQUE_INDEX.md`.
   - name the nearest overlap watch
   - state the sharpest boundary
2. Read the matching seed bundle under `incoming/personal-ingest-wave-2/seed_bundles/...`.
3. Draft the canonical bundle only if the candidate still passes all of these:
   - one bounded reusable pattern
   - plausible public-safe extraction path
   - no unresolved overlap that would widen the contract
   - no new schema or domain required
4. If the candidate still passes:
   - move or rewrite the seed into `techniques/agent-workflows/<slug>/TECHNIQUE.md`
   - create `notes/external-origin.md`
   - keep the smallest honest example and check surface
5. If the candidate does **not** pass:
   - do not force a bundle draft
   - write a blocker note or restaging note instead
6. Before any release-path changes:
   - ask for operator approval
7. After source markdown is accepted:
   - run `python scripts/release_check.py` only if the operator wants validation now

## What to keep out

- secrets
- internal-only paths
- live API credentials
- agent-control doctrine
- remote runtime posture
- automatic memory writeback claims
- unbounded moderation or classification claims

## Desired answer style back to the operator

Always answer in this shape:

- candidate chosen
- overlap watch
- boundary statement
- what stays out
- files you propose to touch
- whether operator approval is needed now
