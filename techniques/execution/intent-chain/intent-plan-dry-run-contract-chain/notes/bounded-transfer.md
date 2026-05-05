# Bounded Transfer

This note explains what transfers cleanly from the ATM10 origin and what should not be mistaken for the core of `AOA-T-0004`.

## What transfers cleanly

- a stable intent payload is normalized into a plan artifact before any execution layer runs
- the execution layer is dry-run only and emits explicit artifacts rather than relying on logs
- a contract-check reads those artifacts and produces a machine-readable verdict
- routing and traceability data can be surfaced in the contract summary when policy requires it
- the contract result is the stop signal that prevents premature progression to real execution

## What is not the core technique

- exact ATM10 script names such as `intent_to_automation_plan.py` or `automation_intent_chain_smoke.py`
- exact artifact names such as `automation_plan.json`, `chain_summary.json`, or `contract_summary.json`
- exact CI workflow layout, summary-table labels, or artifact-upload conventions
- exact thresholds such as minimum action count or minimum step count
- UI-automation specifics, keyboard actions, or other donor-specific payload shapes

## Minimum portability bar

A project can reasonably claim this technique only if all of the following hold:

- the plan artifact is written before dry-run execution
- the dry-run path is side-effect free in the same sense that the project documents and enforces
- the contract-check reads artifacts directly and returns an explicit pass or fail verdict
- routing expectations are checked explicitly instead of being inferred from human log review
- failing the contract blocks progression to any real execution path

## Misreadings to avoid

- adding an adapter with side effects is not this technique
- emitting logs without stable artifacts is not this technique
- carrying trace IDs without checking or publishing them when policy requires them is not this technique
- copying ATM10 filenames or commands without preserving the artifact-first contract misses the transferable core

## Source backing

The transfer boundary comes from the ATM10 sequence around `M6.3`, `M6.4`, `M6.6`, and the 2026-02-24 traceability hardening: the durable pattern is the artifact-first chain plus explicit contract verdict, not the donor repository's exact script or CI layout.
