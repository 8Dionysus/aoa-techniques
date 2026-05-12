# Second Context Adaptation

## Technique
- id: AOA-T-0030
- name: fragmented-agent-context

## Target project
- name: Cline Rules
- environment: public Cline documentation for persistent project and global rule/context files
- runtime: workspace `.clinerules/` markdown and text files that Cline combines into the agent's rule context, with optional conditional path activation

## What changed

- paths: Cline stores workspace rules in `.clinerules/` at project root, with separate markdown files such as coding, testing, and architecture guidance
- services: no deterministic generator, JSON report command, CI stack, or generated aggregate artifact is required for this proof
- dependencies: the adaptation depends on rule/context fragments staying editable, topic-focused, version-controlled, and scoped by filename, content, or optional path conditions
- operating assumptions: contributors edit the source fragments directly and treat Cline's combined runtime context as downstream consumption rather than the canonical authored file

## What stayed invariant

- contract: context is authored in smaller bounded fragments before any aggregate output is trusted
- validation logic: fragment scope and ownership remain visible to reviewers
- safety rules: fragments stay canonical and do not silently give way to a generated aggregate as the editable source of truth

## Risks introduced by adaptation

- Cline combines the fragments for use, so reviewers must keep the source layer distinct from the consumed context
- conditional activation can tempt teams to treat runtime loading behavior as the main technique instead of fragment-first authoring
- rule toggles can hide whether a fragment is active, so the proof must stay on authored fragment structure rather than session behavior

## Evidence

- Cline Rules documentation checked on 2026-05-12 describes rules as persistent markdown instructions and project-specific context
- it stores workspace rules in `.clinerules/`, shows a multi-file layout with `coding.md`, `testing.md`, and `architecture.md`, processes all `.md` and `.txt` files inside `.clinerules/`, and recommends one concern per file
- it supports optional path conditions, but the exact-fit proof here is the fragment-first authored rule/context layer, not conditional activation or runtime injection

## Result

- exact-fit second context confirmed
- the bundle can move from documentation-first promoted posture to canonical default, as long as it stays about bounded fragment-first source authoring rather than generated composition, CI reporting, runtime injection, or rule-toggle behavior
