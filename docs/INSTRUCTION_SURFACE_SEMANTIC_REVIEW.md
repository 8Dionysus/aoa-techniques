# Instruction-Surface Semantic Review

This review-only pilot checks whether the current instruction-surface cluster still reads as four distinct techniques rather than one blurred "managed generated agent docs" package.

Why this cluster was chosen now:

- the cluster now mixes one canonical composition technique with three promoted adjacent imports, so semantic clarity matters before any future status review
- all four techniques govern generated or managed instruction-facing documentation surfaces, which makes seam drift easy to miss if left implicit
- the main remaining question is boundary clarity between source cardinality, source ownership, and output shape, not missing repo structure
- this is the highest-value review pass before any concrete example strengthening or future closure work for the cluster

This doc is a human review surface. It does not change statuses, frontmatter, validator behavior, or bundle contracts by itself.

## Cluster Map

| technique | current role |
|---|---|
| [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) | many-fragment deterministic composition into one generated context artifact |
| [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) | one canonical rule source distributed to multiple agent-facing instruction surfaces |
| [AOA-T-0027](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) | one canonical skill or rule source propagated into multiple managed agent-facing targets |
| [AOA-T-0024](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) | upstream-owned content mirrored into a curated local collection with explicit source manifest and adjacent provenance |

## Seam Review

### `AOA-T-0012` vs `AOA-T-0013`

Question: where does many-source composition into one generated artifact stop and one-source fan-out into many managed instruction targets begin?

- Invariant boundary: [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) owns the case where many source fragments compose into one generated context artifact with deterministic ordering and traceable fragment authority. [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) begins when one canonical rule source already exists and the main problem is fanning that shared rule core out to multiple managed instruction targets without drift.
- Default-use trigger: use `0012` when the system needs fragment-first authoring and one stable generated output. Use `0013` when the system already has one canonical rule source and the main problem is keeping several agent-facing targets synchronized from it.
- Relation check: the current relation set does not justify cleanup in this review wave. `0012` stays readable without direct relation wiring because its bounded contract is already about many inputs narrowing into one output. `0013` keeps its current `AOA-T-0002` complement without collapsing into `0012`, because its contract is still source fan-out rather than fragment composition.
- Evidence check: `0012` support surfaces stay one-output composition centric, focusing on deterministic ordering, source annotations, and fragment traceability. `0013` support surfaces stay one-source distribution centric, focusing on canonical-source authority, managed targets, and wrapper-minimal fan-out. The pair stays distinct so long as future wording keeps source cardinality and output shape explicit. Outcome: `clear`.

### `AOA-T-0013` vs `AOA-T-0024`

Question: where does one local canonical rule source fanning out to many targets stop and one upstream-owned source being mirrored into a local curated collection begin?

- Invariant boundary: [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) owns the case where the canonical source already lives locally and the main problem is fan-out to multiple managed instruction targets. [AOA-T-0024](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) begins when the source of truth stays upstream and external, and the local problem is mirroring with explicit provenance rather than local canonical-source fan-out.
- Default-use trigger: use `0013` when one local canonical rule source must update several managed instruction surfaces. Use `0024` when one upstream-owned source must be mirrored locally with explicit attribution and a repeatable resync path.
- Relation check: `0024` complements `0013` without collapsing into it, because provenance-first mirroring still leaves upstream ownership outside the local repository. `0013` remains a local-source anti-drift technique, not a mirror-and-attribution technique. Outcome: `clear`.

### `AOA-T-0013` vs `AOA-T-0027`

Question: where does one local canonical rule source fanning out across instruction surfaces stop and one canonical skill or rule core propagating into managed agent-facing targets begin?

- Invariant boundary: [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) owns the broader local-source distribution story where one canonical rule source fans out to several instruction surfaces. [AOA-T-0027](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) begins when the center of gravity is the narrower managed-target propagation contract for one shared skill or rule core and the main risk is target drift rather than general instruction-surface governance.
- Default-use trigger: use `0013` when the main question is one local canonical source synchronizing several instruction surfaces. Use `0027` when the main question is how one shared skill or rule core propagates into multiple managed agent-facing targets without widening into marketplace, role, or orchestration semantics.
- Relation check: `0027` complements `0013` without replacing it, because the newer bundle is a narrower sibling centered on managed-target propagation rather than a broader source-distribution default. Outcome: `clear with one watch seam`.

### `AOA-T-0012` vs `AOA-T-0024`

Question: where does many-fragment composition into one generated artifact stop and manifest-driven upstream mirroring with provenance begin?

- Invariant boundary: [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) owns many local source fragments collapsing into one generated context artifact. [AOA-T-0024](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) owns one upstream-owned source or bundle being mirrored locally with explicit provenance and without claiming local authorship.
- Default-use trigger: use `0012` when the main question is how local fragments become one stable output. Use `0024` when the main question is how a local curated mirror stays subordinate to upstream ownership and readable provenance.
- Evidence check: `0012` examples stay composition-centric, while `0024` examples stay source-manifest, attribution, and resync centric. The pair stays distinct so long as future wording keeps local composition separate from upstream mirroring. Outcome: `clear`.

### `AOA-T-0027` vs `AOA-T-0024`

Question: where does managed target propagation from one local canonical skill or rule core stop and upstream-owned mirroring with provenance begin?

- Invariant boundary: [AOA-T-0027](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) owns local canonical source propagation into managed agent-facing targets. [AOA-T-0024](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) owns local curation of upstream-owned content with explicit provenance and repeatable resync.
- Default-use trigger: use `0027` when source ownership is already local and the problem is keeping managed targets synchronized. Use `0024` when source ownership stays upstream and the local question is how to mirror that source without hiding origin ownership.
- Evidence check: `0027` examples stay managed-target and anti-drift centric, while `0024` examples stay manifest, attribution, and resync centric. Outcome: `clear`.

## Findings

- `AOA-T-0012` is semantically distinct as one-output deterministic composition.
- `AOA-T-0013` is semantically distinct as one-source multi-target rule distribution.
- `AOA-T-0027` is semantically distinct as local managed-target skill or rule propagation.
- `AOA-T-0024` is semantically distinct as upstream mirroring with explicit provenance and subordinate local ownership.
- The current relation set does not justify cleanup in this wave.
- The strongest watch seam is that future wording must keep source cardinality, source ownership, output shape, and managed-target scope explicit so the cluster does not blur into generic "managed generated agent docs."
- No status change, relation cleanup, or narrow remediation wave is justified from this pilot alone.

Overall outcome: `clear with one watch seam`

## Next Step

No immediate semantic-remediation wave is justified for this cluster from this pilot alone.

Concrete example strengthening has already landed for all four techniques, `ruler` is now explicitly locked both as the bounded external origin for `AOA-T-0013` and as the narrower adjacent import origin for `AOA-T-0027`, and `n-skills` now lands as the adjacent provenance-mirroring import `AOA-T-0024`. The next step should therefore move to one more independent live instruction-distribution context for `AOA-T-0013` and one future live managed-target propagation context for `AOA-T-0027` rather than more example-only reinforcement or another import-only review.
