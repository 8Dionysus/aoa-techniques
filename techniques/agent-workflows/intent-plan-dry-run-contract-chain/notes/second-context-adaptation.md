# Second Context Adaptation

## Technique
- id: AOA-T-0004
- name: intent-plan-dry-run-contract-chain

## Target project
- name: aoa-skills
- environment: public repository of reusable skills for human+agent workflows
- runtime: markdown-authored skill composition with explicit upstream technique linkage

## What changed
- adaptation path: the full artifact-first automation-chain technique is reused downstream as a narrower skill-level preview-first contract rather than copied as ATM10-shaped workflow detail
- downstream surface: the visible reuse point is a skill trigger, procedure, contract, and verification surface instead of a full implementation guide for plan artifacts and chain wiring
- linkage form: downstream reuse is made explicit through `skills/aoa-dry-run-first/techniques.yaml`, including a pinned upstream `source_ref`, rather than through prose-only borrowing

## What stayed invariant
- preview-first bias: dry-run or preview remains preferred before real execution when the action has meaningful operational consequences
- honesty about proof: preview output should reduce uncertainty without being overstated as proof of total safety
- execution boundary: real execution should not be smuggled into the preview step

## Risks introduced by adaptation
- skill-level narrowing can hide the artifact-first chain detail and make the technique sound like generic caution guidance
- downstream wording can over-center preview mindset and under-surface explicit plan artifact and contract-check structure
- future readers could mistake a linked skill scaffold for proof that every dry-run-first pattern automatically satisfies the full upstream chain contract

## Evidence
- `skills/aoa-dry-run-first/techniques.yaml` already links `AOA-T-0004` as an upstream source with a concrete `source_ref` and a bounded `use_sections` subset, which shows explicit downstream reuse rather than only conceptual similarity.
- `skills/aoa-dry-run-first/SKILL.md` keeps the same preview-first core in narrower skill form: prefer dry-run before real execution, name preview limits honestly, and avoid letting the preview silently become the real action.
- The downstream skill does not copy ATM10-specific artifact names or workflow layout, which shows that the portable contract is the reusable safety discipline rather than donor-specific implementation detail.

## Result
- verdict: works
- note: the technique remains reusable under a narrower downstream skill projection without collapsing into project-specific automation detail
