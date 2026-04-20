# AGENTS.md

Guidance for coding agents and humans working under `generated/`.

## Purpose

`generated/` stores committed derived reader surfaces built from authored sources elsewhere in the repository.

Representative surfaces include `generated/technique_catalog.json`, `generated/technique_promotion_readiness.min.json`, `generated/technique_capsules.json`, `generated/repo_doc_surface_manifest.json`, `generated/kag_export.json`, `generated/agon_technique_binding_candidates.min.json`, the section and checklist manifests, the example and evidence-note manifests, and the semantic/shadow review manifests.

## Core rule

Do not hand-edit files in this directory as if they were canonical prose.
Change the owning source object or the generator, then regenerate the derived output.

## Derivation posture

Keep minified and full surfaces aligned.
Keep generated wording subordinate to authored bundle meaning, docs meaning, and review meaning.
If one generated output drifts, repair the source or generator rather than patching only one committed artifact.
Do not treat candidate-bridge indexes as if they were promoted technique
catalogs or canonical practice bundles.

## Validation

After `python -m pip install -r requirements-dev.txt`, changes here or to the generators that feed this directory should run the smallest covering commands. Common paths include:

- `python scripts/build_catalog.py`
- `python scripts/build_promotion_readiness.py`
- `python scripts/build_capsules.py`
- `python scripts/build_repo_doc_surface_manifest.py`
- `python scripts/build_kag_export.py`
- `python scripts/build_agon_technique_binding_candidates.py --check`
- `python scripts/validate_agon_technique_binding_candidates.py`
- `python scripts/validate_nested_agents.py`
- `python scripts/release_check.py`

## Hard NO

Do not:

- store new canonical doctrine only in `generated/`
- leave min and full files out of sync
- add secret-bearing exports or hidden provenance
- pretend a generated summary replaces the authored source of truth
