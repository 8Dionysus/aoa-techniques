# Second Context Adaptation

## Technique
- id: AOA-T-0070
- name: two-stage-document-ocr-pipeline

## Target project
- name: aoa-techniques
- environment: public technique repository with authored bundle contracts, generated routing surfaces, and validator-backed markdown discipline
- runtime: documentation-first corpus that records the staged OCR handoff pattern rather than shipping donor OCR engines or packaging

## What changed

- donor OCR frameworks were reduced to one portable staged handoff contract rather than one engine-specific implementation recipe
- deployment, serving, and benchmark details were removed from the reusable public bundle
- downstream extraction logic was kept out so the adaptation stops at OCR handoff rather than document-specific field semantics
- the bundle was reduced to one technique doc, one checklist, one example, and four bounded evidence notes

## What stayed invariant

- OCR is treated as at least two explicit stages: detect or layout, then recognize
- region or layout ambiguity remains visible enough for review
- low-confidence spans stay explicit
- downstream consumers receive one structured OCR handoff rather than hidden runtime internals

## Risks introduced by adaptation

- the technique can become vague if later users collapse detection, recognition, and extraction back into one step
- teams may over-associate the technique with one donor engine if the interchangeable handoff contract is not kept explicit
- too much normalization can hide layout ambiguity that later extraction needed

## Evidence

- donor READMEs present OCR as a staged flow where detection or layout and recognition are separable concerns
- the same donor family makes OCR useful before any downstream document-specific logic is finalized
- this adaptation narrows those behaviors into one reusable public technique for confidence-aware OCR handoff

## Result

- works as a documentation-first second context and preserves the bounded core without carrying over serving posture, packaging, or donor-specific field logic
