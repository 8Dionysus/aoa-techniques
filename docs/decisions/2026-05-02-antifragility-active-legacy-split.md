# Antifragility Active Legacy Split

Status: accepted

Date: 2026-05-02

## Context

`mechanics/antifragility/` kept one pre-split flat source,
`CHAOS_WAVE1_PROGRAM.md`, plus a short package README.

`Agents-of-Abyss` owns the center Antifragility mechanic with doctrine, via
negativa, anti-authority rules, fragile-pattern vocabulary, owner map, and
owner request packets. The current AoA queue has no direct
`ORQ-ANTIFRAGILITY-TECHNIQUES-*` request, so `aoa-techniques` should not present
this split as owner-request acceptance.

The local job is narrower: preserve the donor-wave trace while making the
technique-layer stress, degraded-mode, regrounding, and recovery practice route
legible.

## Options Considered

- Keep the flat file in the package root. This would leave donor trace and
  active route mixed together.
- Move the file directly into one active part. This would keep the route short
  but lose the raw donor digest boundary.
- Preserve the file in `legacy/raw/` and distill active parts. This keeps source
  lineage reviewable while giving future work a cleaner active route.

## Decision

Preserve `CHAOS_WAVE1_PROGRAM.md` in `legacy/raw/` and add active package route
files:

- `AGENTS.md`
- `DIRECTION.md`
- `PARTS.md`
- `PROVENANCE.md`
- `LANDING_LOG.md`
- `ROADMAP.md`
- `parts/AGENTS.md`
- `parts/README.md`
- `legacy/AGENTS.md`
- `legacy/README.md`
- `legacy/INDEX.md`
- `legacy/DISTILLATION_LOG.md`
- `legacy/raw/README.md`

Create two active parts:

- `parts/chaos-stress-program/README.md`
- `parts/recovery-practice-bridge/README.md`

Add Antifragility to `mechanics/REQUEST_RECEIPTS.md` only under Non-ORQ Center
Pressure, with `candidate-only` posture.

## Consequences

- The donor pack, donor artifact, and donor digest remain preserved as raw
  provenance.
- Active readers get a shorter route for bounded chaos and stress program
  practice.
- Existing antifragility-recovery bundles remain canonical only through their
  `techniques/**/TECHNIQUE.md` homes.
- AoA doctrine, via negativa, one-score health boundaries, owner-local cleanup,
  proof verdicts, memory truth, stats meaning, playbook choreography, routing
  truth, runtime self-healing, and owner acceptance stay with their owning
  repositories.

## Verification

Verify with:

```bash
python -m unittest tests.test_antifragility_mechanics_topology tests.test_mechanics_request_receipts tests.test_validate_repo
python scripts/validate_repo.py
python -m unittest discover -s tests
```
