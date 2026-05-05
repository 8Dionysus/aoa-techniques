# minimal-perceptual-media-dedupe-with-threshold-review

Input media set:
- `meme-original.png`
- `meme-recompressed.jpg`
- `meme-cropped.png`
- `screenshot-1.png`
- `screenshot-1-copy.png`

Output grouping surface:
- `high_confidence_groups[]`
  - `group_id: dupe-001`
  - `members: [screenshot-1.png, screenshot-1-copy.png]`
  - `confidence_band: high`
- `review_groups[]`
  - `group_id: review-014`
  - `members: [meme-original.png, meme-recompressed.jpg, meme-cropped.png]`
  - `confidence_band: borderline`
  - `review_required: true`

The point of the example is that the technique groups candidates and exposes uncertainty.
It does not delete files by itself.
