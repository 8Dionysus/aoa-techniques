---
id: AOA-T-0046
name: repo-doc-surface-lift
domain: docs
status: promoted
origin:
  project: aoa-techniques
  path: docs/REPO_DOC_SURFACE_LIFT_GUIDE.md
  note: Extracted from the bounded repo-doc surface guide, manifest, and reader surface to keep public docs/status routing derived from authored markdown without turning the surface into a catch-all taxonomy.
owners:
  - 8Dionysus
tags:
  - docs
  - kag
  - routing
  - repo-docs
  - surface-lift
summary: Lift one bounded set of authoritative repo docs and status files into derived routing knowledge without replacing the authored docs or widening into a docs taxonomy.
maturity_score: 3
rigor_level: bounded
reversibility: easy
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-23
export_ready: true
relations:
  - type: complements
    target: AOA-T-0002
  - type: complements
    target: AOA-T-0009
evidence:
  - kind: origin_evidence
    path: notes/origin-evidence.md
---

# repo-doc-surface-lift

## Intent

Lift the repository's bounded public docs/status layer into derived routing knowledge so readers and tooling can answer "which authored repo doc should anchor this question?" without replacing the authored docs themselves.

## When to use

- the question is about which public repo doc should anchor navigation, contribution, safety, or release/status lookup
- the repository already has a bounded authoritative docs/status set with stable public entrypoints
- a generated routing surface is helpful, but the meaning must still live in authored markdown
- the next step is repo-doc routing, not deeper guide exploration or general documentation taxonomy

## When not to use

- local planning docs such as `TODO.md`, `PLANS.md`, or `ROADMAP.md`
- deeper guide docs beyond the bounded repo-doc source set
- semantic-review or shadow-review docs
- questions about bundle meaning, caution language, or selection beyond the public docs/status layer
- cases where the real need is filesystem-wide doc discovery rather than a bounded repo-doc surface

## Inputs

- one bounded set of authored public repo docs and status files
- a reader surface or manifest projection that stays derived from those docs
- an explicit repo-doc routing question
- agreement that the docs themselves remain authoritative

## Outputs

- bounded routing knowledge for public repo docs/status
- a reader-facing surface that points to the right authored doc
- a stable source set that can be regenerated from markdown
- clear separation between repo-doc routing and deeper docs or planning surfaces

## Core procedure

1. Identify the bounded public docs/status set that is actually in scope.
2. Project only that set into a derived routing surface.
3. Keep the meaning in the authored docs and keep the reader surface subordinate.
4. Route questions about status, contribution, safety, and release back to the right authored document.
5. Exclude local planning, deeper guides, and review surfaces from this route.
6. Regenerate the derived surface from markdown whenever the source set changes.
7. Stop widening the surface when the next question needs a broader docs taxonomy or a policy engine.

## Contracts

- the authored docs remain the source of meaning
- the derived surface stays bounded to the explicit public docs/status set
- repo-doc routing does not become a status-policy engine or a release-policy engine
- local planning docs and deeper guides stay outside this source class
- the technique does not require new schema fields, new frontmatter, or a new `kag` domain

## Risks

### Failure modes

- the bounded docs/status set widens until the surface stops being a clear routing aid
- maintainers start editing the derived surface instead of the authored docs
- the route becomes a catch-all index that pulls in local planning or deeper guides by habit

### Negative effects

- a clean routing surface can create false confidence that the docs layer is more complete than it is
- over-broad doc routing can make the repository feel more systematized than the underlying docs actually are
- the surface can hide that deeper meaning still lives only in authored markdown

### Misuse patterns

- adding `TODO.md`, `PLANS.md`, or `ROADMAP.md` to the public docs/status source set
- using the surface as a status-policy or release-policy engine
- treating the repo-doc surface as a substitute for reading the underlying docs

### Detection signals

- route questions begin requiring unrelated docs to answer
- the derived surface starts listing local planning or review docs
- edits to the generated surface are used to fix meaning instead of regenerating from source markdown
- the surface starts behaving like a general documentation taxonomy rather than a bounded routing layer

### Mitigations

- keep the source set explicit and limited to the public docs/status layer
- route meaning questions back to the authored docs immediately
- exclude local planning and deeper guides from this family
- regenerate the derived surface instead of editing it by hand
- split out a new source class only if a genuinely different docs layer emerges

## Validation

Verify the technique by confirming that:
- the docs/status source set is bounded and explicit
- the derived surface points back to the authored repo docs
- local planning docs and deeper guide docs stay outside the source class
- the routing surface answers "which doc should I open?" rather than "what is the full meaning?"
- no policy engine, taxonomy engine, or filesystem-wide doc discovery behavior is needed

See `checks/repo-doc-surface-lift-checklist.md` and `examples/minimal-repo-doc-surface-lift.md`.
For repo-grounded origin evidence, see `notes/origin-evidence.md`.

## Adaptation notes

What can vary across projects:
- the exact public docs/status files that belong in the bounded source set
- the shape of the reader surface or manifest projection
- the specific repo-doc routing questions the surface should answer

What should stay invariant:
- meaning stays in authored docs
- the surface stays derived and bounded
- local planning docs stay out of this source class
- deeper guide docs stay out unless they become part of a separate bounded source set
- the surface should help navigation, not replace the docs it routes to

This technique stays repo-surface-first. If the next need is deeper guide selection, review semantics, or a general docs taxonomy, that is a different technique family.

## Public sanitization notes

This public version keeps the bounded repo-doc routing contract and removes any project-specific implementation detail beyond the current public docs/status set.

## Example

See `examples/minimal-repo-doc-surface-lift.md`.

## Checks

See `checks/repo-doc-surface-lift-checklist.md`.

## Promotion history

- shaped inside `aoa-techniques` while the repo-doc routing surface and manifest stabilized as a bounded reader companion
- extracted into first public reusable form on 2026-03-23 as a docs-domain source-lift technique

## Future evolution

- clarify when a new public docs/status file should enter the bounded source set
- strengthen second-context evidence once another markdown-first repository reuses the same repo-doc routing pattern
- keep the source set bounded if deeper guides or planning docs start asking for their own route surface
