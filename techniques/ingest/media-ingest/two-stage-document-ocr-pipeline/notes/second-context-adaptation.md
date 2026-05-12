# Second Context Adaptation

## Technique
- id: AOA-T-0070
- name: two-stage-document-ocr-pipeline

## Target project
- name: aoa-techniques
- environment: public technique repository with authored bundle contracts, generated routing surfaces, and validator-backed markdown discipline
- runtime: documentation-first corpus that records the staged OCR handoff pattern rather than shipping donor OCR engines or packaging
- source: `https://github.com/JaidedAI/EasyOCR`
- license: Apache-2.0
- inspected commit: `363afb184047ce452e436f4224f3098422df872e`
- inspected surfaces: `README.md`, `easyocr/easyocr.py`, `custom_model.md`, `trainer/craft/README.md`, and `releasenotes.md`
- result: exact-fit public reinforcement beyond the PaddleOCR/docTR donor family

## What changed

- donor OCR frameworks were reduced to one portable staged handoff contract rather than one engine-specific implementation recipe
- deployment, serving, and benchmark details were removed from the reusable public bundle
- downstream extraction logic was kept out so the adaptation stops at OCR handoff rather than document-specific field semantics
- the bundle is kept to one technique doc, one checklist, one example, and bounded evidence notes
- the 2026-05-12 canonical review now records EasyOCR as live second-context reinforcement because its public API and implementation preserve region handles, recognized text, and confidence as an OCR result before downstream application logic

## What stayed invariant

- OCR is treated as at least two explicit stages: detect or layout, then recognize
- region or layout ambiguity remains visible enough for review
- low-confidence spans stay explicit
- downstream consumers receive one structured OCR handoff rather than hidden runtime internals

## Risks introduced by adaptation

- the technique can become vague if later users collapse detection, recognition, and extraction back into one step
- teams may over-associate the technique with one donor engine if the interchangeable handoff contract is not kept explicit
- too much normalization can hide layout ambiguity that later extraction needed
- OCR tool examples can tempt a bundle to absorb language packs, model serving, training, benchmark, or app-specific extraction details that belong outside this technique

## Evidence

- donor READMEs present OCR as a staged flow where detection or layout and recognition are separable concerns
- the same donor family makes OCR useful before any downstream document-specific logic is finalized
- this adaptation narrows those behaviors into one reusable public technique for confidence-aware OCR handoff
- EasyOCR repeats the same practical seam outside the donor family: detection produces horizontal and free-form region lists, recognition consumes those bounded regions, public results carry boxes plus text plus confidence, and simpler text-only output remains optional rather than the invariant handoff
- EasyOCR also keeps detection and recognition model concerns separately visible through CRAFT detection documentation, custom recognition documentation, public release notes for separate `detect` and `recognize` methods, and roadmap language around swappable detection and recognition algorithms

## Result

- works as a documentation-first second context and, after EasyOCR review, as cross-context reinforcement for canonical status without carrying over serving posture, packaging, language-model weights, benchmark claims, or donor-specific field logic
