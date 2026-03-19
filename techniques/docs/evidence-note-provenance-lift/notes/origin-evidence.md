# Origin Evidence

## Technique
- id: AOA-T-0020
- name: evidence-note-provenance-lift

## Source project
- name: aoa-techniques
- source files:
  - `scripts/build_evidence_note_manifest.py`
  - `generated/technique_evidence_note_manifest.json`
  - `docs/EVIDENCE_NOTE_PROVENANCE_GUIDE.md`

## Evidence
- `scripts/build_evidence_note_manifest.py` already lifts typed note roles into a derived provenance surface while preserving note-level context
- `generated/technique_evidence_note_manifest.json` shows the current repo already consumes note roles and paths as bounded provenance handles
- `docs/EVIDENCE_NOTE_PROVENANCE_GUIDE.md` explicitly frames the note layer as provenance-first and keeps note IDs, note graphs, and flattened semantics deferred

## Interpretation
- the live repository already uses note files as typed supporting evidence rather than as unstructured attachment clutter
- the reusable pattern is bounded provenance lookup from markdown notes, not a claim that note manifests replace authored review context
