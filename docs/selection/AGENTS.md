# AGENTS.md

## Applies to

This card applies to `docs/selection/` and every descendant unless a nearer
`AGENTS.md` narrows the path.

## Role

`docs/selection/` owns active guide contracts for choosing, classifying,
handing off, and compactly reading techniques.

It explains selection surfaces, the `kind` axis, neighboring-repo handoff
posture, and capsule lookup boundaries. It does not own authored technique
meaning, generated-reader output, review doctrine, or sibling-repo execution
contracts.

## Read before editing

Read root `AGENTS.md`, `DESIGN.md`, `docs/AGENTS.md`,
`docs/ROOT_SURFACE_LAW.md`, and this district [README](README.md).

For selector or kind changes, also read:

- [Technique Selection Guide](TECHNIQUE_SELECTION_GUIDE.md)
- [Technique Kind Guide](TECHNIQUE_KIND_GUIDE.md)
- [Technique Kind Handoff Pack](TECHNIQUE_KIND_HANDOFF_PACK.md)
- [Technique Topology Contract](../TECHNIQUE_TOPOLOGY_CONTRACT.md)
- [Technique Selection](../readers/selection/TECHNIQUE_SELECTION.md)
- [Technique Kinds](../readers/kind/TECHNIQUE_KINDS.md)

For capsule changes, also read:

- [Technique Capsule Guide](TECHNIQUE_CAPSULE_GUIDE.md)
- [Technique Capsules](../readers/runtime/TECHNIQUE_CAPSULES.md)

For Technique Intelligence changes, also read:

- [Technique Intelligence Guide](TECHNIQUE_INTELLIGENCE_GUIDE.md)
- [Technique Intelligence](../readers/intelligence/TECHNIQUE_INTELLIGENCE.md)

## Boundaries

- Keep selection one-step and bundle-level; do not turn direct relations into
  graph traversal.
- Keep `kind` singular and registry-backed; do not widen it into family,
  substrate, capability, status, or risk posture.
- Keep handoff guidance weaker than neighboring owner truth.
- Keep capsules as derived lookup cards, not as authored technique meaning,
  scoring, policy routing, or KAG/source-lift exports.
- Keep Technique Intelligence as source-linked query, explanation, packing,
  and navigation over atomic moves; do not turn it into execution workflow,
  proof verdict, graph truth, or activation shape.

## Validation

For selection, kind, capsule, or intelligence guide changes, run the affected
builder first when source-backed readers move:

```bash
python scripts/build_catalog.py
python scripts/build_kind_manifest.py
python scripts/build_capsules.py
python scripts/build_technique_intelligence.py
python scripts/validate_repo.py
```

For broad route or release-visible changes, run `python scripts/release_check.py`.

## Closeout

Report which selector, kind, handoff, capsule, or intelligence contract moved;
which generated readers were rebuilt; which checks ran; and whether any
neighboring repo owner needs a handoff update.
