# Skill-Support Semantic Review

This review-only pilot checks whether the recent skill-support cluster still reads as four distinct techniques rather than one blurred "agent-friendly testing and scoping" package.

Why this cluster was chosen now:

- all four techniques were just promoted from the same superseded landing wave
- the main remaining question is semantic separation, not missing repo structure
- the cluster crosses `agent-workflows`, `evaluation`, and `docs`, so drift would be costly if left implicit
- this is the highest-value review pass before any second-context evidence strengthening

This doc is a human review surface. It does not change statuses, frontmatter, validator behavior, or bundle contracts by itself.

## Cluster Map

| technique | current role |
|---|---|
| [AOA-T-0014](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) | bounded test-first implementation slice |
| [AOA-T-0015](../techniques/evaluation/contract-test-design/TECHNIQUE.md) | boundary-contract evaluation discipline |
| [AOA-T-0017](../techniques/evaluation/property-invariants/TECHNIQUE.md) | invariant-oriented coverage broadening |
| [AOA-T-0016](../techniques/docs/bounded-context-map/TECHNIQUE.md) | semantic scoping and handoff map |

## Seam Review

### `AOA-T-0014` vs `AOA-T-0015`

Question: where does bounded test-first slice discipline stop and explicit boundary-contract discipline begin?

- Invariant boundary: [AOA-T-0014](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) owns the workflow of stating one bounded behavior slice, expressing it in tests first where appropriate, implementing the smallest passing change, and keeping refactor pressure inside that slice. [AOA-T-0015](../techniques/evaluation/contract-test-design/TECHNIQUE.md) begins when the main problem is not slice discipline itself, but making a consumer-visible boundary explicit and reviewable.
- Default-use trigger: use `0014` when the change needs a compact execution discipline that keeps one behavior slice from widening. Use `0015` when the key risk is interface drift at an observable boundary such as an API, summary artifact, or service wrapper.
- Evidence check: `0014` checklist and example stay implementation-slice centric, focusing on behavior-first tests, minimal diff, and bounded refactor. `0015` checklist and example stay boundary centric, focusing on observable contract guarantees, downstream assumptions, and refactor freedom behind the contract. The support surfaces reinforce separation rather than blur it.
- Relation check: both currently point to `AOA-T-0001`, but for different reasons. `0014` reads as execution discipline close to plan-diff-apply-verify-report, while `0015` reads as evaluation discipline over a boundary surface. That shared adjacency does not collapse them. Outcome: `clear`.

### `AOA-T-0015` vs `AOA-T-0017`

Question: where does contract-surface validation stop and invariant-oriented broad coverage begin?

- Invariant boundary: [AOA-T-0015](../techniques/evaluation/contract-test-design/TECHNIQUE.md) defines what a consumer-visible boundary promises through explicit inputs, outputs, and failure behavior. [AOA-T-0017](../techniques/evaluation/property-invariants/TECHNIQUE.md) defines stable truths that should hold across many cases, even when there is no single consumer-facing contract shape to anchor the check.
- Default-use trigger: use `0015` when a named boundary and its consumers must stay stable through refactor or interface change. Use `0017` when the main problem is that example coverage is too narrow and the stronger reusable move is to express one meaningful invariant across a wider input or state space.
- Evidence check: `0015` example and checklist remain contract-surface oriented. `0017` example and checklist remain invariant-strength and bounded generator oriented. The current support surfaces still separate boundary design from coverage broadening.
- Watch point: both techniques can appear in the same validation path, and both use testing language. Future wording drift could make `0017` sound like "better contract tests" or make `0015` sound like a generic broad-coverage pattern if later examples stop centering the consumer-visible boundary. Outcome: `watch`.

### `AOA-T-0016` vs `AOA-T-0014` / `AOA-T-0015` / `AOA-T-0017`

Question: where does semantic scoping, vocabulary, and handoff mapping stop and implementation or evaluation technique begin?

- Invariant boundary: [AOA-T-0016](../techniques/docs/bounded-context-map/TECHNIQUE.md) owns the naming and scoping layer: clarify contexts, visible handoffs, and overloaded terms before work widens into the wrong area. It does not prescribe how implementation should be test-driven, how boundaries should be validated, or how broad invariants should be checked once the target area is already clear.
- Default-use trigger: use `0016` when contributors or agents are confused about what belongs inside the target area at all. Use `0014`, `0015`, or `0017` only after the semantic target is already clear enough that implementation or evaluation discipline becomes the main problem.
- Evidence check: `0016` checklist and example stay vocabulary-and-handoff centric rather than architectural-platform centric. The newer testing-oriented techniques stay rooted in execution or validation behavior, not repository mapping.
- Watch point: because `0016` uses words like "bounded context," future examples could drift into generic architecture formalism. If that happens, it could stop reading like a practical docs/scoping pattern and start looking like a broader domain-model technique. Outcome: `watch`.

## Findings

- `AOA-T-0014` is semantically distinct as an execution discipline for one bounded behavior slice.
- `AOA-T-0015` is semantically distinct as a boundary-contract surface, not a generic testing technique.
- `AOA-T-0017` is semantically distinct as invariant-oriented coverage broadening, not a duplicate of contract design.
- `AOA-T-0016` is semantically distinct as a docs/scoping pattern, not an architecture-domain opening and not a test technique.
- The strongest watch seam is `AOA-T-0015` vs `AOA-T-0017`, because both live in evaluation and both can sound like "stronger tests" if future examples lose their current center of gravity.
- The second watch seam is `AOA-T-0016` drifting toward generic architecture formalism if later examples stop being scoping- and handoff-centric.
- No relation cleanup, status change, or narrow remediation wave is justified from this pilot alone.

Overall outcome: `clear with two watch seams`

## Next Step

No immediate semantic-remediation wave is justified for this cluster from this pilot alone.

Second-context evidence strengthening has already landed for `AOA-T-0014` and `AOA-T-0015`, so the next step should focus on monitoring the documented watch seams around `AOA-T-0015` vs `AOA-T-0017` and `AOA-T-0016` drift toward generic architecture formalism.
