# Second Context Adaptation

## Technique
- id: AOA-T-0072
- name: perceptual-media-dedupe-with-threshold-review

## Target project
- name: aoa-techniques
- environment: public technique repository with authored bundle contracts, generated routing surfaces, and validator-backed markdown discipline
- runtime: documentation-first corpus that records the bounded duplicate-grouping pattern rather than shipping donor CLIs, ANN indexes, or delete prompts
- live reinforcement: `qarmin/czkawka` at commit `612c93a6904e819d598f56c59c1f3be75ab42d25` repeats the same perceptual image grouping seam in MIT-licensed core and CLI surfaces, while mixed-license GUI/assets/product layers stay evidence-only and out of the technique

## What changed

- donor dedupe tools were reduced to one portable grouping-and-review contract rather than one cleanup command-line workflow
- delete prompts, preserve defaults, and ANN implementation details were removed from the reusable public bundle
- semantic classification and quality ranking were kept out so the adaptation remains about duplicate grouping only
- the bundle was reduced to one technique doc, one checklist, one example, and bounded evidence notes
- Pack 29 promoted the adaptation to a cross-context canonical default after Czkawka confirmed thresholded perceptual grouping with reviewable grouped output outside the original donor family

## What stayed invariant

- perceptual similarity remains the basis for near-duplicate grouping
- thresholds remain explicit and tunable
- uncertain matches remain visible rather than being silently resolved
- later file actions remain separate from grouping

## Risks introduced by adaptation

- the technique can collapse into cleanup policy if later users stop separating grouping from delete or archive actions
- teams may over-associate the technique with one donor hash family if the grouping contract is not kept generic
- borderline groups can look more authoritative than they are if review evidence becomes too thin

## Evidence

- imagededup's README presents near-duplicate discovery over perceptual hashing or CNN encodings and keeps duplicate output as a reviewable map rather than a fixed deletion policy
- imgdupes' README presents thresholded perceptual-hash grouping and explicitly separates list output from optional preserve-or-delete prompts
- both donors show why duplicate grouping can remain useful before any later cleanup action or taxonomy choice is finalized
- Czkawka's Similar Images path finds non-identical but visually similar images, exposes `max_difference` as a strictness threshold, supports hash algorithm and hash-size tuning, emits grouped image results with similarity labels derived from per-entry difference, supports JSON or text result output, and keeps deletion as a separate default-off option
- inspected Czkawka files: `README.md`, `Changelog.md`, MIT license files for the relevant core/CLI surfaces, `czkawka_core/src/tools/similar_images/mod.rs`, `core.rs`, `traits.rs`, `tests.rs`, and `czkawka_cli/src/commands.rs` plus `main.rs`

## Result

- works as a documentation-first adaptation with live public reinforcement and preserves the bounded core without carrying over donor CLI behavior, Czkawka delete methods, GUI behavior, cache layout, mixed-license assets, or runtime indexing detail
