# Second Context Adaptation

## Technique
- id: AOA-T-0012
- name: deterministic-context-composition

## Target project
- name: aoa-techniques
- environment: public library repository with policy docs, technique catalog, and explicit agent-facing documentation surfaces
- runtime: documentation-first repository that documents the pattern rather than running the donor toolchain itself

## What changed
- paths: the donor composes `AGENTS.md` from `*.agents.md` or `agents-md/**/*.md`; this adaptation presents a generic fragment-to-generated-context pattern that can fit other source layouts
- services: no local compose CLI, watch mode, report output, or migration command is required in this repository
- dependencies: the adaptation depends on deterministic ordering and explicit source traceability, not on Bun, npm, or the donor package
- operating assumptions: contributors should treat generated context surfaces as derived artifacts and edit source fragments instead

## What stayed invariant
- contract: small source fragments compose into one stable generated context artifact
- validation logic: ordering stays deterministic and the output can be traced back to source fragments
- safety rules: generated context should be reviewed through source fragments, not by hand-editing the generated file

## Risks introduced by adaptation
- the pattern can become vague if a project copies fragment composition without writing explicit ordering rules
- some repositories may keep generated context files but skip source annotations or equivalent traceability metadata

## Evidence
- the donor `README.md` documents fragment discovery, generated `AGENTS.md` targets, deterministic ordering, and source annotations
- the donor `docs/design.md` defines stable ordering by priority then path, plus generated-file banners and idempotent writes
- the donor `test/compose.test.ts` verifies source annotations, deterministic ordering, scoped outputs, and no-op rewrites when content does not change
- this imported technique narrows those behaviors into a reusable pattern that fits a public documentation repository

## Result
- works as a documentation-first second context and preserves the bounded core without carrying over donor-specific toolchain assumptions
