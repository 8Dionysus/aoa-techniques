# Technique Kind Handoff Pack

This pack is the human-first handoff surface for the `kind` axis.

Use it when an adjacent AoA repo needs to consume `domain + kind` without copying technique meaning out of `aoa-techniques`.

## What This Pack Is For

The `kind` axis is a bounded second selector inside a chosen `domain`.
`domain` still answers ownership and first routing.
`kind` answers what reusable practice shape the technique is.

For future machine-facing adoption, the reference surface is:

- [`../generated/technique_kind_manifest.min.json`](../generated/technique_kind_manifest.min.json)

For authored doctrine and authoring rules, the source surfaces remain:

- [`TECHNIQUE_KIND_GUIDE.md`](TECHNIQUE_KIND_GUIDE.md)
- [`../config/technique_kind_registry.yaml`](../config/technique_kind_registry.yaml)

## How Neighbor Repos Should Read It

### `aoa-skills`

Use `domain + kind` to help choose which technique should be wrapped, loaded, or composed into a skill workflow.

The useful question is not "which technique exists?"
The useful question is "which bounded practice shape should become the next skill-adjacent action?"

Keep this as a selection hint, not an execution contract.
`aoa-skills` still owns bounded execution behavior, packaging, and invocation discipline.

### `aoa-routing`

Use `domain + kind` as the second cut after owner-layer/domain choice.

That means:

- `domain` gets you to the right owner layer first
- `kind` helps narrow the next surface within that layer
- the result should stay a routing hint, not a traversal engine

This pack is intentionally aligned with bounded next-surface guidance, not graph semantics.

### `aoa-evals`

Treat `kind` as optional context only.

It can help a proof reader understand whether a technique is mainly a workflow, guardrail, validation, artifact, lift, or handoff shape.
It should not become proof doctrine, claim classification, or a substitute for eval-owned verdict surfaces.

## What Not To Do

- do not treat `kind` as promotion status
- do not use `kind` to smuggle role, scenario, or execution-package meaning into `aoa-techniques`
- do not assume `family` exists outside scout reports
- do not copy the registry into neighboring repos as a second source of truth
- do not replace authored technique meaning with a consumer-side interpretation layer
- do not widen `kind` into a freeform taxonomy for every adjacent use case

## Adoption Rule

If a neighboring repo wants to consume this axis, it should read the manifest and registry, then keep its own consumption contract narrow.

The expected adoption shape is:

1. inspect `generated/technique_kind_manifest.min.json`
2. consult the human pack here when the selection path is ambiguous
3. keep neighboring repo meaning local to that repo
4. return to `aoa-techniques` only when the technique contract itself needs clarification

## Boundaries

This pack does not add new frontmatter, schema fields, or validator requirements.

It is weaker than bundle frontmatter by design and weaker than the canonical registry by design.
It exists to make the handoff legible, not to become a second authority.
