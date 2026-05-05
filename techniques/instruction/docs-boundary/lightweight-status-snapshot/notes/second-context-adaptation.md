# Second Context Adaptation

## Technique
- id: AOA-T-0009
- name: lightweight-status-snapshot

## Target project
- name: aoa-techniques
- environment: public library repository with a short top-level entrypoint and canonical policy/catalog docs
- runtime: documentation-first repository without a separate `MANIFEST`

## What changed
- paths: the origin uses both `README.md` and `MANIFEST.md`; this adaptation uses `README.md` as the single lightweight snapshot surface
- services: there is no operator session log, CI dashboard, or active execution plan inside this repository
- dependencies: the adaptation depends on outward links to `TECHNIQUE_INDEX.md`, `CONTRIBUTING.md`, `SECURITY.md`, and `AGENTS.md`
- operating assumptions: the top-level entrypoint should orient new readers quickly and defer policy, contribution, and catalog detail to canonical documents

## What stayed invariant
- contract: the snapshot stays short and link-driven
- validation logic: detailed policy and catalog truth lives outside the entrypoint
- safety rules: the entrypoint is not allowed to become a running archive of status detail

## Risks introduced by adaptation
- without a separate `MANIFEST`, contributors may overload `README.md` with operational detail
- a small repository can make snapshot drift harder to notice because duplicated prose still feels manageable

## Evidence
- `README.md` in `aoa-techniques` remains a short entrypoint for purpose, structure, maturity model, and contribution framing
- detailed technique state lives in `TECHNIQUE_INDEX.md`, while policy and operating guidance live in `AGENTS.md`, `CONTRIBUTING.md`, and `SECURITY.md`
- the adaptation keeps the snapshot discipline even though the repository uses only one top-level snapshot doc instead of two

## Result
- works
