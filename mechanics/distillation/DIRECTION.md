# Distillation Direction

## Current intent

Distillation in `aoa-techniques` is the reusable-practice intake mechanic. It
receives donor pressure, cross-layer notes, and long-gap backlog material, then
decides whether the material should become:

- a candidate ledger entry
- a bounded import runbook path
- a long-gap reentry requirement
- an overlap hold
- a real `techniques/` bundle through the normal review path

The mechanic preserves provenance while keeping current behavior in active
parts.

## Current route

1. Use [Donor Refinery](parts/donor-refinery/README.md) to decide what can be
   extracted without importing foreign doctrine.
2. Use [Candidate Intake](parts/candidate-intake/README.md) for active
   public-safe candidate packets before ledger, import, hold, bundle, or
   archive routing.
3. Use [External Import Runbook](parts/external-import-runbook/README.md) only
   after the donor already looks like a bounded technique candidate.
4. Use [External Candidate Ledger](parts/external-candidate-ledger/README.md)
   for public-safe external candidate accounting.
5. Use [Cross-Layer Candidate Ledger](parts/cross-layer-candidate-ledger/README.md)
   for sibling-repo donor-note accounting.
6. Use [Agon Candidate Handoff](parts/agon-candidate-handoff/README.md) when
   Agon requested-only candidates need Distillation lanes and gate cards before
   any bundle draft.
7. Use [Technique Reform Ingress](parts/technique-reform-ingress/README.md)
   when accumulated topology evidence needs a bounded entry route before future
   classification reform.
8. Use [Long-Gap Reentry](parts/long-gap-reentry/README.md) when old promoted
   material needs a new external contract before another honest canonical pass.

## Boundaries

Distillation does not mint canon by itself. It can name readiness, blocker,
hold, or source pressure, but a promoted or canonical technique still needs the
bundle-local evidence and validation expected by `aoa-techniques`.

Distillation also does not absorb the owning layer of the donor. Skills stay in
`aoa-skills`, eval doctrine stays in `aoa-evals`, role contracts stay in
`aoa-agents`, routing stays in `aoa-sdk`, memory stays in `aoa-memo`, and
center doctrine stays in `Agents-of-Abyss`.

## Current structural posture

The first active split moved five formerly flat distillation files into
part-local homes. Their verdicts and candidate accounting were not rewritten.
That keeps the current project reality intact while creating the same kind of
active/parts/provenance route used by the mature mechanics packages.

The next work should distill one part at a time instead of flattening the whole
candidate universe in one pass.
