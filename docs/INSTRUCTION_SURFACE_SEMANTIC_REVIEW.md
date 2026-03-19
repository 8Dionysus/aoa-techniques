# Instruction-Surface Semantic Review

This review-only pilot checks whether the promoted docs-import pair still reads as two distinct techniques rather than one blurred "managed generated agent docs" package.

Why this pair was chosen now:

- both techniques are still `promoted`, so semantic clarity matters before any future status review
- both techniques govern generated agent-facing documentation surfaces, which makes seam drift easy to miss if left implicit
- the main remaining question is boundary clarity between source cardinality and output shape, not missing repo structure
- this is the highest-value review pass before any concrete example strengthening for the pair

This doc is a human review surface. It does not change statuses, frontmatter, validator behavior, or bundle contracts by itself.

## Pair Map

| technique | current role |
|---|---|
| [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) | many-fragment deterministic composition into one generated context artifact |
| [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) | one canonical rule source distributed to multiple agent-facing instruction surfaces |

## Seam Review

### `AOA-T-0012` vs `AOA-T-0013`

Question: where does many-source composition into one generated artifact stop and one-source fan-out into many managed instruction targets begin?

- Invariant boundary: [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) owns the case where many source fragments compose into one generated context artifact with deterministic ordering and traceable fragment authority. [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) begins when one canonical rule source already exists and the main problem is fanning that shared rule core out to multiple managed instruction targets without drift.
- Default-use trigger: use `0012` when the system needs fragment-first authoring and one stable generated output. Use `0013` when the system already has one canonical rule source and the main problem is keeping several agent-facing targets synchronized from it.
- Relation check: the current relation set does not justify cleanup in this review wave. `0012` stays readable without direct relation wiring because its bounded contract is already about many inputs narrowing into one output. `0013` keeps its current `AOA-T-0002` complement without collapsing into `0012`, because its contract is still source fan-out rather than fragment composition.
- Evidence check: `0012` support surfaces stay one-output composition centric, focusing on deterministic ordering, source annotations, and fragment traceability. `0013` support surfaces stay one-source distribution centric, focusing on canonical-source authority, managed targets, and wrapper-minimal fan-out. The pair stays distinct so long as future wording keeps source cardinality and output shape explicit. Outcome: `clear`.

## Findings

- `AOA-T-0012` is semantically distinct as one-output deterministic composition.
- `AOA-T-0013` is semantically distinct as one-source multi-target rule distribution.
- The current relation set does not justify cleanup in this wave.
- The strongest watch seam is that future wording must keep source cardinality and output shape explicit so the pair does not blur into generic "managed generated agent docs."
- No status change, relation cleanup, or narrow remediation wave is justified from this pilot alone.

Overall outcome: `clear with one watch seam`

## Next Step

No immediate semantic-remediation wave is justified for this pair from this pilot alone.

Concrete example strengthening has already landed for both techniques, so the next step should move to stronger live multi-target reuse evidence for `AOA-T-0013` rather than more example-only reinforcement.
