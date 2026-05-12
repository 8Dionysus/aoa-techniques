# Canonical Readiness

## Technique
- id: AOA-T-0027
- name: cross-agent-skill-propagation

## Verdict
- approve for canonical promotion

## Evidence summary
- external origin: the imported technique has a bounded donor contract and explicit exclusions around marketplace curation, runtime role semantics, MCP propagation, nested loading, and other product-width detail
- exact-fit second context: ai-rulez proves the contract outside the donor by keeping rules, context, skills, agents, and commands in `.ai-rulez/` and generating native agent-tool outputs for many targets
- external review: the first import review passed, and the ai-rulez pass confirms managed skill or rule propagation survives without importing marketplace, MCP, profile-policy, or cross-tool product governance
- validation strength: the bundle now carries one checklist, two examples, a clean external-origin note, exact-fit public second-context evidence, and an adverse-effects review

## Default-use rationale
- this is the right canonical default when one shared skill or rule core must reach multiple agent-facing targets without turning each target into a canonical home
- it remains narrower than `AOA-T-0013`, which keeps the broader one-canonical-rule-source-to-many-managed-targets instruction-surface distribution story in focus
- it also stays distinct from `AOA-T-0024`, which is about upstream mirroring with provenance rather than local skill or rule propagation
- ai-rulez confirms that the move can survive outside the donor even when the source layer covers rules, context, skills, agents, and commands, because the reusable proof is still managed-source fan-out into target-native agent surfaces

## Fresh public-safety check
- review date: 2026-05-12
- result: pass
- sanitization still holds: the bundle keeps the reusable propagation contract and excludes donor-specific orchestration behavior
- public reuse check: the examples, checklist, adaptation notes, and ai-rulez evidence remain understandable without hidden donor-repo context
- public-safety boundary: ai-rulez target names and content types are cited only as evidence of managed multi-target propagation, not as universal required tools, marketplace policy, MCP doctrine, or cross-agent product governance

## Remaining gaps
- no blocking promotion gap remains as long as the bundle stays centered on managed propagation of one shared skill or rule source into multiple agent-facing targets
- future review should reject surfaces that are only one-source rule distribution, target-specific hand copies, skill marketplace curation, MCP propagation, profile policy, or broad cross-tool configuration governance without the same shared-source managed-target fan-out

## Recommendation
- promote `AOA-T-0027` to `canonical`
- use `AOA-T-0027` as the default instruction-surface technique when the reusable object is one shared skill or rule core propagated into multiple managed agent-facing targets while sibling techniques own broader rule distribution, nested precedence, provenance mirroring, marketplace curation, and runtime behavior
