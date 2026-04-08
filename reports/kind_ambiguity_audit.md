# Kind Ambiguity Audit

This file is generated from the current kind registry, family seed, wave1 overlay, and generated catalog.
Do not edit it by hand; run `python scripts/build_kind_manifest.py`.

This audit is scout-only, non-authoritative, and weaker than bundle frontmatter. Use it to review tie-break seams, not to remap techniques automatically.

Use this audit to inspect likely tie-break seams before proposing any later remap wave.

## `workflow` vs `guardrail`

Tie-break rule: pick `workflow` when the main promise is how to do the work; pick `guardrail` when the main promise is how to stop, narrow, or approve the work.

- [AOA-T-0028](../techniques/agent-workflows/confirmation-gated-mutating-action/TECHNIQUE.md) - confirmation-gated-mutating-action (`agent-workflows`, current `guardrail`): current-kind cues `gate`, `gated`; opposing `workflow` cues `workflow`, `step`, `plan`, `loop`. Seed family `agent-workflows-core` already spans both `workflow` and `guardrail`. Verdict: `candidate remap`.
- [AOA-T-0005](../techniques/agent-workflows/new-intent-rollout-checklist/TECHNIQUE.md) - new-intent-rollout-checklist (`agent-workflows`, current `guardrail`): current-kind cues none; opposing `workflow` cues `workflow`, `plan`. Seed family `intent-chain` already spans both `workflow` and `guardrail`. Verdict: `candidate remap`.
- [AOA-T-0068](../techniques/agent-workflows/fail-closed-evidence-gate/TECHNIQUE.md) - fail-closed-evidence-gate (`agent-workflows`, current `guardrail`): current-kind cues `gate`, `approval`, `block`, `fail-closed`; opposing `workflow` cues `workflow`. Verdict: `keep current kind`.
- [AOA-T-0091](../techniques/agent-workflows/workspace-root-ingress-and-mutation-gate/TECHNIQUE.md) - workspace-root-ingress-and-mutation-gate (`agent-workflows`, current `guardrail`): current-kind cues `gate`; opposing `workflow` cues `workflow`. Seed family `owner-truth-closeout` already spans both `workflow` and `guardrail`. Verdict: `revisit later`.
- [AOA-T-0093](../techniques/agent-workflows/recommendation-truth-vs-host-actionability/TECHNIQUE.md) - recommendation-truth-vs-host-actionability (`agent-workflows`, current `guardrail`): current-kind cues none; opposing `workflow` cues `workflow`, `plan`. Verdict: `candidate remap`.
- [AOA-T-0049](../techniques/agent-workflows/dependency-aware-task-graph/TECHNIQUE.md) - dependency-aware-task-graph (`agent-workflows`, current `workflow`): current-kind cues `workflow`, `step`; opposing `guardrail` cues `block`. Verdict: `keep current kind`.

## `validation` vs `assessment`

Tie-break rule: pick `validation` when the output is proof, integrity, or correctness evidence; pick `assessment` when the output is classification, diagnosis, or decision support.

- [AOA-T-0086](../techniques/agent-workflows/automation-fit-matrix/TECHNIQUE.md) - automation-fit-matrix (`agent-workflows`, current `assessment`): current-kind cues `classify`, `classification`, `route`, `matrix`; opposing `validation` cues `proof`. Verdict: `keep current kind`.
- [AOA-T-0076](../techniques/agent-workflows/owner-layer-triage/TECHNIQUE.md) - owner-layer-triage (`agent-workflows`, current `assessment`): current-kind cues `classification`, `route`, `decision`; opposing `validation` cues `proof`. Verdict: `keep current kind`.
- [AOA-T-0096](../techniques/agent-workflows/pinned-validation-matrix-before-generated-publish/TECHNIQUE.md) - pinned-validation-matrix-before-generated-publish (`agent-workflows`, current `validation`): current-kind cues `validation`, `validate`; opposing `assessment` cues `matrix`. Verdict: `keep current kind`.
- [AOA-T-0088](../techniques/agent-workflows/approval-sensitivity-check/TECHNIQUE.md) - approval-sensitivity-check (`agent-workflows`, current `assessment`): current-kind cues `classify`; opposing `validation` cues `check`. Verdict: `revisit later`.
- [AOA-T-0089](../techniques/agent-workflows/quest-unit-promotion-review/TECHNIQUE.md) - quest-unit-promotion-review (`agent-workflows`, current `assessment`): current-kind cues `route`; opposing `validation` cues `proof`. Verdict: `revisit later`.

## `artifact` vs `lift`

Tie-break rule: pick `artifact` when the technique defines a primary durable artifact or storage shape; pick `lift` when it derives a bounded secondary surface from an already authoritative source.

- [AOA-T-0044](../techniques/history/versionable-session-transcripts/TECHNIQUE.md) - versionable-session-transcripts (`history`, current `artifact`): current-kind cues `artifact`, `transcript`, `capture`; opposing `lift` cues `export`. Verdict: `keep current kind`.
- [AOA-T-0075](../techniques/agent-workflows/session-donor-harvest/TECHNIQUE.md) - session-donor-harvest (`agent-workflows`, current `lift`): current-kind cues none; opposing `artifact` cues `artifact`. Seed family `donor-harvest` already spans both `artifact` and `lift`. Verdict: `candidate remap`.
- [AOA-T-0085](../techniques/agent-workflows/multi-axis-quest-overlay/TECHNIQUE.md) - multi-axis-quest-overlay (`agent-workflows`, current `artifact`): current-kind cues none; opposing `lift` cues `overlay`. Seed family `donor-harvest` already spans both `artifact` and `lift`. Verdict: `candidate remap`.
- [AOA-T-0008](../techniques/evaluation/published-summary-remediation-snapshot/TECHNIQUE.md) - published-summary-remediation-snapshot (`evaluation`, current `lift`): current-kind cues none; opposing `artifact` cues `snapshot`. Seed family `published-summary` already spans both `artifact` and `lift`. Verdict: `candidate remap`.
- [AOA-T-0084](../techniques/agent-workflows/progression-evidence-lift/TECHNIQUE.md) - progression-evidence-lift (`agent-workflows`, current `lift`): current-kind cues `lift`; opposing `artifact` cues none. Seed family `donor-harvest` already spans both `artifact` and `lift`. Verdict: `keep current kind`.
- [AOA-T-0006](../techniques/evaluation/latest-alias-plus-history-copy/TECHNIQUE.md) - latest-alias-plus-history-copy (`evaluation`, current `artifact`): current-kind cues none; opposing `lift` cues none. Seed family `published-summary` already spans both `artifact` and `lift`. Verdict: `keep current kind`.

## `composition` vs `distribution`

Tie-break rule: pick `composition` when many pieces become one result; pick `distribution` when one canonical source fans out to many targets.

- [AOA-T-0027](../techniques/docs/cross-agent-skill-propagation/TECHNIQUE.md) - cross-agent-skill-propagation (`docs`, current `distribution`): current-kind cues `distribution`, `propagate`, `propagation`; opposing `composition` cues none. Seed family `instruction-surface` already spans both `composition` and `distribution`. Verdict: `keep current kind`.
- [AOA-T-0012](../techniques/docs/deterministic-context-composition/TECHNIQUE.md) - deterministic-context-composition (`docs`, current `composition`): current-kind cues `composition`, `compose`; opposing `distribution` cues none. Seed family `instruction-surface` already spans both `composition` and `distribution`. Verdict: `keep current kind`.
- [AOA-T-0024](../techniques/docs/upstream-mirroring-with-provenance/TECHNIQUE.md) - upstream-mirroring-with-provenance (`docs`, current `distribution`): current-kind cues `mirror`, `mirroring`; opposing `composition` cues none. Seed family `instruction-surface` already spans both `composition` and `distribution`. Verdict: `keep current kind`.
- [AOA-T-0029](../techniques/docs/nested-rule-loading/TECHNIQUE.md) - nested-rule-loading (`docs`, current `composition`): current-kind cues `layer`, `precedence`; opposing `distribution` cues none. Seed family `instruction-surface` already spans both `composition` and `distribution`. Verdict: `keep current kind`.
- [AOA-T-0035](../techniques/docs/profile-preset-composition/TECHNIQUE.md) - profile-preset-composition (`docs`, current `composition`): current-kind cues `composition`, `compose`; opposing `distribution` cues none. Seed family `instruction-surface` already spans both `composition` and `distribution`. Verdict: `keep current kind`.
- [AOA-T-0013](../techniques/docs/single-source-rule-distribution/TECHNIQUE.md) - single-source-rule-distribution (`docs`, current `distribution`): current-kind cues `distribution`; opposing `composition` cues none. Seed family `instruction-surface` already spans both `composition` and `distribution`. Verdict: `keep current kind`.

## `handoff` vs `workflow`

Tie-break rule: pick `handoff` when transfer, checkpoint, or resume is the center of gravity; pick `workflow` when the center of gravity is the work loop itself.

- [AOA-T-0062](../techniques/agent-workflows/episode-bounded-agent-loop/TECHNIQUE.md) - episode-bounded-agent-loop (`agent-workflows`, current `handoff`): current-kind cues `handoff`, `checkpoint`, `continuation`, `episode`; opposing `workflow` cues `workflow`, `loop`. Verdict: `keep current kind`.
- [AOA-T-0057](../techniques/agent-workflows/structured-handoff-before-compaction/TECHNIQUE.md) - structured-handoff-before-compaction (`agent-workflows`, current `handoff`): current-kind cues `handoff`, `checkpoint`, `resume`, `continuation`; opposing `workflow` cues `workflow`. Verdict: `keep current kind`.
- [AOA-T-0058](../techniques/agent-workflows/receipt-confirmed-handoff-packet/TECHNIQUE.md) - receipt-confirmed-handoff-packet (`agent-workflows`, current `handoff`): current-kind cues `handoff`, `receipt`, `packet`, `continuation`; opposing `workflow` cues `workflow`. Verdict: `keep current kind`.
- [AOA-T-0056](../techniques/agent-workflows/channelized-agent-mailbox/TECHNIQUE.md) - channelized-agent-mailbox (`agent-workflows`, current `handoff`): current-kind cues `handoff`, `continuation`, `mailbox`; opposing `workflow` cues `workflow`. Verdict: `keep current kind`.
- [AOA-T-0060](../techniques/agent-workflows/session-opening-ritual-before-work/TECHNIQUE.md) - session-opening-ritual-before-work (`agent-workflows`, current `handoff`): current-kind cues `handoff`, `resume`, `continuation`; opposing `workflow` cues `workflow`. Verdict: `keep current kind`.
- [AOA-T-0052](../techniques/agent-workflows/review-findings-compaction/TECHNIQUE.md) - review-findings-compaction (`agent-workflows`, current `handoff`): current-kind cues none; opposing `workflow` cues `workflow`. Seed family `review-compaction` already spans both `handoff` and `workflow`. Verdict: `candidate remap`.

## Boundaries

- This audit is scout-only, non-authoritative, and weaker than bundle frontmatter. Use it to review tie-break seams, not to remap techniques automatically.
- Use the registry tie-break rules first, then this audit as a bounded scout aid only.
- A later remap wave should still review bundle meaning directly before changing any frontmatter.
