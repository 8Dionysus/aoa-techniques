# Selection Guides

This district holds active guide contracts for choosing, classifying, handing
off, and compactly reading techniques.

Use it when the question is how selection readers, the `kind` axis, handoff
contracts, or capsule lookup surfaces should behave without replacing authored
`TECHNIQUE.md` meaning.

## Surfaces

| Surface | Role |
|---|---|
| [Technique Selection Guide](TECHNIQUE_SELECTION_GUIDE.md) | bounds chooser surfaces and generated selection readers |
| [Technique Kind Guide](TECHNIQUE_KIND_GUIDE.md) | defines the current bounded second selector axis |
| [Technique Kind Handoff Pack](TECHNIQUE_KIND_HANDOFF_PACK.md) | explains how neighboring AoA repos may consume `domain + kind` |
| [Technique Capsule Guide](TECHNIQUE_CAPSULE_GUIDE.md) | bounds derived runtime lookup cards |

## Owner Split

Authored technique meaning remains in `../../techniques/**/TECHNIQUE.md`.
Generated reader companions remain under `../readers/`.
Generated JSON remains under `../../generated/`.
Review and caution contracts remain under `../review/`.

This district owns selection and compact-use contracts only. It does not own
skill workflows, proof doctrine, routing policy, KAG semantics, memory recall,
or runtime behavior.

## Reading Routes

Selection route:

1. [Technique Selection Guide](TECHNIQUE_SELECTION_GUIDE.md)
2. [Technique Selection](../readers/selection/TECHNIQUE_SELECTION.md)
3. [Selection Patterns](../readers/selection/SELECTION_PATTERNS.md)
4. [TECHNIQUE_INDEX](../../TECHNIQUE_INDEX.md)

Kind and handoff route:

1. [Technique Kind Guide](TECHNIQUE_KIND_GUIDE.md)
2. [Technique Kinds](../readers/kind/TECHNIQUE_KINDS.md)
3. [Technique Kind Handoff Pack](TECHNIQUE_KIND_HANDOFF_PACK.md)
4. [kind registry](../../config/technique_kind_registry.yaml)

Capsule route:

1. [Technique Capsule Guide](TECHNIQUE_CAPSULE_GUIDE.md)
2. [Technique Capsules](../readers/runtime/TECHNIQUE_CAPSULES.md)
3. [technique capsules min JSON](../../generated/technique_capsules.min.json)

Agent read order, validation, and closeout live in [AGENTS](AGENTS.md).
