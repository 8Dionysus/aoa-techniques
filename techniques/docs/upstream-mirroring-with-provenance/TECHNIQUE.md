---
id: AOA-T-0024
name: upstream-mirroring-with-provenance
domain: docs
status: promoted
origin:
  project: n-skills
  path: README.md
  note: Adapted from the open-source n-skills project, which mirrors externally maintained skills through an explicit source manifest and preserved attribution.
owners:
  - 8Dionysus
tags:
  - docs
  - provenance
  - mirroring
  - sync
  - attribution
summary: Mirror upstream-owned content into a curated local collection through an explicit source manifest and preserved provenance so the local copy stays reviewable without pretending to be the canonical source.
maturity_score: 3
rigor_level: bounded
reversibility: moderate
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-21
export_ready: true
relations:
  - type: complements
    target: AOA-T-0013
evidence:
  - kind: external_origin
    path: notes/external-origin.md
  - kind: second_context
    path: notes/second-context-adaptation.md
  - kind: external_review
    path: notes/external-import-review.md
  - kind: canonical_readiness
    path: notes/canonical-readiness.md
---

# upstream-mirroring-with-provenance

## Intent

Reuse externally maintained content in a local curated collection without losing origin ownership, attribution, or sync discipline.

## When to use

- repositories that curate externally maintained content but do not want each mirrored copy to become a new undocumented local source of truth
- collections that need one explicit manifest showing what is mirrored, from where, and into which local destination
- workflows that want a repeatable resync path plus adjacent provenance metadata for mirrored content
- cases where explicit source ownership matters as much as the local reusable copy

## When not to use

- repositories that need one local canonical source to fan out to several managed targets inside the same project
- workflows where the mirrored copy is expected to become the new primary editable home
- collections that cannot preserve adjacent attribution or source metadata
- cases where the real need is typed note provenance or derived manifest routing rather than content mirroring

## Inputs

- one explicit source manifest naming the upstream repository and mirrored source path
- one local destination for the mirrored copy
- one adjacent provenance signal such as `.source.json` or an equivalent attribution record
- one repeatable sync step that refreshes the local mirror from upstream
- one local editing policy that keeps mirrored content subordinate to upstream ownership

## Outputs

- one local mirrored copy of upstream-owned content
- one explicit provenance record that preserves origin attribution
- one repeatable resync path for refreshing the mirror
- lower ownership ambiguity around what is local curation versus what remains upstream-controlled

## Core procedure

1. Record each upstream source in one explicit source manifest before mirroring content locally.
2. Mirror the upstream content into one bounded local destination.
3. Preserve adjacent provenance metadata so reviewers can trace the local copy back to the upstream source.
4. Treat the mirrored content as curated local copy, not as the new canonical upstream.
5. Re-run the sync step when upstream changes instead of hand-maintaining a divergent local branch by default.
6. Keep any local wrappers or curation notes visibly separate from the mirrored source payload.
7. Review both the mirrored content and the provenance metadata so attribution and ownership remain readable after each refresh.

## Contracts

- the upstream source remains the canonical origin of the mirrored content
- the local copy stays subordinate to explicit upstream ownership
- one source manifest names what is mirrored and where it came from
- adjacent provenance metadata keeps attribution readable after sync
- the sync path can refresh the local copy without erasing source identity
- local curation wrappers stay visibly separate from mirrored source payloads
- this technique does not replace `AOA-T-0013`; it starts when the source of truth is upstream and external rather than local and canonical inside the same repository

## Risks

### Failure modes

- mirrored content drifts because local edits accumulate without a clear resync path back to upstream
- provenance metadata goes stale or disappears, making the local copy look locally authored when it is not
- the source manifest stops matching reality, so mirrored destinations no longer reflect their declared upstreams

### Negative effects

- a local mirror can create false confidence that upstream ownership no longer matters because the copy is convenient and nearby
- frequent syncs can hide whether the local collection still adds meaningful curation or is only accumulating copied payloads
- provenance discipline adds overhead that some teams may quietly bypass once the mirror feels familiar

### Misuse patterns

- treating mirrored local copies as if they were new canonical sources of truth
- widening the technique into marketplace policy, installer behavior, or registry generation instead of keeping it focused on mirroring plus provenance
- using a sync manifest without adjacent attribution, which keeps automation but loses readable source ownership

### Detection signals

- reviewers cannot tell which local content is mirrored and which content is locally authored wrapper or curation
- local edits to mirrored files become common while upstream sync stops being the default refresh path
- the source manifest and provenance files disagree about what was mirrored or from where

### Mitigations

- keep one explicit source manifest and one adjacent provenance signal for every mirrored item
- route upstream-origin changes through resync by default instead of ad hoc local patching
- separate mirrored payloads from local wrapper notes so ownership stays legible
- split registry, installer, or marketplace behavior into separate techniques instead of widening this mirroring contract

## Validation

Verify the technique by confirming that:
- each mirrored item is named in one explicit source manifest
- the local mirror carries adjacent provenance or attribution metadata
- upstream ownership remains readable after sync
- the resync path can refresh mirrored content without hiding where it came from
- local wrappers or curation notes remain separate from mirrored upstream payload

See `checks/upstream-mirroring-with-provenance-checklist.md`.

## Adaptation notes

What can vary across projects:
- the manifest file format
- the exact provenance file name or metadata carrier
- the sync engine or cadence
- the local folder structure used for mirrored content

What should stay invariant:
- upstream ownership stays explicit
- the local copy is mirrored through one declared source manifest
- provenance remains adjacent and readable after sync
- the local mirror stays subordinate to upstream rather than becoming a silent local canonical source

Project-shaped details that should not be treated as invariant:
- marketplace curation policy
- installer or plugin registry behavior
- daily cron scheduling
- category taxonomies or agent compatibility matrices

## Public sanitization notes

This import narrows the donor repository to one docs pattern: upstream mirroring through an explicit source manifest plus preserved provenance. Marketplace policy, daily cron specifics, installer behavior, agent compatibility breadth, category taxonomy, and broader registry generation were intentionally left out of the public technique contract.

## Example

See `examples/minimal-upstream-mirroring-with-provenance.md` and `examples/concrete-curated-mirror-with-attribution.md`.

## Checks

See `checks/upstream-mirroring-with-provenance-checklist.md`.

## Promotion history

- adapted from open-source `n-skills`
- promoted into `aoa-techniques` on 2026-03-21 as a bounded external-import technique for source-manifest-driven mirroring with explicit provenance

## Future evolution

- split out a dedicated marketplace-catalog sibling if curated discovery policy proves reusable without the rest of the sync contract
- split out a dedicated derived-attribution-manifest sibling if provenance projection becomes reusable beyond mirrored content collections
- add a stronger second live context if another public repository adopts the same upstream-mirroring and provenance contract
