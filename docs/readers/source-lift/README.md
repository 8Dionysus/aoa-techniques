# Source-Lift Readers

This district holds generated Markdown reader companions for source-lift
families.

The guide surfaces stay in `docs/source-lift/` because they are authored
contracts. The reader companions live here because they are bulky,
builder-backed lookup surfaces.

| Reader | Builder surface | Source contract |
|---|---|---|
| [Technique Sections](TECHNIQUE_SECTIONS.md) | [build_section_manifest.py](../../../scripts/build_section_manifest.py) | [Technique Section Lift Guide](../../source-lift/TECHNIQUE_SECTION_LIFT_GUIDE.md) |
| [Technique Checklists](TECHNIQUE_CHECKLISTS.md) | [build_checklist_manifest.py](../../../scripts/build_checklist_manifest.py) | [Technique Checklist Lift Guide](../../source-lift/TECHNIQUE_CHECKLIST_LIFT_GUIDE.md) |
| [Technique Examples](TECHNIQUE_EXAMPLES.md) | [build_example_manifest.py](../../../scripts/build_example_manifest.py) | [Technique Example Lift Guide](../../source-lift/TECHNIQUE_EXAMPLE_LIFT_GUIDE.md) |
| [Evidence Note Surfaces](EVIDENCE_NOTE_SURFACES.md) | [build_evidence_note_manifest.py](../../../scripts/build_evidence_note_manifest.py) | [Evidence Note Provenance Guide](../../source-lift/EVIDENCE_NOTE_PROVENANCE_GUIDE.md) |

Generated JSON remains in [generated](../../../generated/). Authored technique
meaning remains in [techniques](../../../techniques/).
Use [readers AGENTS](../AGENTS.md#validation) for the exact build and
validation lane.
