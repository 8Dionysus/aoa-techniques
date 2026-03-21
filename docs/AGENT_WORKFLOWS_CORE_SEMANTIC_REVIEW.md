# Agent-Workflows Core Semantic Review

This review-only surface checks whether the current canonical agent-workflows core still reads as three distinct techniques rather than one blurred "good workflow hygiene" package.

Why this cluster was chosen now:

- all three techniques are already `canonical`, so the main risk is default-use blur rather than missing evidence
- the cluster sits in one domain, but the techniques still do different jobs in the same operating path
- the main remaining gap from the audit was review coverage, not bundle quality
- this review should absorb canonical-core pressure so [SKILL_SUPPORT_SEMANTIC_REVIEW.md](SKILL_SUPPORT_SEMANTIC_REVIEW.md) can stay focused on its own cross-domain seams

This doc is a human review surface. It does not change statuses, frontmatter, validator behavior, or bundle contracts by itself.

## Cluster Map

| technique | current role |
|---|---|
| [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) | canonical workflow backbone for bounded repository changes |
| [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) | intent-chain specialization for artifact-first normalization and dry-run checking |
| [AOA-T-0014](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) | bounded execution and test slice discipline inside one implementation change |

## Seam Review

### `AOA-T-0001` vs `AOA-T-0004`

Question: where does the general workflow backbone stop and the intent-chain specialization begin?

- Invariant boundary: [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) owns the generic execution contract of plan, bounded diff, verification, and explicit reporting for repository work. [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) begins when the main problem is not generic execution hygiene, but stabilizing an intent-shaped artifact chain before real execution exists.
- Default-use trigger: use `0001` when the change needs a bounded workflow backbone across planning, implementation, verification, and reporting. Use `0004` when the workflow must first normalize intent into artifacts, plans, and dry-run checks before any real execution path should be trusted.
- Relation check: `0004` still reads like a narrower specialization on top of `0001`, not a replacement for the base workflow contract. The pair reads as backbone plus intent-chain specialization rather than duplicate workflow prose. Outcome: `clear`.

### `AOA-T-0001` vs `AOA-T-0014`

Question: where does the general workflow backbone stop and the bounded test-first slice discipline begin?

- Invariant boundary: [AOA-T-0001](../techniques/agent-workflows/plan-diff-apply-verify-report/TECHNIQUE.md) owns the overall work loop. [AOA-T-0014](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) begins when the main risk is a single behavior slice widening during implementation and the safer move is to keep execution and verification pinned to one bounded slice.
- Default-use trigger: use `0001` when the whole repository change needs a minimal but complete execution contract. Use `0014` when the main problem inside that workflow is keeping one behavior slice small, test-first where appropriate, and resistant to spillover.
- Evidence check: `0001` remains workflow-backbone centric in its checklist and example, while `0014` stays slice centric in its example, checklist, and caution note. The bundles do not currently collapse into one generic "do careful work" doctrine. Outcome: `clear`.

### `AOA-T-0004` vs `AOA-T-0014`

Question: where does intent-chain specialization stop and bounded execution slicing begin?

- Invariant boundary: [AOA-T-0004](../techniques/agent-workflows/intent-plan-dry-run-contract-chain/TECHNIQUE.md) owns artifact-first intent normalization and dry-run contract checking before the live path is trusted. [AOA-T-0014](../techniques/agent-workflows/tdd-slice/TECHNIQUE.md) owns the execution discipline for one bounded implementation slice after the target path is already clear enough to work on directly.
- Default-use trigger: use `0004` when the system first needs the intent-chain artifact layer or one new path still has to be normalized through dry-run-first checks. Use `0014` when the target path is already known and the main issue is keeping one implementation slice small and reviewable.
- Watch point: both techniques can appear in the same end-to-end change, because an intent-chain system can still be implemented or extended through bounded slices. The seam stays healthy as long as `0004` keeps chain artifacts at the center of gravity and `0014` keeps one behavior slice at the center. Outcome: `clear`.

## Findings

- `AOA-T-0001` is semantically distinct as the canonical workflow backbone for bounded repository changes.
- `AOA-T-0004` is semantically distinct as the intent-chain specialization that adds artifact-first normalization and dry-run contract checks.
- `AOA-T-0014` is semantically distinct as bounded execution and test slicing inside one implementation change.
- The main cluster risk was missing review coverage, not bundle blur or missing evidence.
- No relation cleanup, bundle-local rewrite, or new shadow-review family is justified from this review alone.

Overall outcome: `clear`

## Next Step

No immediate semantic-remediation wave is justified for this canonical core from this review alone.

The next step should keep this review as the canonical-core anchor, leave [INTENT_CHAIN_SEMANTIC_REVIEW.md](INTENT_CHAIN_SEMANTIC_REVIEW.md) focused on `AOA-T-0004` vs `AOA-T-0005`, and keep bundle-local notes responsible for promotion and caution posture.
