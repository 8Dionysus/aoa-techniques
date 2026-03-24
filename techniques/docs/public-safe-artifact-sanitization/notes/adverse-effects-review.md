# Adverse Effects Review

## Technique

- id: AOA-T-0034
- name: public-safe-artifact-sanitization

## Review focus

- current role: canonical default for bounded sanitize-for-sharing work over technical artifacts that are useful but not safe to circulate raw
- current watch seam: keep the bundle centered on preparing a shareable artifact without widening into approval classification, incident response, public-release governance, or generic privacy tooling

## Failure modes

- teams over-sanitize until the artifact keeps almost none of the lesson it was meant to preserve
- reviewers treat a sanitized artifact as proof that the underlying action, system, or publication decision is approved
- canonical pressure widens the technique into full public-release policy, disclosure workflow, or incident-summary governance instead of bounded share-prep

## Negative effects

- a successful sanitization pass can create false confidence that all important context is still represented when key caveats were generalized away
- making this the default can encourage ritual sanitization even for already-safe material, adding friction without reducing real exposure
- a strong share-prep pattern can cause teams to postpone harder boundary questions by polishing the artifact instead of deciding whether it should be shared at all

## Misuse patterns

- using `AOA-T-0034` as a substitute for approval gating, dry-run planning, or safe infra-change technique selection
- treating generalized placeholders, pseudonyms, or doc-net replacements as if they automatically preserve the original lesson
- widening the technique into repo-release bootstrap, legal/privacy gatekeeping, or incident communication choreography

## Detection signals

- sanitized outputs read cleanly but reviewers still cannot say what was generalized, omitted, or left uncertain
- pull requests start debating publication policy or execution safety inside a share-prep artifact review
- artifacts keep losing the operational or technical lesson they were supposed to preserve after redaction
- teams cite the sanitized artifact itself as authorization instead of as a bounded sharing surface

## Mitigations

- require one short note about what changed, what remained approximate, and what lesson should still survive the sanitization pass
- route approval, publication, incident, and execution questions to their narrower sibling surfaces instead of letting them accumulate here
- prefer generalization that preserves structure and signal over blanket deletion when the lesson would otherwise disappear
- revisit canonical status if the bundle starts being used mainly for release governance, classification policy, or privacy-engineering programs rather than bounded share-prep

## Recommendation

- keep current `canonical` status and use this note as the watch surface for over-sanitization, false authorization, and public-release-governance creep
