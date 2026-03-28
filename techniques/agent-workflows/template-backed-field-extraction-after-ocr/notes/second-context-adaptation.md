# Second Context Adaptation

## Technique
- id: AOA-T-0071
- name: template-backed-field-extraction-after-ocr

## Target project
- name: aoa-techniques
- environment: public technique repository with authored bundle contracts, generated routing surfaces, and validator-backed markdown discipline
- runtime: documentation-first corpus that records the bounded post-OCR extraction pattern rather than shipping donor parser code, locale packs, or ingestion workflows

## What changed

- donor parser families were reduced to one portable post-OCR extraction contract rather than one invoice or receipt application stack
- locale-specific rules, parser implementations, and ingestion helpers were removed from the reusable public bundle
- OCR-stage ownership was kept out so the adaptation starts from one upstream OCR handoff instead of raw image processing
- the bundle was reduced to one technique doc, one checklist, one example, and four bounded evidence notes

## What stayed invariant

- OCR handoff remains the upstream input
- field targets remain explicit and bounded
- templates or heuristics remain reviewable aids rather than hidden parser law
- missing or conflicting values stay visible instead of being guessed away

## Risks introduced by adaptation

- the technique can collapse into an end-to-end parser if later users stop separating OCR staging from field extraction
- teams may over-associate the technique with one donor template family if interchangeable extraction rules are not kept explicit
- output can look cleaner than the underlying evidence if field-evidence references are dropped too early

## Evidence

- invoice2data's README shows structured extraction over OCR or PDF text through YAML or JSON templates and explicit output fields
- receiptparser's README shows configurable receipt extraction through YAML configuration and explicit structured values such as company, date, and amount
- receipt-parser-legacy's README frames the reusable core as extracting shop, date, and total from scanned receipts after OCR-derived text exists

## Result

- works as a documentation-first second context and preserves the bounded core without carrying over locale lock-in, donor parser code, or bookkeeping automation
