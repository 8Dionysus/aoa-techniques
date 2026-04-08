# Technique Kind Guide

This is the living doctrine for the `kind` axis in `aoa-techniques`.

Use it when you are writing, reviewing, or selecting a technique and need the bounded second cut after `domain`.

See also:

- [Technique Selection Guide](TECHNIQUE_SELECTION_GUIDE.md)
- [Technique Selection](TECHNIQUE_SELECTION.md)
- [Technique Kinds Seed](TECHNIQUE_KINDS_SEED.md)
- [`../config/technique_kind_registry.yaml`](../config/technique_kind_registry.yaml)
- [`../data/technique_kind_wave1.yaml`](../data/technique_kind_wave1.yaml)
- [`../reports/wave1_kind_counts.md`](../reports/wave1_kind_counts.md)
- [`../generated/technique_catalog.min.json`](../generated/technique_catalog.min.json)

## Core Doctrine

- `domain` stays the ownership and first-routing axis.
- `kind` is the bounded second selector axis inside that owner layer.
- Each technique chooses exactly one primary `kind`.
- Use `tags` for extra nuance instead of widening `kind`.
- Keep `family` scout-only and non-authoritative in this wave.

## How To Choose

Pick the narrowest honest `kind` that helps a selector understand default use.

If two kinds feel plausible, use the registry tie-break rules:

- `workflow` vs `guardrail`: choose `workflow` for stepwise doing, `guardrail` for stopping, narrowing, or approving.
- `validation` vs `assessment`: choose `validation` for proof or integrity evidence, `assessment` for classification or diagnosis.
- `artifact` vs `lift`: choose `artifact` for the primary durable shape, `lift` for a weaker derived surface from stronger source material.
- `composition` vs `distribution`: choose `composition` when parts become one result, `distribution` when one source fans out to many targets.
- `handoff` vs `workflow`: choose `handoff` when continuation across a seam is the main contract, `workflow` when the work loop itself is the main contract.

`ingest` stays reserved for raw external inputs that are being normalized into reviewable intermediates.

## Review Rules

- Reviewers should check that the selected `kind` is singular and narrow.
- Reviewers should prefer registry-backed tie-breaks over local intuition when the choice is close.
- Reviewers should not use `kind` as a status, score, or promotion signal.
- Reviewers should send cluster questions to `family` only as scout notes, not as frontmatter truth.

## Current Source Files

The current canonical sources for this axis are:

- `config/technique_kind_registry.yaml`
- `data/technique_kind_wave1.yaml`
- `reports/wave1_kind_counts.md`

The living corpus still belongs in the technique bundles and generated catalog. This guide only defines how to choose and review the axis.
