# Evaluation-Chain Shadow Review

This review-only pilot checks whether the canonical evaluation-chain pair still exposes two bounded shadow seams rather than one blended "summary plus rollout caution" layer.

Why this pair was chosen now:

- both techniques are already `canonical`
- both already have typed `adverse-effects-review.md` notes
- the pair already has a semantic-boundary review, so the next bounded question is shadow clarity rather than role confusion
- evaluation-chain systems are the nearest canonical family where false-success, log-scrape relapse, and hidden strictness can look like healthy operational discipline

This doc is a human review surface. It does not change statuses, frontmatter, validator behavior, or bundle contracts by itself.

## Pair Map

| technique | current role | current shadow seam |
|---|---|---|
| [AOA-T-0003](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) | default summary-contract producer for runnable smoke and probe paths | green-looking summary publication can still hide thin failure context or drift back toward log scraping |
| [AOA-T-0007](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) | default staged-promotion pattern for moving one observed signal toward one narrow strict enforcement surface | staged rollout language can look disciplined while strictness leaks early or telemetry starts masking an undecided enforcement boundary |

## Seam Review

### `AOA-T-0003`

Question: when does a summary producer keep publishing "success" while diagnosability is already degrading underneath it?

- Invariant shadow seam: [AOA-T-0003](../techniques/evaluation/contract-first-smoke-summary/TECHNIQUE.md) owns one stable machine-readable producer contract across success and failure paths. Its main shadow is false confidence from summary publication continuing while failure context gets too thin and downstream readers quietly return to log scraping.
- Successful-failure pattern: the summary still lands at the expected path, but error cases collapse into sparse status fields, supporting details move back into logs, and the contract keeps looking healthy only because the file still exists.
- Wording check: the bundle and note keep the watch seam on thin failure context, log-scrape relapse, and producer drift into storage or rollout language rather than generic "more detail would be nice" commentary. Outcome: `clear`.

### `AOA-T-0007`

Question: when does staged promotion stop being one explicit rollout path and start acting like hidden strictness with too much telemetry theater?

- Invariant shadow seam: [AOA-T-0007](../techniques/evaluation/signal-first-gate-promotion/TECHNIQUE.md) owns history-backed promotion from observation to one narrow strict surface. Its main shadow is that shallow readiness history, leaking strict behavior, or ever-richer telemetry vocabulary make the rollout look governed even when the real enforcement boundary is still unclear.
- Successful-failure pattern: dashboards and summaries multiply, but operators cannot state which surface is actually strict, strict consequences appear earlier than intended, or the pair stays stuck in performative observation without a real decision.
- Wording check: the bundle and note keep the watch seam on premature strictness from shallow history, strict-surface leakage, and telemetry-rich rollout theater rather than broad governance-stack skepticism. Outcome: `clear`.

## Findings

- `AOA-T-0003` still owns producer-contract false success: publication alone is not enough if failures stop carrying bounded diagnostic context and readers drift back to logs.
- `AOA-T-0007` still owns hidden-strictness drift: the caution is not "telemetry is bad," but that rollout language can outgrow one explicit enforcement boundary.
- The pair remains shadow-distinct even inside one evaluation chain: `AOA-T-0003` guards contract and diagnosability, while `AOA-T-0007` guards how one observed signal becomes strict.
- The current adverse-effects notes are already aligned enough for a second shadow-review pilot without reopening either bundle.

Overall outcome: `clear`

## Next Step

No broader unified review spine is justified from this pair alone.

Keep the evaluation-chain pair as the second shadow-reviewed canonical family, and treat the docs-boundary pair as the next candidate only if duplicate-summary relapse or navigability loss develops the same need for repo-level shadow lookup.
