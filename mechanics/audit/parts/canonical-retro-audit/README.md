# Canonical Retro Audit

This part records bounded retro-checks over techniques that are already
`canonical`.

Use it when the question is not "which promoted bundle can move next?", but
"does the current canonical corpus still line up with the canonical-review
contract and its own bundle-local evidence?"

This part does not issue proof verdicts, browse every donor again by default,
or demote techniques from queue pressure. If a future pass finds a real
contradiction, update the bundle-local `notes/canonical-readiness.md` and the
owning `TECHNIQUE.md` first, then reflect the shared audit posture here.

## Review Contract

A canonical retro-audit checks for internal canon fitness, not new promotion
evidence. The minimum corpus-wide checks are:

- `TECHNIQUE.md` status is `canonical`
- frontmatter has `maturity_score: 5`
- frontmatter has `validation_strength: cross_context`
- evidence includes `canonical_readiness`
- evidence includes `adverse_effects_review`
- evidence includes either `second_context` or `external_review`
- the canonical-readiness `Verdict` and `Recommendation` sections approve or
  sustain canonical status
- no `Verdict` or `Recommendation` section still says defer, not approved,
  keep promoted, or not canonical

The check is intentionally stricter than the historical minimum because it is a
retro-audit over already-canonical rows. It can surface stale metadata without
implying that the original canonical decision was wrong.

## 2026-05-14 Corpus Pass

Scope:

- source catalog: `generated/technique_catalog.json`
- corpus size: `107` techniques
- canonical rows checked: `98`
- promoted rows ignored for this pass: `9`
- live external-source rebrowse: not performed in this pass

Result:

- `93` canonical rows were confirmable from current metadata, evidence
  declarations, and bundle-local canonical-readiness verdicts.
- `5` canonical rows were watch rows because metadata lagged the already
  accepted canonical evidence.
- `0` rows were reopen candidates.
- `0` canonical downgrades were justified by this pass.

The five watch rows were metadata drift, not failed canon:

| technique | watch signal | verdict |
|---|---|---|
| `AOA-T-0003 contract-first-smoke-summary` | `validation_strength` still said `source_backed` even though the bundle has second-context evidence and an approved canonical review. | keep canonical; update metadata to `cross_context` |
| `AOA-T-0007 signal-first-gate-promotion` | `validation_strength` still said `source_backed` even though the bundle has concrete second-context reinforcement and an approved canonical review. | keep canonical; update metadata to `cross_context` |
| `AOA-T-0008 published-summary-remediation-snapshot` | `maturity_score` still said `4` even though the bundle is canonical with approved default-use rationale. | keep canonical; update metadata to `5` |
| `AOA-T-0010 telemetry-integrity-snapshot` | `maturity_score` still said `4` even though the bundle is canonical with approved default-use rationale. | keep canonical; update metadata to `5` |
| `AOA-T-0012 deterministic-context-composition` | `maturity_score` still said `4` even though the bundle is canonical with external review, second context, and approved canonical review. | keep canonical; update metadata to `5` |

Confirmable rows:

- `AOA-T-0001`, `AOA-T-0002`, `AOA-T-0004`, `AOA-T-0006`, `AOA-T-0009`, `AOA-T-0011`, `AOA-T-0013`, `AOA-T-0014`, `AOA-T-0015`, `AOA-T-0016`, `AOA-T-0017`, `AOA-T-0018`
- `AOA-T-0019`, `AOA-T-0021`, `AOA-T-0023`, `AOA-T-0024`, `AOA-T-0025`, `AOA-T-0026`, `AOA-T-0027`, `AOA-T-0028`, `AOA-T-0029`, `AOA-T-0030`, `AOA-T-0031`, `AOA-T-0033`
- `AOA-T-0034`, `AOA-T-0036`, `AOA-T-0037`, `AOA-T-0038`, `AOA-T-0039`, `AOA-T-0040`, `AOA-T-0041`, `AOA-T-0043`, `AOA-T-0044`, `AOA-T-0045`, `AOA-T-0046`, `AOA-T-0048`
- `AOA-T-0049`, `AOA-T-0050`, `AOA-T-0051`, `AOA-T-0052`, `AOA-T-0053`, `AOA-T-0054`, `AOA-T-0055`, `AOA-T-0056`, `AOA-T-0057`, `AOA-T-0060`, `AOA-T-0061`, `AOA-T-0062`
- `AOA-T-0063`, `AOA-T-0064`, `AOA-T-0065`, `AOA-T-0066`, `AOA-T-0067`, `AOA-T-0068`, `AOA-T-0069`, `AOA-T-0070`, `AOA-T-0071`, `AOA-T-0072`, `AOA-T-0073`, `AOA-T-0074`
- `AOA-T-0075`, `AOA-T-0076`, `AOA-T-0077`, `AOA-T-0078`, `AOA-T-0079`, `AOA-T-0080`, `AOA-T-0081`, `AOA-T-0082`, `AOA-T-0083`, `AOA-T-0084`, `AOA-T-0085`, `AOA-T-0086`
- `AOA-T-0087`, `AOA-T-0088`, `AOA-T-0089`, `AOA-T-0090`, `AOA-T-0091`, `AOA-T-0092`, `AOA-T-0093`, `AOA-T-0094`, `AOA-T-0095`, `AOA-T-0096`, `AOA-T-0097`, `AOA-T-0098`
- `AOA-T-0099`, `AOA-T-0100`, `AOA-T-0101`, `AOA-T-0102`, `AOA-T-0103`, `AOA-T-0104`, `AOA-T-0105`, `AOA-T-0106`, `AOA-T-0107`

## Interpretation

The pass supports the current canonical corpus. The only corrections are
metadata alignment for five early canonical rows whose bundle-local evidence
already justified canonical status.

Post-fix verification on the regenerated catalog reported `98` confirmable
canonical rows, `0` watch rows, and `0` reopen candidates.

The pass also marks a boundary for future work: if the next question is whether
external public sources still exist, open a separate live-source freshness pass.
Do not treat that as the same job as internal canonical-status coherence.

## Next Honest Trigger

Reopen this part when one of these changes:

- a canonical bundle's `canonical-readiness.md` is edited
- a canonical bundle's status, maturity, validation strength, or evidence list
  changes
- a release changes the canonical count
- a future pass needs live external-source freshness checks for all canonical
  evidence anchors
