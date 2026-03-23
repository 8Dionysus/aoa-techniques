---
id: AOA-T-0041
name: skill-marketplace-curation
domain: docs
status: promoted
origin:
  project: n-skills
  path: README.md
  note: Adapted from the open-source n-skills repository, which presents a curated marketplace layer over upstream-owned skills while keeping sync plumbing and installer behavior separate from the discoverability surface.
owners:
  - 8Dionysus
tags:
  - docs
  - skills
  - marketplace
  - discovery
  - curation
summary: Curate a local discoverability layer over upstream-owned skill sources so selection stays editorial and reviewable without pretending the catalog owns sync, capability meaning, or registry policy.
maturity_score: 3
rigor_level: bounded
reversibility: moderate
review_required: true
validation_strength: source_backed
public_safety_reviewed_at: 2026-03-23
export_ready: true
relations:
  - type: complements
    target: AOA-T-0024
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

# skill-marketplace-curation

## Intent

Keep a local skill marketplace or catalog reviewable as a curated discovery layer over upstream-owned skills instead of letting it collapse into raw mirroring, installer behavior, or registry policy.

## When to use

- a repository wants a local discovery surface for upstream-owned skills
- selection quality, grouping, and short descriptions matter as much as raw source availability
- the local layer should add editorial value without claiming upstream skill ownership
- users need one bounded place to browse skill options before reading a specific skill
- the reusable object is curated discoverability rather than sync, health checks, or capability contracts

## When not to use

- the real need is manifest-driven mirroring plus provenance
- the real need is a boundary between reusable skill meaning and command invocation
- the real need is registry generation, installer behavior, or routing policy
- the local collection adds no editorial or discovery value beyond copying upstream entries
- the local layer would become the canonical source of the underlying skills

## Inputs

- one bounded set of upstream-owned skills or skill entries
- one local curation surface such as a catalog, marketplace page, or discovery file
- one explicit rule that upstream ownership remains visible
- one editorial policy for summaries, grouping, or inclusion quality
- one review path that can distinguish curation from raw sync plumbing

## Outputs

- a local discovery layer that helps users browse or inspect upstream-owned skills
- explicit editorial grouping or summaries over the available skill set
- preserved visibility of upstream ownership
- lower pressure to treat the marketplace layer as installer, registry, or sync doctrine
- a clearer boundary between curation and adjacent substrate concerns

## Core procedure

1. Choose the bounded local discovery surface that will present the skill collection.
2. Make upstream ownership readable for every curated entry.
3. Add editorial value through category placement, short summaries, or selection guidance.
4. Keep mirrored payloads, sync manifests, or provenance files outside the center of the curated surface.
5. Keep installer, registry, and command syntax details subordinate to the discovery purpose.
6. Review the collection as an editorial layer: what is included, how it is grouped, and why it is discoverable.
7. If a neighboring concern becomes dominant, split it into a separate technique instead of widening the marketplace layer.

## Contracts

- the local marketplace or catalog is a discoverability layer, not the canonical source of the skills
- upstream ownership remains visible for curated entries
- curation adds editorial value beyond plain mirroring
- category, summary, or selection guidance stays readable without dragging in installer or registry policy
- sync plumbing, provenance substrate, and health checking remain separate sibling concerns
- the technique stays distinct from command-boundary, propagation, routing, and capability-spec ownership

Relationship to adjacent techniques: unlike `AOA-T-0024 upstream-mirroring-with-provenance`, this technique starts after upstream ownership and sync posture are already legible and owns only editorial discoverability. Unlike `AOA-T-0040 skill-vs-command-boundary`, it does not decide where reusable skill meaning stops and command invocation begins. Unlike `AOA-T-0027 cross-agent-skill-propagation`, it does not propagate one source into managed targets. Unlike `AOA-T-0025 capability-spec-versioning`, it does not become the canonical capability-contract surface.

## Risks

### Failure modes

- the curated layer quietly becomes a disguised sync engine or registry
- editorial summaries drift until they misrepresent the upstream skills they are surfacing
- users start treating the marketplace page as if it owns the underlying skill meaning
- categories or featured placement become opaque enough that discovery loses reviewability

### Negative effects

- a curated layer adds maintenance overhead beyond plain mirroring
- editorial selection can create false confidence that omitted skills are lower quality for reasons the surface never explains
- category structures can become stale faster than the underlying skill sources

### Misuse patterns

- widening the bundle into installer behavior, registry generation, or plugin lifecycle semantics
- treating command wrappers as the main curated object instead of the underlying skills
- collapsing curation into raw sync plumbing with no added editorial value
- turning the discovery layer into routing or ranking doctrine

### Detection signals

- the local surface spends more space on install or sync mechanics than on discoverability
- reviewers cannot explain what editorial value the curated layer adds beyond mirroring
- the marketplace page starts reading like the canonical source of capability meaning
- health checks, registry rules, or routing decisions dominate the curation surface

### Mitigations

- keep one explicit sentence that the layer is curated and not canonical
- require visible editorial value such as grouping, summaries, or inclusion rationale
- move sync, provenance, installer, and health details into separate sibling techniques
- review category and summary language whenever the curated entry set changes

## Validation

Verify the technique by confirming that:
- curated entries still show upstream ownership clearly
- the local surface adds editorial discoverability beyond plain mirroring
- installer, sync, registry, and health-check concerns stay outside the main contract
- the curated layer can be reviewed without treating it as the canonical home of skill meaning
- the bundle does not drift into command-boundary, propagation, routing, or capability-spec ownership

See `checks/skill-marketplace-curation-checklist.md`.

## Adaptation notes

What can vary across projects:
- the exact discovery surface format
- whether curation uses categories, tags, featured rows, or short selection blurbs
- the number of curated entries
- how upstream source links are displayed

What should stay invariant:
- the curated layer remains local and editorial
- upstream ownership stays visible
- discoverability stays separate from sync and installer substrate
- the catalog does not become the canonical source of the underlying skills

Project-shaped details that should not be treated as invariant:
- plugin installer commands
- registry payload formats
- sync schedules or GitHub Actions wiring
- exact category taxonomy names
- command or slash-command syntax

## Public sanitization notes

This import keeps only the reusable curation contract: a local marketplace or catalog adds editorial discoverability over upstream-owned skills. Installer flows, registry generation, sync automation, daily schedules, and command syntax details were intentionally left out of the public technique contract.

## Example

See `examples/minimal-skill-marketplace-curation.md`.

## Checks

See `checks/skill-marketplace-curation-checklist.md`.

## Promotion history

- adapted from open-source `n-skills`
- promoted into `aoa-techniques` on 2026-03-23 as a bounded external-import technique for curated local discoverability over upstream-owned skills

## Future evolution

- keep `upstream-skill-health-checking` as the source-readiness sibling rather than widening this bundle into health doctrine
- keep `AOA-T-0024` as the mirroring and provenance sibling rather than turning curation into sync substrate
- add another live context if a second public collection shows the same editorial marketplace boundary without collapsing into registry or installer behavior
