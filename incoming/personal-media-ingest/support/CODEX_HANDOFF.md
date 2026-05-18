# Codex Handoff - Personal Media Ingest

You are operating inside `aoa-techniques` under explicit human control.

## Your job

Use the evidence surfaces in `incoming/personal-media-ingest/` to inspect the
landed media-ingest wave and the closed auth/session non-import verdict. The
first-pass landing queue is closed.

## Read first

1. `README.md` at repo root
2. `mechanics/distillation/parts/donor-refinery/README.md`
3. `mechanics/distillation/parts/external-import-runbook/README.md`
4. `TECHNIQUE_INDEX.md`
5. `incoming/personal-media-ingest/docs/EXTERNAL_TECHNIQUE_CANDIDATES_PERSONAL_MEDIA_INGEST.md`
6. `incoming/personal-media-ingest/docs/PERSONAL_MEDIA_INGEST_PLANTING_ORDER.md`

## Operating posture

- treat this packet as evidence, not merge authority
- do not land candidates from this closed packet
- prefer source markdown edits over generated-surface churn
- keep technique wording public-safe, bounded, and donor-narrow
- keep auth, runtime, memory, and scenario doctrine out unless the operator explicitly asks for cross-layer routing notes
- do not recreate packet-local seed bundles for already landed `AOA-T-0070` through `AOA-T-0074`

## New Intake Route

For the closed auth/session bridge:

1. Read `docs/TELEGRAM_ACCOUNT_AUTH_AND_SESSION_BRIDGE_CLOSEOUT_MEMO.md`.
2. Compare the proposed smaller seam against `TECHNIQUE_INDEX.md`,
   `docs/TECHNIQUE_ATOM_CONTRACT.md`, and `docs/TECHNIQUE_TOPOLOGY_CONTRACT.md`.
3. Do not create a candidate bundle unless a new Distillation pass is
   explicitly approved and the bridge can name one bounded public-safe artifact
   contract from fresh evidence.
4. Keep auth, session-secret, runtime control, and memory-writeback doctrine
   out unless a stronger owner supplies a clean public contract.

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

- candidate or closed verdict chosen
- overlap watch
- boundary statement
- what stays out
- files you propose to touch
- whether a new intake is justified now
