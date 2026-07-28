# Documentation Map

This is the map for the `docs/` district of `aoa-techniques`.

Use the root [README](../README.md) as the public front door, [START_HERE](START_HERE.md)
as the shortest repo-owned route, and this file when you already know you are
inside `docs/` and need the right owner surface.

Editing under `docs/` starts with [AGENTS](AGENTS.md), then the placement rules
in [ROOT_SURFACE_LAW](ROOT_SURFACE_LAW.md), [THEMATIC_DISTRICT_PROTOCOL](guardrails/THEMATIC_DISTRICT_PROTOCOL.md),
and [CURRENT_SURFACE_INDEX](guardrails/CURRENT_SURFACE_INDEX.md).

## Start Here

For the shortest repo overview, read:

1. [README](../README.md)
2. [Charter](../CHARTER.md)
3. [Start Here](START_HERE.md)
4. [TECHNIQUE_INDEX](../TECHNIQUE_INDEX.md)
5. [Technique Selection](readers/selection/TECHNIQUE_SELECTION.md)

For design shape, add [DESIGN](../DESIGN.md) and [DESIGN.AGENTS](../DESIGN.AGENTS.md).
For the compact repo-doc reader, open [REPO_DOC_SURFACES](readers/repo/REPO_DOC_SURFACES.md):
its [repo_doc_surface_manifest.json](../generated/repo_doc_surface_manifest.json)
lifts the 20 authoritative public route/canon/status files into routing knowledge only.

## Root Docs

| Surface | Owns |
|---|---|
| [AGENTS](AGENTS.md) | docs-local route card |
| [README](README.md) | this district map |
| [START_HERE](START_HERE.md) | shortest self-serve route |
| [ROOT_SURFACE_LAW](ROOT_SURFACE_LAW.md) | root and docs-root placement law |
| [ECOSYSTEM_CONTEXT](ECOSYSTEM_CONTEXT.md) | technique layer position in AoA |
| [DOMAIN_MAP](DOMAIN_MAP.md) | current domain meanings |
| [TECHNIQUE_ATOM_CONTRACT](TECHNIQUE_ATOM_CONTRACT.md) | one atomic executable technique |
| [TECHNIQUE_TOPOLOGY_CONTRACT](TECHNIQUE_TOPOLOGY_CONTRACT.md) | faceted classification |
| [TECHNIQUE_TREE_CONTRACT](TECHNIQUE_TREE_CONTRACT.md) | authored corpus path architecture |
| [RELEASING](RELEASING.md) | release-prep route |

## Districts

| District | Use first when |
|---|---|
| [guardrails](guardrails/README.md) | placement, link hygiene, generated-reader limits, or AGENTS mesh shape is in question |
| [decisions](decisions/README.md) | the reader needs why a durable route, owner split, or validator exists |
| [review](review/README.md) | maturity, promotion, semantic-review, shadow, or caution interpretation is in scope |
| [selection](selection/README.md) | choosing, kind routing, handoff, or runtime capsule use is in scope |
| [source-lift](source-lift/README.md) | KAG/source-lift contracts are in scope |
| [readers](readers/README.md) | generated Markdown reader companions are needed |

Guardrails are concentrated in [THEMATIC_DISTRICT_PROTOCOL](guardrails/THEMATIC_DISTRICT_PROTOCOL.md),
[LINK_AND_SHAPE_HYGIENE_PROTOCOL](guardrails/LINK_AND_SHAPE_HYGIENE_PROTOCOL.md),
[HYGIENE_GUARDRAIL_INDEX](guardrails/HYGIENE_GUARDRAIL_INDEX.md),
[AGENTS_MESH_PROTOCOL](guardrails/AGENTS_MESH_PROTOCOL.md), and
[AGENTS_MESH_INDEX](guardrails/AGENTS_MESH_INDEX.md).

## Reader Routes

| Reader family | Contract | Reader or manifest |
|---|---|---|
| Repo docs | [REPO_DOC_SURFACE_LIFT_GUIDE](source-lift/REPO_DOC_SURFACE_LIFT_GUIDE.md) | [REPO_DOC_SURFACES](readers/repo/REPO_DOC_SURFACES.md), [repo_doc_surface_manifest.json](../generated/repo_doc_surface_manifest.json) |
| Selection and kind | [TECHNIQUE_SELECTION_GUIDE](selection/TECHNIQUE_SELECTION_GUIDE.md), [TECHNIQUE_KIND_GUIDE](selection/TECHNIQUE_KIND_GUIDE.md), [TECHNIQUE_KIND_HANDOFF_PACK](selection/TECHNIQUE_KIND_HANDOFF_PACK.md) | [TECHNIQUE_SELECTION](readers/selection/TECHNIQUE_SELECTION.md), [SELECTION_PATTERNS](readers/selection/SELECTION_PATTERNS.md), [TECHNIQUE_KINDS](readers/kind/TECHNIQUE_KINDS.md) |
| Capsule | [TECHNIQUE_CAPSULE_GUIDE](selection/TECHNIQUE_CAPSULE_GUIDE.md) | [TECHNIQUE_CAPSULES](readers/runtime/TECHNIQUE_CAPSULES.md), [technique_capsules.json](../generated/technique_capsules.json), [technique_capsules.min.json](../generated/technique_capsules.min.json) |
| Technique Intelligence | [TECHNIQUE_INTELLIGENCE_GUIDE](selection/TECHNIQUE_INTELLIGENCE_GUIDE.md) | [TECHNIQUE_INTELLIGENCE](readers/intelligence/TECHNIQUE_INTELLIGENCE.md), [technique_intelligence_registry.json](../generated/technique_intelligence_registry.json), [technique_intelligence_dag.json](../generated/technique_intelligence_dag.json) |
| KAG/source lift | [KAG_SOURCE_LIFT_GUIDE](source-lift/KAG_SOURCE_LIFT_GUIDE.md) | [TECHNIQUE_SECTIONS](readers/source-lift/TECHNIQUE_SECTIONS.md), [TECHNIQUE_SECTION_LIFT_GUIDE](source-lift/TECHNIQUE_SECTION_LIFT_GUIDE.md), [technique_section_manifest.json](../generated/technique_section_manifest.json), [TECHNIQUE_CHECKLISTS](readers/source-lift/TECHNIQUE_CHECKLISTS.md), [TECHNIQUE_CHECKLIST_LIFT_GUIDE](source-lift/TECHNIQUE_CHECKLIST_LIFT_GUIDE.md), [technique_checklist_manifest.json](../generated/technique_checklist_manifest.json), [TECHNIQUE_EXAMPLES](readers/source-lift/TECHNIQUE_EXAMPLES.md), [TECHNIQUE_EXAMPLE_LIFT_GUIDE](source-lift/TECHNIQUE_EXAMPLE_LIFT_GUIDE.md), [technique_example_manifest.json](../generated/technique_example_manifest.json), [EVIDENCE_NOTE_SURFACES](readers/source-lift/EVIDENCE_NOTE_SURFACES.md), [technique_evidence_note_manifest.json](../generated/technique_evidence_note_manifest.json) |
| Semantic and shadow review | [SEMANTIC_REVIEW_GUIDE](review/SEMANTIC_REVIEW_GUIDE.md), [TECHNIQUE_SHADOW_GUIDE](review/TECHNIQUE_SHADOW_GUIDE.md) | [Shadow Patterns](readers/review/SHADOW_PATTERNS.md), [SHADOW_PATTERNS.md](readers/review/SHADOW_PATTERNS.md), [shadow_review_manifest.json](../generated/shadow_review_manifest.json), and the [review packet route](review/README.md) for mechanic-owned authored packets |

Generated JSON belongs in [generated](../generated/). Generated Markdown
readers belong under [readers](readers/README.md). Authored contracts stay in
their owning docs district.

## Lift Anchors

Reusable KAG/source-lift technique bundles live under
`../techniques/knowledge-lift/kag-source-lift/`:

| Bundle | Use |
|---|---|
| [markdown-technique-section-lift](../techniques/knowledge-lift/kag-source-lift/markdown-technique-section-lift/TECHNIQUE.md) | lift authored technique sections into bounded readers and manifests |
| [frontmatter-metadata-spine](../techniques/knowledge-lift/kag-source-lift/frontmatter-metadata-spine/TECHNIQUE.md) | keep metadata lift bounded to authored frontmatter |
| [evidence-note-provenance-lift](../techniques/knowledge-lift/kag-source-lift/evidence-note-provenance-lift/TECHNIQUE.md) | lift evidence-note shapes without replacing notes |
| [bounded-relation-lift-for-kag](../techniques/knowledge-lift/kag-source-lift/bounded-relation-lift-for-kag/TECHNIQUE.md) | lift direct relations without graph inference |
| [risk-and-negative-effect-lift](../techniques/knowledge-lift/kag-source-lift/risk-and-negative-effect-lift/TECHNIQUE.md) | lift caution material without policy scoring |

## Claim Routes

| Question | Route |
|---|---|
| Does the candidate belong here? | [Charter](../CHARTER.md), then [TECHNIQUE_ATOM_CONTRACT](TECHNIQUE_ATOM_CONTRACT.md) |
| Is it one atomic technique? | [TECHNIQUE_ATOM_CONTRACT](TECHNIQUE_ATOM_CONTRACT.md) |
| Which domain, kind, family, or relation applies? | [TECHNIQUE_TOPOLOGY_CONTRACT](TECHNIQUE_TOPOLOGY_CONTRACT.md), [TECHNIQUE_KIND_GUIDE](selection/TECHNIQUE_KIND_GUIDE.md), [TECHNIQUE_KIND_HANDOFF_PACK](selection/TECHNIQUE_KIND_HANDOFF_PACK.md) |
| Where should the bundle live? | [TECHNIQUE_TREE_CONTRACT](TECHNIQUE_TREE_CONTRACT.md), then [TECHNIQUE_INDEX](../TECHNIQUE_INDEX.md) |
| Is canonical status justified? | [CANONICAL_REVIEW_GUIDE](review/CANONICAL_REVIEW_GUIDE.md), [CANONICAL_RUBRIC](review/CANONICAL_RUBRIC.md), then [Mechanics](../mechanics/README.md) or [Audit](../mechanics/audit/README.md) |
| Which generated reader is safe to use? | [REPO_DOC_SURFACES](readers/repo/REPO_DOC_SURFACES.md), [TECHNIQUE_SELECTION](readers/selection/TECHNIQUE_SELECTION.md), [TECHNIQUE_CAPSULES](readers/runtime/TECHNIQUE_CAPSULES.md), or [TECHNIQUE_INTELLIGENCE](readers/intelligence/TECHNIQUE_INTELLIGENCE.md), then the source bundle |
| Why was a route chosen? | [decisions](decisions/README.md) |

## Change Routes

| Change | First route |
|---|---|
| Root or docs placement | [ROOT_SURFACE_LAW](ROOT_SURFACE_LAW.md), [THEMATIC_DISTRICT_PROTOCOL](guardrails/THEMATIC_DISTRICT_PROTOCOL.md), [CURRENT_SURFACE_INDEX](guardrails/CURRENT_SURFACE_INDEX.md) |
| Technique authoring or promotion | [TECHNIQUE_ATOM_CONTRACT](TECHNIQUE_ATOM_CONTRACT.md), [TECHNIQUE_TOPOLOGY_CONTRACT](TECHNIQUE_TOPOLOGY_CONTRACT.md), [CANONICAL_REVIEW_GUIDE](review/CANONICAL_REVIEW_GUIDE.md) |
| Generated reader parity | source doc, builder, generated output, validator, and test together |
| KAG/source-lift contract | [source-lift](source-lift/README.md), then the matching guide |
| Review contract | [review](review/README.md), then the matching guide |
| Selection or kind behavior | [selection](selection/README.md), then the matching guide |
| Decision rationale | [decisions/AGENTS](decisions/AGENTS.md), [decisions/README](decisions/README.md) |
| Public release path | [RELEASING](RELEASING.md), then [CHANGELOG](../CHANGELOG.md) |
| Mechanic-owned evidence or movement | [mechanics/README.md](../mechanics/README.md), then the owning mechanic `AGENTS.md` |

Mechanic runbooks, candidate ledgers, review packets, Agon bridges, and
antifragility practice bridges stay in [Mechanics](../mechanics/README.md).

## Recommended Reading Paths

1. [README](../README.md)
2. [Charter](../CHARTER.md)
3. [Start Here](START_HERE.md)
4. [TECHNIQUE_INDEX](../TECHNIQUE_INDEX.md)
5. [Technique Selection](readers/selection/TECHNIQUE_SELECTION.md)

For authoring, read [Technique Atom Contract](TECHNIQUE_ATOM_CONTRACT.md),
[Technique Topology Contract](TECHNIQUE_TOPOLOGY_CONTRACT.md),
[Technique Tree Contract](TECHNIQUE_TREE_CONTRACT.md), then one current bundle
with its `checks/`, `examples/`, and `notes/`.

For generated-reader work, read the matching source-lift guide first. Then open
one family guide such as [Technique Section Lift Guide](source-lift/TECHNIQUE_SECTION_LIFT_GUIDE.md),
one reader or manifest such as [Technique Sections](readers/source-lift/TECHNIQUE_SECTIONS.md),
and one reusable lift bundle in `../techniques/knowledge-lift/kag-source-lift/`.

For review work, read [Review Guides](review/README.md), then the specific
canonical, semantic, or shadow guide before opening mechanic-owned packets.

## Adjacent Routes

| Route | Use |
|---|---|
| [mechanics](../mechanics/README.md) | practice movement around the technique canon |
| [examples](../examples/README.md) | root-owned public worked examples |
| [generated](../generated/) | compact machine companions |
| [scripts](../scripts/) | builders, validators, and release checks |
| [tests](../tests/AGENTS.md) | repo-wide validation |
| [templates](../templates/) | technique authoring and promotion scaffolds |
| [legacy](../legacy/README.md) | repo-wide public-safe raw, archive, and migration receipts |

Neighboring AoA repositories own adjacent object classes:
[aoa-skills](https://github.com/8Dionysus/aoa-skills),
[aoa-evals](https://github.com/8Dionysus/aoa-evals),
[aoa-sdk](https://github.com/8Dionysus/aoa-sdk),
[aoa-playbooks](https://github.com/8Dionysus/aoa-playbooks), and
[Agents-of-Abyss](https://github.com/8Dionysus/Agents-of-Abyss).

## Notes

- Prefer [Start Here](START_HERE.md) when the question is where to begin.
- Prefer [Current Surface Index](guardrails/CURRENT_SURFACE_INDEX.md) when the question is why a flat `docs/*.md` file still exists.
- Prefer [Root Surface Law](ROOT_SURFACE_LAW.md) before adding, moving, or deleting root or docs-root surfaces.
- Prefer [Decisions District](decisions/README.md) when the question is why a structural route was chosen.
- Prefer [Root Legacy](../legacy/README.md) and [Root Legacy Index](../legacy/INDEX.md) for public-safe receipts, archives, and migration history.
