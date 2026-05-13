# Canonical Readiness

## Technique
- id: AOA-T-0072
- name: perceptual-media-dedupe-with-threshold-review

## Verdict
- approve for canonical promotion

## Evidence summary

- external origin: the imported technique has a bounded donor contract and explicit exclusions around delete policy, semantic taxonomy, ranking doctrine, and donor runtime detail
- second context: `aoa-techniques` now records the same duplicate-grouping seam as a documentation-first adaptation with one example and one checklist
- external review: the first import review passed and confirmed the technique is public-safe and bounded at the current scale
- `qarmin/czkawka` provides exact-fit public reinforcement beyond the `imagededup` and `imgdupes` donor family: its Similar Images surface finds images that are visually similar rather than byte-identical, exposes an explicit `max_difference` threshold, supports perceptual hash algorithm and hash-size tuning, groups similar image entries with per-entry difference and similarity labels, can print or save grouped results as JSON, and keeps deletion as a separate option with `NONE` as the default
- Czkawka's inspected public source has MIT-licensed core and CLI surfaces at commit `612c93a6904e819d598f56c59c1f3be75ab42d25`; the repository has mixed licensing for non-core assets and GUI/application layers, so this bundle uses it as evidence only and does not import code, GUI behavior, icons, audio, app workflow, cache layout, delete method names, or product cleanup posture. Inspected files include `README.md` (`35eb6f82a24537bca7733f1124e8a7e7dcec00a1`), `Changelog.md` (`3e958cb054e57c07c92e5a07e4d183472bc91f1a`), `LICENSE_MIT_EVERYTHING_OUTSIDE_ANY_CARGO_APP_LIBRARY` (`ca43755e89be613ff2d2de1ebb30a1e57bf6d62c`), `czkawka_core/LICENSE_MIT` (`ca43755e89be613ff2d2de1ebb30a1e57bf6d62c`), `czkawka_core/src/tools/similar_images/mod.rs` (`7bdbabc24a683b3a159d2eb748f809b1446c5bd9`), `czkawka_core/src/tools/similar_images/core.rs` (`7395386e1f33706d525304b1d36f71c2a7137abe`), `czkawka_core/src/tools/similar_images/traits.rs` (`e8598e4d0a9aa0fe369a2f6ffa070f516f1cf9d8`), `czkawka_core/src/tools/similar_images/tests.rs` (`7ecf281eb562ce3af0514f7b731577fb4685f736`), `czkawka_cli/src/commands.rs` (`d367b1f85a1cb348b6f0f796f8d8cc9f6bf4419f`), and `czkawka_cli/src/main.rs` (`f6009b32e171fe75c3c729db17007612630d540b`)
- adjacent lanes were checked and kept out of the canonical proof: Czkawka's duplicate files, music, video, empty-folder, cleanup, GUI selection, cache, and hardlink/delete paths are product or sibling behavior, not part of this technique; the reusable proof is only the thresholded perceptual image grouping and visible review output seam
- validation strength: the bundle now carries one checklist, one example, a clean external-origin note, a documentation-first second context, and public cross-context reinforcement that repeats bounded perceptual dedupe outside the donor dedupe family

## Default-use rationale

- this is the right canonical default when the main problem is grouping near-duplicate media while keeping borderline matches visible and later file actions separate
- it remains narrower than a later semantic bucketing technique because it does not assign media taxonomy
- it also remains narrower than cleanup automation because it stops at duplicate grouping and review signals rather than preserve or delete decisions
- it is now strong enough as a canonical default because the second public context repeats the key shape: perceptual similarity produces candidate groups, thresholds tune strictness, grouped results preserve enough evidence for review, and file actions stay separate from the grouping contract

## Fresh public-safety check

- review date: 2026-05-12
- result: pass
- sanitization still holds: the bundle keeps only the reusable duplicate-grouping seam and excludes donor CLI behavior, delete defaults, ANN backend detail, and cleanup governance
- public reuse check: the example, checklist, and adaptation notes remain understandable without hidden donor-repo context; Czkawka is cited only as public evidence, and the technique does not copy its Rust source, GUI application flow, mixed-license assets, cleanup commands, cache format, delete strategies, or broader media-management product behavior

## Remaining gaps

- no blocker remains for canonical status
- future sources can reinforce the default, but they must preserve the narrow boundary: bounded media set, perceptual similarity, explicit threshold or similarity bands, reviewable groups or candidate pairs, and a stop-line before cleanup policy, archive policy, semantic taxonomy, ranking, quality scoring, or full media-management products

## Recommendation

- move `AOA-T-0072` to `canonical`
- add an adverse-effects review to preserve the boundary between thresholded perceptual grouping, review output, cleanup/delete policy, semantic media bucketing, quality ranking, and media-management products
