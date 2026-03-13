# Second Context Adaptation

## Technique
- id: AOA-T-0002
- name: source-of-truth-layout

## Target project
- name: aoa-techniques
- environment: public library repository with community files, technique catalog, and authoring templates
- runtime: documentation-first repository without in-repo `TODO`, `PLANS`, or `RUNBOOK` surfaces

## What changed
- paths: the origin mapped `README`, `MANIFEST`, `TODO`, `PLANS`, `DECISIONS`, `RUNBOOK`, and `SESSION_*`; this adaptation maps `README`, `TECHNIQUE_INDEX`, `AGENTS`, `CONTRIBUTING`, `SECURITY`, and `templates/`
- services: no operator runbook or session-log layer lives in this repository; the document-role map is reduced to the information classes that actually exist here
- dependencies: the adaptation depends on a small stable set of public docs instead of a larger operational doc tree
- operating assumptions: entrypoint docs should link to canonical policy or catalog docs rather than duplicate contribution, security, or index content

## What stayed invariant
- contract: each recurring information class still has one canonical home
- validation logic: routing questions can still be answered by asking which document owns a given class of information first
- safety rules: entrypoint docs stay lightweight, and policy or index details are not duplicated across multiple top-level docs

## Risks introduced by adaptation
- the smaller repository can hide missing document classes behind simplicity and make the role map feel implicit again
- contributors may treat `README` as a catch-all summary unless the role map stays explicit

## Evidence
- origin evidence in `atm10-agent/docs/SOURCE_OF_TRUTH.md` explicitly assigns canonical roles to `README.md`, `MANIFEST.md`, `TODO.md`, `PLANS.md`, `docs/SESSION_*.md`, `docs/DECISIONS.md`, and `docs/RUNBOOK.md`
- the same source file also fixes update-routing rules such as `behavior/architecture -> docs/DECISIONS.md`, `commands/setup -> docs/RUNBOOK.md`, `important run/result -> docs/SESSION_*.md`, `active steps -> TODO.md`, and `goals/DoD -> PLANS.md`
- `atm10-agent/README.md` and `atm10-agent/MANIFEST.md` both act as lightweight entrypoints that link outward to canonical documents instead of duplicating long history
- in `aoa-techniques`, `README.md` acts as the short public entrypoint, `TECHNIQUE_INDEX.md` owns catalog state, `CONTRIBUTING.md` owns contribution rules, `SECURITY.md` owns sensitive reporting, and `AGENTS.md` owns collaboration workflow
- this is a reduced variant of the technique rather than a full operational map with `TODO`, `PLANS`, `RUNBOOK`, and `SESSION_*`

## Result
- works
