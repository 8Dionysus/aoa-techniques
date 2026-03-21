# External Origin Note

Use this note when a technique is adapted from an external open-source source.
It complements `TECHNIQUE.md` and records provenance, adaptation boundaries, and public-safety review.

## Source

- source_repo: `https://github.com/iagooar/qqqa`
- source_license: MIT
- inspired_by: not used in this import
- adapted_from: `qqqa`'s stateless shell model where `qq` stays read-only and `qa` performs at most one confirmed tool-using step per invocation

## What changed

- what_changed: narrowed the donor repository to one bounded pattern: mostly independent shell invocations with a clear split between read-only question mode and one confirmed tool-using action mode
- invariant core kept: stateless-by-default invocations, optional transient context, one-step agent behavior, and an explicit confirmation gate before mutating actions
- project-shaped details removed or generalized: provider/profile matrix, install flows, config format, optional history toggles, ANSI formatting, and product-specific integrations

## Public-safety review

- secrets or tokens removed: none from the donor surface used for this import
- private paths, URLs, or IDs removed: donor-specific local configuration paths and provider-specific environment assumptions were generalized away
- environment-specific assumptions generalized: OpenRouter, OpenAI, Codex CLI, Claude CLI, and other runtime choices were removed from the invariant core
- remaining public-safety concerns: future follow-on techniques should review optional history or provider-profile behavior separately rather than widening this fast-path contract

## Review notes

- why this adaptation is reusable here: many repositories need a small shell-side fast path that stays bounded and confirmation-gated before broader workflows or hidden multi-step loops begin
- limits or follow-up review concerns: this first import intentionally keeps only the single-shot invocation contract and excludes broader product behavior, provider routing, and optional continuity features
