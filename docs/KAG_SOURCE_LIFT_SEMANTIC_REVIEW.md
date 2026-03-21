# KAG Source Lift Semantic Review

This review-only pilot checks whether the first reusable KAG/source-lift family still reads as five distinct techniques rather than one blurred "lift everything from markdown" package.

Why this family was chosen now:

- the family now has two `canonical` anchors plus three `promoted` companions
- the family now spans section lift, metadata spine, provenance lift, relation lift, and markdown-first caution lift
- the main question is semantic clarity across the family boundaries, not missing structure
- `AOA-T-0022` is a caution-oriented companion and should stay outside shadow-policy semantics

This doc is a human review surface. It does not change statuses, frontmatter, validator behavior, or bundle contracts by itself.

## Family Map

| technique | current role |
|---|---|
| [AOA-T-0018](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) | section-first markdown lift for stable `TECHNIQUE.md` headings |
| [AOA-T-0019](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) | bounded metadata spine for bundle routing and derived catalog lookup |
| [AOA-T-0020](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) | typed evidence-note provenance handles without note-graph semantics |
| [AOA-T-0021](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) | direct relation hints without graph traversal or rationale expansion |
| [AOA-T-0022](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) | markdown-first caution lookup over `Risks` and adverse-effects review surfaces |

## Seam Review

### `AOA-T-0018` vs `AOA-T-0019`

Question: where does section lift stop and metadata-spine routing begin?

- Invariant boundary: [AOA-T-0018](../techniques/docs/markdown-technique-section-lift/TECHNIQUE.md) owns the extraction of stable `TECHNIQUE.md` headings into one derived section-level surface while keeping the bundle markdown authoritative. [AOA-T-0019](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) begins only after bundle meaning already exists and turns bounded frontmatter plus derived catalog outputs into one routing spine.
- Default-use trigger: use `0018` when a reader or tool needs bounded lookup over stable sections such as `Intent`, `Contracts`, or `Validation`. Use `0019` when the question is bundle identity, status, review posture, or direct adjacency rather than section payload.
- Relation check: `complements` is still the right signal. It says the metadata spine and section lift strengthen one another without turning into the same contract.
- Evidence check: `0018` stays section-first and source-first. `0019` stays metadata-first and catalog-first. The support surfaces keep the boundary readable instead of making the two techniques look like one generic extraction layer. Outcome: `clear`.

### `AOA-T-0019` vs `AOA-T-0020` / `AOA-T-0021`

Question: where does shallow routing metadata stop and note or edge lifting begin?

- Invariant boundary: [AOA-T-0019](../techniques/docs/frontmatter-metadata-spine/TECHNIQUE.md) owns bundle identity and derived catalog routing. [AOA-T-0020](../techniques/docs/evidence-note-provenance-lift/TECHNIQUE.md) begins when supporting markdown notes need typed provenance handles. [AOA-T-0021](../techniques/docs/bounded-relation-lift-for-kag/TECHNIQUE.md) begins when direct relations need to power bounded adjacency hints.
- Default-use trigger: use `0019` when the surface should remain shallow and bundle-level. Use `0020` when the question is "which supporting note should I open?" Use `0021` when the question is "which directly related technique should I inspect next?"
- Relation check: `used_together_for` and `requires` are bounded here because the three techniques form a small source-lift stack, not a graph engine. The relation set says they commonly travel together without collapsing their different jobs.
- Evidence check: `0020` keeps note meaning in authored markdown and avoids note IDs or note graphs. `0021` keeps edges direct and typed and avoids rationale or multi-hop inference. That preserves the boundary between metadata routing, provenance lookup, and adjacency hints. Outcome: `clear`.

### `AOA-T-0022` vs the rest of the family

Question: where does markdown-first caution lift stop and shadow-policy semantics begin?

- Invariant boundary: [AOA-T-0022](../techniques/docs/risk-and-negative-effect-lift/TECHNIQUE.md) owns bounded caution lookup over authored `Risks` language and can supplement a canonical adverse-effects review note when a bundle is already canonical. It stops before shadow metadata, scoring, generated caution outputs, or any policy engine. The other four techniques stay on the source-lift side of sections, metadata, provenance, and relations.
- Default-use trigger: use `0022` when a reviewer wants one bounded way to inspect failure, harm, misuse, detection, and mitigation language without leaving markdown-first contracts. Use shadow-review surfaces when the question is whether a canonical technique quietly makes a system worse at the cluster level.
- Relation check: `complements` with `0018` is enough because both techniques lift from bundle markdown while still doing different work. A stronger relation would risk making caution lift look like shadow policy rather than a bounded companion.
- Evidence check: the fixed five-part `Risks` contract, the canonical adverse-effects review supplement, and the current guide text keep `0022` markdown-first. The technique remains a companion to review, not a generated caution layer. Outcome: `clear`.

## Findings

- `AOA-T-0018` is semantically distinct as the section lift.
- `AOA-T-0019` is semantically distinct as the canonical metadata spine.
- `AOA-T-0020` is semantically distinct as the provenance lift.
- `AOA-T-0021` is semantically distinct as the bounded relation lift.
- `AOA-T-0022` is semantically distinct as the markdown-first caution lift, and it should remain outside shadow-policy semantics.
- Live donor posture is now uneven but useful across the family: `AOA-T-0019` is strongest because three sibling repos already rely on the metadata spine for shared routing and review posture, and that proof is now strong enough for canonical default-use.
- `AOA-T-0021` now has strong live donor evidence through `aoa-evals` plus a committed `aoa-routing` one-hop relation-hint surface, which is enough for bounded canonical default-use while still staying outside graph semantics.
- `AOA-T-0020` still has strong live donor evidence through `aoa-evals`, but it should stay promoted until another non-eval markdown-first corpus proves the same typed provenance split.
- `AOA-T-0018` is now bridge-backed through `aoa-skills`, which is enough to strengthen the section-lift case without making it the dominant family donor.
- `AOA-T-0022` remains caution-specific and still under-evidenced as a live donor because adjacent caution language in sibling repos does not reproduce the same five-part `Risks` contract.
- Current `relations` are helpful and still bounded. No cleanup is justified in this pilot.
- Current examples, checks, and review notes support the five-way family split well enough for a review-only semantic surface.

Overall outcome: `clear`

## Next Step

No immediate remediation wave is justified for this family from this pilot alone.

The next step is to keep `AOA-T-0019` narrow as the canonical metadata spine and `AOA-T-0021` narrow as the canonical direct-relation hint companion while `AOA-T-0018`, `AOA-T-0020`, and `AOA-T-0022` keep accumulating bounded live evidence without collapsing into a broader graph, metadata, or shadow-policy package.
