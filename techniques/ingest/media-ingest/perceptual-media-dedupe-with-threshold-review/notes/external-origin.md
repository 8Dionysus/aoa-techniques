# External Origin Note

Use this note when a technique is adapted from an external open-source or public documentation source.
It complements `TECHNIQUE.md` and records provenance, adaptation boundaries, and public-safety review.

## Source

- source_repo: `https://github.com/idealo/imagededup` plus `https://github.com/knjcode/imgdupes`
- source_license: `Apache-2.0 + MIT` donor family
- inspired_by: not used in this import
- adapted_from: upstream README guidance from imagededup and imgdupes showing perceptual near-duplicate discovery, threshold tuning, group display, and optional later delete actions

## What changed

- what_changed: narrowed the donor family to one bounded media-dedupe seam: perceptual similarity forms near-duplicate groups and borderline cases remain visible through review buckets
- reusable object extracted: one reviewable duplicate-grouping surface with high-confidence groups, uncertain groups, and explicit threshold posture
- invariant core kept: similarity-based grouping stays explicit, thresholds remain tunable, and later file actions remain separate
- project-shaped details removed or generalized: donor CLI flags, delete prompts, approximate-nearest-neighbor implementation detail, container packaging, and one-threshold cleanup doctrine
- nearest existing technique or overlap watch: `semantic-media-bucketing-with-vision-plus-ocr`
- what stays out of the donor: semantic taxonomy, deletion or archive policy, ranking or quality-scoring doctrine, and donor-specific runtime packaging

## Public-safety review

- secrets or tokens removed: none from the donor surfaces used for this import
- private paths, URLs, or IDs removed: none; the donor inputs are public upstream repositories and public README documentation
- environment-specific assumptions generalized: the public technique does not depend on one hash implementation, one ANN backend, one CLI prompt model, or one storage layout
- remaining public-safety concerns: the main risks are drift into automatic cleanup policy on one side and drift into semantic media taxonomy or ranking doctrine on the other

## Review notes

- why this adaptation is reusable here: many screenshot, meme, and photo collections need near-duplicate grouping to stay visible and reviewable before any preserve, delete, or archive decision happens
- downstream repo impact: later action policies or cleanup workflows belong in `aoa-skills`, while this repository keeps only the reusable grouping contract
- limits or follow-up review concerns: this import still needs one second live adopter beyond the donor dedupe family and documentation-first adaptation before any canonical discussion is honest
