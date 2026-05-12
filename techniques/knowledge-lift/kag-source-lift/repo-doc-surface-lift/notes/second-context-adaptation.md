# Second Context Adaptation

## Technique
- id: AOA-T-0046
- name: repo-doc-surface-lift

## Target project
- name: nuxt-llms
- repository: `nuxt-content/nuxt-llms`
- observed revision: `6faa1c45e082274267eae9295b501ab0053d0365`
- public surfaces:
  - `src/runtime/server/routes/llms.txt.get.ts`
  - `src/runtime/types.ts`

## What changed
- docs reader shape: Nuxt LLMs turns configured documentation sections into a `llms.txt` reader route made of titles, descriptions, links, and notes.
- source boundary: the reader route is downstream from configured documentation metadata rather than the authored docs themselves becoming generated truth.
- route purpose: the generated text surface answers "which docs links should an LLM or reader open?" rather than replacing the source documentation or becoming a product-wide docs taxonomy.
- adaptation fit: this closes the first non-origin repo-doc routing consumer for the bundle's bounded source-lift contract.

## What stayed invariant
- authored documentation and configured doc links remain the source layer.
- the derived reader is route-oriented and bounded.
- the reader output is useful because it points back to source docs instead of embedding all meaning.
- the surface does not claim release policy, status policy, scoring, or filesystem-wide doc discovery authority.

## Risks introduced by adaptation
- an `llms.txt` surface can be mistaken for a full docs authority if maintainers stop routing readers back to source docs.
- a framework module can hide which source set was intentionally selected unless the configuration remains explicit.
- broad "LLM-ready docs" tooling can drift into documentation conversion rather than repo-doc routing; this bundle only uses the bounded route-reader portion.

## Evidence
- `src/runtime/server/routes/llms.txt.get.ts` builds a text route from configured sections and link entries.
- `src/runtime/types.ts` defines section entries with `title`, optional `description`, and linked `href` values, keeping the reader surface route-shaped.
- the public module repository provides a real non-origin implementation of docs-to-reader projection without making the generated reader the authored source of meaning.

## Result
- first second-context adaptation recorded
- keep `AOA-T-0046` promoted until canonical review has more than one fresh extraction proof point and a sharper default-use rationale
