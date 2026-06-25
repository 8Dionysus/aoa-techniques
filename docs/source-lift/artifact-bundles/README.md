# Source-Lift Artifact Bundles

This directory holds OS Abyss artifact-bundle input manifests for public
source-lift export surfaces owned by `aoa-techniques`.

The manifests are transport and trust envelopes. They do not make generated
exports stronger than authored `TECHNIQUE.md` bundles, and they do not define
KAG substrate behavior.

Current bundle:

- `kag_export.bundle.json` wraps `generated/kag_export.min.json` as
  `source_owned_kag_export_capsule` with ABI identity, SLSA/in-toto generation
  provenance, durable evidence promotion, materialized subject-store checks,
  fail-closed consumer trust-gate selection, and explicit
  no-SBOM/no-Sigstore/no-C2PA deferrals.

Validate with:

```bash
python scripts/validate_abyss_machine_kag_export_bundle.py
```
